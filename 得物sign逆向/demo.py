# -*- coding: utf-8 -*-
# @Time    : 2023/6/5 21:06
# @Name    : demo.py
# @email   : liu78103@gmail.com
# @Author  : 刘鑫路
import execjs
import requests

cookies = {
    'sajssdk_2015_cross_new_user': '1',
    'sensorsdata2015jssdkcross': '%7B%22distinct_id%22%3A%221888b8407d247e-0f4b2646ef7ec58-7e56547a-1327104-1888b8407d317b7%22%2C%22first_id%22%3A%22%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E5%BC%95%E8%8D%90%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC%22%2C%22%24latest_referrer%22%3A%22https%3A%2F%2Fgithub.com%2F%22%7D%2C%22identities%22%3A%22eyIkaWRlbnRpdHlfY29va2llX2lkIjoiMTg4OGI4NDA3ZDI0N2UtMGY0YjI2NDZlZjdlYzU4LTdlNTY1NDdhLTEzMjcxMDQtMTg4OGI4NDA3ZDMxN2I3In0%3D%22%2C%22history_login_id%22%3A%7B%22name%22%3A%22%22%2C%22value%22%3A%22%22%7D%2C%22%24device_id%22%3A%221888b8407d247e-0f4b2646ef7ec58-7e56547a-1327104-1888b8407d317b7%22%7D',
}

headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6,zh-TW;q=0.5',
    'AppId': 'h5',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Content-Type': 'application/json',
    # 'Cookie': 'sajssdk_2015_cross_new_user=1; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%221888b8407d247e-0f4b2646ef7ec58-7e56547a-1327104-1888b8407d317b7%22%2C%22first_id%22%3A%22%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E5%BC%95%E8%8D%90%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC%22%2C%22%24latest_referrer%22%3A%22https%3A%2F%2Fgithub.com%2F%22%7D%2C%22identities%22%3A%22eyIkaWRlbnRpdHlfY29va2llX2lkIjoiMTg4OGI4NDA3ZDI0N2UtMGY0YjI2NDZlZjdlYzU4LTdlNTY1NDdhLTEzMjcxMDQtMTg4OGI4NDA3ZDMxN2I3In0%3D%22%2C%22history_login_id%22%3A%7B%22name%22%3A%22%22%2C%22value%22%3A%22%22%7D%2C%22%24device_id%22%3A%221888b8407d247e-0f4b2646ef7ec58-7e56547a-1327104-1888b8407d317b7%22%7D',
    'Origin': 'https://m.poizon.com',
    'Pragma': 'no-cache',
    'Referer': 'https://m.poizon.com/',
    'SK': '9MHVJyB4AEVUPZE5z00WPc3C2LYHJBltkjiMGjP1ib1WGVeaVtlM6evhdexVyCIvCch5aGZl2dhLwaNtDL0U6MNM6L1s',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-site',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Mobile Safari/537.36 Edg/114.0.1823.37',
    'appVersion': '5.19.0',
    'ltk': 'DcKjwrbDgMO5NcO1w6bCq8KUJcKnw6rCpMOoUMOmwpfCkcKnPjrCnnrDnsOnXcOHLQTCvnPDmyfCtcOHwq8ZB8OpNW7CrsKHwqfCjsO4w7nDnsOJ',
    'platform': 'h5',
    'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Microsoft Edge";v="114"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sessionid': 'woltmp11-4qft-5lce-gmno-k5tz34njh33wvcxp',
    'shumeiId': 'BeNC3MJ8gGmOrU1D5mBCJWDfMacNvJVJcRG3jr9WZlQUXzA5KwUgivpQRqTm+ycT8p7rzzTae2fxV33oCbc53Mg==',
}

js1 = open('sign.js', 'r', encoding='utf-8').read()
sign = execjs.compile(js1).call('get_sign')

json_data = {
    'sign': sign,
    'tabId': '',
    'limit': 20,
    'lastId': 2,
    'platform': 'h5',
    'version': '4.73.0',
    'isVisitor': False,
    'newAdvForH5': True,
}

response = requests.post('https://app.poizon.com/api/v1/h5/index/fire/index', cookies=cookies, headers=headers, json=json_data)
print(response.text)
