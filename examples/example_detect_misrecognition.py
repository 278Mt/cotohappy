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

    sentence = '温泉認識は誤りを起こす'
    detect_misrecognition = coy.detect_misrecognition(sentence)
    for candidate in detect_misrecognition.candidates:
        print(candidate)

