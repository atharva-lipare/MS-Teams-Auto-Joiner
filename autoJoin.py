from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
import json
import os

sleepDelay = 2      # increase if you have a slow internet connection
timeOutDelay = 60   # increase if you have a slow internet connection

opt = Options()
opt.add_argument("--disable-infobars")
opt.add_argument("start-maximized")
opt.add_argument("--disable-extensions")
# Pass the argument 1 to allow and 2 to block
opt.add_experimental_option("prefs", { \
    "profile.default_content_setting_values.media_stream_mic": 1, 
    "profile.default_content_setting_values.media_stream_camera": 1,
    "profile.default_content_setting_values.notifications": 1 
})

browser = webdriver.Chrome(ChromeDriverManager().install(),options=opt)

def wait_and_find_ele_by_id(id, timeout=timeOutDelay):
    sleep(sleepDelay)
    for i in range(timeout):
        try:
            ele = browser.find_element_by_id(id)
        except:
            sleep(sleepDelay)
        else:
            return ele

def wait_and_find_ele_by_link_text(text, timeout=timeOutDelay):
    sleep(sleepDelay)
    for i in range(timeout):
        try:
            ele = browser.find_element_by_link_text(text)
        except:
            sleep(sleepDelay)
        else:
            return ele

def wait_and_find_element_by_xpath(xpath, timeout=timeOutDelay):
    sleep(sleepDelay)
    for i in range(timeout):
        try:
            ele = browser.find_element_by_xpath(xpath)
        except:
            sleep(sleepDelay)
        else:
            return ele

def wait_and_find_elements_by_xpath(xpath, timeout=timeOutDelay):
    sleep(sleepDelay)
    for i in range(timeout):
        try:
            ele = browser.find_elements_by_xpath(xpath)
        except:
            sleep(sleepDelay)
        else:
            return ele

def joinMeeting():
    if wait_and_find_element_by_xpath('//button[@id="hangup-button"]', 3) != None: # currently in meeting
        return
    if wait_and_find_element_by_xpath('//button[@name="Details"]', 3) != None: # organiser ended the meeting
        browser.get('https://teams.microsoft.com/_#/calendarv2')
    joins = wait_and_find_elements_by_xpath('//button[.="Join"]', 3)
    if len(joins) == 0: # no meeting scheduled
        return
    return
    joins[-1].click()   # join the latest meeting scheduled i.e if join buttons for 9 A.M and 10 A.M available, will join 10 A.M
    elem = wait_and_find_element_by_xpath('//*[@id="page-content-wrapper"]/div[1]/div/calling-pre-join-screen/div/div/div[2]/div[1]/div[2]/div/div/section/div[2]/toggle-button[1]/div/button', timeOutDelay)
    if elem.get_attribute('aria-pressed') == 'true': # turn off camera
        elem.click()
    elem = wait_and_find_element_by_xpath('//*[@id="preJoinAudioButton"]/div/button', timeOutDelay)
    if elem.get_attribute('aria-pressed') == 'true': # turn off microphone
        elem.click()
    wait_and_find_element_by_xpath('//button[.="Join now"]', timeOutDelay).click() # join meeting

def init():
    browser.get('https://teams.microsoft.com/_#/calendarv2')
    with open(os.path.join(os.path.curdir, 'config.json')) as f:
        data = json.load(f)
    wait_and_find_ele_by_id('i0116', timeOutDelay).send_keys(data['username'])
    wait_and_find_ele_by_id('idSIButton9', timeOutDelay).click()
    wait_and_find_ele_by_id('i0118', timeOutDelay).send_keys(data['password'])
    wait_and_find_ele_by_id('idSIButton9', timeOutDelay).click()
    wait_and_find_ele_by_id('idSIButton9', timeOutDelay).click()
    wait_and_find_ele_by_link_text('Use the web app instead', timeOutDelay).click()
    sleep(40)   # waits for calendar page to load completely    # find better way #PENDING
    wait_and_find_element_by_xpath('//button[@title="Switch your calendar view"]', timeOutDelay).click()
    actions = ActionChains(browser)
    actions.send_keys(Keys.ARROW_DOWN)
    actions.send_keys(Keys.ARROW_DOWN)
    actions.send_keys(Keys.ARROW_DOWN)
    actions.send_keys(Keys.ENTER)
    actions.perform()
    #wait_and_find_element_by_xpath('//button[@aria-label="Week view"]', timeOutDelay).click()  # don't know why this line doesn't work ? #PENDING

def main():
    global browser
    init()
    while True:
        joinMeeting()
        sleep(5)

if __name__ == "__main__":
    main()