import praw
import time
import datetime
import prawcore

user = '' #Bot Username
pass = '' #Bot Password
c_id = '' #Bot Client ID
c_secret = '' #Bot Client Secret

sub = '' #Subreddit you want the bot to run in

minimum_submission_time = 3600 #The amount of milliseconds you want to pass for a post to get the allotted amount of minimum karma
minimum_karma = 10 #Replace with the minimum karma you want a post to have

reddit = praw.Reddit(
    username = user,
    password = pass,
    client_id = c_id,
    client_secret = c_secret,
    user_agent = 'MinimumKarmaBot by Rubix'
)

def removePost(submission):
    
    now = datetime.datetime.now() #Current Time
    submission_created = datetime.datetime.fromtimestamp(submission.created) #Time submission was created
    
    if(now - submission_created.seconds >= minimum_submission_time and submission.score < minimum_karma):
        comment = submission.reply("Your submission didn't reach the amount of minimum karma within the allotted time.")
        try:
            comment.distinguish(how='yes', sticky=True)
            submission.mod.remove()
        except prawcore.exceptions.Forbidden:
            print('Cannot remove post, check if bot has moderators privileges')
            input('Press any key to close')
            exit()


def main(r):
    while True:
        for s in reddit.subreddit(str(sub)).new():
            remove(s)
        time.sleep(60) #waits 1 minute before rechecking all posts

if __name__ == '__main__':
    main(r);
