#使用params关键字 传递参数，以一个字典来传递这些参数
import requests
data = {
    'name':'zhaofan',
    'age':'22'
}
response = requests.get('http://httpbin.org/get',params=data)
print(response.url)
print(response.text)
