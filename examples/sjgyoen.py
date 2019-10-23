#!/usr/bin/env python3.8
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 20 12:00:00 2019
        
COTOHA API for Python3.8
@author: Nicolas Toba Nozomi
@id: 278mt
"""

import cotohappy
import requests
from bs4 import BeautifulSoup


def get_kotonoha_story():
    
    url = 'https://www.kotonohanoniwa.jp/page/product.html'
    res = requests.get(url)

    soup = BeautifulSoup(res.content, 'html.parser')
    p = soup.find_all('p', class_='mb24')[-1]

    return p.text


if __name__ == '__main__':

    payload_fname = 'payload.json'
    
    """ if you prepare authority file for your account on Cotoha API, you can write such as: """
    coy = cotohappy.API(payload_fname=payload_fname)    # payload_fname's default: 'payload.json'

    """ so you can omit payload_fname:
    coy = cotohappy.API()
    """
    
    """ or you can do another type:
    ACCESS_TOKEN_PUBLISH_URL = 'https://api.ce-cotoha.com/v1/oauth/accesstokens'
    API_BASE_URL             = 'https://api.ce-cotoha.com/api/dev/'
    CLIENT_ID                = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ123456'
    CLIENT_SECRET            = '7890abcdefghijkl'
    coy = cotohappy.API(
        ACCESS_TOKEN_PUBLISH_URL,
        API_BASE_URL,
        CLIENT_ID,
        CLIENT_SECRET
    )
    # you can confirm your Access Token Publish URL, API Base URL, Client ID, and Client secret on the website (https://api.ce-cotoha.com/home)
    """

    """ getting parse """
    print('\n#### parse origin ####')
    sentence = get_kotonoha_story()
    type_    = 'default'
    parse_li = coy.parse(sentence, type_)
    for parse in parse_li:
        print(parse)

    print(parse.key_name)

    """ getting tokens; it is a little more difficult than MeCab Janome """
    print('\n#### parse tokens ####')
    for parse in parse_li:
        for token in parse.tokens:
            print(token)

    print(token.key_name)

    """ if you extract just nouns, you write: """
    print('\n#### extract nouns ####')
    nouns = []
    for parse in parse_li:
        for token in parse.tokens:
            if token.pos == '名詞':
                nouns.append(token.form)

    print(nouns)

