---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-06-26_dos-attack-possible-on-reset-2fa-feature-of-hackerone.md
original_filename: 2023-06-26_dos-attack-possible-on-reset-2fa-feature-of-hackerone.md
title: 'DOS attack possible on Reset 2FA feature of #Hackerone'
category: documents
detected_topics:
- rate-limit
- mfa
- automation-abuse
- access-control
- command-injection
- graphql
tags:
- imported
- documents
- rate-limit
- mfa
- automation-abuse
- access-control
- command-injection
- graphql
language: en
raw_sha256: 35f50280de3195ac7f07dc6b6f7470ce4e27b207cf7c8b8e69d70112be1f9db8
text_sha256: 0dd5a9a395a53a3a547a5ee37bccd4955169e7920b3d84add5db231c694eb087
ingested_at: '2026-06-28T07:32:22Z'
sensitivity: unknown
redactions_applied: false
---

# DOS attack possible on Reset 2FA feature of #Hackerone

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-06-26_dos-attack-possible-on-reset-2fa-feature-of-hackerone.md
- Source Type: markdown
- Detected Topics: rate-limit, mfa, automation-abuse, access-control, command-injection, graphql
- Ingested At: 2026-06-28T07:32:22Z
- Redactions Applied: False
- Raw SHA256: `35f50280de3195ac7f07dc6b6f7470ce4e27b207cf7c8b8e69d70112be1f9db8`
- Text SHA256: `0dd5a9a395a53a3a547a5ee37bccd4955169e7920b3d84add5db231c694eb087`


## Content

---
title: "DOS attack possible on Reset 2FA feature of #Hackerone"
page_title: "A Potential DOS Attack on user account through 2FA Reset Feature on HackerOne Site | Medium"
url: "https://medium.com/@lokesh.leads13/disallow-any-hackerone-user-permanent-access-to-his-her-own-hackerone-account-using-vulnerability-147ce9957692"
authors: ["Lokesh Ranjan"]
programs: ["HackerOne"]
bugs: ["Application-level DoS", "Lack of rate limiting"]
publication_date: "2023-06-26"
added_date: "2023-06-27"
source: "pentester.land/writeups.json"
original_index: 1006
scraped_via: "browseros"
---

# DOS attack possible on Reset 2FA feature of #Hackerone

1

·

Lokesh Ranjan
 highlighted

Hackerone 2FA reset vulnerability - Potential DOS attack possible on User Account using Reset 2FA feature
Lokesh Ranjan
Follow
2 min read
·
Jun 26, 2023

144

5

Severity: Medium (5.0)
Weakness: Insecure Design & No Rate Limiting in place

Summary:

I have found a vulnerability in “Hackerone’e reset 2FA” feature of hackerone using which any malicious user on hackerone can permanently deny access to H1 site to all the users.

Only requirement is Attacker need to have the Victim’s email. This can be easily achieved using manual web scraping on hackerone site.

Description:
There is no rate limiting or authorization check in place on “Reset Two factor authentiction” graphql endpoint and this bug can be leveraged by malicious hacker to deny access to the user’s hackerone account permanently.

Steps To Reproduce

Proof Of Concept-

Get Lokesh Ranjan’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Victim — victim1@gmail.com
Attacker- hackerone_user@gmail.com

Two Factor Authentication is enabled on both Victim and Attacker.
Attacker will login into hackerone site using his/her valid “email address” and “Password” on the sign in page — https://hackerone.com/users/sign_in.
Application redirects to the “Two-factor Authentication” page.
Click on “Reset Two-factor Authentication” and intercept the request using burp suite.
Attacker sends the intercepted request to “intruder” and replaces the Email with “Victim’s email” and sets a bruteforce payload on “password” field.
Run the brute force attack using intruder.
Brute force attack will lockout the Victim account and since there is no Rate Limiting in place Brute Force attack will successfully run(infinite times) locking out the Victim thus denying the co-hacker to access or unlock his/her hacekrone account.
Simultaneous brute force attack can be run on 10’s or 100’s of users. Since, no rate limiting/IP restriction/authorization check implemented on reset 2FA functionality it can be easily exploited.

Note: “account unlock instruction” will be on use since brute force can be run infinitely and Victim’s account will keep getting locked.

There is a violation of security design principle, as once user have passed the intial password based login flow, on two factor authentication they must not be able to use any other user email on “Reset Two-factor authentication” graphql endpoint.

Hackerone team closed this vulnerability as “informative”.
However a live demo was done with the H1 team as well and show cased that WAF didn’t blocked the bruteforce attack and account got locked permanently with restricting the user access. Also, many H1 users email addressess are publicly available on H1 site, so not much effort required to scrape the emails.

Simple mitigation would have been to either implement API rate limiting and Block the IP trying brute force or not allow any hacker to user their “Reset two factor authentication” flow to send the request for any other user’s email id. Request should result in “unauthorized” HTTP request.

After reporting this issue under responsible disclosure program and repeated follow up no action was taken. It have been closed as “Informational”. But i think security community must be aware of this flaw.
