# -*- coding: utf-8 -*-
# @Time    : 2023/4/26 21:35
# @Name    : demo1.py
# @email   : liu78103@gmail.com
# @Author  : 刘鑫路
import requests
import execjs

cookies = {
    'Hm_lvt_1521e0fb49013136e79181f2888214a7': '1682513142,1682515916,1682555759',
    'Hm_lpvt_1521e0fb49013136e79181f2888214a7': '1682555759',
    'JSESSIONID': '0202F5A6CFB2D341066804A3C05FA34D',
    '_ACCOUNT_': 'ODM5ZGRlNjYxMDZhNGJiNjg5M2I2ODZkMGY2Yjk4ZWUlNDAlNDBtb2JpbGU6MTY4Mzc2NTM3NDUyNTpkNzY0NjI3N2Y3Y2Q4ZmFmNDgyNWJhNjNiYmEzOWQ3Ng',
}

headers = {
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6,zh-TW;q=0.5',
    'Auth-Plus': '',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    # 'Cookie': 'Hm_lvt_1521e0fb49013136e79181f2888214a7=1682513142,1682515916,1682555759; Hm_lpvt_1521e0fb49013136e79181f2888214a7=1682555759; JSESSIONID=0202F5A6CFB2D341066804A3C05FA34D; _ACCOUNT_=ODM5ZGRlNjYxMDZhNGJiNjg5M2I2ODZkMGY2Yjk4ZWUlNDAlNDBtb2JpbGU6MTY4Mzc2NTM3NDUyNTpkNzY0NjI3N2Y3Y2Q4ZmFmNDgyNWJhNjNiYmEzOWQ3Ng',
    'Origin': 'https://www.hanghangcha.com',
    'Pragma': 'no-cache',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-site',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 Edg/112.0.1722.58',
    'X-Requested-With': 'XMLHttpRequest',
    'clientInfo': 'web',
    'clientVersion': '1.0.0',
    'sec-ch-ua': '"Chromium";v="112", "Microsoft Edge";v="112", "Not:A-Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

params = {
    'filter': '{"city":"","lv":null,"province":"","userId":3500726,"companyId":null,"limit":20,"skip":0,"keyword":null,"companyType":"foreign"}',
}

response = requests.get('https://api.hanghangcha.com/hhc/invest/getProduct', params=params, cookies=cookies, headers=headers)
text = response.json()['data']
js1 = open('./标准库法)数据解密.js', 'r', encoding='utf-8').read()
data = execjs.compile(js1).call('code', text)
print(data)