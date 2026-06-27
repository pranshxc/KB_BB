---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '218324'
original_report_id: '218324'
title: An unsafe design practice in the Passphrase may result in Secret being accidentally
  changed.
weakness: Violation of Secure Design Principles
team_handle: phabricator
created_at: '2017-04-03T15:46:42.562Z'
disclosed_at: '2017-04-04T05:10:38.594Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 2
tags:
- hackerone
- violation-of-secure-design-principles
---

# An unsafe design practice in the Passphrase may result in Secret being accidentally changed.

## Metadata

- HackerOne Report ID: 218324
- Weakness: Violation of Secure Design Principles
- Program: phabricator
- Disclosed At: 2017-04-04T05:10:38.594Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

Summary:
An unsafe design practice in the Passphrase may result in Secret being accidentally changed.
Preface:
If a user wants to share his/hers secrets, he/she may use the Passphrase. But when he/she created the credential and setted who can view it and who can edit it, they will soon discover that if they not set the edit permission to the one they want to share secret with, it is impossible success. Naturally, they would give the edit permission to everyone they want to share the secret with. So, here is the problem. It means they can change the secret. If someone ignores the edit records, he/she may under attack inadvertently. Because the secret has been modified.
Reproduction steps:
Open three different browsers (to simulate three different users)
BROWSER A: Log in as user A
BROWSER B: Log in as user B
BROWSER C: Log in as user C
BROWSER A: Go to the Passphrase and create new credential. Make it visible to both user A user B and user C. Make it editable to only user A.
BROWSER B: Open the https://yourdomain.com/K1(your id) and discover it is impossible to show the secret.
BROWSER A: Make it editable to both user A user B and user C.
BROWSER B: User B can see the secret and can change it.
BROWSER C: Open the https://yourdomain.com/K1(your id) but only can see the the secret has been modified.

Please fix it right away.

Best regards,
Kevin C.

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
