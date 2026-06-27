---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '147744'
original_report_id: '147744'
title: Back Refresh Attack after registration and successful logout
weakness: Violation of Secure Design Principles
team_handle: mailru
created_at: '2016-06-27T17:22:35.746Z'
disclosed_at: '2016-07-01T09:11:10.034Z'
has_bounty: false
visibility: full
substate: not-applicable
vote_count: 4
tags:
- hackerone
- violation-of-secure-design-principles
---

# Back Refresh Attack after registration and successful logout

## Metadata

- HackerOne Report ID: 147744
- Weakness: Violation of Secure Design Principles
- Program: mailru
- Disclosed At: 2016-07-01T09:11:10.034Z
- Has Bounty: No
- Visibility: full
- Substate: not-applicable

## Original Report

About the vulnerability:

The back, forward and refresh buttons of the browser can be used to steal the password of a previous user. In this article we examine the vulnerability and look at ways to solve them.A web browser has the functionality to store the recent pages browsed by the user in its history. The back and forward buttons on the browser make use of this history to display the pages that the user visited recently. The browser also keeps track of the variables that were sent as part of the request to the server for each page. The refresh feature of the browser automates posting of the variables to the server thereby greatly improving the user experience while browsing.These features enhance the user experience but at the same time they expose a high risk vulnerability. This happens due to the application being insecurely designed. Attackers exploit these functionalities of the browser to obtain access to user credentials. Let’s see how this works and the solutions to overcome this problem.

Steps to reproduce: (Attached is the live POC)

 1.Go to https://m.my.mail.ru/cgi-bin/my/registration
2. Complete the registration process.
3. You will be logged in to the application
4. Logout from the application
At this point of time the victim will leave the system as he is insure he has already logged out.

Now the attacker comes and do the following activities. 
5. Pressed the back button twice, 
6. Now it asks me to resubmit the details.
7.Credentials got captured in Burpsuite.

How to Fix:

1. use an intermediate page between the login page and the first page displayed after authentication (myhome.asp in this case). This intermediate page should be used to redirect the user via an “HTTP Redirect command” to myhome.asp after successful login. In such a scenario, the login request is redirected immediately by the intermediate page. 
2, use a salted hash technique for authentication. In this method, the password is hashed before sending it to the server. This hash is made random using a salt (a random value) provided by the server. This salt is added to the hash generated from the password and then hashed again. This salted hash is sent to the server for authentication. This way, even if the attacker uses the refresh button to capture the request, only the salted hash value will be visible. It will not allow the attacker to login by refreshing as the salt would change at the next login.

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
