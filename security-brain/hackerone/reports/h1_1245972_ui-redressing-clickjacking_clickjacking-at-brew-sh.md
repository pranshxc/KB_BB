---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1245972'
original_report_id: '1245972'
title: clickjacking at  brew.sh
weakness: UI Redressing (Clickjacking)
team_handle: homebrew
created_at: '2021-06-28T03:40:59.332Z'
disclosed_at: '2021-06-28T09:56:01.004Z'
has_bounty: false
visibility: full
substate: not-applicable
vote_count: 2
tags:
- hackerone
- ui-redressing-clickjacking
---

# clickjacking at  brew.sh

## Metadata

- HackerOne Report ID: 1245972
- Weakness: UI Redressing (Clickjacking)
- Program: homebrew
- Disclosed At: 2021-06-28T09:56:01.004Z
- Has Bounty: No
- Visibility: full
- Substate: not-applicable

## Original Report

hello ,
While performing security testing of your website i have found the vulnerability called Clickjacking.
URL is in scope and vulnerable to Clickjacking.
What is Clickjacking ?
Clickjacking (User Interface redress attack, UI redress attack, UI redressing) is a malicious technique of tricking a Web user into clicking on something different from what the user perceives they are clicking on, thus potentially revealing confidential information or taking control of their computer while clicking on seemingly innocuous web pages.
The server didn't return an X-Frame-Options header which means that this website could be at risk of a clickjacking attack. The X-Frame-Options HTTP response header can be used to indicate whether or not a browser should be allowed to render a page in a <frame> or <iframe>. Sites can use this to avoid clickjacking attacks, by ensuring that their content is not embedded into other sites.
vulnerable url:
https://brew.sh/
no x-frames in the above website 
For POC we can use either the html script or burpsuite
script:
<html lang="en-US">
<head>
<meta charset="UTF-8">
<title>I Frame</title>
</head>
<body>
<h3>clickjacking vulnerability</h3>
<iframe src="https://brew.sh" width="700px"></iframe>
</body>
</html>

## Impact

Using a similar technique, keystrokes can also be hijacked. With a carefully crafted combination of stylesheets, iframes, and text boxes, a user can be led to believe they are typing in the password to their email or bank account, but are instead typing into an invisible frame controlled by the attacker.

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
