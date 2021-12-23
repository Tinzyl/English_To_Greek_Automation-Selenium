from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path='/Users/macbookpro/Downloads/chromedriver')

with open('input.txt', 'r') as f:
    text = f.read().strip()

driver.get('https://www.deepl.com/translator')
driver.find_element_by_css_selector('.dl_cookieBanner--buttonSelected').click()

driver.find_element_by_css_selector('.lmt__language_container_prim .lmt__language_select__opener').click()
driver.find_element_by_css_selector('[dl-test="translator-lang-option-el-EL"]').click()

inputTextArea = driver.find_element_by_css_selector('.lmt__textarea')
inputTextArea.send_keys(text)
time.sleep(5)
driver.find_element_by_css_selector('.lmt__target_toolbar__copy').click()
# driver.quit()
