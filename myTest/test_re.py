#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
@author: JY
@project: Treefrog
@file: test_re.py
@function:
@time: 2020-3-8 23:48
"""
import re

ret = re.findall("(http.*?jpg)","http://www.cc518.com/res/2018/06-27/13/5947442c8344adfedf2780ac51d72806.jpg\
http://www.cc518.com/res/2018/06-27/13/3bdced4d0eb1c8334317e74e7aafff42.jpg\
http://www.cc518.com/res/2018/06-27/13/324c587f74b0be6643648dc9831834ea.jpg")
print(ret)