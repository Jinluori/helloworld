import  lxml  # 因为需要使用lxml HTML解析库来解析html页面内容，需要安装该模块
import  requests
from bs4 import BeautifulSoup
import time

headers = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36'}

#解析获取的网页
def get_info(url):
    wb_data = requests.get(url, headers=headers)
    soup = BeautifulSoup(wb_data.text, 'lxml')
    ranks = soup.select('span.pc_temp_num')
    titles = soup.select('div.pc_temp_songlist>ul>li>a')
    times = soup.select('span.pc_temp_time')
    for rank, title, time in zip(ranks, titles, times):
        # str1 = title.get_text().split('.')  # 酷狗代码更新，不能用‘.’，需要使用‘-’
        str1 = title.get_text().split('-')
        data = {
            'rank': rank.get_text().strip(),
            # 'songname': str1[0],    # 酷狗代码更新
            'songname': str1[0].strip().ljust(20),
            # 'singer': str1[-1],     # 酷狗代码更新
            'singer': str1[-1].strip().ljust(15),
            'songtime': time.get_text().strip(),
        }
        # print(data)
        f = open('D:/spider/info/songs.txt', 'a+', encoding='utf-8')
        for item in data.items():
            for i in range(len(item)):
                str1 = item[i]
                f.write(str1)
                f.write('\t')
        f.write('\r')
        f.close


if __name__ == '__main__':
    urls = ["https://www.kugou.com/yy/rank/home/{}-8888.html?from=rank".format((str(i))) for i in range(1,30) ]
    for url in urls:
        get_info(url)
        time.sleep(2)

    # down_mp3(data1)
