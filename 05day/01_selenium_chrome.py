import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def main():
    print("欢迎使用")
    options = Options()
    options.add_argument("--headless")  # 浏览器不提供可视化页面,linux下如果系统不支持可视化不加这条会启动失败
    options.add_argument("--no-sandbox")  # 解决DevToolsActivePort文件不存在的报错
    options.add_argument("--disable-dev-shm-usage")  #在某些VM环境中,/dev/shm分区太小,导致Chrome发生故障或崩溃,使用此标志解决此问题
    options.add_argument('window-size=1920x3000')  # 指定浏览器分辨率
    options.add_argument('--disable-gpu')  # 谷歌文档提到需要加上这个属性来规避bug

    driver = webdriver.Chrome(chrome_options=options)  # 打开浏览器
    print("正在打开百度首页...")
    driver.get("http://www.baidu.com")  # 打开百度
    driver.save_screenshot("baidu.png")  # 截图
    print("正在搜索美女...")
    driver.find_element_by_id("kw").send_keys(u"美女")  # 在搜索框输入“美女”
    driver.find_element_by_id("su").click()  # 点击“百度一下”按钮
    time.sleep(2)  # 等浏览器加载到搜索结果
    driver.save_screenshot("baidu_meinv.png")  # 再次截图
    driver.close()  # 关闭浏览器
    print("运行成功，截图在当前目录，分别是baidu.png、baidu_meinv.png")


if __name__ == "__main__":
    main()

"""
options的全部配置：
    https://peter.sh/experiments/chromium-command-line-switches/
"""

