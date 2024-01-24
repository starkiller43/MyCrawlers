# -*- coding: utf-8 -*-
# @Time    : 2023/4/29 11:14
# @Name    : demo.py
# @email   : liu78103@gmail.com
# @Author  : 刘鑫路
import requests
import execjs

js1 = open('./进制数据逆向.js', 'r', encoding='utf-8').read()
bdata = execjs.compile(js1).call('main')
data = bytes(bdata['data'])
print(data)

cookies = {
    'JSESSIONID': 'DB6EBB1A03FCCFE42B714325C978BB96',
}

headers = {
    'Connection': 'keep-alive',
    'Accept': 'application/json, text/plain, */*',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36',
    'Content-Type': 'application/octet-stream',
    'Origin': 'http://www.spolicy.com',
    'Accept-Language': 'en,zh;q=0.9,en-GB;q=0.8,en-US;q=0.7,zh-CN;q=0.6',
    # 'Cookie': 'JSESSIONID=DB6EBB1A03FCCFE42B714325C978BB96',
}



response = requests.post(
    'http://www.spolicy.com/info_api/policyType/showPolicyType',
    cookies=cookies,
    headers=headers,
    data=data,
    verify=False,
)
print(response.json())