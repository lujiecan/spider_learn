import requests
import hashlib
from bs4 import BeautifulSoup


def main():
    # 创建一个session对象，可以保持cookies
    sess = requests.Session()
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/" \
            "537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36",
    }
    # 获取登录页面，找到需要post的数据(csrfmiddlewaretoken), 同时会记录当前网页的cookie值
    html = sess.get("http://lujiecan.me/user/login", headers=headers).text
    # 调用lxml解析库
    bs = BeautifulSoup(html, "lxml")
    # 获取之前get的页面里的csrfmiddlewaretoken值
    csrf = bs.find("input", attrs={"name": "csrfmiddlewaretoken"}).get("value")
    # print(csrf)
    formdata = {
        "csrfmiddlewaretoken": csrf,
        "name": "123",
        "pswd": hashlib.sha1("000000".encode("utf-8")).hexdigest()
    }
    resp = sess.post("http://lujiecan.me/user/to_login", headers=headers, data=formdata).text
    # print(resp)
    user_info_page = sess.get("http://lujiecan.me/user/my_info", headers=headers).text
    print(user_info_page)


if __name__ == "__main__":
    main()

