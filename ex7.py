import requests
response = requests.get('https://www.baidu.com')
print(response.text)
print(type(response))
print(response.status_code)
print(response.content)
print(response.content.decode("utf-8"))
print(response.cookies)
