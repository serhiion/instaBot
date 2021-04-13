from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from authData import username, password
import time
import random


# def login(username, password):
#     browser = webdriver.Chrome("/home/serhiy/instaBot/chromedriver")
#
#     try:
#         browser.get("https://www.instagram.com/?hl=ru")
#         time.sleep(random.randrange(3, 5))
#
#         username_input = browser.find_element_by_name("username")
#         username_input.clear()
#         username_input.send_keys(username)
#
#         time.sleep(3)
#
#         password_input = browser.find_element_by_name("password")
#         password_input.clear()
#         password_input.send_keys(password)
#
#         password_input.send_keys(Keys.ENTER)
#         time.sleep(10)
#
#         browser.close()
#         browser.quit()
#
#     except Exception as ex:
#         print(ex)
#         browser.quit()
#
# login(username, password)

def search_hashtags(username, password, hashtags):
    browser = webdriver.Chrome("/home/serhiy/instaBot/chromedriver")

    try:
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

        try:
            browser.get(f"https://www.instagram.com/explore/tags/{hashtags}/")
            time.sleep(5)

            for item in range(1, 5):
                browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")

            hrefs = browser.find_elements_by_tag_name("a")

            # Парсинг сторінки на силки, вибір тільки постів
            post_urls = []
            for item in hrefs:
                href = item.get_attribute("href")

                if "/p/" in href:
                    post_urls.append(href)
            print(post_urls)

            try:
                for url in post_urls:
                    browser.get(url)
                    time.sleep(3)
                    like_button = browser.find_element_by_xpath(
                        "//span[@class='fr66n']/button").click()
                    time.sleep(random.randrange(5, 50))
            except Exception as ex:
                print(ex)

            # for url in post_urls[0:1]:
            #     browser.get(url)
            #     follow_button = browser.find_element_by_xpath(
            #         '//span[@class="bY2yH"]/button').click()
            #     input()
            #     time.sleep(5)


            browser.close()
            browser.quit()

        except Exception as ex:
            print(ex)
            browser.close()
            browser.quit()

    except Exception as ex:
        print(ex)
        browser.close()
        browser.quit()

search_hashtags(username, password, "взаимнаяподписка")


