---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-09-30_how-i-found-bug-on-google-cloud.md
original_filename: 2021-09-30_how-i-found-bug-on-google-cloud.md
title: How I found bug on Google Cloud
category: documents
detected_topics:
- xss
- sqli
- command-injection
- otp
tags:
- imported
- documents
- xss
- sqli
- command-injection
- otp
language: en
raw_sha256: 919e2122ad34ec5691eac0993c6d0d466a674d7f9d4aa18697ddae03797235cc
text_sha256: 104f2e84a2905a747c887c6d0a23b2e9f8cea54dc6b4c2fbfeedc3ed8cc5037c
ingested_at: '2026-06-28T07:32:08Z'
sensitivity: unknown
redactions_applied: false
---

# How I found bug on Google Cloud

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-09-30_how-i-found-bug-on-google-cloud.md
- Source Type: markdown
- Detected Topics: xss, sqli, command-injection, otp
- Ingested At: 2026-06-28T07:32:08Z
- Redactions Applied: False
- Raw SHA256: `919e2122ad34ec5691eac0993c6d0d466a674d7f9d4aa18697ddae03797235cc`
- Text SHA256: `104f2e84a2905a747c887c6d0a23b2e9f8cea54dc6b4c2fbfeedc3ed8cc5037c`


## Content

---
title: "How I found bug on Google Cloud"
url: "https://medium.com/@anuragbhoir06/hello-everyone-this-is-anurag-bhoir-and-its-my-first-writeup-d8904d539ad2"
authors: ["Anuragbhoir11"]
programs: ["Google"]
bugs: ["OTP bypass"]
publication_date: "2021-09-30"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3274
scraped_via: "browseros"
---

# How I found bug on Google Cloud

How I found bug on Google Cloud
Anuragbhoir11
Follow
2 min read
·
Sep 30, 2021

47

3

Hello Everyone, This is Anurag Bhoir and its my first writeup.

Publishing this write-up regarding how I found low hanging fruit bug on google cloud.

Without wasting any time, lets start!

First let me give your common questions answer.

Q: What was the bug?

A : Phone verification OTP Bypass
_____________________
Q: Aquisition or Google domain?

A: Google Cloud
______________________

Q: How did you bypassed?

A: Response Manipulation using logic
______________________

Q: How to choose google domain?

A: There will be many suggestions but I have mentioned below, my experience based suggestions.

1. Acquisitions
2. Domain with lots of functionality

3. New google domains
4. Read writeups and choose those domains
______________________

Vulnerability Details:

I have chosen google cloud as target, tried to find xss, xxe, sqli, rce etc.

But no luck🙄

Then I thought lets focus on low hanging fruits, because developers mostly focus on critical and high severity issues and sometimes they forget to focus on low hanging fruits.

Then I started looking at signup and verification process.

I filled the form and then I noticed there is phone verification page and I decided to play with this page.

I entered my phone number and clicked on send otp, received otp on my phone but I entered wrong otp 000000 and captured request, and analysed response.

In response body I noticed

“status": “invalid code"

i changed to

Get Anuragbhoir11’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

“status": “Valid code"

And

“status": “Success"

And forwarded the request but no change on page.

Then i decided to check another method,

Again I entered my valid number and clicked on send otp this time I entered correct otp to analyse and copy response.
I noticed in response body there were 3 data present

“status": “Success"

“session data": “abcdefghijklmn"

“eti”:”qwertyuiop ”

I decided to replace this whole valid response with invalid response
I did the same but no change in page.

Now I noticed “eti":”qwerttuiop"

Value is different for different mobile numbers
I understood the logic behind verification now.

Again I started entering mobile number and clicked on send otp.

Now i entered wrong otp 000000 and captured request

I replaced only below two values :

“Status":”success"

“session data":”abcdefghijklm"

And kept “eti":”hfkscisnii" value as it is
And yes phone verification page is bypassed

I immediately reported this issue, got response from google

“Nice Catch🎉”

They changed severity to

P4→P2

S4→S2

And I got listed on google’s honorable mentions security researchers wall. 😊

Linkedin- https://www.linkedin.com/in/anurag-bhoir-b1687615a
