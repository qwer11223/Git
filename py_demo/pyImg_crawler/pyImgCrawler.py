import requests
import re
import os


def getHtml(url):
    try:
        path = './img'
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'}
        print('Searching images...')
        response = requests.get(url, timeout=10, headers=headers)  # 超时抛出异常
        html = response.text
        pattern = r'<img.*src="([http|https]\S+)"'
        match = re.findall(pattern, html)  # 提取img标签
        print(match)
        for index, img in enumerate(match):
            response = requests.get(img, timeout=10, headers=headers)
            imgDownload = response.content
            if not os.path.exists(path):
                os.mkdir(path)
            if os.path.exists(path):
                with open(path+'/'+str(index)+'.jpg', 'wb') as f:
                    f.write(imgDownload)
                print('get ' + str(index) + ' pic')
                f.close()
        input('Done!\nPress any key to quit ...')
    except Exception as e:
        print(str(e))
        input('Press any key to quit ...')


if __name__ == "__main__":
    url = input('Enter Url: ')
    getHtml(url)
