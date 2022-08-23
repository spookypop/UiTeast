import time
from Pages.LoginPage import LoginPage
from PublicFunc.assertion import assertion_equal
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


class LoginCase:
    def __init__(self):
        service = ChromeService(executable_path=ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service)

    def test_login_success(self):
        case_description = '输入正确的用户名密码，登录成功，跳转到首页'
        login = LoginPage(self.driver)
        login.login_valid('小明', '123456Xm')
        time.sleep(3)
        assertion_equal(self.driver.current_url, 'http://www.softwarebox.club/', case_description)

    def test_login_fail_username(self):
        case_description = '输入的用户名不存在，系统提示用户不存在'
        login = LoginPage(self.driver)
        login.login_valid('小朱', '123')
        time.sleep(3)
        alert, message = login.alert_message()
        assertion_equal(message, '用户不存在', case_description)
        # 关闭弹窗
        alert.accept()

    def test_login_fail_password(self):
        case_description = '输入的密码不正确，登录失败'
        login = LoginPage(self.driver)
        login.login_valid('小明', '123')
        time.sleep(3)
        alert, message = login.alert_message()
        assertion_equal(message, '账号或密码不正确', case_description)
        alert.accept()

    def __str__(self):
        print('**登录模块**')

    # 执行用例
    def run_test(self):
        self.__str__()
        self.test_login_success()
        self.test_login_fail_username()
        self.test_login_fail_password()
        self.driver.quit()

