import requests
import re
import json
import urllib.request
import time
import os
import shutil
from PIL import Image
from natsort import natsorted

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'
}

search_url = u'https://max.book118.com/search.html?q=2021高职%20大数据技术与应用%20任务书'  # 起始搜索url
base_url = u'https://max.book118.com'
preView_url = u'https://openapi.book118.com/getPreview.html'

current_download_path = ''
total_task = 0
# complete_task = 0


def getSearchList(url):
    # 1.获取搜索列表
    # @return: set()
    res = requests.get(url, headers=headers)
    # with open('1.html', 'w', encoding='utf8') as fp:
    #     fp.write(res.text)
    pages = re.findall(
        r'<a href="(.*)" .* title="2021高职 大数据技术与应用 任务书.*?"', res.text)
    return list(set(pages))


def getPage(url):
    # 2.获取单个页面
    # @return: html
    res = requests.get(url, headers=headers)
    # with open('a.html', 'w', encoding='utf-8') as fp:
    #     fp.write(res.text)
    return res.text


def getParmas(html):

    # 3.获取
    # @return: dict()
    # project_id: 1
    # aid:xxx
    # view_token:xxx
    # page:xxx
    # actual_page:xxx
    params = {
        'project_id': 1,
        'actual_page': re.search(r'actual_page: (\d+)', html).group(1),
        'aid': re.search(r'aid: (3\d+)', html).group(1),
        'view_token': re.search(r"view_token: '(.*?)'", html).group(1)
    }

    title = re.search(r'<title>(.*).*.docx.*</title>', html).group(1)

    return params, title


def getPics(api, params, title):
    # 4.获取pdf图片
    # @return: path(string)
    down_path = ''
    for i in range(1, int(params['actual_page']), 6):
        params['page'] = i
        res = requests.get(api, params=params)
        data = re.search(r'jsonpReturn\((.*?)\)', res.text).group(1)
        json_ = json.loads(data)['data']
        down_path = downloadPics(json_, title)
        time.sleep(3)
    return down_path


def downloadPics(json_data, folder_name):
    # 5.下载图片
    path = 'pics/{}/'.format(folder_name)
    if(not os.path.exists(path)):
        os.makedirs(path)

    for i in json_data.items():
        filepath = path+i[0]+'.png'
        urllib.request.urlretrieve('https:'+i[1], filename=filepath)
        print('getPic: {}'.format(filepath))
    return path


def transToPDF(imgs_path, pdf_path, pdf_name):
    # 6.转换pdf
    if(not os.path.exists(pdf_path)):
        os.makedirs(pdf_path)

    file_save_path = pdf_path+pdf_name
    file_list = os.listdir(imgs_path)
    img_list = []

    file_list = natsorted(file_list)
    img1 = Image.open(os.path.join(imgs_path, file_list[0]))
    file_list.pop(0)

    for i in file_list:
        img = Image.open(os.path.join(imgs_path, i))
        if img.mode == 'RGBA':
            img = img.convert('RGB')
            img_list.append(img)
        else:
            img_list.append(img)
    img1.save(file_save_path, "PDF", resolition=100.0,
              save_all=True, append_images=img_list)
    print('转换完成：'+file_save_path)


def start(search_url):
    urls = getSearchList(search_url)
    total_task = len(urls)
    print('总计任务数: '+'('+str(total_task)+')')
    for i in range(total_task):
        # 遍历请求urls
        print('get: '+base_url+urls[i])

        html = getPage(base_url+urls[i])
        params, title = getParmas(html)

        current_download_path = './pics/'+title
        if(os.path.exists(current_download_path)):
            continue

        # 下载图片
        down_path = getPics(preView_url, params, title)

        print('转换PDF中...')
        transToPDF(down_path, './out/', title+'.pdf')

        time.sleep(5)


if __name__ == "__main__":
    try:
        start(search_url)
    except Exception as e:
        print('Exception: '+e)
        print('delete folder...')
        shutil.rmtree(current_download_path)
        print('retrying...')
        time.sleep(3)
        start(search_url)

    print('complete!')
