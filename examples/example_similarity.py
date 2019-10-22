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

    s1    = '近くのレストランはどこですか？'
    s2    = 'このあたりの定食屋はどこにありますか？'
    type_ = 'default'
    similarity = coy.similarity(s1, s2, type_)
    print(similarity)
