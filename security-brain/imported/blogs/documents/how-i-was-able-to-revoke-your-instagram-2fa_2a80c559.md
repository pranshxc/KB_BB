---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-10-23_how-i-was-able-to-revoke-your-instagram-2fa.md
original_filename: 2021-10-23_how-i-was-able-to-revoke-your-instagram-2fa.md
title: How I was able to revoke your Instagram 2FA
category: documents
detected_topics:
- rate-limit
- sso
- command-injection
- mfa
- otp
- cloud-security
tags:
- imported
- documents
- rate-limit
- sso
- command-injection
- mfa
- otp
- cloud-security
language: en
raw_sha256: 2a80c55966dd02b3e6b7086d845a503b482256b21230d42bc0b986e5a5b01c02
text_sha256: 10ac0de791305874ec12fe5d5853f3fd52c044d4645bf209d209a145b2a40452
ingested_at: '2026-06-28T07:32:08Z'
sensitivity: unknown
redactions_applied: false
---

# How I was able to revoke your Instagram 2FA

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-10-23_how-i-was-able-to-revoke-your-instagram-2fa.md
- Source Type: markdown
- Detected Topics: rate-limit, sso, command-injection, mfa, otp, cloud-security
- Ingested At: 2026-06-28T07:32:08Z
- Redactions Applied: False
- Raw SHA256: `2a80c55966dd02b3e6b7086d845a503b482256b21230d42bc0b986e5a5b01c02`
- Text SHA256: `10ac0de791305874ec12fe5d5853f3fd52c044d4645bf209d209a145b2a40452`


## Content

---
title: "How I was able to revoke your Instagram 2FA"
page_title: "How I was able to revoke your Instagram 2FA – Geek Freak"
url: "https://dhiyaneshgeek.github.io/web/security/2021/10/23/how-i-was-able-to-revoke-your-instagram-2fa/"
final_url: "https://dhiyaneshgeek.github.io/web/security/2021/10/23/how-i-was-able-to-revoke-your-instagram-2fa/"
authors: ["Dhiyaneshwaran (@DhiyaneshDK)"]
programs: ["Meta / Facebook"]
bugs: ["Bruteforce", "Rate limiting bypass"]
bounty: "5,000"
publication_date: "2021-10-23"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3219
---

Hello Everyone,

Back in November 2019, I was going through one of the Old Writeups on Facebook Bug Bounty Reports, [_“How I was able to remove your Instagram Phone number”_](https://infosecwriteups.com/how-i-was-able-to-remove-your-instagram-phone-number-d346515e79c3) by [Neeraj Sonaniya](https://www.linkedin.com/in/neerajsonaniya/)

After reading this blog, it clicked in my mind that this can be bypassed by using **IP Rotation** Technique.

![](/images/instagram/ig1.jpeg)

**What is IP Rotation ?**

  * IP rotation is the process of changing IP Address on Each Request that is sent to the server where assigned IP addresses are distributed to a device at random or at scheduled intervals.
  * For example, when a connection is active via an Internet Service Provider (ISP), an IP address is automatically attached from a pool of IPs.

There is already a detailed article written [How to Rotate IP ADDRESS For Each Request in Burp Suite](https://lokeshdlk77.medium.com/how-to-rotate-ip-address-for-each-request-in-burp-suite-4e29645ef23e) by [Lokesh Kumar](https://www.facebook.com/lokeshdlk77)

**Attack Scenario**

![](/images/instagram/ig6.png)

**Steps to Reproduce:**

  * Navigate to this URL https://www.instagram.com/, fill the Signup page.

  * Enter the already Existing Instagram Users Mobile Number on the Signup page and Click on submit.

  * It will navigate you to the below page.

![](/images/instagram/ig2.png)

  * Enter any Random 6 digit OTP number, as shown below.

![](/images/instagram/ig3.png)

  * Intercept the Request using Client Side Proxy such as Burpsuite.

![](/images/instagram/ig4.png)

  * Now send the request to the **Intruder tab** in the Burpsuite and insert **$$** placeholder in the **sms_code** as shown below.

![](/images/instagram/ig5.png)

  * Move to the **Payloads Option** tab and specify the payload option as below.

![](/images/instagram/ig7.png)

**NOTE:**

Burpsuite User Option Configuration.

![](/images/instagram/ig8.png)

Open Proxy Configuration

![](/images/instagram/ig9.png)

  * Click on the Attack button to start the attack.

  * Now in the length you can see **2547** shows the code is **Invalid** as shown below.

![](/images/instagram/ig10.png)

  * When the **Correct** code matches , it shows **3453** and **Account Created** as shown below.

![](/images/instagram/ig11.png)

  * In result to this reaction, the number which belongs to the user gets an email that **“Phone number removed as Two Factor Authentication Method”**.

![](/images/instagram/ig14.png)

**Impact:-**

  * The mobile number that is registered in Instagram can be reused to register again and it will take us to 6 digit OTP page which can be bypassed using IP Rotation Technique, this could be used to remove a confirmed mobile number from another user.

  * If the User uses the same mobile number for Two factor authentication, it will disable the Two Factor authentication without that user’s interaction.

**Timeline:-**

27 January 2020 at 01:40 - Report Submitted  
31 January 2020 at 11:00 - Not able to Reproduce  
6 February 2020 at 23:08 - Detailed POC Video Sent  
7 February 2020 at 01:01 - Issue Triaged  
14 February 2020 at 22:12 - Issue Patched  
14 February 2020 at 22:23 - **$5000** Bounty Awarded

![](/images/instagram/ig13.png)

**References:-**

  * [Bypassing IP Based Blocking with AWS API Gateway](https://rhinosecuritylabs.com/aws/bypassing-ip-based-blocking-aws/)
  * [How I Could Have Hacked Any Instagram Account](https://thezerohack.com/hack-any-instagram)
  * [How I Hacked Instagram Again](https://thezerohack.com/hack-instagram-again)
  * [Disable Any Unconfirmed Account in Facebook](https://lokeshdlk77.medium.com/disable-any-unconfirmed-account-in-facebook-123aeba19426)
  * [Confirming any new Email Address bug in Facebook (Part-4)](https://lokeshdlk77.medium.com/confirming-any-new-email-address-bug-in-facebook-part-4-70cfe1b4dca5)

![](https://media.giphy.com/media/MBIcJIaE8SLY6jKrqp/giphy.gif)

This post is only for **Educational Purposes**.

Many websites uses **IP based Blocking** so please do not use this technique for **Illegal Activities**.

Thanks a lot for reading !!!.
