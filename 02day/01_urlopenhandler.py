import urllib.request as urllib2


def main():
    # 创建一个httphandler处理器对象，用来发送http请求
    # http_handler = urllib2.HTTPHandler()

    # 在创建httphandler对象时传入参数debuglevel=1，会自动打开debug模式
    # 程序在执行是会自动打印请求信息
    http_handler = urllib2.HTTPHandler(debuglevel=1)

    # 创建一个自定义opener，传递参数是上面的处理器对象
    opener = urllib2.build_opener(http_handler)

    request = urllib2.Request("http://www.baidu.com")
    # 使用自定义的opener对象发送请求
    response = opener.open(request)

    print("-" * 50)
    print(response.getcode())


if __name__ == "__main__":
    main()

