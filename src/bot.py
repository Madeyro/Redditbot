''' Reddit bot

@Author Maros Kopec maroskopec@outlook.com
@Description
The requirements for this file are:

1   A function `anonymous` with no arguments, which returns a `praw.Reddit`
    instance that has a Useragent but is otherwise anonymous / unauthenticated.
    This will be used in bots that need to make requests but don't need any
    permissions.

2   A function `login` with optional parameter `r`, which returns an
    authenticated Reddit instance.
    If `r` is provided, authenticate it.
    If not, create one using `anonymous` and authenticate that.
    Either way, return the instance when finished.
'''

import os
import praw


USERAGENT = os.environ.get('RBOT_AGENT')
CLIENT_ID = os.environ.get('RBOT_CLIENT')
CLIENT_SECRET = os.environ.get('RBOT_SECRET')
USERNAME = os.environ.get('RBOT_USER')
PASSWORD = os.environ.get('RBOT_PASS')


def login(r=None):
    new_r = praw.Reddit(
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        password=PASSWORD,
        user_agent=USERAGENT,
        username=USERNAME
    )
    if r:
        r.__dict__.clear()
        r.__dict__.update(new_r.__dict__)
    return new_r
