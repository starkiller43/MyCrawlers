# -*- coding: utf-8 -*-
# @Time    : 2023/4/28 19:50
# @Name    : demo.py
# @email   : liu78103@gmail.com
# @Author  : 刘鑫路
import requests
import execjs

js1 = open('./参数逆向.js', 'r', encoding='utf-8').read()
hexin = execjs.compile(js1).call('hexin')

cookies = {
    'ta_random_userid': 'yndmt2583b',
    'cid': 'c7939b56751fad9709451730602572c61658891262',
    'ComputerID': 'c7939b56751fad9709451730602572c61658891262',
    'WafStatus': '0',
    'other_uid': 'Ths_iwencai_Xuangu_r1kpnlh6hmb2idr12lpnhpwe2p3mgxt6',
    'wencai_pc_version': '1',
    'v': hexin,
}

headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6,zh-TW;q=0.5',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Content-Type': 'application/json',
    # 'Cookie': 'ta_random_userid=yndmt2583b; cid=c7939b56751fad9709451730602572c61658891262; ComputerID=c7939b56751fad9709451730602572c61658891262; WafStatus=0; other_uid=Ths_iwencai_Xuangu_r1kpnlh6hmb2idr12lpnhpwe2p3mgxt6; wencai_pc_version=1; v=A5Gkf533keuziv3_UNDhupdboJYu_gcxr3OphHMmjsZ3Pb_Iu04VQD_CuUUA',
    'Origin': 'http://www.iwencai.com',
    'Pragma': 'no-cache',
    'Referer': 'http://www.iwencai.com/unifiedwap/result?w=5g&querytype=stock&addSign=1682682629983',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 Edg/112.0.1722.58',
    'hexin-v': hexin,
}

json_data = {
    'source': 'Ths_iwencai_Xuangu',
    'version': '2.0',
    'query_area': '',
    'block_list': '',
    'add_info': '{"urp":{"scene":1,"company":1,"business":1,"is_lowcode":1},"contentType":"json","searchInfo":true}',
    'question': '5g',
    'perpage': '100',
    'page': 1,
    'secondary_intent': 'stock',
    'log_info': '{"input_type":"typewrite"}',
    'rsh': 'Ths_iwencai_Xuangu_r1kpnlh6hmb2idr12lpnhpwe2p3mgxt6',
}

response = requests.post(
    'http://www.iwencai.com/customized/chart/get-robot-data',
    cookies=cookies,
    headers=headers,
    json=json_data,
    verify=False,
)
print(response.json())