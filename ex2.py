import re
keyword = "谁有口子黑户的推荐,谁有口子不上征信的推荐下sadasda"
#提取‘口子’后面谁有字符
'''
re 模块：匹配字符
语法：re.search
'''
a = re.search(r'(.*?口子)',keyword)
print(a.group(1))
list = [1,2,3,4]
it = iter(list)
print(next(it))
html = '''
<head>
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
    <meta property="qc:admins" content="465267610762567726375" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>正则表达式 &#8211; 语法 | 菜鸟教程</title>   
    <meta name="apple-mobile-web-app-title" content="title菜鸟教程">
    <link rel='dns-prefetch' href="//s.w.org" />
    <link rel="canonical" href="http://www.runoob.com/regexp/regexp-syntax.html" />
    <meta name="keywords" content="正则表达式 &#8211; 语法">
    <meta name="description" content="正则表达式 - 语法  正则表达式(regular expression)描述了一种字符串匹配的模式（pattern），可以用来检查一个串是否含有某种子串、将匹配的子串替换或者从某个串中取出符合某个条件的子串等。 例如：  runoo+b，可以匹配 runoob、runooob、runoooooob 等，+ 号代表前面的字符必须至少出现一次（1次或多次）。   runoo*b，可以匹配 runob、runoob、runoooooob 等..">
    <link rel="apple-touch-icon" href="//static.runoob.com/images/icon/mobile-icon.png"/>
</head>'''

import re
title = re.search(r'name="description" content="(.*?)"', html).group(1)

print (title)

import re
keyword = re.search(r'name="keywords" content="(.*?)"',html).group(1)
print(keyword)

import re
header = re.search(r'<title>(.*?)</title> )',html).group(1)
print(header)