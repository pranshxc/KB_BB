---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-01-01_a-tale-of-zero-click-account-takeover.md
original_filename: 2022-01-01_a-tale-of-zero-click-account-takeover.md
title: A tale of zero click account takeover
category: documents
detected_topics:
- access-control
- idor
- command-injection
- password-reset
- otp
- api-security
tags:
- imported
- documents
- access-control
- idor
- command-injection
- password-reset
- otp
- api-security
language: en
raw_sha256: cc4de65e87859f98fd199efe79352f11d2559695d3beab5de340775191508fec
text_sha256: 3bedd8d76ad44fbe9fda9f1af1f32ac8336c103556c3b4682b1ca207d1c27aa7
ingested_at: '2026-06-28T07:32:09Z'
sensitivity: unknown
redactions_applied: false
---

# A tale of zero click account takeover

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-01-01_a-tale-of-zero-click-account-takeover.md
- Source Type: markdown
- Detected Topics: access-control, idor, command-injection, password-reset, otp, api-security
- Ingested At: 2026-06-28T07:32:09Z
- Redactions Applied: False
- Raw SHA256: `cc4de65e87859f98fd199efe79352f11d2559695d3beab5de340775191508fec`
- Text SHA256: `3bedd8d76ad44fbe9fda9f1af1f32ac8336c103556c3b4682b1ca207d1c27aa7`


## Content

---
title: "A tale of zero click account takeover"
url: "https://medium.com/pentesternepal/a-tale-of-zero-click-account-takeover-56b51fdbd7ae"
authors: ["Veshraj Ghimire (@GhimireVeshraj)"]
bugs: ["Account takeover", "IDOR"]
publication_date: "2022-01-01"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3040
scraped_via: "browseros"
---

# A tale of zero click account takeover

A tale of zero click account takeover
Veshraj Ghimire
Follow
4 min read
·
Jan 1, 2022

288

2

Hello there!
I hope everything is going well with you; today I’m back with the story of my first critical discovery on Hackerone, which is also my 1st $$$$ bounty.

Initial Recon:
As usual, I began with subdomain discovery and began probing it. I was more interested in this target because the scope was a wildcard: *.target.com. I didn’t come across any unusual or interesting subdomains during my subdomain scanning.
That is why I started looking for main domain. After few days of messing around with features in main domain, I came over a broken access control to view Personal information of any user, Anyone could view personal information including emailID, Address, PhoneNumber, Date of Birth and many more by passing a unique userID to following endpoint:
/api/Customer/GetAdditional?customerId=

So, I reported the vulnerability quickly. As aspected, triager was asking info about how do i get that unique id to disclose PII of other user. I tried looking every features and everything i could do, but was unable to get any other user’s unique id.

Press enter or click to view image in full size

After few days, it was closed as informative as i was unable to find those unique userID.

The Game Changer:
I didn’t gave-up, I was still looking for things on the same site. One day, while I was browsing the site by proxifying it with Burp, I came over a javascript file which was discovered by BurpJSLinkFinder which you can get from BApp Store. I beautified it and saved the code locally then started looking after it. After spending few hours in analyzing the JS code, I came over an endpoint: /api/AdditionalCustomerFields which was disclosing UserID of all customers up to the date. Then i simply replied to closed report by explaining how i was able to get unique UserID of every user on that site which leaded to mass PII discloser of every user of the target. After few days, it was reopened and triaged as High.

Critical Where?

Get Veshraj Ghimire’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

The game didn’t ended here, as the JS code was found interesting, I planned to dig more deeper. After few days, I came over an endpoint /api/PushToken which was taking the same UserID parameter as post request and returning critical information including passwordHash and resetToken on it’s response. Luckily, it was too lacking access control.

Press enter or click to view image in full size

As, I was able to get reset token by passing unique UserID of any user. I was able to chain it with older finding, since i had userID of every users on the site. I could simply do forget password and use the recoveryToken which i could get through /api/PushToken endpoint. Here is the steps to reproduce for account takeover of every users on the site:

Sending /api/AdditionalCustomerFields request would give every user’s unique UserID.
Sending request to /api/Customer/GetAdditional?customerId= with UserID would disclose his/her email address.
Resetting the password of user which i got from step2.
Sending POST request to /api/PushTokenwith unique UserID in body would simply show the recovery code requested on step3.

This is how, I could simply takeover anyone’s account on the site.

Takeaways:

Never Give up (Good things takes time).
Try to understand the site and try every features.
Don’t forget to analyze JS file, they can contain lots of sensitive information and hidden endpoints.

Bonus: You can learn more about utilizing JS files to find hidden endpoints and sensitive informations here:
https://www.bugbountyhunter.com/guides/?type=javascript_files

That is all for this time,
Hope you enjoyed the writeup. Happy New Year ❤️
You can find me on Twitter , if you wish to connect with me.

If you are just starting out in any field of Cyber Security, Pentester Nepal community can be very helpful for you, make sure to join it.
