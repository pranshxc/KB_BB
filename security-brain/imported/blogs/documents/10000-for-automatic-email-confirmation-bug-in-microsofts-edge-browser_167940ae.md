---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-01-23_10000-for-automatic-email-confirmation-bug-in-microsofts-edge-browser.md
original_filename: 2021-01-23_10000-for-automatic-email-confirmation-bug-in-microsofts-edge-browser.md
title: $10,000 for automatic email confirmation bug in Microsoft’s Edge browser
category: documents
detected_topics:
- ssrf
- command-injection
- password-reset
- business-logic
tags:
- imported
- documents
- ssrf
- command-injection
- password-reset
- business-logic
language: en
raw_sha256: 167940ae65b033137415e1e8ac407bf6964b71977442ccc73cd4d832e9ef3d60
text_sha256: 8170be2cd60df10f0e949c721df422d8a100dc8be7c6a3d6faba1bb038bbf9e4
ingested_at: '2026-06-28T07:32:04Z'
sensitivity: unknown
redactions_applied: false
---

# $10,000 for automatic email confirmation bug in Microsoft’s Edge browser

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-01-23_10000-for-automatic-email-confirmation-bug-in-microsofts-edge-browser.md
- Source Type: markdown
- Detected Topics: ssrf, command-injection, password-reset, business-logic
- Ingested At: 2026-06-28T07:32:04Z
- Redactions Applied: False
- Raw SHA256: `167940ae65b033137415e1e8ac407bf6964b71977442ccc73cd4d832e9ef3d60`
- Text SHA256: `8170be2cd60df10f0e949c721df422d8a100dc8be7c6a3d6faba1bb038bbf9e4`


## Content

---
title: "$10,000 for automatic email confirmation bug in Microsoft’s Edge browser"
url: "https://kingkaran977.medium.com/10-000-for-automatic-email-confirmation-bug-in-microsofts-edge-browser-22f15ceccb4a"
authors: ["Karan Chaudhary (@0xKaran)"]
programs: ["Microsoft"]
bugs: ["Logic flaw"]
bounty: "10,000"
publication_date: "2021-01-23"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3973
scraped_via: "browseros"
---

# $10,000 for automatic email confirmation bug in Microsoft’s Edge browser

$10,000 for automatic email confirmation bug in Microsoft’s Edge browser
Karan Chaudhary
Follow
4 min read
·
Jan 22, 2021

1K

3

Hey folks, welcome to my first bug bounty writeup, which I found on Microsoft Edge (Chromium) browser.

During quarantine, I saw this facebook post:

Press enter or click to view image in full size

This post was enough to boost my motivation, So I learnt alot about web security. And on 1st december I decided to actually go and hunt on real programs

It took me whole first day to select the program on hackerone and some basic recon, and finally I decided to hack “Lark Technologies”

On 2nd of december 2020, I Spent around 5–6 countinuous hours hunting for bug but got nothing.

I mostly hunt on Firefox browser but that day I decided to test the application on multiple browsers. Opened the website on Edge browser and commenced the testing of Login/Signup functionality.

Entered my testing email on registration.

Press enter or click to view image in full size

Opened my mailbox where I got the e-mail confirmation link.

But before clicking on confirm email button, I copied the link to see if I can get any juicy info.

But as I copied the link, I saw my target website took me to the next page where you go if you verify your e-mail, but… wait… 🤔 I didn’t verified my email, I only copied link in my clipboard.

I considered this as a bug on my target program.

To verify the issue, I repeated the same step with different email on different browsers (Firefox & Chrome), entered my e-mail > recieved email confirmation link > copied the link, but nothing happened on target website, I was still on the same page. Next I pasted the link on the Edge browser’s search bar (without hitting enter or visiting the link), Again I see my email got verified 🤥.

I was confused how is this happening? 🤔

I changed my target to Facebook, Spotify etc., repeated the same step registered > recieved email confirmation link > copied the link but those accounts didn’t verify. pasted the link on Edge browser search bar but again accounts didn’t verify

At this point I thought this automatic email verification bug is on my target website, but also curious about knowing how is this happening.

Get Karan Chaudhary’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

To remove curtain from this doubt I fired up my Burp Suite and generated a burp collaborator payload, pasted the payload on browser search bar and suddenly recieved a DNS query coming form 125.20.208.158 IP address. Did a reverse IP lookup and found out this IP belongs to microsoft.

Press enter or click to view image in full size

At this point of time I concluded this as, whenever a link is either copied from Edge browser or pasted on search bar (even copied from other location), Edge browser makes a DNS lookup request. And when my target sees this request it thinks that the user clicked and made a HTTP request, hence email gets verified.

I reported this vulnerability to the program on hackerone and they replied me, “we can’t consider this as a bug and closed the report as N/A”

Press enter or click to view image in full size

After getting disappointed from this reply I thought why not submit same report to microsoft because as mentioned in their valid report rules, If attack is possible on Microsoft Edge (chromium) but not on Google chrome browser, the report will be considered as valid.

So I did 😁 but without any expectation 😪

On 4 am morning on 6th of Jan 2020 I recieved an email from microsoft saying that this report is eligible for a $10,000 bounty award, I was shocked and not believing that my report got triaged and got my first bounty in life (huge 😍)

Press enter or click to view image in full size

After few months of diving deep into Bug Hunting I realised it was a SSRF bug.

Timestamp

2 dec 2020 : reported bug to Lark Technology & Microsoft

2 dec 2020 : report rejected from Lark Technology

3 dec 2020 : microsoft opened my report

23 dec 2020 : microsoft confirmed the issue

6 jan 2021 : microsoft awarded $10,000 as bounty award

14 jan 2021 : vuln patched and new update released

Thankyou everyone for reading this writeup ❤️🙏
