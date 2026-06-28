---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-05-06_chained-bug-xml-file-upload-to-xss-to-csrf-to-full-account-take-over-ato.md
original_filename: 2022-05-06_chained-bug-xml-file-upload-to-xss-to-csrf-to-full-account-take-over-ato.md
title: 'Chained Bug: XML File Upload to XSS to CSRF to Full Account Take Over (ATO)'
category: documents
detected_topics:
- sso
- xss
- command-injection
- file-upload
- path-traversal
- otp
tags:
- imported
- documents
- sso
- xss
- command-injection
- file-upload
- path-traversal
- otp
language: en
raw_sha256: fac82e9cadc350ca143243b03aa96a847ae3f73cdd233c6c9a927beed238009e
text_sha256: 8bdeb288d81749cce2a5377d87ea27754887951f32bcc8e23cea8293667aa295
ingested_at: '2026-06-28T07:32:11Z'
sensitivity: unknown
redactions_applied: false
---

# Chained Bug: XML File Upload to XSS to CSRF to Full Account Take Over (ATO)

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-05-06_chained-bug-xml-file-upload-to-xss-to-csrf-to-full-account-take-over-ato.md
- Source Type: markdown
- Detected Topics: sso, xss, command-injection, file-upload, path-traversal, otp
- Ingested At: 2026-06-28T07:32:11Z
- Redactions Applied: False
- Raw SHA256: `fac82e9cadc350ca143243b03aa96a847ae3f73cdd233c6c9a927beed238009e`
- Text SHA256: `8bdeb288d81749cce2a5377d87ea27754887951f32bcc8e23cea8293667aa295`


## Content

---
title: "Chained Bug: XML File Upload to XSS to CSRF to Full Account Take Over (ATO)"
url: "https://systemweakness.com/chained-bug-xml-file-upload-to-xss-to-csrf-to-full-account-take-over-ato-156409c41b57"
authors: ["Zulfi Al-Farizi"]
bugs: ["XSS", "CSRF", "Account takeover"]
publication_date: "2022-05-06"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 2662
scraped_via: "browseros"
---

# Chained Bug: XML File Upload to XSS to CSRF to Full Account Take Over (ATO)

Chained Bug: XML File Upload to XSS to CSRF to Full Account Take Over (ATO)
Zulfi Al-Farizi
Follow
5 min read
·
May 6, 2022

170

3

Hello Community, today I'm gonna share my experience about how I was able to chain some vulnerabilities into Full Account Take Over. This time I will not explain what is file upload, XSS, CSRF, or ATO because many of you already know these. With all that being said let’s Begin…

What is XML?

According to wikipedia XML (Extensible Markup Language) is a markup language and file format for storing, transmitting, and reconstructing arbitrary data. It defines a set of rules for encoding documents in a format that is both human-readable and machine-readable. The design goals of XML emphasize simplicity, generality, and usability across the Internet. It is a textual data format with strong support via Unicode for different human languages. Although the design of XML focuses on documents, the language is widely used for the representation of arbitrary data structures such as those used in web services.

XML example:

<note>
  <to>Tove</to>
  <from>Jani</from>
  <heading>Reminder</heading>
  <body>Don't forget me this weekend!</body>
</note>

Target | Vuln: 1 Defeating XML file upload

The target is still the same in my previous article. example.com has a feature to upload various kinds of extensions including .xml files, first, I tried all the basic to advance payloads i know to get XXE but no one worked i feel so desperate but suddenly i think about SVG.

Wait what ?? svg ?? yess svg, svg stand for Scalable Vector Graphic but if you look closer it’s kind of xml style format even the header is <?xml?> so i think svg is just another XML tag. But svg is formatted with .svg extension isn’t it? yes correct and the target site is black listed svg extension, what happens if .svg is changed to .xml? they’re just the same and work the same, don’t believe me ?? see the following picture.

Press enter or click to view image in full size

Vuln 2: XSS

So far we have defeated xml file upload that contains svg tag. Now to trigger xss i use the following xml payload.

once i upload the xml payload and visit the uploaded file link I was surprised by pop-up and yelled “YEAHH BABY !”

Press enter or click to view image in full size

But something inside me wants a higher impact so I look deeper on the website and I got another sensitive token leak when using the invite a friend feature and in ViewCart url.

Press enter or click to view image in full size

the url looks like https://www.example.com/ViewCart.asp?mid=7BA2xxxxxxx and the merchantId is leaked on image link of the cart (picture product)

Press enter or click to view image in full size

If another user opens the picture on another tab, it will open the link onhttps://www.example.com/assets/46/461xxx/shoes.jpg notice the 461XXX is the merchantId.

So i got my SID and MerchantID token which other users shouldn’t be able to see. With all that i think about how can I use that information to exploit another user's account ??

Vuln 3: CSRF

The first thing that came to my mind was CSRF, why? because some pages can only be accessed with SID and MerchantId (Cookie too of course). If you visit that page with invalid token or use another user token the website will automatically log out of your account and send you back to login page (I bet the website match the SID and MerchantId with my cookie somehow).

Page like BillingInfo and OwnerDetails use sid and merchantId these page is used for changing email and username. That was an interesting page, i wonder how can i able to exploit that so i intercept the following request on OwnerDetails to change my username.

Press enter or click to view image in full size

What surprised me more is that the page did not use any csrf_token. But on BillingInfo page it uses RequestVerificationToken, it’s value act like csrf token so every time a user changes their email address these value will change.

So with all that knowledge, i create the following javascript to change the victim username on OwnerDetails page:

This script will change the victim's username to an attacker.

Get Zulfi Al-Farizi’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

On the BillingInfo page, i create the script that grabs RequestVerificationToken and pass it to the POST data. I learned this trick in the Ippsec video that solve HackTheBox Crossfit machine, watch his full video here. I recommend you to subscribe his youtube channel for the amazing content about CTF.

These script will change the email address of the victim to attacker@gmail.com.

So my final exploit (xml) script look like the following:

Account Take Over

Now all has been ready it’s time to launch the exploit.

Create 2 (two) account one for victim and another for attacker, on the victim’s account:

Create a store and a product to sell

on attacker’s account:

Go to victim’s store and gather the required information such as merchanId and sid of the victim.
Customize the final (xml) exploit script.
Upload the script, copy the uploaded file link.
Send the link to the victim.

Once victim visit the link and if he/she is logged in then his/her username and email address will be changed automatically to attacker and attacker@gmail.com.

After that just request the reset password of the victim’s account using the new username and email address. Now you have turned the victim’s account into yours.

Rewards?

After i submit this submission, instead of triaged i got this:

Press enter or click to view image in full size

My submission is marked as a duplicate on another endpoint (while mine is on file upload feature) i did contact the Bugcrowd’s support team but not helping at all. Honestly this was my first Account Take Over :)

Thank’s for reading my article, hope you enjoy it !

Please check out my github repository, i created simple python http server that logs incoming requests it can be used for replacing burpcollaborator (if you don’t have burp pro version) since it logs all the incoming request headers. Hope it will be useful.

https://github.com/zulfi0/hserv

Credits:

Ippsec for the lesson, checkout his youtube channel here.

Reference:

https://en.wikipedia.org/wiki/XML
