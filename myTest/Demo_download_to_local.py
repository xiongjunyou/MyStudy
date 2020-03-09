#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
@author: JY
@project: Treefrog
@file: Demo_download_to_local.py
@function: 下载文件到本地
@time: 2020-3-8 21:44
"""

from urllib import request

"""
urlretrieve参数说明：
1.传入网址,网址的类型一定是字符串

2.传入的，本地的网页保存路径+文件名

3.一个函数的调用，我们可以随便定义这个函数，但是必须得有3个参数
    ①到目前为此传递的数据块数量
    ②是每个数据块的大小，单位是byte,字节
    ③远程文件的大小
"""


def callback(a1, a2, a3):
    """
        显示下载文件的进度
        @a1:目前为此传递的数据块数量
        @a2:每个数据块的大小，单位是byte,字节
        @a3:远程文件的大小
    """
    download_pg = 100.0 * a1 * a2 / a3
    if download_pg > 100:
        download_pg = 100

    print("%.2f%%" % download_pg, )


url = "http://www.hao6v.com/"
# url = "http://www.cc518.com/res/2017/11-26/19/b9a1e651b958b26f11ba2dc8618b6a92.jpg"
local = ".\\hellobi.html"
# local = ".\\hellobi.jpg"

# urllib模块提供的urlretrieve()函数,urlretrieve()方法直接将远程的数据下载到本地
request.urlretrieve(url, local, callback)