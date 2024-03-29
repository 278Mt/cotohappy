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

    document        = 'レストランで昼食を食べた。'
    kuzure          = False
    do_segment      = True
    max_keyword_num = 2
    keyword_li = coy.keyword(document, kuzure, do_segment, max_keyword_num)
    for keyword in keyword_li:
        print(keyword)

