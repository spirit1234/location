# -*- coding:utf-8 -*-
import unittest
from employee import Employee


class TestEmployee(unittest.TestCase):
    """为Employee 编写一个测试用例，其中包含两个测试方法：test_give_default_raise() 和test_give_custom_raise() 。
       使用方法setUp() ， 以免在每个测试方法中都创建新的雇员实例。 运行这个测试用例， 确认两个测试都通过了。"""

    def setUp(self):
        self.info = Employee('john', 'conner', 3000)
        self.add = 6000
        self.sal = [8000, 9000]

    def test_give_default_raise(self):
        self.info.give_raise()
        self.assertEqual(self.info.salary, self.sal[0])

    def test_give_custom_raise(self):
        self.info.give_raise(self.add)
        self.assertEqual(self.info.salary, self.sal[1])


unittest.main()
