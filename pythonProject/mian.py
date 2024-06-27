import requests
from bs4 import BeautifulSoup
import re
from DrissionPage import WebPage

proxies = {
    'http': 'http://198.18.0.1:9000',
    'https': 'http://198.18.0.1:9000'
}

wp = WebPage()

# 小说
wp.get('https://www.qidian.com/book/1039141715/')

# 章节url
chapter_elements = wp.eles('xpath://li[@class="chapter-item"]/a')

# chapter_test = wp.ele('xpath://*[@id="chapter-item-783334210"]/a')
# print(chapter_test)

# for e in chapter_elements:
#     print(e.href)

chapter_urls = []

for element in chapter_elements:
    href = element.href
    chapter_urls.append(href)

# for url in chapter_urls:
#     print(url)

# 简介
novel_introduction = wp.ele('css:p#book-intro-detail').text
print(novel_introduction)

# 内容
headers = {
    'Cookie': 'w_tsfp=ltvgWVEE2utBvS0Q6K/rkk6nFzo7Z2R7xFw0D+M9Os09BaAgUpyG1IV4vdfldCyCt5Mxutrd9MVxYnGEVdclfxIdQ8+Zb5tH1VPHx8NlntdKRQJtA87cXlcbJbt9uTAUf2tbcEXhjWh3JdBEyb0221sFsSNw37ZlCa8hbMFbixsAqOPFm/97DxvSliPXAHGHM3wLc+6C6rgv8LlSgW2DugDuLi11A7lK1EGR1C4aG3pV8w2pJbsDal7wcpK9Uv8wrTPzwjn3apCs2RYj4VA3sB49AtX02TXKL3ZEIAtrZUqukO18Lv3wdaN4qzsLXPgaQFkTqgtP4bQ6+UdIXnq+Y3eMVKly4AIER/QP/sm+NA==; Hm_lpvt_f00f67093ce2f38f215010b699629083=1715310226; Hm_lvt_f00f67093ce2f38f215010b699629083=1715265914,1715305781,1715307604,1715307644; _ga=GA1.1.2069852771.1715265918; _ga_FZMMH98S83=GS1.1.1715305795.3.1.1715310225.0.0.0; _ga_PFYW0QLV3P=GS1.1.1715305795.3.1.1715310225.0.0.0; newstatisticUUID=1715305780_1806921029; supportWebp=true; traffic_utm_referer=https%3A%2F%2Fwww.google.com%2F; trkf=1; ywguid=854050638064; ywkey=ywX2DTknxFgk; ywopenid=F33954FBB9E530D8D0116D07B1D0AECE; supportwebp=true; e1=%7B%22l6%22%3A%22%22%2C%22l1%22%3A11%2C%22pid%22%3A%22qd_p_qidian%22%2C%22eid%22%3A%22qd_A117%22%2C%22l2%22%3A2%7D; e2=%7B%22l6%22%3A%22%22%2C%22l1%22%3A6%2C%22pid%22%3A%22qd_p_qidian%22%2C%22eid%22%3A%22qd_A86%22%7D; _yep_uuid=a79c7d4b-1e55-a52c-6425-f8a838ba1695; _csrfToken=f53ee0ca-07ee-4fc0-8330-35d5960ec36f; fu=912732339',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.2 Safari/605.1.15',
}

with open('novel.txt', 'w', encoding='utf-8') as f:
    f.write(novel_introduction + '\n\n')
    for chapter_url in chapter_urls:
        response = requests.get(url=chapter_url, headers=headers, proxies=proxies, verify=False)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')

            chapter_title = soup.find('title').text.strip()
            chapter_title = re.match(r"^(.*?)\s+(\S*)", chapter_title).group(1) + ' ' + re.match(r"^(.*?)\s+(\S*)",
                                                                                                 chapter_title).group(2)

            main_content = soup.find('main')

            paragraphs = main_content.find_all('p')
            chapter_content = ''

            for p in paragraphs:
                chapter_content += p.get_text().strip() + '\n'

            f.write(chapter_title + '\n')
            print(chapter_title)
            f.write(chapter_content + '\n\n')
