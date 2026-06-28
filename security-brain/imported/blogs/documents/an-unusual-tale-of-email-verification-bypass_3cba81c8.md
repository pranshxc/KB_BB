---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-08-13_an-unusual-tale-of-email-verification-bypass.md
original_filename: 2022-08-13_an-unusual-tale-of-email-verification-bypass.md
title: An Unusual Tale of Email Verification Bypass
category: documents
detected_topics:
- rate-limit
- command-injection
- password-reset
- otp
tags:
- imported
- documents
- rate-limit
- command-injection
- password-reset
- otp
language: en
raw_sha256: 3cba81c8fbcf0d951b88d347665b4f5b5268f6a5be417e9d8745fdb9447165cb
text_sha256: 7736f5c008dd3257b8caa333e9434d81007a1b41b1d7613d4cf7e99d47a1fd82
ingested_at: '2026-06-28T07:32:13Z'
sensitivity: unknown
redactions_applied: false
---

# An Unusual Tale of Email Verification Bypass

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-08-13_an-unusual-tale-of-email-verification-bypass.md
- Source Type: markdown
- Detected Topics: rate-limit, command-injection, password-reset, otp
- Ingested At: 2026-06-28T07:32:13Z
- Redactions Applied: False
- Raw SHA256: `3cba81c8fbcf0d951b88d347665b4f5b5268f6a5be417e9d8745fdb9447165cb`
- Text SHA256: `7736f5c008dd3257b8caa333e9434d81007a1b41b1d7613d4cf7e99d47a1fd82`


## Content

---
title: "An Unusual Tale of Email Verification Bypass"
url: "https://sagarsajeev.medium.com/an-unusual-tale-of-email-verification-bypass-dcf884d544eb"
authors: ["Sagar Sajeev (@Sagar__Sajeev)"]
bugs: ["Email verification bypass", "Bruteforce", "Rate limiting bypass"]
publication_date: "2022-08-13"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 2320
scraped_via: "browseros"
---

# An Unusual Tale of Email Verification Bypass

An Unusual Tale of Email Verification Bypass
Sagar Sajeev
Follow
3 min read
·
Aug 13, 2022

507

3

Hey Guys. I’m Sagar Sajeev .

In this small writeup I would like to share how I reported a case of Email Verification Bypass. But what makes it unique is the way in which it has to be exploited.

Press enter or click to view image in full size

Let the domain be :-

“https://www.redacted.com/account/login”

Login into the account as attacker@email.com
Go to change email option and change the mail from attacker@email.com to victim@email.com
4 digit OTP is sent to victim@email.com to confirm(verify) the change.
No rate limit was set. Thus, correct OTP was found via bruteforcing.
But upon filing the Correct OTP, the page showed incorrect OTP.

I was like….

I couldn't understand why the correct OTP was rejected by the website.
I inspected every request manually (the OTP bruteforce requests in repeater) and it was only after 2 hrs of trial and error, I came across a hidden parameter called “sec” embedded between the request.
It was quite a peculiar parameter as it appeared only after the 120th request in the repeater. I verified it thrice and it was indeed appearing only after the 120th request.
Also it was incrementing by a step value of 1 after the 120th request. i.e;

>120th request has sec value 1

>121st request has sec value 2

>122nd request has sec value 3

Get Sagar Sajeev’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

>123rd request has sec value 4

> etc

I also noticed that every attempt after the 120th request led to a 302 redirect to a different subdomain.
I’m not sure whether I’m right, but I feel like it’s a way the target has chose either to reduce traffic on the website or as something to prevent bruteforce attacks.
The Fun Part!
The param was heavily dependent on client side, So just remove the sec param from the 120th request. This removes the parameter from every subsequent request.
Now again try the above mentioned OTP bruteforcing and get the correct OTP and type it in.
Email has been changed from attacker@email.com to victim@email.com.
Press enter or click to view image in full size
I know this is rather a common bug. But the verification process of the website was rather unique and thus I wanted to make a writeup on it.
I had reported this a while back, but didn’t get a reply from the Sec team. It was in fact last week that I got a reply from them and by then even I had forgot about this finding.
Impact — This issue can be used to bypass email verification. Attackers can create account on behalf on any person without having access to that email account.

Timeline

Submitted : 02–07–2022

Accepted : 03–08–2022

Rewarded with Swag : 09–08–2022

I do occasionally share some tips about Bug Bounties and related stuff over at my Twitter and LinkedIn handle. So do follow me there. If you’ve got any queries, feel free to message me. I will be more than happy to help.

LinkedIn : https://www.linkedin.com/in/sagar-sajeev-663491208/

Twitter : https://twitter.com/Sagar__Sajeev

Thanks for going through my writeup and I hope it was useful to you. I’ve made 6 other writeups on my Medium handle. Please do check those out as well.

Happy Hunting!
