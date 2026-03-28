from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# launching the chrome driver
o = ChromeOptions()
o.add_experimental_option("detach", True)
driver = Chrome(options=o)
driver.implicitly_wait(100)

# here opening the website
driver.get("https://www.shoppersstack.com/")

# maximizing the window
driver.maximize_window()

#here using the action
actions = ActionChains(driver)
#finding the element and storing in the variable
apple = driver.find_element(By.XPATH,'//img[@alt="iphone"]')

# scroll to the element then wait for a bit then click the product
actions.scroll_to_element(apple).pause(3).click(apple).perform()

# clicking the delivery textarea
driver.find_element(By.XPATH, '//input[@id="Check Delivery"]').send_keys("302017")

# waiting for process to be completed
actions.pause(5).perform()

# clicking on check button
but = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//button[@id="Check"]')))
but.click()
# closing all the tab
driver.quit()








