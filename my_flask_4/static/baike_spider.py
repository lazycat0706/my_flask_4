import requests
import re
import time

exist_urls = []
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.62 Safari/537.36',
}


def get_link(url):
    try:
        response = requests.get(url=url, headers=headers)
        response.encoding = 'utf-8'
        html = response.text
        link_lists = re.findall('.*?<a target=_blank href="/item/([^:#=<>]*?)".*?</a>', html)
        return link_lists
    except Exception as e:
        pass
    finally:
        exist_urls.append(url)


def main(star_url, depth=1):
    link_lists = get_link(star_url)
    if link_lists:
        unique_lists = list(set(link_lists) - set(exist_urls))
        for unique_url in unique_lists:
            unique_url = 'https://baike.baidu.com/item/' + unique_url

            with open('url.txt', 'a+') as f:
                f.write(unique_url+'\n')
                f.close()

        if depth < 10:
            main(unique_url, depth + 1)


if __name__ == '__main__':
    start_url = 'https://baike.baidu.com/item/%E7%99%BE%E5%BA%A6%E7%99%BE%E7%A7%91'
    main(start_url)
















