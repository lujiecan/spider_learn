import urllib.parse as urllib
import urllib.request as urllib2


def write_page(html, filename):
    """
        保持爬取的页面到文件中
        html: 页面数据
        filename: 文件名
    """
    print(f"爬取{filename}完成,正在保存")
    # html是bytes对象，写入文件需要wb，w只能写str对象
    with open(filename, "wb") as f:
        f.write(html)
        print("保存完成")
        print("-" * 50)


def load_page(fullurl, filename):
    """
        根据url发送请求，获取服务器响应内容
        fullurl: 完整的url
        filename: 处理的文件名
    """
    print("-" * 50)
    print(f"开始爬取{filename}...")
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:34.0) Gecko/20100101 Firefox/34.0"}
    request = urllib2.Request(fullurl, headers=headers)
    response = urllib2.urlopen(request)
    return response.read()  # read返回的是bytes对象，不是str对象


def tieba_spider(url, start_page, end_page, keyword):
    """
        贴吧爬虫调度器，负责综合处理要爬取的所有页面的url
        url: 完整url的前面部分
        start_page: 要爬取的开始页
        end_page: 要爬取的结束页
        keyword: 贴吧名字
    """
    for page in range(start_page, end_page + 1):
        pn = (page - 1) * 50
        fullurl = f"{url}&pn={pn}"
        filename = f"{page}页-{keyword}-百度贴吧.html"
        html = load_page(fullurl, filename)
        write_page(html, filename)


def main():
    keyword = input("请输入要爬取的贴吧名：")
    start_page = int(input("请输入要爬取的开始页："))
    end_page = int(input("请输入要爬取的结束页："))

    url = "http://tieba.baidu.com/f?"
    kw = urllib.urlencode({"kw": keyword})
    url += kw

    print(f"开始爬取{keyword}吧第{start_page}页到第{end_page}页。\n")
    tieba_spider(url, start_page, end_page, keyword)
    print("\n全部爬取完成！")


if __name__ == "__main__":
    main()

