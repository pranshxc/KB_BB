---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '2007235'
original_report_id: '2007235'
title: insecure storage of information, you can view any file uploaded to the server
  without authentication and only with a single link
weakness: Insecure Storage of Sensitive Information
team_handle: radancy
created_at: '2023-05-31T08:15:34.424Z'
disclosed_at: '2023-08-21T14:39:07.182Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 54
asset_identifier: '*.maximum.nl'
asset_type: WILDCARD
max_severity: critical
tags:
- hackerone
- insecure-storage-of-sensitive-information
---

# insecure storage of information, you can view any file uploaded to the server without authentication and only with a single link

## Metadata

- HackerOne Report ID: 2007235
- Weakness: Insecure Storage of Sensitive Information
- Program: radancy
- Disclosed At: 2023-08-21T14:39:07.182Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

**Domain and URL:**
http://███
https://███████
https://████/maximum-wiki-prod-app/

**Summary:** 
From a single link I have access to a multitude of uploaded files on the server. All I have to do is search for keywords such as "png" or "user" and I can retrieve the target file without authentication, without blocking by the server, and without any particular effort. In short, users expose their files to anyone who has seen the public link.

**Description:** [add more details about this vulnerability]
I can download files, get personal information from users, view file extensions and view them directly in the browser from the link. I think the main vulnerability is that the site in question has given me free access to the xml file when I should simply be blocked.

## Browsers Verified In:
firefox browser 113.0.2
firefox browser 102.11.0esr
Microsoft Edge 113.0.1774.57

## Steps To Reproduce:
  1.search on google : site:*.██████████
  2. click on ████/login
  3. in a linux machine, use an tool called "gobuster" on a terminal
  4. type that commande on a terminal : gobuster dir -v -u https://███████ -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt
  5. You will see on the result : status: 301 -> https://████/uploads
  6. In a teminal use a tool called "curl".
  7. type that commande on a terminal : curl https://█████/uploads/
  8. It returned : 403 Forbidden.
  9. Put uppercase and lowercase to bypass it
  10. type that commande on a terminal : curl https://██████/uPlOaDs/
 11. Line : 103 you will see the vulnerable link : https://█████████/maximum-wiki-prod-app/uploads/images/system/2020-04/█████-Maximum_TMP_RGB-on_image.png
  12. Go on : https://████████/maximum-wiki-prod-app/ you will see all of uploads files.

## Known steps to resolve:
block the user when he try to get access to the vulnerable link

## Impact

An attacker can gain access to the website's tree structure, and thus obtain precise information to target his attacks. He could also extract information from users, and negotiate a ransom.

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
