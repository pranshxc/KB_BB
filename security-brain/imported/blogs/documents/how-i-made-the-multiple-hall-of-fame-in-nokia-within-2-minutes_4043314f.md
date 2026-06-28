---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-09-17_how-i-made-the-multiple-hall-of-fame-in-nokia-within-2-minutes.md
original_filename: 2022-09-17_how-i-made-the-multiple-hall-of-fame-in-nokia-within-2-minutes.md
title: How i made the multiple hall of fame in Nokia within 2 minutes
category: documents
detected_topics:
- clickjacking
- command-injection
- sqli
- automation-abuse
tags:
- imported
- documents
- clickjacking
- command-injection
- sqli
- automation-abuse
language: en
raw_sha256: 4043314ff3d4ef8f2fb2434f8a6c33cacded20643a6359a78aea2cc064f37037
text_sha256: 8dd43c86d0c35e2328699e0d5838f8d5bd239d7c3f53cf98e1d2ac3bf3f4d683
ingested_at: '2026-06-28T07:32:14Z'
sensitivity: unknown
redactions_applied: false
---

# How i made the multiple hall of fame in Nokia within 2 minutes

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-09-17_how-i-made-the-multiple-hall-of-fame-in-nokia-within-2-minutes.md
- Source Type: markdown
- Detected Topics: clickjacking, command-injection, sqli, automation-abuse
- Ingested At: 2026-06-28T07:32:14Z
- Redactions Applied: False
- Raw SHA256: `4043314ff3d4ef8f2fb2434f8a6c33cacded20643a6359a78aea2cc064f37037`
- Text SHA256: `8dd43c86d0c35e2328699e0d5838f8d5bd239d7c3f53cf98e1d2ac3bf3f4d683`


## Content

---
title: "How i made the multiple hall of fame in Nokia within 2 minutes"
url: "https://systemweakness.com/how-i-made-the-multiple-hall-of-fame-in-nokia-within-2-minutes-535056fcb66d"
authors: ["Vedavyasan"]
programs: ["Nokia"]
bugs: ["Clickjacking"]
publication_date: "2022-09-17"
added_date: "2022-09-17"
source: "pentester.land/writeups.json"
original_index: 2159
scraped_via: "browseros"
---

# How i made the multiple hall of fame in Nokia within 2 minutes

How i made the multiple hall of fame in Nokia within 2 minutes
Vedavyasan S (@ved4vyasan)
Follow
4 min read
·
Sep 17, 2022

124

1

Hello guys, Vedavyasan here👽✨.

Recently I got several HoF (HALL OF FAME) for reporting a sinlge bug on their several domains through their Nokia vulnerability disclosure program.So that simple bug is called “clickjacking aka ui redressing”.SO let’s get started and please dont forget to clap✨😁😂

clickjacking
so let’s start
What is clickjacking or ui redressing?

Clickjacking, also known as a “UI redress attack”, is when an attacker uses multiple transparent or opaque layers to trick a user into clicking on a button or link on another page when they were intending to click on the top level page. Thus, the attacker is “hijacking” clicks meant for their page and routing them to another page, most likely owned by another application, domain, or both.

Using a similar technique, keystrokes can also be hijacked. With a carefully crafted combination of stylesheets, iframes, and text boxes, a user can be led to believe they are typing in the password to their email or bank account, but are instead typing into an invisible frame controlled by the attacker.

Examples

For example, imagine an attacker who builds a web site that has a button on it that says “click here for a free iPod”. However, on top of that web page, the attacker has loaded an iframe with your mail account, and lined up exactly the “delete all messages” button directly on top of the “free iPod” button. The victim tries to click on the “free iPod” button but instead actually clicked on the invisible “delete all messages” button. In essence, the attacker has “hijacked” the user’s click, hence the name “Clickjacking”

Press enter or click to view image in full size
clickjaking visual presentation 1
Press enter or click to view image in full size
clickjacking visual presentation 2
How to find clickjacking attack ?

By Manual method
<html>
<head>
<title>Clickjacking POC</title>
</head>
<body>
<p>Website is vulnerable to clickjacking</p>
<iframe src=”http://example.website.nokia.com” width=”500" height=”500">
</iframe>
</body>
</html>

Save this as .html file and open it in browser.
If the targeted site is loaded successfully then it is vulnerable to clickjacking attack.

Method 2:

Visit the URL https://securityheaders.com/ and paste the target and click go.
If the X-Frame-Options header is shows in red colour then it is vulnerable to clickjacking. If it shows in green colour it is not vulnerable to clickjacking.

Method 3:

Visit https://clickjacker.io and paste the target URL. If the page loads successfully, it is vulnerable to clickjacking.

Method 4:

Step1: Check the network tab and reload the site.
Step2: Now visit the target url and check for X-Frame-Options header.
Step3: If the X-Frame-Options header was same origin then it is not vulnerable to clickjacking.
Here for example the site “flipkart.com” has a X-Frame-Options header in its response and it is same origin, so it is not vulnerable to clickjacking attacks. But incase of “testphp.vulnweb.com” it doesn’t has X-Frame-Options header in response so it is vulnerable to clickjacking attacks.

Method 5:

To increase the severity we will use burpsuite.
Step1: Click burp → burp clickbandit → copy clickbandit to clipboard. Once we copied, then go to target site and click inspect element and go to console tab. Paste it and click enter and press start. If the page loads successfully it is vulnerable to clickjacking.

Get Vedavyasan S (@ved4vyasan)’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Step2: Click the input fields and click finish to check if the field is vulnerable.
Click the “click” button till it says You’ve been clickjacked!.

https://www.youtube.com/watch?v=eKt5q2_7Wwc

impact

With a crafted combination of stylesheets, iframes, and text boxes, a user can be led to believe they are typing in the password to their email or bank account, but are instead typing into an invisible frame controlled by the attacker.

RESPONSE FROM NOKIA

Press enter or click to view image in full size
Press enter or click to view image in full size
NOKIA HALL OF FAME POC.

i got about 4 hof from nokia for finding clickjacking vulnerability

So this is all about this write-up, hope you liked it, if you found this informative, do not forget to clap👏 and do let me know if you have any doubts✌️.

Thanks For Reading😊

References:
Clickjackings in Google worth 14981.7$
Instead of going for Cross Site Scripting, Remote Code Execution, SQL Injection, etc. I decided to find clickjacking in…

medium.com

Weaponizing Clickjacking Attack With Click Content Jacking
I Would like to share one simple trick to make clickjacking attack’s more impactful in simple Word’s.

arbazhussain.medium.com

$1800 worth Clickjacking
In this writeup, I will talk about how I earned a total of $1800 by exploiting Clickjacking on pages where User…

medium.com

Account Taker with Clickjacking
This writeup is about how I was able to change other users account email with clickjacking. It was a private program on…

medium.com

Profile links:

https://www.instagram.com/ved4vyasan/

https://www.linkedin.com/in/vedavyasan-s-a9825b228/

https://twitter.com/ved4vyasan
