---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1176104'
original_report_id: '1176104'
title: Vulnerable for clickjacking attack
weakness: UI Redressing (Clickjacking)
team_handle: sifchain
created_at: '2021-05-07T20:41:20.747Z'
disclosed_at: '2021-05-08T06:41:13.309Z'
has_bounty: false
visibility: full
substate: duplicate
vote_count: 6
tags:
- hackerone
- ui-redressing-clickjacking
---

# Vulnerable for clickjacking attack

## Metadata

- HackerOne Report ID: 1176104
- Weakness: UI Redressing (Clickjacking)
- Program: sifchain
- Disclosed At: 2021-05-08T06:41:13.309Z
- Has Bounty: No
- Visibility: full
- Substate: duplicate

## Original Report

## Summary:
Hii Team,
I know that I have reported to you outside of Scope. The report is related to the mentioned company and the vulnerability can endanger your business so I  report this vulnerability to you.
Clickjacking (User Interface redress attack, UI redress attack, UI redressing) is a malicious technique of tricking a Web user into clicking on something different from what the user perceives they are clicking on, thus potentially revealing confidential information or taking control of their computer while clicking on seemingly innocuous web pages.
The server didn't return an X-Frame-Options header which means that this website could be at risk of a clickjacking attack. The X-Frame-Options HTTP response header can be used to indicate whether or not a browser should be allowed to render a page in a <frame> or <iframe>. Sites can use this to avoid clickjacking attacks, by ensuring that their content is not embedded into other sites.
This vulnerability affects the Web Server.

## Steps To Reproduce:
  1.Copy URL: https://sifchain.finance
  2. put the URL in the below code of the iframe

<html>
<head>
<title>Clickjack test page</title>
</head>
<body>
<p>Website is vulnerable to clickjacking!</p>
 <iframe src="https://sifchain.finance/" width="1000" height="600"></iframe>
</body>
</html>

  3. Observe that site is getting displayed in Iframe

## Impact

With a carefully crafted combination of stylesheets, iframes, and text boxes, a user can be led to believe they are typing in the password to their email or bank account, but are instead typing into an invisible frame controlled by the attacker.

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
