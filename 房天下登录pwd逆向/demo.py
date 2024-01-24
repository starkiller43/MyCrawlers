# -*- coding: utf-8 -*-
# @Time    : 2023/6/2 18:07
# @Name    : demo.py
# @email   : liu78103@gmail.com
# @Author  : 刘鑫路
import requests
import execjs


js1 = open('./pwd.js', 'r', encoding='utf-8').read()
pwd = execjs.compile(js1).call('password', '5214833lxl')

cookies = {
    'global_cookie': '6mdqlfkti3zsow6zyqdwfz2cq22lh31zf91',
    'g_sourcepage': 'txz_dl%5Egg_pc',
    'token': '564c25fed21b46aeb5c4011e4f641160',
    'unique_cookie': 'U_vyw25o1zp9a5wl5byuxa6kfiq5hliedl4ht*3',
}
headers = {
    'Accept': '*/*',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6,zh-TW;q=0.5',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    # 'Cookie': 'global_cookie=6mdqlfkti3zsow6zyqdwfz2cq22lh31zf91; g_sourcepage=txz_dl%5Egg_pc; token=564c25fed21b46aeb5c4011e4f641160; unique_cookie=U_vyw25o1zp9a5wl5byuxa6kfiq5hliedl4ht*3',
    'Origin': 'https://passport.fang.com',
    'Pragma': 'no-cache',
    'Referer': 'https://passport.fang.com/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36 Edg/113.0.1774.57',
    'X-Requested-With': 'XMLHttpRequest',
    'sec-ch-ua': '"Microsoft Edge";v="113", "Chromium";v="113", "Not-A.Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}
data = {
    'uid': '17503232528',
    'pwd': pwd,
    'Service': 'soufun-passport-web',
    'AutoLogin': '1',
}

response = requests.post('https://passport.fang.com/login.api', cookies=cookies, headers=headers, data=data)
print(response.text)