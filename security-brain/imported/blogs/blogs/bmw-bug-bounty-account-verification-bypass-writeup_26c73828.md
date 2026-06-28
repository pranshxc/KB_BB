---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-01-26_bmw-bug-bounty-account-verification-bypass-writeup.md
original_filename: 2021-01-26_bmw-bug-bounty-account-verification-bypass-writeup.md
title: BMW Bug Bounty – Account Verification Bypass writeup
category: blogs
detected_topics:
- rate-limit
- xss
- command-injection
- otp
tags:
- imported
- blogs
- rate-limit
- xss
- command-injection
- otp
language: en
raw_sha256: 26c73828463ff0336d39af3e5af6e40ef140c2015749b64294e132a64c568e97
text_sha256: 1c230a418d2f5a9ce5b7483a4e338f6eb4b141cb4d884680d8a27478a11cae7c
ingested_at: '2026-06-28T07:32:04Z'
sensitivity: unknown
redactions_applied: false
---

# BMW Bug Bounty – Account Verification Bypass writeup

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-01-26_bmw-bug-bounty-account-verification-bypass-writeup.md
- Source Type: markdown
- Detected Topics: rate-limit, xss, command-injection, otp
- Ingested At: 2026-06-28T07:32:04Z
- Redactions Applied: False
- Raw SHA256: `26c73828463ff0336d39af3e5af6e40ef140c2015749b64294e132a64c568e97`
- Text SHA256: `1c230a418d2f5a9ce5b7483a4e338f6eb4b141cb4d884680d8a27478a11cae7c`


## Content

---
title: "BMW Bug Bounty – Account Verification Bypass writeup"
page_title: "BMW Bug Bounty - Account Verification Bypass writeup - Pethuraj's Blog"
url: "https://www.pethuraj.com/blog/bmw-bugbounty-writeup/"
final_url: "https://www.pethuraj.com/blog/bmw-bugbounty-writeup/"
authors: ["Pethuraj (@Pethuraj)"]
programs: ["BMW"]
bugs: ["OTP bypass", "Bruteforce", "Lack of rate limiting"]
publication_date: "2021-01-26"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3966
---

![BMW Bug Bounty Writeup](https://www.pethuraj.com/blog/wp-content/uploads/2021/01/BMW-Bug-Bounty-Writeup.png)

[Uncategorized](https://www.pethuraj.com/blog/category/uncategorized/)

# BMW Bug Bounty – Account Verification Bypass writeup

[26/01/202128/03/2021](https://www.pethuraj.com/blog/bmw-bugbounty-writeup/) by [admin](https://www.pethuraj.com/blog/author/admin/)

It all started with the BMW Security Experts Acknowledgment page, missing my name and I decided to give it a try.

![](https://www.pethuraj.com/blog/wp-content/uploads/2021/01/BMW-1024x464.png)

I started with the BMW security page and tested BMW Singapore website as per their policy and I picked [ _https://accessbybmw.com.sg/_](https://accessbybmw.com.sg/) domain as my target and quickly started the recon activity.

So, this application has a lot of functionalities and an account registration and login page. To register for an account – I need to use a Singapore mobile number.

![](https://www.pethuraj.com/blog/wp-content/uploads/2021/01/BMW-Bug-Bounty-Registration-page.png)

So I picked a disposable mobile number (there are so many sites that offer these services) which lets us receive SMS when creating an account.

I entered the mobile number and started to brute force the OTP and I understood that the OTP is four digits long with just only numerals.

![](https://www.pethuraj.com/blog/wp-content/uploads/2021/01/BMW-Bug-Bounty-writeup-Registration-form.png)

I captured the request in Burp suite and sent to the intruder to brute force the OTP with the payload type as four-digit numbers which ranged from 0000-9999.

![](https://www.pethuraj.com/blog/wp-content/uploads/2021/01/BMW-Bug-Bounty-writeup-OTP-Bruteforce-1024x473.png)

By analysing the Http response from the intruder tab – it was observed that the wrong OTP returns 400 status code.

So, I filtered the status code which does not contain 4xx series of status codes.

![](https://www.pethuraj.com/blog/wp-content/uploads/2021/01/BMW-Bug-Bounty-writeup-Intruder-filter.png)

Now I could see a request popping up in the intruder tab returning 200 status code as per the filter.

By analyzing the response – I can see the OTP is accepted.

![](https://www.pethuraj.com/blog/wp-content/uploads/2021/01/BMW-Bug-Bounty-writeup-OTP-Accepted.png)

Upon entering the OTP in the browser – it got accepted.

![](https://www.pethuraj.com/blog/wp-content/uploads/2021/01/BMW-Bug-Bounty-writeup-Correct-OTP.png)

Boom! So here comes the next step to provide with Email address field to continue with the registration process thus bypassing the Account verification.

![](https://www.pethuraj.com/blog/wp-content/uploads/2021/01/BMW-Bug-Bounty-writeup-Verification-bypass.png)

For reporting this security flaw to BMW – **I’m honoured on their Security Experts Acknowledgment page**.

You can find the acknowledgement here :

[https://www.bmwgroup.com/en/Security.html](https://www.bmwgroup.com/en/general/Security.html)

![](https://www.pethuraj.com/blog/wp-content/uploads/2021/01/BMW-Hall-of-Fame-926x1024.png)

## You may like!

[![](https://www.pethuraj.com/blog/wp-content/uploads/2025/01/Use-Burp-Suite-like-a-PRO-Part-2-300x150.png)](https://www.pethuraj.com/blog/how-to-use-burp-suite-like-a-pro-part-2/)

#### [How to use Burp Suite Like a PRO? PART – 2](https://www.pethuraj.com/blog/how-to-use-burp-suite-like-a-pro-part-2/)

Ready to level up your Burp Suite skills? In part 2, I've compiled some awesome tips and tricks to help ...  

[Read More](https://www.pethuraj.com/blog/how-to-use-burp-suite-like-a-pro-part-2/)

[![burp suite advanced tutorials](https://www.pethuraj.com/blog/wp-content/uploads/2022/07/Mastering-Burp-suite-300x150.png)](https://www.pethuraj.com/blog/use-burpsuite-like-a-pro-part-1/)

#### [How to use Burp Suite Like a PRO? PART – 1](https://www.pethuraj.com/blog/use-burpsuite-like-a-pro-part-1/)

This blog series is an advanced tutorial of the popular web application security and penetration testing tool Burp Suite, to help ...  

[Read More](https://www.pethuraj.com/blog/use-burpsuite-like-a-pro-part-1/)

Share on Social Media

[x](https://x.com/share?url=https://www.pethuraj.com/blog/bmw-bugbounty-writeup/&text=BMW+Bug+Bounty+%26%238211%3B+Account+Verification+Bypass+writeup)[facebook](https://www.facebook.com/sharer.php?u=https://www.pethuraj.com/blog/bmw-bugbounty-writeup/)[linkedin](https://www.linkedin.com/shareArticle?url=https://www.pethuraj.com/blog/bmw-bugbounty-writeup/&title=BMW+Bug+Bounty+%26%238211%3B+Account+Verification+Bypass+writeup)[email](mailto:?subject=BMW+Bug+Bounty+%26%238211%3B+Account+Verification+Bypass+writeup&body=https://www.pethuraj.com/blog/bmw-bugbounty-writeup/)[whatsapp](https://api.whatsapp.com/send?text=BMW+Bug+Bounty+%26%238211%3B+Account+Verification+Bypass+writeup%20https://www.pethuraj.com/blog/bmw-bugbounty-writeup/)

## Post navigation

[Microsoft Bug Bounty Writeup – Stored XSS Vulnerability](https://www.pethuraj.com/blog/microsoft-bug-bounty-writeup-stored-xss-vulnerability/)

[How I made to Paypal Bug Bounty $750](https://www.pethuraj.com/blog/paypal-bug-bounty-writeup/)
