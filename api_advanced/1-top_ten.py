import requests

def top_ten(subreddit):
    # Define the URL with the subreddit name
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    # Set up custom headers to mimic a browser request
    headers = {'User-Agent': 'Python:top_ten:v1.0 (by /u/your_username)'}
    
    try:
        # Make the GET request
        response = requests.get(url, headers=headers, params={'limit': 10}, allow_redirects=False)
        
        # Check if subreddit is invalid
        if response.status_code != 200:
            print(None)
            return
        
        # Parse JSON response
        data = response.json()
        posts = data.get('data', {}).get('children', [])
        
        # Print titles of the first 10 hot posts
        for post in posts:
            print(post.get('data', {}).get('title', None))
    except Exception as e:
        # Handle exceptions (e.g., connection errors)
        print(None)
