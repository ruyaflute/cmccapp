# CMCC App and Demo

### Demo in Django
###### Ideally: use Django to build a website to demostrate how the case management and care coordination app is going to work - I still have no idea what the app is going to look like.
- Phone number should be able to connect with cell phone and directly call patient from the app, video calling is even better. Providers can access it when it is necessary for patient.

- Address should be able to connect to google map.

- Patient categorization base on need - assessment tool(and barriers, acuity, intensity, deadline) - mental health need vs medical need

- Interpretation tool!!

- Tasks reminder for care plan implementation and creation.

- Appointment tracking-how?

- ER visit tracking-how? and follow up 

- Patient's providers tree and should be easy to use to connect virtually

- Patient's input for issues

- Resources for patient including health insurance, INN providers, social services... Reminder for patient.............................

- Assignment tool for other people to assist with specific tasks

- Event annnouncement for group meetup, etc

###### Reality: image uploaded to postgreSQL but not shown in html page; page url-id not connected. -- not important yet
#### For Case Manager
- You can directly reach to patient via phone call or video call through app. You can locate patient's address. Convenient assessment tools to identify patient's acuity level (medical and mental health assessment). Creating care plan, and tracking tool. Appointment and ER follow up (entered by patient). Provider tree and phone/video call. Assignment tool for other Case Manager. Announce group events.
#### For Patient
- Input for demographic information and medical background, Provider tree, appointment, ER visit, interpretation tool (or call), complaints/issues, Entitlement resources, group event, reminder for patient.....
#### For Providers
- Providers and care worker tree and connect, Recent medical/mental path report, ER discharge summary. Care plan/task reminder/assign to Case Manager. Able to view patient's demo, acuity level, entitlement issues.
#### Where my project idea came from
- blahhhh


### React Native

- newbie: https://snack.expo.io

- XDE was deprecated 

- reinstalled
- git --version git version 2.22.0
- npm --version 6.13.4
- node.js

- sudo npm install expo-cli --global  expo-cli@3.13.8
- Installed Watchman

- expo whoami
- expo register

- run the command `npm install`. NPM will look at the[`package.json`](/package.json) file's `dependencies` key and install those libraries

- iOS Simulator:
- Installed Xcode
- expo init my-new-project; cd my-new-project; expo start

### Git
- git init; git remote add origin https://github.com/... ; git remote -v; git add . ; git status; git commit -m ""; git push origin master; (git pull origin master --rebase)
- git init; git add .; git commit -m ""; git push
- remove all local changes, including files that are untracked by git, from working copy: git stash push --include-untracked
