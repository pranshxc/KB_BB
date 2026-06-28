---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2018-12-04_complete-user-account-takeover-on-an-android-application.md
original_filename: 2018-12-04_complete-user-account-takeover-on-an-android-application.md
title: Complete User Account Takeover on an Android Application
category: documents
detected_topics:
- password-reset
- mobile-security
- access-control
- command-injection
- mfa
- otp
tags:
- imported
- documents
- password-reset
- mobile-security
- access-control
- command-injection
- mfa
- otp
language: en
raw_sha256: 02d7a5b073f5547cb0e7e1c0b648a9fed9ddd6714741048edb5d5ce5a6bcd743
text_sha256: ea93d0549f7b7d6b5fbf78e1fa68a9525061be38a206b2664620d086588c2942
ingested_at: '2026-06-28T07:31:58Z'
sensitivity: unknown
redactions_applied: true
---

# Complete User Account Takeover on an Android Application

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2018-12-04_complete-user-account-takeover-on-an-android-application.md
- Source Type: markdown
- Detected Topics: password-reset, mobile-security, access-control, command-injection, mfa, otp
- Ingested At: 2026-06-28T07:31:58Z
- Redactions Applied: True
- Raw SHA256: `02d7a5b073f5547cb0e7e1c0b648a9fed9ddd6714741048edb5d5ce5a6bcd743`
- Text SHA256: `ea93d0549f7b7d6b5fbf78e1fa68a9525061be38a206b2664620d086588c2942`


## Content

---
title: "Complete User Account Takeover on an Android Application"
page_title: "Complete User Account Takeover on an Android Application | I'm Gaurav Narwani"
url: "https://gauravnarwani.com/android-acc-takeover/"
final_url: "https://gauravnarwani.com/android-acc-takeover/"
authors: ["Gaurav Narwani (@gauravnarwani97)"]
bugs: ["Account takeover", "OTP bypass", "Password reset"]
publication_date: "2018-12-04"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5545
---

[ ![](https://i0.wp.com/gauravnarwani.com/wp-content/uploads/2018/12/android-hack.jpg?fit=700%2C500&ssl=1) ](https://gauravnarwani.com/android-acc-takeover/)

# Complete User Account Takeover on an Android Application

[admin](https://gauravnarwani.com/author/admin/ "Posts by admin") / [December 4, 2018](https://gauravnarwani.com/android-acc-takeover/)

Hello, welcome to my second blog post. Today we will be discussing the impacts of different attacks on an android application. Websites tend to contain more endpoints and as a result stores more information on the server. Generally, a web application is compacted into an android application which is very small and less responsive with respect to a web application. The impact of endpoints not been secured can lead to some critical data exposure and the possibility of manipulation of the same.

A week ago, I came across a few critical bugs on an android application, which could lead to full account takeover of the user without any interaction. In this blog, I will walk through each case study and also stating my experience in finding these bugs.

The following are the two case studies which I will discuss in detail:

  1. **OTP bypass leading to full account takeover.**
  2. **Password change of another user without interaction**.

Both of these bugs are a result of misconfigured API and access to unnecessary privileges given to a user to perform operations. As a result of no sufficient checks on the links, sensitive data was disclosed which compromised the user’s account. Only an admin should have the privileges to change another user’s password as well as monitor the OTP sent to the user’s mobile device.

### Software/Tools used:

  1. **Genymotion Emulator** : Used for loading and testing of an Android Application.
  2. **Burp Proxy:** Used for intercepting communications between the application and the server.

Let us assume the site to be **example.com** _(The program doesn’t allow public disclosures)_

### Case 1: OTP Bypass leading to full account takeover

In mobile applications, it is most likely for the OTP to be brute-forced which is an interesting vulnerability itself. The OTP in this application was sent when the user clicks on **Forgot Password** and enters a mobile number for verification. In this case, when an OTP was entered in the OTP request page, there was no request sent to the server from the application. This seemed strange! I thought that my **Genymotion** wasn’t connected to the internet or the proxy wasn’t set properly.

![](https://i0.wp.com/gauravnarwani.com/wp-content/uploads/2018/12/geny_forg_pass_1.png?fit=520%2C858&ssl=1) The Forgot Password Functionality sends an OTP to mobile

On checking the **History** Panel under the **Proxy** column in my **Burp**. All the previous requests sent by the application to the server were visible when requesting for OTP. While checking the response for that request, it was found that the _server sent out OTP in the response_.

The application sent out a post request as:

POST /api/otp_password?countrycode=91&mobile=XXXXXXXXXX HTTP/1.1  
**Host: api.example.com**

And we got a response as:

HTTP/1.1 200 OK

{“status”:”success”,”message”:null,”otp_code”:”XXXXXX”}

![](https://i0.wp.com/gauravnarwani.com/wp-content/uploads/2018/12/otp_1.png?fit=1000%2C333&ssl=1) The OTP obtained in the response section of a request

To Verify, the request was forwarded to the repeater and sent again. But this time it threw back an error stating that there was a time limit for the user to resend the request. The request was then resent after a _time period of 1min as this was the period of the OTP to expire_. On hitting button**Go** **Now** , the server responded with another OTP. After entering the OTP in the password reset section, we found that somehow the OTP wasn’t being accepted by the server. The _only option_ to prove the existence of the bug was to show the Proxy History and copying the OTP generated by the server during the request made by the application. While making the **Proof of Concept** video, the OTP obtained from the history panel of requests was pasted, which gave access to the account. The application now allowed any user to set a new password for any mobile phone. This is a critical bug as an attacker could take over an account by just knowing the mobile number of the victim.

![](https://i0.wp.com/gauravnarwani.com/wp-content/uploads/2018/12/new_pass_1.png?fit=518%2C861&ssl=1) The New password setting page after entering correct OTP

### Case 2: Password change of another user without interaction

After performing more tests on the application, a password reset page was hidden in the background and was accessible after the correct OTP was entered. It is on this page the user enters a new password for his account. When the request was submitted, the password resets and the user logs in to his account. The application was connected through the **Burp Proxy** the entire time while it was firing these requests. The History of requests was then examined.

There was one URL having 2 parameters: Mobile Number and Password

POST /api/update_password?password=***REDACTED*** HTTP/1.1

**Host: api.example.com**

![](https://i0.wp.com/gauravnarwani.com/wp-content/uploads/2018/12/upd_pass_2.png?fit=1000%2C469&ssl=1) The Request and Response for a custom mobile number and password

The request was captured in the repeater to test whether the request would fire if the password was changed. If the request was _successful_ , User gained admin privileges and could change the password bypassing two-factor authentication.

The request was then sent in the repeater with a different password, where the response was now a success with status code 200. This concluded that the parameter password had no access control set on it and any attacker having the mobile number of victims could change his password and take over his entire account.

To _completely test my theory_ , a different account using another mobile number as well as a different password was used to sign into the application. The request from the repeater was then fired after making the appropriate changes in parameters. The server gave out a success in response. The new set of credentials was now tested on the application which was later accepted by the server logging the attacker on behalf of the victim.

Unfortunately, both of these bugs were marked as duplicate by the program manager as these bugs were already reported a few months back by some researcher. It was an amazing find and so wanted to share it.

**#Bug Bounty Tip** – If a website does not verify your email, you can try signing up with <email>@domain.com (the mail id of the company). Sometimes you can get privileges like viewing/deleting any other users’ profile. To show a small example, an application in a private program was put to test. The web application did not verify the email and so any anonymous user could sign up with  he***@ex*****.com (where example.com was the actual domain name of the website). While logging in, an application feedback page was encountered which was hidden to users with emails from other domains.

That’s all for today. Please Subscribe to my [blog](https://gauravnarwani.com). Connect with me on [LinkedIn](https://www.linkedin.com/in/gauravnarwani97). Also, a huge shout-out to Avinash for helping me find these Bugs. Connect with him on [LinkedIn](https://www.linkedin.com/in/avinash-s-548936156), [Twitter](https://twitter.com/_AVizard) and also subscribe to his [YouTube](https://www.youtube.com/channel/UCDSVQkRrnGbAF7udnuVUS3w) Channel.

Until then! Keep Hunting.

## Gaurav Narwani

### Share this:

  * [Twitter](https://gauravnarwani.com/android-acc-takeover/?share=twitter "Click to share on Twitter")
  * [Facebook](https://gauravnarwani.com/android-acc-takeover/?share=facebook "Click to share on Facebook")
  * [LinkedIn](https://gauravnarwani.com/android-acc-takeover/?share=linkedin "Click to share on LinkedIn")
  * [WhatsApp](https://gauravnarwani.com/android-acc-takeover/?share=jetpack-whatsapp "Click to share on WhatsApp")
  * [Telegram](https://gauravnarwani.com/android-acc-takeover/?share=telegram "Click to share on Telegram")
  * [Print](https://gauravnarwani.com/android-acc-takeover/#print "Click to print")
  * 

### Like this:

Like Loading...

Posted in: [Bug Bounty](https://gauravnarwani.com/category/bugb/)
