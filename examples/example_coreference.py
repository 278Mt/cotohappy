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

    document   = '太郎は友人です。彼は焼き肉を食べた。'
    type_      = 'default'
    do_segment = True
    coreference = coy.coreference(document, type_, do_segment)

    print('\n#### coreference reference ####')
    for content in coreference.coreference:
        for referent in content.referents:
            print(referent)
