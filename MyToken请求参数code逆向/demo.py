# -*- coding: utf-8 -*-
# @Time    : 2023/6/4 10:28
# @Name    : demo.py
# @email   : liu78103@gmail.com
# @Author  : 刘鑫路
import requests
import execjs
import time

headers = {
    'authority': 'api.mytokenapi.com',
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6,zh-TW;q=0.5',
    'cache-control': 'no-cache',
    'content-type': 'application/x-www-form-urlencoded;charset=utf-8',
    'origin': 'https://www.mytokencap.com',
    'pragma': 'no-cache',
    'referer': 'https://www.mytokencap.com/',
    'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Microsoft Edge";v="114"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.37',
}
timestamp = str(int(time.time() * 1000))
js1 = open('./code.js', 'r', encoding='utf-8').read()
code = execjs.compile(js1).call('get_code', timestamp)
params = {
    'pages': '1,1',
    'sizes': '100,100',
    'subject': 'market_cap',
    'language': 'en_US',
    'timestamp': timestamp,
    'code': code,
    'platform': 'web_pc',
    'v': '0.1.0',
    'legal_currency': 'USD',
    'international': '1',
}

response = requests.get('https://api.mytokenapi.com/ticker/currencylistforall', params=params, headers=headers)
print(response.text)