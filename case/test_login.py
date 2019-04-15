import unittest
from page.LoginPage import LoginPage, login_url


class TestLogin(unittest.TestCase):
    """
    测试登录用例，分别测试登录成功和登录失败场景
    """
    def setUp(self):
        self.driver = LoginPage('chrome')
        self.driver.open(login_url)

    # 测试登录成功（上面）
    def test_login_001(self):
        """
        测试登录成功
        """
        self.driver.input_account("zuhu0410")
        self.driver.input_password("Ctp#8899")
        code = self.driver.get_check_code()
        self.driver.input_code(code)
        self.driver.click_login_btn()
        result = self.driver.is_login_success()
        self.assertTrue(result)
        self.driver.quit()

    # def test_login_002(self):
    #     """
    #     测试登录失败：账号错误
    #     """
    #     self.driver.input_account("weifuwuabcd")
    #     self.driver.input_password("Ctp#8899")
    #     code = self.driver.get_check_code()
    #     self.driver.input_code(code)
    #     self.driver.click_login_btn()
    #     result = self.driver.is_login_failure_account()
    #     self.assertTrue(result)
    #     self.driver.quit()
    #
    # def test_login_003(self):
    #     """
    #     测试登录失败：密码错误
    #     """
    #     self.driver.input_account("zuhu0410")
    #     self.driver.input_password("Ctp#88991")
    #     code = self.driver.get_check_code()
    #     self.driver.input_code(code)
    #     self.driver.click_login_btn()
    #     result = self.driver.is_login_failure_password()
    #     self.assertTrue(result)
    #     self.driver.quit()
    #
    # def test_login_004(self):
    #     """
    #     测试登录失败：账号为空
    #     """
    #     self.driver.input_account("")
    #     self.driver.input_password("Ctp#8899")
    #     code = self.driver.get_check_code()
    #     self.driver.input_code(code)
    #     self.driver.click_login_btn()
    #     result = self.driver.is_login_failure_empty_account()
    #     self.assertTrue(result)
    #     self.driver.quit()
    #
    # def test_login_005(self):
    #     """
    #     测试登录失败：密码为空
    #     """
    #     self.driver.input_account("zuhu0410")
    #     self.driver.input_password("")
    #     code = self.driver.get_check_code()
    #     self.driver.input_code(code)
    #     self.driver.click_login_btn()
    #     result = self.driver.is_login_failure_empty_password()
    #     self.assertTrue(result)
    #     self.driver.quit()
    #
    # def test_login_006(self):
    #     """
    #     测试登录失败：验证码为空
    #     """
    #     self.driver.input_account("zuhu0410")
    #     self.driver.input_password("Ctp#8899")
    #     self.driver.input_code("")
    #     self.driver.click_login_btn()
    #     result = self.driver.is_login_failure_empty_code()
    #     self.assertTrue(result)
    #     self.driver.quit()
    #
    # def test_login_007(self):
    #     """
    #     测试登录失败：验证码错误
    #     """
    #     self.driver.input_account("zuhu0410")
    #     self.driver.input_password("Ctp#8899")
    #     self.driver.input_code(code="test")
    #     self.driver.click_login_btn()
    #     result = self.driver.is_login_failure_code()
    #     self.assertTrue(result)
    #     self.driver.quit()


if __name__ == '__main__':
    unittest.main()
