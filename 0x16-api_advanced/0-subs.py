#!/usr/bin/python3
"""
This module contains the function number_of_subscribers.
"""
import requests


def number_of_subscribers(subreddit):
    """Returns the number of subscribers for a given reddit"""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 \
        (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0"

    result = requests.get(
        url, headers={"user-agent": user_agent}, allow_redirects=False
    )
    if result.status_code == 200:
        jsonresult = result.json()
        return jsonresult["data"]["subscribers"]
    else:
        return 0
