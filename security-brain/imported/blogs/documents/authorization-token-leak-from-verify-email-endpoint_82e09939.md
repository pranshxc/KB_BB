---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-07-16_authorization-token-leak-from-verify-email-endpoint.md
original_filename: 2022-07-16_authorization-token-leak-from-verify-email-endpoint.md
title: Authorization token leak from verify email endpoint
category: documents
detected_topics:
- access-control
- command-injection
- password-reset
- otp
- information-disclosure
tags:
- imported
- documents
- access-control
- command-injection
- password-reset
- otp
- information-disclosure
language: en
raw_sha256: 82e099395ab761fae8564e18f0216585ef642fcacff86ac975967a923220e726
text_sha256: 12b54ff60dd7d20840cef5afe35781febaca3610e8c6cbe8dac238af458c6d49
ingested_at: '2026-06-28T07:32:12Z'
sensitivity: unknown
redactions_applied: false
---

# Authorization token leak from verify email endpoint

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-07-16_authorization-token-leak-from-verify-email-endpoint.md
- Source Type: markdown
- Detected Topics: access-control, command-injection, password-reset, otp, information-disclosure
- Ingested At: 2026-06-28T07:32:12Z
- Redactions Applied: False
- Raw SHA256: `82e099395ab761fae8564e18f0216585ef642fcacff86ac975967a923220e726`
- Text SHA256: `12b54ff60dd7d20840cef5afe35781febaca3610e8c6cbe8dac238af458c6d49`


## Content

---
title: "Authorization token leak from verify email endpoint"
url: "https://vengeance.medium.com/authorization-token-leak-from-verifying-email-endpoint-f28803476680"
authors: ["Vengeance"]
bugs: ["Account takeover", "Information disclosure"]
publication_date: "2022-07-16"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 2445
scraped_via: "browseros"
---

# Authorization token leak from verify email endpoint

Authorization token leak from verify email endpoint
Vengeance
Follow
3 min read
·
Jul 16, 2022

113

While testing a website I found that the verify email endpoint was leaking the authorization tokens of any verified users by just passing their email as an input.

As I can not disclose the website name let's say the website is example.com

As the program had one domain in its scope. I opened the burp suite in the background to collect all the requests and responses so I could review them later. First I used the website like an average user to understand its functionality and flow of the website.

Then I proceeded to register a new user for the application. The email verification was done using a POST request with “email” and “code” as a parameter.

Request:

POST /api/user/verifymail HTTP/1.1
Host: www.example.com
…
…

{
“email”:”test@test.com”
“code”:”51754516ec7a4be928213796bda74fec”
}

In response, email verification was successful and the token was displayed along with other information.

After noticing the email parameter in the request, I thought of registering two new users using different emails and test if the code assigned for the first user’s email can be used to verify the second user. But the test failed. Then I tested by removing the code parameter from the request and just forwarded the request with the email only. The application did not verify the email. So with no luck, I just went on to test the other functionalities of the application.

Get Vengeance’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

After some testing, I was closing the tabs in the repeater on the burp suite. Then I saw /api/user/verifymail endpoint with just email as a parameter. I clicked on send and to my surprise, the response was 200 OK with the email verified successful message along with the token and other information. As I had already verified this email before, it showed the email verified successful again without displaying any error message like email already verified or verification failed.

Press enter or click to view image in full size

I got curious and started testing the endpoint further. I found that if an already verified email is passed as a value in the email parameter, the application responded with the token. Using the token obtained, any action can be performed on behalf of the victim.

Then I tried with the admin account of the application which I found during the testing process. The admin token was leaked in the response.

Press enter or click to view image in full size

Then I created a POC and reported the vulnerability.

Using this vulnerability an attacker could obtain tokens of any verified users by just using the email address of the victim.

Thanks for reading.

Twitter: Vengeance0x0
