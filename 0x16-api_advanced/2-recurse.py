#!/usr/bin/python3
"""
Module: 2-recurse

Instructions:

Request the json data a RedditAPI and return a lists containing
the titles of all hot articles for a given subreddit.

Should use: recursive

"""


from requests import get


reddit = 'https://www.reddit.com/r/'


def recurse(subreddit, hot_list=[], after=None, count=0):
    """
    Return the numbers of subscribers of a given subreddit
    """
    url = reddit + subreddit + '/hot.json'

    # print(url) -> for debugging purposes

    headers = {
        'user-agent': 'myUsr'
    }

    params = {
        'after': after,
        'count': count
        # 'limit': 10
    }

    response = get(url, allow_redirects=False, headers=headers, params=params)

    # print(response.json()) -> for debuggin purposes
    # print(response.json().get('data').get('children')) -> for debug purposes

    if response.status_code == 200:
        responseData = response.json().get('data')
        after = responseData.get('after')
        count += responseData.get('dist')

        for dt in responseData.get('children'):
            hot_list.append(dt.get('data').get('title'))
            # print(hot_list) -> for debugging purporses

        if after is not None:
            return recurse(subreddit, hot_list, after, count)

        return hot_list

    else:
        return None
