---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2017-02-20_how-i-was-able-to-remove-your-instagram-phone-number.md
original_filename: 2017-02-20_how-i-was-able-to-remove-your-instagram-phone-number.md
title: How I was able to remove your Instagram Phone number
category: documents
detected_topics:
- command-injection
- otp
- rate-limit
tags:
- imported
- documents
- command-injection
- otp
- rate-limit
language: en
raw_sha256: 2ea36d2e7de6961d3da0d9c799b0d85760c293f19fbf606e27247e02c1667ed2
text_sha256: 6dba8e086763a77c661ebb616027b377b56cbf969acbe5bd5d5c52dad1d1001f
ingested_at: '2026-06-28T07:31:55Z'
sensitivity: unknown
redactions_applied: false
---

# How I was able to remove your Instagram Phone number

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2017-02-20_how-i-was-able-to-remove-your-instagram-phone-number.md
- Source Type: markdown
- Detected Topics: command-injection, otp, rate-limit
- Ingested At: 2026-06-28T07:31:55Z
- Redactions Applied: False
- Raw SHA256: `2ea36d2e7de6961d3da0d9c799b0d85760c293f19fbf606e27247e02c1667ed2`
- Text SHA256: `6dba8e086763a77c661ebb616027b377b56cbf969acbe5bd5d5c52dad1d1001f`


## Content

---
title: "How I was able to remove your Instagram Phone number"
url: "https://medium.com/bugbountywriteup/how-i-was-able-to-remove-your-instagram-phone-number-d346515e79c3"
authors: ["Neeraj Sonaniya (@neeraj_sonaniya)"]
programs: ["Meta / Facebook"]
bugs: ["Bruteforce"]
bounty: "1,000"
publication_date: "2017-02-20"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 6221
scraped_via: "browseros"
---

# How I was able to remove your Instagram Phone number

How I was able to remove your Instagram Phone number
Neeraj Sonaniya
Follow
3 min read
·
Feb 21, 2017

193

1

Phone numbers are the most important Out-of-band features in network and security, now a days from phone number we register, login for an account.

Instagram have feature to login, sign up through mobile number, and after signing up instagram through mobile number we have to verify that we are real person, through OTP (One Time Password) sent to that mobile number.

Press enter or click to view image in full size

But while searching for vulnerability in Instagram, I found that verifying OTP endpoint have no limit, it means we can brute-force the 6 digit code sent to mobile number.

Other thing is that even if your mobile number is registered with instagram then also you are able to reuse that mobile number again on registration page.

Press enter or click to view image in full size

While bruteforcing OTP responses I got are:

Response when OTP is wrong:

{“status”: “ok”, “error_type”: “form_validation_error”, “errors”: {“sms_code”: [“That code is no longer valid. Go back to request a new one.”]}, “account_created”: false}
Press enter or click to view image in full size

Response when OTP is correct.:

{“status”: “ok”, “account_created”: true}
Press enter or click to view image in full size

As you can see in the above screenshot that, 636 requests were made by me and no lockout is there.

Get Neeraj Sonaniya’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Finally, I bruteforced the OTP successfully and was able to create account from that mobile number.

When I logged out from that test account, and signed in on my real Instagram account(initially registered with that mobile number from which I have created test account).

And got this page after logging in

Press enter or click to view image in full size

From above photo we can confirm that the mobile number has been removed from my Instagram account.

Here is the POC video:

Timeline:

8 November 2016: Report Submitted
16 November 2016: Facebook response that not able to reproduce the issue
18 November 2016: POC video provided by me.
19 November 2016: Again Not accepted
19 November 2016: Again provided POC video with time and date
19 November 2016: Issue triaged
27 December 2016: Issue Patched
29 December 2016: $1000 bounty awarded.

Thanks
Regards
Neeraj Edwards
