import requests
headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36"
}
response =  requests.get('https://www.zhihu.com',headers=headers)
print(response.text)
print(type(response))
print(response.status_code)
print(response.cookies)
print(response.content)
print(response.content.decode("utf-8"))
print(response.headers)