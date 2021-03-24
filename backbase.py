from selenium import webdriver
import unittest
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class BackBaseTest(unittest.TestCase):

    selectors = {
        "main": {
            "path": "body > app-root > app-home > div",
        },
        "articles": {
            "path": "body > app-root > app-home > div > div.container.page > div > div.col-md-9",
            "list_path": "body > app-root > app-home > div > div.container.page > div > div.col-md-9 > app-article-list",
            "comments_path": "[class='article-preview']",
            "favorite_articles_path": "[class='tag-list']",
        },
        "users": {
            "path": "[class='row']",
        }
    }

    @classmethod
    def setUpClass(cls):
        main_path = cls.selectors['main']['path']

        cls.driver = webdriver.Chrome(executable_path="/Users/rizwan.memon/Documents/driver/chromedriver 2")

        url = 'https://candidatex:qa-is-cool@qa-task.backbasecloud.com/'

        cls.driver.get(f"{url}")

        timeout = 5
        try:
            element_present = EC.presence_of_element_located((By.CSS_SELECTOR, f'{main_path}'))
            WebDriverWait(cls.driver, timeout).until(element_present)
        except TimeoutError:
            print('Page timed out trying to load')

    def test_01_verify_articles_are_present(self):
        articles_path = self.selectors['articles']['path']

        articles = self.driver.find_element_by_css_selector(f'{articles_path}').get_attribute('innerHTML')
        assert len(articles) > 0, 'Articles were not loaded'

    def test_02_verify_comments_on_articles_are_present(self):
        articles_comments_path = self.selectors['articles']['comments_path']

        time.sleep(1)
        article_comments = self.driver.find_element_by_css_selector(f"{articles_comments_path}").get_attribute('innerHTML')
        assert len(article_comments) > 0, 'Articles Comments were not loaded'

    def test_03_verify_total_list_of_articles_are_present(self):
        total_articles_path = self.selectors['articles']['list_path']

        time.sleep(1)
        total_articles = self.driver.find_element_by_css_selector(f"{total_articles_path}").get_attribute('childElementCount')
        assert int(total_articles) == 13, f'The total amount of articles should be 13 not {total_articles}'

    def test_04_verify_favorite_articles_are_present(self):
        favorite_articles_comments_path = self.selectors['articles']['favorite_articles_path']

        favorite_articles = self.driver.find_element_by_css_selector(f"{favorite_articles_comments_path}").get_attribute('innerHTML')
        assert len(favorite_articles) > 0, 'Favorite articles are not present'

    def test_05_verify_user_can_follow_other_users(self):
        users_path = self.selectors['users']['path']

        users = self.driver.find_elements_by_xpath("//a[@href]")
        for user in users:
            my_href = user.get_attribute("href")
            self.driver.execute_script("window.open('" + my_href +"');")

        users_page_redirect = self.driver.find_element_by_css_selector(f"{users_path}").get_attribute('innerHTML')
        assert len(users_page_redirect) > 0, 'User was not able to follow other users'

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == 'main':
    unittest.main()