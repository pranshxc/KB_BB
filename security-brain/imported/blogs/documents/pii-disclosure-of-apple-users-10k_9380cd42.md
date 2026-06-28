---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-07-07_pii-disclosure-of-apple-users-10k.md
original_filename: 2022-07-07_pii-disclosure-of-apple-users-10k.md
title: PII Disclosure of Apple Users ($10k)
category: documents
detected_topics:
- rate-limit
- api-security
- idor
- command-injection
- information-disclosure
- supply-chain
tags:
- imported
- documents
- rate-limit
- api-security
- idor
- command-injection
- information-disclosure
- supply-chain
language: en
raw_sha256: 9380cd423b2752d489b060883d8dab4178a4b3106136687893de401d345e5784
text_sha256: f472aea4edfcec2c2c996f7b45ffe2dbcd2b18223d9032c1cb4c40e171d638cc
ingested_at: '2026-06-28T07:32:12Z'
sensitivity: unknown
redactions_applied: false
---

# PII Disclosure of Apple Users ($10k)

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-07-07_pii-disclosure-of-apple-users-10k.md
- Source Type: markdown
- Detected Topics: rate-limit, api-security, idor, command-injection, information-disclosure, supply-chain
- Ingested At: 2026-06-28T07:32:12Z
- Redactions Applied: False
- Raw SHA256: `9380cd423b2752d489b060883d8dab4178a4b3106136687893de401d345e5784`
- Text SHA256: `f472aea4edfcec2c2c996f7b45ffe2dbcd2b18223d9032c1cb4c40e171d638cc`


## Content

---
title: "PII Disclosure of Apple Users ($10k)"
url: "https://ahmdhalabi.medium.com/pii-disclosure-of-apple-users-10k-d1e3d29bae36"
authors: ["Ahmad Halabi (@Ahmad_Halabi_)"]
programs: ["Apple"]
bugs: ["IDOR", "Lack of rate limiting", "Bruteforce", "Information disclosure"]
bounty: "10,000"
publication_date: "2022-07-07"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 2478
scraped_via: "browseros"
---

# PII Disclosure of Apple Users ($10k)

PII Disclosure of Apple Users ($10k)
Ahmad Halabi
Follow
7 min read
·
Jul 7, 2022

1.3K

15

Press enter or click to view image in full size

بِسْمِ اللَّـهِ الرَّحْمَـٰنِ الرَّحِيمِ

Hello,

My name is Ahmad Halabi. I work as a Senior Cyber Security Specialist in UAE. I also do some Bug Bounty Hunting when I have a Free Time. You can check my Biography here: https://ahmadhalabi.net/biography/ .

Intro ::

After I saw that Apple started paying for Impactful Web Application Vulnerabilities, I decided to spend couple of hours hacking Apple, And yes I was able to find some cool bugs.

In this article, I will be disclosing one of my favorite bugs that I found in Apple. Enjoy Reading ^_^

Finding my Target ::

When you come across a big Asset like Apple or Microsoft, you have to know from where to start and what to check. For me I was looking for a target that is considered an important asset to Apple and contains valuable private information so the bounty will be worthy.

I found an interesting website which is https://applepaysupplies.com/.

Apple Pay Supplies: allows you to order Apple related Kits such as `Apple Pay Decals Kit` and `Apple Pay Signage Kit`.

Studying the Application Structure ::

I started checking the target website as a normal user who wants to order a kit. I turned on Burp Suite to intercept all the traffic of this website, then I proceeded with the order and navigated to `Place Order`.

After that I filled my Shipping Information and submitted my order.

Shipping Information includes: Full name, Company, Address information (Country, City, Street, Zip code) and Phone Number.

There is tracking order feature so after submitting your order you can track it.

To track your order, you have to put your email address and the order number that is assigned once the order is created.

I noticed here two interesting variables that need to be investigated further which are Order Number and Email .

Identifying the Vulnerability :: Chaining IDOR with Rate Limit discloses Shipping Information.

1st Step:

After hitting Submit button to track the Order Status, The page showed me Order details and I noticed this URL in the browser tab:

https://applepaysupplies.com/trackorder?order_id=APP1162306&email=my.test.email@gmail.com&language_id=1

Press enter or click to view image in full size
Tracking Your Order

2nd Step:

Here I thought about an IDOR vulnerability chained with Rate Limit mechanism to guess the order_id of an Apple user who I already know his email ID.

So I started analyzing the order_id value: APP1162306 by generating multiple Orders and comparing their order_id values.

APP characters are fixed.
We have 7 numbers after APP which can be brute forced.

3rd Step:

I navigated to the target URL https://applepaysupplies.com/trackorder?order_id=APP1162306&email=my.test.email@gmail.com&language_id=1 but the surprised thing was that it showed a blank page other than the Order Details response that was shown after hitting the Submit button.

Press enter or click to view image in full size
Blank Page

I was not able to do the attack by hitting Submit button nor intercept its request because the Application was using front-end fetching via JavaScript thus no backend request related to the target URL was sent. So I needed to analyze JavaScript Files / Burp History and check for an API and see how the data are being fetched and retrieved.

4th Step:

After some Recon and Analysis, I found an API that interacts with the backend to fetch the Order Information.

Alternative Request: https://applepaysupplies.com/api/Home/GetOrderStatus?orderno=APP1162306&email=my.test.email@gmail.com

This API Request is responsible for Fetching the Order Status Details.

Press enter or click to view image in full size
Get Order Status Details

5th Step:

Now it was easy to proceed by generating 7 numbers wordlist and brute forcing the Order number in order to get the Valid Order Status Details.

Press enter or click to view image in full size
Setting up Attack in Intruder

Luckily there was no Rate Limit Protection in place so I was able to brute force the Order Number of any valid Apple User and I will disclose his Shipping Address Information.

Press enter or click to view image in full size
Found Valid orderno and disclosed Shipping Information

Reporting ::

I made a detailed PoC and Reported this Vulnerability to Apple.
After a while, Apple Fixed the Vulnerability and Requested me to check the Fix.

Checking The Fix ::

Apple fixed the Vulnerability by removing the API call responsible for fetching the Order Status Details (/api/Home/GetOrderStatus). So now users can only use the main Functionality which is Track Order.

Press enter or click to view image in full size
Removing /api/Home/GetOrderStatus

Instead of the removed API endpoint, they used the Track Order request (https://applepaysupplies.com/trackorder?order_id=APP1162306&email=my.test.email@gmail.com) to fetch the status details.

Get Ahmad Halabi’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

But they did some enhancement to this Track Order Functionality. They used CryptoJS Library to encrypt the values since now they are being sent and fetched from the Client Side.

So I had to check the Application carefully again and analyze the new changes deployed in addition to the new Encryption added.

Bypassing The Fix ::

Step 1:

I was checking the website again. I already know the main endpoint to track orders (https://applepaysupplies.com/trackorder) that accepts GET request with the following parameters: order_id that stands for the Order Number and email.

Step 2:

I started analyzing the Request.

Using Burp Suite, I tried sending a GET request to the target URL:

https://applepaysupplies.com/trackorder?order_id=APP1162306&email=my.test.email@gmail.com

but the response was not showing the Order Status nor Shipping details of this valid order.

Press enter or click to view image in full size
No Order Status Details in the Response

This was a protection done by Apple End when they Fixed my old bug. So I was unable to use Intruder to brute force `Order Number` as I did in the previous bug with the API Endpoint.

Step 3:

I started analyzing the Client Side Behavior.

I opened the request (https://applepaysupplies.com/trackorder?order_id=APP1162306&email=my.test.email@gmail.com) in the browser.

I noticed that there is a delay in showing the order details. It takes 1–2 seconds after loading to show the order details.

Press enter or click to view image in full size

This behavior explained why I was not able to see the shipping details on the request level in Burp Suite.

Step 4:

I started analyzing JavaScript Files.

After checking JavaScript files, I noticed that the application is using a Library called CryptoJS to encrypt the Email and the Order Number once requesting an order status. By this technique, Apple made it hard to brute force the Order Number.

I analyzed how the Encryption is done in the Application, and with the help of my Friend Max (h1 Profile), We wrote a script to encrypt the needed values using CryptoJS library as the Application did and brute force the Order Number.

Press enter or click to view image in full size
Script to Encrypt the values with CryptoJS and Brute Force the Order Number

With the advantage of the absence of Rate Limit protection against this GET endpoint, I was able to brute force the Order Number successfully and disclose the Shipping Information Again.

Press enter or click to view image in full size
Brute Force Succeeded and Disclosure of Shipping Information

Reporting ::

Apple requested me to send the Bypass Details in a New Report since the Old Fix is Successful and the Vulnerability is now found in a different Endpoint.
Apple confirmed the Vulnerability And Rewarded me the first half of the Bounty.
Apple Took some time to implement a new Fix.

Confirming the Fix ::

Apple kept the Crypto JS Library in place, They just enhanced and increased the Encryption Level to make it harder to break.

Apple didn’t implement a Rate Limit Protection, but they Increased the Length of the Order Number.

Before, the Order Number was made up of: APP + 7 numbers.

Now, the Order Number is made up of: APP + 28 Characters & Numbers.

Example: `APPF68CAA9D1F174F91B61ECC7568D7`

Brute Forcing 28 Random Characters is unfeasible even if you were able to decrypt their Encryption.

So I saw that the Vulnerability is Well Fixed and Reported back to Them.

Bounty ::

Apple decided to reward me in Total $10,000 for the Main Vulnerability and the Bypass. My highest bounty so Far.

Press enter or click to view image in full size
Press enter or click to view image in full size

Apple is a great Bug Bounty Program with Big Scope. The only problem is that they are Late in Operation (Need time to investigate / Fix). But it is worth spending time on it because it is highly rewardable if you find an Interesting Vulnerability.

I created private bug bounty course to help struggled hunters find valid bugs and earn bounties.

If you are struggling in finding valid bugs or earning enough bounties, you just need to enroll and your mindset about approaching bug bounty hunting will improve.

Check Student bounties and feedbacks and enroll now: https://ahmadhalabi.net/course

Press enter or click to view image in full size

You can follow me on:

LinkedIn / Twitter / Instagram / My Website

Press enter or click to view image in full size
Press enter or click to view image in full size

Kind Regards.
