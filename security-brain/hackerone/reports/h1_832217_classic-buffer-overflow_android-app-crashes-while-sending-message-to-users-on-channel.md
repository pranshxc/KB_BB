---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '832217'
original_report_id: '832217'
title: Android App Crashes while sending message to users/ on channel
weakness: Classic Buffer Overflow
team_handle: rocket_chat
created_at: '2020-03-26T16:15:23.098Z'
disclosed_at: '2021-03-18T13:03:48.953Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 3
tags:
- hackerone
- classic-buffer-overflow
---

# Android App Crashes while sending message to users/ on channel

## Metadata

- HackerOne Report ID: 832217
- Weakness: Classic Buffer Overflow
- Program: rocket_chat
- Disclosed At: 2021-03-18T13:03:48.953Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

## Description
 I found a security vulnerability in Rocket's latest android app by which I was able to remotely crash any  user’s app  instantly just by just sending a simple message in private or in channel. The vulnerability  require the victim open the message. 


## Devices and Versions

Rocket.Chat.Android version: (e.g. 4.5.1)
Mobile device model and OS version: (tested on :+1: -- " **Android 6.0, 8.0, 10.0**"), probably any other android version

## Steps to reproduce

> Create new #test channel
> Send POC Code onto the channel
> Open Mobile App
> App gets crashed

## POC
### Crafted code to crash mobile app
https://i.postimg.cc/zvBWdMzT/Screenshot-20200320-112405.png

### Message Preview
https://i.postimg.cc/fbCJ6KgC/Screenshot-20200320-112541.png

### App Gets Crashed
https://i.postimg.cc/26J8DXdQ/Screenshot-20200320-112711.png

### Code Link
https://pastebin.com/raw/JEDcC5Yr

**There is no such problem in iOS client and rocket web**

## Impact

An attacker could crash the internal chat user's phone, everytime he/she opens the rocket chat , i.e posting crafted code on #general channel

Hi, i even posted the issue on github, before i got to know about rocket chat on H1, but issue still not fixed, so just tryna keep you updated guys.

https://github.com/RocketChat/Rocket.Chat.ReactNative/issues/1907

## Extracted Security Notes

### Likely Vulnerability Class

*Leave this section for future enrichment.*

### Likely Root Cause

*Leave this section for future enrichment.*

### Potential Impact

*Leave this section for future enrichment.*

### Defensive Test Cases

*Leave this section for future enrichment.*

### Remediation Ideas

*Leave this section for future enrichment.*
