import requests
import re
content = requests.get('https://book.douban.com/').text

 
#print (content)
pattern = re.compile(r'<li.*?cover.*?href="(.*?)"\stitle="(.*?)".*?more-meta.*?author">(.*?)</span>.*?year">(.?)</span>.?</li>', re.S)##这里应该要在URL和title之间匹配空格，用\s
results = re.findall(pattern, content)

 
#print(results)
for result in results:
url , name , author , date = result
name = re.sub('\s','',name)
author = re.sub('\s','',author)
date = re.sub('\s','',date)
print(url,name,author,date)