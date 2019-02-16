#!/usr/bin/env python
# coding: utf-8

# # 获取页面

# In[1]:


# -*- coding:utf-8 -*-
import sys
import requests
from bs4 import BeautifulSoup  #从bs4库导入BeautifulSoup
link = 'http://www.santostang.com'
headers = {
    'User-Agent':
    'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
}
r = requests.get(link, headers=headers)  # 获取页面
soup = BeautifulSoup(r.text, 'lxml')
title = soup.find('h1', class_='post-title').a.string.rstrip()  # 提取标题数据
print(title)

with open('title.txt', 'w') as f:
    f.write(title)  # 存储标题到title.txt中

