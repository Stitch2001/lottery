import re

with open('test.txt', encoding='utf-8') as f:
    content = f.read()
# result = re.findall(r'<div class="bili-dyn-forward-item__uname"><span.+?>(.+?)</span>', content)
# ↑转发名单
# result = re.findall(r'<span class="fans-name".*?>(.+?)</span>', content)
# ↑粉丝名单
# result = re.findall(r'<span.+?class="name-field"><a.+?>(.+?)</a>', content)
# ↑点赞的名单
result = re.findall(r'<div class="con "><div class="user"><a.*?>(.+?)</a>', content)
# ↑评论的名单

print(result)