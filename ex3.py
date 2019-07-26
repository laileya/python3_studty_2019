import re
keyword ='北京公积金提取条件'
new_keyword = re.sub('北京','深圳',keyword)
print(new_keyword)
import re
keyword =['北京公积金提取条件','深圳公积金提取条件','广州住房公积金提取']
for word in keyword:
    new_word = re.sub(r'(北京|广州|深圳)','',word)
    print(new_word)


import requests

html = requests.get('https://www.baidu.com')
html.encoding = 'utf-8'
print (html.text)