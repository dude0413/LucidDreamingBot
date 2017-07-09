import praw
import config
import re


bot = praw.Reddit(user_agent='LDbot v0.1',
                  client_id=config.client_id,
                  client_secret=config.client_secret,
                  username=config.username,
                  password=config.password)

reply = "Lucid Dreaming means you are aware that you are dreaming. This can mean with or without control. Use " \
        "this information to make your decision. This is a bot. Please contact /u/dude0413 for bugs or" \
        " suggestions. First bot version v0.1"

with open('posts_replied_to', 'r') as f:
    posts_replied_to = f.read()
    posts_replied_to = posts_replied_to.split('\n')
    posts_replied_to = list(filter(None, posts_replied_to))

subreddit = bot.subreddit('LucidDreaming')
for submission in subreddit.hot(limit=5):
    if submission.id not in posts_replied_to:
        if re.search("was this a lucid dream?", submission.title, re.IGNORECASE):
            submission.reply(reply)
            print("Bot replying to : ", submission.title)
            posts_replied_to.append(submission.id)
    if submission.id not in posts_replied_to:
        if re.search("Was this a LD?", submission.title, re.IGNORECASE):
            submission.reply(reply)
            print("Bot replying to: ", submission.title)
            posts_replied_to.append(submission.id)
    if submission.id not in posts_replied_to:
        if re.search("Was this a Lucid Dream?", submission.title, re.IGNORECASE):
            submission.reply(reply)
            print("Bot replying to: ", submission.title)
            posts_replied_to.append(submission.id)
    if submission.id not in posts_replied_to:
        if re.search("Lucid Dream?", submission.title, re.IGNORECASE):
            submission.reply(reply)
            print("Bot replying to: ", submission.title)
            posts_replied_to.append(submission.id)
with open("posts_replied_to", "w") as f:
    for post_id in posts_replied_to:
        f.write(post_id + "\n")
