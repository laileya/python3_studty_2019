import requests

response = requests.get("https://www.12306.cn")
print(response.status_code)
#set proxies
import requests

proxies ={
    "http":"http://127.0.0.1:9999",
    "http":"http://127.0.0.1:8888"
}
response = requests.get("https://www.baidu.com",proxies=proxies)
print(response.text)

#auth
import requests
from requests.auth import HTTPBasicAuth

response = requests.get("http://www.baidu.com",auth=HTTPBasicAuth("user","123"))
print(response.status_code)

#error
import requests

from requests.exceptions import ReadTimeout,ConnectionError,RequestException

try:
    response = requests.get("http://httpbin.org/get",timeout=0.1)
    print(response.status_code)
except ReadTimeout:
    print("timeout")
except ConnectionError:
    print("connection Error")
except RequestException:
    print("error")