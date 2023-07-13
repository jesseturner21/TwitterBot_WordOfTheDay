from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from time import sleep

TWITTER_WEBSITE = 'https://twitter.com/i/flow/login'


class TwitterBot:
    def __init__(self, email, password, chrome_driver_path):
        self.driver = webdriver.Chrome(executable_path=chrome_driver_path)
        self.driver.get(url=TWITTER_WEBSITE)
        # ----------EMAIL-------------#
        login_going = True
        while login_going:
            try:
                login_email = self.driver.find_element(by='name', value='text')
                login_going = False
            except NoSuchElementException:
                sleep(2)
        login_email.send_keys(email)
        login_email.send_keys(Keys.ENTER)

        # ---------PASSWORD------------#
        password_going = True
        while password_going:
            try:
                login_password = self.driver.find_element(by='name', value='password')
                password_going = False
            except NoSuchElementException:
                sleep(2)
        login_password.send_keys(password)
        login_password.send_keys(Keys.ENTER)

    def make_post(self, text):
        # -----------COMPOSE TWEET-------------#
        compose_find = True
        while compose_find:
            try:
                print("searching")
                compose_tweet = self.driver.find_element(by='xpath',
                                                         value='//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div/div[2]/div/div/div/div')
                print(compose_tweet)
                compose_find = False
            except NoSuchElementException:
                sleep(2)
        compose_tweet.send_keys(text)

        tweet_button = self.driver.find_element(by='xpath',
                                                value='//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[2]/div[2]/div/div/div[2]/div[3]/div')
        print(tweet_button)
        tweet_button.click()
        sleep(10)
