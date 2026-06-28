---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2018-04-18_how-i-get-the-name-of-the-hotel-and-other-data-that-you-ever-stay-personal-data-.md
original_filename: 2018-04-18_how-i-get-the-name-of-the-hotel-and-other-data-that-you-ever-stay-personal-data-.md
title: 'How I Get the Name of the Hotel (and other Data) that you ever Stay - Personal
  Data Leaks: Private Bug Bounty Program'
category: documents
detected_topics:
- idor
- access-control
- command-injection
- otp
- csrf
- api-security
tags:
- imported
- documents
- idor
- access-control
- command-injection
- otp
- csrf
- api-security
language: en
raw_sha256: 387d65b884c739fa69a337d12c4bc7198803827ab3218a1b91920644d1246733
text_sha256: a853ce777ab6c3a74485d0172fa06a030548abe366b58a836c4633c82aa4d3dd
ingested_at: '2026-06-28T07:31:57Z'
sensitivity: unknown
redactions_applied: false
---

# How I Get the Name of the Hotel (and other Data) that you ever Stay - Personal Data Leaks: Private Bug Bounty Program

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2018-04-18_how-i-get-the-name-of-the-hotel-and-other-data-that-you-ever-stay-personal-data-.md
- Source Type: markdown
- Detected Topics: idor, access-control, command-injection, otp, csrf, api-security
- Ingested At: 2026-06-28T07:31:57Z
- Redactions Applied: False
- Raw SHA256: `387d65b884c739fa69a337d12c4bc7198803827ab3218a1b91920644d1246733`
- Text SHA256: `a853ce777ab6c3a74485d0172fa06a030548abe366b58a836c4633c82aa4d3dd`


## Content

---
title: "How I Get the Name of the Hotel (and other Data) that you ever Stay - Personal Data Leaks: Private Bug Bounty Program"
url: "https://medium.com/@YoKoKho/idor-at-private-bug-bounty-program-that-could-leads-to-personal-data-leaks-d2536d026bf5"
authors: ["YoKo Kho (@YokoAcc)"]
bugs: ["IDOR"]
publication_date: "2018-04-18"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5911
scraped_via: "browseros"
---

# How I Get the Name of the Hotel (and other Data) that you ever Stay - Personal Data Leaks: Private Bug Bounty Program

How I Get the Name of the Hotel (and other Data) that you ever Stay - Personal Data Leaks: Private Bug Bounty Program
YoKo Kho
Follow
6 min read
·
Apr 18, 2018

77

بسم الله الرحمن الرحيم

Please kindly visit this simple paper directly to looking this release in simple:

[English Version] IDOR (at Private Bug Bounty Program) that could Leads to Personal Data Leaks

I. PRE-INTRODUCTION

Few months ago, I got an invitation to private bug bounty program at Hackerone. To be honest, when I see that the program has been launch since September 2015, I really lost the interest to participate. But when I see the resolved report are only 29, then I think: “Why we not give it a try for a while?”

In short, after few hours of testing, finally I found 2 subdomain takeover issue and one of the good one is finally found an IDOR that could result of Personal Data Leak. And yes, the detailed about IDOR could be seen at this simple report.

II. INTRODUCTION

2.1. Flow of the Application
Just like a common site that has an online shopping feature for their customer, this private program also provides the various payment method that could be choose by customer to pay their bill. To be honest, since its already around 3 months from the issue has been closed, then we didn’t remember exactly the list of payment choice except accepted the various international credit card.

When we learn how the application works, the flow to pay the bill itself need several steps to be conduct by the customer before the payment was proceed into the 3rd party service. Here are the general flows that we learn.

As could be seen from the flow above:

2.1.1. User should choose the destination that they would like to choose. After the choice is decided and submitted, then the application will generate the temporary URL that saving our session that contains our choice (its normal and common at the shopping application) and send the POST Request that contains our personal data (that saved at our profile).

POST /booking2/numbers_here/save_session/unique_sessions_over_here HTTP/1.1
Host: target.com
POST Value: the detail that has been saved into our profile

2.1.2. In this part, the user should fill the personal detail including choosing the payment method. When the payment detail has been submitted, then the application will changes the URL from “save_session” into “order” request.

POST /booking2/numbers_here/order/unique_sessions_over_here HTTP/1.1
Host: target.com
POST Value: the detail that has been saved into our profile including the chosen payment method

2.1.3. When the POST request has check correctly by the server (in other words, there is no needed data anymore), then the application will automatically send the request to the function (including the unique hash and payment numbers) that proceed the payment to communicate with the 3rd party service (we guess it because the name of the function is very similar with the company that provides this kind of service). To censored the name, then we will name it “xyzabc”.

GET /xyzabc/unique_hash_over_here/payment_numbers_over_here/payment HTTP/1.1
Host: target.com

2.1.4. After the unique hash and payment numbers are generated at the URL, then the application send this request to the POST Method to checkout the payment process to the 3rd party service. Here are a sample requests that sent by the application.

POST /xyzabc/checkout/ HTTP/1.1
Host: target.com
csrfmiddlewaretoken=random_value_over_here&payment_id=means_payment_numbers&payment_product=card&card=unique_hash_of_the_card

2.1.5. It doesn’t matter if the detail is correct or not, the application will automatically generate the booking number. In this case, if the payment was failed, then the booking number (transaction ID) will contain the failed payment process information at the page.

GET /order/X-12312312/instalment/resolve/?NTO=random_character_here HTTP/1.1
Host: target.com

After few analysis, then we found out if there is a problem at the point 2.1.4, which is when the application was try to proceed the payment by send the “payment_id” parameter to the server. In other words, by manipulating this parameter, then we could enumerate the success or failed booking that made by the other user.

Get YoKo Kho’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

2.2. Few words about Insecure Direct Object Reference
This kind of vulnerability could allow the Attacker to gain the access into some purposes without the need to has a valid authorization. Basically, this execution is conduct by manipulate a value of the parameter that exist at the application. In its “implementation”, the purposes of this execution are to see or changing the (sensitive) information that just could be access by the user that has a valid authorization into that information.

In this situation, the problem related IDOR appears at the “payment_id” parameter because the application didn’t validate the session yet in the checkout request.

III. SUMMARY OF ISSUE

As described above, the site didn’t validate the session yet in the “payment_id” request. This vulnerability could allow the Attacker to get the failed or succeed booking that created by other user at this site without the knowledge of their account and password.

As an information, the best part of this issue is we could enumerate those data automatically by brute forcing the “payment_id” value.

IV. PROOF OF CONCEPT

Previously, I try to enumerate directly the Booking Number (Transaction ID that explained at point 2.1.5) since the number looks so easy to be guessed. But the result of this is activity is failed (doesn’t show anything even at the browser or by viewing the frond-end source).

But, the good result has appeared when we try to change the “payment_id” parameter. By changing this parameter, then automatically the system will generate the other user’s booking number that could be used to enumerate the data that has the relation with those booking number. But please kindly note, this data can’t be seen without viewing the source.

For clearing the explanation, here is the simple step that should be conduct: For example, if we change into another ID (at this case, we change from 4055809 to 4055311), we will get redirected into another user Booking Number (B-213xxxxx). At this part, we will get the information that someone with cencored@cencored.com as their email address was ordered the Hotel with 1 day trip duration. We also could get the other information such as total transaction, departure month, group size, location, and other.

Here is the sample request of sent “payment_id” parameter:

Press enter or click to view image in full size
Figure 1: Sample Request of sent “Payment_id”
Press enter or click to view image in full size
Figure 2: Sample Response — Enumerating Other Users’ Booked

And yes, one of the best part, we also could enumerate this data automatically. By using the intruder mode and setting the redirect to always, then we could enumerate all of other user’s data.

Press enter or click to view image in full size
Figure 3: Enumerate other user Data Automatically

And for the recap, here is the flow of Attack related this issue:

Press enter or click to view image in full size
Figure 4: Flow of Attack
V. RESPONSE FROM THE PROGRAM’S OWNER

Around Four hours after they received the report (probably read the report), they fixed the issue completely and send the reward around 50 minutes after the fix has been verified.

Press enter or click to view image in full size
Figure 5: Response from the Program’s Owner

To be honest, this one really break the records that I ever met.

VI. REFERENCES
OTG-AUTHZ-004 — Testing for Insecure Direct Object References
CWE-932: Insecure Direct Object References
