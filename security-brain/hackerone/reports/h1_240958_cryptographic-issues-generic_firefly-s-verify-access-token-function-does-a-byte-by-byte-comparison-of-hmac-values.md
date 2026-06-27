---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '240958'
original_report_id: '240958'
title: Firefly's verify_access_token() function does a byte-by-byte comparison of
  HMAC values.
weakness: Cryptographic Issues - Generic
team_handle: yelp
created_at: '2017-06-17T10:03:52.550Z'
disclosed_at: '2017-07-10T16:42:06.997Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 7
tags:
- hackerone
- cryptographic-issues-generic
---

# Firefly's verify_access_token() function does a byte-by-byte comparison of HMAC values.

## Metadata

- HackerOne Report ID: 240958
- Weakness: Cryptographic Issues - Generic
- Program: yelp
- Disclosed At: 2017-07-10T16:42:06.997Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Dear Yelp bug bounty team,

# Summary
---

[Firefly](https://github.com/Yelp/firefly) is vulnerable to timing attacks, because the `verify_access_token()` function performs a byte-by-byte comparison, which terminates early when two characters do not match.

Timing attacks are a type of side channel attack where one can discover valuable information by recording the time it takes for a cryptographic algorithm to execute.

~~~python
def verify_access_token(token, key):
    """Verify that the given access token is still valid. Returns true if it is,
    false if it either failed to validate or has expired.
    A token is a combination of a unix timestamp and a signature"""
    t = token[:15]
    signature = token[15:]
    expected_signature = hmac.new(key, msg=t, digestmod=hashlib.sha1).hexdigest()
    return signature == expected_signature and int(t) >= int(time.time())
~~~

The `==` operation does a byte-by-byte comparison of two values and as soon as the two differentiate it terminates. This means the longer it takes until the operation returns, the more correct characters the attacker has guessed. An attacker can then create a valid HMAC without knowing the HMAC key.

# How can this be fixed?
---

You have already imported the hmac module, so this fix simply consists of changing one line.

~~~diff
def verify_access_token(token, key):
    """Verify that the given access token is still valid. Returns true if it is,
    false if it either failed to validate or has expired.
    A token is a combination of a unix timestamp and a signature"""
    t = token[:15]
    signature = token[15:]
    expected_signature = hmac.new(key, msg=t, digestmod=hashlib.sha1).hexdigest()
-   return signature == expected_signature and int(t) >= int(time.time())
+   return hmac.compare_digest(signature, expected_signature) and int(t) >= int(time.time())
~~~

The `hmac.compare_digest()` function does not terminate as soon as two bytes are not the same.

If you would like me to submit a PR to address this issue, I would be more than happy to do that.

Best regards,
Ed

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
