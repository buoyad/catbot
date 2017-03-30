#! /usr/bin/python3

import praw, time

reddit = praw.Reddit(client_id='CqLZi59OIemE0Q',
                     client_secret='rOmaFw7vGII43MNHF5AyfdDJcyo',
                     user_agent='cat bot',
                     username='cat-caller',
                     password='cattybrat');

subreddit = reddit.subreddit('CatsStandingUp');
reply = 'Cat.'

for submission in subreddit.stream.submissions():
    try:
        submission.reply(reply)
        pass
    except praw.exceptions.APIException as ex:
        print(ex.message);
        minOut = [int(s) for s in ex.message.split() if s.isdigit()][0] + 1;
        print('Pausing for ' + str(minOut) + ' minutes.');
        time.sleep((minOut)*60)
