---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-04-20_playing-with-iframes-bypassing-content-security-policy.md
original_filename: 2021-04-20_playing-with-iframes-bypassing-content-security-policy.md
title: 'Playing With iframes: Bypassing Content-Security-Policy'
category: documents
detected_topics:
- xss
- command-injection
- automation-abuse
tags:
- imported
- documents
- xss
- command-injection
- automation-abuse
language: en
raw_sha256: 7481f49b0267f1ab4c402b266426e1682ffc88b1515d7808556dc2f73d632fdc
text_sha256: 8df2153d9940d301ec46dd9d4a8392d077331d615405eb247ad92629404c9ffd
ingested_at: '2026-06-28T07:32:05Z'
sensitivity: unknown
redactions_applied: false
---

# Playing With iframes: Bypassing Content-Security-Policy

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-04-20_playing-with-iframes-bypassing-content-security-policy.md
- Source Type: markdown
- Detected Topics: xss, command-injection, automation-abuse
- Ingested At: 2026-06-28T07:32:05Z
- Redactions Applied: False
- Raw SHA256: `7481f49b0267f1ab4c402b266426e1682ffc88b1515d7808556dc2f73d632fdc`
- Text SHA256: `8df2153d9940d301ec46dd9d4a8392d077331d615405eb247ad92629404c9ffd`


## Content

---
title: "Playing With iframes: Bypassing Content-Security-Policy"
url: "https://jmrcsnchz.medium.com/playing-with-iframes-bypassing-content-security-policy-987c2f0b8e8a"
authors: ["JM Sanchez / 0xEchidonut (@jmrcsnchz)"]
bugs: ["CSP bypass", "Open redirect", "HTML injection"]
publication_date: "2021-04-20"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3722
scraped_via: "browseros"
---

# Playing With iframes: Bypassing Content-Security-Policy

Playing With iframes: Bypassing Content-Security-Policy
0xEchidonut
Follow
4 min read
·
Apr 21, 2021

59

2

Hi fellow hackers and bug bounty hunters! I’m JM Sanchez, and today I’ll be sharing how I found my first bug in a bug bounty program. I hope you’ll learn something or at least be entertained about the story I will be telling in a few seconds.

[UPDATE] Report is now available on Hackerone. Click Here to View

Scope

I will be temporarily naming itcompany.com, because I’m still not allowed to disclose any further details about this program.

company.com has features that lets you customize a template with drop-down widgets, HTML editor, or a mix of both.

In a mind of a hunter, this is an easy HTML Injection, or even XSS (Cross-Site-Scripting). We don’t have to worry about escaping out of attributes and such things because there is already an HTML Editor built for that.

Protection

Of course, the site is running a bug bounty program and is at least aware of common security vulnerabilities. That is why they implemented CSP (Content-Security-Policy) that limits which resources can be included by the user in the template.

The CSP prohibits us from executing inline or remote javascript, if it does, then this article must be titled with somewhat related to XSS.

Since we can’t insert any working javascript in the template, let’s take a look at other things we can insert that may inflict some impact against users.

This is a self made list of what came to my mind after failing to execute javascript

<iframe>
<object>
<embed>

I tried to host a malicious page in my localhost, then forwarded it with ngrok. Then I inserted an iframe tag to the template

<iframe src="https://d2ffae02f9f9.ngrok.io"></iframe>

The result:

It’s blocked, how sad.

Then I changed the src of the iframe to company.com

<iframe src="https://company.com"></iframe>

It returned the homepage as expected. At this point, I assumed that iframes can be sourced only from the company.com domain. However, I was proven wrong. It only took me 2 key presses to find the solution. Surprise surprise, it’s ctrl+u or view-source

Solution

I found the culprit of the filter. In <meta http-equiv=”Content-Security-Policy” content=”…”>, I found this

frame-src data: *.firebaseapp.com *.█████.com *.google.com *.facebook.com 'self';

Iframes in the page are only allowed from *.firebaseapp.com, *.█████.com, *.google.com, *.facebook.com, and from the company.com domain.

Get 0xEchidonut’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

When I saw this, I knew it’s going to be exploitable.

*.firebaseapp.com is FREE. Anyone can just host static html pages in here. So I quickly searched up how to host my page in firebaseapp. Turns out it requires nodeJS, so I quickly installed one then followed steps to deploy my page.

I now own hackerone-jm.firebaseapp.com, a sub-domain included in the *.firebaseapp.com wildcard. Then I inserted it using an iframe

<iframe src="https://hackerone-jm.firebaseapp.com"></iframe>

Result:

Boom! It works. CSP is now bypassed and we can include my own page in the iframe.

What Now?

What can iframes do? It can’t even access the parent’s cookies! All of CSP bypass for nothing!

Well, the statement above is half true. It is true that since my page in firebaseapp.com and company.com do not share the same domain, they also do not share cookies. Cookies can be sent from domain to its subdomain, but not to others.

company.com -> parent window
hackerone-jm.firebaseapp.com -> child (iframe)

Well, iframes are naughty children, they can mess with their parents most of the time if not given proper counter-measures. I watch anime in pirated streaming sites, and one thing all of us will remember are those annoying pop-ups and redirects. This is what inspired my findings

From a simple iframe injection, I upgraded mine to an open redirect. I placed the code below in https://hackerone-jm.firebaseapp.com/index.html

<script>
  top.location = 'https://www.attacker.com';
window.open('https://www.popup.com',"popup","width=825,height=500,resizable=Yes,status=yes,toolbar=no,scrollbars=yes,,left=0,top=0");</script>

I successfully escaped from the iframe. Everytime the iframe is loaded, the whole page including company.com will redirect and there can even be a popup window.

document.location will redirect the current page it is hosted in, but top.location will redirect even the outermost parent.

Press enter or click to view image in full size
Impact

[+] Phishing against other users

[+] The template cannot be edited anymore without reasonable effort. The page is highly dependent on javascript. Disabling javascript will make the webpage useless but not disabling javascript won’t get rid of the pesky iframe

Triaged after 3 days
