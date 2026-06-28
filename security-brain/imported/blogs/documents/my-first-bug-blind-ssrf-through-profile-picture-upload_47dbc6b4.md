---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-07-05_my-first-bug-blind-ssrf-through-profile-picture-upload.md
original_filename: 2020-07-05_my-first-bug-blind-ssrf-through-profile-picture-upload.md
title: 'My First Bug: Blind SSRF Through Profile Picture Upload'
category: documents
detected_topics:
- jwt
- idor
- ssrf
- command-injection
- file-upload
- automation-abuse
tags:
- imported
- documents
- jwt
- idor
- ssrf
- command-injection
- file-upload
- automation-abuse
language: en
raw_sha256: 47dbc6b448cb3f46b3a706d2ad8fb765925bbfab6e233a36b597b5b86ad2d6c9
text_sha256: 0634ff815b1b96c29836048a0a5aa44456e9d1b50172bf11e64a8643bdd1fb8f
ingested_at: '2026-06-28T07:32:02Z'
sensitivity: unknown
redactions_applied: false
---

# My First Bug: Blind SSRF Through Profile Picture Upload

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-07-05_my-first-bug-blind-ssrf-through-profile-picture-upload.md
- Source Type: markdown
- Detected Topics: jwt, idor, ssrf, command-injection, file-upload, automation-abuse
- Ingested At: 2026-06-28T07:32:02Z
- Redactions Applied: False
- Raw SHA256: `47dbc6b448cb3f46b3a706d2ad8fb765925bbfab6e233a36b597b5b86ad2d6c9`
- Text SHA256: `0634ff815b1b96c29836048a0a5aa44456e9d1b50172bf11e64a8643bdd1fb8f`


## Content

---
title: "My First Bug: Blind SSRF Through Profile Picture Upload"
url: "https://medium.com/@swaysthinking/my-first-bug-blind-ssrf-through-profile-picture-upload-72f00fd27bc6"
authors: ["swaysthinking (@swaysThinking)"]
bugs: ["SSRF"]
publication_date: "2020-07-05"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4434
scraped_via: "browseros"
---

# My First Bug: Blind SSRF Through Profile Picture Upload

Top highlight

My First Bug: Blind SSRF Through Profile Picture Upload
swaysthinking
Follow
5 min read
·
Jul 9, 2020

555

3

Press enter or click to view image in full size
Photo by Ryoji Iwata on Unsplash

Hello all! This is a writeup for my first bug, an SSRF!

My next writeup will most likely be about my specific approach to learning in bugbounty hunting which I hope will be massively helpful for newcomers. Feel free to follow me right here on medium, or on twitter for updates. Both are: 
@swaysthinking

Overview:
Motivation and advice for new bug hunters…
The story of my first bug!
Credits and Extra Resources…
For the beginners:

Before I landed on this sweet sweet bug, I hacked on 11 different targets(mostly private programs) for days/weeks on end. As I progressed, one thing I always kept in mind was that even though I didn’t land any big bounties or bugs like I had always imagined bugbounty would be like, I took something new from each target.

Everytime I sat down and started hacking on a new target, I would come across something new and intriguing that triggered my curiousity. This prompted me to search, ask, read and learn all about it. It was like being a bloodhound, catching a scent and following it relentlessly until you get it.

“We are always paid for our suspicion by finding what we suspect.” — Henry D.T

Through all of these attempts, I learned so much about different vulnerabilities like JWT, IDOR’s, XXE’s, and what got me my first bug, SSRF.

One thing I want to make clear to hackers feeling unmotivated, do not view your bounties or triaged/resolved bugs as a measure of your success, but rather what new material you have learned, new online connections you have made, and others you have helped.

The story of my first bug!
How I came across this bug:

One day I got a private program invite through CTF’s on Hackerone. But this day as I accepted the invite, I came with a trick up my sleeve. I was going to focus on this program for a week, without hacking on any other program.

Within two days I submitted the report for this bug.

A few key things I think helped me specifically. First of all, before hacking on this program I made sure that I had some sort of methodology and mindmap for hacking on programs. I made one on whimsical.com the previous day and it really helped with my structure.

Day 1:

The first bug on my list, and the one I spent all of May learning was SSRF.

So I started searching. I came a bunch of fishy endpoints with URL parameters, and external links, all of the usual things that would lead to SSRF. However the point of focus was that I got a feel of a couple in-scope domains on the program, and that I harvested some suspicious endpoints.

Day 2:

Get swaysthinking’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

On one of the domains, I found out that they relied heavily on XML HTTP Requests in POST requests.

*Interest levels spike*

So I decided, why not, lets try and go for an XXE approach instead of SSRF. I changed the body of the requests to a bunch of different XXE payloads but nothing. Finally, I decided to try and hack the profile picture upload for my avatar.

Heres where it gets interesting. When I looked at the POST request to upload my image, I then realized it was just a request with the content type, and the raw image in the body.

Press enter or click to view image in full size
My POST Request

So I replaced it with an SVG, to see if the server would accept it, and to gain a larger attack surface with it. This was my malicious SVG Image:

<svg xmlns:svg="http://www.w3.org/2000/svg" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="200" height="200"> 
<image height="30" width="30" 
xlink:href="https://controlledserver.com/pic.svg" /> 
</svg>

In SVG, the xlink:href attribute is used so that the server requests images with any URL provided. Whatever image URL that is inside of the quotes, will be uploaded as the svg image. Through this, I gained blind SSRF to any URL on the internet with an image extension endpoints.

Literally me.
How did you prove Impact?

Through this malicious image upload I was able to:

Make GET requests as their server to any HTTPS URL with an image extension at the end of it.
Fingerprint their libraries, by putting in internal paths to the URI so that I could upload internal server files.
Overlay my image with a static XXE and write whatever I wanted on it.
Along with this I was also able to execute the infamous Billion Laughs Attack although DOS was sadly out of scope. Check out my blog on it for more info!
Credits and Extra Resources

Credits for revision on this blog goes to:

Lucius Fox

Authors Conclusion:

Sorry if this seemed like a short one! This was my first bug so I wanted to create a writeup about it. There are some extra resources under here, so feel free to check them out if you are interested.

Peace out y’all… swaysthinking out

For the bugbounty hunters who want to go a little deeper with this than what I explained, check out this amazing report on hackerone for an exact replica of what I did.

Shopify disclosed on HackerOne: SVG Server Side Request Forgery (SSRF)
I found an issue which seems to be regression of the following issue: https://hackerone.com/reports/97501 . It seems…

hackerone.com

Kill ’em With Laughter: “The Billion Laughs” Attack Through Image Uploads
Hackers always have the last laugh.

medium.com

Lab: Exploiting XXE to perform SSRF attacks | Web Security Academy
This lab has a “Check stock” feature that parses XML input and returns any unexpected values in the response. The lab…

portswigger.net
