import urllib.parse as urllib
import urllib.request as urllib2


def main():
    url = "https://movie.douban.com/j/chart/top_list?type=11&interval_id=100%3A90&action="
    formdata = {
        "start": 0,
        "limit": 20
    }
    data = urllib.urlencode(formdata)
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.71 Safari/537.1 LBBROWSER"
    }
    request = urllib2.Request(url, data=data.encode("utf-8"), headers=headers)
    response = urllib2.urlopen(request).read()
    print(response.decode("utf-8"))


if __name__ == "__main__":
    main()

