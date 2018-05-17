from src.bot import login

reddit = login()
print(reddit.user.me())
