---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-01-01_bypass-premium-account-payment-getpocket.md
original_filename: 2023-01-01_bypass-premium-account-payment-getpocket.md
title: Bypass Premium Account Payment (GetPocket)
category: documents
detected_topics:
- mobile-security
- oauth
- sso
- command-injection
tags:
- imported
- documents
- mobile-security
- oauth
- sso
- command-injection
language: en
raw_sha256: 5f23112ad9e12d38ad5a701e4936172ab2a22ca3cbff7eb30a79c335157774ae
text_sha256: 1c27917233906df95b042d4675a937340bd1936f5bae8bf166488dcc6a826695
ingested_at: '2026-06-28T07:32:16Z'
sensitivity: unknown
redactions_applied: false
---

# Bypass Premium Account Payment (GetPocket)

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-01-01_bypass-premium-account-payment-getpocket.md
- Source Type: markdown
- Detected Topics: mobile-security, oauth, sso, command-injection
- Ingested At: 2026-06-28T07:32:16Z
- Redactions Applied: False
- Raw SHA256: `5f23112ad9e12d38ad5a701e4936172ab2a22ca3cbff7eb30a79c335157774ae`
- Text SHA256: `1c27917233906df95b042d4675a937340bd1936f5bae8bf166488dcc6a826695`


## Content

---
title: "Bypass Premium Account Payment (GetPocket)"
url: "https://medium.com/@querylab/bypass-premium-account-payment-getpocket-d813b249687c"
authors: ["querylab"]
programs: ["Mozilla (GetPocket)"]
bugs: ["Payment bypass"]
publication_date: "2023-01-01"
added_date: "2023-01-06"
source: "pentester.land/writeups.json"
original_index: 1714
scraped_via: "browseros"
---

# Bypass Premium Account Payment (GetPocket)

Bypass Premium Account Payment (GetPocket)
querylab
Follow
3 min read
·
Jan 4, 2023

70

1

Greetings Guys! 🤙 Today I bring you a Bug I found at the Beginning of the Year 2022 You know GetPocket Web Application, a popular for Saving Online Content. It is for iOS, Android, and other mobile devices as well as desktop. This app allows you to save content from the web so that it can be read later. You can save articles, videos, notes and more to view at any time.

Press enter or click to view image in full size

I decided to browse the web and create my account, so I decide to use Mozilla Firefox OAuth authentication method to create my account for the first time on GetPocket.

Press enter or click to view image in full size
Press enter or click to view image in full size

Once I access my GetPocket account you will see that it is a normal Regular account with no privileges 😔.

I thought 🤔 How could I get a free premium account?

Then I remembered 💡 I had done some online shopping and had a Visa Gift Card 💳 No Funds and said why not use it to load GetPocket Premium account. I should give not accept it, as most of these web applications employ payment processing like Stripe, which uses a feature called https://stripe.com/radar radar that allows to detect this kind of abuse.

Press enter or click to view image in full size

So I opened my Burpsuit https://portswigger.net/ my Favorite Tool 🔨🔥 to hunt bugs. Once I got the Request I sent it to the Repeater and added the following line X-Forward-For: 127.0.0.1 and hit Send ️

Press enter or click to view image in full size
Press enter or click to view image in full size

Served Accepted the Request 🥳🎉200 OK

Get querylab’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Stripe Payment Processor bypass and gave me a purchase confirmation order to be reflected in email ********@gmail.com

Press enter or click to view image in full size
Press enter or click to view image in full size
Press enter or click to view image in full size

I could see how the user account is no longer the same, it has other functions, as it is now a premium account 🙃

Press enter or click to view image in full size
Press enter or click to view image in full size

Apparently, Stripe’s Radar feature is not Enabled, which allowed this abuse. Knowing all this, I proceeded to inform Mozilla Security Team to report the security flaw to them, and thoroughly investigate the issue and take the necessary steps to correct it. The Mozilla Security Team responded very quickly and were very nice.

The Bug, Turned Out to be a Duplicate.
