# 验证码登录
import time
from PIL import ImageEnhance
import pytesseract
from selenium import webdriver

# 避免出现系统错误：[WinError 2] 系统找不到指定的文件
try:
    import Image
except ImportError:
    from PIL import Image

pytesseract.pytesseract.tesseract_cmd = r'C:/Program Files (x86)/Tesseract-OCR/tesseract.exe'

# 打开浏览器
url = "http://XXX.XX.XX.XX:XXX/SPMTest/login.html"
browser = webdriver.Chrome()
browser.implicitly_wait(10)
browser.maximize_window()
browser.get(url)

# 用户元素
userElement = browser.find_element_by_id("loginname")
passElement = browser.find_element_by_id("password1")
codeElement = browser.find_element_by_id("code")
lgButton = browser.find_element_by_id("login_value")

# 验证码截取+识别（页面验证码地址不是固定连接，所以采用截图方式）
# 截取屏幕内容，保存到本地
browser.save_screenshot("D://PyDemo/01.png")
# 打开截图，获取验证码位置，截取保存验证码
ran = Image.open("D://PyDemo/01.png")
box = (1165, 380, 1240, 415)  # 获取验证码位置，手动定位（左，上，右，下）--验证码图片的绝对定位
ran.crop(box).save("D://PyDemo/02.png")
# 获取验证码图片，读取验证码
code = pytesseract.image_to_string(Image.open('D://PyDemo/02.png'))
print(code)

# 输入数据登录
userElement.send_keys('tt')
passElement.send_keys('1234')
codeElement.send_keys(code)
time.sleep(3)
lgButton.click()