# -*- coding: utf-8 -*-
# 小蓝中央控制

import sys
import os
import re
import setting
from speech_center.stt import baidu_stt
from speech_center.stt import ifly_stt
from speech_center.tts import baidu_tts
from speech_center.tts import youdao_tts
from Base import xiaolanBase
import speech_center.speaker as speaker
import visual_centre.face as face

class Xiaolan(xiaolanBase):

    def __init__(self):

        super(Xiaolan, self).__init__()

    def awaken(self):
    
        self.snowboy.awaken()

    def welcome(self):
    
        print ('''

        #############################################
        #       小蓝——语音交互式智能家居机器人        #  
        #  https://www.github.com/xiaoland/xiaolan  #
        #    （c）袁翊闳——1481605673@qq.com         #
        #############################################
        
        ''')

        self.tts.tts(setting.setting()['main_setting']['your_name'] + '，你好啊，我是你的小蓝', tok)
        speaker.speak()
        os.system('pulseaudio --start')
        if self.set['main_setting']['awaken'] == 'hotword':
            self.awaken()
        elif self.set['main_setting']['awaken'] == 'face':
            face.awaken()
        elif self.set['main_setting']['awaken'] == 'all':
            pass

welcome()
