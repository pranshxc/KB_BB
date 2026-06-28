---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-01-25_how-i-hacked-thousand-of-subdomains.md
original_filename: 2022-01-25_how-i-hacked-thousand-of-subdomains.md
title: HOW I hacked thousand of subdomains
category: documents
detected_topics:
- command-injection
- mobile-security
tags:
- imported
- documents
- command-injection
- mobile-security
language: en
raw_sha256: fa2d5fb27d288dd0607da50d68b8cc3b3f30b433bc4a1700eaa162700d648dfa
text_sha256: 7c13896adeb7a64996f22dc058cb81206245fbe576386ff7426478b72d6919a8
ingested_at: '2026-06-28T07:32:09Z'
sensitivity: unknown
redactions_applied: false
---

# HOW I hacked thousand of subdomains

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-01-25_how-i-hacked-thousand-of-subdomains.md
- Source Type: markdown
- Detected Topics: command-injection, mobile-security
- Ingested At: 2026-06-28T07:32:09Z
- Redactions Applied: False
- Raw SHA256: `fa2d5fb27d288dd0607da50d68b8cc3b3f30b433bc4a1700eaa162700d648dfa`
- Text SHA256: `7c13896adeb7a64996f22dc058cb81206245fbe576386ff7426478b72d6919a8`


## Content

---
title: "HOW I hacked thousand of subdomains"
url: "https://medium.com/@moSec/how-i-hacked-thousand-of-subdomains-6aa43b92282c"
authors: ["MoSec (@moe1n1)"]
bugs: ["Subdomain takeover"]
bounty: "5,000"
publication_date: "2022-01-25"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 2982
scraped_via: "browseros"
---

# HOW I hacked thousand of subdomains

1

MoSec
 highlighted

HOW I hacked thousand of subdomains
MoSec
Follow
4 min read
·
Jan 25, 2022

1.1K

12

Hello everyone

in march 0f 2021, I continued my hunting and I invested my time in subdomain finding and subdomain takeover,

subdomain takeover in itself is a low hanging fruit but finding that vulnerable subdomain is really hard

so as you know this was one of my tabs every day

Press enter or click to view image in full size
the repo that helps you in STO

this repo is really useful it helps you to know quickly which engine is vulnerable to STO or not I was looking at it every time I found a different subdomain engine

and this blog https://0xpatrik.com/ is a helpful resource to learn about STO(sub-domain takeover)

“sometimes no matter how hard you try you just have to continue trying”

I learned new things every day I was really happy about it and not finding any vulnerable subdomains made me a bit upset but I didn't stop.

let's begin, during recon on one of my targets after the Aquatone finished. as always I will take a look at every subdomains screenshot and I saw something weird then I dig it on https://toolbox.googleapps.com/ to see it’s CNAME and it was

TARGET: spfmx.domainkey.freshdesk.com.

Press enter or click to view image in full size
a subdomain with a weird response

“ dig deeper than others ”

I don't know why this time I didn't went to the `can I takeover XYZ` repo to check if the Freshdesk is vulnerable or not BUT I am sure if i went there I would stop where the others stopped.

I clicked the signup link

Press enter or click to view image in full size
signup

and after signup, I saw it is not possible to take over it, because verification is required.

Press enter or click to view image in full size
not possible to takeover it

me:

I told myself lets see how these requests going through in burp,

one of the most important things that I think beginners messing is that

you just have to be curious and guess everything, plays with it, and read docs until you realize how it is working

if you can understand it you can hack it better.

this is how my curiosity flow when I want to focus on something let's assume a single request. I created a hundred questions in my mind and answer each of them practically

for example, I ask myself how the front-end handle this request for answering this I go for response manipulation and many other things,

how the backend will process it if I send a different request, what about changing HTTP methods for example PUT to DELETE, and …etc, changing headers … converting body type …just observe each response in result you will figure out how it is working. then you can make it to do something that was not designed for it.

let me make it shorter, do you remember when we were a kid, we were enjoying breaking the toy to see what is inside it?

let's go back to the story.

Get MoSec’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

I played with it for a few minutes then guess what

Press enter or click to view image in full size
I did it
Press enter or click to view image in full size

I was like 😂

there was a missing server-side validation anyone with a burp proxy could capture and manipulate the request and do the takeover.

this is the video POC https://youtu.be/9CISKSddHl4

this is one of the disclosed reports

Zomato disclosed on HackerOne: subdomain takeover on fddkim.zomato.com
Our subdomain fddkim.zomato.com was vulnerable to a 0-day subdomain takeover vulnerability on Freshdesk. The DNS entry…

hackerone.com

then next day I made a fingerprint and started using Subjack to find vuln subdomains. I scanned the whole bug bounty scope and I also scanned TOP one million Alexa websites I found out that thousands of subdomains are vulnerable to this zero-day including:-

dhl.com

stackoverflow.com

raspberrypi.org

avast.com

imperva.com

joebiden.com

and much more famous websites

I submitted more than10 reports and earned 5k in total reward.

the ultimate tip in this write-up is to dig deeper than others, imagine if I visited https://github.com/EdOverflow/can-i-take-over-xyz

and looking for Freshdesk and reading the threads

Press enter or click to view image in full size

it says that it is not vulnerable so I wouldn't find this zero-day,

one of the program triager said this

congratulations on finding a bypass on what many people thought was not possible

Press enter or click to view image in full size

I am still a NOOB and learn every day I do my best to succeed in bug bounty and ethical hacking because it is my hobby and I started exactly one year ago.

I wish success for everyone on this journey.

if you have any questions ping me on Twitter.

thank you for reading my first writeup.
