import re

content = '''hello 123456 world_this
my name is zhaofan
'''
result = re.match('^he.*?(\d+).*?zhaofan$',content,re.S)
print(result)
print(result.group())
print(result.group(1))