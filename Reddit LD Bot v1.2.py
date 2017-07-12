import re
import praw
import config

bot = praw.Reddit(user_agent='LDbot v1.0',
                  client_id=config.client_id,
                  client_secret=config.client_secret,
                  username=config.username,
                  password=config.password)
with open('posts_replied_to') as f:
    for i, l in enumerate(f):
        number_of_lines = i + 2

reply = "Lucid Dreaming means you are aware that you are dreaming. This can mean with or without control. Use " \
        "this information to make your decision. This is a bot. Please contact /u/dude0413 for bugs or" \
        " suggestions. First bot version v0.1. Has replied to: " + str(number_of_lines) + ' posts.'

with open('posts_replied_to', 'r') as f:
    posts_replied_to = f.read()
    posts_replied_to = posts_replied_to.split('\n')
    posts_replied_to = list(filter(None, posts_replied_to))

subreddit = bot.subreddit('LucidDreaming')
for submission in subreddit.new(limit=10):
    id_of_post = submission.id
    title_of_post = submission.title
    author_of_post = submission.author

    post_names = ['was this a lucid dream?', 'Was this a LD?', 'Was this a Lucid Dream?', 'lucid dream']
    post_names_length = len(post_names) - 1
    x = 0
    while x < post_names_length:
        x += 1
        if id_of_post not in posts_replied_to:
            if re.search(post_names[x], title_of_post, re.IGNORECASE):
                submission.reply(reply)
                print('Bot replying to : "', title_of_post + '"' + ' by: "' + str(author_of_post) + '"')
                posts_replied_to.append(id_of_post)

with open("posts_replied_to", "w") as f:
    for post_id in posts_replied_to:
        f.write(post_id + "\n")
