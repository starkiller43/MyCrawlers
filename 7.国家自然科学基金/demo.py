# -*- coding: utf-8 -*-
# @Time    : 2023/11/19 13:26
# @Name    : demo.py
# @email   : liu78103@gmail.com

import time
import requests
import execjs
import csv


def get_data():
    page = 0
    while True:
        json_data = {
            'code': 'G01',
            'fuzzyKeyword': '',
            'complete': True,
            'isFuzzySearch': False,
            'conclusionYear': '2020',
            'dependUnit': '',
            'keywords': '',
            'pageNum': page,
            'pageSize': 10,
            'personInCharge': '',
            'projectName': '',
            'projectType': '218',
            'subPType': '',
            'psPType': '',
            'ratifyNo': '',
            'ratifyYear': '',
            'order': 'enddate',
            'ordering': 'desc',
            'codeScreening': '',
            'dependUnitScreening': '',
            'keywordsScreening': '',
            'projectTypeNameScreening': '',
        }
        response = requests.post('https://kd.nsfc.gov.cn/api/baseQuery/completionQueryResultsData', headers=headers, json=json_data).text
        js1 = open('./decrypt.js', 'r', encoding='utf-8').read()
        result = execjs.compile(js1).call('main', response)
        datas = result['data']['resultsData']
        if len(datas) != 0:
            save_data(datas)
            page += 1
        else:
            break


def save_data(datas):
    for data in datas:
        time.sleep(1)
        title = data[1]
        infopage = f'https://kd.nsfc.gov.cn/api/baseQuery/conclusionProjectInfo/{data[0]}'
        json_reslut = requests.post(url=infopage, headers=headers).json()
        projectAbstractC = json_reslut['data']['projectAbstractC']
        data_list = [title, projectAbstractC]
        print(data_list)
        csv_writer.writerow(data_list)


if __name__ == '__main__':
    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'Authorization': 'Bearer undefined',
        'Connection': 'keep-alive',
        'Content-Type': 'application/json;charset=UTF-8',
        'Origin': 'https://kd.nsfc.gov.cn',
        'Referer': 'https://kd.nsfc.gov.cn/finalProjectInit?advanced=true',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 Edg/119.0.0.0',
        'sec-ch-ua': '"Microsoft Edge";v="119", "Chromium";v="119", "Not?A_Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }
    f = open('data.csv', mode='a', encoding='utf-8-sig', newline='')
    columns = ['标题', '中文摘要']
    csv_writer = csv.writer(f)
    csv_writer.writerow(columns)
    get_data()
    f.close()
