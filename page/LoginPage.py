from common.base import BasePage


# login_url = 'http://10.10.3.112/web/login.html'
login_url = 'http://10.10.3.78:30303/login.html'


class LoginPage(BasePage):
        """
        PaaS登录页面定位元素、操作

        """
        account_loc = ('id', 'account')
        account_clear_loc = ('xpath', '//*[@title="清空账号"]')
        password_loc = ('id', 'password')
        password_clear_loc = ('xpath', '//*[@title="清空密码"]')
        input_code_loc = ('id', 'inputCode')
        check_code_loc = ('xpath', '//*[@id="checkCode"]/span')
        remember_me_loc = ('id', 'rememberMe')
        log_in_loc = ('id', 'btn-login')
        success_loc = ('xpath', '//a[text()="租户0410"]')
        failure_wrong_account = ('xpath', '//*[text()="账号或密码错误"]')
        failure_wrong_password = ('xpath', '//*[text()="账号或密码错误"]')
        failure_empty_account = ('xpath', '//*[text()="账号和密码不为空"]')
        failure_empty_password = ('xpath', '//*[text()="账号和密码不为空"]')
        failure_empty_code = ('xpath', '//*[text()="请输入验证码"]')
        failure_wrong_code = ('xpath', '//*[text()="验证码输入错误"]')

        def input_account(self, account):
            """
            输入用户名
            :param account: 用户名

            """
            self.send_keys(self.account_loc, account)

        def input_password(self, password):
            """
            输入密码
            :param password: 密码

            """
            self.send_keys(self.password_loc, password)

        def get_check_code(self):
            """
            获取验证码（code）并返回
            :return: code
            """
            elements = self.find_elements(self.check_code_loc)
            code = ''
            for i in range(len(elements)):
                code += elements[i].text
            return code

        def input_code(self, code):
            """
            输入验证码
            :param code:  验证码

            """

            self.send_keys(self.input_code_loc, code)

        def click_login_btn(self):
            """
            点击登录按钮

            """
            self.click(self.log_in_loc)

        def is_login_success(self):
            """
            登录成功后返回 True
            :return: True
            """
            return self.is_text_in_element(self.success_loc, "租户0410")

        def is_login_failure_account(self):
            """
            账号输入错误时返回 True
            :return: True
            """
            return self.is_text_in_element(self.failure_wrong_account, "账号或密码错误")

        def is_login_failure_password(self):
            """
            密码输入错误时返回True
            :return: True
            """
            return self.is_text_in_element(self.failure_wrong_password, "账号或密码错误")

        def is_login_failure_empty_account(self):
            """
            账号输入为空时返回True
            :return: True
            """
            return self.is_text_in_element(self.failure_empty_account, "账号和密码不为空")

        def is_login_failure_empty_password(self):
            """
            密码输入为空时返回True
            :return: True
            """
            return self.is_text_in_element(self.failure_empty_password, "账号和密码不为空")

        def is_login_failure_empty_code(self):
            """
            验证码输入为空时返回True
            :return: True
            """
            return self.is_text_in_element(self.failure_empty_code, "请输入验证码")

        def is_login_failure_code(self):
            """
            验证码输入错误时返回True
            :return: True
            """
            return self.is_text_in_element(self.failure_wrong_code, "验证码输入错误")

        def getasd(self):
            self.find_elements()