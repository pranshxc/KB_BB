---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-10-12_disclose-emails-phone-numbers-more-for-facebook-users-who-tried-to-add-funds-to-.md
original_filename: 2020-10-12_disclose-emails-phone-numbers-more-for-facebook-users-who-tried-to-add-funds-to-.md
title: Disclose Emails, phone numbers, more For Facebook users who tried to add funds
  to their account
category: documents
detected_topics:
- sso
- command-injection
- otp
- information-disclosure
- supply-chain
tags:
- imported
- documents
- sso
- command-injection
- otp
- information-disclosure
- supply-chain
language: en
raw_sha256: 812cf57b62b9ae04a249323a8c26bf98060a0f2a5b47bc00a100266dbf7befb1
text_sha256: 92a67ff8ba48b18bd1d31844d892df8b66ec80f947401805b3e276c7cdb00fc7
ingested_at: '2026-06-28T07:32:03Z'
sensitivity: unknown
redactions_applied: false
---

# Disclose Emails, phone numbers, more For Facebook users who tried to add funds to their account

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-10-12_disclose-emails-phone-numbers-more-for-facebook-users-who-tried-to-add-funds-to-.md
- Source Type: markdown
- Detected Topics: sso, command-injection, otp, information-disclosure, supply-chain
- Ingested At: 2026-06-28T07:32:03Z
- Redactions Applied: False
- Raw SHA256: `812cf57b62b9ae04a249323a8c26bf98060a0f2a5b47bc00a100266dbf7befb1`
- Text SHA256: `92a67ff8ba48b18bd1d31844d892df8b66ec80f947401805b3e276c7cdb00fc7`


## Content

---
title: "Disclose Emails, phone numbers, more For Facebook users who tried to add funds to their account"
url: "https://medium.com/@mustafa0x2021/disclose-emails-phone-numbers-other-information-for-facebook-users-who-tried-to-add-funds-to-31aea5f973a5"
authors: ["Mustafa Ahmed (@mustafa0x2021)"]
programs: ["Meta / Facebook"]
bugs: ["Information disclosure"]
bounty: "500"
publication_date: "2020-10-12"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4201
scraped_via: "browseros"
---

# Disclose Emails, phone numbers, more For Facebook users who tried to add funds to their account

Disclose Emails, phone numbers, more For Facebook users who tried to add funds to their account
Mustafa
Follow
3 min read
·
Oct 12, 2020

65

Press enter or click to view image in full size

Facebook users can add funds to their ADS, business account using several options one of them by using local payment this option is available in more than 20 countries
I found issue affect all the users who clicked on the local payment option

while I was testing on Facebook I found an option to send the invoice to an email

viewing the request for that options found out that using incrementing id

POST /fb-payment/7777777/send-email
{"email":examle@example.com}

in this request, I could send any invoice to my email by changing the id

continue test found an easier way to get invoices

Request

POST /fb-payment/7777777/execute

the response for it was

{"amount":777,"payment_method_id":"EX","country":"EG","refrence_number":"777","order_id":"777","status":"pending","create_data":"2020-9-10T05:08:08"}

continue search reading some documentation and some fuzzing found that I could use the “order_id” and “payment_method_id” to retrieve a payments information

Get Mustafa’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

which I can get these variables for all the users who tried that option from the previous request which is using incrementing id not random at all

Retrieve payments information
GET
fb-payments?payment_method_code=XX&payment_id=XXXXXXXXXXXXXXXX&payer_amount=null&currency=null&country=null&redirect=https://facebook.com

the response of this request was

{"id":7777777,"state":"PENDING","amount":400,"currency":"EGP","country":"EG","redirect":"https://facebook.com","payment_method_code":"EX","name":"Mustafa Ahmed",user_id:100,"email":"example@example.com""phone":"01111111111",user_agent":{"ua":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36","browser":{"name":"Chrome","version":"85.0.4183.121","major":"85"},"engine":{"name":"Blink"},"os":{"name":"Windows","version":"10"},"device":{},"cpu":{"architecture":"amd64"}}}
by that I was able to disclose this information for all Facebook users who tried to add funds to their Facebook by this option like
email
phone number
user name
user id for the ads ,business account managed
User-agent
fund amount
etc.
There was about 7 million records for users at that time
Also I mention issue that this data doesn’t get deleted ever still stored and shard with other third parties than the payment processor

Facebook is using a partner to process that payment

according to Facebook whitehat info(https://www.facebook.com/whitehat/info)

Vulnerabilities in third-party Applications that affect Facebook users data in the scope

reporting this issue Facebook replied this issue, not qualify as it not in their scope

Timeline

September 23, 2020: Submitted the report to Facebook.

September 23, 2020: Facebook closed it as N/A out of the scope

September 23, 2020:send more details

September 23, 2020:Facebook reply

After further discussion we determined we will need to investigate this further to determine the impact of this and how many users are impacted

September 24, 2020:Vulnerability has been fixed

October 9, 2020:Facebook rewarded me $500 as out of the scope

Bounty message

Asking Facebook why they made bounty decision like a low impact bug

It’s not a low issue but it’s not in our code . We usually don’t issue payouts However, we made an exception in this case and paid a small token amount since it was a serious issue in the partner’s code. Hope that makes sense
