---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-01-20_two-factor-authentication-bypass-on-facebook.md
original_filename: 2023-01-20_two-factor-authentication-bypass-on-facebook.md
title: Two Factor Authentication Bypass On Facebook
category: documents
detected_topics:
- mfa
- command-injection
- otp
- rate-limit
- automation-abuse
tags:
- imported
- documents
- mfa
- command-injection
- otp
- rate-limit
- automation-abuse
language: en
raw_sha256: cd75e798dfe45ff53277b032f994f3a4c3ab20f349742f159d76208faff45fed
text_sha256: 7cb9d7e0881b7dcb271ad95945818ea554607df44703899a0394683e41780700
ingested_at: '2026-06-28T07:32:17Z'
sensitivity: unknown
redactions_applied: false
---

# Two Factor Authentication Bypass On Facebook

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-01-20_two-factor-authentication-bypass-on-facebook.md
- Source Type: markdown
- Detected Topics: mfa, command-injection, otp, rate-limit, automation-abuse
- Ingested At: 2026-06-28T07:32:17Z
- Redactions Applied: False
- Raw SHA256: `cd75e798dfe45ff53277b032f994f3a4c3ab20f349742f159d76208faff45fed`
- Text SHA256: `7cb9d7e0881b7dcb271ad95945818ea554607df44703899a0394683e41780700`


## Content

---
title: "Two Factor Authentication Bypass On Facebook"
url: "https://medium.com/pentesternepal/two-factor-authentication-bypass-on-facebook-3f4ac3ea139c"
authors: ["Gtm Mänôz (@Gtm0x01)"]
programs: ["Meta / Facebook"]
bugs: ["2FA / MFA bypass"]
publication_date: "2023-01-20"
added_date: "2023-01-23"
source: "pentester.land/writeups.json"
original_index: 1646
scraped_via: "browseros"
---

# Two Factor Authentication Bypass On Facebook

Gtm Mänôz
 highlighted

Two Factor Authentication Bypass On Facebook
Gtm Mänôz
Follow
5 min read
·
Jan 20, 2023

566

7

Summary: I discovered the lack of rate-limiting issue in instagram which could have allowed an attacker to bypass two factor authentication on facebook by confirming the targeted user’s already-confirmed facebook mobile number using the Meta Accounts Center.

Hello Everyone,

This is Gtm Mänôz from Kathmandu, Nepal. This is my first ever bug bounty write-up and the highest bounty reward from facebook.

Back in Mid-July 2022, I had got an invitation to attend BountyCon 2022 in Singapore because of my exceptional performance in Meta Bug Bounty program in early 2022. After getting the invitation, the only thing in my mind was to find at least a valid bug and be on the leaderboard of the live hacking event.

So, it all started when I found a new looking UI of Meta Accounts Center in instagram.

New Instagram Accounts Center

In the above image , personal details section had an option to add email and phone number to both instagram and linked facebook account which can be verified after placing the correct 6-digits code received in email/phone. At the time of reporting, the endpoint verifying the 6-digits code was vulnerable to lack of rate-limit protection allowing anyone to confirm unknown/known email and phone number both in instagram and linked facebook accounts.

Steps to Reproduce:

1.Generation Of Encrypted Authproof:

Navigate to the personal details section as shown in below image and enter the already registered facebook mobile number to add in your instagram linked facebook account.

Simultaneously, it will make post request to /api/v1/fxcal/get_native_linking_auth_blob/ endpoint to generate ig encrypted authproof (token) which will be added in step 2 to add contact points and also later to verify the confirmation code.

Below is the sample HTTP request from burp suite showing the generation of encrypted token.

Press enter or click to view image in full size
Step 1 : Generation Of Encrypted Authproof

2. Adding Contact Points:

While adding contact points (email/phone), it will make post request to /api/v1/bloks/apps/com.bloks.www.fx.settings.contact_point.add.async/ endpoint to request the server to send 6 digits code for verification.

Press enter or click to view image in full size
Step 2 : Adding Contact Points

3. Code Verification

Now, enter any random 6 digits code and intercept the request using web proxy such as burp suite.

Press enter or click to view image in full size
Step 3: Code Verification

Then, send the above request to the intruder and insert $$ placeholder in the pin_code value in order to brute force the confirmation code.

Since, there was no rate-limit protection at all in this /api/v1/bloks/apps/com.bloks.www.fx.settings.contact_point.verify.async/ endpoint, anyone could bypass the contact points verification.

While brute-forcing,

If the 6 digit code is wrong, the response will be “Wrong code: That code didn’t work. Please check the code and try again.”

Press enter or click to view image in full size
Wrong Code

And, if the 6 digit code matches, the response will be long and the entered email/phone will be confirmed to attacker’s account.

Press enter or click to view image in full size
Right Code

As a result,

Get Gtm Mänôz’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

If the phone number was fully confirmed and 2FA enabled in facebook, then the 2FA will be turned off or disabled from victim’s account.

And, if the phone number was partially confirmed that means only used for 2FA, it will revoke the 2FA and also the phone number will be removed from victim’s account.

Press enter or click to view image in full size

Since, the endpoint verifying both the contact points (email/phone) in instagram and linked facebook accounts was same , I was able to bypass both unknown and already registered contact points (email/phone) verification in instagram and facebook (unable to add already existed email in fb).

Impact
Revoke anyone’s SMS based facebook 2FA
Bypass contact points verification for both unknown and already registered email/phone in instagram & facebook(unable to add already existed email in fb).
Timeline
14 Sep, 2022 — Report Sent to Meta.
16 Sep, 2022 — Meta responded that they were not able to reproduce the issue.
20 Sep, 2022 — Gave my credentials to the security team for reproduction as the new account center feature was not rolled out in their accounts.
21 Sep, 2022 — The feature completely vanished from the account after the team logged in from the new location.
21 Sep, 2022 — The feature reappeared while un-linking the linked facebook account and informed this weird behaviour to the team.
22 Sep, 2022 — Triaged.
24 Sep,2022 — Bounty awarded by facebook for contact points verification bypass for instagram
3 Oct, 2022 — Sent additional impact about revoking anyone’s SMS-based facebook 2FA.
17 Oct, 2022 — Confirmation of fix by facebook
17 Oct, 2022 — Asked facebook team to increase the bounty amount as facebook always pay based on the maximum possible impact of the report.
14 Dec, 2022 — Got the reply from facebook team saying they will be issuing “The additional bounty amount that will reflect the maximum potential impact in addition to the value of the bug I initially reported.”
15 Dec, 2022 — Additional bounty awarded by facebook as per the New Payout Guidelines for 2FA Bypass.

Also, on the same day my report was highlighted as one of the most impactful bug submitted during 2022 on the Facebook News Room and Meta Bug Bounty official facebook page.

Link to the FB Newsroom: https://about.fb.com/news/2022/12/metas-bug-bounty-program-2022/

Thanks for reading my write-up 🤗 Happy Hacking 🎭️

Thanks & best regards,
Gtm Mänôz

Linkedin: https://linkedin.com/in/gtm0x01

Twitter: https://www.twitter.com/gtm0x01/

Facebook: https://www.facebook.com/gtm0x01

Instagram: https://www.instagram.com/gtm0x01/
