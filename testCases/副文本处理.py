import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait


d = webdriver.Chrome()
d.maximize_window()
d.get('http://10.10.14.84:9000/zentao/user-login.html')


def ele_wait(driver, times, func):
    return WebDriverWait(driver, times).until(func)


user_ele = ele_wait(d, 10, lambda x: x.find_element_by_id('account'))
user_ele.send_keys('tangguobing')
pwd_ele = ele_wait(d, 10, lambda x: x.find_element_by_name('password'))
pwd_ele.send_keys('Ctp#8899')
login_btn = ele_wait(d, 10, lambda x: x.find_element_by_id('submit'))
login_btn.click()

ceShi = ele_wait(d, 10, lambda x: x.find_element_by_link_text('测试'))
ceShi.click()
bug = ele_wait(d, 10, lambda x: x.find_element_by_link_text('Bug'))
bug.click()
create_bug = ele_wait(d, 10, lambda x: x.find_element_by_link_text('提Bug'))
create_bug.click()

product = ele_wait(d, 10, lambda x: x.find_element_by_xpath('//*[@id="product_chosen"]/a/span'))
product.click()
product1 = ele_wait(d, 10, lambda x: x.find_element_by_xpath('//*[@id="product_chosen"]/div/ul/li'))
product1.click()
version = ele_wait(d, 10, lambda x: x.find_element_by_xpath('//*[@id="openedBuild_chosen"]/ul/li/input'))
version.click()
version1 = ele_wait(d, 10, lambda x: x.find_element_by_xpath('//*[@id="openedBuild_chosen"]/div/ul/li'))
version1.click()
title = ele_wait(d, 10, lambda x: x.find_element_by_id('title'))
title.send_keys('这是一条自动化测试Bug')
time.sleep(1)
# severity = ele_wait(d, 10, lambda x: x.find_elements_by_xpath('//*[@id="dataform"]/table/tbody/tr[5]/td/div[2]/div[2]/div/div[1]/button'))
# severity.click()
severity = d.find_elements_by_class_name("caret")[3]
severity.click()
time.sleep(1)
severity1 = ele_wait(d, 10, lambda x: x.find_element_by_class_name('severity2'))
severity1.click()
time.sleep(2)
# 副文本处理-不行
js_text = "[步骤] 先这样，再那样，就行了\n[结果] 结果就这样了\n[期望] 期望是那样的！！！"
js = "document.getElementsByClassName('ke-edit-iframe')[0].contentWindow.document.body.innerHTML='%s'" % js_text
d.execute_script(js)
time.sleep(1)
# f = d.find_element_by_class_name("ke-edit-iframe")
# d.switch_to.frame(f)
# time.sleep(1)
# step = d.find_element_by_xpath('/html/body')
# step.clear()
# time.sleep(1)
# step.send_keys('[步骤] 现这样，在那样，就行了\n[结果] 结果就这样了\n[期望] 期望是那样的')
# time.sleep(2)
# d.switch_to.default_content()
submit = ele_wait(d, 10, lambda x: x.find_element_by_id('submit'))
submit.click()
time.sleep(3)
d.quit()

