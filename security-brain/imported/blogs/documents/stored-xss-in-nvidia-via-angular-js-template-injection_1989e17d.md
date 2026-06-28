---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-09-25_stored-xss-in-nvidia-via-angular-js-template-injection.md
original_filename: 2022-09-25_stored-xss-in-nvidia-via-angular-js-template-injection.md
title: Stored XSS in Nvidia via Angular JS template injection
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
raw_sha256: 1989e17d59ef021498da6c04423c6f6155bbf9fb86e8a0e787980ace47229088
text_sha256: 81ce851864fad8ad6fd3b2924a0a7263aaeb99ace40697087e502892fdd1170a
ingested_at: '2026-06-28T07:32:14Z'
sensitivity: unknown
redactions_applied: false
---

# Stored XSS in Nvidia via Angular JS template injection

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-09-25_stored-xss-in-nvidia-via-angular-js-template-injection.md
- Source Type: markdown
- Detected Topics: xss, command-injection, otp
- Ingested At: 2026-06-28T07:32:14Z
- Redactions Applied: False
- Raw SHA256: `1989e17d59ef021498da6c04423c6f6155bbf9fb86e8a0e787980ace47229088`
- Text SHA256: `81ce851864fad8ad6fd3b2924a0a7263aaeb99ace40697087e502892fdd1170a`


## Content

---
title: "Stored XSS in Nvidia via Angular JS template injection"
page_title: "tored XSS in Nvidia via Angular JS template injection | Medium"
url: "https://xthemo.medium.com/stored-xss-at-nvidia-via-angular-js-template-injection-3c9793218860"
authors: ["Mohamed Abdelhady"]
programs: ["Nvidia"]
bugs: ["CSTI", "Stored XSS"]
publication_date: "2022-09-25"
added_date: "2022-09-26"
source: "pentester.land/writeups.json"
original_index: 2120
scraped_via: "browseros"
---

# Stored XSS in Nvidia via Angular JS template injection

Stored XSS in Nvidia via Angular JS template injection
Mohamed Abdelhady
Follow
3 min read
·
Sep 25, 2022

35

Hello security folks , I’m going talk about how I got Stored XSS in Nvidia

Press enter or click to view image in full size
Summary :-

Client-side template injection vulnerabilities arise when applications using a client-side template framework dynamically embed user input in web pages. When a web page is rendered, the framework will scan the page for template expressions, and execute any that it encounters. An attacker can exploit this by supplying a malicious template expression that launches a cross-site scripting (XSS) attack. As with normal cross-site scripting, the attacker-supplied code can perform a wide variety of actions, such as stealing the victim’s session token or login credentials, performing arbitrary actions on the victim’s behalf, and logging their keystrokes.

At first I create a new account and use the website as normal user , I found create post function so I tried to create a new post and see how the request was
Press enter or click to view image in full size
I tested normal XSS payload <img only=1 src=x onerror=alert(1)> & <svg/onload=confirm(1)> but there wasn’t any alert and the payloads were printed as text .
Then I tried {{ 2*10 }} , { 2*10 } , ${2*10} , ${{2*10}} , #{2*10} , <%=2*10%> , <%@2*10%> because the website uses Java and Node js languages
Press enter or click to view image in full size
The post was published like that and the {{}} was only executed
Press enter or click to view image in full size
The {{ 2*10 }} was executed then I said it’s maybe get SSTI or XSS , I tested SSTI payloads like {{config.items()}} but I found an angular error in console with it’s version 1.8.3 and there was no output of the payload
So I realized it can get XSS via Angular
I Tried {{constructor.constructor(‘alert(1)’)()}}
Press enter or click to view image in full size
Then I found the payload worked and it got alert
Press enter or click to view image in full size
document.cookie
Press enter or click to view image in full size

And Finally, I got Nvidia Hall of fame.

Get Mohamed Abdelhady’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Thanks, everyone for reading:)
