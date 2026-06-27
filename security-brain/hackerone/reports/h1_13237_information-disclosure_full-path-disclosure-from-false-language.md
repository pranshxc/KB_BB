---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '13237'
original_report_id: '13237'
title: full path disclosure from false language
weakness: Information Disclosure
team_handle: localize
created_at: '2014-05-24T22:04:44.154Z'
disclosed_at: '2014-08-06T00:56:27.799Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 2
tags:
- hackerone
- information-disclosure
---

# full path disclosure from false language

## Metadata

- HackerOne Report ID: 13237
- Weakness: Information Disclosure
- Program: localize
- Disclosed At: 2014-08-06T00:56:27.799Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

https://www.localize.im/projects/3t/languages/4xX

 Fatal error: Uncaught exception 'Exception' with message 'Unknown language ID 3083' in /srv/data/web/vhosts/www.localize.im/htdocs/classes/Language.php:423 Stack trace: #0 /srv/data/web/vhosts/www.localize.im/htdocs/classes/Language.php(221): Language::getLanguageName(3083) #1 /srv/data/web/vhosts/www.localize.im/htdocs/classes/Language.php(217): Language::getLanguageNameFull(3083) #2 /srv/data/web/vhosts/www.localize.im/htdocs/classes/UI.php(1375): Language->getNameFull() #3 /srv/data/web/vhosts/www.localize.im/htdocs/classes/UI.php(208): UI::getPage_Project(Array, Array) #4 /srv/data/web/vhosts/www.localize.im/htdocs/classes/UI.php(183): UI::findPage(6, Array, Array) #5 /srv/data/web/vhosts/www.localize.im/htdocs/index.php(226): UI::getPage(6) #6 {main} thrown in /srv/data/web/vhosts/www.localize.im/htdocs/classes/Language.php on line 423

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
