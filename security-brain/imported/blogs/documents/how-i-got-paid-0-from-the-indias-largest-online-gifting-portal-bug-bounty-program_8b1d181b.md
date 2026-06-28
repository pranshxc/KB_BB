---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2018-05-05_how-i-got-paid-0-from-the-indias-largest-online-gifting-portal-bug-bounty-progra.md
original_filename: 2018-05-05_how-i-got-paid-0-from-the-indias-largest-online-gifting-portal-bug-bounty-progra.md
title: How I Got Paid $0 From the India’s largest online gifting portal — Bug Bounty
  Program
category: documents
detected_topics:
- mobile-security
- xss
- command-injection
- business-logic
tags:
- imported
- documents
- mobile-security
- xss
- command-injection
- business-logic
language: en
raw_sha256: 8b1d181b66a59aec9dd6c2f618cec386998de8c3be5e1d9c829bf6ab393cc8f1
text_sha256: fb66a23a1f638c2b9cedac4062423070ffe31016aa3fd0a0eb44c1be73d1b92c
ingested_at: '2026-06-28T07:31:57Z'
sensitivity: unknown
redactions_applied: false
---

# How I Got Paid $0 From the India’s largest online gifting portal — Bug Bounty Program

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2018-05-05_how-i-got-paid-0-from-the-indias-largest-online-gifting-portal-bug-bounty-progra.md
- Source Type: markdown
- Detected Topics: mobile-security, xss, command-injection, business-logic
- Ingested At: 2026-06-28T07:31:57Z
- Redactions Applied: False
- Raw SHA256: `8b1d181b66a59aec9dd6c2f618cec386998de8c3be5e1d9c829bf6ab393cc8f1`
- Text SHA256: `fb66a23a1f638c2b9cedac4062423070ffe31016aa3fd0a0eb44c1be73d1b92c`


## Content

---
title: "How I Got Paid $0 From the India’s largest online gifting portal — Bug Bounty Program"
url: "https://medium.com/bugbountywriteup/how-i-got-paid-0-from-the-indias-largest-online-gifting-portal-bug-bounty-program-fd9e14f9ca20"
authors: ["Hariom Vashisth"]
bugs: ["Payment tampering", "Parameter tampering"]
publication_date: "2018-05-05"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5888
scraped_via: "browseros"
---

# How I Got Paid $0 From the India’s largest online gifting portal — Bug Bounty Program

How I Got Paid $0 From the India’s largest online gifting portal — Bug Bounty Program
Hariom Vashisth
Follow
3 min read
·
May 5, 2018

108

2

“The greatest gift you can give yourself is a little bit of your own attention.” ~Anthony J. D’Angelo

Hey everyone!

It all started with this awesome quote and I began exploring about gifts, As usual, After 10–15 minutes I lost my vision and landed on a gift shopping website and started browsing like a small kid ..umm, I want this , I want that, ohh! I want all. But while going through, I unintentionally opened my console and begin searching for XHR calls and source code, recalling my good old days when I used to learn bootstrap and css. I am opening and analysing everything like a child and trying to understand the web app-flow and my mind is connecting every single dot for making a complete API flow or I can say one product purchase flow. I am noting everything on notepad++ and wow, I see something weird. I am doubtful about the secure checkout method. Curiosity to know this leads me to perform MITM (Man In The Middle) test. oh, I forgot to tell you that I am shopping with the mobile app (android app) although I used my laptop to pass traffic from my penetration testing tool. I got the plain-text product_amount which caught in uncertainty.

Press enter or click to view image in full size

I’m not sure about the impact of changing this. So, I decided to give it a try because I must know the reason. I changed it and forward my request to the server. My request is successfully processed without any validation. well, I thought they put validation layer after payment (on those success and failure web-hook which every programmer configured in payment module). I paid 1Rs. and the original price before changing was 725 (as you can see in the screenshot) and finally, I found a serious vulnerability ~ price manipulation

Press enter or click to view image in full size

Website of this vulnerable mobile application is free from this vulnerability.

Get Hariom Vashisth’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

This is a short explanation of how I got lucky!

As you can see most people are doing basic recon on the target looking for reflected XSS, open redirect or exposed directories. You need to be extremely lucky to find that sort of low hanging fruit but it doesn’t hurt to try.

As far as this finding goes, I submitted my report and waiting for reply!

Timeline:

April 15, 2018: Report Submitted and triaged
