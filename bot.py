#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tweepy
from tweepy import OAuthHandler
import time
import sys
import os
from random import randint

argfile = str(sys.argv[1])
'''
CONSUMER_KEY = os.environ['CONSUMER_KEY']
CONSUMER_SECRET = os.environ['CONSUMER_SECRET']
ACCESS_KEY = os.environ['ACCESS_KEY']
ACCESS_SECRET = os.environ['ACCESS_SECRET']
'''
CONSUMER_KEY = 'YzcmOhS5vLRTYh2dBPSOGrBHa'
CONSUMER_SECRET = 'pad1355Svxr8IzeEjmJ6f6KBdcyC6AbxQWP1iIaD4vck9IswAJ'
ACCESS_KEY = '761208704448524288-ifLM5ZfbAQCf44TPKzcO2Mk54yauzfG'
ACCESS_SECRET = 'kgMWUieQqz8D1TMqhqsvZuePBAPwxxQfiQEfKtHwSebD5'
auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

if __name__ == "__main__":
    while True:
        with open(argfile) as f:
            lines = f.readlines()
            if len(lines) >= 1:
              rand_line_num = randint(0, len(lines) - 1)
              line = lines[rand_line_num]
              api.update_status(line.strip())
              del lines[rand_line_num]
              rand_time = randint(0, 7500)
              time.sleep(rand_time)
            else:
              api.update_status("!!!?!!!!!!!!!")
              break
        nf = open(argfile, 'w')
        nf.write("".join(lines))
        nf.close()
