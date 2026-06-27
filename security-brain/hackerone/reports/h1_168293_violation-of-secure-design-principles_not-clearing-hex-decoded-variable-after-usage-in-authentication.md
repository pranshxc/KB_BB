---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '168293'
original_report_id: '168293'
title: Not clearing hex-decoded variable after usage in Authentication
weakness: Violation of Secure Design Principles
team_handle: paragonie
created_at: '2016-09-14T11:57:21.746Z'
disclosed_at: '2016-11-03T04:57:58.979Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 2
tags:
- hackerone
- violation-of-secure-design-principles
---

# Not clearing hex-decoded variable after usage in Authentication

## Metadata

- HackerOne Report ID: 168293
- Weakness: Violation of Secure Design Principles
- Program: paragonie
- Disclosed At: 2016-11-03T04:57:58.979Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

All the sensitive information variables are zeroed from memory, expect the hex2bin value of "validator".

https://github.com/paragonie/airship/blob/8f04f071c414c3893cf66311839d20a343af1237/src/Engine/Security/Authentication.php#L223-L236

```
        $stored = \Sodium\hex2bin($record[$f['validator']]);
        \Sodium\memzero($record[$f['validator']]);
        if (!\hash_equals($stored, $val)) {
            throw new LongTermAuthAlert(
                \trk('errors.security.invalid_persistent_token')
            );
        }
        $userID = (int) $record[$f['userid']];
        $_SESSION['session_canary'] = $this->db->cell(
            'SELECT session_canary FROM airship_users WHERE userid = ?',
            $userID
        );
        return $userID;
```

The encoded value of "validator" is zeroed from memory, but the **decoded** version is not.
The value of $stored is not returned anywhere, so it should be zeroed from memory.

Note. As the exception throw stops the flow, it should *also* be cleared when the hash doesn't equal 👍

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
