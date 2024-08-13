#!/usr/bin/python3
import requests


def number_of_subscribers(subreddit):
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {
        'User-Agent': 'subreddit-subscriber-checker/0.1 by your_username'
    }

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code == 200:
            data = response.json()
            return data['data']['subscribers']
        else:
            return 0
    except requests.RequestException:
        return 0


# Example usage
subreddit = "python"
subscribers = number_of_subscribers(subreddit)
print(f"The subreddit r/{subreddit} has {subscribers} subscribers.")
