import re, praw, config
version = 'v1.6'
# Common subreddits #
LD = 'LucidDreaming'
CBT = 'Cool_Bot_Testing'
# Login into the bot #
bot = praw.Reddit(user_agent='LDbot v1.0',
                  client_id=config.client_id,
                  client_secret=config.client_secret,
                  username=config.username,
                  password=config.password)
# Gets the number of posts that the bot has replied to #
with open('posts_replied_to') as r:
    for i, l in enumerate(r):
        number_of_post_replies = i + 2
        str_number_of_post_replies = str(number_of_post_replies)
# Get the number of lines of the replies and look for. Also numbers the segments of the post replies #
with open('replies_to_reply', 'r') as c:
    for i, l in enumerate(c):
        number_of_lines_for_post_replies = i + 1
        number_of_segments = number_of_lines_for_post_replies / 2
# Opens the posts_replied_to txt file and reads the lines #
with open('posts_replied_to', 'r') as f:
    posts_replied_to = f.read()
    posts_replied_to = posts_replied_to.split('\n')
    posts_replied_to = list(filter(None, posts_replied_to))
# Enters the subreddit #
subreddit = bot.subreddit(CBT)
# Main work for posts #
for submission in subreddit.new(limit=50):
        id_of_post = submission.id
        title_of_post = submission.title
        author_of_post = submission.author
        variable = 0
        while variable < number_of_segments:
            with open('replies_to_reply', 'r') as w:
                lines = w.readlines()
                look_for_list = lines[variable * 2].split(';')
                new_look_for_list = look_for_list[:-1]
                replies = lines[variable * 2 + 1]
                final_reply = str(replies + '\n\n Has replied to: ' + str_number_of_post_replies + ' posts.  This is a bot. Please contact /u/dude0413 for bugs or suggestions.' + version)
            length_of_look_for_list = len(new_look_for_list)
            variable += 1
            x = 0
            while x < length_of_look_for_list:
                if id_of_post not in posts_replied_to:
                    if re.search(new_look_for_list[x], title_of_post, re.IGNORECASE):
                        submission.reply(final_reply)
                        print('Bot replying to : "', title_of_post + '"' + ' by: "' + str(author_of_post) + '"' + ' ')
                        posts_replied_to.append(id_of_post)
                x += 1
with open("posts_replied_to", "w") as f:
    for post_id in posts_replied_to:
        f.write(post_id + "\n")
