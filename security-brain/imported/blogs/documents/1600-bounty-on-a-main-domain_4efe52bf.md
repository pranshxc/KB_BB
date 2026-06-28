---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2024-08-18_1600-bounty-on-a-main-domain_2.md
original_filename: 2024-08-18_1600-bounty-on-a-main-domain_2.md
title: $1600 Bounty on a Main Domain
category: documents
detected_topics:
- mfa
- otp
- command-injection
- password-reset
- information-disclosure
- mobile-security
tags:
- imported
- documents
- mfa
- otp
- command-injection
- password-reset
- information-disclosure
- mobile-security
language: en
raw_sha256: 4efe52bf37454173935fc2df6e8792a2569ea5e4bad0d389930df4c5d09a3625
text_sha256: 14329caf691a1d37635e727f862e5e4e731a2b773eb52a70150088cc25e4bef9
ingested_at: '2026-06-28T07:32:37Z'
sensitivity: unknown
redactions_applied: false
---

# $1600 Bounty on a Main Domain

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2024-08-18_1600-bounty-on-a-main-domain_2.md
- Source Type: markdown
- Detected Topics: mfa, otp, command-injection, password-reset, information-disclosure, mobile-security
- Ingested At: 2026-06-28T07:32:37Z
- Redactions Applied: False
- Raw SHA256: `4efe52bf37454173935fc2df6e8792a2569ea5e4bad0d389930df4c5d09a3625`
- Text SHA256: `14329caf691a1d37635e727f862e5e4e731a2b773eb52a70150088cc25e4bef9`


## Content

---
title: "$1600 Bounty on a Main Domain"
url: "https://medium.com/@debu8er/1600-bounty-on-a-main-domain-8c30557c0f64"
authors: ["debug (@debug50)"]
bugs: ["Session fixation", "2FA / MFA bypass", "Information disclosure", "Authentication bypass", "Open redirect"]
bounty: "1,600"
publication_date: "2024-08-18"
added_date: "2024-08-22"
source: "pentester.land/writeups.json"
original_index: 63
scraped_via: "browseros"
---

# $1600 Bounty on a Main Domain

1

debug debug
 highlighted

$1600 Bounty on a Main Domain
debug debug
Follow
3 min read
·
Aug 19, 2024

474

4

Hello, I am debu8er, and I want to explain how I found some bugs in an RDP program.

A while ago, I started reporting bugs on a VDP program with the goal of triaging 20 bugs. During that time, I read write-ups and watched videos to learn more. One of the videos I watched was by Sean (zseano) on YouTube titled “PUTTING YOUR MIND TO IT: BUG BOUNTIES FOR 12 MONTHS.”

I received a private invite to a program with a wildcard scope (.redacted.com). Instead of discovering subdomains, I focused solely on the main domain. After testing function by function without any results, I continued working with the program. After three weeks, I finally found my first RDP bug.

Bug 1: Open Redirect (duplicate)

After logging out, the user is redirected to https://www.redacted.com/login?redirectTo=/account. During the login process, if the URL contains ?redirectTo=/account, the user will be redirected accordingly.

Steps to Reproduce

I tried changing the value to https://www.redacted.com/login?redirectTo=https://evil.com and logged in, but it didn’t work.
Then I tried https://www.redacted.com/login?redirectTo=//evil.com, but it didn’t work either.
Finally, I tried https://www.redacted.com/login?redirectTo=/%0d/evil.com and boom, it worked! I was redirected to evil.com.

I reported this bug, but it was marked as duplicate, with the original report being submitted just one day earlier.

Bug 2: Authentication Bypass in Multi-Factor Authentication by Misusing Email Verification Codes for Phone Verification (300$)

For signing up in the application, email verification is not required. However, after creating an account and logging in, email verification is needed to add a phone number, change the password, or update the email. The application sends a 6-digit code (XXXXXX) to the email.

Two-Factor Request for Email:
POST /api/v1/users/two_factor_auth?email=email@gmail.com HTTP/2
Host: www.redacted.com
Cookie: cookie
Content-Length: 30

The application sends a 2FA code to the email. After confirming the code, you can change the password, phone number, etc. When attempting to change the phone number, the application sends a 2FA code to the phone number, similar to the request above.

Two-Factor Request for Phone:
POST /api/v1/users/two_factor_auth?phone=12405456545 HTTP/2
Host: www.redacted.com
Cookie: cookie
Content-Length: 30

I noticed that the application uses the same API to verify the 2FA code:

Verify Request:
POST /api/v1/users/verify_two_factor_auth HTTP/2
Host: www.redacted.com
Cookie: cookie
Content-Length: 24
Content-Type: application/json

{"otp_attempt":"116293"}

I hypothesized that after initiating phone 2FA, I could confirm the phone number using the email 2FA code.

Steps to Reproduce
Initiate the email verification to generate a new code.
Intercept the network request using Burp Suite and capture the new email verification code.
Start the phone verification process.
Modify the intercepted request to submit the new email verification code instead of the phone code.
Observe that the system accepts the email code for phone verification, completing the process erroneously.

I reported this bug and triage as Medium (6.1) and 300$ bounty

Bug 3: Premature Information Disclosure Post-Email and Password Authentication ($300)

I found this bug on a subdomain, but the subdomain is part of the main website, and I didn’t perform subdomain discovery.

Get debug debug’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

After entering the email and password, the application sends a 2FA code. Upon submitting the 2FA code

I noticed that the login response(before confirming the 2FA code) leaks account information such as name, last name, username, secret token, phone number, PIN, and address. Although I couldn’t modify this information, I was able to view it without needing to complete the 2FA process, Just by submit username and password.

Steps to Reproduce
Navigate to the login page of https://few.redacted.com/login.
Enter valid email and password credentials.
Observe the HTTP response from the server which includes sensitive user information before the 2FA code is requested or entered.

I reported this and it was triaged as Medium (4.4) with a $300 bounty.

Bug 4: Session Fixation in Website 2FA Flow Allows Bypassing 2FA for Sensitive Actions ($1000)

The application sets a session cookie _sc_session after a user completes the 2FA process. This session cookie is intended to authenticate the user for sensitive actions such as changing email, password, or phone number. However, this session cookie can be reused across different accounts, allowing an attacker to bypass 2FA checks after it has been authorized once.

Steps to Reproduce
Create two accounts, Account A and Account B.
Log in to Account A and initiate a sensitive action that requires 2FA.
Complete the 2FA process and capture the _sc_session cookie set by the server.
Use this _sc_session cookie to perform a sensitive action on Account B without completing 2FA.

I reported this bug, but it was marked as duplicate. Then, I checked the Android application and found the same bug in another API. I reported this and it was triaged as High (7.7) with a $1000 bounty.

Thanks for reading my write-up.
