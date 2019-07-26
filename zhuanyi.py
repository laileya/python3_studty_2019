import re
content = "price is $5.00"
result = re.match('price is \$5',content)
print(result)
print(result.group())