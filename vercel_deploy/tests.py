from django.test import TestCase

# Create your tests here.
import requests

res=requests.get("https://v5-gzb-a.douyinvod.com/2aa0f59bcfbd69941b50e5a6ffe74959/66b157e3/video/tos/cn/tos-cn-ve-15/oof5PjxWRmTjIgEFE1fFPAyDBLIAsE9xKoCAQA/?a=1128&br=537&bt=537&btag=c0000e000ad200&cd=0%7C0%7C0%7C0&cdn_n80=1&ch=0&cquery=100y&cr=0&cs=0&cv=1&dr=0&ds=3&dy_q=1722894678&dy_va_biz_cert=&er=0&feature_id=f0150a16a324336cda5d6dd0b69ed299&ft=rAHInzwwZRd0shPo1PDS6kFgAX1tGDecGf9eF7Hx8Ar12nzXT&l=202408060551181ED63255D91F922DB02B&mime_type=video_mp4&qs=0&rc=ZDQ7aTozNzQ8NzllNmdlZUBpMzZldG45cmhrdDMzNGkzM0AyYS4tYjZeNS4xMGA0Y2IwYSMtc2MwMmRjMmxgLS1kLS9zcw%3D%3D&req_cdn_type=")

print(res.content)

with open('a.mp4','wb') as f:
    
    f.write(res.content)