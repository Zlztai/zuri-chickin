
from Method import *
import time

username = sys.argv[1] # 登录账号
password = sys.argv[2] # 登录密码

my_sender = sys.argv[3]  # 填写发信人的邮箱账号
my_pass = sys.argv[4]  # 发件人邮箱授权码
my_user = sys.argv[5]  # 收件人邮箱账号

def suyunChinck():
    try:
        driver = get_web_driver()
        driver.get("https://yooo.one/auth/login")
        time.sleep(3)
        driver.find_element('xpath', '//*[@id="email"]').send_keys(username)
        time.sleep(2)
        driver.find_element('xpath', '//*[@id="password"]').send_keys(password)
        time.sleep(2)
        driver.find_element('xpath', '//*[@id="login_submit"]').click()
        time.sleep(5)
        try:
            driver.find_element('xpath', '//*[@id="checkin"]').click()
            #获取元素值
            result = driver.find_element('xpath', '//*[@id="checkin"]').text
        finally: 
            print('按钮不可点击，已签到？？')
    except:
        raise
    finally:
        driver.quit()
    return result
    print(result)
    mail(result,my_sender,my_user,my_pass)

if __name__ == '__main__':
    suyunChinck()
