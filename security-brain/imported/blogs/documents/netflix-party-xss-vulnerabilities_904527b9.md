---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-04-14_netflix-party-xss-vulnerabilities_2.md
original_filename: 2020-04-14_netflix-party-xss-vulnerabilities_2.md
title: Netflix Party — XSS Vulnerabilities
category: documents
detected_topics:
- xss
- command-injection
- mobile-security
tags:
- imported
- documents
- xss
- command-injection
- mobile-security
language: en
raw_sha256: 904527b94980e603fedbe31a349b99cbf219b2971a703f72ab79d3dec633fb1d
text_sha256: d63c772b07f50bb320decc225fca283c1c1343fa030b1646c3e14848eb0c83d0
ingested_at: '2026-06-28T07:32:01Z'
sensitivity: unknown
redactions_applied: false
---

# Netflix Party — XSS Vulnerabilities

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-04-14_netflix-party-xss-vulnerabilities_2.md
- Source Type: markdown
- Detected Topics: xss, command-injection, mobile-security
- Ingested At: 2026-06-28T07:32:01Z
- Redactions Applied: False
- Raw SHA256: `904527b94980e603fedbe31a349b99cbf219b2971a703f72ab79d3dec633fb1d`
- Text SHA256: `d63c772b07f50bb320decc225fca283c1c1343fa030b1646c3e14848eb0c83d0`


## Content

---
title: "Netflix Party — XSS Vulnerabilities"
page_title: "Netlifx Party - Two Severe XSS Vulnerabilities | Medium"
url: "https://medium.com/@kristian.balog/netflix-party-simple-xss-ec92ed1d7e18"
authors: ["kr-b (@pirxcy)"]
programs: ["Netflix"]
bugs: ["XSS"]
publication_date: "2020-04-14"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4654
scraped_via: "browseros"
---

# Netflix Party — XSS Vulnerabilities

Netflix Party — XSS Vulnerabilities
kr-b
Follow
4 min read
·
Apr 15, 2020

259

https://netflixparty.com Chrome extension that lets you watch Netflix shows and movies with your friends.
User nickname
Discovery

One late night playing some World of Warcraft, my friend and I decided we wanted to watch a Netflix show together, so we went ahead and installed the new Netflix Party Chrome add-on that is all over the news and social media. We start up a party, and out of curiosity I start looking around to see what we can do with this, and I spot a set user nickname field.. So just as a shot in the dark I thought why not just try it? I set my name as

<script>alert(1)</script>

I get nothing…

Then I pause the video and a popup appears! Whenever I paused/played the video, sent a message, joined or left a party, it would write my nickname to the chat bar on the right and execute the JavaScript on all members of the party.

Vulnerability

After looking around at the JavaScript of the extension, I spot the vulnerable code in the addMessage() function:

Unfiltered user input being inserted into HTML

The developers were clever enough to escape the input string for messagevariable however, the userNickname variable was inserted into the HTML without any filtering, thus creating the XSS vulnerability as any HTML tags will be parsed by the browser.

Exploits

An XSS vulnerability allows an attacker to inject HTML and also execute arbitrary JavaScript. Here are a few examples of possible attacks I could think of.

Get kr-b’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Change chat history
Starting with a fun, harmless one. You can change the messages and usernames of all the party member with the below payload by setting it as your nickname.

Users exchange messages (just me right now 😢 very lonely)
After changing nickname to payload, all the messages are changed

Convincing phishing attack
This can also lead to a more severe attack. By setting your nickname to the below payload, a full screen iframe will be created on the page, covering it, containing the attacker’s webpage which can contain a fake Netflix login page saying for example “Your session has expired, Please Login again”, the credentials will then get sent to the attacker. All this will happen without the victims ever leaving netflix.com.

Fix

I reported the vulnerability to the developers, after a couple days with no response I chased them up and they fixed it within 1 week.

Fixed code in version 1.7.7 where the userNickname variable is also escaped.
XSS Vulnerability — User Icon
Discovery

After reviewing the fix for the previous bug, I stumbled upon something else, that I’m surprised I didn’t notice before, maybe I was too preoccupied playing with the first thing I found (good tip, look for the same vulnerability). There was another use input field which I forgot about, the user icon.

Vulnerability

Users can’t change their icons by uploading files however, they choose an icon from a list of files stored locally by the extension. This code below then prints that to the page

This value is created with chrome.runtime.getURL('img/' + newicon) and newIcon can’t be edited directly from the extension, but the value is stored in and fetched from Chrome’s local storage, which can be edited!

The $userIcon variable is not filtered, so a simple payload like this would work:

x" onerror=alert(1)
// which turns into
<img src="chrome-extension://.../img/x" onerror="alert(1)">
// this can be stored by (while in context of NetflixParty)
chrome.storage.local.set({"userIcon": 'x" onerror=alert(1)'});
Press enter or click to view image in full size
User can then join any party or have members join their party, and the JavaScript will be executed instantly
Exploits

The exploits possible with this are exactly the same as the previous examples but they just need to be tweaked a little bit and not be within <script> tags but part of the onerror function.

Fix

I then reported this bug, and chased them up a couple times over a few weeks but still no response. So I thought giving this to the hacker community might make them notice :\

Conclusion

As this is a very trending and popular extension, with it being promoted by big media outlets and at time of writing, has over 8 million downloads, it’s quite important to also consider the security aspects when building such an application. Although the vulnerability here doesn’t impact the developer’s assets such as their own servers or any stored information on their side, this does put their users at risk

Extra Info

Just out of curiosity and wanting to practice some programming, I reverse engineered the application and wrote a full exploit tool for this in Python as the application is using unprotected/unauthenticated web sockets (another vulnerability for another time) anyone that has the details of a Netflix Party (npSessionId, npServerId) can talk to the server and interact with it. This means that an attacker can exploit the above mentioned XSS without even needing a Netflix account, they just join a session by providing the payload in the JSON parameter of the request.

The code is very messy sorry
https://github.com/kr-b/netflixparty_exploit
