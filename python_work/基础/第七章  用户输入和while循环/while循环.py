# -*- coding:utf-8 -*-
# 循环1-5的数字
current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1

# 让用户选择退出
prompt = "Tell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "
message = ''
while message != 'quit':
    message = input(prompt)
    if message != 'quit':
        print(message)
