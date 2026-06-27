---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '504731'
original_report_id: '504731'
title: Predictable Random Number Generator
weakness: Use of Cryptographically Weak Pseudo-Random Number Generator (PRNG)
team_handle: nextcloud
created_at: '2019-03-04T10:43:54.221Z'
disclosed_at: '2019-06-26T15:34:05.876Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 12
asset_identifier: com.nextcloud.client
asset_type: GOOGLE_PLAY_APP_ID
max_severity: medium
tags:
- hackerone
- use-of-cryptographically-weak-pseudo-random-number-generator-prng
---

# Predictable Random Number Generator

## Metadata

- HackerOne Report ID: 504731
- Weakness: Use of Cryptographically Weak Pseudo-Random Number Generator (PRNG)
- Program: nextcloud
- Disclosed At: 2019-06-26T15:34:05.876Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

Description:
The mobile application uses a predictable Random Number Generator (RNG).
Under certain conditions this weakness may jeopardize mobile application data encryption or other protection based on randomization. For example, if encryption tokens are generated inside of the application and an attacker can provide application with a predictable token to validate and then execute a sensitive activity within the application or its backend.

Example of insecure code:
Random random = new Random();
byte bytes[] = new byte[20];
random.nextBytes(bytes);

Example of secure code:
SecureRandom random = new SecureRandom();
byte bytes[] = new byte[20];
random.nextBytes(bytes);

Details:
There is 'new Random()' found in file 'org/jsoup/helper/DataUtil.java':
line 211:         StringBuilder stringBuilder = new StringBuilder(32);

line 212:         Random random = new Random();

line 213:         for (int i = 0; i < 32; i++) {
There is 'new Random()' found in file 'com/owncloud/android/ui/notifications/NotificationUtils.java':
line 31:         stringBuilder.append("NotificationDelayerThread_");

line 32:         stringBuilder.append(new Random(System.currentTimeMillis()).nextInt());

line 33:         HandlerThread handlerThread = new HandlerThread(stringBuilder.toString(), 10);
There is 'new Random()' found in file 'com/owncloud/android/jobs/MediaFoldersDetectionJob.java':
line 48:     public static final String TAG = "MediaFoldersDetectionJob";

line 49:     private Random randomId = new Random();

line 50:
There is 'new Random()' found in file 'com/owncloud/android/authentication/AuthenticatorActivity.java':
line 1672:             stringBuilder2.append("OAuth_user");

line 1673:             stringBuilder2.append(new Random(System.currentTimeMillis()).nextLong());

line 1674:             str = stringBuilder2.toString();


Reference:
https://developer.android.com/reference/java/util/Random.html
https://developer.android.com/reference/java/security/SecureRandom.html

## Impact

When a non-cryptographic PRNG is used in a cryptographic context, it can expose the cryptography to certain types of attacks.

Often a pseudo-random number generator (PRNG) is not designed for cryptography. Sometimes a mediocre source of randomness is sufficient or preferable for algorithms that use random numbers. Weak generators generally take less processing power and/or do not use the precious, finite, entropy sources on a system. While such PRNGs might have very useful features, these same features could be used to break the cryptography.

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
