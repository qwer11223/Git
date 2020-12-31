from lxml import etree
import requests
import csv

with open('./book.csv', 'wt', newline='', encoding='utf-8') as fp:
    i=0
    writer = csv.writer(fp)
    writer.writerow(('name', 'url', 'author', 'publisher',
                     'date', 'price', 'rate', 'comment'))
    urls = [
        'https://book.douban.com/top250?start={}'.format(str(i)) for i in range(0, 250, 25)]
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'}
    for url in urls:
        html = requests.get(url, headers=headers)
        selector = etree.HTML(html.text)
        infos = selector.xpath('//tr[@class="item"]')
        for index, info in enumerate(infos):
            i+=1
            print('get {} info ...'.format(str(i)))
            name = info.xpath('td/div/a/@title')[0]
            url = info.xpath('td/div/a/@href')[0]
            book_infos = info.xpath('td/p/text()')[0]
            temp = book_infos.split('/')
            author = temp[0]
            publisher = temp[-3]
            date = temp[-2]
            price = temp[-1]
            rate = info.xpath('td/div/span[2]/text()')[0]
            comments = info.xpath('/ td/p/span/text()')
            comment = comments[0] if len(comments) != 0 else 'null'
            writer.writerow((name, url, author, publisher,
                             date, price, rate, comment))
input('Done!')
fp.close()
