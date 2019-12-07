import urllib.request as urllib2


def main():
    name = "test"
    pswd = "123456"
    webserver = "192.168.78.1"

    # 很少用到这种情况
    # 创建一个密码管理对象，用来保存和http请求相关的授权账号信息
    pswd_mgr = urllib2.HTTPPasswordMgrWithPriorAuth()
    # 添加一个账号授权信息，第一个参数realm（域）如果没有就天None，然后依次是站点ip，用户名，密码
    pswd_mgr.add_password(None, webserver, name, pswd)

    # http基础验证处理器类
    http_auth_handler = urllib2.HTTPBasiAuthHandler(pswd_mgr)
    # 代理基础验证处理器类,(代理验证用ProxyHandler({"http":"user:pswd@ip:port"})更方便)
    proxy_auth_handler = urllib2.ProxyBasicAuthHandler(pswd_mgr)

    # build_opener可以添加多个处理器
    opener = urllib2.build_opener(http_auth_handler, proxy_auth_handler)
    request = urllib2.Request(f"http://{webserver}")
    response = opener.open(request)
    print(response.read())


if __name__ == "__main__":
    main()

