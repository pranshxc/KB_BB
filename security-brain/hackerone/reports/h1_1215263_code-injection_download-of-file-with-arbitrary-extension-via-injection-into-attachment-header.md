---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1215263'
original_report_id: '1215263'
title: Download of file with arbitrary extension via injection into attachment header
weakness: Code Injection
team_handle: nextcloud
created_at: '2021-06-02T10:31:29.334Z'
disclosed_at: '2021-08-11T09:15:26.776Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 8
asset_identifier: nextcloud/mail
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
- code-injection
---

# Download of file with arbitrary extension via injection into attachment header

## Metadata

- HackerOne Report ID: 1215263
- Weakness: Code Injection
- Program: nextcloud
- Disclosed At: 2021-08-11T09:15:26.776Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Description
-----------

When downloading mail attachments, the app fails to properly escape quotes in the content disposition header. Because of this, an attacker can send a victim a file with a benign extension such as `.txt` or `.png` which when downloaded will be stored with a malicious extension such as `.bat` or `.docm`. 

This vulnerability can for example be exploited in the following scenarios:

- It allows bypassing of extension-based attachment filtering by email providers (or other intermediate email systems), as is common in many networks.
- As the attachment is displayed as a benign file in Nextcloud, a user may incorrectly trust it to be a benign file.


POC
---

- Send a mail to an email address that is connected to Nextcloud Mail with an attached file called `test.bat".png`. 
- open the mail -> click on the attachment icon -> click on the download icon. While Nextcloud correctly displays the file as a benign `.png` file, it will be downloaded as `test.bat` instead.  

Tested with Firefox under Windows.

As alternative to `.bat` files (which may be prevented from executing by Microsoft Defender SmartScreen), an attacker can also send other malicious files such as for example `.vbs` files, as well as `.docm` files containing macro viruses.


Request
-------

```
    GET /nextcloud/index.php/apps/mail/api/messages/26/attachment/2 HTTP/1.1
    Host: 192.168.0.101

    HTTP/1.1 200 OK
    [...]
    Content-Disposition: attachment; filename="test.bat".png"
    [...]
    Content-Type: application/octet-stream

    C:\Windows\system32\calc.exe
```

Solution
--------

Quotes should be properly escaped before being inserted into the Content-Disposition header.

## Impact

Offering malicious files for download, leading to code execution on the computer of the victim if they download and open the file.

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
