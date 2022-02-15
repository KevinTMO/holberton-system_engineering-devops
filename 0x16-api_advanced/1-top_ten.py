#!/usr/bin/python3
"""
Module: 1-top_ten

Instructions:

Request the json data a RedditAPI and prints the first 10 hot posts listed for
a given subreddit

"""


from requests import get


reddit = 'https://www.reddit.com/r/'


def top_ten(subreddit):
    """
    Return the numbers of subscribers of a given subreddit
    """
    url = reddit + subreddit + '/.json?limit=10'

    # print(url) -> for debugging purposes

    headers = {
        'user-agent': 'myUsr'
    }

    response = get(url, headers=headers)

    # print(response.json()) -> for debuggin purposes
    # print(response.json().get('data').get('children')) -> for debug purposes

    if response.status_code == 200:
        childs = response.json().get('data').get('children')

        for dt in childs:
            dt = dt.get('data').get('title')
            print(dt)
    else:
        print('None')
