#!/usr/bin/python3
"""
Write a function that queries the Reddit API and returns the number of
subscribers (not active users, total subscribers) for a given subreddit.
If an invalid subreddit is given, the function should return 0.
"""
import requests


def number_of_subscribers(subreddit):
    """ returns the number of subscribers """
    try:
        url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
        uname = {'User-Agent': 'Trollolol'}
        req = requests.get(url, headers=uname)
        req_json = req.json().get('data').get('subscribers')
        return (req_json)

    except BaseException:
        return(0)
