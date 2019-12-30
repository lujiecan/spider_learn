import os
import urllib.request as urllib2
from lxml import etree


class tieba_image_spider(object):
    def __init__(self, start=1, end=1):
        """
        初始化爬虫类
        start: 要爬取的开始页,默认为1
        end：要爬取的结束页,默认为1
        """
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 " \
                "(KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36",
        }
        self.start = start
        self.end = end
        self.url = "https://tieba.baidu.com/f?kw=%E7%BE%8E%E5%A5%B3&pn="

    def work(self):
        """
        开始爬取
        """
        for page in range(self.start-1, self.end):
            pn = page * 50
            full_url = self.url + str(pn)
            self.load_tieba_page(full_url)

    def load_tieba_page(self, url):
        """
        下载贴吧页面，并获取贴子的url
        url: 需要爬取的贴吧页面(贴子列表页)的url
        """
        request = urllib2.Request(url, headers=self.headers)
        try:
            html = urllib2.urlopen(request).read().decode("utf-8")
        except Exception as e:
            print(e)
            return
        # with open("html.html", "w") as f:
            # f.write(html)
        # 数据在页面数据的注释中---》"<!-- ... -->"
        xml = etree.HTML(html)
        data = xml.xpath('//code[@id="pagelet_html_frs-list/pagelet/thread_list"]')
        # 去掉注释符号，再解析
        data = etree.tostring(data[0]).decode("utf-8")
        data = data.replace("<!--", "").replace("-->", "")
        xml = etree.HTML(data)
        url_list = xml.xpath('//a[@class="j_th_tit "]/@href')
        for tiezi_url in url_list:
            tiezi_url = "https://tieba.baidu.com/" + tiezi_url
            print("贴子url:" + tiezi_url)
            self.load_tiezi_page(tiezi_url)

    def load_tiezi_page(self, url):
        """
        下载贴子页面，并获取图片的url
        url: 需要爬取的贴子内容的url
        """
        request = urllib2.Request(url, headers=self.headers)
        try:
            html = urllib2.urlopen(request).read().decode("utf-8")
        except Exception as e:
            print(e)
            return
        # with open("tiezi.html", "w") as f:
            # f.write(html)
        xml = etree.HTML(html)
        other_urls = xml.xpath('//ul[@class="l_posts_num"]//a/@href')  # 贴子内容其他页的链接
        print(f"other_urls: {other_urls}")
        other_urls = set(other_urls)  # 去重

        # 获取本页内容里的图片
        url_list = xml.xpath('//cc//img[@class="BDE_Image"]/@src')
        for image_url in url_list:
            print("图片url:" + image_url)
            self.load_image(image_url)

        n = 1  # 已爬贴子内容页数
        for url in other_urls:  # 爬本帖的其他页
            url = "https://tieba.baidu.com/" + url
            request = urllib2.Request(url, headers=self.headers)
            try:
                html = urllib2.urlopen(request).read().decode("utf-8")
            except Exception as e:
                print(e)
                return
            url_list = xml.xpath('//cc//img[@class="BDE_Image"]/@src')
            for image_url in url_list:
                print("图片url:" + image_url)
                self.load_image(image_url)
            if n > 4:
                break  # 每个贴子最多爬5页
            n += 1

    def load_image(self, url):
        """
        下载贴子里的图片，并保存在本地
        url: 需要下载的图片的url
        """
        request = urllib2.Request(url, headers=self.headers)
        try:
            image_data = urllib2.urlopen(request).read()
        except Exception as e:
            print(e)
            return
        img_name = url[-10:]
        if not os.path.isdir("image"):
            os.mkdir("image")
        with open(f"image/{img_name}", "wb") as f:
            f.write(image_data)


if __name__ == "__main__":
    spider = tieba_image_spider()
    spider.work()


