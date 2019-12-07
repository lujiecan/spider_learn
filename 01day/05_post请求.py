import urllib.parse as urllib
import urllib.request as urllib2

def main():
    url = "http://fanyi.youdao.com/translate"
    key = input("请输入要翻译的字符：")
    formdata = {
        "doctype": "json",
        "type": "AUTO",
        "i": key,
    }
    data = urllib.urlencode(formdata)
    headers = {
        "Content-Type":"application/x-www-form-urlencoded",
        "Host": "fanyi.youdao.com",
        "Connection": "keep-alive",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
        "Accept-Language": "zh-CN,zh;q=0.9",
    }
    # 当有传data参数，请求自动使用post方式，没有就会用get
    request = urllib2.Request(url, data=data.encode("utf-8"), headers=headers)
    response = urllib2.urlopen(request).read().decode("utf-8")
    print(response.strip())


if __name__ == "__main__":
    main()

