from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

# lauch the browser
o = ChromeOptions()
o.add_experimental_option("detach", True)
o.add_argument("--disable-notifications")
driver = Chrome(options=o)
driver.implicitly_wait(100)

# opening website and maximizse the window
driver.get("https://www.myntra.com/")
driver.maximize_window()

# calling actionchain drivers
actions = ActionChains(driver)

# hovering on GENZ and selecting the Jacket
gen = driver.find_element(By.XPATH, '//a[. = "Genz"]')
actions.move_to_element(gen).perform()
driver.find_element(By.XPATH, '//a[. = "Jackets Under ₹899"]').click()

## selecting the filters
actions.pause(3).perform()
driver.find_element(By.XPATH, '(//div[@class="common-checkboxIndicator"])[11]').click()
actions.pause(3).perform()
driver.find_element(By.XPATH, '(//div[@class="common-checkboxIndicator"])[19]').click()

## sort by popularity

actions.pause(2).perform()
ss = driver.find_element(By.XPATH, '//div[@class="horizontal-filters-sortContainer"]')
actions.move_to_element(ss).perform()
actions.pause(1).perform()
pop = driver.find_element(By.XPATH, '(//label[@class="sort-label "])[3]')
actions.move_to_element(pop).click(pop).perform()

## clicking the first product
driver.find_element(By.XPATH, '(//li[@class="product-base"])[1]').click()

## switch the window handles
driver.switch_to.window(driver.window_handles[1])

# selecting ethe size and add to cart
driver.find_element(By.XPATH, '(//p[@class="size-buttons-unified-size"])[3]').click()
driver.find_element(By.XPATH, '//div[. = "ADD TO BAG"]').click()

## closing all the tabs

