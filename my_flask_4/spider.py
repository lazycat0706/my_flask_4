import requests


def get_html(keywords):
    headers = {
        "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1",
    }
    response = requests.get("https://www.baidu.com/s?wd={}&rsv_spt=1&rsv_iqid=0x9f603f1b000665af&issp=1&f=8&rsv_bp=1&rsv_idx=2&ie=utf-8&tn=baiduhome_pg&rsv_enter=1&rsv_sug3=9&rsv_sug1=8&rsv_sug7=100&rsv_sug2=0&inputT=3638&rsv_sug4=3638&rsv_sug=2".format(keywords), headers=headers).text
    return response





















