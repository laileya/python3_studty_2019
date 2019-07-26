import requests
requests.post('http://httpbin.org/post')
requests.put('http://httpbin.org/put')
requests.delete('http://httpbin.org/delete')
requests.head('http://httpbin.org/get')
requests.options('http://httpbin.org/get')

#base get requests
import requests
response = requests.get('http://httpbin.org/get')
print(response.text)
#带参数的get请求 例子1
import requests
response = requests.get('http://httpbin.org/get?name=zhaofan&age=23')
print(response.text)

