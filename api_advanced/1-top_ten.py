#!/usr/bin/python3
"""Prints the title of the first 10 hot posts listed for a given subreddit"""
import requests

def top_ten(subreddit):
    """Main function"""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {"User-Agent": "PostmanRuntime/7.35.0"}

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        response.raise_for_status()  # Raises an HTTPError for bad responses (4XX, 5XX)

        data = response.json()
        hot_posts = data.get("data", {}).get("children", [])

        for post in hot_posts:
            title = post.get('data', {}).get('title')
            if title:  # Check if title exists
                print(title)

    except requests.exceptions.RequestException:
        print(None)

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        top_ten(sys.argv[1])
