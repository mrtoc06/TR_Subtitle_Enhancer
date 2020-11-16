# -*- coding: utf-8 -*-
"""
Created on Sun Nov 15 20:55:32 2020

@author: Mr. Toç
"""

convert_map = {
    ord(u'Ý'): u'İ',
    ord(u'ý'): u'ı',
    ord(u'ð'): u'ğ',
    ord(u'þ'): u'ş',
    ord(u'Þ'): u'Ş'
    }

name = 'Shutter.Island.2010.1080p.BluRay.x264.YIFY-tur.srt'

file = open(name, 'r')
subtitle = file.readlines()
file.close()

new_subtitle = []
for i in subtitle:
    newline = i.translate(convert_map)
    new_subtitle.append(newline)

newfile = open(name, 'w', encoding='utf-8')
newfile.writelines(new_subtitle)