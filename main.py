import praw
import random
import time
# QUOTES is an array of "inspirational" quotes!!
QUOTES = [
    "Would I rather be happy or right? Michael, I am always right. It's not even a question -Michael Scott",
"Do I need to be liked? Absolutely not. I like to be liked. I enjoy being liked. I have to be liked. But it's not like this, compulsive, need, to be liked. Like my need to be praised. -Michael Scott",
"I knew exactly what to do. But in a much more real sense, I had no idea what to do. -Michael Scott",
"Would I rather be a great salesman or a great leader? I've discovered that I can be both, because I am awesome at sales. -Michael Scott",
"I am ready to face any challenges that might be foolish enough to face me. -Michael Scott",
"Sometimes I'll start a sentence and I don't even know where it's going. I just hope I find it along the way. -Michael Scott",
"Would I rather be in pain or have pleasure? I'd rather be in pain. Pleasure is fleeting, but pain is forever. -Michael Scott"
]

reddit = praw.Reddit(
    client_id="2uyavVlISkMegCKI2K2ieg",
    client_secret="Cd2oGQhU1iSmx6t0Jgx3OPiZ6JvKyQ",
    user_agent="<console:froyo:1.0>",
    username=" Mediocre-Froyo-9033 ",
    password="chocomoco"
)
subreddit = reddit.subreddit("bollywood")
for post in subreddit.hot(limit=140):
    print("^^^^^^^^^^^^^^")
    print(post.title)

    for comment in post.comments:
        if hasattr(comment,'body'):
            commentlower=comment.body.lower()
            if " sad " in commentlower:
                print("**************")
                print(comment.body)
                random_index=random.randint(0,len(mike)-1)
                comment.reply(mike[random_index])
                time.sleep(660)

