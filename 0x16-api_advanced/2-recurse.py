#!/usr/bin/python3
"""
Write a recursive function that queries the Reddit API and returns a list
containing the titles of all hot articles for a given subreddit. If no results
are found for the given subreddit, the function should return None.
"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """
       returns a list containing the titles of all hot
       articles for a given subreddit
    """
    try:
        url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
        uname = {'User-Agent': 'Trollolol'}
        req = requests.get(url, headers=uname, params={'after': after})
        top = req.json().get('data').get('children')
        afters = req.json()['data'].get('after')
        for i in top:
            hot_list.append(i['data'].get('title'))
        if afters is not None:
            recurse(subreddit, hot_list, afters)
        return hot_list
    except:
        return None
