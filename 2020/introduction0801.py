#!/usr/bin/env python

print("Hello, World!")


# Python中默认的编码格式是 ASCII 格式，在没修改编码格式时无法正确打印汉字，所以在读取中文时会报错。解决方法为只要在文件开头加入   # -*- coding: UTF-8 -*- 或者 # coding=utf-8 就行了
# -*- coding: UTF-8 -*-
# 注意：Python3.X 源码文件默认使用utf-8编码，所以可以正常解析中文，无需指定 UTF-8 编码。
# 注意：如果你使用编辑器，同时需要设置 py 文件存储的格式为 UTF-8
# 20200801 学习到  中文编码  https://www.runoob.com/python/python-chinese-encoding.html
print("你好")

# 基础语法 https://www.runoob.com/python/python-basic-syntax.html

# geektime 第四章 12节 if 条件语句
x = 'abc'
if x == 'abc':
    print('x 的值等于abc')

# geektime 第十五章 爬虫

from urllib import request
url = 'http://www.baidu.com'
response = request.urlopen(url,timeout=1)
print (response.read())

#网页数据的采集与urllib
from urllib import request
url = 'http://www.baidu.com'
response = request.urlopen(url,timeout=1)
print (response.read().decode('UTF-8 '))
# 网页的常见两种请求方式 get， post   ， http测试网站 httpbin.org
# get的好处是简单， 缺点有大小限制
# post

