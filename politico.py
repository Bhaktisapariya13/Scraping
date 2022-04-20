from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support import expected_conditions as EC


chromePath = "D:\selenium\chromedriver_win32 (1)\chromedriver.exe" 
driver = webdriver.Chrome(chromePath)
topic= []
data_list = []
for i in range(1,3):
    url = 'https://www.politico.com/politics/page-'+str(i)
    page = driver.get(url)
    time.sleep(10)

    div = driver.find_elements(By.XPATH, '/html/body/div[2]/main/div[2]/div/div/section[1]/article[2]/ul/section/ul/li/article')
    
    for i in div:
        data = {}
        data["headline"] = i.find_element(By.CSS_SELECTOR, '.format-sm h3 a').text
        data["topic"] = topic
        source=i.find_element(By.CSS_SELECTOR, '.format-sm h3 a')
        data["source"] = source.get_attribute("href")
        times = i.find_element(By.CSS_SELECTOR, '.timestamp time')
        data["date"] = times.text[:-4]
        try:
            data["thumbnail_url"] = i.find_element(By.CSS_SELECTOR,".fig-graphic img").get_attribute('src')
        except:
            data["thumbnail_url"]= None

        new = requests.get(data["source"])
        soup = BeautifulSoup(new.content, "html.parser")
        desc=""
        a=soup.select(".story-text")
        for q in a:
            desc += q.text
        data["description"] = desc
        data_list.append(data)
print(data_list)
print(len(data_list))
driver.quit()