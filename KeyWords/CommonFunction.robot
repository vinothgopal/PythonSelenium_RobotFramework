*** Settings ***
Library           Selenium2Library
Library           String
Library           Collections
Library           Screenshot
Library           Process
Library           OperatingSystem
Library           ../Functions/Config.py
Library         ../Functions/Keywords.py
Resource          ../Configurtion/Config.txt
*** Variables ***
${LOGIN URL}      https://www.google.com/
${BROWSER}        Chrome

*** Keywords ***
Login
    [Arguments]    ${userName}    ${passWord}
    Open Browser    ${LOGIN URL}    ${BROWSER}
    log    ${userName}
    log    ${passWord}
    maximize_browser
    enterGoogle
