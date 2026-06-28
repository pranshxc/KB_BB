---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2018-04-17_idor-at-private-bug-bounty-program-that-could-leads-to-personal-data-leaks.md
original_filename: 2018-04-17_idor-at-private-bug-bounty-program-that-could-leads-to-personal-data-leaks.md
title: IDOR (at Private Bug Bounty Program) that could Leads to Personal Data Leaks
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
raw_sha256: 2d144eee90b3ca9cbabbe0f95fb32dfe67f5dc6c2c4b4fb3e326d7c1a642bf1e
text_sha256: 10d9cc7493aa2fd010cc6a7f47ea6056be7fad56f796fb4bfe7efbd06abfbf05
ingested_at: '2026-06-28T07:31:57Z'
sensitivity: unknown
redactions_applied: false
---

# IDOR (at Private Bug Bounty Program) that could Leads to Personal Data Leaks

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2018-04-17_idor-at-private-bug-bounty-program-that-could-leads-to-personal-data-leaks.md
- Source Type: markdown
- Detected Topics: idor, access-control, command-injection, otp, csrf, api-security
- Ingested At: 2026-06-28T07:31:57Z
- Redactions Applied: False
- Raw SHA256: `2d144eee90b3ca9cbabbe0f95fb32dfe67f5dc6c2c4b4fb3e326d7c1a642bf1e`
- Text SHA256: `10d9cc7493aa2fd010cc6a7f47ea6056be7fad56f796fb4bfe7efbd06abfbf05`


## Content

---
title: "IDOR (at Private Bug Bounty Program) that could Leads to Personal Data Leaks"
page_title: "IDOR (at Private Bug Bounty Program) that could Leads to Personal Data Leaks – Just Another Simple Write-Up"
url: "http://firstsight.me/2018/04/idor-at-private-bug-bounty-program-that-could-leads-to-personal-data-leaks/"
final_url: "http://firstsight.me/2018/04/idor-at-private-bug-bounty-program-that-could-leads-to-personal-data-leaks/"
authors: ["YoKo Kho (@YokoAcc)"]
bugs: ["IDOR"]
publication_date: "2018-04-17"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5912
---

[Bug Report](http://firstsight.me/category/bug-report/) / [Web Apps](http://firstsight.me/category/web-apps/) / [Write-Up](http://firstsight.me/category/write-up/)

# IDOR (at Private Bug Bounty Program) that could Leads to Personal Data Leaks

April 17, 2018 

[__]()

**In the name of Allah, the Most Gracious, the Most Merciful.**

Please kindly visit this simple paper directly to looking this release in simple:  
[[English Version] IDOR (at Private Bug Bounty Program) that could Leads to Personal Data Leaks](http://firstsight.me/fia07a53c4ec63d2b0d47fe27ea2645d82f8c98648/\[ENG\]%20IDOR%20\(at%20Private%20Bug%20Bounty%20Program\)%20that%20could%20Result%20of%20Information%20Leakage.pdf)

* * *

### I. PRE-INTRODUCTION

Few months ago, I got an invitation to private bug bounty program at Hackerone. To be honest, when I see that the program has been launch since **September 2015** , I really lost the interest to participate. But when I see the resolved report are only 29, then I think: “ _Why we not give it a try for a while?_ ”

In short, after few hours of testing, finally I found 2 subdomain takeover issue and one of the good one is finally found an IDOR that could result of **Personal Data Leak**. And yes, the detailed about IDOR could be seen at this simple report.

* * *

### II. INTRODUCTION

#### 2.1. Flow of the Application

Just like a common site that has an online shopping feature for their customer, this private program also provides the various payment method that could be choose by customer to pay their bill. To be honest, since its already around 3 months from the issue has been closed, then we didn’t remember exactly the list of payment choice except accepted the various international credit card.

When we learn how the application works, the flow to pay the bill itself need several steps to be conduct by the customer before the payment was proceed into the 3rd party service. Here are the general flows that we learn.

![](http://www.firstsight.me/wp-content/uploads/2019/12/Flow-of-the-Application.png)_Figure 1. Flow of the Application_

As could be seen from the flow above:  
**2.1.1.** User should choose the destination that they would like to choose. After the choice is decided and submitted, then the application will generate the temporary URL that saving our session that contains our choice (its normal and common at the shopping application) and send the POST Request that contains our personal data (that saved at our profile).
  
  
  POST /booking2/numbers_here/save_session/unique_sessions_over_here HTTP/1.1
  Host: target.com
  
  POST Value: the detail that has been saved into our profile

**2.1.2.** In this part, the user should fill the personal detail including choosing the payment method. When the payment detail has been submitted, then the application will changes the URL from “save_session” into “order” request.
  
  
  POST /booking2/numbers_here/order/unique_sessions_over_here HTTP/1.1
  Host: target.com
  
  POST Value: the detail that has been saved into our profile including the chosen payment method

**2.1.3.** When the POST request has check correctly by the server (in other words, there is no needed data anymore), then the application will automatically send the request to the function (including the unique hash and payment numbers) that proceed the payment to communicate with the 3rd party service (we guess it because the name of the function is very similar with the company that provides this kind of service). To censored the name, then we will name it “**xyzabc** ”.
  
  
  GET /xyzabc/unique_hash_over_here/payment_numbers_over_here/payment HTTP/1.1
  Host: target.com

**2.1.4.** After the unique hash and payment numbers are generated at the URL, then the application send this request to the POST Method to checkout the payment process to the 3rd party service. Here are a sample requests that sent by the application.
  
  
  POST /xyzabc/checkout/ HTTP/1.1
  Host: target.com
  
  csrfmiddlewaretoken=random_value_over_here&payment_id=means_payment_numbers&payment_product=card&card=unique_hash_of_the_card

**2.1.5.** It doesn’t matter if the detail is correct or not, the application will automatically generate the booking number. In this case, if the payment was failed, then the booking number (transaction ID) will contain the failed payment process information at the page.
  
  
  GET /order/X-12312312/instalment/resolve/?NTO=random_character_here HTTP/1.1
  Host: target.com

After few analysis, then we found out if there is a problem at the point 2.1.4, which is when the application was try to proceed the payment by send the “**payment_id** ” parameter to the server. In other words, by manipulating this parameter, then we could enumerate the success or failed booking that made by the other user.

* * *

#### 2.2. Few words about Insecure Direct Object Reference

This kind of vulnerability could allow the Attacker to gain the access into some purposes without the need to has a valid authorization. Basically, this execution is conduct by manipulate a value of the parameter that exist at the application. In its “implementation”, the purposes of this execution are to see or changing the (sensitive) information that just could be access by the user that has a valid authorization into that information.

In this situation, the problem related IDOR appears at the “**payment_id** ” parameter because the application didn’t validate the session yet in the checkout request.

* * *

### III. SUMMARY OF ISSUE

As described above, the site didn’t validate the session yet in the “**payment_id** ” request. This vulnerability could allow the Attacker to **get the failed or succeed booking** that created by other user at this site without the knowledge of their account and password.

As an information, **the best part of this issue** is we could enumerate those data automatically by brute forcing the “**payment_id** ” value.

* * *

### IV. PROOF OF CONCEPT

Previously, I try to enumerate directly the Booking Number (Transaction ID that explained at point 2.1.5) since the number looks so easy to be guessed. But the result of this is activity is failed (doesn’t show anything even at the browser or by viewing the frond-end source).

But, the good result has appeared when we try to change the “payment_id” parameter. By changing this parameter, then automatically the system will generate the other user’s booking number that could be used to enumerate the data that has the relation with those booking number. But please kindly note, this data can’t be seen without viewing the source.

For clearing the explanation, here is the simple step that should be conduct: For example, if we change into another ID (at this case, we change from **4055809** to **4055311**), we will get redirected into another user Booking Number (B-213xxxxx). At this part, we will get the information that someone with **[[email protected]](/cdn-cgi/l/email-protection)** as their email address was ordered the Hotel with 1 day trip duration. We also could get the other information such as total transaction, departure month, group size, location, and other.

Here is the sample request of sent “payment_id” parameter:

![](http://www.firstsight.me/wp-content/uploads/2019/12/Sample-Request-of-sent-Payment_id.png)_Figure 2. Sample Request of sent “Payment_id”_ ![](http://www.firstsight.me/wp-content/uploads/2019/12/Sample-Response-–-Enumerating-Other-Users’-Booked.png)_Figure 3. Sample Response – Enumerating Other Users’ Booked_

And yes, **one of the best part, we also could enumerate this data automatically**. By using the intruder mode and setting the redirect to always, then we could enumerate all of other user’s data.

![](http://www.firstsight.me/wp-content/uploads/2019/12/Enumerate-other-user-Data-Automatically.png)_Figure 4. Enumerate other user Data Automatically_

And for the recap, here is the flow of Attack related this issue:

![](http://www.firstsight.me/wp-content/uploads/2019/12/Flow-of-the-Attack.png)_Figure 5. Flow of the Attack_

* * *

### V. RESPONSE FROM THE PROGRAM’S OWNER

Around Four hours after they received the report (probably read the report), they fixed the issue completely and send the reward around 50 minutes after the fix has been verified.

![](http://www.firstsight.me/wp-content/uploads/2019/12/crop-0-0-1024-578-0-Response-from-the-Program’s-Owner.png)_Figure 6. Response from the Program’s Owner_

To be honest, **this one really break the records that I ever met.**

* * *

### VI. REFERENCES

• OTG-AUTHZ-004 – Testing for Insecure Direct Object References  
• CWE-932: Insecure Direct Object References
