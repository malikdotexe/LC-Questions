#!/usr/bin/env python3
import os
import subprocess
import requests
import tweepy
import textwrap
import urllib.parse
from pathlib import Path

# =====================================================
# 1️⃣  TWITTER AUTH (v1.1 + v2 HYBRID)
# =====================================================
required_env = [
    "TWITTER_API_KEY",
    "TWITTER_API_SECRET",
    "TWITTER_ACCESS_TOKEN",
    "TWITTER_ACCESS_SECRET",
]

missing = [k for k in required_env if not os.getenv(k)]
if missing:
    raise EnvironmentError(f"Missing Twitter credentials: {', '.join(missing)}")

# v1.1 (for media upload)
auth = tweepy.OAuth1UserHandler(
    os.getenv("TWITTER_API_KEY"),
    os.getenv("TWITTER_API_SECRET"),
    os.getenv("TWITTER_ACCESS_TOKEN"),
    os.getenv("TWITTER_ACCESS_SECRET"),
)
api = tweepy.API(auth, wait_on_rate_limit=True)

# v2 (for tweeting)
client = tweepy.Client(
    consumer_key=os.getenv("TWITTER_API_KEY"),
    consumer_secret=os.getenv("TWITTER_API_SECRET"),
    access_token=os.getenv("TWITTER_ACCESS_TOKEN"),
    access_token_secret=os.getenv("TWITTER_ACCESS_SECRET"),
)

try:
    api.verify_credentials()
    print("✅ Twitter authentication successful.")
except Exception as e:
    raise RuntimeError("❌ Twitter authentication failed.") from e


# =====================================================
# 2️⃣  DETECT LATEST COMMITTED FOLDER
# =====================================================
def get_latest_folder(base="."):
    excluded_dirs = {".git", ".github", "scripts", "images"}

    try:
        # Get list of .py files modified in the latest commit
        result = subprocess.run(
            ["git", "diff-tree", "--no-commit-id", "--name-only", "-r", "HEAD"],
            cwd=base,
            capture_output=True,
            text=True,
            check=True,
        )
        changed_files = [line.strip() for line in result.stdout.splitlines()]
        py_files = [
            f for f in changed_files
            if f.endswith(".py") and not f.startswith(("scripts/", ".github/"))
        ]

        if not py_files:
            print("🟡 No new Python solution detected in the latest commit. Skipping tweet.")
            exit(0)

        latest_file = Path(py_files[-1])
        for parent in latest_file.parents:
            if parent.name not in excluded_dirs and parent != Path(base):
                print(f"🕒 Latest committed file: {latest_file} in {parent.name}")
                return parent

        raise FileNotFoundError("No valid problem folder found for latest .py commit.")
    except Exception as e:
        raise RuntimeError(f"Git detection failed: {e}")


# =====================================================
# 3️⃣  GENERATE TWEET USING POLLINATIONS.AI
# =====================================================
def generate_tweet(problem_title, code_path):
    with open(code_path, "r") as f:
        code_content = f.read().strip()

    prompt = textwrap.dedent(f"""
    You are a concise technical writer.
    Write a tweet describing the LeetCode problem "{problem_title}" based on the solution code below.

    Code:
    ```
    {code_content}
    ```

    Requirements:
    - 1 line intro with the problem name
    - 2–3 concise lines summarizing the approach used in THIS code
    - Mention time and space complexity if clear
    - Confident, helpful tone
    - Use Emojis so that it looks pretty to the eyes
    - Under 250 characters

    Example:
    🧠 Solved the Two Sum problem!
    📍 Approach: Hashmap to store complements
    💡 O(n) time, O(n) space for quick lookups
    """)

    encoded_prompt = urllib.parse.quote(prompt)
    url = f"https://text.pollinations.ai/{encoded_prompt}"

    try:
        resp = requests.get(url, timeout=15)
        tweet = resp.text.strip()
    except Exception as e:
        print(f"⚠️ Pollinations request failed: {e}")
        tweet = ""

    if not tweet:
        tweet = f"✅ Solved {problem_title}! Another step forward in #LeetCode #DSA #Python 🚀"

    # Add static hashtags, prevent duplicates
    static_tags = " #LeetCode #100DaysOfCode"
    for tag in static_tags.split():
        if tag not in tweet:
            tweet += f" {tag}"
    
    # Ensure final tweet <= 280 chars without cutting hashtags
    max_len = 260
    hashtags = " ".join([tag for tag in static_tags.split() if tag in tweet])
    # Reserve space for hashtags plus a space
    allowed_len = max_len - len(hashtags) - 1
    
    # Truncate only the main tweet text, not the hashtags
    if len(tweet) > max_len:
        # Isolate main text by removing hashtags
        main_text = tweet.replace(hashtags, "").rstrip()
        main_text = main_text[:allowed_len].rstrip()
        tweet = f"{main_text} {hashtags}"
    
    return tweet



# =====================================================
# 4️⃣  GENERATE CARBON IMAGE
# =====================================================
def generate_carbon_image(code_path, output_dir="./images"):
    os.makedirs(output_dir, exist_ok=True)

    if subprocess.run(["which", "carbon-now"], capture_output=True).returncode != 0:
        print("⚠️ carbon-now not found; skipping image generation.")
        return None

    subprocess.run([
    "carbon-now", str(code_path),
    "--theme", "cobalt",
    "--headless",
    "--save",
    "--bg", "#07DDDD",
    "--output", str(Path(output_dir).resolve())
    ], check=True)

    # ✅ search both in output_dir and repo root (fallback)
    files = list(Path(output_dir).glob("*.png")) + list(Path(".").glob("*.png"))

    if not files:
        raise FileNotFoundError("No carbon image generated.")

    latest_image = max(files, key=lambda p: p.stat().st_mtime)
    print(f"🖼️ Found generated image: {latest_image}")
    return latest_image



# =====================================================
# 5️⃣  POST TWEET (v2 for posting, v1.1 for media)
# =====================================================
TWEET_LOG = Path("scripts/tweeted_problems.txt")
TWEET_LOG.touch(exist_ok=True)

def already_tweeted(problem_name):
    with open(TWEET_LOG, "r") as f:
        return problem_name in f.read().splitlines()

def mark_tweeted(problem_name):
    with open(TWEET_LOG, "a") as f:
        f.write(problem_name + "\n")
        
def post_tweet_with_image(text, image_path=None):
    if not text:
        raise ValueError("Tweet text is missing or empty.")

    try:
        if image_path:
            # Upload media via v1.1
            media = api.media_upload(image_path)
            media_id = media.media_id
            print(f"🖼️ Uploaded media ID: {media_id}")

            # Post tweet via v2
            client.create_tweet(text=text, media_ids=[media_id])
            print("✅ Tweet posted successfully with image (v2 endpoint).")
        else:
            client.create_tweet(text=text)
            print("✅ Tweet posted successfully (text only, v2 endpoint).")

    except tweepy.errors.Forbidden as e:
        try:
            print("resp:", e.response.text)   # full JSON error from X
        except Exception:
            pass
        print("codes:", getattr(e, "api_codes", None))
        raise


# =====================================================
# 6️⃣  MAIN EXECUTION
# =====================================================
if __name__ == "__main__":
    latest = get_latest_folder(".")
    print(f"📁 Latest folder: {latest}")

    py_files = list(latest.glob("*.py"))
    if not py_files:
        print("⚠️ No Python solution found in this folder. Exiting.")
        exit(0)


    code_file = py_files[0]
    slug = "-".join(latest.name.split("-")[1:])
    problem_name = slug.replace("-", " ").title()
    print(f"🧠 Problem detected: {problem_name}")


    tweet_text = generate_tweet(problem_name, code_file)
    print(f"💬 Generated tweet:\n{tweet_text}")

    try:
        image = generate_carbon_image(code_file)
        print(f"🖼️ Generated image: {image}")
    except Exception as e:
        print(f"⚠️ Image generation skipped: {e}")
        image = None

    post_tweet_with_image(tweet_text, str(image) if image else None)
    mark_tweeted(problem_name)

