---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2019-02-10_csrf-bypass-using-cross-frame-scripting.md
original_filename: 2019-02-10_csrf-bypass-using-cross-frame-scripting.md
title: Csrf Bypass Using Cross Frame Scripting
category: documents
detected_topics:
- command-injection
- otp
- csrf
- clickjacking
tags:
- imported
- documents
- command-injection
- otp
- csrf
- clickjacking
language: en
raw_sha256: b0b082c8770ccd6bc006cd5d460e51245ed34adc6d8ca716cbb587aa59e8357b
text_sha256: ea31bb37f801dc20b9cd009abffb602d224a7f15b7ed2dc20c7c48db46ac1168
ingested_at: '2026-06-28T07:31:58Z'
sensitivity: unknown
redactions_applied: false
---

# Csrf Bypass Using Cross Frame Scripting

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2019-02-10_csrf-bypass-using-cross-frame-scripting.md
- Source Type: markdown
- Detected Topics: command-injection, otp, csrf, clickjacking
- Ingested At: 2026-06-28T07:31:58Z
- Redactions Applied: False
- Raw SHA256: `b0b082c8770ccd6bc006cd5d460e51245ed34adc6d8ca716cbb587aa59e8357b`
- Text SHA256: `ea31bb37f801dc20b9cd009abffb602d224a7f15b7ed2dc20c7c48db46ac1168`


## Content

---
title: "Csrf Bypass Using Cross Frame Scripting"
page_title: "CSRF BYPASS USING CROSS FRAME SCRIPTING | by ?Mr.Hacker | Medium"
url: "https://medium.com/@mr_hacker/csrf-bypass-using-cross-frame-scripting-c349d6f33eb6"
authors: ["Mr.Hacker (@mr_hacker0007)"]
bugs: ["CSRF"]
publication_date: "2019-02-10"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5422
scraped_via: "browseros"
---

# Csrf Bypass Using Cross Frame Scripting

?Mr.Hacker
Follow
3 min read
·
Feb 10, 2019

111

2

Csrf Bypass Using Cross Frame Scripting

Hello Everyone!! Mr.Hacker here, in this article I am going to show how I bypassed csrf using cross frame scripting in a public program on HackerOne.

So directly cutting to the point, there is a module in the web application to send messages to users as shown below.

Press enter or click to view image in full size
Send Message Form

Initially i tested for csrf vulnerability on this module but it was completely mitigated and there was a token in the post request which was validated by the server, hence csrf was not possible. But later i noticed that after generating csrf poc in burp and removing the csrf token and executing it, the server would respond back with the same form values and new csrf token set in the new message form as the response.

Get ?Mr.Hacker’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

So now if i click on “Post Message” then the request would be sent to the server with the form values already being set by the server and request would get successfully executed. Later i came up to chain cross frame scripting and csrf as the entire web application was vulnerable to cross frame scripting.

Press enter or click to view image in full size
CSRF File In Clickjacking
Press enter or click to view image in full size
Chaining CrossFrameScripting and CSRF

Attack Scenario :

The attacker will generate a valid csrf poc with burp with form values and removing csrf token.
Now if we execute the csrf poc server will respond with all form values pre set in the response and also with a valid token, Hence an attacker will include the csrf file inside clickjacking file.
So when the victim clicks on the malicious url sent by attacker, the clickjacking file will load the csrf file and inturn it would auto submit the form with the respective values and later server will send a response with the same form values set and also with the valid csrf token. Hence now the response is loaded using clickjacking and when the user clicks on Post Message it would generate a valid request and it will be executed successfully.

Later i submitted this vulnerability and got a bounty reward, the reason behind the article was to understand that no vulnerability is low if we try to chain it with few other it can also give a high impact issues. Mostly people avoid submitting cross frame scripting or other low impact vulnerabilities as they are out of scope but if we can use it in a unique way then low hanging fruits can also give us a great impact with few other vulnerabilities.

You can see the video Poc Here.

That’s it, i hope you enjoyed this article and Happy Hacking!.
