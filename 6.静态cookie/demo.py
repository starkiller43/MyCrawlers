# -*- coding: utf-8 -*-
# @Time    : 2023/4/30 21:28
# @Name    : demo.py
# @email   : liu78103@gmail.com
# @Author  : 刘鑫路
import requests
import execjs

js1 = open('./cookie.js', 'r', encoding='utf-8').read()
ck = execjs.compile(js1).call('main')

headers = {
    'authority': 'www.ontariogenomics.ca',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6,zh-TW;q=0.5',
    'cache-control': 'no-cache',
    'cookie': ck,
    'pragma': 'no-cache',
    'sec-ch-ua': '"Chromium";v="112", "Microsoft Edge";v="112", "Not:A-Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 Edg/112.0.1722.64',
}

response = requests.get('https://www.ontariogenomics.ca/news-events/', headers=headers).text
print(response)