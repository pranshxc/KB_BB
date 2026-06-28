---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-09-08_unveiling-rce-on-dutch-government-website.md
original_filename: 2023-09-08_unveiling-rce-on-dutch-government-website.md
title: Unveiling RCE on Dutch Government Website
category: documents
detected_topics:
- idor
- xss
- command-injection
- sso
- ssrf
- file-upload
tags:
- imported
- documents
- idor
- xss
- command-injection
- sso
- ssrf
- file-upload
language: en
raw_sha256: 87da941f7921f9e95141bdd1fb4a4d81992afc31abb9ecf3ada7a8c94883de79
text_sha256: 3ffd9db774725a60cbfe08614c59bc35def6de12aa5c1fe48f6fbaa50a45452d
ingested_at: '2026-06-28T07:32:25Z'
sensitivity: unknown
redactions_applied: false
---

# Unveiling RCE on Dutch Government Website

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-09-08_unveiling-rce-on-dutch-government-website.md
- Source Type: markdown
- Detected Topics: idor, xss, command-injection, sso, ssrf, file-upload
- Ingested At: 2026-06-28T07:32:25Z
- Redactions Applied: False
- Raw SHA256: `87da941f7921f9e95141bdd1fb4a4d81992afc31abb9ecf3ada7a8c94883de79`
- Text SHA256: `3ffd9db774725a60cbfe08614c59bc35def6de12aa5c1fe48f6fbaa50a45452d`


## Content

---
title: "Unveiling RCE on Dutch Government Website"
page_title: "File Upload bypass to RCE on Dutch Government Website | by nayeems3c | Medium"
url: "https://medium.com/@nayeems3c/unveiling-rce-on-dutch-government-website-f001a1c5b4fb"
authors: ["Nayeem Islam (@nayeems3c)"]
programs: ["Dutch Government"]
bugs: ["RCE", "Unrestricted file upload"]
publication_date: "2023-09-08"
added_date: "2023-09-13"
source: "pentester.land/writeups.json"
original_index: 798
scraped_via: "browseros"
---

# Unveiling RCE on Dutch Government Website

Unveiling RCE on Dutch Government Website
My story of bypassing File upload feature to achieve Remote Code Execution (RCE) on a Dutch government website.
Nayeem Islam
Follow
4 min read
·
Sep 8, 2023

171

7

Introduction

Assalamu Alaikum! This is Nayeem Islam. I’m currently an undergrad student and a passionate Webapp security learner from Bangladesh.

This is my first write-up and I’ll be sharing how I bypassed File upload to achieve Remote Code Execution (RCE) vulnerability on a Dutch government website. You can skip my background story and head to the exploitation part ahead.

For free writeup link Click here

Background

My bug bounty journey started in September 2021. That time, I saw a few researchers sharing a picture of a cool black T-shirt on Twitter. Since then, it’s been my dream to get Dutch government swag.

Press enter or click to view image in full size
This picture is taken from Tahmid Niloy bhai's timeline.

I began my journey by targeting low-hanging fruits, often receiving informative or not-applicable responses on platforms like HackerOne. I kept trying and finally found my first valid bug in April 2022 and it worked like a motivation to test my luck with Dutch government websites.

My Journey

I gathered some articles about hacking the Dutch government to get an initial idea of the process. Reading those articles, I learned that they only offer swags for impactful bugs, ruling out any low-hanging fruits.

Googled for scopes and found this repository. I found a site related to healthcare. At the time, my recon skills were fairly basic, limited to subdomain enumeration.

I found a single live subdomain using crt.sh. It was an e-learning platform where anyone can sign-up. So, I chose this as my target because more functionality increase the possibility of finding more bugs.

Additionally, I noticed the e-learning portal was built using the PHP Laravel framework which further fueled my anticipation of finding a bug.

File Upload Bypass

So my target was elearning.example.nl. I registered an account, explored my profile and tested for XSS, HTML injection, CSRF, but came up empty-handed.

Then I started testing profile picture upload feature. I tried uploading a simple test.txt file & the upload was successful. However, my joy was vanished as I discovered the following error when attempting to view the uploaded image. There is an error with this image file

Have a close look at the URL structure. You can see below my txt file has been renamed and converted to jpg as well.

Press enter or click to view image in full size

I tried IDOR on this endpoint /storage/528 because this number was user identifier & sequential. It didn’t work. I took a short break to recharge myself then revisited the target.

This time I paid close attention to the sub directory conversions in the URL. I asked myself what the hell is this directory doing here? They might be storing my original text file in the /528/ directory then converting it to jpg and saving it to conversions.

So, I attempted to access the uploaded text file directly from /528/, resulting in a URL like this.

https://elearning.example.nl/528/my-image.txt

My assumption was right. The txt file executed! Then I documented my findings with a Proof of Concept (PoC) and submitted my initial report.

Get Nayeem Islam’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Meanwhile, I was exploring ways to further exploit the file upload feature and came across this excellent article.

Hunting for Bugs in File Upload Feature:
In this blog, I will be listing down some file upload Vulnerability such RCE, SSRF, CSRF, XSS and many more such…

sm4rty.medium.com

Exploiting RCE

Later, I learned about how File Upload can be exploited to achieve RCE. Then I uploaded this simple one liner php shell to see whether it works.

<?php system($_GET['cmd']); ?>

Opened profile image in a new tab and modified the URL with RCE command. The outcome? Voilààà! I had successfully achieved Remote Code Execution.

Press enter or click to view image in full size

Send additional report to prove the impact of this newfound vulnerability.

End Story

I was happy and hopeless at the same time. This discovery seemed too easy, raising the possibility of it being a duplicate. To my surprise, my report was triaged! NCSC-NL also advised me not to upload shell on their system!

Before this discovery, I had never completed a single Portswigger lab on File Upload or Command Execution, except for basic TryHackMe rooms.

This issue was resolved within a month and I was awarded the dream Swag! It was my first critical finding on a real target as well as my first ever bug submission on the Dutch Government. I thought I was lucky but I was wrong. My swag got lost in the shipment. 😞

They say, Enjoy the journey, not just the destination. How true that turned out to be. I learned a ton of lessons throughout this journey.

Timeline

18–06–2022 — Reported the vulnerability.
19–06–2022 — Received the first response.
20–06–2022 — Bug confirmed and triaged.
18–07–2022 — Bug Resolved.
22–07–2022 — Swag shipped by NCSC-NL and lost in the shipment.

I’d like to extend my gratitude to all the members of the Bug Bounty Community of Bangladesh for their mentorship and the InfoSec community on Twitter for sharing invaluable research and tips.

Thank you for taking the time to read this lengthy blog.

You can follow me on

Twitter : https://twitter.com/nayeems3c
