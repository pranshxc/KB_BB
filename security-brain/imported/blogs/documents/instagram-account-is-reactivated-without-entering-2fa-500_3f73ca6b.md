---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2019-08-21_instagram-account-is-reactivated-without-entering-2fa-500.md
original_filename: 2019-08-21_instagram-account-is-reactivated-without-entering-2fa-500.md
title: Instagram account is reactivated without entering 2FA ($500)
category: documents
detected_topics:
- mfa
- command-injection
tags:
- imported
- documents
- mfa
- command-injection
language: en
raw_sha256: 3f73ca6bbf0ef8ead00ae04f37def7088603fe6f164fa70521a018da8623bd59
text_sha256: 7bff0f0872d528cb49bb53ca62c96b60e7ff88f4d4a00756ad262aaad92bc6e2
ingested_at: '2026-06-28T07:32:00Z'
sensitivity: unknown
redactions_applied: false
---

# Instagram account is reactivated without entering 2FA ($500)

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2019-08-21_instagram-account-is-reactivated-without-entering-2fa-500.md
- Source Type: markdown
- Detected Topics: mfa, command-injection
- Ingested At: 2026-06-28T07:32:00Z
- Redactions Applied: False
- Raw SHA256: `3f73ca6bbf0ef8ead00ae04f37def7088603fe6f164fa70521a018da8623bd59`
- Text SHA256: `7bff0f0872d528cb49bb53ca62c96b60e7ff88f4d4a00756ad262aaad92bc6e2`


## Content

---
title: "Instagram account is reactivated without entering 2FA ($500)"
page_title: "Instagram account is reactivated without entering 2FA ($500) - Bug Bounty POC"
url: "https://bugbountypoc.com/instagram-account-is-reactivated-without-entering-2fa/"
final_url: "https://bugbountypoc.com/instagram-account-is-reactivated-without-entering-2fa/"
authors: ["Aman Shahid (@amansmughal)"]
programs: ["Meta / Facebook"]
bugs: ["2FA / MFA bypass", "Broken authentication"]
bounty: "500"
publication_date: "2019-08-21"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5069
---

# Instagram account is reactivated without entering 2FA ($500)

by  [Aman Shahid](https://bugbountypoc.com/author/aman/ "Posts by Aman Shahid") · Published August 21, 2019 · Updated October 9, 2023

**Description:**

When we have 2FA enabled on our Instagram account, let’s say I have an Instagram account with 2FA enabled. If I deactivate it for any reason, such as choosing to deactivate my Instagram account instead of deleting it to prevent others from viewing my Instagram profile or accessing its data an attacker can reactivate it using my credentials and without needing 2FA. I’ve noticed that if the 2FA-enabled Instagram account is deactivated and an attacker obtains access to its credentials, they can reactivate the account without needing the 2FA code. This is different from Facebook, where entering the 2FA code is required for reactivation. This discrepancy highlights a vulnerability, and it could potentially impact many users. 2FA is a crucial part of authentication, and an account should not be reactivated or any other action taken without requiring the 2FA code.

**Timline:**

**24 June, 2019:** Triaged

**18 July, 2019:** Fixed

**20 July, 2019:** Bounty awarded $500

**Twitter:** <https://twitter.com/amansmughal>
