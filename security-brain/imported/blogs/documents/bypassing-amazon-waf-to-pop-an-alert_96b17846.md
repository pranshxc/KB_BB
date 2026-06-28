---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-08-29_bypassing-amazon-waf-to-pop-an-alert.md
original_filename: 2022-08-29_bypassing-amazon-waf-to-pop-an-alert.md
title: Bypassing Amazon WAF to pop an alert()
category: documents
detected_topics:
- xss
- sqli
- command-injection
- automation-abuse
tags:
- imported
- documents
- xss
- sqli
- command-injection
- automation-abuse
language: en
raw_sha256: 96b1784642c22695c198323c030d43844577ea2bb566361ec9ff9345a3e18e4c
text_sha256: 7bfc00a200e700318296f4396bec4dd9497985e66cb2e24228a543db46dc61e2
ingested_at: '2026-06-28T07:32:13Z'
sensitivity: unknown
redactions_applied: false
---

# Bypassing Amazon WAF to pop an alert()

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-08-29_bypassing-amazon-waf-to-pop-an-alert.md
- Source Type: markdown
- Detected Topics: xss, sqli, command-injection, automation-abuse
- Ingested At: 2026-06-28T07:32:13Z
- Redactions Applied: False
- Raw SHA256: `96b1784642c22695c198323c030d43844577ea2bb566361ec9ff9345a3e18e4c`
- Text SHA256: `7bfc00a200e700318296f4396bec4dd9497985e66cb2e24228a543db46dc61e2`


## Content

---
title: "Bypassing Amazon WAF to pop an alert()"
url: "https://infosecwriteups.com/bypassing-amazon-waf-to-pop-an-alert-4646ce35554e"
authors: ["Manash (@manash036)"]
bugs: ["WAF bypass", "XSS"]
publication_date: "2022-08-29"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 2247
scraped_via: "browseros"
---

# Bypassing Amazon WAF to pop an alert()

Top highlight

Bypassing Amazon WAF to pop an alert()
Manash
Follow
4 min read
·
Aug 29, 2022

325

2

Press enter or click to view image in full size

Hey everyone, its been a while since I published anything. This time, I’ll be sharing how I bypassed Amazon WAF to get XSS on the target. If you’re into bugbounty, it will help you in creating a mindset to create payloads that can bypass WAFs. Otherwise, it will be a good read. I promise!

For the unknown, a WAF (Web Application Firewall) is a firewall which is used to protect web applications from common attacks such as SQL injection, Cross-Site Scripting (XSS), etc., by filtering out malicious traffic.

Discovery

During the content discovery phase, I was trying to gather as many endpoints as possible. Always do it with Burpsuite Proxy in the background with passive scanning extensions enabled. After spending a good amount of time I analyzed the sitemap that Burpsuite generated to inspect the endpoints manually. The target website itself was quite limited in functionality and therefore, I wasn’t able to find anything of use. Moving over to the robots.txt file, I saw a disallowed endpoint, namely /index.aspx .This was a bit strange because the website was running on Wordpress and pages with .aspx endpoints are not something that you’d see on a wordpress website.

The page itself was blank but on checking the source code, I saw some HTML and some javascript. This got me wondering what the purpose of this page is. I felt something was missing from the puzzle. Then I remembered that I can do some parameter discovery. Arjun (https://github.com/s0md3v/Arjun) is a great tool for this purpose. It can query a huge list of parameter names with minimal requests to the server.

Using arjun to discover parameters

Out of the three parameters, the parameter acc is reflected on the webpage inside a <script>tag . The javascript looked like this:

xt_multc ='&x1=0&x2=REFLECTION_POINT';

REFLECTION_POINT refers to the area where our parameter value is reflected. I need to escape the single quote to be able to inject javascript into the page.

I quickly ran kxss on the page with this parameter to identify special characters that are not sanitized/encoded and are reflected as is.

Press enter or click to view image in full size
kxss is a great tool to identify unfiltered characters in parameters

As can be seen, there are a plenty of special characters that aren’t filtered, out of which, the single quote character is also one of them. This is good news since we are now one step closer to our goal.

Get Manash’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

At this point, I tried a simple payload such as ';alert(document.domain);// . The WAF kicked in and the attempt failed.

Press enter or click to view image in full size
Blocked ☠️
Bypassing the WAF

Upon playing with different payloads, I came to a conclusion that payloads containing valid javascript function names such as alert( (yes, if there is an opening bracket after alert, it will get blocked. Without the opening bracket, it doesn’t get blocked) are blocked. I tried bypassing it by inserting a comment between the alert and the opening bracket and that too got blocked.

I tried fuzzing payloads based on this context (reflection inside Javascript string) with Burpsuite Intruder but it turned out to be unfruitful.

Fuzzing with functions other than alert(), I saw that some functions such as fetch() and print() are allowed. While, I could have used these to demonstrate the proof of concept in my report, I took it as a challenge to defeat the WAF and execute the alert() function.

Instead of writing alert(document.domain), we can use the windowobject to call the alert function: window["alert"](document.domain) .

Unfortunately, this payload was also blocked. Then I remembered that I can use the multi-line comment syntax in Javascript in between the payload to fool the WAF which usually runs based on a set of rules and regular expressions.

The final payload is ';window/*aabb*/['al'%2b'ert'](document./*aabb*/location);//. I split the “alert” string into two parts of “al” and “ert” and then added them. The plus symbol need to be URL encoded; otherwise it would be interpreted as the space symbol.

Press enter or click to view image in full size
Popped an alert finally!

If you liked reading this, please consider following and giving a clap. I’ll be bringing more such content in the coming days. Thanks for reading and I’ll see you around :)

From Infosec Writeups: A lot is coming up in the Infosec every day that it’s hard to keep up with. Join our weekly newsletter to get all the latest Infosec trends in the form of 5 articles, 4 Threads, 3 videos, 2 Github Repos and tools, and 1 job alert for FREE!
