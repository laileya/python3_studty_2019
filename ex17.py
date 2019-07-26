import re
content = "hello 123 4567 World_This is a regex Demo"
result = re.match('^hello.*Demo$',content)
print (result)
print (result.group())
print (result.span())
#regex 匹配目标
import re
content= "hello 1234567 World_This is a regex Demo"
result = re.match('^hello\s(\d+)\sWorld.*Demo$',content)
print(result)
print(result.group())
print(result.group(1))
print(result.span())

#regex 贪婪匹配
import re

content= "hello 1234567 World_This is a regex Demo"
result = re.match('^hello.*(\d+).*Demo',content)
print(result)
print(result.group(1))

import re
content= "hello 1234567 World_This is a regex Demo"
result = re.match('^h.*?(\d+).*Demo$',content)
print(result)
print(result.group())
print(result.group(1))
print(result.span())