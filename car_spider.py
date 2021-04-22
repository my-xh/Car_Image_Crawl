# -*- coding: utf-8 -*-

"""
@File    : car_spider.py
@Time    : 2021/4/22 22:31
@Author  : my-xh
@Version : 1.0
@Software: PyCharm
@Desc    : 用于爬取汽车图片
"""

import os
import time
import requests

from bs4 import BeautifulSoup
from itertools import count

CHUNK_SIZE = 512 * 1024


class CarSpider():
    """汽车图片爬虫类"""

    def __init__(self):
        self.cwd = os.getcwd()  # 获取当前工作目录
        self.urls = [
            'https://car.autohome.com.cn/pic/series-s32890/385-1.html#pvareaid=2042222',  # 车身外观
            'https://car.autohome.com.cn/pic/series-s32890/385-10.html#pvareaid=2042222',  # 中控方向盘
            'https://car.autohome.com.cn/pic/series-s32890/385-3.html#pvareaid=2042222',  # 车厢座椅
            'https://car.autohome.com.cn/pic/series-s32890/385-12.html#pvareaid=2042222',  # 其他细节
        ]
        self.session = requests.Session()
        self.session.headers.update({
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36',
        })

    def get_img(self):
        """获取汽车图片"""
        start = time.time()

        for img, title, num in self.__crawl_strategy():
            self.__download(img, title, num)

        end = time.time()
        print(f'run time: {end - start}')

    def __crawl_strategy(self):
        """爬取策略"""
        for url in self.urls:
            response = self.session.get(url)
            soup = BeautifulSoup(response.text, 'html.parser')
            root = soup.find('div', class_='uibox-con carpic-list03 border-b-solid')
            title = soup.find('div', class_="cartab-title").next_sibling.div.text
            title = title[:title.index('(')].strip()
            num = count()
            for img in root.find_all('img'):
                yield ('https:' + img.get('src'), title, next(num))

    def __download(self, img, title, num):
        """下载图片"""
        dir_name = os.path.join(self.cwd, f'car/{title}').replace('/', '\\')
        if not os.path.exists(dir_name):
            os.makedirs(dir_name)

        _, img_ext = os.path.splitext(img)
        img_name = os.path.join(dir_name, f'{num}{img_ext}').replace('/', '\\')
        response = self.session.get(img)
        print(f'正在下载{img_name}...')
        with open(img_name, 'wb') as f:
            for chunk in response.iter_content(chunk_size=CHUNK_SIZE):
                if not chunk:
                    break
                f.write(chunk)


if __name__ == '__main__':
    spider = CarSpider()
    spider.get_img()
