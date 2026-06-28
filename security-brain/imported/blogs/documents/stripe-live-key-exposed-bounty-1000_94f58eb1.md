---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-12-09_stripe-live-key-exposed-bounty-1000.md
original_filename: 2022-12-09_stripe-live-key-exposed-bounty-1000.md
title: 'STRIPE Live Key Exposed:: Bounty: $1000'
category: documents
detected_topics:
- oauth
- command-injection
- otp
- information-disclosure
tags:
- imported
- documents
- oauth
- command-injection
- otp
- information-disclosure
language: en
raw_sha256: 94f58eb1f6b167cdb4d26414907cf61b64e554df84bfcd1fcb4262606f32d57d
text_sha256: ba28714e9e0739eda700debb665941cadc3829f3726886c4ff2cc8f9ce61900d
ingested_at: '2026-06-28T07:32:16Z'
sensitivity: unknown
redactions_applied: false
---

# STRIPE Live Key Exposed:: Bounty: $1000

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-12-09_stripe-live-key-exposed-bounty-1000.md
- Source Type: markdown
- Detected Topics: oauth, command-injection, otp, information-disclosure
- Ingested At: 2026-06-28T07:32:16Z
- Redactions Applied: False
- Raw SHA256: `94f58eb1f6b167cdb4d26414907cf61b64e554df84bfcd1fcb4262606f32d57d`
- Text SHA256: `ba28714e9e0739eda700debb665941cadc3829f3726886c4ff2cc8f9ce61900d`


## Content

---
title: "STRIPE Live Key Exposed:: Bounty: $1000"
url: "https://infosecwriteups.com/stripe-live-key-exposed-bounty-1000-dc670f2c5d9c"
authors: ["Vipul Sahu"]
bugs: ["Information disclosure"]
bounty: "1,000"
publication_date: "2022-12-09"
added_date: "2022-12-09"
source: "pentester.land/writeups.json"
original_index: 1801
scraped_via: "browseros"
---

# STRIPE Live Key Exposed:: Bounty: $1000

STRIPE Live Key Exposed:: Bounty: $1000
Vipul Sahu
Follow
2 min read
·
Dec 9, 2022

193

Hey Hunters,

I have found a sensitive stripe live token leaking on a private program.[let’s say redacted.com]

Initial Foothold

I collected all the subdomains using tools like Subfinder and Amass. After that, I filtered the live subdomains using httprobe. Found a subdomain admin.redacted.com which redirects the user/admin to google OAuth.

Your browser can execute JavaScript, which can, in turn, change the document; in this case, it redirects to google OAuth. After this, I used curl for admin.redacted.com to get the plain original output and nothing else.

Press enter or click to view image in full size
Leaking stripe live token

Now I have a leaking stripe live token, but the token’s validity needs to be checked.

Exploiting Stripe Tokens

After checking the Keyhacks and the Stripe API Documentation. I was able to get a bunch of information, including:

Get Vipul Sahu’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Balance: It retrieves the current balance in the Stripe account.

curl https://api.stripe.com/v1/balance -u sk_live_<Secret-Key>:

Press enter or click to view image in full size
Balance in the Stripe Account

Customers: It retrieves the customer’s data and tracks payments. Including the Customer’s Name, Email, IP used, and many more.

curl https://api.stripe.com/v1/customers -u sk_live_<Secret-Key>:

Press enter or click to view image in full size
Multiple customer’s data and upcoming payments

Charges: It retrieves charges and card information. One such card details are also attached below. Stripe only gives you the last four digits.

curl https://api.stripe.com/v1/charges -u sk_live_<Secret-Key>:

Card Details

Files: Retrieves Files that the admin uploads. Files generally have invoices, disputes, events, balances, bank accounts, tokens, charges, and more.

curl https://api.stripe.com/v1/files -u sk_live_<Secret-Key>:

Press enter or click to view image in full size
Files retrieved
Impact and Timeline

Companies and other end users Sensitive Information Disclosure.

Reported — 21st August

Rewarded and Fixed — 30th August

Let's connect: https://www.linkedin.com/in/vipul-sahu-a7a420174/

From Infosec Writeups: A lot is coming up in the Infosec every day that it’s hard to keep up with. Join our weekly newsletter to get all the latest Infosec trends in the form of 5 articles, 4 Threads, 3 videos, 2 GitHub Repos and tools, and 1 job alert for FREE!
