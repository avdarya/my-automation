from selenium.webdriver.chrome.webdriver import WebDriver as ChromeDriver
from selenium.webdriver.firefox.webdriver import WebDriver as FfDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class InventoryPage:
  _driver: ChromeDriver | FfDriver
  
  def __init__(self, driver:  ChromeDriver | FfDriver) -> None:
    self._driver = driver
    
  def add_to_cart_by_inventory(self, inventory_title: str) -> None:
    WebDriverWait(self._driver, 4).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div.inventory_list')))
    loaded_inventories = self._driver.find_elements(By.CSS_SELECTOR, 'div.inventory_item')
    for inventory_card in loaded_inventories:
      if inventory_card.find_element(By.CSS_SELECTOR, 'div.inventory_item_name').text == inventory_title:
        inventory_card.find_element(By.CSS_SELECTOR, 'button.btn_inventory').click()

  def press_cart(self) -> None:
    self._driver.find_element(By.CSS_SELECTOR, 'a.shopping_cart_link').click()


