*** Settings ***
Library           Selenium2Library
Library           String
Library           Collections
Library           Screenshot
Library           Process
Library           OperatingSystem
Library           ../Functions/Config.py
Library           ../Functions/Login.py
Resource          ../KeyWords/CommonFunction.robot
Resource          ../Configurtion/Config.txt
Variables         ../Functions/returnData.py    RIDE_DEMO\\DemoProject\\DataSheet\\TestData.xlsx

*** Variables ***
${LOGIN URL}      https://www.facebook.com/
${BROWSER}        Chrome
${url1}           ${url}

*** Test Cases ***
TestCase1
    Login    ${${TEST_NAME}.UserName}    ${${TEST_NAME}.Password}

TestCase2
    Open Browser    ${url}    ${BROWSER}
    loginhexaware
TestCase3
    Open Browser    ${url}    ${BROWSER}
    maximize_browser
    LoginFBandVerifyTitle
