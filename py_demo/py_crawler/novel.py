import requests,re
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'}
f = open('./text1.txt','a+')
urls=['http://www.doupoxs.com/doupocangqiong/{}.html'.format(str(i)) for i in range(2,3)]
for url in urls:
    res = requests.get(url,headers=headers)
    if res.status_code == 200:
        contents=re.findall('<p>(.*?)</p>',res.content.decode('utf-8'),re.S)
        for content in contents:
            f.write(content+'\n')
    else:
        pass
f.close()
