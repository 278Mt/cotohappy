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

    document = '私は昨日田町駅で飲みに行ったら奥さんに怒られた。'
    kuzure   = False
    user_attribute = coy.user_attribute(document, kuzure)
    print(user_attribute)

