import time
import selenium
from GoodJob import *

email = sys.argv[1] # 登录账号
password = sys.argv[2] # 登录密码


def  Chickin():
        driver = get_web_driver()
        driver.get('https://pfvpn.com/auth/login')  # 打开登陆页面
        time.sleep(5)
        driver.fullscreen_window()
        time.sleep(15)
        driver.get_screenshot_as_file('FullPictures.png')  # 全屏截图
        page_snap_obj = Image.open('FullPictures.png')
        time.sleep(3)
        # 验证码元素位置
        # img = self.driver.find_element('xpath','//*[@id="main"]/div[1]/form/fieldset/p[3]/img')
        # print(img)
        # time.sleep(1)
        # location = img.location#获取图片坐标，左上角
        # size = img.size  # 获取验证码的大小参数（长宽）
        # print(location,size)
        # left = 'x'
        # top = 'y'
        # right = left + size['width']
        # bottom = top + size['height']
        #使用工具获取要截取的坐标区域   如：https://uutool.cn/img-coord/
        image_obj = page_snap_obj.crop((510, 16, 774, 105))  # 按照验证码的长宽，切割验证码
        image_obj.save('MachPicture')
        # image_obj.show()  # 打开切割后的完整验码证
        time.sleep(10)
        number = Ocr_Captcha("MachPicture")  # 验证码识别
        print(number)
        time.sleep(3)
        driver.find_element('xpath', '//*[@id="GOEDGE_WAF_CAPTCHA_CODE"]').send_keys(number)
        time.sleep(2)
        driver.find_element('xpath','/html/body/form/div[3]/button').click()
        time.sleep(3)
        #logion in
        driver.find_element('xpath','//*[@id="email"]').send_keys(email)
        time.sleep(2)
        driver.find_element('xpath','//*[@id="password"]').send_keys(password)
        time.sleep(2)
        driver.find_element('xpath','//*[@id="app"]/section/div/div[1]/div/form/div[4]/button').click()
        time.sleep(2)
        #chick in
        driver.find_element('xpath', '//*[@id="popup-ann-modal"]/div/div/div[3]/button').click()
        time.sleep(2)
        driver.find_element('xpath', '//*[@id="checkin-div"]/a/div/h1').click()
        time.sleep(3)
        driver.quit()





