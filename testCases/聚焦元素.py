import time
from selenium import webdriver


d = webdriver.Chrome()
d.get("https://www.booktxt.net/")


# 聚焦元素
def js_focus(locator):

    target = d.find_elements_by_xpath(locator)[1]
    time.sleep(1)
    d.execute_script("arguments[0].scrollIntoView();", target)
    time.sleep(2)


js1 = "window.scrollTo(0, document.body.scrollHeight)"
# 底部
d.execute_script(js1)
time.sleep(2)
# 顶部
js2 = "window.scrollTo(0, 0)"
# 右边
d.execute_script(js2)
time.sleep(2)
js3 = "window.scrollTo(document.body.scrollWidth, 0)"
time.sleep(3)
d.quit()
