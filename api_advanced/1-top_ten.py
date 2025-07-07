#!/usr/bin/python3
"""
Script that fetches 10 hot posts for a given subreddit.
It prints the titles of the first 10 hot posts listed for a given subreddit.
If the subreddit is invalid or no posts are found, it prints None.
"""

import requests

def top_ten(subreddit):
    """
    Prints the titles of the first 10 hot posts for a given subreddit.
    If the subreddit is invalid or no posts are found, it prints None.
    """
    headers = {'User-Agent': 'MyAPI/0.0.1'}
    subreddit_url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"

    try:
        response = requests.get(subreddit_url, headers=headers, allow_redirects=False)
        if response.status_code == 200:
            json_data = response.json()
            posts = json_data.get('data', {}).get('children', [])

            if not posts:
                print(None)
                return

            for post in posts[:10]:
                print(post.get('data', {}).get('title'))
        else:
            print(None)
    except requests.exceptions.RequestException:
        print(None)

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        top_ten(sys.argv[1])
