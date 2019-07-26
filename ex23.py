import re
content =""" hello 12345 world_this
123 fan
"""
pattern=re.compile("hello.*fan",re.S)
result = re.match(pattern,content)
print(result)
print(result.group())