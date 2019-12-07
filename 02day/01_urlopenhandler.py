import urllib.request as urllib2


def main():
    # 创建一个httphandler处理器对象，用来发送http请求
    http_handler = urllib2.HTTPHandler()

    # 创建一个自定义opener，传递参数是上面的处理器对象
    opener = urllib2.build_opener(http_handler)

    request = urllib2.Request("http://www.baidu.com")
    # 使用自定义的opener对象发送请求
    response = opener.open(request)

    print(response.getcode())


if __name__ == "__main__":
    main()

