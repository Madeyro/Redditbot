from src.bot import login
import json

# Read subreddits from file
with open('subreddits.json', 'r') as file:
    file_data = json.load(file)

print(file_data['subreddits'])
reddit = login()
print(reddit.user.me())
