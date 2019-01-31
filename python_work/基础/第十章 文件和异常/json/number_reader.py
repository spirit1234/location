# -*- coding:utf-8 -*-
import json

filename = 'numbers.json'
with open(filename, 'r') as file_object:
    print(json.load(file_object))
