import time

from selenium.webdriver.common.by import By
from base.base_page import BasePage


class LoginPage(BasePage):
    # 页面的元素
    username_loc = (By.NAME, "username")
    password_loc = (By.NAME, "password")
    Authentication_loc = (By.NAME, "loginauth")
    submit_loc = (By.NAME, "imageField")
    tuichu_loc = (By.LINK_TEXT, '退出')

    def login_ecshop(self, username='admin', password='admin', loginauth='admin'):
        self.send_keys(LoginPage.username_loc, username)
        self.send_keys(LoginPage.password_loc, password)
        self.send_keys(LoginPage.Authentication_loc, loginauth)
        self.click(LoginPage.submit_loc)
        time.sleep(3)

    # 断言
    def get_except_result(self):
        time.sleep(2)
        self.get_value(LoginPage.tuichu_loc)
        return self.get_value(LoginPage.tuichu_loc)
