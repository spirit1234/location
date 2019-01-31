# -*- coding:utf-8 -*-
import json

numbers = [1, 2, 3, 4, 5, 6, 7]
filename = 'json/numbers.json'
with open(filename, 'w') as file_obj:
    json.dump(numbers, file_obj)
