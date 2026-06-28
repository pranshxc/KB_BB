---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-06-30_testing-cookies-worth-500.md
original_filename: 2021-06-30_testing-cookies-worth-500.md
title: Testing Cookies worth $500
category: documents
detected_topics:
- otp
- sso
- jwt
- idor
- command-injection
- password-reset
tags:
- imported
- documents
- otp
- sso
- jwt
- idor
- command-injection
- password-reset
language: en
raw_sha256: 2cf04c7c3f4ce4a4e7ceb87c050c58ccd5aa95ab4107474b5bf1ed1ad1e86586
text_sha256: e6b5241005b1d10808fc509057ba658057eb07592a71bda1f5ec53eeff56abe6
ingested_at: '2026-06-28T07:32:06Z'
sensitivity: unknown
redactions_applied: false
---

# Testing Cookies worth $500

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-06-30_testing-cookies-worth-500.md
- Source Type: markdown
- Detected Topics: otp, sso, jwt, idor, command-injection, password-reset
- Ingested At: 2026-06-28T07:32:06Z
- Redactions Applied: False
- Raw SHA256: `2cf04c7c3f4ce4a4e7ceb87c050c58ccd5aa95ab4107474b5bf1ed1ad1e86586`
- Text SHA256: `e6b5241005b1d10808fc509057ba658057eb07592a71bda1f5ec53eeff56abe6`


## Content

---
title: "Testing Cookies worth $500"
url: "https://sankalpa02.medium.com/testing-cookies-worth-500-8fc2310e6d7e"
authors: ["Sankalpa Acharya (@sankalpa_02)"]
bugs: ["Account takeover", "IDOR"]
bounty: "500"
publication_date: "2021-06-30"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3531
scraped_via: "browseros"
---

# Testing Cookies worth $500

Sankalpa Acharya
 highlighted

Sankalpa Acharya
 highlighted

Testing Cookies worth $500
Sankalpa Acharya
Follow
3 min read
·
Jun 30, 2021

561

5

Hey everyone, I’m Sankalpa Acharya from Nepal. A few weeks ago, I discovered an IDOR vulnerability that was worth $500 to me. So, let’s kick off my journey with this first bounty!

Impact of Vulnerability: Account Takeover

Press enter or click to view image in full size

Before diving straight into the report, I have a tip for those who are struggling to get their first bounty. If you’re finding bugs on targets available in HackerOne and Bugcrowd, consider switching your target. Use Google dorks (inurl: /responsible-disclosure/ bounty) to discover some bug bounty programs because there is less competition, and as a beginner, that’s what you want.

Let’s Begin,

I have a bad habit of continuously changing targets without even proper recon. While searching for reports about SSO login vulnerabilities, I came across a website in my search results: ‘sso.example.io’ (can’t disclose the website name). This time, I had a strong gut feeling that I might find a vulnerability in this target.

New beginning, New Target with some positive energy

I created two accounts there, at first I tested CSRF vulnerability but no luck :(

Then I went to test password reset functionality hopping any OTP code or token might get leaked in Referer header or in Response again no luck :(

Get Sankalpa Acharya’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Again:

With a slight trace of sadness on my face, I decided to observe the login flow of the website. I was hoping to discover JWT misconfiguration if the website used JWT tokens to identify users. I intercepted the request after entering my ID and password and clicked the ‘Login’ button, but there wasn’t much in the request. When I intercepted the response, I found that there was no JWT token or any other code in the response body. :(

Press enter or click to view image in full size
Wait a Minute

What identifies the user to the browser? Cookies, right? So, I began testing the cookies.

Press enter or click to view image in full size
Response From Server

So, I replaced every cookie header one by one with those from my other account. There was a “Set-Cookie” header: example_token=token, which was identifying the user. I decided to delve deeper into this header. Within it, there were some random tokens separated like this → 1|random_string_and_integer|4-digit code|4-digit code|random_string_and_integer|. One thing that caught my eye was that 4-digit code because it was repeated in the header, and there was only one letter different from my second account.

Press enter or click to view image in full size
Cookies

As you can see in the token header, a 5-digit code (47402) was being repeated, and my second account had the code 47403. So, I replaced that 5-digit code with my second account’s code, and… Boooooooom!!!! My second account was logged in. To be doubly sure, I replaced that code (47402) with 47401, and then I was logged into another user’s account from China. Yessssssssssss, I did it!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! Then, I reported the vulnerability.

Press enter or click to view image in full size

After few days I got response to my report

Press enter or click to view image in full size

Hope You Enjoyed it,

Follow me on twitter for more cybersecurity and Development Content. sankalpa_02
