#!/usr/bin/env python3.8
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 20 12:00:00 2019
        
COTOHA API for Python3.8
@author: Nicolas Toba Nozomi
@id: 278mt
"""

import cotohappy


if __name__ == '__main__':

    coy = cotohappy.API()

    print('\n#### sentiment origin ####')
    sentence = '人生の春を謳歌しています'
    sentiment = coy.sentiment(sentence)
    print(sentiment)

    print('\n#### sentiment emotional_phrase ####')
    emotional_phrase_li = sentiment.emotional_phrase
    for emotional_phrase in emotional_phrase_li:
        print(emotional_phrase)

