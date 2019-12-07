import urllib.request as urllib2


def main():
    # User-Agent是爬虫和反爬虫的第一步
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 " \
            "(KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36",
    }
    request = urllib2.Request("http://www.baidu.com/", headers=headers)
    response = urllib2.urlopen(request)

    # response返回的内容，是一个类文件对象，除了支持文件的操作方法外，还支持以下方法
    # read方法读取返回文件的所有内容
    # getcode方法获取响应码，geturl方法返回真正响应的url地址（请求的url可能会重定向）
    # info方法获取服务器响应的http报头

    print(response.getcode())
    print('-'*70)
    print(response.info())
    print('-'*70)
    html = response.read()
    print(html.decode("utf-8"))


if __name__ == "__main__":
    main()

