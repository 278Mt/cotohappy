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

    sentence = 'あなたの名前は何ですか？'
    type_    = 'default'
    sentence_type = coy.sentence_type(sentence, type_)
    print(sentence_type)

