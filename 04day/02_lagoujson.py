import urllib.request as urllib2
import json
import jsonpath


def main():
    url = "https://www.lagou.com/lbs/getAllCitySearchLabels.json"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/" \
            "537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36",
    }
    request = urllib2.Request(url, headers=headers)
    city_json = urllib2.urlopen(request).read().decode("utf-8")
    # print(city_json)
    # 将json字符串转换成字典类型对象
    city_dict = json.loads(city_json)

    # 用jsonpath解析获取城市名，返回值是列表
    city_names = jsonpath.jsonpath(city_dict, "$..name")

    print(f"总共：{len(city_names)}个城市，前十个是:{city_names[:10]}")


if __name__ == "__main__":
    main()

