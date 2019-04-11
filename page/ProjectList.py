from common.base import BasePage

login_url = 'http://10.10.3.112/web/login.html'


class ProjectList(BasePage):
    """
    PaaS项目列表页面定位元素、操作

    """
    # 首页
    index_page_loc = ('xpath', '//*[text()="首页"]')
    # 项目管理>>项目列表
    project_manage_loc = ('xpath', '//*[text()="项目管理"]')
    project_list_loc = ('xpath', '//*[text()="项目列表"]')
    # 新增项目元素
    iframe_loc = ('id', 'iframepage')
    project_add_loc = ('xpath', '//*[text()="新增"]')
    project_add_name_loc = ('id', 'projectName')
    project_add_code_loc = ('id', 'projectCode')
    project_add_remark_loc = ('id', 'remark')
    project_add_save_loc = ('xpath', '//button[text()="提交"]')
    project_add_backBtn_loc = ('xpath', '//button[text()="返回"]')

    # 搜索项目元素
    project_query_name_loc = ('id', 'qprojectName')
    project_query_btn_loc = ('id', 'projectQuery')

    # 修改项目元素
    project_edit_trangle_loc = ("xpath", "//i[@class='iconfont']")
    project_edit_btn_loc = ("xpath", "//span[text()='修改']")
    project_edit_name_loc = ('name', 'projectName')
    project_edit_remark_loc = ("name", "remark")
    project_edit_quit_loc = ('class name', 'layui-layer-setwin')
    project_edit_save_loc = ('xpath', '//*[text()="保存"]')
    project_edit_close_loc = ('xpath', '//*[text()="关闭"]')

    # 项目列表头元素
    order_number_list_loc = ('xpath', '//th[text()="序号"]')
    project_name_list_loc = ('xpath', '//th[text()="项目名称"]')
    project_code_list_loc = ('xpath', '//th[text()="项目编码"]')
    tenancy_name_list_loc = ('xpath', '//th[text()="租户名称"]')
    creator_list_loc = ('xpath', '//th[text()="创建人"]')
    create_time_list_loc = ('xpath', '//th[text()="创建日期"]')
    is_syn_list_loc = ('xpath', '//th[text()="已同步"]')
    action_list_loc = ('xpath', '//th[text()="操作"]')

    # 项目列表中元素
    project_name_loc = ('xpath', '//a[@ng-bind="v.projectName"]')
    project_code_loc = ('xpath', '//td[@ng-bind="v.projectCode"]')
    tenancy_name_loc = ('xpath', '//td[@ng-bind="v.tenancyName"]')
    creator_loc = ('xpath', '//td[@ng-bind="v.createName"]')
    create_time_loc = ('xpath', '//td[contains(@ng-bind, "v.createTime")]')

    # 集群关联元素
    link_cluster_loc = ('xpath', '//*[text()="集群关联"]')
    link_cluster_checkbox_loc = ("xpath", "//input[@type='checkbox']")
    cluster_set_left_loc = ('xpath', '//*[@id="cluster_set"]/form/div/div/div[2]/a[1]/i')
    link_cluster_save_loc = ('xpath', '//*[@id="item.clusterId"]')
    cluster_set_right_loc = ('xpath', '//*[@id="cluster_set"]/form/div/div/div[2]/a[2]/i')
    link_cluster_close_loc = ("xpath", "//a[text()='关闭']")
    link_cluster_quit_loc = ('class name', 'layui-layer-setwin')

    # 成员管理元素
    member_manage_loc = ('xpath', '//*[text()="成员管理"]')
    # 新增
    employee_add_loc = ('xpath', '//*[text()="新增"]')
    employee_name_loc = ('name', 'employeeName')
    employee_account_loc = ('name', 'account')
    employee_password_loc = ('name', 'password')
    employee_password1_loc = ('name', 'password1')
    employee_email_loc = ('name', 'email')
    employee_role_loc = ('name', 'roleId')
    employee_remark_loc = ('id', 'remark')
    employee_save_loc = ('xpath', '//button[@type="button"]')
    employee_cancel_loc = ('xpath', '//button[contains(text(), "取消")]')
    employee_quit_loc = ('class name', 'layui-layer-setwin')
    # 搜索
    employee_query_name_loc = ('id', 'userName')
    employee_query_btn_loc = ('id', 'projectMembersQuery')
    # 修改
    employee_edit_loc = ("xpath", "//a[text()='修改']")
    employee_edit_email_loc = ('name', 'email')
    employee_edit_role_loc = ('name', 'roleId')
    employee_edit_remark_loc = ('id', 'remark')
    employee_edit_save_loc = ('css', '[ng-show="data.id"][type="button"]')
    employee_edit_cancel_loc = ('xpath', '//button[contains(text(), "取消")]')
    employee_edit_quit_loc = ('class name', 'layui-layer-setwin')
    # 删除
    employee_delete_loc = ('xpath', '//*[text()="删除"]')
    # 返回
    employee_select_back_loc = ('xpath', '//*[text()="返回"]')
    # 选择用户
    employee_select_loc = ('xpath', '//*[text()="选择用户"]')
    employee_select_employeeName_loc = ('id', 'employeeName')
    employee_select_projectMembersQuery_loc = ('id', 'projectMembersQuery')
    employee_select_radio_loc = ('name', 'userId')
    # 项目列表中元素
    employee_select_account_loc = ('xpath', '//td[@ng-bind="v.account"]')
    employee_select_name_loc = ('xpath', '//td[@ng-bind="v.employeeName"]')
    employee_select_email_loc = ('xpath', '//td[@ng-bind="v.email"]')
    employee_select_remark_loc = ('xpath', '//td[@ng-bind="v.remark"]')
    employee_select_save_loc = ('xpath', '//*[text()="确定"]')
    employee_select_cancel_loc = ('xpath', '//*[text()="取消"]')
    employee_select_quit_loc = ('class name', 'layui-layer-setwin')

    def click_index_page(self):
        self.click(self.index_page_loc)

    def click_project_manage(self):
        self.click(self.project_manage_loc)

    def click_project_list(self):
        self.click(self.project_list_loc)

    def project_add(self):
        self.click(self.project_add_loc)

    def input_project_name(self, name):
        self.send_keys(self.project_add_name_loc, name)

    def input_project_code(self, code):
        self.send_keys(self.project_add_code_loc, code)

    def input_project_remark(self, remark):
        self.send_keys(self.project_add_remark_loc, remark)

    def save_project(self):
        self.click(self.project_add_save_loc)

    def is_project_add_success(self):
        return self.is_visibility_elements(self.project_name_loc)

# if __name__ == '__main__':
#     pl = ProjectList()
#     TestLogin.test_login_001(pl)
#     pl.test()
#


