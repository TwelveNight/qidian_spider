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

for e in chapter_elements:
    print(e.href)