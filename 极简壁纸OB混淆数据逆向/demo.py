# -*- coding: utf-8 -*-
# @Time    : 2023/4/30 15:35
# @Name    : demo.py
# @email   : liu78103@gmail.com
# @Author  : 刘鑫路
import requests
import execjs
import time

# headers = {
#     'authority': 'api.zzzmh.cn',
#     'accept': 'application/json, text/plain, */*',
#     'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6,zh-TW;q=0.5',
#     'cache-control': 'no-cache',
#     'content-type': 'application/json;charset=UTF-8',
#     'origin': 'https://bz.zzzmh.cn',
#     'pragma': 'no-cache',
#     'referer': 'https://bz.zzzmh.cn/',
#     'sec-ch-ua': '"Chromium";v="112", "Microsoft Edge";v="112", "Not:A-Brand";v="99"',
#     'sec-ch-ua-mobile': '?0',
#     'sec-ch-ua-platform': '"Windows"',
#     'sec-fetch-dest': 'empty',
#     'sec-fetch-mode': 'cors',
#     'sec-fetch-site': 'same-site',
#     'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 Edg/112.0.1722.64',
# }
#
# json_data = {
#     'size': 24,
#     'current': 5,
#     'sort': 0,
#     'category': 0,
#     'resolution': 0,
#     'color': 0,
#     'categoryId': 0,
#     'ratio': 0,
# }
#
# response = requests.post('https://api.zzzmh.cn/bz/v3/getData', headers=headers, json=json_data)
#
# js1 = open('./数据解密.js', 'r', encoding='utf-8').read()
# data = execjs.compile(js1).call('main', response.json()['result'])

data = {'currPage': 5, 'list': [{'t': 2, 'w': 1920, 'h': 1200, 'i': '83eec0c90f224797aeb170cd11e6ce76'}, {'t': 2, 'w': 1920, 'h': 1091, 'i': 'de215fabe5044929852c9ce2253724c0'}, {'t': 2, 'w': 1920, 'h': 1081, 'i': '96b26df8437c44e899f67d2fee4777ae'}, {'t': 2, 'w': 3500, 'h': 2333, 'i': 'bc999d1fff264a6a85a752ec710dfe44'}, {'t': 1, 'w': 2560, 'h': 1600, 'i': '09701ebe9fd9496eb7e41400d00d097a'}, {'t': 1, 'w': 1920, 'h': 1080, 'i': 'b60f5da1df784e92bdb27706227eea4a'}, {'t': 2, 'w': 4096, 'h': 1756, 'i': '0e060445cc5849989801026120ebf3c7'}, {'t': 2, 'w': 1920, 'h': 1080, 'i': '4439c0327c1e4092a2bf397deb56933d'}, {'t': 2, 'w': 1920, 'h': 1080, 'i': '9c3a2c7029a9450c95cbfbf6912f5c0a'}, {'t': 2, 'w': 3840, 'h': 2160, 'i': '4967c5536daa47528ca92e5d599c30e3'}, {'t': 2, 'w': 1920, 'h': 1080, 'i': '73b623986ee14859bb7a3c7850223e3d'}, {'t': 2, 'w': 2560, 'h': 1440, 'i': '6e501611880511ebb6edd017c2d2eca2'}, {'t': 2, 'w': 1920, 'h': 1080, 'i': '25448d9b7f114fd9ac3730cf6f83c95d'}, {'t': 2, 'w': 3607, 'h': 2550, 'i': '32268e96a5734b158b6ad29bb9aa6d0d'}, {'t': 1, 'w': 1920, 'h': 1080, 'i': '76bbb6e9e2c8448089eea969e1a7c479'}, {'t': 2, 'w': 2557, 'h': 1535, 'i': '759a476599af41a7a9e79cbfcc577026'}, {'t': 2, 'w': 7680, 'h': 4320, 'i': '4dd06e4787714b08a2d56b5528569a67'}, {'t': 2, 'w': 3840, 'h': 2160, 'i': '6b522359092f4f48a1168e482085ce7a'}, {'t': 2, 'w': 1920, 'h': 1231, 'i': '6a03a373f9cf4607989f770f784b6a68'}, {'t': 1, 'w': 2560, 'h': 1440, 'i': '6488824910784e05bfcf59a207a87829'}, {'t': 2, 'w': 5472, 'h': 3648, 'i': 'e13eb4c9704e4fada3fb261a6ba6327e'}, {'t': 2, 'w': 1500, 'h': 1022, 'i': 'f7b45c9a0b794c789877e1d687d4ef76'}, {'t': 2, 'w': 1920, 'h': 1248, 'i': '04fee98caa1445c4a4e5a6b8f726d3ad'}, {'t': 2, 'w': 1920, 'h': 1080, 'i': 'f67bb9ab6192415ea13beda6e2d99c7b'}], 'number': 1684080000, 'pageSize': 24, 'totalCount': 41584, 'totalPage': 1733}

for i in data['list']:
    url = f'https://api.zzzmh.cn/bz/v3/getUrl/{i["i"]}21'
    x = time.time()
    cookies = {
        'Hm_lvt_7a0674d0cd558ae070889291eef84e9a': f'{int(x)}',
        'Hm_lpvt_7a0674d0cd558ae070889291eef84e9a': f'{int(x)}',
    }
    headers = {
        'authority': 'api.zzzmh.cn',
        'accept': 'image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8',
        'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6,zh-TW;q=0.5',
        'cache-control': 'no-cache',
        # 'cookie': 'Hm_lvt_7a0674d0cd558ae070889291eef84e9a=1682852693; Hm_lpvt_7a0674d0cd558ae070889291eef84e9a=1682852693',
        'pragma': 'no-cache',
        'referer': 'https://bz.zzzmh.cn/',
        'sec-ch-ua': '"Chromium";v="112", "Microsoft Edge";v="112", "Not:A-Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'image',
        'sec-fetch-mode': 'no-cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 Edg/112.0.1722.64',
    }

    response = requests.get(
        url=url,
        cookies=cookies,
        headers=headers,
    )
    print(response.headers)


    break