# -*- coding: utf-8 -*-
# @Time    : 2023/4/30 16:59
# @Name    : demo.py
# @email   : liu78103@gmail.com
# @Author  : 刘鑫路
import requests
import execjs

cookies = {
    'routeId': '.uc2',
    'Hm_lvt_489bd07e99fbfc5f12cbb4145adb0a9b': '1682843689',
    'JSESSIONID': '28EB5C825F239E01FD1D5BDD9E2AE273',
    'Hm_lpvt_489bd07e99fbfc5f12cbb4145adb0a9b': '1682845059',
}

js1 = open('./mcode.js', 'r', encoding='utf-8').read()
mcode = execjs.compile(js1).call('main')

headers = {
    'Accept': '*/*',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6,zh-TW;q=0.5',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    # 'Cookie': 'routeId=.uc2; Hm_lvt_489bd07e99fbfc5f12cbb4145adb0a9b=1682843689; JSESSIONID=28EB5C825F239E01FD1D5BDD9E2AE273; Hm_lpvt_489bd07e99fbfc5f12cbb4145adb0a9b=1682845059',
    'Origin': 'http://webapi.cninfo.com.cn',
    'Pragma': 'no-cache',
    'Referer': 'http://webapi.cninfo.com.cn/',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 Edg/112.0.1722.64',
    'X-Requested-With': 'XMLHttpRequest',
    'mcode': mcode,
}

data = {
    'scode': '000001-SZE',
    'sdate': '2022-04-30',
    'edate': '2023-04-30',
    'ctype': '0',
}

response = requests.post(
    'http://webapi.cninfo.com.cn/api/sysapi/p_sysapi1008',
    cookies=cookies,
    headers=headers,
    data=data,
    verify=False,
)
print(response.json())