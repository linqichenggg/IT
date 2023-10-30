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
option = webdriver.ChromeOptions()
option.add_experimental_option("detach", True)
driver = webdriver.Edge("C:/Program Files (x86)/Microsoft/Edge/Application/msedgedriver.exe")
driver.maximize_window()
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

#翻页
for i in range(1):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)


#等待
search = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, 'responsive_search_name_combined'))
    )

#获取
singles = driver.find_elements(By.CLASS_NAME, 'search_result_row')
for i in range(len(singles)):
    singles = driver.find_elements(By.CLASS_NAME, 'search_result_row')
    # 点击游戏链接
    singles[i].click()

#划分本体与DLC
    try:
        name = driver.find_element(By.CLASS_NAME, 'apphub_AppName')
        print(name.text)
        img = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'game_header_image_full'))
        )
        img = driver.find_element(By.CLASS_NAME, 'game_header_image_full')
        img_src = img.get_attribute("src")
        print(img_src)
    except:
        name = driver.find_element(By.XPATH, '//*[@id="tabletGrid"]/div[1]/div/div[1]/h2')
        print(name.text)
        img = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'package_header'))
        )
        img = img.find_element(By.XPATH, '//*[@id="package_header_container"]/img')
        img_src = img.get_attribute("src")
        print(img_src)
    # 返回到搜索结果页面
    driver.back()



