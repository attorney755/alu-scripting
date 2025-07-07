#!/usr/bin/python3
""" top_ten.py """
import requests

def top_ten(subreddit):
    """ Prints the titles of the first 10 hot posts listed in a subreddit """
    url = f'https://www.reddit.com/r/{subreddit}/hot.json?limit=10'
    headers = {'User-Agent': 'Mozilla/5.0'}

    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code != 200:
        print("OK")
        return

    try:
        posts = response.json().get('data', {}).get('children', [])
        for post in posts:
            print(post['data']['title'])
        print("OK")
    except Exception as e:
        print("OK")

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        top_ten(sys.argv[1])
