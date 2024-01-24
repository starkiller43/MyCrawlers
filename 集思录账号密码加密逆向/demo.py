# -*- coding: utf-8 -*-
# @Time    : 2023/4/29 15:49
# @Name    : demo.py
# @email   : liu78103@gmail.com

import requests
import execjs

cookies = {
    'kbz_newcookie': '1',
    'kbzw__Session': 'loc35k01i39hdfjf7ec7uv5r60',
    'Hm_lvt_164fe01b1433a19b507595a43bf58262': '1682751791,1682751862,1682752839',
    'Hm_lpvt_164fe01b1433a19b507595a43bf58262': '1682754715',
}

headers = {
    'authority': 'www.jisilu.cn',
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6,zh-TW;q=0.5',
    'cache-control': 'no-cache',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    # 'cookie': 'kbz_newcookie=1; kbzw__Session=loc35k01i39hdfjf7ec7uv5r60; Hm_lvt_164fe01b1433a19b507595a43bf58262=1682751791,1682751862,1682752839; Hm_lpvt_164fe01b1433a19b507595a43bf58262=1682754715',
    'origin': 'https://www.jisilu.cn',
    'pragma': 'no-cache',
    'referer': 'https://www.jisilu.cn/account/login/',
    'sec-ch-ua': '"Chromium";v="112", "Microsoft Edge";v="112", "Not:A-Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 Edg/112.0.1722.64',
    'x-requested-with': 'XMLHttpRequest',
}

info = {
    'user': '17503232528',
    'pwd': '5214833lxl'
}


js1 = open('./getpwd.js', 'r', encoding='utf-8').read()
user = execjs.compile(js1).call('jslencode', info['user'])
pwd = execjs.compile(js1).call('jslencode', info['pwd'])


data = {
    'return_url': 'https://www.jisilu.cn/',
    'user_name': user,
    'password': pwd,
    'auto_login': '1',
    'aes': '1',
}
print(user, pwd)
session =requests.session()
response = session.post('https://www.jisilu.cn/webapi/account/login_process/', cookies=cookies, headers=headers, data=data)
print(response.text)
res = session.get(url='https://www.jisilu.cn/inbox/', headers=headers).text
print(res)
