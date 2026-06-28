---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-09-08_facebook-email-disclosure-and-account-takeover.md
original_filename: 2021-09-08_facebook-email-disclosure-and-account-takeover.md
title: Facebook email disclosure and account takeover
category: documents
detected_topics:
- rate-limit
- command-injection
- password-reset
- otp
- information-disclosure
- api-security
tags:
- imported
- documents
- rate-limit
- command-injection
- password-reset
- otp
- information-disclosure
- api-security
language: en
raw_sha256: e46d9de1a5e8eb3345e1b32f9439a87842526ad930028f8f99dbdbb33a24f305
text_sha256: e2c35d4ce8b2bf63e7b52f1c391ccca596c11f4478562f5a69b0f1957b8673d6
ingested_at: '2026-06-28T07:32:07Z'
sensitivity: unknown
redactions_applied: false
---

# Facebook email disclosure and account takeover

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-09-08_facebook-email-disclosure-and-account-takeover.md
- Source Type: markdown
- Detected Topics: rate-limit, command-injection, password-reset, otp, information-disclosure, api-security
- Ingested At: 2026-06-28T07:32:07Z
- Redactions Applied: False
- Raw SHA256: `e46d9de1a5e8eb3345e1b32f9439a87842526ad930028f8f99dbdbb33a24f305`
- Text SHA256: `e2c35d4ce8b2bf63e7b52f1c391ccca596c11f4478562f5a69b0f1957b8673d6`


## Content

---
title: "Facebook email disclosure and account takeover"
url: "https://rikeshbaniyaaa.medium.com/facebook-email-disclosure-and-account-takeover-ecdb44ee12e9"
authors: ["Rikesh Baniya (@rikeshbaniya)"]
programs: ["Meta / Facebook"]
bugs: ["Information disclosure", "Account takeover"]
publication_date: "2021-09-08"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3334
scraped_via: "browseros"
---

# Facebook email disclosure and account takeover

Facebook email disclosure and account takeover
Rikesh Baniya
Follow
4 min read
·
Sep 8, 2021

940

3

I have a preference for apps over web when it comes to hunting, so in January I decided to dive deep into apk endpoints hoping to find something juicy.

I downloaded bunch of FB and messenger apks of different versions, grepped all the endpoints, sorted them and was going through them

During the process, I came across another an interesting endpoint named:

POST auth/flashcall_account_recovery

Press enter or click to view image in full size

The endpoint required 3 parameters:
cuid, encrypted_phone_numbers & cli

The CUID basically meant encrypted email/phone and can be easily found.

Just supply victim’s email in

POST /recover_accounts

Press enter or click to view image in full size

And in response you’d get the CUID.

Secondly, while going through the Facebook’s password recovery flow.

I noticed that in the endpoint responsible for sending the FB OTP code, there was a parameter named:

should_use_flash_call=false

If its false, you'd receive an OTP SMS in your phone and if set true, you receive a phone call instead of OTP for account recovery.

And in the response it contained the required encrypted phone numbers.

Press enter or click to view image in full size

Now, I could not figure out what cli was.
The only thing coming to my mind was “cli~command line interface”

Unable to figure out, I supplied null value instead.

When made the request,
I received the userID belonging to the user, whose email value I supplied as the CUID.

Meaning an attacker could supply anyone’s email/phone as CUID and in response he would be exactly able to determine who that email belonged to.

Press enter or click to view image in full size

I quickly submitted the report and it was triaged and fixed within a day.

I was veryyyyy curious about this endpoint as I had never used a “phone call recovery” to reset my password.

Neither it was present in my UI, nor was there much info available regarding this account recovery flow in Google as well as Youtube.

So I started to analyze how this recovery flow works by reading the smali files.

The endpoint worked in following manner.

I enter my email/phone.
Choose phone call recovery option.
I receive a phone call.
That phone number will be automatically supplied to the endpoint as:

POST /flash_call_recovery

Get Rikesh Baniya’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

cuid=x&enc_phone=x&cli=+1xxxxx

Turns out in cli parameter we are basically supposed to supply the phone number from which we received the phone call in Step3.

Now it all made sense why it was called phone call recovery🤦‍♂️

I guess the cli means something like caller identification.

In an ideal scenario when supplied all valid values, we would then receive this following response:

{“id”:”UserID”,”nonce”:”XXXX”,"skip_logout_pw_reset":""}

This nonce value acts as an OTP code and then will be supplied to the OTP verification endpoint.

The OTP verification endpoint is then responsible for validating the nonce and setting the new password.

Press enter or click to view image in full size

In POST /flash_call_recovery , I initially tested if supplying another user’s valid cli with victim’s cuid would work, but it didn't.

I tried flipping every parameters here and there but non of them worked.

Now, the only option I was left with was bruteforcing the cli.

Considering how strict FB is with rate limiting since it even has rate limit implemented on non authentication endpoints I had little to no hope.

But to my absolute surprise, it had no rate limit implemented in this endpoint.

Hence the attack would work like this:

User supplies victim’s cuid and enc_phone_number in flashcall recovery endpoint
Bruteforces the cli
Receives the nonce from the response
Supplies the nonce in OTP verification endpoint and sets a new password for victim’s account.

Here’s video demonstrating how a default phone call account recovery process works:

Timeline of Email Disclosure

Submitted: April 25, 2021
Triaged: April 27,2021
Fixed: April 27,2021

Timeline of Account Takeover

Submitted: April 29, 2021
Triaged : April 30, 2021 at 3:32 PM
Fixed: April 30, 2021 at 3:49 PM

It took me more time to verify the fix then FB took to release the fix, lol🤣

After thorough investigation, Facebook found no evidence of abuse and the issue was finally closed in September 2.
