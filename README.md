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
    "minimumParticipants":10
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
- If the organiser does not end the meeting i.e the organiser leaves the meeting instead of ending the meeting and tells the attendee to leave the meeting, the script will leave the meeting after the strength of the meeting falls down to 10 or any minimum value set by user.
- To set a custom condition to automatically leave the meeting change the code on line 105 of [autoJoin.py](autoJoin.py)

## Contributing:
- When contributing to this repository, feel free to discuss the change you wish to make via [Issue](https://github.com/atharva-lipare/MS-Teams-Auto-Joiner/issues) or [gitter chat room](https://gitter.im/MS-Teams-Auto-Joiner/community?utm_source=share-link&utm_medium=link&utm_campaign=share-link) before making a change.
- Add don't forget to ⭐ the repo, 😃.