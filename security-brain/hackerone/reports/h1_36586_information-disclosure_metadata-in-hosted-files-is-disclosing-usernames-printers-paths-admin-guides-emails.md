---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '36586'
original_report_id: '36586'
title: Metadata in hosted files is disclosing Usernames, Printers, paths, admin guides.
  emails
weakness: Information Disclosure
team_handle: qiwi
created_at: '2014-11-18T13:25:00.156Z'
disclosed_at: '2015-01-18T15:11:34.562Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 3
tags:
- hackerone
- information-disclosure
---

# Metadata in hosted files is disclosing Usernames, Printers, paths, admin guides. emails

## Metadata

- HackerOne Report ID: 36586
- Weakness: Information Disclosure
- Program: qiwi
- Disclosed At: 2015-01-18T15:11:34.562Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

Hi
- vulnerable hosts;
agent.qiwi.com
static.qiwi.com
visa.qiwi.com
w.qiwi.com
www.qiwi.com

• the type of vulnerability;
Information disclosure

• where exactly;
There are multiple locations for documents with valuable metadata attached.
These are both Qiwi documents and documents uploaded by agents/clients of yours.
Please see filelocations.txt for a list of locations.
Please see folders, usernames, software, printers, and emails.txt for a list of metadata retrieved from the documents.
Separately, these documents possibly should be restricted:
https://w.qiwi.com/business/agents/files/QIWIPos_Ingenico_AdminGuide.pdf	
https://w.qiwi.com/business/agents/files/QIWIPos_PAX_AdminGuide.pdf	
https://w.qiwi.com/business/agents/files/QIWIPos_Nurit_AdminGuide.pdf
Please note: the folders file contains two usernames as they are entered, which will give an attacker insight into how usernames are formed.

• security impact;
This information will aid an attacker greatly. 
The information can be used by a hacker to; 
- attempt to brute force qiwi employee logins with valid usernames already supplied
- send phishing emails to valid email addresses
- target malware to known applications (especially pdf tools)
- attack printers
- attack server shares
- attack potentially cohosted websites
- discover configuration steps and versions of software installed (such as QIWI POS INGENICO 2.10)

E.g if i know a number of users are using Adobe Distiller 7.0.5 (which is out of date) an attacker could spear-phish users with an exploit pdf targetting this software.

• steps impact;
When a file is uploaded to the website, metadata is preserved. Metadata in a file can include anything from servernames to passwords.
Due to the fact that this information is readily available via a google search (inurl:qiwi.com filetype:.pdf for example) this would be easy for an attacker to discover.

• recommendations for fixing.
Remove all metadata before a file is uploaded.
Also restrict access to sensitive files such as https://w.qiwi.com/business/agents/files/QIWIPos_Nurit_AdminGuide.pdf)

Any more information required, please let me know.

Thanks!
Jamie

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
