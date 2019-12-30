import json
import urllib.request as urllib2
from lxml import etree


class DuanziSpider(object):
    def __init__(self, start=1, end=1):
        """
        初始化爬虫
        start: 要爬取的开始页(默认1)
        end：要爬取的结束页(默认1)
        """
        self.url = "http://www.haoduanzi.com/category/?1-{}.html"
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/" \
                "537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36",
        }
        self.start = start
        self.end = end

    def spider_work(self):
        """
        开始爬取
        """
        for pn in range(self.start, self.end + 1):
            fullurl = self.url.format(pn)
            print(f"\n开始爬取第 {pn} 页...")
            self.load_page(fullurl)

    def load_page(self, url):
        """
        发送请求获取页面
        url：要获取的页面的url
        """
        request = urllib2.Request(url, headers=self.headers)
        html = urllib2.urlopen(request).read().decode("utf-8")
        print("爬取完成，开始解析...")
        self.parse_page(html)

    def parse_page(self, html):
        """
        解析获取到的html源码，获取段子数据
        html: 页面源码
        """
        text = etree.HTML(html)
        node_list = text.xpath('//ul[@class="list-box"]/li[not(@class)]')
        for node in node_list:
            name = node.xpath('./div[@class="head"]/span/text()')
            title = node.xpath('./div[@class="head"]/h2/text()')
            content = node.xpath('string(./div[@class="content"]/a)')
            good = node.xpath('./div[@class="ping-fen"]//a[@class="good"]/span/text()')
            bad = node.xpath('./div[@class="ping-fen"]//a[@class="bad"]/span/text()')
            data = {
                "name": name[0] if name else "",
                "title": title[0] if title else "",
                "content": content,
                "good": good[0][1:-1] if good else "",
                "bad": bad[0][1:-1] if bad else ""
            }
            # print(data)
            self.save_duanzi(data)
        print("解析并保存完成！")


    def save_duanzi(self, data):
        """
        保存段子数据到文件中
        data: 段子数据
        """
        json_data = json.dumps(data, ensure_ascii=False)
        filename = f"duanzi{self.start}-{self.end}.json"
        with open(filename, "a") as f:
            f.write(json_data + "\n")


if __name__ == "__main__":
    print("欢迎使用\n本程序作用：爬取好段子网站的段子，并存为json格式的文件。")
    try:
        start = int(input("请输入要爬取的开始页："))
    except:
        start = 1
    try:
        end = int(input("请输入要爬取的结束页："))
    except:
        end = 1
    spider = DuanziSpider(start, end)
    spider.spider_work()
    print("\n爬取结束，欢迎再次使用！")

