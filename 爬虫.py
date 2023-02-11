# Author:JackZhang9
# Time: 20230211 1:11
import re
import requests

url='http://www.lg.gov.cn/xxgk/zwgk/tzgg/index.html'

with open('file.txt','a+',encoding='utf-8') as ff:


    for i in range(50):
        r=requests.get(url)
        print(r.status_code)
        res=r.text
        # print(res)
        pat=r'<li><a h(.*?)</li>'
        news=re.findall(pat,re.sub('\n','',res))
        url=re.findall(r'<li><a class="next up" href="(.*?)">下一页</a></li>',re.sub('\n','',res))[0]
        print('当前爬取url：{}'.format(url))
        print(len(news))
        # print(news)

        for new in news:
            news_title=re.findall(r'target="_blank">(.*?)</a><span',new)[0]
            news_date=re.findall(r'class="t">(.*?)</',new)[0]
            news_url=re.findall(r'ref="(.*?)"',new)[0]
            print(news_date,news_title,news_url)
            ff.write(''.join([news_date,news_title,news_url,'\n']))
        print('>第{}页爬取完毕{}'.format(i+1,'>'*50))





