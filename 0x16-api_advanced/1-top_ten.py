#!/usr/bin/python3
"""
This module contains the function top_ten.
"""

import requests


def top_ten(subreddit):
    """
    Queries Reddit API & prints titles of the first 10 hot posts
    listed for a given subreddit.
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {
        "User-Agent": "Linux 0x16 api advanced:v1.0.0 (by /u/nazaVivian)"
    }
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        try:
            data = response.json()
            posts = data["data"]["children"]
            for post in posts:
                print(post["data"]["title"])
        except (KeyError, ValueError):
            print(None)
    else:
        print(None)
