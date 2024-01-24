# -*- coding: utf-8 -*-
# @Time    : 2023/6/5 19:08
# @Name    : demo.py
# @email   : liu78103@gmail.com
# @Author  : 刘鑫路
import execjs
import requests

cookies = {
    'acw_tc': '0b328f2216859629901296922e11da5c39d08f1c0faec91aacf35845c7d762',
    'sensorsdata2015jssdkcross': '%7B%22distinct_id%22%3A%221888587c91a16b2-05b6f944fb6996-7e56547a-1327104-1888587c91b1138%22%2C%22first_id%22%3A%22%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E5%BC%95%E8%8D%90%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC%22%2C%22%24latest_referrer%22%3A%22https%3A%2F%2Fgithub.com%2Fliyf-code%2Freverse_practice%22%7D%2C%22%24device_id%22%3A%221888587c91a16b2-05b6f944fb6996-7e56547a-1327104-1888587c91b1138%22%7D',
}

headers = {
    'authority': 'login.fenbi.com',
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6,zh-TW;q=0.5',
    'cache-control': 'no-cache',
    'content-type': 'application/x-www-form-urlencoded;charset=UTF-8',
    # 'cookie': 'acw_tc=0b328f2216859629901296922e11da5c39d08f1c0faec91aacf35845c7d762; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%221888587c91a16b2-05b6f944fb6996-7e56547a-1327104-1888587c91b1138%22%2C%22first_id%22%3A%22%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E5%BC%95%E8%8D%90%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC%22%2C%22%24latest_referrer%22%3A%22https%3A%2F%2Fgithub.com%2Fliyf-code%2Freverse_practice%22%7D%2C%22%24device_id%22%3A%221888587c91a16b2-05b6f944fb6996-7e56547a-1327104-1888587c91b1138%22%7D',
    'origin': 'https://fenbi.com',
    'pragma': 'no-cache',
    'referer': 'https://fenbi.com/',
    'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Microsoft Edge";v="114"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.37',
}

params = {
    'kav': '100',
    'app': 'web',
    'av': '100',
    'hav': '100',
    'client_context_id': 'e2d14a53bf529836f2aa028c3b1d0047',
}
js1 = open('./password.js', 'r', encoding='utf-8').read()
passwd = execjs.compile(js1).call('get_password', '123456')

data = {
    'password': passwd,
    'persistent': 'true',
    'app': 'web',
    'email': '1371315815@qq.com',
}
print(data)

response = requests.post('https://login.fenbi.com/api/users/loginV2', params=params, cookies=cookies, headers=headers, data=data)

print(response.text)