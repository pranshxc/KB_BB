---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-05-02_reflected-xss-on-microsoftcom-via-angular-js-template-injection.md
original_filename: 2020-05-02_reflected-xss-on-microsoftcom-via-angular-js-template-injection.md
title: Reflected XSS on Microsoft.com via Angular Js template injection
category: documents
detected_topics:
- xss
- command-injection
- otp
tags:
- imported
- documents
- xss
- command-injection
- otp
language: en
raw_sha256: 0fafc9a70ac2219b856e28dabf21d773044d82da4ad05d775290fa0815be1ef3
text_sha256: 2ceb3244b0381a5847b7ca2e7b343357747ba1a0760d3892f7304097088d6552
ingested_at: '2026-06-28T07:32:01Z'
sensitivity: unknown
redactions_applied: false
---

# Reflected XSS on Microsoft.com via Angular Js template injection

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-05-02_reflected-xss-on-microsoftcom-via-angular-js-template-injection.md
- Source Type: markdown
- Detected Topics: xss, command-injection, otp
- Ingested At: 2026-06-28T07:32:01Z
- Redactions Applied: False
- Raw SHA256: `0fafc9a70ac2219b856e28dabf21d773044d82da4ad05d775290fa0815be1ef3`
- Text SHA256: `2ceb3244b0381a5847b7ca2e7b343357747ba1a0760d3892f7304097088d6552`


## Content

---
title: "Reflected XSS on Microsoft.com via Angular Js template injection"
url: "https://medium.com/@impratikdabhi/reflected-xss-on-microsoft-com-via-angular-template-injection-2e26d80a7fd8"
authors: ["Pratik Dabhi (@impratikdabhi)"]
programs: ["Microsoft"]
bugs: ["CSTI", "XSS"]
publication_date: "2020-05-02"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4613
scraped_via: "browseros"
---

# Reflected XSS on Microsoft.com via Angular Js template injection

Top highlight

Reflected XSS on Microsoft.com via Angular Js template injection
Pratik Dabhi
Follow
3 min read
·
May 2, 2020

361

1

Press enter or click to view image in full size

I got lots of message for Microsoft POC on Instagram and whatsapp also So i think write a blog for it.

Summary:-

Client-side template injection vulnerabilities arise when applications using a client-side template framework dynamically embed user input in web pages. When a web page is rendered, the framework will scan the page for template expressions, and execute any that it encounters. An attacker can exploit this by supplying a malicious template expression that launches a cross-site scripting (XSS) attack. As with normal cross-site scripting, the attacker-supplied code can perform a wide variety of actions, such as stealing the victim’s session token or login credentials, performing arbitrary actions on the victim’s behalf, and logging their keystrokes.

Browser cross-site scripting filters are typically unable to detect or prevent client-side template injection attacks.

I started my hunting on Microsoft from finding subdomains

I got my target site which is https://flow.microsoft.com/ with some advance recon also Here i noted some points like which technology used by that websites

Press enter or click to view image in full size

Angular templates can contain expressions — JavaScript-like code snippets inside double curly braces. To see how they work have a look at the following jsfiddle:

http://jsfiddle.net/2zs2yv7o/

The text input {{7*7}} is evaluated by Angular, which then displays the output: 49.

This means anyone able to inject double curly braces can execute Angular expressions.

then start sort out the parameters and find out which is “filter”

i used xss payload but no payload is working here :(

Then i manually checked where it values reflected in sources code then i realize that its by recon and source code reading that it is use a angular template and found a version of that template and search a payload for that here i got that payload

Press enter or click to view image in full size

then i use Google for it and

Get Pratik Dabhi’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

https://portswigger.net/research/xss-without-html-client-side-template-injection-with-angularjs

Press enter or click to view image in full size
Video poc:-

And Finally, I got Microsoft Hall of Fame.

https://portal.msrc.microsoft.com/en-us/security-guidance/researcher-acknowledgments-online-services?rtc=1

Press enter or click to view image in full size

Timeline :

13-July-2019 — Report
18-July-2019 — Triaged
28-July-2019 — Valid & Fixed
20-August-2019 — Hall Of Fame

Thanks, everyone for reading:)

Happy Hacking ;)

Support me if you like my work! Buy me a coffee and Follow me on twitter.

impratikdabhi
Hey, 👋 I just created a page here. You can now buy me a coffee!

www.buymeacoffee.com

Website:- https://www.pratikdabhi.com/

Instagram:- https://www.instagram.com/i.m.pratikdabhi

Twitter:- https://twitter.com/impratikdabhi

Youtube:- https://www.youtube.com/impratikdabhi
