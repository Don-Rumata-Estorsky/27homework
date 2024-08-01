"""
узнать погоду с сайта 
"""

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

def main():

    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get("https://www.gismeteo.kz/weather-almaty-5205/")

    temperature = driver.find_element(By.XPATH, '//span[@class="temp"]').text
    wind_speed = driver.find_element(By.XPATH, '//span[@class="unit unit_wind_speed"]').text

    print("Температура:", temperature)
    print("Скорость ветра:",  wind_speed)

    driver.quit()

if __name__ == "__main__":
    main()
