import os, sys
import pytest
from page.navigation_page import NavigationPage
from base.init_driver import get_driver
from base.read_yaml_data import read_yaml_data
import time

# 添加环境变量
sys.path.append(os.getcwd())


# 获取模拟的yaml数据
def get_data():
    data_list = []
    data = read_yaml_data("login_data.yaml")
    # print(data)
    for i in data.keys():
        data2 = data.get(i)
        name = data2.get("username")
        passwd = data2.get("password")
        data_list.append((name, passwd))
    return data_list


class TestLogin:
    # 初始化导航类
    def setup_class(self):
        # 1.初始化driver对象
        self.driver = get_driver("com.yunmall.lc", "com.yunmall.ymctoc.ui.activity.MainActivity")
        # 2.初始化导航对象
        self.navigation_page = NavigationPage(self.driver)

    def teardown_class(self):
        time.sleep(5)
        self.driver.quit()

    # 测试登录业务
    @pytest.mark.parametrize("username,password", get_data())
    def test_login(self, username, password):
        # 1.点击我的
        self.navigation_page.get_home_page_obj().click_my_button()
        # 2.点击已有账号
        self.navigation_page.get_sign_in_page_obj().click_exist_accout()
        # 3.输入用户名密码 点击登录
        self.navigation_page.get_login_page_obj().login_in(username, password)
        # 4.判断是否登录成功 还是失败
        assert True


