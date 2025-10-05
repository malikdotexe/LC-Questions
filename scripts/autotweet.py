import os
import subprocess
import requests
import tweepy
from pathlib import Path

# Twitter API Auth
auth = tweepy.OAuth1UserHandler(
    os.getenv("TWITTER_API_KEY"),
    os.getenv("TWITTER_API_SECRET"),
    os.getenv("TWITTER_ACCESS_TOKEN"),
    os.getenv("TWITTER_ACCESS_SECRET"),
)
api = tweepy.API(auth)

def get_latest_folder(base="."):
    excluded_dirs = {".git", ".github", "scripts", "images"}

    folders = [
        f for f in Path(base).iterdir()
        if f.is_dir() and f.name not in excluded_dirs
    ]

    # Keep only folders that have at least one Python solution
    folders = [f for f in folders if any(f.glob("*.py"))]

    if not folders:
        raise FileNotFoundError("No valid problem folder with a .py file found.")

    latest = max(folders, key=lambda p: p.stat().st_mtime)
    return latest


def generate_tweet(problem_title):
    prompt = textwrap.dedent(f"""
    Write a concise, enthusiastic tweet about solving the LeetCode problem "{problem_title}".
    Format it exactly like this example:

    🧠 Cracked the Next Permutation algorithm! ✨ In-place solution with O(n) complexity  
    📍 Find pivot → Swap with successor → Reverse suffix  
    🔗 leetcode.com/problems/next-permutation  
    👨‍💻 #LeetCode #DSA #Algorithms #Python  

    Your task:
    - Replace the title, summary line, and use hashtags as they are.
    - Mention time complexity and key idea in 1–2 bullet-style lines.
    - Keep it under 280 characters.
    - Do NOT include explanations or extra commentary.
    """)    
    url = f"https://text.pollinations.ai/{prompt}"
    tweet = requests.get(url).text.strip()
    return tweet[:280]

def generate_carbon_image(code_path, output_dir="./images"):
    os.makedirs(output_dir, exist_ok=True)
    subprocess.run([
        "carbon-now",
        str(code_path),
        "--theme", "nord",
        "--headless",
        "--save",
        "--output", output_dir
    ], check=True)
    # Return latest generated file
    files = list(Path(output_dir).glob("carbon-*.png"))
    return max(files, key=lambda p: p.stat().st_mtime)

def post_tweet_with_image(text, image_path):
    api.update_status_with_media(status=text, filename=image_path)
    print(f"✅ Tweet posted: {text[:50]}...")

if __name__ == "__main__":
    latest = get_latest_folder(".")
    print(f"📁 Latest folder: {latest}")

    # detect solution file (e.g., pascals-triangle.py)
    py_files = list(latest.glob("*.py"))
    if not py_files:
        raise FileNotFoundError("No Python solution found.")

    code_file = py_files[0]
    problem_name = latest.name.split("-")[-1].replace("-", " ").title()

    print(f"🧠 Problem: {problem_name}")
    tweet_text = generate_tweet(problem_name)
    print(f"💬 Generated tweet:\n{tweet_text}")

    image = generate_carbon_image(code_file)
    print(f"🖼️ Generated image: {image}")

    post_tweet_with_image(tweet_text, str(image))
