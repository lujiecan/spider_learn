import urllib.request as urllib2
import urllib.parse as urllib


def main():
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 5.1; U; en; rv:1.8.1) Gecko/20061208 Firefox/2.0.0 Opera 9.50"}
    url = "http://www.baidu.com/s"

    keyword = input("请输入要查询的关键字：")
    wd = {"wd": keyword}
    # 将字典转码并拼接成url查询字符串
    # (中文字符转码，键值用=连接,多个键值对用&拼接)
    # url编码转回中文使用unquote()
    wd = urllib.urlencode(wd)

    fullurl = url + "?" + wd
    print(fullurl)

    # request = urllib2.Request(fullurl, headers=headers)
    # response = urllib2.urlopen(request)
    # print(response.read())


if __name__ == "__main__":
    main()

