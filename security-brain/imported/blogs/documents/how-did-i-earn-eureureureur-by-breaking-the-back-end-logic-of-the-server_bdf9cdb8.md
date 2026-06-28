---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-04-28_how-did-i-earn-by-breaking-the-back-end-logic-of-the-server.md
original_filename: 2021-04-28_how-did-i-earn-by-breaking-the-back-end-logic-of-the-server.md
title: How did I earn €€€€ by breaking the back-end logic of the server
category: documents
detected_topics:
- command-injection
- information-disclosure
- business-logic
- api-security
tags:
- imported
- documents
- command-injection
- information-disclosure
- business-logic
- api-security
language: en
raw_sha256: bdf9cdb8a7434d9ddc266d30b893e3577adda49d19b6a6d519e3aa10ab059b62
text_sha256: e2d566c8d18812cf8cf69382e19f5ba2f777ddbb4866bca5cdf7845e9a77af0d
ingested_at: '2026-06-28T07:32:05Z'
sensitivity: unknown
redactions_applied: false
---

# How did I earn €€€€ by breaking the back-end logic of the server

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-04-28_how-did-i-earn-by-breaking-the-back-end-logic-of-the-server.md
- Source Type: markdown
- Detected Topics: command-injection, information-disclosure, business-logic, api-security
- Ingested At: 2026-06-28T07:32:05Z
- Redactions Applied: False
- Raw SHA256: `bdf9cdb8a7434d9ddc266d30b893e3577adda49d19b6a6d519e3aa10ab059b62`
- Text SHA256: `e2d566c8d18812cf8cf69382e19f5ba2f777ddbb4866bca5cdf7845e9a77af0d`


## Content

---
title: "How did I earn €€€€ by breaking the back-end logic of the server"
url: "https://dewcode.medium.com/how-did-i-earn-by-breaking-the-back-end-logic-of-the-server-fd94882cbdf6"
authors: ["Dewanand Vishal (@dewcode91)"]
bugs: ["Logic flaw", "Information disclosure"]
publication_date: "2021-04-28"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3698
scraped_via: "browseros"
---

# How did I earn €€€€ by breaking the back-end logic of the server

Top highlight

How did I earn €€€€ by breaking the back-end logic of the server
Dewanand Vishal
Follow
3 min read
·
Apr 28, 2021

490

3

Hello bug hunters! I am back with another blog. I found these cool bugs in one of the private programs at intigriti. So will not disclose the program name, I will use example.com instead of the original domain name.

Press enter or click to view image in full size
Issue 1: Bypassing input validation via `null` value

The target program is a self-developed customer portal from Hotels High. Customer can book their visits. This program targets the staging environment where data can safely be created and modified. Normally customers are provided with a customer registration code with which they can make a booking.

Get Dewanand Vishal’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

While testing the application. I noticed in the registration workflow, it is not possible to create a booking without phoneNumber/email and other required parameters. I observed a suspicious behavior at an endpoint that allows a user to create a booking with null values.

{
  "registerCode": "CS1337", 
  "gender": "male",
  "booking_date": "2021-10-03", 
  "email": null,
  "firstName": "first_name",
  "lastName": "Last_name",
  "gdprConfirmed": null, 
  "phoneNumber": null,
  "booking_time": "14:50" 
}

If a user looks for path API/v1/rest/customer/booking/create/ in proxy history, send a request to the repeater and replace email, gdprConfirmed, phoneNumber parameter with null value then he can able to bypass back-end validation and create bookings.

Press enter or click to view image in full size
http_request

After validation, I submitted this issue to the intigriti team, They confirmed this is a valid security issue, 2 days later they accepted my report and awarded me a €€€ bounty.

Issue 2: Information disclosure via an empty array [ ]

While testing the application as a low privilege user. I have found an endpoint that allows us to access the bookings data. I noticed this endpointevent/api/v1/bookings?page=0&perpage=25&pagesize=25&sort=%2BbookingDate&sortby=bookingDate&ascending=true&bookingdatefrom=<DATE>&visitdatefrom=<DATE>.
When a user makes a GET request to the above endpoint, he will get a null response.

Press enter or click to view image in full size

But if a user makes a GET request and appends an empty array []at bookingdatefrom parameter then he can able to access the booking data.

Press enter or click to view image in full size

I immediately submit this issue to the intigriti team, They confirmed this is a valid security issue, accepted my report, and awarded me a €€€ bounty.

If you have any query regarding the issue then feel free to dm me @dewcode91
happy hunting!

References:
https://owasp.org/www-community/attacks/Full_Path_Disclosure
