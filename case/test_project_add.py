import unittest
from page.LoginPage import LoginPage, login_url
from page.ProjectList import ProjectList


class TestProjectAdd(unittest.TestCase):
    """
    测试登录用例，分别测试登录成功和登录失败场景
    """
    def setUpClass(self):
        self.driver = LoginPage('chrome')
        self.driver.open(login_url)
        self.driver.input_account("weifuwu")
        self.driver.input_password("Ctp#8899")
        code = self.driver.get_check_code()
        self.driver.input_code(code)
        self.driver.click_login_btn()

    def setUp(self):
        self.driver.click_index_page()
        self.driver.click_project_manage()
        self.driver.click_project_list()

    def tearDown(self):
        self.driver.switch_to_frame_out()

    # 测试登录成功（上面）
    def test_add_001(self):

        self.driver.switch_to_frame(self.iframe_loc)
        self.project_add()
        self.switch_to_frame_out()
        self.switch_to_frame(self.iframe_loc)
        self.input_project_name('test03291')
        self.input_project_code('test03291')
        self.save_project()
        self.switch_to_frame_out()
        self.switch_to_frame(self.iframe_loc)
        self.is_project_add_success()


