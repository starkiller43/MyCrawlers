# -*- coding: utf-8 -*-
# @Time    : 2023/4/30 11:27
# @Name    : demo.py
# @email   : liu78103@gmail.com
# @Author  : 刘鑫路
import requests
import execjs
import ddddocr

# def get_code():
#     url = f'https://mp.weixin.qq.com/cgi-bin/verifycode?username={info["uname"]}&r=1682827983893'
#     header = {
#         'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 Edg/112.0.1722.64'
#     }
#     response = requests.get(url=url, headers=header)
#     with open('code.jpg', 'wb') as f:
#         f.write(response.content)
#     code_img = open('code.jpg', 'rb').read()
#     ocr = ddddocr.DdddOcr()
#     res = ocr.classification(code_img)
#     print(res)

cookies = {
    'RK': 'ZviUhGfqNT',
    'ptcz': '415a1cb8614d7650a5cfb44d9454af3941e200837f657304704d4aa6638c1425',
    'pgv_pvid': '1519915250',
    'tvfe_boss_uuid': '1a6de6a82ef8b4db',
    'o_cookie': '1371315815',
    'pac_uid': '1_1371315815',
    'iip': '0',
    'sd_userid': '96341664203372644',
    'ua_id': 'q2KbRL92EoGOCf5ZAAAAACNMk4NmcXEjQzf_GIu441s=',
    'wxuin': '69615854008931',
    'eas_sid': 'k1Z6485212i1f8V6m7Q2L591q1',
    'cert': '_eexmf7W03XU3vNdncmESirjIpDqiq90',
    'sig': 'h012fd8202170fbaafcef56e897c07428408e584954572352903590c42997fd508fd4bb74a3391c966a',
    'uuid': '6ebae2edf89564525ca127d7199473f9',
}

headers = {
    'authority': 'mp.weixin.qq.com',
    'accept': '*/*',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6,zh-TW;q=0.5',
    'cache-control': 'no-cache',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    # 'cookie': 'RK=ZviUhGfqNT; ptcz=415a1cb8614d7650a5cfb44d9454af3941e200837f657304704d4aa6638c1425; pgv_pvid=1519915250; tvfe_boss_uuid=1a6de6a82ef8b4db; o_cookie=1371315815; pac_uid=1_1371315815; iip=0; sd_userid=96341664203372644; ua_id=q2KbRL92EoGOCf5ZAAAAACNMk4NmcXEjQzf_GIu441s=; wxuin=69615854008931; eas_sid=k1Z6485212i1f8V6m7Q2L591q1; cert=_eexmf7W03XU3vNdncmESirjIpDqiq90; sig=h012fd8202170fbaafcef56e897c07428408e584954572352903590c42997fd508fd4bb74a3391c966a; uuid=6ebae2edf89564525ca127d7199473f9',
    'origin': 'https://mp.weixin.qq.com',
    'pragma': 'no-cache',
    'referer': 'https://mp.weixin.qq.com/',
    'sec-ch-ua': '"Chromium";v="112", "Microsoft Edge";v="112", "Not:A-Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 Edg/112.0.1722.64',
    'x-requested-with': 'XMLHttpRequest',
}

params = {
    'action': 'startlogin',
}

info = {
        'uname': '15373505183',
        'passwd': '123456'
    }

js1 = open('./pwd.js', 'r', encoding='utf-8').read()
pwd = execjs.compile(js1).call('main', info['passwd'])

data = {
    'username': info['uname'],
    'pwd': pwd,
    'imgcode': 'OATH',
    'f': 'json',
    'userlang': 'zh_CN',
    'redirect_url': '',
    'token': '',
    'lang': 'zh_CN',
    'ajax': '1',
}

response = requests.post('https://mp.weixin.qq.com/cgi-bin/bizlogin', params=params, cookies=cookies, headers=headers, data=data)
print(response.text)
