import time

import ddt

from pageobject.login_page import LoginPage, read_excel
import unittest


@ddt.ddt()
class TestCase(unittest.TestCase):
    def setUp(self) -> None:
        print("\n用例开始执行")

    def doCleanups(self) -> None:
        print("\n用例执行结束")

    @ddt.data(*read_excel())
    @ddt.unpack
    def test_login_01(self, a, b, c):
        ip = LoginPage()
        ip.login_ecshop(a, b, c)
        time.sleep(3)
        if ip.get_except_result() == "Casual Womens Clothing Store Online, Womens Dresses & Tops | noracora":
            self.assertEqual(ip.get_except_result(), "Casual Womens Clothing Store Online, Womens Dresses & Tops | noracora")
        else:
            self.assertEqual(ip.get_except_result(), "Login |noracora")
        ip.quit()

