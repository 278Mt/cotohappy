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

    print('\n#### parse origin ####')
    sentence = '犬は歩く。'
    type_    = 'default'
    parse_li = coy.parse(sentence, type_)
    for parse in parse_li:
        print(parse)
    print('\n#### parse tokens ####')
    for parse in parse_li:
        for token in parse.tokens:
            print(token)

