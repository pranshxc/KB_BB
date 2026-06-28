---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-03-01_how-a-simple-idor-impacted-the-data-of-thousands-of-customers-of-an-indian-autom.md
original_filename: 2023-03-01_how-a-simple-idor-impacted-the-data-of-thousands-of-customers-of-an-indian-autom.md
title: How a simple IDOR impacted the data of thousands of customers of an Indian
  automotive giant
category: documents
detected_topics:
- password-reset
- idor
- command-injection
- otp
- rate-limit
- automation-abuse
tags:
- imported
- documents
- password-reset
- idor
- command-injection
- otp
- rate-limit
- automation-abuse
language: en
raw_sha256: bfda66f85d0497b0a955e200e9b3ce6354a9f21280dde7f5e2fa6bb3795df148
text_sha256: 2dd8b0fd8756bceb22d5e9f33370f56c53349717ea3a5d3a1304969ea8c5fffb
ingested_at: '2026-06-28T07:32:19Z'
sensitivity: unknown
redactions_applied: false
---

# How a simple IDOR impacted the data of thousands of customers of an Indian automotive giant

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-03-01_how-a-simple-idor-impacted-the-data-of-thousands-of-customers-of-an-indian-autom.md
- Source Type: markdown
- Detected Topics: password-reset, idor, command-injection, otp, rate-limit, automation-abuse
- Ingested At: 2026-06-28T07:32:19Z
- Redactions Applied: False
- Raw SHA256: `bfda66f85d0497b0a955e200e9b3ce6354a9f21280dde7f5e2fa6bb3795df148`
- Text SHA256: `2dd8b0fd8756bceb22d5e9f33370f56c53349717ea3a5d3a1304969ea8c5fffb`


## Content

---
title: "How a simple IDOR impacted the data of thousands of customers of an Indian automotive giant"
url: "https://medium.com/@kushjain0107/how-simple-idor-impacted-the-data-of-thousands-of-customers-of-an-indian-automotive-giant-fdbd2ef1c2c6"
authors: ["Kushal Jain", "Ashutosh Mahajan"]
bugs: ["Account takeover", "Information disclosure", "IDOR"]
publication_date: "2023-03-01"
added_date: "2023-03-06"
source: "pentester.land/writeups.json"
original_index: 1445
scraped_via: "browseros"
---

# How a simple IDOR impacted the data of thousands of customers of an Indian automotive giant

How a simple IDOR impacted the data of thousands of customers of an Indian automotive giant
Kushal Jain
Follow
3 min read
·
Mar 1, 2023

50

3

On 9th August 2022, I and my colleague 
Ashutosh Mahajan
 were testing a production-based android application as a part of our practice. The application on which we were testing was related to an EV company.

Brief about the app :

The app was XYZ and it is an app that EV users use to locate charging stations and pay for the facility.

Findings :

Insecure System Design :

As we started our testing, on the very first minute we found a issue. The OTP which were sent at the time of registration and password reset was given beforehand in the response (this plays a very crucial role later on).

Press enter or click to view image in full size
OTP disclosed in response

Indirect Object Reference :

As the app was specifically developed to pay at charging station via the application. So, they integrated two wallets for the payments at the EV charging stations. One being PayTm wallet and the other was the application’s built-in wallet. So whenever, any user topped-up their wallet, an invoice was created for that transaction. The request which was responsible for downloading the invoice had a invoiceNo parameter that was vulnerable to IDOR.

Press enter or click to view image in full size
IDOR at downloading invoices

When examining the above request, if we change the invoiceNo to another invoiceNo of our other testing account, we got a valid response and we were able to download their invoice.

Press enter or click to view image in full size
Image of invoice downloaded.

The invoice had details like Name, GST No., Address, Mobile No., Customer ID., and transaction details.

Get Kushal Jain’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Chaining the above mentioned findings :

For demonstration purposes, we created two users Test1 and Test2 . Test1 being the attacker and Test2 being a normal customer.

We login using Test1 and we then enumerate for invoiceNo of Test2 .
After, enumerating the invoice which belonged to Test2 , we found it’s mobileNo from it.
Now heading back to the login page, to login as Test2 we entered their mobileNo and clicked on the forgot password option to reset their password.
As we were getting the OTP in the response, and also the application was vulnerable to response manipulation we were able to change the password of Test2 without their consent and without them knowing.
And on the side of Test2 , they were completely unaware of the fact that their password is changed and their account has been compromised.
More Findings :

This app not only has the above mentioned two major vulnerabilities but also there are other severe vulnerabilities such as response manipulation, no proper validation of phone number which could be exploited to create multiple bot accounts, clear text transmission of credentials, no rate limit, and many more such vulnerabilities.

Note:

On 24/10/2022, we were able to get invoices of more than 25,000+ customers.

Press enter or click to view image in full size
Enumerated invoices.
Conclusion :

After linking all of these vulnerabilities, its impact is high. It affects the company and the customer both. This could be further escalated to monetary loss of customers and harming the nature of the app, as there are no strict security policies implemented in order to make the app safe.

Updates :

As of today i.e. 01/03/2023 all the issues which have been reported have been fixed.
