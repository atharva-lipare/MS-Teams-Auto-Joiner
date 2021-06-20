# [MS-Teams-Auto-Joiner](https://github.com/atharva-lipare/MS-Teams-Auto-Joiner)

![banner](https://i.imgur.com/xtq5Muz.png)

[![Gitter](https://badges.gitter.im/MS-Teams-Auto-Joiner/community.svg)](https://gitter.im/MS-Teams-Auto-Joiner/community?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge)

## This python script will automatically join [Microsoft Teams](https://www.microsoft.com/en-in/microsoft-365/microsoft-teams/group-chat-software) meetings appearing in your [Teams calendar](https://teams.microsoft.com/_#/calendarv2).

## Features:
- This python script will automatically open a chrome tab, enter your username, your password, open the calendar tab and then join a meeting if available.
- Before joining any meeting, it will by default turn off your camera and microphone.
- After the organiser ends the meeting, it will open the calendar tab to look for new meetings and join the next meeting if available.
- If the organiser does not end the meeting i.e. attendees are made to leave the meeting, the script will automatically leave the meeting after the number of participants present in the meeting falls below the minimum participants allowed set by the user (default is 10), but will rejoin the meeting if the join button is still visible on the calendar tab. To not rejoin the same meeting user must stop the script by CTRL+C.

## Requirements:
- [Python3](https://www.python.org/downloads/)
- [Google Chrome browser](https://www.google.com/intl/en_in/chrome/)

## Prerequisites:
### After cloning the repo, go in the repo directory and then follow below steps:
- Step 1:
    Install dependencies from [requirements.txt](requirements.txt):
    ```bash
    pip install -r requirements.txt
    ```

- Step 2:
    To set login credentials and minimum number of participants allowed, modify [config.json](config.json):
    ```json
    {
    "username":"example@example.com",
    "password":"example",
    "minimumParticipants":10,
    "use_twillio":false,
    "account_sid": "AC506be2ab8a6f4d8602cccccccccccccccc",
    "auth_token":"9f2ca3f98b46c57ab0a77accccccccccccc",
    "your_no":"+91894900000",
    "twillio_no":"+17039970000", 
    "nickname" : "Wolfie"
    }
    ```

### if use_twillio value is set to false there is no need to update or modify parameters below leave them as it is ( that means you won't able to use the message service, if it is true that means you want to use the message serive proceed to next section about how to set it up.

### If you want to use twillio( a message alert) for your script 

- Step 1:
    To create a free trial account on twillio [https://www.twilio.com/try-twilio](url)
- Step 2:
    Sign up and verify your mobile number ( if you already have account just login)
- Step 3:
    Open twillio console 
- Step 4:
    There you will see account_ssid, auth token and to get the number ( which will be used to send the messgae ), click on Get trial number .
- Step 5:
    Modift all the details in [config.json](config.json):
    ```json
    {
    "username":"example@example.com",
    "password":"example",
    "minimumParticipants":10,
    "use_twillio":true,
    "account_sid": "AC506be2ab8a6f4d8602cccccccccccccccc",
    "auth_token":"9f2ca3f98b46c57ab0a77accccccccccccc",
    "your_no":"+91894900000",
    "twillio_no":"+17039970000", 
    "nickname" : "Wolfie"
    }
    ```
## Usage:
-   Run [autoJoin.py](autoJoin.py):
    ```bash
    python autoJoin.py
    ```
- The script might not work as expected if the browser is minimised i.e you may open other windows above it but do not minimize the chrome window.

## Sample Scenario:
- You have a meeting at 9 A.M, you may run the script anytime before 9 A.M. and the script will automatically join the meeting when the join button is available.
- The script will then automatically join the next meeting scheduled at e.g.:- 10 A.M. AFTER the organiser ends the meeting.
- If the organiser does not end the meeting i.e the organiser leaves the meeting instead of ending the meeting, the script will leave the meeting after the strength of the meeting falls down to 10 or any minimum value set by the user.
- To set a custom condition to automatically leave the meeting change the code on line# 111 of [autoJoin.py](autoJoin.py)

## Contributing:
- When contributing to this repository, feel free to discuss the change you wish to make via [Issues](https://github.com/atharva-lipare/MS-Teams-Auto-Joiner/issues), [Discussions](https://github.com/atharva-lipare/MS-Teams-Auto-Joiner/discussions) or [gitter chat room](https://gitter.im/MS-Teams-Auto-Joiner/community?utm_source=share-link&utm_medium=link&utm_campaign=share-link) before making a change.
- And don't forget to ⭐ the repo, 😃.
