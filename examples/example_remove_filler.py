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

    text       = 'えーーっと、あの、今日の打ち合わせでしたっけ。すみません、ちょっと、急用が入ってしまって。'
    do_segment = True
    remove_filler_li = coy.remove_filler(text, do_segment)
    for remove_filler in remove_filler_li:
        print(remove_filler)

