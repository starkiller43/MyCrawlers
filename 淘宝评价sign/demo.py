# -*- coding: utf-8 -*-
# @Time    : 2023/4/29 20:37
# @Name    : demo.py
# @email   : liu78103@gmail.com
# @Author  : 刘鑫路
import requests
import execjs

cookies = {
    'miid': '6015323462087575869',
    'cna': 'OGQbGgw5fWgCAd3Ash1L4+TW',
    'tracknick': 'tb151883055',
    'enc': 'ccneM8ctMbU494U%2FpM%2FeEn7ciEvJIncLisX3SH4GRJ0WwkJ6XNS6RffjNpoGd4m7YTa%2BTA1EvbSQU0vvpCko9GBsCISq5CZN9P8fi11jiTs%3D',
    'useNativeIM': 'false',
    't': '693ad2b49720b5f8ce439d248b21bc3a',
    '_m_h5_tk': '6abde0e800aeb56ddb6e271c12e1f8ac_1682777601471',
    '_m_h5_tk_enc': '37436dfaea30556515e7de1c8d4ca087',
    '_samesite_flag_': 'true',
    'cookie2': '1ffe898e832425911a3533c5c9c13a68',
    '_tb_token_': 'e6fb11fe1f0eb',
    'xlly_s': '1',
    'sgcookie': 'E100g6c4GEFRwJsCKcmG3ZoLVPSmnt6OuJFGJjrjOYQT6nVWV0dRuKsMlcc3JsOPxYrClR4FA8U2VsEQ2jaZ%2F%2FA91uR6skrrZ2SIkX0AH0dnATU%3D',
    'unb': '2207907202479',
    'uc3': 'lg2=VFC%2FuZ9ayeYq2g%3D%3D&id2=UUphzW5Wcy0zs%2FZQMg%3D%3D&vt3=F8dCsfPhGa8Im78Rq1w%3D&nk2=F5REO%2BkxqWhczCI%3D',
    'csg': '395dd606',
    'lgc': 'tb151883055',
    'cancelledSubSites': 'empty',
    'cookie17': 'UUphzW5Wcy0zs%2FZQMg%3D%3D',
    'dnk': 'tb151883055',
    'skt': '3a3c3b82d16fc9de',
    'existShop': 'MTY4Mjc3MDA2MA%3D%3D',
    'uc4': 'nk4=0%40FY4PaQsDN9wr0Vkqs2TtKg4UIQGWHQ%3D%3D&id4=0%40U2grFnGX65V1XK9Lc4fPwjI%2Bqh5ELViX',
    '_cc_': 'Vq8l%2BKCLiw%3D%3D',
    '_l_g_': 'Ug%3D%3D',
    'sg': '598',
    '_nk_': 'tb151883055',
    'cookie1': 'BxfSnB9FyeStMkyXeiYmtmiBpcAfiy1Q51r7ZatoNNo%3D',
    'mt': 'ci=1_1',
    'thw': 'cn',
    'uc1': 'pas=0&cookie21=VT5L2FSpcHv%2BujM8lw%3D%3D&cookie15=Vq8l%2BKCLz3%2F65A%3D%3D&cookie16=WqG3DMC9UpAPBHGz5QBErFxlCA%3D%3D&existShop=false&cookie14=Uoe8iCYmUh9r3A%3D%3D',
    'l': 'fB_TioZqTj827lQdBOfZourza77TRIRfguPzaNbMi9fPOb5p5S6AW1NQwNL9CnGVEsgDR3-bnsAHB2TTUyzH0xv9-eG2cMptndLnwpzHU',
    'tfstk': 'c-CABLOznuqD_3rMaIeobyov_t4laMuvjqtt66VtQKftFXGEtsxVt6d3s-TwYnUR.',
    'isg': 'BAMDdbcpYyfOcyiZBYfrlzjpkseteJe6_BoX7TXgXmkL9CEWvUjaCm4iaoK61O-y',
}

headers = {
    'authority': 'h5api.m.taobao.com',
    'accept': '*/*',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6,zh-TW;q=0.5',
    'cache-control': 'no-cache',
    # 'cookie': 'miid=6015323462087575869; cna=OGQbGgw5fWgCAd3Ash1L4+TW; tracknick=tb151883055; enc=ccneM8ctMbU494U%2FpM%2FeEn7ciEvJIncLisX3SH4GRJ0WwkJ6XNS6RffjNpoGd4m7YTa%2BTA1EvbSQU0vvpCko9GBsCISq5CZN9P8fi11jiTs%3D; useNativeIM=false; t=693ad2b49720b5f8ce439d248b21bc3a; _m_h5_tk=6abde0e800aeb56ddb6e271c12e1f8ac_1682777601471; _m_h5_tk_enc=37436dfaea30556515e7de1c8d4ca087; _samesite_flag_=true; cookie2=1ffe898e832425911a3533c5c9c13a68; _tb_token_=e6fb11fe1f0eb; xlly_s=1; sgcookie=E100g6c4GEFRwJsCKcmG3ZoLVPSmnt6OuJFGJjrjOYQT6nVWV0dRuKsMlcc3JsOPxYrClR4FA8U2VsEQ2jaZ%2F%2FA91uR6skrrZ2SIkX0AH0dnATU%3D; unb=2207907202479; uc3=lg2=VFC%2FuZ9ayeYq2g%3D%3D&id2=UUphzW5Wcy0zs%2FZQMg%3D%3D&vt3=F8dCsfPhGa8Im78Rq1w%3D&nk2=F5REO%2BkxqWhczCI%3D; csg=395dd606; lgc=tb151883055; cancelledSubSites=empty; cookie17=UUphzW5Wcy0zs%2FZQMg%3D%3D; dnk=tb151883055; skt=3a3c3b82d16fc9de; existShop=MTY4Mjc3MDA2MA%3D%3D; uc4=nk4=0%40FY4PaQsDN9wr0Vkqs2TtKg4UIQGWHQ%3D%3D&id4=0%40U2grFnGX65V1XK9Lc4fPwjI%2Bqh5ELViX; _cc_=Vq8l%2BKCLiw%3D%3D; _l_g_=Ug%3D%3D; sg=598; _nk_=tb151883055; cookie1=BxfSnB9FyeStMkyXeiYmtmiBpcAfiy1Q51r7ZatoNNo%3D; mt=ci=1_1; thw=cn; uc1=pas=0&cookie21=VT5L2FSpcHv%2BujM8lw%3D%3D&cookie15=Vq8l%2BKCLz3%2F65A%3D%3D&cookie16=WqG3DMC9UpAPBHGz5QBErFxlCA%3D%3D&existShop=false&cookie14=Uoe8iCYmUh9r3A%3D%3D; l=fB_TioZqTj827lQdBOfZourza77TRIRfguPzaNbMi9fPOb5p5S6AW1NQwNL9CnGVEsgDR3-bnsAHB2TTUyzH0xv9-eG2cMptndLnwpzHU; tfstk=c-CABLOznuqD_3rMaIeobyov_t4laMuvjqtt66VtQKftFXGEtsxVt6d3s-TwYnUR.; isg=BAMDdbcpYyfOcyiZBYfrlzjpkseteJe6_BoX7TXgXmkL9CEWvUjaCm4iaoK61O-y',
    'pragma': 'no-cache',
    'referer': 'https://h5.m.taobao.com/',
    'sec-ch-ua': '"Chromium";v="112", "Microsoft Edge";v="112", "Not:A-Brand";v="99"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'script',
    'sec-fetch-mode': 'no-cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36 Edg/112.0.1722.64',
}

p = {
    'jsv': '2.7.0',
    'appKey': '12574478',
    't': '1682771791815',
    'sign': 'bc095d23c3ae41905994a12b77ecba41',
    'api': 'mtop.taobao.rate.detaillist.get',
    'v': '5.0',
    'ecode': '1',
    'type': 'jsonp',
    'timeout': '20000',
    'dataType': 'jsonp',
    'sessionOption': 'AutoLoginOnly',
    'jsonpIncPrefix': 'haloMtop',
    'callback': 'mtopjsonphaloMtop5',
    'data': '{"showTrueCount":false,"auctionNumId":"667386832922","rateType":"","searchImpr":"-8","expression":"","orderType":"","pageSize":10,"pageNo":5}',
}

js1 = open('./sign.js', 'r', encoding='utf-8').read()
sign = execjs.compile(js1).call('main', '6abde0e800aeb56ddb6e271c12e1f8ac', p['t'], p['appKey'], p['data'])

params = {
    'jsv': '2.7.0',
    'appKey': '12574478',
    't': '1682771791815',
    'sign': sign,
    'api': 'mtop.taobao.rate.detaillist.get',
    'v': '5.0',
    'ecode': '1',
    'type': 'jsonp',
    'timeout': '20000',
    'dataType': 'jsonp',
    'sessionOption': 'AutoLoginOnly',
    'jsonpIncPrefix': 'haloMtop',
    'callback': 'mtopjsonphaloMtop5',
    'data': p['data'],
}

response = requests.get(
    'https://h5api.m.taobao.com/h5/mtop.taobao.rate.detaillist.get/5.0/',
    params=params,
    cookies=cookies,
    headers=headers,
)
print(response.text)