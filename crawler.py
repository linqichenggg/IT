# import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
#存于文件夹
import os
import wget

# 进入Steam主页
# browser = webdriver.Edge()
driver = webdriver.Edge("C:/Program Files (x86)/Microsoft/Edge/Application/msedgedriver.exe")
driver.get("https://store.steampowered.com/")

#等到网页出现“登录“字样（右上角），才进行下一步操作，防止在加载未结束时就进行读取
element = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CLASS_NAME, "global_action_link"))
)

#进入“优惠”界面
entry = driver.find_element(By.XPATH, '//*[@id="responsive_page_template_content"]/div[1]/div[2]/div[16]/div/div/a[2]')
entry.click()
#同样等待
search = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, '//*[@id="term"]'))
)


#获取游戏名
# for i in range(2):
#     driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
#     time.sleep(5)
# names = driver.find_elements(By.CLASS_NAME, 'title')
# for name in names:
#     print(name.text)


# 获取游戏封面
search = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, 'responsive_search_name_combined'))
    )

game = driver.find_element(By.CLASS_NAME, 'responsive_search_name_combined')
game.click()
search = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CLASS_NAME, 'game_header_image_full'))
)
img = driver.find_element(By.CLASS_NAME, 'game_header_image_full')
print(img.get_attribute("src"))
driver.back()
time.sleep(3)

