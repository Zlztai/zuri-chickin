
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
        driver.get("https://zhuri.cc/auth/login")
        time.sleep(3)
        driver.find_element('xpath', '//*[@id="email"]').send_keys(username)
        time.sleep(2)
        driver.find_element('xpath', '//*[@id="password"]').send_keys(password)
        time.sleep(2)
        driver.find_element('xpath', '//*[@id="login-form"]/button').click()   
        time.sleep(5)
        try:
            #签到
            driver.find_element('xpath', '//*[@id="checkin"]').click()  
            time.sleep(2)
        except NoSuchElementException:
            pass
        finally: 
            print('按钮不可点击，已签到？？')
            #获取元素值
#             result = driver.find_element('xpath', '//*[@id="kt_subheader"]/div/div[2]/a').text
           
#     except:
#         pass
#     finally:
#         driver.quit()
#     time.sleep(3)
#     print(result)
#     #发送邮件
#     ret = mail(result,my_sender,my_user,my_pass)
#     if ret:
#         print("邮件发送成功")
#     else:
#         print("邮件发送失败")
#     return result
if __name__ == '__main__':
    suyunChinck()
