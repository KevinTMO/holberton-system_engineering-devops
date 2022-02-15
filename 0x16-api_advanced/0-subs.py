#!/usr/bin/python3
"""
Module: 0-subs

Instructions:

Request the json data of all subscribers from a given subreddit

"""


from requests import get


reddit = 'https://www.reddit.com/r/'

def number_of_subscribers(subreddit):
    """
    Return the numbers of subscribers of a given subreddit
    """
    url = reddit + subreddit + '/about.json'

    # print(url) -> for debugging purposes

    headers = {
        'user-agent': 'myUsr'
    }

    response = get(url, allow_redirects=False, headers=headers)

    # print(response.json()) -> for debuggin purposes

    if response.status_code == 200:
        return response.json().get('data').get('subscribers')
    else:
        return 0
