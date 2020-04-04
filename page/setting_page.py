import allure

from base.base_aciton import BaseAciton
import page

"""
    负责 设置页面相关逻辑
"""
class SettingPage(BaseAciton):
    def __init__(self,driver):
        BaseAciton.__init__(self,driver)

    #退出当前登录的账号
    def logout_account(self):
        #1.滑动页面低端 才会看见退出按钮 才能找到元素 drag
         self.swipe_screen(1)
        #2.点击退出按钮
         self.click_element(page.setting_center_login_out_btn)
        #3.点击弹出对话框确定按钮
         self.click_element(page.setting_center_login_dialog_confirm_btn)
