---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '8013'
original_report_id: '8013'
title: Full Path Disclosure (2)
weakness: Information Disclosure
team_handle: localize
created_at: '2014-04-18T11:22:39.643Z'
disclosed_at: '2014-04-19T03:46:46.144Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 2
tags:
- hackerone
- information-disclosure
---

# Full Path Disclosure (2)

## Metadata

- HackerOne Report ID: 8013
- Weakness: Information Disclosure
- Program: localize
- Disclosed At: 2014-04-19T03:46:46.144Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

During the import of an XML file,I edited the "file" to "url" for importing XML's through URL.So it became:
```html
<input id="importFileXML" class="form-control" type="url" name="importFileXML"></input>
```
And then I tried to import a random XML file.I tried with this:
http://www.swarthmore.edu/libraries.xml
It was not a valid XML file.And after the importing it showed the following error which discloses full path of the application.

```text
Notice: Undefined index: importFileXML in /var/www/vhosts/lvps178-77-99-228.dedicated.hosteurope.de/httpdocs_localize/index.php on line 421 
```

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
