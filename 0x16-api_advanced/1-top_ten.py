#!/usr/bin/python3
"""
Write a function that queries the Reddit API and prints the titles
of the first 10 hot posts listed for a given subreddit.
"""
import requests


def top_ten(subreddit):
    """
       prints the titles of the first 10 hot posts listed for a given subreddit
    """
    try:
        url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
        uname = {'User-Agent': 'Trollolol'}
        req = requests.get(url, headers=uname, params={'limit': 10})
        top = req.json().get('data').get('children')
        for i in top:
            print(i.get('data').get('title'))
    except:
        print(None)
