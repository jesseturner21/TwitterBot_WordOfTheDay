import os

from TwitterBot import TwitterBot
from bs4 import BeautifulSoup
import requests

CHROME_DRIVER_PATH = '/Users/jesseturner/Desktop/Development/chromedriver114/chromedriver'
TWITTER_EMAIL = os.environ.get("TWITTER_EMAIL")
TWITTER_PASSWORD = os.environ.get("TWITTER_PASSWORD")
print(TWITTER_PASSWORD)
print(TWITTER_EMAIL)
WORD_OF_THE_DAY_WEBSITE = 'https://www.merriam-webster.com/word-of-the-day'

twit = TwitterBot(TWITTER_EMAIL, TWITTER_PASSWORD, CHROME_DRIVER_PATH)

# -------------GET THE WORD OF THE DAY---------#
response = requests.get(url=WORD_OF_THE_DAY_WEBSITE)
soup = BeautifulSoup(response.text, features='html.parser')
word = soup.find('h2').text
word = word.upper()
definition = soup.find('p').text
post_text = f" - {word} - \n {definition}"

# ----------------MAKE POST--------------------#
twit.make_post(post_text)
