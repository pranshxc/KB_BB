---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-10-13_500-bug-sensitive-data-exposure-to-broken-access-control-leads-how-i-able-to-tak.md
original_filename: 2021-10-13_500-bug-sensitive-data-exposure-to-broken-access-control-leads-how-i-able-to-tak.md
title: '500$ Bug: Sensitive Data Exposure to Broken Access Control leads, How I able
  to take over any account of India’s Biggest College Ever.👨‍💻'
category: documents
detected_topics:
- access-control
- password-reset
- command-injection
- otp
- information-disclosure
- api-security
tags:
- imported
- documents
- access-control
- password-reset
- command-injection
- otp
- information-disclosure
- api-security
language: en
raw_sha256: 04156bbdffe3fd8a934f41133d3de763d4fc5bef5b567cf2d94fb1efb98c53b3
text_sha256: fd5817d12eb21926409a80fe9846b4056ffd4cca0d7ec7f537f5ca418c31e8f5
ingested_at: '2026-06-28T07:32:08Z'
sensitivity: unknown
redactions_applied: false
---

# 500$ Bug: Sensitive Data Exposure to Broken Access Control leads, How I able to take over any account of India’s Biggest College Ever.👨‍💻

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-10-13_500-bug-sensitive-data-exposure-to-broken-access-control-leads-how-i-able-to-tak.md
- Source Type: markdown
- Detected Topics: access-control, password-reset, command-injection, otp, information-disclosure, api-security
- Ingested At: 2026-06-28T07:32:08Z
- Redactions Applied: False
- Raw SHA256: `04156bbdffe3fd8a934f41133d3de763d4fc5bef5b567cf2d94fb1efb98c53b3`
- Text SHA256: `fd5817d12eb21926409a80fe9846b4056ffd4cca0d7ec7f537f5ca418c31e8f5`


## Content

---
title: "500$ Bug: Sensitive Data Exposure to Broken Access Control leads, How I able to take over any account of India’s Biggest College Ever.👨‍💻"
url: "https://gowtham-naidu.medium.com/500-bug-sensitive-data-exposure-to-broken-access-control-leads-how-i-able-to-take-over-any-33658f16e265"
authors: ["Gowtham_Naidu (@NaiduPonnana)"]
bugs: ["OTP bypass", "Account takeover", "Password reset"]
bounty: "500"
publication_date: "2021-10-13"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3240
scraped_via: "browseros"
---

# 500$ Bug: Sensitive Data Exposure to Broken Access Control leads, How I able to take over any account of India’s Biggest College Ever.👨‍💻

500$ Bug: Sensitive Data Exposure to Broken Access Control leads, How I able to take over any account of India’s Biggest College Ever.👨‍💻
Gowtham_Naidu
Follow
4 min read
·
Oct 12, 2021

467

5

* Introduction *

Hello Hackers, This is Gowtham here an Ethical Hacker and Penetration Tester who loves to look into loopholes😅. This is my first blog out here on Internet, So Kindly forgive me if there are any mistakes. So today, I am gonna tell you “How I am able to take over any user account of India’s popular and biggest college within 3mins”. Without any delay, Let’s start our Journey of Learning❤️[Note: I don’t want to disclose the Name of the College due to some reasons, We will call it as <example.com>]

Sensitive Data Exposure aka Information disclosures :

This college is having two domains namely “example.com” where students can participate in exams and check their results, So this is not having many functionalities. The other domain is “target.com” which is the main domain where it had many great functionalities like Payment System, Creation of Student ID’s and whole students data along with their credit cards, and much more.

Get Gowtham_Naidu’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

So Usually, Everyone will start with a domain which is having many functionalities and even I did the same😁But I can’t able to login into this domain because I am not having the credentials to do so. Then I switched to the next domain (example.com) and started looking into Javascript files and capturing all the requests and looking into their responses. There I see something crispy in Forgot Password, where the request looks like this

Press enter or click to view image in full size

Here I supplied my own admission number, and then while I am seeing the Response, The Registered Mobile Number is being disclosed. You may think about what’s wrong here but even If I give another user an admission number I can able to get his/her mobile number. Now the website asks us to enter the Mobile Number to send the OTP to Reset the Password.

Broken Access Control aka Account Takeover :

So when I enter some wrong number other than the Registered Number, It’s popping up a Message to Enter the Register Number. It means It’s only validating the Phone Number on the Client-Side So at this moment I entered the Registered Mobile Number of some other user which we found out earlier. Hurray!!!, It’s successfully Bypassed, Now I can tamper the mobile number field to my own number so that I can get OTP instead of going to the Registered mobile number.

Press enter or click to view image in full size
When I enter the Registered Mobile Number and change the Phone Number value to mine.

Yes, We did it. Now we got the OTP of the User and we entered it, Now I can able to reset the password of any user without knowing him/her. This leads to account takeover of anyone on the 2nd domain.

“ I immediately reported this bug to the domain administrator and got appreciated along with the Bounty of 500$”.

Final Touch:

This is where our story should usually end, but not in our case.

In my next blog, I am gonna tell you I used these vulnerabilities to bypass the Payment system and be able to pay every student for only 1$. That will be most interesting and helpful to newcomers and others too.

Thanks for spending your valuable time. Meet you in my 2nd blog very soon. For More tips and suggestions follow me on Twitter and Instagram.

Instagram: https://www.instagram.com/gowtham_ponnana/

Twitter: https://www.twitter.com/gowtham_ponnana/

Regards,

Gowtham Naidu Ponnana

Press enter or click to view image in full size
