---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-03-18_bypass-confirmation-to-add-payment-method.md
original_filename: 2022-03-18_bypass-confirmation-to-add-payment-method.md
title: Bypass confirmation to add payment method.
category: documents
detected_topics:
- access-control
- command-injection
- password-reset
- otp
- business-logic
tags:
- imported
- documents
- access-control
- command-injection
- password-reset
- otp
- business-logic
language: en
raw_sha256: 797154b12386241a11fb9faeb02dc3430f166f0f6026e107d4523cbe87fc2828
text_sha256: a39f6739bd8b6b4405855e7314fc0f93a70ba2e59e1a709fc74d0ce6e47e394c
ingested_at: '2026-06-28T07:32:10Z'
sensitivity: unknown
redactions_applied: false
---

# Bypass confirmation to add payment method.

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-03-18_bypass-confirmation-to-add-payment-method.md
- Source Type: markdown
- Detected Topics: access-control, command-injection, password-reset, otp, business-logic
- Ingested At: 2026-06-28T07:32:10Z
- Redactions Applied: False
- Raw SHA256: `797154b12386241a11fb9faeb02dc3430f166f0f6026e107d4523cbe87fc2828`
- Text SHA256: `a39f6739bd8b6b4405855e7314fc0f93a70ba2e59e1a709fc74d0ce6e47e394c`


## Content

---
title: "Bypass confirmation to add payment method."
url: "https://yajdesu.medium.com/bypass-confirmation-to-add-payment-method-df2772a36561"
authors: ["Yaj Desu"]
bugs: ["Email verification bypass", "Logic flaw"]
publication_date: "2022-03-18"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 2805
scraped_via: "browseros"
---

# Bypass confirmation to add payment method.

Yaj Desu
Follow
1 min read
·
Mar 18, 2022

3

Bypass confirmation to add payment method.
Summary:

This website requires confirmation from the email to successfully attach the payment method that you wanted to connect to the store. The problem occurs when you see the response after adding the payment method or PayPal email address.

Step to Reproduce

Go to add payment feature. Enter the PayPal address and intercept the request to see the response. After analyzing the whole process. I notice that the authorization or the verification token is visible in the response.

Press enter or click to view image in full size
response of the API

I notice when I verify my account through email, the request went to the specific endpoint with the eventId header on it.

Press enter or click to view image in full size

I try the eventId in the response and It verify the email without opening the e-mail of the victim.

Timeline

Reported: 3rd Feb, 2022

Get Yaj Desu’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Triage: 7th Feb, 2022

Bounty Awarded: 15th Feb, 2022 $XXX

Resolved: 24th Feb, 2022

Takeaway

Always analyze the response to know information about the application. Maybe it leaks the verification_token.
