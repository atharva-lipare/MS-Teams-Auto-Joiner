from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from datetime import datetime
import json
TEAMS_URL = 'https://teams.microsoft.com/_#/calendarv2'

sleepDelay = 2  # increase if you have a slow internet connection
timeOutDelay = 30  # increase if you have a slow internet connection

curParticipants = 0
minParticipants = 10

opt = Options()
opt.add_argument("--disable-infobars")
opt.add_argument("start-maximized")
opt.add_argument("--disable-extensions")
# Pass the argument 1 to allow and 2 to block
opt.add_experimental_option("prefs", {"profile.default_content_setting_values.media_stream_mic": 1,
                                      "profile.default_content_setting_values.media_stream_camera": 1,
                                      "profile.default_content_setting_values.notifications": 1
                                      })

browser = webdriver.Chrome(ChromeDriverManager().install(), options=opt)


def wait_and_find_ele_by_id(html_id, timeout=timeOutDelay):
    sleep(sleepDelay)
    for i in range(timeout):
        try:
            ele = browser.find_element_by_id(html_id)
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


def check_and_join_meeting():
    global curParticipants
    joins = wait_and_find_elements_by_xpath('//button[.="Join"]', 3)
    if len(joins) == 0:  # no meeting scheduled
        return
    joins[-1].click()  # join the latest meeting scheduled i.e if join buttons for 9, 10 A.M available, will join 10 A.M
    elem = wait_and_find_element_by_xpath(
        '//*[@id="page-content-wrapper"]/div[1]/div/calling-pre-join-screen/div/div/div[2]/div[1]/div['
        '2]/div/div/section/div[2]/toggle-button[1]/div/button')
    if elem.get_attribute('aria-pressed') == 'true':  # turn off camera
        elem.click()
    elem = wait_and_find_element_by_xpath('//*[@id="preJoinAudioButton"]/div/button')
    if elem.get_attribute('aria-pressed') == 'true':  # turn off microphone
        elem.click()
    wait_and_find_element_by_xpath('//button[.="Join now"]').click()  # join meeting
    print('Joined the meeting at {}'.format(datetime.now()))
    sleep(60 * 5)
    browser.execute_script("document.getElementById('roster-button').click()")
    sleep(sleepDelay)
    num_str = wait_and_find_elements_by_xpath(
        '//span[@class="toggle-number"][@ng-if="::ctrl.enableRosterParticipantsLimit"]')
    if len(num_str) >= 2:
        if num_str[1].text[1:-1] != '':
            curParticipants = int(num_str[1].text[1:-1])
        else:
            browser.execute_script("document.getElementById('roster-button').click()")


def check_and_end_or_leave_or_join_meeting():
    global curParticipants, minParticipants
    hangup_btn = wait_and_find_element_by_xpath('//button[@id="hangup-button"]', 2)
    if hangup_btn is not None:  # currently in meeting
        num_str = wait_and_find_elements_by_xpath(
            '//span[@class="toggle-number"][@ng-if="::ctrl.enableRosterParticipantsLimit"]')
        if len(num_str) >= 2:
            if num_str[1].text[1:-1] != '':
                curParticipants = int(num_str[1].text[1:-1])
            else:
                browser.execute_script("document.getElementById('roster-button').click()")
        if curParticipants <= minParticipants and curParticipants != 0:  # leaves meeting for given condition
            browser.execute_script("document.getElementById('hangup-button').click()")
            print('Left meeting at {}'.format(datetime.now()))
            browser.get(TEAMS_URL)  # open calendar tab
            browser.refresh()
            sleep(5)
        else:
            return
    else:
        curParticipants = 0
        browser.get(TEAMS_URL)
        browser.refresh()
        sleep(5)
        check_and_join_meeting()


def init():
    global minParticipants
    browser.get(TEAMS_URL)  # open calendar tab in teams
    sleep(sleepDelay)
    with open('config.json') as f:
        data = json.load(f)
    minParticipants = data['minimumParticipants']
    wait_and_find_ele_by_id('i0116').send_keys(data['username'])  # enter username
    wait_and_find_ele_by_id('idSIButton9').click()  # click next
    wait_and_find_ele_by_id('i0118').send_keys(data['password'])  # enter password
    wait_and_find_ele_by_id('idSIButton9').click()  # click next
    wait_and_find_ele_by_id('idSIButton9').click()  # click yes to stay signed in
    web_ele = wait_and_find_ele_by_link_text('Use the web app instead', 5)
    if web_ele is not None:
        web_ele.click()
    while wait_and_find_element_by_xpath('//button[@title="Switch your calendar view"]') is None:
        sleep(5)    # wait for calendar tab to completely load
    while wait_and_find_element_by_xpath('//button[@title="Switch your calendar view"]').get_attribute('name') != "Day":
        wait_and_find_element_by_xpath('//button[@title="Switch your calendar view"]').click()
        wait_and_find_element_by_xpath('//button[@name="Day"]').click() # change calender work-week view to day view
    print('Initialized Successfully at {}'.format(datetime.now()))
    check_and_join_meeting()


def main():
    global browser
    try:
        init()
    except:
        print('init failed, trying again')
        main()
    else:
        while True:
            try:
                check_and_end_or_leave_or_join_meeting()
            except:
                print('join meeting failed, trying again')
                browser.get(TEAMS_URL)  # open calendar tab in teams
            else:
                sleep(10)


if __name__ == "__main__":
    main()
