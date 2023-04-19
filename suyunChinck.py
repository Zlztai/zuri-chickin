
from util import *
import time

username = sys.argv[1] # 登录账号
password = sys.argv[2] # 登录密码

@retry(stop_max_attempt_number=5)
def hupu():
    try:
        driver = get_web_driver()
        driver.get("https://yooo.one/auth/login")
        driver.find_element('xpath', '//*[@id="email"]').send_keys(username)
        driver.find_element('xpath', '//*[@id="password"]').send_keys(password)
        driver.find_element('xpath', '//*[@id="login_submit"]').click()
        time.sleep(5)
        driver.find_element('xpath', '//*[@id="checkin"]').click()
        #获取元素值
        result = driver.find_element('xpath', '//*[@id="checkin"]').text
    except:
        raise
    finally:
        driver.quit()
    return result

if __name__ == '__main__':
    suyunChinck()
