"""
Coursera 2014 Introduction to Data Science
Assignment: Twitter Sentiment Analysis in Python Problem 3
Program Description: term_sentiment.py
    This program computes the sentiment of each tweet based on the sentiment scores of the
    terms in the tweet. It is equivalent to the sum of the sentiment scores for each term in
    the tweet.
Program Notes:
    Using the output.txt file (generated from python twitterstream.py > output.txt
    Script computes the sentiment for the terms that do not appear in the AFINN-111.txt
Output notes:
    File format is json
    streaming message... most are tweets, but not all
$ python term_sentiment.py AFINN-111.txt output_first_20.txt
Example:

...
Skeleton code provided in original file:
def hw():
    print 'Hello, world!'

def lines(fp):
    print str(len(fp.readlines()))

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    hw()
    lines(sent_file)
    lines(tweet_file)

if __name__ == '__main__':
    main()

"""

from __future__ import division
import sys
import json


def read_scores(sent_file):
    with open(sent_file) as f:
        return {line.split('\t')[0]: int(line.split('\t')[1]) for line in f}


def score_tweet(tweet, scores):
    return sum(scores.get(word, 0) for word in tweet)


def unknown_word_scores(tweet_file, scores):
    with open(tweet_file) as f:
        tweets = (json.loads(line).get('text', '').split() for line in f)
        return {word: score_tweet(tweet, scores) / len(tweet)
                for tweet in tweets if tweet
                for word in tweet if word not in scores}


if __name__ == '__main__':
    scores = read_scores(sent_file=sys.argv[1])
    sys.stdout.writelines('{0} {1}\n'.format(word.encode('utf-8'), score)
                          for word, score in unknown_word_scores(
                              tweet_file=sys.argv[2],
                              scores=scores).items())