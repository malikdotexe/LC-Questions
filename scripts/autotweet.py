#!/usr/bin/env python3
import os
import subprocess
import requests
import tweepy
import textwrap
import urllib.parse
from pathlib import Path


# =============================================ð========
# 1️⃣  TWITTER AUTH SETUP
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

auth = tweepy.OAuth1UserHandler(
    os.getenv("TWITTER_API_KEY"),
    os.getenv("TWITTER_API_SECRET"),
    os.getenv("TWITTER_ACCESS_TOKEN"),
    os.getenv("TWITTER_ACCESS_SECRET"),
)
api = tweepy.API(auth, wait_on_rate_limit=True)
try:
    api.verify_credentials()
except Exception as e:
    raise RuntimeError("❌ Twitter authentication failed.") from e


# =====================================================
# 2️⃣  FOLDER + FILE DETECTION
# =====================================================
def get_latest_folder(base="."):
    excluded_dirs = {".git", ".github", "scripts", "images"}

    # Try git-based detection first
    try:
        result = subprocess.run(
            ["git", "log", "-1", "--pretty=format:", "--name-only", "--", "*.py"],
            cwd=base,
            capture_output=True,
            text=True,
            check=True,
        )
        files = [line.strip() for line in result.stdout.splitlines() if line.strip().endswith(".py")]

        if files:
            latest_file = Path(files[-1])
            for parent in latest_file.parents:
                if parent.name not in excluded_dirs and parent != Path(base):
                    print(f"🕒 Latest committed file: {latest_file} in {parent.name}")
                    return parent
        else:
            print("⚠️ Git log did not return any .py files; falling back to modification time.")
    except Exception as e:
        print(f"⚠️ Git-based detection failed: {e}. Falling back to file timestamps.")

    # Fallback: filesystem-based detection
    folders = [
        f for f in Path(base).iterdir()
        if f.is_dir() and f.name not in excluded_dirs
    ]
    py_files = [f for folder in folders for f in folder.glob("*.py")]

    if not py_files:
        raise FileNotFoundError("No Python files found in any folder.")

    latest_file = max(py_files, key=lambda f: f.stat().st_mtime)
    print(f"🕒 Fallback to latest modified file: {latest_file}")
    return latest_file.parent

# =====================================================
# 3️⃣  TWEET GENERATION VIA POLLINATIONS
# =====================================================
def generate_tweet(problem_title):
    prompt = textwrap.dedent(f"""
    Write a short, engaging tweet about solving the LeetCode problem "{problem_title}".
    Follow this structure and tone:
    🧠 Solved the Next Permutation problem! ✨  
    📍 Approach: Identify pivot → swap with next greater → reverse suffix  
    💡 Key Idea: Traverse from right, apply in-place changes for O(n) time and O(1) space  
        
    Your task:
    - Replace the title, summary line, and steps with the correct logic for "{problem_title}".
    - Explain the approach in 2–3 concise bullet-style lines.
    - Mention time and space complexity naturally within the description.
    - Keep it under 280 characters.
    - Maintain an informative, confident tone — not too flashy, not verbose.
    """)

    encoded_prompt = urllib.parse.quote(prompt)
    url = f"https://text.pollinations.ai/{encoded_prompt}"
    
    try:
        resp = requests.get(url, timeout=20)
        if resp.status_code != 200:
            raise RuntimeError(f"Pollinations API returned {resp.status_code}")
        tweet = resp.text.strip()
        if not tweet:
            raise ValueError("Empty response from Pollinations API.")
    except Exception as e:
        print(f"⚠️ Pollinations API failed: {e}")
        tweet = f"✅ Solved {problem_title}! Another step forward in #LeetCode #DSA #Python 🚀"
    
    # Append static hashtags (ensure no duplicates and keep within 280 chars)
    static_tags = " #LeetCode #DSA #Algorithms #Python #100DaysOfCode #InterviewPrep"
    
    # Avoid double-hashtag repetition if they already exist in the text
    for tag in static_tags.split():
        if tag not in tweet:
            tweet += f" {tag}"
    
    # Ensure tweet is within 280 chars
    tweet = tweet[:280]
    return tweet


# =====================================================
# 4️⃣  CARBON IMAGE GENERATION
# =====================================================
def generate_carbon_image(code_path, output_dir="./images"):
    os.makedirs(output_dir, exist_ok=True)

    # Check if carbon-now CLI exists
    if subprocess.run(["which", "carbon-now"], capture_output=True).returncode != 0:
        print("⚠️ carbon-now not found; skipping image generation.")
        return None

    subprocess.run([
    "carbon-now",
    str(code_path),
    "--theme", "nord",
    "--headless",
    "--save",
    "--output", str(Path(output_dir).resolve())
    ], check=True)


    files = list(Path(output_dir).glob("*.png")) or list(Path(".").glob("*.png"))

    if not files:
        raise FileNotFoundError("No carbon image generated.")
    return max(files, key=lambda p: p.stat().st_mtime)


# =====================================================
# 5️⃣  TWEET POSTING
# =====================================================
def post_tweet_with_image(text, image_path=None):
    client = tweepy.Client(
        consumer_key=os.getenv("TWITTER_API_KEY"),
        consumer_secret=os.getenv("TWITTER_API_SECRET"),
        access_token=os.getenv("TWITTER_ACCESS_TOKEN"),
        access_token_secret=os.getenv("TWITTER_ACCESS_SECRET"),
    )

    if image_path:
        # upload still needs v1.1 API
        media = api.media_upload(image_path)
        client.create_tweet(text=text, media_ids=[media.media_id])
    else:
        client.create_tweet(text=text)

    print(f"✅ Tweet posted successfully via v2 API")


# =====================================================
# 6️⃣  MAIN EXECUTION
# =====================================================
if __name__ == "__main__":
    latest = get_latest_folder(".")
    print(f"📁 Latest folder: {latest}")

    py_files = list(latest.glob("*.py"))
    if not py_files:
        raise FileNotFoundError("No Python solution found in the latest folder.")

    code_file = py_files[0]

    # Extract proper title (ignore leading number)
    slug = "-".join(latest.name.split("-")[1:])
    problem_name = slug.replace("-", " ").title()
    print(f"🧠 Problem detected: {problem_name}")

    tweet_text = generate_tweet(problem_name)
    print(f"💬 Generated tweet:\n{tweet_text}")

    try:
        image = generate_carbon_image(code_file)
        print(f"🖼️ Generated image: {image}")
    except Exception as e:
        print(f"⚠️ Image generation skipped: {e}")
        image = None

    post_tweet_with_image(tweet_text, image and str(image))
