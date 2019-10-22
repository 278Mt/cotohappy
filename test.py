#!/usr/bin/env python3.8
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 20 12:00:00 2019
        
COTOHA API for Python3.8
@author: Nicolas Toba Nozomi
@id: 278mt
"""

import unittest
import cotohappy
from time import sleep


class CotohapPyAPITests(unittest.TestCase):

    def __ignore(fn):

        def inr_fn(self, *arg, **kwarg):

            pass

        return inr_fn


    def __interrupt(fn):

        def inr_fn(self, *arg, **kwarg):

            sleep(1)
            return fn(self, *arg, **kwarg)

        return inr_fn


    @__interrupt
    def test_parse(self):

        coy = cotohappy.API()

        sentence = '犬は歩く。'
        type_    = 'default'
        parse_li = coy.parse(sentence, type_)

        self.assertEqual('犬は\t 0,1,D,0,1', str(parse_li[0]))
        self.assertEqual('歩く。\t 1,-1,O,0,1', str(parse_li[1]))
        self.assertEqual('は\t 1,ハ,は,連用助詞,*,*,*,*,*', str(parse_li[0].tokens[1]))
        self.assertEqual('歩\t 2,アル,歩く,動詞語幹,K,*,*,*,*', str(parse_li[1].tokens[0]))


    @__interrupt
    def test_ne(self):

        coy = cotohappy.API()

        sentence = '昨日は東京駅を利用した。'
        type_    = 'default'
        ne_li = coy.ne(sentence, type_)

        self.assertEqual('昨日\t 0,2,昨日,DAT,,*,basic', str(ne_li[0]))
        self.assertEqual('東京駅\t 3,6,東京駅,LOC,,*,basic', str(ne_li[1]))


    @__interrupt
    def test_coreference(self):

        coy = cotohappy.API()

        document   = '太郎は友人です。彼は焼き肉を食べた。'
        type_      = 'default'
        do_segment = True
        coreference = coy.coreference(document, type_, do_segment)

        self.assertEqual('0', str(coreference.coreference[0]))
        self.assertEqual('彼\t 1,1,0,0', str(coreference.coreference[0].referents[1]))


    @__interrupt
    def test_keyword(self):

        coy = cotohappy.API()

        document        = 'レストランで昼食を食べた。'
        type_           = 'default'
        do_segment      = True
        max_keyword_num = 2
        keyword_li = coy.keyword(document, type_, do_segment, max_keyword_num)

        self.assertEqual('昼食\t 12.1121', str(keyword_li[0]))
        self.assertEqual('レストラン\t 9.42937', str(keyword_li[1]))


    @__interrupt
    def test_similarity(self):

        coy = cotohappy.API()

        s1    = '近くのレストランはどこですか？'
        s2    = 'このあたりの定食屋はどこにありますか？'
        type_ = 'default'
        similarity = coy.similarity(s1, s2, type_)

        self.assertEqual('0.88565135', str(similarity))


    @__interrupt
    def test_sentence_type(self):

        coy = cotohappy.API()

        sentence = 'あなたの名前は何ですか？'
        type_    = 'default'
        sentence_type = coy.sentence_type(sentence, type_)

        self.assertEqual('interrogative\t information-seeking,*,*,*,*', str(sentence_type))

    @__interrupt
    def test_sentiment(self):

        coy = cotohappy.API()

        sentence = '人生の春を謳歌しています'
        sentiment = coy.sentiment(sentence)

        self.assertEqual('Positive,0.19562121911742972', str(sentiment))
        self.assertEqual({'安心', '喜ぶ', '*'}, set(str(sentiment.emotional_phrase[0]).split('\t')[-1][1:].split(',')))


    @__interrupt
    def test_user_attribute(self):

        coy = cotohappy.API()

        document = '私は昨日田町駅で飲みに行ったら奥さんに怒られた。'
        type_    = 'default'
        user_attribute = coy.user_attribute(document, type_)

        self.assertEqual('60歳以上,既婚,*,*,*,*,*,*,*,*,*,ANIMAL,CAMERA,COOKING,FISHING,FORTUNE,*,*', str(user_attribute))


    @__interrupt
    def test_remove_filler(self):

        coy = cotohappy.API()

        text       = 'えーーっと、あの、今日の打ち合わせでしたっけ。すみません、ちょっと、急用が入ってしまって。'
        do_segment = True
        remove_filler_li = coy.remove_filler(text, do_segment)

        self.assertEqual('えーっと、あの、今日の打ち合わせでしたっけ。\t 、今日の打ち合わせでしたっけ。', str(remove_filler_li[0]))
        self.assertEqual('すみません、ちょっと、急用が入ってしまって。\t すみません、急用が入ってしまって。', str(remove_filler_li[1]))


    @__interrupt
    def test_detect_misrecognition(self):

        coy = cotohappy.API()

        sentence = '温泉認識は誤りを起こす'
        detect_misrecognition = coy.detect_misrecognition(sentence)

        self.assertEqual('0.9999968696704667', str(detect_misrecognition))
        self.assertEqual('温泉\t 0,2,0.9999968696704667,音声,厭戦,怨念,おんねん,モンセン', str(detect_misrecognition.candidates[0]))



if __name__ == '__main__':

    unittest.main()

