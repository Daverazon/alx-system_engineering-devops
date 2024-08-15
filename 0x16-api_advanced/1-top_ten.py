#!/usr/bin/python3
"""
Prints the titles of the first 10 hot posts listed for a given subreddit
"""
import requests


def top_ten(subreddit):
    """
    Queries the Reddit API and prints the titles of the first
    10 hot posts listed for a given subreddit

    Arguments:
        subreddit (str): The given subreddit
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    params = {
            'limit': 10
            }
    headers = {
            'User-Agent': '1-top_ten:1.0 by daverazon'
            }
    response = requests.get(
            url, params=params, headers=headers, allow_redirects=False
            )
    if response.status_code == 404:
        print("None")

    posts_list = response.json()['data']['children']
    for data in posts_list:
        print(data['data']['title'])
