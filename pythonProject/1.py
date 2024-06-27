import requests

proxies = {
    'http': 'http://127.0.0.1:9000',
    'https': 'http://127.0.0.1:9000'
}

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
    'Cookie': '_yep_uuid=ea2c8c82-4b5c-02c5-b9e0-6e19405d3516; newstatisticUUID=1714741497_966209319; fu=40962424; e1=%7B%22l6%22%3A%22%22%2C%22l1%22%3A2%2C%22pid%22%3A%22qd_p_qidian%22%2C%22eid%22%3A%22%22%7D; e2=%7B%22l6%22%3A%22%22%2C%22l1%22%3A2%2C%22pid%22%3A%22qd_p_qidian%22%2C%22eid%22%3A%22%22%7D; _csrfToken=7dec9918-7861-47de-a788-878828e592f9; supportwebp=true; supportWebp=true; ywguid=854050638064; ywkey=ywNvXQmYayGz; ywopenid=F33954FBB9E530D8D0116D07B1D0AECE; traffic_utm_referer=; trkf=1; w_tsfp=ltvgWVEE2utBvS0Q6K7ukEqqHz07Z2R7xFw0D+M9Os09BKQpVZ6B1oJ4vNfldCyCt5Mxutrd9MVxYnGFUd4ifRUTQM6Zb5tH1VPHx8NlntdKRQJtA57bCFFLJOgkvzYTKmhXc0zi2Dp5dtcSz7Zh314M4iYk37ZlCa8hbMFbixsAqOPFm/97DxvSliPXAHGHM3wLc+6C6rgv8LlSgWyEtBu/eRlhAcxD0EaT0iAXCHwk9BPNcuFbNBqtIsiqTe9GuDCFhmCkMcXozBVXpRRV1U1GX6T8j0SZOnRCaUw8IAHml71Qc6uvNuMlvzIRXKpLXFsT4Ehm9bdngBBaDlzLY3aGAP4Mx3IJM/da/7mkDSvE15yYIA8r6aku5C5EzoAZ/WkgOTa1cI8GWmvZZXMPeY0Aa5y7NCoyUUNTXTdM5hUWPHhYC+sjaYee6xekN1ENiuRgP6SodPYGe3WSVPLtAOQ1DzHt85c17RMMDfesFNBSKcELAiCN287+hck=',
}

url = 'https://www.qidian.com/chapter/1031788647/686160165/?ticket=ttRUcKmA8fAc&ywguid=854050638064&ywOpenId=F33954FBB9E530D8D0116D07B1D0AECE'

response = requests.get(url=url,headers=headers,proxies=proxies,verify=False)

print(response.text)

