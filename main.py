from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from authData import username, password
from instapy import InstaPy
import time
import random


class instaBot(object):

    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.browser = webdriver.Chrome("/home/serhiy/instaBot/chromedriver")
        self.post_urls = []

    def close(self):

        self.browser.close()
        self.browser.quit()

    def login(self):

        browser = self.browser
        browser.get("https://www.instagram.com/?hl=ru")
        time.sleep(random.randrange(3, 5))

        username_input = browser.find_element_by_name("username")
        username_input.clear()
        username_input.send_keys(username)

        time.sleep(3)

        password_input = browser.find_element_by_name("password")
        password_input.clear()
        password_input.send_keys(password)

        password_input.send_keys(Keys.ENTER)
        time.sleep(10)

    def pars(self, hashtags):

        browser = self.browser
        browser.get(f"https://www.instagram.com/explore/tags/{hashtags}/")
        time.sleep(5)

        for item in range(1, 5):
            browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        hrefs = browser.find_elements_by_tag_name("a")

        # Парсинг сторінки на силки, вибір тільки постів
        for item in hrefs:
            href = item.get_attribute("href")
            if "/p/" in href:
                self.post_urls.append(href)
        print(self.post_urls)


    def like_by_hashtags(self):

        try:
            for url in self.post_urls:
                self.browser.get(url)
                time.sleep(3)
                like_button = self.browser.find_element_by_xpath(
                    '//span[@class="fr66n"]/button').click()
                time.sleep(random.randrange(5, 50))
        except Exception as ex:
            print(ex)

    def follow_by_hashtags(self):

        # try:
        #     for url in self.post_urls:
        #         self.browser.get(url)
        #         time.sleep(3)
        #         follow_button = self.browser.find_element_by_xpath(
        #             '//span[@class="bY2yH"]/button').click()
        #         time.sleep(random.randrange(5, 50))
        # except Exception as ex:
        #     print(ex)


bot = instaBot(username, password)
bot.login()
bot.pars("взаимныелайки")
bot.follow_by_hashtags()
# bot.like_by_hashtags()
