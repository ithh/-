#!/usr/bin/python3
# -*- coding:utf-8 -*-

import time

filename = input("输入文件名不带格式后缀：")

s = time.asctime( time.localtime(time.time()) )
str1 = '''
#!/usr/bin/python3
# -*- coding:utf-8 -*-

"""
功能：
作者：ithh
时间：%s
"""

'''%s

# 可通过vscode代码块实现

# print(str1)
with open(filename + '.py', 'w', encoding='utf-8') as f:
    f.write(str1)