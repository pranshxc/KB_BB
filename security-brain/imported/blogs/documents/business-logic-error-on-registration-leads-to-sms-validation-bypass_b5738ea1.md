---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-03-10_business-logic-error-on-registration-leads-to-sms-validation-bypass.md
original_filename: 2021-03-10_business-logic-error-on-registration-leads-to-sms-validation-bypass.md
title: Business Logic Error on Registration Leads to SMS Validation Bypass
category: documents
detected_topics:
- mfa
- command-injection
- otp
- business-logic
tags:
- imported
- documents
- mfa
- command-injection
- otp
- business-logic
language: en
raw_sha256: b5738ea1bc21ecded84a6c88ee12ed4c92f3231b8ea43e616e76347336f5c92a
text_sha256: e9b1919f281347711209910a3090140a8cb8d07bf5573bbe7a2349cbf8f35a13
ingested_at: '2026-06-28T07:32:05Z'
sensitivity: unknown
redactions_applied: false
---

# Business Logic Error on Registration Leads to SMS Validation Bypass

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-03-10_business-logic-error-on-registration-leads-to-sms-validation-bypass.md
- Source Type: markdown
- Detected Topics: mfa, command-injection, otp, business-logic
- Ingested At: 2026-06-28T07:32:05Z
- Redactions Applied: False
- Raw SHA256: `b5738ea1bc21ecded84a6c88ee12ed4c92f3231b8ea43e616e76347336f5c92a`
- Text SHA256: `e9b1919f281347711209910a3090140a8cb8d07bf5573bbe7a2349cbf8f35a13`


## Content

---
title: "Business Logic Error on Registration Leads to SMS Validation Bypass"
url: "https://infosecwriteups.com/business-logic-error-on-registration-leads-to-sms-validation-bypass-80380b3ff629"
authors: ["pleorqy (@pleorqy)"]
bugs: ["2FA / MFA bypass"]
publication_date: "2021-03-10"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3825
scraped_via: "browseros"
---

# Business Logic Error on Registration Leads to SMS Validation Bypass

Business Logic Error on Registration Leads to SMS Validation Bypass
pleorqy
Follow
4 min read
·
Mar 11, 2021

529

1

Hello, fellow hunters. It is time for another write-up. It was basically a business logic error which let me to bypass the SMS validation on registration. Let’s get right into it.

Target

This time, my target was a financial services company, which has nothing to do with the story. They had very few assets in their scope. Registration / log-in panel and a few static websites that did not have any functionality. Since only the registration panel had functionality, I decided to test it briefly and move forward to other programs. I will not be disclosing any screenshots from the app as it does not allow me to disclose details about the bug. However, there will be snippets from my Burp Suite logs placed in the story. The target website will be mentioned as “redacted.com”.

Registration Flow

First thing to do when testing functionality or an app is using it like a normal user, and understand the flow thoroughly. I fired up my Burp Suite and went through the registration process as explained below while logging all the requests and responses:

1- Navigate to redacted.com/registration
2- The user is asked to enter his/her First Name, Last Name, Email Address and Phone Number. The application forwards the user to redacted.com/registration/api/email-confirmation
3- After providing the information required, first, a 6-digit alphanumeric confirmation code is sent to your email address. The user enters the code and proceeds to the next step on another endpoint, which is redacted.com/registration/api/confirm-mobile
4- On this step, a 6-digit numeric confirmation code is sent to the phone of the user with SMS. User enters the code and gets redirected to redacted.com/registration/api/user-credentials
5- As the last step, the user is asked to enter his/her username and password. Registration process is completed when the user provides the credentials.

Exploitation

On step 3, when the user enters the confirmation code sent to their email, a POST request is sent with the following request body:

Step 3) Email confirmation

Pretty straightforward, right? The current step, the next step, and the optional parameter really does not matter. The only parts that matter is the current step and the next step.

Get pleorqy’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

On step 4, when confirming the code sent with SMS, another POST request is initiated with the following body:

Step 4) SMS confirmation

There is a resemblance, right? Here comes the fun part, which is exploitation. Here are the steps I followed:

1- On step 3, turn the intercept on and enter the confirmation code sent to your email address. In the body, as shown in the first picture above, the current step is specified to be email confirmation. Now before forwarding the request, replace the highlighted area in picture 1 with the highlighted area in the second picture. Forward the request.
2- The user is asked to enter the verification code sent with SMS, which means that the user is currently on step 4. The URL is redacted.com/registration/api/confirm-mobile currently.
3- Without entering the SMS code, navigate to redacted.com/registration.

After the 3rd step, I was prompted to enter a username and a password for my account, which indicated that I successfully bypassed the SMS validation.

Why did that happen though?

When I changed the body of the email confirmation request to the body of the SMS confirmation request, the application accepted the email code as valid. However, it also supposed that SMS confirmation was also done, since I have change the body parameters, and got a successful response. When I entered the URL redacted.com/registration manually, the application assumed that I have already completed the SMS code verification, and therefore redirected me to the page where I was asked for a username and a password.

Takeaway
When a program has a specific functionality or an endpoint in their scope, try to play around with it as much as you can. As this functionality was directly specified in the scope, my report was of great importance, hence I got a payout of $$$.

I hope this write-up helps you in your bug hunting journey and gives you a feeling of how versatile business logic vulnerabilities can be. See you in a future write-up!

You can follow me on Twitter. @pleorqy
