from bs4 import BeautifulSoup
import requests
header ={
'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
'Accept-Encoding': 'gzip, deflate, br',
'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
'Cache-Control': 'max-age=0',
'Connection': 'keep-alive',
'Cookie': '',
'DNT': '1',
'Host': 'www.baidu.com',
'Upgrade-Insecure-Requests': '1',
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36',    
}
html = requests.get('http://www.baidu.com/baidu?tn=dealio_dg&wd=seo',headers=headers)
html.encoding = 'utf-8'
content=html.text

soup = BeautifulSoup(content)
# get web title
title = soup.title.get_text()
#get search ruslut
#get c-container
for line in soup.find_all('div',class_='c-container'):
    rank_title = line.find('h3'.get_text().strip()
    try:
        rank_descript = line.find("div",class_="c-abstract").get_text().strip()
    except:
        rank_descript = "特形展示，湖绿"
    rank_id = line['id']

    try:
        rank_domain =re.sub(r".source-icon[\s\S]*?}","",line.find("a",class_="c-showurl").get_text())
    except:
        rank_domain = line.find("span",class_="c-showurl").get_text()
print(rank_id,rank_domain)
print(rank_title)
print('\n')