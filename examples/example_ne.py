#!/usr/bin/env python3.8
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 20 12:00:00 2019
        
COTOHA API for Python3.8
@author: Nicolas Toba Nozomi
@id: 278mt
"""

import cotohappy
from time import sleep


if __name__ == '__main__':

    coy = cotohappy.API()

    sentence = '昨日は東京駅を利用した。'
    type_    = 'default'
    ne_li = coy.ne(sentence, type_)
    for ne in ne_li:
        print(ne)

