with open('realFans.txt',encoding='utf-8') as f:
    fans1 = set(f.readlines())
with open('评论视频的fans.txt',encoding='utf-8') as f:
    fans2 = set(f.readlines())
realFans = set.intersection(fans1,fans2)
with open('3rdReward.txt','w',encoding='utf-8',newline='') as f:
    for i in realFans:
        f.write(i)
