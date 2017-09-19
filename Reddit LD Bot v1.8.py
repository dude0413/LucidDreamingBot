from package import config
import praw, re
from package.credentials import account_sid, auth_token, my_twilio, my_cell
from twilio.rest import Client

version = 'v1.8'
# Common sub-reddits #
LD = 'LucidDreaming'
CBT = 'Cool_Bot_Testing'

# Login into the bot and SMS #
bot = praw.Reddit(user_agent='LDbot v1.8',
                  client_id=config.client_id,
                  client_secret=config.client_secret,
                  username=config.username,
                  password=config.password)
client = Client(account_sid, auth_token)
# Gets the number of posts that the bot has replied to and reads and splits the contents of the txt file #
with open('posts_replied_to') as r:
    for i, l in enumerate(r):
        number_of_post_replies = i + 2
        str_number_of_post_replies = str(number_of_post_replies)
    posts_replied_to = r.read()
    posts_replied_to = posts_replied_to.split('\n')
    posts_replied_to = list(filter(None, posts_replied_to))
# Get the number of lines of the replies and look for. Also numbers the segments of the post replies #
with open('replies_to_reply', 'r') as c:
    for i, l in enumerate(c):
        number_of_lines_for_post_replies = i + 1
        number_of_segments = number_of_lines_for_post_replies / 2
# Enters the subreddit #
subreddit = bot.subreddit(LD)
# Main work for posts #
for submission in subreddit.new(limit=50):
        id_of_post = submission.id
        title_of_post = submission.title
        author_of_post = submission.author
        segment_variable = 0
        while segment_variable < number_of_segments:
            with open('replies_to_reply', 'r') as w:
                lines = w.readlines()
                look_for_list = lines[segment_variable * 2].split(';')
                new_look_for_list = look_for_list[:-1]
                replies = lines[segment_variable * 2 + 1]
                final_reply = str(replies + '\n\n Has replied to: ' + str_number_of_post_replies + ' posts.  This is a bot. Please contact /u/dude0413 for bugs or suggestions.\n\n' + version + '\n\n ')
            length_of_look_for_list = len(new_look_for_list)
            segment_variable += 1
            list_variable = 0
            while list_variable < length_of_look_for_list:
                if id_of_post not in posts_replied_to:
                    if re.search(new_look_for_list[list_variable], title_of_post, re.IGNORECASE):
                        submission.reply(final_reply)
                        replying_to = 'Bot replying to : "'+ title_of_post + '"' + ' by: "' + \
                                      str(author_of_post) + '"' + ' '
                        print(replying_to)
                        posts_replied_to.append(id_of_post)
                        # SMS work #
                        client.messages.create(
                            to=my_cell,
                            from_=my_twilio,
                            body=replying_to
                        )
                list_variable += 1

with open("posts_replied_to", "w") as f:
    for post_id in posts_replied_to:
        f.write(post_id + "\n")
