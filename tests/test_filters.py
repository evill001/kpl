from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest

class TestProductPage(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()  # Используйте подходящий драйвер браузера (например, ChromeDriver)
        self.driver.get("http://localhost:8000/products")  # Замените URL на URL вашего веб-приложения с продуктами

    def test_filter_products_by_category(self):
        dropdown = self.driver.find_element_by_id('category-filter')
        dropdown.click()
        dropdown.find_element_by_css_selector('option[value="category1"]').click()  # Выберите категорию "НОВИНКИ"
        
        souvenirs = self.driver.find_elements_by_css_selector('.souvenir')
        for souvenir in souvenirs:
            self.assertIn('category1', souvenir.get_attribute('data-category'))  # Проверяем, что все продукты относятся к выбранной категории

    def test_filter_products_by_name(self):
        search_input = self.driver.find_element_by_id('name-filter')
        search_input.send_keys('Баба Яга')  # Вводим имя продукта в поле поиска
        
        souvenirs = self.driver.find_elements_by_css_selector('.souvenir')
        for souvenir in souvenirs:
            name = souvenir.get_attribute('data-name').lower()
            self.assertIn('баба яга', name)  # Проверяем, что отображаемые продукты содержат в названии введенное имя

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()