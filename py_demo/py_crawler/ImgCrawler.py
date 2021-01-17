import requests
import re
import os

headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36',
           'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3'}
folder = './img'


def getHTML(url):
    """
    获取HTML页面
    """
    try:
        r = requests.get(url, headers=headers, timeout=30, verify=False)
        r.raise_for_status()  # 如果状态不为200，则抛出异常requests.HTTPError
        r.encoding = r.apparent_encoding
        # r.enconding 从 HTTP header 中猜测的响应内容编码方式
        # r.apparent_enconding   从内容中分析出的响应内容编码方式(备选编码方式)
        return r.text
    except:
        return ''


def parserHTML(html):
    """
    分析HTML获取图片URL
    """
    pattern = r'"picUrl":"(.*?)"'
    urls = re.findall(pattern, html)
    return urls


def downloadIMG(urls):
    """
    下载图片
    """
    if not os.path.exists(folder):
        os.mkdir(folder)
    for url in urls:
        try:
            path = folder+'/'+url.split('/')[-1]
            r = requests.get(url, timeout=30)
            r.raise_for_status()
            r.encoding = r.apparent_encoding
            if not os.path.exists(path):
                with open(path, 'wb') as f:
                    f.write(r.content)
                    f.close()
                    print(path + ' saved')
            else:
                print('File already exist')
        except Exception as e:
            print(e)
            continue


if __name__ == "__main__":
    name = input('Search img name: ')
    num = int(input('Number of download (n*48): '))
    for i in range(num):
        n = num-1 if num == 1 else num*48
        url = 'https://pic.sogou.com/napi/pc/searchList?mode=1&start={n}&xml_len=48&query={name}'.format(
            n=n, name=name)
        html = getHTML(url)
        urls = parserHTML(html)
        downloadIMG(urls)
    print('Done')
    input()
