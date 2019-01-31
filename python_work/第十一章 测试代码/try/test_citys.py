# -*- coding:utf-8 -*-
"""创建一个名为test_cities.py的程序， 对刚编写的函数进行测试（别忘了， 你需要导入模块unittest 以及要测试的函数） 。
编写一个名为test_city_country() 的方法， 核实使用类似于'santiago' 和'chile' 这样的值来调用前述函数时，
得到的字符串是正确的。 运行test_cities.py ， 确认测试test_city_country() 通过了。"""
import unittest
from city_function import city_country


class CityTest(unittest.TestCase):
    def test_city_country(self):
        information = city_country('beijing', 'China')
        self.assertEqual(information, 'Beijing, China')

    def test_city_country_population(self):
        """再编写一个名为test_city_country_population() 的测试， 核实可以使用类似于'santiago' 、 'chile' 和
        'population=5000000' 这样的值来调用这个函数。 再次运行test_cities.py， 确认测试test_city_country_population()
         通过了。"""
        information = city_country('shanghai', 'China', population=50000)
        self.assertEqual(information, 'Shanghai, China - Population 50000')

unittest.main()
