from DrissionPage import WebPage

wp = WebPage()
wp.get(
    'https://www.qidian.com/chapter/1039141715/783334210/')

for page in range(30):
    title = wp.ele('css:h1.title').text
    print(title)
    with open('test.txt', mode='a', encoding='utf-8') as f:
        f.write(title + '\n\n')
        all_span = wp.eles('xpath://main//span[@class="content-text"]')
        text = '\n'.join(span.text for span in all_span)
        f.write(text + '\n\n')
        if page == 0:
            wp.run_js(
                'document.querySelector("#reader-content > div.min-h-100vh.relative.z-1.bg-inherit > div > '
                'div.mx-64px.pb-64px.mt-auto > div > a:nth-child(2)").click()'
            )
        else:
            wp.run_js(
                'document.querySelector("#reader-content > div.min-h-100vh.relative.z-1.bg-inherit > div > '
                'div.mx-64px.pb-64px.mt-auto > div > a:nth-child(3)").click()'
            )
