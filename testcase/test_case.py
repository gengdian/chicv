import time

import ddt

from pageobject.login_page import LoginPage, read_excel
import unittest


@ddt.ddt()
class TestCase(unittest.TestCase):
    def setUp(self) -> None:
        print("\n用例开始执行"+time.strftime("%Y-%m-%d %H:%M:%S"))

    def doCleanups(self) -> None:
        print("\n用例执行结束"+time.strftime("%Y-%m-%d %H:%M:%S"))

    @ddt.data(*read_excel())
    @ddt.unpack
    def test_login_01(self, a, b, c):
        """登录测试"""
        ip = LoginPage()
        print("账号:"+a)
        print("密码："+str(b))
        ip.login_ecshop(a, b, c)
        time.sleep(3)
        print(ip.get_except_result())
        if a == "gengdian@chicv.com" or b == "111111":
            print("账号密码正确，登录成功")
        else:
            print("账号密码错误，登录失败")
        if ip.get_except_result() == "Casual Womens Clothing Store Online, Womens Dresses & Tops | noracora":
            self.assertEqual(ip.get_except_result(), "Casual Womens Clothing Store Online, Womens Dresses & Tops | noracora")
            print(self.assertEqual(ip.get_except_result(), "Casual Womens Clothing Store Online, Womens Dresses & Tops | noracora"))
        else:
            self.assertEqual(ip.get_except_result(), "Login |noracora")
            print(self.assertEqual(ip.get_except_result(), "Login |noracora"))
        ip.quit()

