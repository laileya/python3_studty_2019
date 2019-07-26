import requests
import re
content = requests.get('https://www.douban.com/').text
pattern = re.compile()