import re
content = "extra thing hello 123455 world_this is a Re Extra things"

result = re.search("hello.*?(\d+).*?Re",content)
print(result)
print(result.group())
print(result.group(1))
