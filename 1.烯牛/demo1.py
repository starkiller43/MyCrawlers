# -*- coding: utf-8 -*-
# @Time    : 2023/4/26 9:11
# @Name    : demo1.py
# @email   : liu78103@gmail.com
# @Author  : 刘鑫路
import requests
import execjs

cookies = {
    'btoken': 'PUBO04ML4ZUQR2VVOT3VFQ218P6X2734',
    'Hm_lvt_42317524c1662a500d12d3784dbea0f8': '1682471191',
    'hy_data_2020_id': '187bb190326abd-0e7a2c2a4d2e19-7e57547c-1327104-187bb1903279fb',
    'hy_data_2020_js_sdk': '%7B%22distinct_id%22%3A%22187bb190326abd-0e7a2c2a4d2e19-7e57547c-1327104-187bb1903279fb%22%2C%22site_id%22%3A211%2C%22user_company%22%3A105%2C%22props%22%3A%7B%7D%2C%22device_id%22%3A%22187bb190326abd-0e7a2c2a4d2e19-7e57547c-1327104-187bb1903279fb%22%7D',
    'sajssdk_2020_cross_new_user': '1',
    'export_notice': 'true',
    'Hm_lpvt_42317524c1662a500d12d3784dbea0f8': '1682471314',
}

headers = {
    'authority': 'www.xiniudata.com',
    'accept': 'application/json',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6,zh-TW;q=0.5',
    'cache-control': 'no-cache',
    'content-type': 'application/json',
    # 'cookie': 'btoken=PUBO04ML4ZUQR2VVOT3VFQ218P6X2734; Hm_lvt_42317524c1662a500d12d3784dbea0f8=1682471191; hy_data_2020_id=187bb190326abd-0e7a2c2a4d2e19-7e57547c-1327104-187bb1903279fb; hy_data_2020_js_sdk=%7B%22distinct_id%22%3A%22187bb190326abd-0e7a2c2a4d2e19-7e57547c-1327104-187bb1903279fb%22%2C%22site_id%22%3A211%2C%22user_company%22%3A105%2C%22props%22%3A%7B%7D%2C%22device_id%22%3A%22187bb190326abd-0e7a2c2a4d2e19-7e57547c-1327104-187bb1903279fb%22%7D; sajssdk_2020_cross_new_user=1; export_notice=true; Hm_lpvt_42317524c1662a500d12d3784dbea0f8=1682471314',
    'origin': 'https://www.xiniudata.com',
    'pragma': 'no-cache',
    'referer': 'https://www.xiniudata.com/industry/newest?from=data',
    'sec-ch-ua': '"Chromium";v="112", "Microsoft Edge";v="112", "Not:A-Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 Edg/112.0.1722.58',
}

js1 = open('./请求参数获取.js', 'r', encoding='utf-8').read()
canshu = execjs.compile(js1).call('main')
json_data = {
    'payload': canshu['payload'],
    'sig': canshu['sig'],
    'v': 1,
}

response = requests.post(
    'https://www.xiniudata.com/api2/service/x_service/person_industry_list/list_industries_by_sort',
    cookies=cookies,
    headers=headers,
    json=json_data,
).json()['d']

js2 = open('./数据解密.js', 'r', encoding='utf-8').read()
data = execjs.compile(js2).call('main', response)
print(data)

