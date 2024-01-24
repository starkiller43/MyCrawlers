# -*- coding: utf-8 -*-
# @Time    : 2023/4/27 8:45
# @Name    : demo.py
# @email   : liu78103@gmail.com
# @Author  : 刘鑫路
import requests
import execjs


json_data = {
    'pageNo': 1,
    'pageSize': 20,
    'total': 0,
    'AREACODE': '',
    'M_PROJECT_TYPE': '',
    'KIND': 'GCJS',
    'GGTYPE': '1',
    'PROTYPE': '',
    'timeType': '6',
    'BeginTime': '2022-10-27 00:00:00',
    'EndTime': '2023-04-27 23:59:59',
    'createTime': [],
    'ts': 1682669987000,
}

js1 = open('./头部参数解密.js', 'r', encoding='utf-8').read()
sign = execjs.compile(js1).call('main', json_data)

cookies = {
    'ASP.NET_SessionId': 'vb2qgksjs2w5nuenxx3mcuoh',
}

headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6,zh-TW;q=0.5',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Content-Type': 'application/json;charset=UTF-8',
    # 'Cookie': 'ASP.NET_SessionId=vb2qgksjs2w5nuenxx3mcuoh',
    'Origin': 'https://ggzyfw.fj.gov.cn',
    'Pragma': 'no-cache',
    'Referer': 'https://ggzyfw.fj.gov.cn/business/list/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 Edg/112.0.1722.58',
    'portal-sign': sign,
    'sec-ch-ua': '"Chromium";v="112", "Microsoft Edge";v="112", "Not:A-Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}



response = requests.post('https://ggzyfw.fj.gov.cn/FwPortalApi/Trade/TradeInfo', cookies=cookies, headers=headers, json=json_data)
text = response.json()['Data']
js2 = open('./数据解密.js', 'r', encoding='utf-8').read()
data = execjs.compile(js2).call('main2', text)
print(data)