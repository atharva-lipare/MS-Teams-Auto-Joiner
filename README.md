# MS-Teams-Auto-Joiner

![banner](banner.png)

## This python script will automatically join the most recent scheduled Microsoft Teams meeting appearing in your Teams calendar.

## Features:
- This python script will automatically open a chrome tab, enter your username, your password, open the calender tab and then join a meeting if available.
- Before joining any meeting, it will by default turn off your camera and microphone.
- After the organiser ends the meeting, it will open the calendar tab to look for new meetings and join the next meeting if available.

## Requirements:
- [Python3](https://www.python.org/downloads/)

## Prerequisites:
### After cloning the repo, go in the repo directory and then follow below steps:
- Step 1:
    Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

- Step 2:
    Modify login credentials in [config.json](config.json):
    ```json
    {
    "username":"email@domain.com",
    "password":"password"
    }
    ```
## Usage:
- Step 3:
    Run [autoJoin.py](autoJoin.py):
    ```bash
    python autoJoin.py
    ```

## Sample Scenario:
- You have a meeting at 9 A.M, you may run the script anytime before 9 A.M and the script will automatically join the meeting at 9 A.M.
- The script will then automatically join the meeting scheduled at eg:- 10 A.M after the organiser ends the meeting.
- However it will not leave the meeting automatically, ONLY IF the organiser DOES NOT END the meeting i.e if the organiser leaves the meeting instead of ending the meeting. (Corresponding feature will be added shortly.)
- If the organiser does not end the meeting i.e tells the attendee to leave the meeting, the user / attendee will have to manually end the meeting. After which the script will join future meetings as scheduled as long as the script is running.

## Troubleshooting:
- If your internet connection is slow, increase the sleepDelay and timeOutDelay variable on line 8 of [autoJoin.py](autoJoin.py). The default value is set to 2 and 60 seconds respectively.
- If you get the following error:- ```selenium.common.exceptions.StaleElementReferenceException: Message: stale element reference: element is not attached to the page document``` ; increase the sleepDelay.
- Please refer to the ample resources on the internet if facing issues with installing python3 or the dependencies in [requirements.txt](requirements.txt)

## Contributing:
- When contributing to this repository, please first discuss the change you wish to make via issue with the owner(s) of this repository before making a change.
