---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '197253'
original_report_id: '197253'
title: formassembly.com is vulnerable to padding-oracle attacks.
weakness: Cryptographic Issues - Generic
team_handle: formassembly
created_at: '2017-01-10T13:38:12.460Z'
disclosed_at: '2017-03-17T16:53:51.058Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 5
tags:
- hackerone
- cryptographic-issues-generic
---

# formassembly.com is vulnerable to padding-oracle attacks.

## Metadata

- HackerOne Report ID: 197253
- Weakness: Cryptographic Issues - Generic
- Program: formassembly
- Disclosed At: 2017-03-17T16:53:51.058Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Dear Formassembly bug bounty team,

# Summary
---

formassembly.com is vulnerable to CVE-2016-2107, allowing remote attackers to obtain sensitive information via padding-oracle attacks.

~~~
$ git clone https://github.com/FiloSottile/CVE-2016-2107.git
$ go run main.go www.formassembly.com
... Vulnerable: true
~~~

The code above checks whether the TLS alert is `DATA_LENGTH_TOO_LONG` (vulnerable) or `BAD_RECORD_MAC` (not vulnerable).

# What is CVE-2016-2107?
---

Filippo Valsorda, the author of the tool I used to discover this issue, wrote a fantastic article on CVE-2016-2107 here: https://blog.cloudflare.com/yet-another-padding-oracle-in-openssl-cbc-ciphersuites/

# What are padding-oracle attacks?
---

During the decryption and the HMAC verification process the length of the padding is revealed. Padding-oracle attacks iterate over the padding of the cryptographic message, revealing the contents of the message.

# More information
---

While I am at it I may as well let you know that you also support 1024-bit Diffie-Hellman keys. I would recommend using a 2048-bit Diffie-Hellman group.

Link to GitHub repo: https://github.com/FiloSottile/CVE-2016-2107
Link to online test: https://filippo.io/CVE-2016-2107/

Yours sincerely,
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
