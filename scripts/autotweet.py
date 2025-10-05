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

    folders = [
        f for f in Path(base).iterdir()
        if f.is_dir() and f.name not in excluded_dirs
    ]
    # Keep only folders containing at least one Python file
    folders = [f for f in folders if any(f.glob("*.py"))]

    if not folders:
        raise FileNotFoundError("No valid problem folder with a .py file found.")

    # Sort by modification time, then by name as tiebreaker
    return max(folders, key=lambda p: (p.stat().st_mtime, p.name))


# =====================================================
# 3️⃣  TWEET GENERATION VIA POLLINATIONS
# =====================================================
def generate_tweet(problem_title):
    prompt = textwrap.dedent(f"""
    Write a concise, enthusiastic tweet about solving the LeetCode problem "{problem_title}".
    Format it exactly like this example:

    🧠 Cracked the Next Permutation algorithm! ✨ In-place solution with O(n) complexity  
    📍 Find pivot → Swap with successor → Reverse suffix    
    👨‍💻 #LeetCode #DSA #Algorithms #Python  

    Your task:
    - Replace the title, summary line, and use hashtags as they are.
    - Mention time complexity, space complexity and key idea in 2-3 bullet-style lines.
    - Keep it under 280 characters.
    - Do NOT include explanations or extra commentary.
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

    if len(tweet) > 280:
        tweet = tweet[:277] + "..."
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

    print(f"✅ Tweet posted successfully via v2 API: {text[:70]}...")


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
