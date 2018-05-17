#!/usr/bin/python3

import praw
from src.bot import login

reddit = login()
print(reddit.user.me())
