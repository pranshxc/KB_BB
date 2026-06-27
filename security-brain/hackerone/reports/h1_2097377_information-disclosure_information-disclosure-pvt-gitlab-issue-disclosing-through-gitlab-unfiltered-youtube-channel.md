---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '2097377'
original_report_id: '2097377'
title: Information Disclosure - Pvt Gitlab Issue Disclosing Through GitLab Unfiltered
  YouTube channel.
weakness: Information Disclosure
team_handle: gitlab
created_at: '2023-08-05T06:03:24.413Z'
disclosed_at: '2023-09-13T15:29:31.682Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 14
asset_identifier: gitlab.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- information-disclosure
---

# Information Disclosure - Pvt Gitlab Issue Disclosing Through GitLab Unfiltered YouTube channel.

## Metadata

- HackerOne Report ID: 2097377
- Weakness: Information Disclosure
- Program: gitlab
- Disclosed At: 2023-09-13T15:29:31.682Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Dear GitLab Security Team,

I hope this message finds you well. I am writing to report a potential security vulnerability related to information disclosure on GitLab.

##Description:
During my routine usage of GitLab, I came across a video on the official GitLab Unfiltered YouTube channel that inadvertently disclosed sensitive information. The video, titled "[2023-07-25 Product Analytics Group Sync]," showcased a private issue report containing details of a security vulnerability within GitLab. This issue report should not have been publicly accessible or disclosed, as it contains potentially sensitive information.

Upon viewing the video, it was evident that the issue report contained details like specific URLs, snippets of code, and descriptions of the vulnerability. This level of information disclosure poses a significant security risk to GitLab users and potentially to GitLab itself.

##Steps to Reproduce:

1.) Visit the GitLab Unfiltered YouTube channel This Video: https://youtu.be/ndCUIp1gfsA?t=203
█████████
##Recommendation:
I strongly advise GitLab's security team to take immediate action to remove or restrict access to the video that contains the disclosed private issue report. Additionally, Plz Recheck the video Before uploading... On YouTube Channel :)

## Impact

##Impact:
The potential consequences of this information disclosure could be severe, including but not limited to:

1.) Unauthorized access to sensitive information about a security vulnerability.
2.) Possible exploitation of the disclosed vulnerability by malicious entities.
3.) Damage to the reputation of GitLab as a secure development platform.
4.) Violation of privacy and confidentiality of GitLab users who reported the issue.

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
