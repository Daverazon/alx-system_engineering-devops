#!/usr/bin/python3
"""
This script queries the Reddit API and returns a list containing the titles\
        of all hot topics for a give subreddit.
"""
import requests


def recurse(subreddit, hot_list=[], count=0, after=None):
    """
    Queries the Reddit API and generates a list containing the titles of all \
            hot topics for a given subreddit.

    Arguments:
        subreddit (str): The given subreddit
        hot_list (list): list of hot topic titles
        count (int): Number of topics already seen in the hot section
        after (str): unique identifier to next set of topics

    Returns:
        the list of hot topic titles
        None if not a valid subreddit
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {
            'User-Agent': '2-recurse:1.0 by daverazon'
            }
    params = {
            'limit': 100, 'count': count, 'after': after
            }

    response = requests.get(
            url, headers=headers, params=params, allow_redirects=False
            )

    if response.status_code == 200:
        count += 100
        result = response.json()
        after = result.get('data').get('after')
        posts_list = result.get('data').get('children')
        hot_list.extend(
                [data.get('data').get('title') for data in posts_list]
                )
        if after is None:
            print(hot_list)
            return hot_list
        else:
            return recurse(subreddit, hot_list, count, after)
    return None
