# CSP TelCo Tools Slack App
**Self Hosting**
To self host this app, you will need to create a Slack App and set up the necessary environment variables. You can follow the steps below to set up the app:
1. Create a new Slack App in your workspace.
2. Add the following Slash Commands to your app:
   - /lookup-cnam
   - /lookup-lrn
   - /lookup-cnam-private
   - /lookup-lrn-private
3. Set the Request URL for each command to the endpoint where your app will be hosted (e.g., https://yourdomain.com/slack/events).
4. ``git clone https://github.com/csptechnologies/slacktelcotools.git``
5. ``pip3 install -r requirements.txt``
6. Configure the .env file
7. (six seven lol), run main.py ``python3 main.py``


**Purpose**
This slack app lets you look up the location routing number and the CNAME for a given phone number, which the information is provided by [CSP Technologies](https://csptech.org) API

**Commands**
/lookup-cnam - Looks up the CNAME for a given phone number
/lookup-lrn - Looks up the LRN for a given phone number
/lookup-cnam-private - Looks up the CNAME for a given phone number and responds privately
/lookup-lrn-private - Looks up the LRN for a given phone number and responds privately

**Usage (Examples)**
/lookup-cnam 19402776677
/lookup-lrn 19402776677
/lookup-cnam-private 19402776677
/lookup-lrn-private 19402776677

**Troubleshooting**
If you encounter any issues while using the app, please ensure that you are providing a valid **11** Digit US phone number. The app only supports Toll Free and United States numbers. If the issue persists, please contact the ryan@csptech.org for further assistance.

API Terms of service
You are permitted to use the CSP API found in the source code for personal usage, with the exceptions:
    - You may not mass lookup ranges
    - You may not use the API for commercial purposes without permission from CSP Technologies
    - You may not use the API for stalking purposes
