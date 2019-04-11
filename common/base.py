import os
import time

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select

from common.Logger import Logger


class BasePage(object):
    """
        BlueRose framework are committed to a simpler automated testing,
    based on the original selenium.
    """

    def __init__(self, browser='chrome'):
        """
        Run class initialization method, the default is proper
        to drive the Firefox browser,. Of course, you can also
        pass parameter for other browser, such as Chrome browser for the "Chrome",
        the Internet Explorer browser for "internet explorer" or "ie".
        """
        self.logger = Logger('blueRose.log', level='debug').logger
        if browser == "chrome":
            driver = webdriver.Chrome()
        elif browser == "firefox":
            driver = webdriver.Firefox()
        elif browser == "ie":
            driver = webdriver.Ie()
        try:
            self.driver = driver
        except Exception:
            raise NameError("Not found this browser,You can enter 'firefox', 'chrome', 'ie'.")

    def open(self, url):
        """
        Open url,same as get.

        Usage:
        driver.get("https://www.baidu.com")
        """
        self.driver.get(url)
        self.driver.maximize_window()

    def set_window_size(self, wide, high):
        """
        Set browser window wide and high.

        Usage:
        driver.set_window_size(wide,high)
        """
        self.driver.set_window_size(wide, high)

    def wait(self, seconds):
        """
        Implicitly wait.All elements on the page.

        Usage:
        driver.wait(10)
        """
        self.driver.implicitly_wait(seconds)

    def find_element(self, locator):
        """
        定位元素，参数locator是元组类型
        """
        return WebDriverWait(self.driver, 10, 0.5).until(EC.presence_of_element_located(locator))

    def find_elements(self, locator):
        """
        定位一组元素，参数locator是元组类型。
        返回值是一个列表，通过列表下标访问各个元素
        """
        return WebDriverWait(self.driver, 10, 0.5).until(EC.presence_of_all_elements_located(locator))

    def send_keys(self, locator, text):
        """
        Operation input content after clear.

        Usage:
        driver.send_keys("id=kw","selenium")
        """
        self.find_element(locator).clear()
        self.find_element(locator).send_keys(text)

    def send_keyboards_event(self, locator, key_event):
        """
        Operation send key board event on target.

        Usage:
        driver.send_keyBoardsEvent("id=kw","Keys.ENTER")
        """
        self.find_element(locator).send_keys(key_event)

    def send_keys_index(self, locator, index, text):
        """
        Operation input content after clear.

        Usage:
        driver.send_keys("id=kw",5,"selenium")
        """
        self.find_elements(locator)[index].clear()
        self.find_elements(locator)[index].send_keys(text)

    def click(self, locator):
        """
        It can click any text / image can be clicked
        Connection, check box, radio buttons, and even drop-down box etc..

        Usage:
        driver.click("id=kw")
        """
        self.find_element(locator).click()

    def click_index(self, locator, index):
        """
        It can click any text / image can be clicked
        Connection, check box, radio buttons, and even drop-down box etc..

        Usage:
        driver.click("id=kw",5)
        """
        self.find_elements(locator)[index].click()

    def right_click(self, locator):
        """
        Right click element.

        Usage:
        driver.right_click("class=right")
        """
        ActionChains(self.driver).context_click(self.find_element(locator)).perform()

    def move_to_element(self, locator):
        """
        Mouse over the element.

        Usage:
        driver.move_to_element("css=choose")
        """
        element = self.find_element(locator)
        ActionChains(self.driver).move_to_element(element).perform()

    def move_to_element_index(self, locator, index):
        """
        Mouse over the element.

        Usage:
        driver.move_to_element("css=choose")
        """
        element = self.find_elements(locator)[index]
        ActionChains(self.driver).move_to_element(element).perform()

    def double_click(self, locator):
        """
        Double click element.

        Usage:
        driver.double_click("name=baidu")
        """
        ActionChains(self.driver).double_click(self.find_element(locator)).perform()

    def drag_and_drop(self, source_element, target_element):
        """
        Drags an element a certain distance and then drops it.

        Usage:
        driver.drag_and_drop("id=s","id=t")
        """
        ActionChains(self.driver).drag_and_drop(self.find_element(source_element),
                                                self.find_element(target_element)).perform()

    def back(self):
        """
        Back to old window.

        Usage:
        driver.back()
        """
        self.driver.back()

    def forward(self):
        """
        Forward to old window.

        Usage:
        driver.forward()
        """
        self.driver.forward()

    def get_attribute(self, locator, attribute):
        """
        Gets the value of an element attribute.

        Usage:
        driver.get_attribute("id=kw","attribute")
        """
        return self.find_element(locator).get_attribute(attribute)

    def get_text(self, locator):
        """
        Get element text information.

        Usage:
        driver.get_text("name=johnny")
        """
        return self.find_element(locator).text

    def get_display(self, locator):
        """
        Gets the element to display,The return result is true or false.

        Usage:
        driver.get_display("id=ppp")
        """
        return self.find_element(locator).is_displayed()

    def get_title(self):
        """
        Get window title.

        Usage:
        driver.get_title()
        """
        return self.driver.title

    def get_url(self):
        """
        Get the URL address of the current page.

        Usage:
        driver.get_url()
        """
        return self.driver.current_url

    def get_screenshot_as_base64(self):
        return self.driver.get_screenshot_as_base64()

    def get_screenshot(self):
        """
        Get the current window screenshot.

        Usage:
        driver.get_screenshot()
        """
        current_time = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
        current_date = time.strftime("%Y-%m-%d", time.localtime(time.time()))
        pic_path = os.path.abspath(os.path.dirname(os.getcwd())) + "\\result\\screenshot\\" + current_date
        pic_name = current_time + '.png'
        if os.path.exists(pic_path):
            pass
        else:
            # 创建多层级的文件夹
            os.makedirs(pic_path)
        self.driver.get_screenshot_as_file(pic_path + '\\' + pic_name)
        return pic_path + '\\' + pic_name

    def submit(self, locator):
        """
        Submit the specified form.

        Usage:
        driver.submit("id=mainFrame")
        """
        self.find_element(locator).submit()

    def switch_to_frame(self, locator):
        """
        Switch to the specified frame.

        Usage:
        driver.switch_to_frame("id=mainFrame")
        """
        self.driver.switch_to.frame(self.find_element(locator))

    def switch_to_frame_index(self, index):
        """
        Switch to the specified frame.

        Usage:
        driver.switch_to_frame("id=mainFrame")
        """
        self.driver.switch_to.frame(index)

    def switch_to_frame_out(self):
        """
        Returns the current form machine form at the next higher level.
        Corresponding relationship with switch_to_frame () method.

        Usage:
        driver.switch_to_frame_out()
        """
        self.driver.switch_to.parent_frame()

    def switch_to_default(self):
        """
        Returns the current form machine form at the next higher level.
        Corresponding relationship with switch_to_frame () method.

        Usage:
        driver.switch_to_default()
        """
        self.driver.switch_to.default_content()

    def open_new_window(self):
        """
        Open the new window and switch the handle to the newly opened window.

        Usage:
        driver.open_new_window()
        """
        handles = self.driver.window_handles
        for handle in handles:
            if handle != self.driver.current_window_handle:
                self.driver.switch_to.window(handle)
        # current_windows = self.driver.current_window_handle
        # all_handles = self.driver.window_handles
        # for handle in all_handles:
        #     if handle != current_windows:
        #         self.driver.switch_to.window(handle)
        # handles = self.driver.window_handles
        # self.driver.switch_to.window(handles[len(handles) - 1])

    def F5(self):
        """
        Refresh the current page.

        Usage:
        driver.F5()
        """

        self.driver.refresh()

    def execute_js(self, script):
        """
        Execute JavaScript scripts.

        Usage:
        driver.js("window.scrollTo(200,1000);")
        """
        self.driver.execute_script(script)

    def accept_alert(self):
        """
        Accept warning box.

        Usage:
        driver.accept_alert()
        """
        self.driver.switch_to.alert.accept()

    def dismiss_alert(self):
        """
        Dismisses the alert available.

        Usage:
        driver.dismiss_alert()
        """
        self.driver.switch_to.alert.dismiss()

    def close(self):
        """
        Close the windows.

        Usage:
        driver.close()
        """
        self.driver.close()

    def quit(self):
        """
        Quit the driver and close all the windows.

        Usage:
        driver.quit()
        """
        self.driver.quit()

    def is_text_in_element(self, locator, text):
        try:
            result = WebDriverWait(self.driver, 10, 1).until(EC.text_to_be_present_in_element(locator, text))
            return result
        except:
            return False

    def is_text_in_value(self, locator, text):
        try:
            result = WebDriverWait(self.driver, 10, 1).until(EC.text_to_be_present_in_element_value(locator, text))
            return result
        except:
            return False

    def is_title(self, title):
        try:
            result = WebDriverWait(self.driver, 10, 1).until(EC.title_is(title))
            return result
        except:
            return False

    def is_title_contains(self, title):
        try:
            result = WebDriverWait(self.driver, 10, 1).until(EC.title_is(title))
            return result
        except:
            return False

    def is_selected(self, locator):
        try:
            result = WebDriverWait(self.driver, 10, 1).until(EC.element_located_to_be_selected(locator))
            return result
        except:
            return False

    def is_selected_be(self, locator, is_selected=True):
        try:
            result = WebDriverWait(self.driver, 10, 1).until(EC.element_located_selection_state_to_be(locator, is_selected))
            return result
        except:
            return False

    def is_alert_present(self):
        try:
            result = WebDriverWait(self.driver, 10, 1).until(EC.alert_is_present())
            return result
        except:
            return False

    def is_visibility(self, locator):
        try:
            result = WebDriverWait(self.driver, 10, 1).until(EC.visibility_of_element_located(locator))
            return result
        except:
            return False

    def is_visibility_elements(self, locator):
        try:
            result = WebDriverWait(self.driver, 10, 1).until(EC.visibility_of_all_elements_located(locator))
            return result
        except:
            return False

    def is_invisibility(self, locator):
        try:
            result = WebDriverWait(self.driver, 10, 1).until(EC.invisibility_of_element_located(locator))
            return result
        except:
            return False

    def is_clickable(self, locator):
        try:
            result = WebDriverWait(self.driver, 10, 1).until(EC.element_to_be_clickable(locator))
            return result
        except:
            return False

    def select_by_index(self, locator, index=0):
        element = self.find_element(locator)
        Select(element).select_by_index(index)

    def select_by_value(self, locator, value):
        element = self.find_element(locator)
        Select(element).select_by_value(value)

    def select_by_text(self, locator, text):
        element = self.find_element(locator)
        Select(element).select_by_visible_text(text)

    def scroll_to_top(self):
        js = "window.scrollTo(0, 0)"
        self.driver.execute_script(js)

    def scroll_to_bottom(self):
        js = "window.scrollTo(0, document.body.scrollHeight)"
        self.driver.execute_script(js)

    def js_focus_element(self, locator):
        """聚焦元素"""
        target = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", target)


if __name__ == '__main__':
    driver = BasePage(browser="chrome")
    driver.open("http://www.baidu.com")
    ele1 = ('id', 'kw')
    ele2 = ('id', 'su')
    ele3 = ('xpath', '//*[text()="selenium"]')
    driver.send_keys(ele1, "selenium")  # 该元素位置输入内容
    time.sleep(2)
    driver.click(ele2)
    time.sleep(2)
    driver.click_index(ele3, 5)  # 点击元素
    time.sleep(2)
    driver.F5()  # 刷新页面
    driver.get_screenshot()  # 截图
    time.sleep(2)
    driver.back()  # 后退
    print(driver.get_title())
    time.sleep(2)
    driver.forward()  # 前进
    driver.close()
