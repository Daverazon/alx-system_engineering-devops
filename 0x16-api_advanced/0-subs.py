#!/usr/bin/python3
"""This script queries the Reddit and returns a given subreddit's
    subscriber number"""
import requests


def number_of_subscribers(subreddit):
    '''
    Queries the Reddit API and return the number of subscribers
        (not active users, total subscribers) for a given subreddit

    Args:
        subreddit(str): The subreddit

    Returns:
        int: number of subscribers for the given subreddit
                0 if subreddit is invalid
    '''

    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': '0-subs:1.0 by daverazon'}
    # Add user agent to prevent rate limiting
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        return response.json()['data']['subscribers']
    elif response.status_code == 404:
        # 404 is status code for not found
        return 0
