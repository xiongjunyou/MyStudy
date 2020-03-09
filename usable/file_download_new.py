#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
@author: JY
@project: Treefrog
@file: test_download_new.py
@function: 解决urlretrieve下载文件不完全的问题且避免下载时长过长陷入死循环
@time: 2020-3-9 9:48
"""
import pathlib
import re
import socket
import time
import urllib.request

url = "http://www.cc518.com/res/2017/10-09/13/d359aa8796e5612be81623bb6f03aa19.jpg\
http://www.cc518.com/res/2017/10-09/13/cc5851398893b72fc58aadc85d4dafe7.jpg\
http://www.cc518.com/res/2017/10-09/13/1cb1c68aac661884638d4a9700f56733.jpg\
http://www.cc518.com/res/2017/10-09/13/09cb849cdcf54068bb24ec90b7fd3008.jpg\
http://www.cc518.com/res/2017/10-09/13/860ba3ba2ed5c20f36cddcd3f02d691a.jpg\
http://www.cc518.com/res/2017/10-09/13/66888f05ce1678b3734d10850e72fb2a.jpg\
http://www.cc518.com/res/2017/10-09/13/7e4838993718e8c78bd8f4c319c609a2.jpg\
http://www.cc518.com/res/2017/10-09/13/10fa45fc14981e835019f25e84e4481e.jpg\
http://www.cc518.com/res/2017/10-09/13/3db477769ca55f8993d13917adf295ae.jpg\
http://www.cc518.com/res/2017/10-09/13/ea0a409d5c87ac117ec8fc515d744e55.jpg\
http://www.cc518.com/res/2017/10-09/13/b16a2aa249a3e9b33ad98c6f86162695.jpg\
http://www.cc518.com/res/2017/10-09/13/dbf5508361c7082bb0d3ffef712df4fc.jpg\
http://www.cc518.com/res/2017/10-09/13/455d165fab679b63b98b012dacc2024d.jpg\
http://www.cc518.com/res/2017/10-09/13/151db99dcef8acd05147480bf5624a25.jpg\
http://www.cc518.com/res/2017/10-09/13/04508403ab26b7f0f181d9b6cac16f4b.jpg\
http://www.cc518.com/res/2017/10-09/13/7bae29029f2e1e836f6cf78eb84119cf.jpg\
http://www.cc518.com/res/2017/10-09/13/b0f332a5c10778f698de0f38b9b2fb68.jpg\
http://www.cc518.com/res/2017/10-09/13/6fd701d7583da174018f58684829ad13.jpg\
http://www.cc518.com/res/2017/10-09/13/56e94393209d06bc14819e82c8afd7b5.jpg\
http://www.cc518.com/res/2017/10-09/13/f639c0f1c6ad0ec576543c7058b6284c.jpg\
http://www.cc518.com/res/2017/10-09/13/f8b21f997ef6ebd1ea5e106d33724184.jpg\
http://www.cc518.com/res/2017/10-09/13/09999ee470099fbd47c152b8a3ccbcb6.jpg\
http://www.cc518.com/res/2017/10-09/13/986ee8c0967faa245f9fccdd207e3402.jpg\
http://www.cc518.com/res/2017/10-09/13/5b8649c8cd4edc920a99449ce0d39591.jpg\
http://www.cc518.com/res/2017/10-09/13/5304a2091fa16649a0ef911eebeb2d34.jpg\
http://www.cc518.com/res/2017/10-09/13/ac0d433a7a30e5c423f49d5fcedaa83a.jpg\
http://www.cc518.com/res/2017/10-09/13/db52992dfa2f682d71a274c64dfdbd85.jpg\
http://www.cc518.com/res/2017/10-09/13/3a41460587fd6e83ac4c660ed2bfd3f8.jpg\
http://www.cc518.com/res/2017/10-09/13/c8f008a535d81bee817ccda22243841f.jpg\
http://www.cc518.com/res/2017/10-09/13/e298d62348ca13d417a2de530c326a03.jpg\
http://www.cc518.com/res/2017/10-09/13/726a00767ada15b9fa2420fd72adcde8.jpg\
http://www.cc518.com/res/2017/10-09/13/a1cd55ad2586441d5b57f4d876b448bb.jpg\
http://www.cc518.com/res/2017/10-09/13/eb866e19f29a287c109ca9ecdb2cff0b.jpg\
http://www.cc518.com/res/2017/10-09/13/b387eb0e009e687d337f4316b95107f9.jpg\
http://www.cc518.com/res/2017/10-09/13/b21aacaf4d30114f29b50435b6dda33d.jpg\
http://www.cc518.com/res/2017/10-09/13/e2c339d55d7bf45c138d2ee73671c541.jpg\
http://www.cc518.com/res/2017/10-09/13/baeb8deec5e0817426265b6950c72276.jpg\
http://www.cc518.com/res/2017/10-09/13/61334b1db7792bea34113aab1936041c.jpg\
http://www.cc518.com/res/2017/10-09/13/2e2f54f171c61a8a82e7be6109e17b18.jpg\
http://www.cc518.com/res/2017/10-09/13/09542adf15992a7a86a8f36f9bc901fe.jpg"

headers = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.80 Safari/537.36'
header = headers.encode()  # 不进行类型转换无法传入urlretrieve()，需转换成bytes类型


def callback(a1, a2, a3):
    """
    显示下载文件的进度
    :param @a1:目前为此传递的数据块数量
    :param @a2:每个数据块的大小，单位是byte,字节
    :param @a3:远程文件的大小
    :return: None
    """
    download_pg = 100.0 * a1 * a2 / a3
    if download_pg > 100:
        download_pg = 100

    print("当前下载进度为: %.2f%%" % download_pg, )


def download(url, filename, callback, header):
    """
    封装了 urlretrieve()的自定义函数，递归调用urlretrieve(),当下载失败时，重新下载
    download file from internet
    :param url: path to download from
    :param savepath: path to save files
    :return: None
    """

    try:
        urllib.request.urlretrieve(url, filename, callback, header)
    # except urllib.ContentTooShortError:
    #     print('Network conditions is not good.Reloading.')
    #     download(url, filename, callback, header)
    except Exception as e:
        print(e)
        print('Network conditions is not good.\nReloading.....')
        download(url, filename, callback, header)


img_urls = re.findall('http.*?jpg', url)
print(img_urls)
file_name = "图片"
index = 1
# print("1$" * 50)
# print("\n")
for img_src in img_urls:
    # print("2$" * 50)
    # print(img_src)
    # print("\n")
    img_path = '.\\' + file_name + '{}.jpg'.format(index)
    index += 1
    i = pathlib.Path(img_path)
    if not i.exists():
        # print("3$" * 50)
        print("\n")
        print('Downloading data from %s' % img_src)
        # time.sleep(1.5)  # 设置的缓冲时间，个人习惯

        # 设置超时时间为10s,时间长短自定义
        socket.setdefaulttimeout(10)
        # 解决下载不完全问题且避免陷入死循环
        try:
            download(img_src, img_path, callback, header)
            print(img_path, '\nDownload finished!')
        except socket.timeout:
            count = 1
            while count <= 5:
                try:
                    download(url, img_path, callback, header)  # 封装了 urlretrieve()的自定义函数，递归调用urlretrieve
                    break
                except socket.timeout:
                    err_info = 'Reloading for %d time' % count if count == 1 else 'Reloading for %d times' % count
                    print(err_info)
                    count += 1
            if count > 5:
                print("downloading picture fialed!")
    else:
        # print("4$" * 50)
        print("\n")
        print(img_path, "'File already exsits!'")
    # 获取文件大小
    filesize = i.stat().st_size
    # 文件大小默认以Bytes计， 转换为Mb
    print('File size = %.2f Mb(%.2f Kb)' % (filesize / 1024 / 1024, filesize / 1024))
