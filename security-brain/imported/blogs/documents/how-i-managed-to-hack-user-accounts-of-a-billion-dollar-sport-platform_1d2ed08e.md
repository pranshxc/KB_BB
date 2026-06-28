---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-12-04_how-i-managed-to-hack-user-accounts-of-a-billion-dollar-sport-platform.md
original_filename: 2021-12-04_how-i-managed-to-hack-user-accounts-of-a-billion-dollar-sport-platform.md
title: How I managed to hack User accounts of a billion-dollar sport platform
category: documents
detected_topics:
- rate-limit
- command-injection
- otp
- api-security
- cloud-security
- mobile-security
tags:
- imported
- documents
- rate-limit
- command-injection
- otp
- api-security
- cloud-security
- mobile-security
language: en
raw_sha256: 1d2ed08eac0d0a2e90c3a10ae0545b8052d5ce13233a4d3d3ce68109a2ce5b52
text_sha256: 80b6da5b3ff925a66a49c1780fceb19a8760d45ceaec8b7bc4004dd6a3a47e7d
ingested_at: '2026-06-28T07:32:08Z'
sensitivity: unknown
redactions_applied: false
---

# How I managed to hack User accounts of a billion-dollar sport platform

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-12-04_how-i-managed-to-hack-user-accounts-of-a-billion-dollar-sport-platform.md
- Source Type: markdown
- Detected Topics: rate-limit, command-injection, otp, api-security, cloud-security, mobile-security
- Ingested At: 2026-06-28T07:32:08Z
- Redactions Applied: False
- Raw SHA256: `1d2ed08eac0d0a2e90c3a10ae0545b8052d5ce13233a4d3d3ce68109a2ce5b52`
- Text SHA256: `80b6da5b3ff925a66a49c1780fceb19a8760d45ceaec8b7bc4004dd6a3a47e7d`


## Content

---
title: "How I managed to hack User accounts of a billion-dollar sport platform"
url: "https://medium.com/@vishnu0002/how-i-managed-to-hack-into-a-billion-dollar-sport-platform-7cc667081229"
authors: ["Vishnuraj"]
bugs: ["OTP bypass", "Bruteforce", "Lack of rate limiting"]
publication_date: "2021-12-04"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3114
scraped_via: "browseros"
---

# How I managed to hack User accounts of a billion-dollar sport platform

How I managed to hack User accounts of a billion-dollar sport platform
vishnuraj
Follow
3 min read
·
Dec 4, 2021

93

1

Hello everyone,

This post is regarding one of my favorite types of vulnerability, Account takeover. I was able to execute an account takeover in a bugcrowd private program, which allows a complete takeover of user accounts.

Vulnerability Category:

Broken Authentication

Description

An account takeover is a form of online identity theft in which a cybercriminal illegally gains unauthorized access to an account belonging to someone else. The victim’s account will be of value to the hacker because it either holds funds or access to products, services, or other stored value of some kind (such as sellable private information. This is an interesting type of vulnerability, as hackers/attackers use it as a means to gain access to a user account, tied to any organisation.

Impact

On successful account takeover, it allows the attacker to access the linked user PII or saved credit card details. This becomes an even bigger issue if the account takeover is possible on admin privileged users.

Login Flow of the application

On performing the initial recon and application walk through, I noticed the app uses OTP login for authentication. An OTP that can be sent to a linked email/mobile number is used as the single source for authentication.

Flow
Press enter or click to view image in full size
https://www.arengu.com/tutorials/the-complete-guide-to-email-otp-flows

HTTP request from IOS application

Press enter or click to view image in full size
Analyzing the Login flow

The OTP used here was a 6 digit number, and we need access to the user email account to get the OTP. My initial thought was to check the responses of the login requests to see if the OTP is being leaked anywhere. It was of no luck. Bruteforcing the OTP was what I did next, but the app had a proper rate limit set, so it blocked me for consecutive wrong tries of OTP.

Get vishnuraj’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

But interestingly, I noticed that if I send the test OTP from a different IP, the application does not block me for consecutive wrong tries. This allowed me to perform IP rotation to bypass the current protection in place.

IP rotation is a process where assigned IP addresses are distributed to a device at random or at scheduled intervals.

By doing IP rotation, I was able to bruteforce the OTP to obtain the correct OTP and successfully log in to any user account, giving me complete access to that account.

Proof of Concept

For exploiting this vulnerability, we need to set up an environment to use IP rotation for every single request send.

I used AWS, Burpsuite, and IpRotate addon to set it.

Press enter or click to view image in full size

After setting up the IpRotate addon, we can send each request with a different IP address.

POC how IP rotate working (not target)

TA- DA!!! Successful exploitation.

Press enter or click to view image in full size

Using this vulnerability, an attacker can gain access to any user account in less than a few minutes.

Press enter or click to view image in full size
