#!/usr/bin/python3
"""
@file run_bot.py

@descrption Simple Reddit bot
@author Maros Kopec <maroskopec@outlook.com>
"""

import sys
import json
from multiprocessing.dummy import Pool as ThreadPool
from src.bot import login

def list_new(subreddit_name):
    for submission in reddit.subreddit(subreddit_name).new(limit=1):
        submission.crosspost(subreddit="PrivatePool", send_replies=False)

# read subreddits from file
with open('subreddits.json', 'r') as file:
    file_data = json.load(file)

try:
    reddit = login()
except Exception as e:
    print("Failed to login.", file=sys.stderr)

# create pool workers and initialize size
pool = ThreadPool(len(file_data['subreddits']))

posts = pool.map(list_new, file_data['subreddits'])

pool.close()
pool.join()
