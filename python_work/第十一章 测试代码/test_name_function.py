# -*- coding:utf-8 -*-
import unittest
from name_function import get_formatted_name


class NameTestCase(unittest.TestCase):
    # 定义的函数前面一定要加test方可自动执行
    def test_first_last_name(self):
        formatted_name = get_formatted_name('john', 'conner')
        # 利用断言的方法判断是否相等
        self.assertEqual(formatted_name, 'John Conner')

    def test_first_last_middle(self):
        formatted_name = get_formatted_name('aa', 'bb', 'cc')
        self.assertEqual(formatted_name, 'Aa Cc Bb')


unittest.main()
