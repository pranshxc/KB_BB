---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-08-22_bypass-two-factor-authentication-of-facebook-accounts-25300.md
original_filename: 2023-08-22_bypass-two-factor-authentication-of-facebook-accounts-25300.md
title: Bypass Two-Factor Authentication of Facebook Accounts ($25,300)
category: documents
detected_topics:
- mfa
- rate-limit
- command-injection
- otp
- automation-abuse
- api-security
tags:
- imported
- documents
- mfa
- rate-limit
- command-injection
- otp
- automation-abuse
- api-security
language: en
raw_sha256: 03f9c451a6aa5b6d9ba53174e2cdbfe807ad23051bcb22273bc1e9702ec581fb
text_sha256: 2aa08db374612cc39cf3df0dabec583a3941607a1555a4ac224cf81c4946c09d
ingested_at: '2026-06-28T07:32:25Z'
sensitivity: unknown
redactions_applied: false
---

# Bypass Two-Factor Authentication of Facebook Accounts ($25,300)

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-08-22_bypass-two-factor-authentication-of-facebook-accounts-25300.md
- Source Type: markdown
- Detected Topics: mfa, rate-limit, command-injection, otp, automation-abuse, api-security
- Ingested At: 2026-06-28T07:32:25Z
- Redactions Applied: False
- Raw SHA256: `03f9c451a6aa5b6d9ba53174e2cdbfe807ad23051bcb22273bc1e9702ec581fb`
- Text SHA256: `2aa08db374612cc39cf3df0dabec583a3941607a1555a4ac224cf81c4946c09d`


## Content

---
title: "Bypass Two-Factor Authentication of Facebook Accounts ($25,300)"
url: "https://medium.com/@bazzounbassem/bypass-two-factor-authentication-of-facebook-accounts-25-300-7ae152d7836a"
authors: ["Bassem M Bazzoun (@bassemmbazzoun)"]
programs: ["Meta / Facebook (Instagram)"]
bugs: ["2FA / MFA bypass"]
bounty: "25,300"
publication_date: "2023-08-22"
added_date: "2023-08-25"
source: "pentester.land/writeups.json"
original_index: 842
scraped_via: "browseros"
---

# Bypass Two-Factor Authentication of Facebook Accounts ($25,300)

Bypass Two-Factor Authentication of Facebook Accounts ($25,300)
Bassem M Bazzoun
Follow
6 min read
·
Aug 21, 2023

1.3K

6

In this writeup, I will explain how I discovered a Two-Factor Authentication bypass in Facebook during Meta bug bounty Researchers conference in Seoul, South Korea, 2023 where I was awarded for $25,300 and ranked 2nd place on the conference Leaderboard. If you’re curious about the technical details, this writeup is for you!

Press enter or click to view image in full size

Meta Bug Bounty Researchers Conference

Last June, I received an invitation from Meta (Formerly Facebook) to attend their annual researchers conference known as Meta Bug Bounty Researchers Conference (Formerly BountyCon). The most accomplished researchers of Meta bug bounty program, Google bug bounty program and other programs would receive an exclusive invitation to attend the conference; It includes a live hack, informative talks, and valuable networking opportunities with fellow researchers and the Meta security team.

How I found it?

Three weeks before the conference, the pre-submission window opened up, giving us the opportunity to submit security vulnerabilities in advance. My primary aim was to concentrate on submitting critical bugs to Facebook. As a result, my focus was primarily on searching for vulnerabilities related to Account takeover, 2FA bypass, and Contact Point disclosure.

Before we dive in, it’s important to know that Facebook assumes the victim’s email address and password are set up for 2FA bypass. The purpose of 2FA bypass is to prevent hackers from gaining access to your account even if they manage to steal your credentials. They would encounter the two-factor authentication screen and would be unable to enter your account until they add the correct verification code that you receive. So, Let’s start!

I started digging into the login pages and recovery flows of both Facebook and Instagram. My exploration led me to the sign-up page of Instagram, where I observed the following behavior: When you sign up to create a new Instagram account and you enter the same phone number and password as that of an already existing account, Instagram permits you to log into the existing account instead of creating a new one.

To illustrate:

Consider you already have an instagram account with these credentials (e.g: phone number: +1123456 password “password123”)

If you try to create a new instagram account using +1123456 phone number and same password of your account; Instagram will let you logging into your existing account rather than creating a new one.

Well, so first thing will come into your mind now is what? You will try to create an Instagram account using the victim’s credentials to see if Instagram will let you login to the victim account instead of creating a new account and maybe without requiring a 2FA code. However, this approach will not work. The reason for this is that the behavior of letting you log in instead of creating a new account is tied to the specific device and network. In other words, it only works if you have already logged in from this device/network before.

After spending multiple days researching and testing these endpoints, It all started when I discovered a vulnerable enpoint on Instagram’s sign-up page that lacked proper rate limiting (This vulnerable endpoint was like a needle in the haystack). This endpoint was responsible for creating a new Instagram account using a given phone number and verification code. By bruteforcing the verification code, I was able to create a new Instagram account linked to the target victim’s phone number. This will end up with a bounty of ~$3000 for confirming any number on Instagram since I still cannot bypass 2FA and instead just bypassing the phone number confirmation.

So, I continued my research and tried to esclate it to 2FA bypass. After some investigation, I found myself within the Facebook account center. I speculated that if I connected the newly created Instagram account with my Facebook account (both belonging to the attacker), the confirmed phone number from the Instagram account (the victim’s number) might be transferred to my Facebook account without asking to reverifying the phone number. Given that the phone number had already been confirmed on Instagram, I reasoned that this transfer could occur.

Get Bassem M Bazzoun’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

And yes, my idea turned out to be correct! Linking the Instagram account successfully transferred the phone number to the account center. Consequently, I could add the phone number to my Facebook account without being asked for a re-verification prompt. Adding the phone number to my Facebook account will remove the phone number from the victim’s account, which will disable the 2FA and … BOOM! Two Factor Authentication is disabled/removed and we can enter the victim account!

I discovered the 2FA bypass at ~5:00 AM and woke up my brother (Kassem Bazzoun) to tell him about it since we had been discussing the need to escalate it to a 2FA bypass for the past few days; The excitement kept us awake until 9:00 AM. Then, I reported it to Facebook directly.

The below images will summarize everything and how the attack work:

Press enter or click to view image in full size
Press enter or click to view image in full size

Reproduction Steps:

1- Send the verification code to the target victim phone number:

POST /api/v1/accounts/send_signup_sms_code/ HTTP/2
Host: i.instagram.com
-other headers-

signed_body=SIGNATURE.{
  "phone_id": "redacted",
  "phone_number": "TARGET_PHONE_NUMBER",
  "guid": "redacted",
  "device_id": "redacted",
  "android_build_type": "release",
  "waterfall_id": "redacted"
}

2- Brute force the verification code that will create an Instagram account with the victim phone number

POST /api/v1/accounts/create_validated/ HTTP/2
Host: i.instagram.com
---Other headers

signed_body=SIGNATURE.{
"verification_code": "CODE_TO_BRUTE_FORCE",
"enc_password": "ENCRYPTED_PASS",
"phone_number": "VICTIM_PHONE_NUMBER",
"username": "USERNAME_OF_THE_NEW_ACCOUNT_TO_CREATE",
"first_name": "",
----other params
}

3- Go to https://accountscenter.facebook.com/ and link the instagram account created in step 2 with your Facebook account (“Add accounts”) which will transfer the phone number of the victim confirmed in step 2 to the account center “Personal details”

Press enter or click to view image in full size

4- Now, the victim phone number will show up in the “Personal Details” section; Click Personal details, and add the phone number to your Facebook account; Facebook will not ask to reverify the phone number and this step will remove the phone number from the victim Facebook account and therefore disabling the 2FA!

Facebook rewarded me for a bounty of 20,000 which is the maximum payout for a 2FA bypass + Hacker Plus Bonus + Conference Bonus. (Making the total bounty $25,300)

Press enter or click to view image in full size
Press enter or click to view image in full size

I hope you enjoyed reading the writeup! If you are interested in reading about how I was able to delete any video/reel on Facebook feel free to check out the link below.

Delete any Video or Reel on Facebook (11,250$)
Setting my goal While I was attempting to discover more vulnerabilities as part of Facebook's bug bounty program, I…

bugreader.com

The tools that I used: Burp suite, Turbo Intruder, Genymotion

Linkedin: https://linkedin.com/bassembazzoun

For business inquiries: https://academy.semicolonlb.com/

Facebook: https://www.facebook.com/bassemmbazzoun

Instagram: https://www.instagram.com/bassembazzoun/
