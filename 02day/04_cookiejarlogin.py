import urllib.parse as urll
import urllib.request as urll2
from http import cookiejar


def main():
    # 创建一个cookiejar对象，用来保持cookie
    cookie = cookiejar.CookieJar()
    # 创建一个HttpCookieProcessor处理器对象,用来处理cookie,参数是上面的cookiejar对象
    cookie_headler = urll2.HTTPCookieProcessor(cookie)
    # 创建自定义opener
    opener = urll2.build_opener(cookie_headler)
    # 通过给opener的addheaders属性赋值，添加自定义http请求头
    opener.addheaders = [("User-Agent", "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.57.2 (KHTML, like Gecko) Version/5.1.7 Safari/534.57.2")]
    # 登录接口
    url = "http://localhost:8080/user/to_login"
    # 登录所需数据，用户名、密码
    formdata = {
        "name": "test",
        "pswd": "123456"
    }
    # 转换成url编码并连接
    data = urll.urlencode(formdata)
    # 创建request对象,data数据需要编码成bytes,headers在opener中已经设置了,这里就不需要了
    login_request = urll2.Request(url, data=data.encode("utf-8"))
    # 发送登录请求，主要是用来获取cookie并保存
    login_res = opener.open(login_request)
    print(login_res.read().decode("utf-8"))

    # 登录请求成功的话，这里就能利用登录后的cookie请求需要登录才能访问的页面
    response = opener.open("http://localhost:8080/user/my_info")
    print(response.read().decode("utf-8"))


if __name__ == "__main__":
    main()

