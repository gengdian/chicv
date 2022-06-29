from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class BasePage:
    def __init__(self):
        global driver
        self.driver = webdriver.Chrome()
        driver = self.driver
        self.driver.get("http://localhost/e/admin/index.php")

    #  封装定位元素并返回， 注意参数loc解包
    def locator_element(self, loc):
        return self.driver.find_element(*loc)

    #  封装需要输入值的数据
    def send_keys(self, loc, value):
        self.locator_element(loc).send_keys(value)

    # 封装点击
    def click(self, loc):
        self.locator_element(loc).click()

    # 封装进入frame框架
    def goto_frame(self, frame_name):
        self.driver.switch_to.frame(frame_name)

    # 封装退出frame框架
    def quit_frame(self):
        self.driver.switch_to.default_content()

    # 封装下拉框关键字
    def choice_select(self, loc, value):
        sel = Select(driver.find_element(*loc))
        sel.select_by_value(value)

    # 封装获取定位元素的值
    def get_value(self, loc):
        return self.locator_element(loc).text