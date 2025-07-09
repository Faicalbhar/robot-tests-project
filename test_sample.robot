*** Settings ***
Library    OperatingSystem

*** Test Cases ***
Passing Test
    Log    This test will pass

Failing Test
    Fail    This test is intentionally failed
