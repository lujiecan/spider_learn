import urllib.request as urllib2


def main():
    # 创建一个代理的httphandler对象，参数是字典类型，键是协议名，值是代理服务器的ip和port
    # 私密代理的使用{"http": "账号:密码@ip:port"}
    proxy_http_handler = urllib2.ProxyHandler({"http": "119.57.108.65:53281"})

    opener = urllib2.build_opener(proxy_http_handler)
    # 自定义opener还可以使用urllib2.install_opener方法创建全局的自定义opener
    # 然后直接使用urllib2.urlopen方法就可以了

    request = urllib2.Request("http://www.baidu.com/")

    response = opener.open(request)

    print(response.getcode())


if __name__ == "__main__":
    main()

