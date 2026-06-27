---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '7036'
original_report_id: '7036'
title: Bug in iOS application which could lead to unauthorised access.
weakness: Improper Authentication - Generic
team_handle: irccloud
created_at: '2014-04-11T04:48:36.732Z'
disclosed_at: '2014-05-15T14:16:41.277Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 5
tags:
- hackerone
- improper-authentication-generic
---

# Bug in iOS application which could lead to unauthorised access.

## Metadata

- HackerOne Report ID: 7036
- Weakness: Improper Authentication - Generic
- Program: irccloud
- Disclosed At: 2014-05-15T14:16:41.277Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hi,

The file under the Preferences folder within the iOS application stores sensitive information: com.irccloud.IRCCloud.plist. This file stores the user's authenticated session identifier. Stealing this information would allow unauthorised access to a user's account.

The content of the file can be seen in the file attached to this report.

This file is accessible from the phone even while the phone is locked with a passcode suggesting that the application does not secure the file using the appropriate data protection class.

This can also be verified by using the tool available at the following link:

https://github.com/ciso/ios-dataprotection/

If a user is logged into the application, all that an attacker needs to do is surreptitiously take the phone and dump the file within the folder. This would work while the phone is locked and does not require the phone to be jailbroken.

I should also mention that I haven't looked through all the files, but any sensitive file with the Protection class set to anything other than NSFileProtectionComplete would be extractable from the iPhone without requiring the passcode.

If you would like to test this, you can use the ios-data protection tool mentioned above or extract the data with iExplorer (Demo version) while the phone is locked and the user logged in.

More information regarding data protection is available here:

https://developer.apple.com/library/ios/documentation/iPhone/Conceptual/iPhoneOSProgrammingGuide/AdvancedAppTricks/AdvancedAppTricks.html#//apple_ref/doc/uid/TP40007072-CH7-SW24

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
