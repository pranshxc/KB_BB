---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2019-03-09_account-takeover-using-cross-site-websocket-hijacking-cswh.md
original_filename: 2019-03-09_account-takeover-using-cross-site-websocket-hijacking-cswh.md
title: Account Takeover Using Cross-Site WebSocket Hijacking (CSWH)
category: documents
detected_topics:
- password-reset
- otp
- command-injection
- csrf
- webhooks
tags:
- imported
- documents
- password-reset
- otp
- command-injection
- csrf
- webhooks
language: en
raw_sha256: 7026421435297edacc64b2d1124c46e7ecfdc7f7acf5782513e0b496921cdebc
text_sha256: cd343ecb1c40ce441d7aceac4fdb1597edf8567b58a41add1cd918b70dd1b17e
ingested_at: '2026-06-28T07:31:59Z'
sensitivity: unknown
redactions_applied: false
---

# Account Takeover Using Cross-Site WebSocket Hijacking (CSWH)

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2019-03-09_account-takeover-using-cross-site-websocket-hijacking-cswh.md
- Source Type: markdown
- Detected Topics: password-reset, otp, command-injection, csrf, webhooks
- Ingested At: 2026-06-28T07:31:59Z
- Redactions Applied: False
- Raw SHA256: `7026421435297edacc64b2d1124c46e7ecfdc7f7acf5782513e0b496921cdebc`
- Text SHA256: `cd343ecb1c40ce441d7aceac4fdb1597edf8567b58a41add1cd918b70dd1b17e`


## Content

---
title: "Account Takeover Using Cross-Site WebSocket Hijacking (CSWH)"
url: "https://medium.com/@sharan.panegav/account-takeover-using-cross-site-websocket-hijacking-cswh-99cf9cea6c50"
authors: ["Sharan Panegav (@PanegavSharan)"]
bugs: ["Cross-Site WebSocket Hijacking (CSWH)", "Account takeover"]
publication_date: "2019-03-09"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5371
scraped_via: "browseros"
---

# Account Takeover Using Cross-Site WebSocket Hijacking (CSWH)

Sharan Panegav
 highlighted

Account Takeover Using Cross-Site WebSocket Hijacking (CSWH)
Sharan Panegav
Follow
3 min read
·
Mar 9, 2019

820

5

Hello ,

While Hunting on a private program. I found the application using WebSocket connection so I checked the WebSocket URL and I found it was vulnerable to CSWH(Cross-site websocket-hijacking)

for more details about CSWH you can go through below blog

https://www.christian-schneider.net/CrossSiteWebSocketHijacking.html

So let’s assume an application is an establishing connection with websocket on URL wss://website.com. to verify the URL is vulnerable to CSWH I follow below steps

Open the web application on browser and login into it.
After this visit, http://websocket.org/echo.html in a new tab, enter the WebSocket URL and click ‘Connect’.
Once the connection is established you must be able to send frames to the server from this page. Capture the websocket frames using burp proxy from a valid session and send them to see how the server responds. If the server responds in the same way as it did for the valid session then it most likely is vulnerable to Cross-Site WebSocket Hijacking
Press enter or click to view image in full size

By following above steps I determined the application is vulnerable to Cross-site-websocket-Hijacking.

Once I established the WebSocket connection on the new tab I have received below websocket response

Press enter or click to view image in full size

If you observe the above response, there is parameter “forgotPasswordId” and its value is “null”.

Get Sharan Panegav’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Now need to determine the value of “_forgotPasswordId” to complete the attack I decided to check the forgot password page and submitted the password reset request.

Press enter or click to view image in full size

Once again I checked the Websocket connection and this time observed the below Response and it contains forgotPassword token

Press enter or click to view image in full size

Exploit :

Now to prepare the exploit of account takeover need to chain CSWH and password reset request. So I prepared below payload to send WebSocket response the attacker site using XHR.

Steps:

Send Password reset link to Victim (Using Forgot password page)
Host the Above CSWH.html and Send URL to Vitim (Similar to CSRF attacks)
Once victim click on URL you will get websocket response on your listener as show in below Image
Press enter or click to view image in full size
Response on Webhook Listener of attacker

Once we have forgot password token we can reset the victim password
