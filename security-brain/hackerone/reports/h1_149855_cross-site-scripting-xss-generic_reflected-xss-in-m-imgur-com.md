---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '149855'
original_report_id: '149855'
title: Reflected XSS in m.imgur.com
weakness: Cross-site Scripting (XSS) - Generic
team_handle: imgur
created_at: '2016-07-07T21:02:59.894Z'
disclosed_at: '2017-10-07T21:29:45.620Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 49
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# Reflected XSS in m.imgur.com

## Metadata

- HackerOne Report ID: 149855
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: imgur
- Disclosed At: 2017-10-07T21:29:45.620Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

There is a reflected XSS vulnerability in https://m.imgur.com as shown below:

https://m.imgur.com/account/testcatplzignore%22%3E%3Cimg%20src=x%20onerror=prompt(document.domain)%3E/messages

It appears that the username field in the url does not sanitize angle bracket characters on the mobile version of the site, allowing an attacker to execute arbitrary Javascript on the m.imgur.com domain.

I have attached several screenshots demonstrating this attack in the mobile context. While this attack affects devices loading the mobile site, I did notice that requests made with the standard User-Agent would issue a 302 redirect to the standard site, throwing a 404 error. This attack does execute on browsers that load the mobile version of the site.

The impact of this vulnerability is variable, depending on how it is used. An attacker could use this vulnerability to target a specific victim or post it on a site such as reddit, which is frequented by users of this application. If an authenticated imgur user could be tricked into clicking the link it may result in malicious JavaScript executing in the context of the user's session and could result in credential/session theft or other targeted attacks. This could result in multiple compromised accounts.

This vulnerability was tested in Google Chrome Version 51.0.2704.103 using the following User-Agent from the developer tools to load the mobile site:

User-Agent: Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.76 Mobile Safari/537.36

To mitigate this vulnerability, consider encoding any angle brackets (< >) reflected back to the user when handling user input.

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
