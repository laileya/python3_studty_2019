#re.sub replace
import re
content ="Extra things hello 123455 World_this is a regex Demo extra things"
content = re.sub('\d+','',content)
print(content)

import re
content ="Extra things hello 123455 World_this is a regex Demo extra things"
content =re.sub('(\d+)',r'\1 7890',content)
print(content)