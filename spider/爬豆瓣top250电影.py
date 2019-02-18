#!/usr/bin/env python
# coding: utf-8

# # 网站分析

# In[2]:


# -*- coding:utf-8 -*-
import requests


def get_movie():
    headers = {
        'user-agent':
        'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
        'Host':
        'movie.douban.com'
    }
    for i in range(0, 10):
        link = 'https://movie.douban.com/top250?start=' + str(i * 25)
        r = requests.get(link, headers=headers, timeout=10)
        print(str(i + 1), '响应状态码:', r.status_code)
        print(r.text)


get_movie()


# # 爬取Top前250电影(名称+评分+简介)

# In[99]:


# -*- coding:utf-8 -*-
import requests
from bs4 import BeautifulSoup
import re

movie_list = []  # 电影名称列表
infomation_list = []  # 简介列表
jjq_list = []  # 电影评分列表
final_list = []  # 最终全部列表
movie_dict = {}  # 电影名称简介字典
word = '豆瓣'


def get_movies():
    headers = {
        'user-agent':
        'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
        'Host':
        'movie.douban.com'
    }

    for i in range(10):
        link = 'https://movie.douban.com/top250?start=%s' % (i * 25)
        r = requests.get(link, headers=headers, timeout=10)
        print('%s,响应状态码: %s' % ((i + 1), r.status_code))
        soup = BeautifulSoup(r.text, 'lxml')
        div_list = soup.find_all('div', class_='hd')  # 获取电影名称
        sorce_list = soup.find_all('span', class_='rating_num') # 获取电影评分
        info_list = soup.find_all('div', class_='bd')  #获取简介

        for each in div_list:
            movie = each.a.span.text.strip()
            movie_list.append(movie)

        for j in sorce_list:
            sorce = str(j.text) + '分'
            jjq_list.append(sorce)

        for l in info_list:
            info = l.p.text.strip()
            if info == '豆瓣':
                pass
            else:
                infomation_list.append(info)


def add_dict():
    for k in range(250):
        movie_dict[movie_list[k]] = infomation_list[k]

    for key, value in movie_dict.items():
        with open('电影名称+简介.txt', 'a+', encoding='utf-8') as df:
            df.write(key + '\n 简介: \n ' + str(value) + '\n')


def add_all():
    for x in range(250):
        final_list.append(movie_list[x])
        final_list.append(jjq_list[x])
        final_list.append(infomation_list[x])
    for i in final_list:
        with open('电影名+评分+简介', 'a', encoding='utf-8') as wr:
            wr.write(i + '\n')


get_movies()
add_all()


# In[ ]:




