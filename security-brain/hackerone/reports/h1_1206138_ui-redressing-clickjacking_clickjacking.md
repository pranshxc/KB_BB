---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1206138'
original_report_id: '1206138'
title: Clickjacking
weakness: UI Redressing (Clickjacking)
team_handle: sifchain
created_at: '2021-05-23T03:36:51.891Z'
disclosed_at: '2021-12-09T17:48:36.397Z'
has_bounty: false
visibility: full
substate: spam
vote_count: 2
tags:
- hackerone
- ui-redressing-clickjacking
---

# Clickjacking

## Metadata

- HackerOne Report ID: 1206138
- Weakness: UI Redressing (Clickjacking)
- Program: sifchain
- Disclosed At: 2021-12-09T17:48:36.397Z
- Has Bounty: No
- Visibility: full
- Substate: spam

## Original Report

Bug Bounty Report(Vulnerability Report)

Vulnerability Name:  UI Redressing (Clickjacking)

Vulnerability Description:  Clickjacking (classified as a User Interface redress attack, UI redress attack, UI redressing) is a malicious technique of tricking a user into clicking on something different from what the user perceives, thus potentially revealing confidential information or allowing others to take control of their computer while clicking on seemingly innocuous objects, including web pages.Clickjacking is an instance of the confused deputy problem, wherein a computer is tricked into misusing its authority.

Summery: The below listed links, dont have X-FRAME-OPTIONS set to DENY or SAMEORIGIN so they are vulnerable to clickjacking

Vulnerable Website: https://sifchain.finance/

Beowser Verified in:Firefox[Version: 78.3.0esr (64-bit)]

Steps To Reproduce: 
       i. Here are the steps to reproduce the attack:
     1.Run the bellow code from browser and you can see that the website is vulnerable to clickjacking attack
<!doctype html>
<html>
 <head> 
  <style>
      iframe{
        width:500px;
        height:900px;
      }
      #http{
        height:900px;
        width:500px;
      }
  </style> 
 </head> 

 <body> 
  <h1>--------------------This is a malicious website-------------------</h1>
  <h1>The vulnerable website:-</nn></h1>
  <iframe src="https://sifchain.finance/"></iframe>
  <iframe id="http" src="https://dex.sifchain.finance/#/peg"></iframe>
 </body>
</html>

this html code can embed these urls  on another malicious website whice can be harmful for 
users.


Following links are vulnerable to Clickjacking:
1.https://sifchain.finance/
2.https://dex.sifchain.finance/#/peg
3.https://blockexplorer.sifchain.finance/voting-power-distribution
4.https://blockexplorer.sifchain.finance/transactions
5.https://dex.sifchain.finance/#/stake-delegate
6.https://dex.sifchain.finance/#/swap
7.https://dex.sifchain.finance/#/pool/add-liquidity
8.etc.

## Impact

Here are the impacts of the vulnerability:
 1.with this vulnerability attackers can control or hijack users clicks
2.Affect the users interaction on your platform. Such unintended behavior is definitely not wanted by any user.
3.Such effect upon your users could significantly harm your overall reputation and customer loss.
4.Using a similar technique, keystrokes can also be hijacked. With a carefully crafted combination of stylesheets, iframes, and text boxes, a user can be led to believe they are typing in the password to their email or bank account, but are instead typing into an invisible frame controlled by the attackerp

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
