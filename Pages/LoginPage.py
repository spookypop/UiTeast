from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


# 登录页面
class LoginPage(object):
    def __init__(self, driver):
        # 浏览器驱动
        self.driver = driver
        # 页面地址
        self.driver.get('http://www.softwarebox.club/pages/OnlineTools/AutoLearn')
        try:
            # 用户名输入框
            self.usernameBy = self.driver.find_element(By.ID, 'username')
            # 密码输入框
            self.passwordBy = self.driver.find_element(By.ID, 'password')
            # 登录按钮
            self.submitBy = self.driver.find_element(By.XPATH, '//*[@id="contentmain"]/section/div[2]/form/button[1]')
        except Exception as e:
            message = '元素定位失败'
            print(e)
            print(message)

    # 登录功能
    def login_valid(self, username, password):
        # 输入用户名
        self.usernameBy.send_keys(username)
        # 输入密码
        self.passwordBy.send_keys(password)
        # 点击登录按钮
        self.submitBy.click()

    # 获取页面弹窗
    def alert_message(self):
        wait = WebDriverWait(self.driver, 10)
        alert = wait.until(expected_conditions.alert_is_present())
        # 返回弹窗和弹窗信息
        return alert, alert.text
