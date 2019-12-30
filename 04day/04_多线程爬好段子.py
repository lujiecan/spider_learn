import json
import threading
import requests
from lxml import etree
from queue import Queue


# 表示所有采集线程是否结束(采集结束、解析才能结束)
CRAWL_END = False


class ThreadCrawl(threading.Thread):
    def __init__(self, name, page_queue, data_queue):
        super().__init__()
        self.name = name
        self.page_queue = page_queue
        self.data_queue = data_queue
        self.url = "http://www.haoduanzi.com/category/?1-{}.html"
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/" \
                "537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36",
        }

    def run(self):
        print(f"{self.name}开始工作...")
        while True:
            try:
                pn = self.page_queue.get(False)  # False表示不堵塞
            except:
                break
            else:
                print(f"{self.name}正在采集第{pn}页...")
                fullurl = self.url.format(pn)
                html = requests.get(url=fullurl, headers=self.headers)
                self.data_queue.put(html.text)
        print(f"{self.name}结束。")


class ParseThread(threading.Thread):
    def __init__(self, name, data_queue):
        super().__init__()
        self.name = name
        self.data_queue = data_queue

    def run(self):
        print(f"{self.name}开始工作...")
        while not (CRAWL_END and self.data_queue.empty()):
            try:
                html = self.data_queue.get(False)
            except:
                pass
            else:
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
                    json_data = json.dumps(data, ensure_ascii=False)
                    filename = "duanzi_多线程爬取.json"
                    with open(filename, "a") as f:
                        f.write(json_data + "\n")
        print(f"{self.name}结束。")


def main():
    global CRAWL_END
    # 页码的队列，10表示队列中最多有10个对象
    page_queue = Queue(10)
    for i in range(1, 11):
        page_queue.put(i)
    # 爬取下来的数据(页面)队列,不传值表示不限制队列里对象的个数
    data_queue = Queue()

    # 采集线程列表
    crawl_threads = []
    # 采集线程名字列表
    crawl_list = [f"采集线程{n}号" for n in range(1, 4)]
    for crawl_name in crawl_list:
        thread = ThreadCrawl(crawl_name, page_queue, data_queue)
        thread.start()
        crawl_threads.append(thread)

    # 解析线程名字
    parse_list = [f"解析线程{n}号" for n in range(1, 4)]
    for parse_name in parse_list:
        thread = ParseThread(parse_name, data_queue)
        thread.start()

    for th in crawl_threads:
        th.join()
    CRAWL_END = True


if __name__ == "__main__":
    main()

