#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
@author: JY
@project: Treefrog
@file: test_redis.py
@function:
@time: 2020-3-7 22:09
"""
from redis import StrictRedis

if __name__ == '__main__':
    # 创建一个StrictRedis对象，链接redis数据库
    try:
        sr = StrictRedis('192.168.31.234',6379,0)
        # 添加一个key，为name，value firstredis
        res = sr.set('name','firstredis')
        print(res)

    except Exception as e:
        print(e)