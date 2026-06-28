---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2019-04-29_two-factor-authentication-bypass.md
original_filename: 2019-04-29_two-factor-authentication-bypass.md
title: Two-Factor Authentication Bypass
category: documents
detected_topics:
- mfa
- rate-limit
- xss
- otp
- access-control
- ssrf
tags:
- imported
- documents
- mfa
- rate-limit
- xss
- otp
- access-control
- ssrf
language: en
raw_sha256: cf2a9bb85201ebaa52a7d0f969600d59f535415db95731e12ca16244150f5de9
text_sha256: a07772d9cb8d097bf10707321ca91ab0ce8730a06c507d25d6d0d4dd01d4b206
ingested_at: '2026-06-28T07:31:59Z'
sensitivity: unknown
redactions_applied: true
---

# Two-Factor Authentication Bypass

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2019-04-29_two-factor-authentication-bypass.md
- Source Type: markdown
- Detected Topics: mfa, rate-limit, xss, otp, access-control, ssrf
- Ingested At: 2026-06-28T07:31:59Z
- Redactions Applied: True
- Raw SHA256: `cf2a9bb85201ebaa52a7d0f969600d59f535415db95731e12ca16244150f5de9`
- Text SHA256: `a07772d9cb8d097bf10707321ca91ab0ce8730a06c507d25d6d0d4dd01d4b206`


## Content

---
title: "Two-Factor Authentication Bypass"
page_title: "Two-Factor Authentication Bypass | I'm Gaurav Narwani"
url: "https://gauravnarwani.com/two-factor-authentication-bypass/"
final_url: "https://gauravnarwani.com/two-factor-authentication-bypass/"
authors: ["Gaurav Narwani (@gauravnarwani97)"]
bugs: ["2FA / MFA bypass"]
publication_date: "2019-04-29"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5280
---

[ ![](https://i0.wp.com/gauravnarwani.com/wp-content/uploads/2019/04/2fa.png?fit=1000%2C571&ssl=1) ](https://gauravnarwani.com/two-factor-authentication-bypass/)

# Two-Factor Authentication Bypass

[admin](https://gauravnarwani.com/author/admin/ "Posts by admin") / [April 29, 2019](https://gauravnarwani.com/two-factor-authentication-bypass/)

With advent of account takeovers, Companies like Google, Facebook have implemented this feature on various sensitive pages where an attacker could get or modify data of a user without his intent. This Authentication method improves the security posture & provides a secure access to users. Using two-factor authentication prevents hackers or attackers from compromising your account even if your account credentials are leaked publicly or bypassed. Two-factor authentication (2FA), sometimes referred to as two-step verification or dual factor authentication, is a security process in which the user provides two different authentication factors to verify themselves to better protect both the user’s credentials and the resources the user can access.

Authentication factors, listed in approximate order of adoption for computing, include:

  1. A knowledge factor is something the user knows, such as a password, a PIN or some other type of shared secret.
  2. A possession factor is something the user has, such as an ID card, a security token, a smartphone or other mobile device.
  3. An inherence factor, more commonly called a biometric factor, is something inherent in the user’s physical self.
  4. A location factor, usually denoted by the location from which an authentication attempt is being made.
  5. A time factor restricts user authentication to a specific time window.

### Case Study: Two-Factor Authentication Bypass

The application in the test is assumed to be example.com as the program doesn’t public disclosures. The application had a login page where the user was allowed to login via two-factor authentication. The two-factor authentication included a knowledge factor (**Credentials of the user**) as well as a possession factor (**Mobile device**). Once the user logs in with his credentials, an **OTP** was sent to the registered mobile number after successfully logging in the application. Once the correct **OTP** was entered, the homepage of the application was available to the users.

This is the actual functionality of the authentication. This following feature was bypassed by the attacker by knowing just the username and email to login. Let’s see how this was done.

Once logging into the application, a request was sent to the registered phone number as:

POST api/sms-enroll  
Host: example.com  
Authorization: Bearer ***REDACTED***………  
  
{“phone_number”:”1212112322”}

Now by the POST request, we can understand that a request was sent to the mobile number requesting for OTP. The phone_number was modified and the request was replayed such that the OTP was now sent to the attacker’s device. The response had the **status 200** indicating the request was submitted successfully and the OTP had been sent to the attacker’s device. As the new OTP sent to the attacker matches the latest OTP in the application, the check was indirectly bypassed helping the attacker gain hold of victims account.

This submission is triaged as a medium priority bug as the attacker needs to know the credentials of the user beforehand, via credentials stuffing or various other methods to phish the user.

### Other cases found online:

  1. **Bypass HackerOne 2FA requirement and reporter blacklist**

The researcher used the Embedded Submission form in the program to submit reports anonymously. The actual form submission required a 2fa to send a report. The way to use the embedded form bypassed this feature and hence the researcher was rewarded with $10k from Hackerone.

Link to blog: [https://medium.com/japzdivino/bypass-hackerone-2fa-requirement-and-reporter-blacklist-46d7959f1ee5](https://medium.com/japzdivino/bypass-hackerone-2fa-requirement-and-reporter-blacklist-46d7959f1ee5)

  2. **2FA Bypass – Confirmation tokens don’t expire**

The researcher could reuse the confirmation tokens even after 24 hours to Bypass the 2fa authentication on the login page to gain access to the victim’s account.

Link to Blog: [https://mustafakemalcan.com/bypass-two-factor-authentication-on-login-gov/](https://mustafakemalcan.com/bypass-two-factor-authentication-on-login-gov/)

  3. **2FA Bypass – No rate limiting on 2FA text box**

The researcher could brute-force 2FA on the login page of Skype and hence would bypass it leading to account of the Victim.

Link to Report: [https://hackerone.com/reports/121696](https://hackerone.com/reports/121696)

  4. **Two-factor authentication bypass on Grab Android App**

The researcher could bypass the profile edit two-factor authentication via brute-forcing OTP. An incorrect code was denoted by the status code 400 and a correct with a status code 204.

Link to Report: [https://hackerone.com/reports/202425](https://hackerone.com/reports/202425)

  5. **2FA Bypass – Resending a successful request**

The researcher could resend a successful request captured when entering a right OTP the first time to bypass the incorrect OTP entered next time.

Link to Blog: [http://c0d3g33k.blogspot.com/2018/02/how-i-bypassed-2-factor-authentication.html](http://c0d3g33k.blogspot.com/2018/02/how-i-bypassed-2-factor-authentication.html)

That’s all for this Blog. Hope you liked it.

**#bugbounty ProTip:**  
Escalate everything you find!  
Don’t report SSRF, Escalate to RCE.  
Don’t report Self-XSS, Chain it with Clickjacking.  
Don’t report Self-Stored XSS, Chain it with CSRF.  
Don’t report Information Disclosure, try to use it (Privileges Escalation).  
Don’t report Open Redirect, Escalate it to ATO.

Credits to [@Youssef](https://twitter.com/GeneralEG64) for this tip as well as [@Avinash](https://twitter.com/dedsec_69) for the support to find the vulnerability.

That’s all for today. Please subscribe to my[ blog](https://gauravnarwani.com/blog). Connect with me on [LinkedIn](https://linkedin.com/in/gauravnarwani97).

### Gaurav Narwani

### Share this:

  * [Twitter](https://gauravnarwani.com/two-factor-authentication-bypass/?share=twitter "Click to share on Twitter")
  * [Facebook](https://gauravnarwani.com/two-factor-authentication-bypass/?share=facebook "Click to share on Facebook")
  * [LinkedIn](https://gauravnarwani.com/two-factor-authentication-bypass/?share=linkedin "Click to share on LinkedIn")
  * [WhatsApp](https://gauravnarwani.com/two-factor-authentication-bypass/?share=jetpack-whatsapp "Click to share on WhatsApp")
  * [Telegram](https://gauravnarwani.com/two-factor-authentication-bypass/?share=telegram "Click to share on Telegram")
  * [Print](https://gauravnarwani.com/two-factor-authentication-bypass/#print "Click to print")
  * 

### Like this:

Like Loading...

Posted in: [Bug Bounty](https://gauravnarwani.com/category/bugb/)
