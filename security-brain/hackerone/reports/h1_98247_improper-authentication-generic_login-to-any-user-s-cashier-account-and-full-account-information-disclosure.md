---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '98247'
original_report_id: '98247'
title: login to any user's cashier account and full account information disclosure
weakness: Improper Authentication - Generic
team_handle: deriv
created_at: '2015-11-06T12:03:55.131Z'
disclosed_at: '2015-11-14T21:36:47.469Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 21
tags:
- hackerone
- improper-authentication-generic
---

# login to any user's cashier account and full account information disclosure

## Metadata

- HackerOne Report ID: 98247
- Weakness: Improper Authentication - Generic
- Program: deriv
- Disclosed At: 2015-11-14T21:36:47.469Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hi , I have found an  issue allowing an attacker to login to any user's cashier account and view sensitive user information by just knowing the user account ID.
#Steps to reproduce:
1. open 2 browsers and create 2 accounts , login with each account on a browser.
2. let's call account 1 , the victim and account 2 is the attacker.
3. from the victim account , make sure you are using real account and then go to https://www.binary.com/cashier then click **Deposit** then click **Continue**. 

4. From the attacker account go to https://www.binary.com/cashier then click **Deposit** then click **Continue**. 
5. Now you'll see your cashier account , inspect the page elements using your browser inspector then find the `<iframe>` tag with the id attribute **cashiercont**. it will look like this : 

```
<iframe src="https://cashier.binary.com/login.asp?Sportsbook=Binary (CR) SA USD&amp;PIN=CR342435&amp;Lang=en&amp;Password=0e552ae717a1d08cb147f132a31676559e3273ef&amp;Secret=1328d47abeda2b672b6424093c4dbc76&amp;Action=DEPOSIT" frameborder="0" width="100%" height="2000" id="cashiercont" scrolling="auto" style="padding:0px;margin:0px;"></iframe>
```
6. Edit the `<iframe>` element and Change the `PIN` parameter value to the victim account id value  so it should be like this after the edit:

```
<iframe src="https://cashier.binary.com/login.asp?Sportsbook=Binary (CR) SA USD&amp;PIN=<VICTIM_ACCOUNT_ID>&amp;Lang=en&amp;Password=0e552ae717a1d08cb147f132a31676559e3273ef&amp;Secret=1328d47abeda2b672b6424093c4dbc76&amp;Action=DEPOSIT" frameborder="0" width="100%" height="2000" id="cashiercont" scrolling="auto" style="padding:0px;margin:0px;"></iframe>
```
7. Now you have successfully logged in the victim's cashier account , to view the victim account details , click the **cashier** button then next to the **customer name** click the _view_ link and you'll see all the account details of the victim , including _Full name_ , _email_ and _phone number_ which are the most sensitive here since they can be used in phishing.

Please tell me if you are having any issue reproducing this.
Thanks

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
