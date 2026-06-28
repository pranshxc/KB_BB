---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-12-20_how-i-was-able-to-reveal-page-admin-of-almost-any-page-on-facebook_2.md
original_filename: 2021-12-20_how-i-was-able-to-reveal-page-admin-of-almost-any-page-on-facebook_2.md
title: How I was able to reveal page admin of almost any page on Facebook
category: documents
detected_topics:
- idor
- command-injection
- automation-abuse
- graphql
- mobile-security
tags:
- imported
- documents
- idor
- command-injection
- automation-abuse
- graphql
- mobile-security
language: en
raw_sha256: fcf7b3e2d4e80fa8d8fdde78adead546bb01adad44e6c3be70a6c8778d54a926
text_sha256: 776e22e4f1afa9a9d6fd4e06796889ef21b34bb1f5c284660f4342aa0170710c
ingested_at: '2026-06-28T07:32:09Z'
sensitivity: unknown
redactions_applied: false
---

# How I was able to reveal page admin of almost any page on Facebook

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-12-20_how-i-was-able-to-reveal-page-admin-of-almost-any-page-on-facebook_2.md
- Source Type: markdown
- Detected Topics: idor, command-injection, automation-abuse, graphql, mobile-security
- Ingested At: 2026-06-28T07:32:09Z
- Redactions Applied: False
- Raw SHA256: `fcf7b3e2d4e80fa8d8fdde78adead546bb01adad44e6c3be70a6c8778d54a926`
- Text SHA256: `776e22e4f1afa9a9d6fd4e06796889ef21b34bb1f5c284660f4342aa0170710c`


## Content

---
title: "How I was able to reveal page admin of almost any page on Facebook"
url: "https://medium.com/pentesternepal/how-i-was-able-to-reveal-page-admin-of-almost-any-page-on-facebook-5a8d68253e0c"
authors: ["Sudip Shah"]
programs: ["Meta / Facebook"]
bugs: ["IDOR"]
bounty: "4,500"
publication_date: "2021-12-20"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3077
scraped_via: "browseros"
---

# How I was able to reveal page admin of almost any page on Facebook

How I was able to reveal page admin of almost any page on Facebook
Sudip Shah
Follow
5 min read
·
Dec 20, 2021

480

3

Hello there , I am Sudip Shah from Pokhara, Nepal(a 19 yo independent security researcher). I found a bug on Facebook for Android where I was able to leak any page admin’s personal account id through IDOR.

It’s been a long time since I wrote an article about my resolved reports due to some internal problems. Today, I am going to write about a high impact vulnerability on Facebook which I found after lots of tries.

Background: I was very devastated and frustrated by the thought that I tried but was not able to find some cool bugs like you see on Twitter or anywhere. Seeing them made me realize that I should learn more about stuff. The logical bugs of Facebook which most people always try at their first attempts were never my first attempts. From the beginning, I always tried to find some high impact bugs on a technical basis but I always ended up finding logical bugs more. Logical and technical both bugs are nice actually, no arguments on that. It was fine actually as I was able to pay my bills due to them. But I wanted more, I wanted to get myself involved on the technical side more. So after 2 years of trying to find on the technical side of Facebook and after lots of duplicates and informative, I finally managed to find an IDOR vulnerability on Facebook’s Android app .

Why did I choose Facebook android? I was frustrated with trying on the Facebook web, checking all those responses and requests, trying to find something hidden. So I tried intercepting on the Facebook Android app.
I managed to find a strange behaviour while checking the request and responses of my HTTP history were while viewing the live video of any page, I was getting the admin’s real id in the response stated in the “broadcaster_id” parameter.

The Bug:

While intercepting and navigating to the other page’s live video section in FB android, I found a vulnerable endpoint in the doc_id=4449530781773796 , where when the page_id in the request is changed to any page then the page admin is disclosed in the response in the broadcaster_id parameter.

Impact:
It leads to page admin disclosure which is a privacy issue to the page. The impact is high because the page’s admin information is meant to be kept private and not shown to the public.

Repro Steps:

1. Send a Post request to graph.facebook.com/graphql with doc_id=4449530781773796
2. Edit the page_id in the request to any page.
3.In the response, we can disclose the admin easily by seeing the broadcaster_id=

Press enter or click to view image in full size

Here is the poc : https://youtu.be/bskV-Nr64rE

This bug could’ve affected most of the pages on Facebook because most of the pages have live video features nowadays.To perform the exploit on a mass scale ,a script would be created to automate and change the value of the page_id in the request and capture the broadcaster_id from the response and save it in a file .
Or ,
We can use the Intruder option of Burpsuite and select the page_id and insert the list of page_id’s in the payloads and run it . Then we could get the admin info in the response and save it in a text file for targeting .

2nd Scenario:

I found one more scenario of the issue where the exact live_video_id can be provided in the request and then the admin will be disclosed in the response through IDOR vulnerability .
The Upper case used directly any page_id but this case uses the exact live_video_id . In this case, the vulnerable doc_id is doc_id=5048752835141848 where the video_id can be changed to any live video’s id then the admin of the page will be disclosed in the response in the broadcaster_id parameter.

Here are the steps :
1. Page conducts a live video
2. Attacker intercepts FB4A and then searches for doc_id=5048752835141848
3. Change the video id to the required page’s live video id
4. We can see the admin of the page being disclosed in the broadcaster_id= parameter in the response.

Press enter or click to view image in full size
idor2

The second case got duplicated of the first issue because they both had the same root cause.

Get Sudip Shah’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Timeline:

Initial report sent: October 5, 2021
The second scenario sent: October 6, 2021
Triaged: October 7, 2021

Press enter or click to view image in full size

Fixed: October 21, 2021

Press enter or click to view image in full size

Rewarded: 4500$ Bounty rewarded on November 5, 2021

Press enter or click to view image in full size
my highest on a single report till now (4500$) xD

I was so happy as I received the bounty notification because it was my highest of all time on a single report. I will try more and learn more to find more high impact bugs in the upcoming days.

Thank you for taking the time to read my article. Have a great day!

Coverage:

Teen hacker scoops $4,500 bug bounty for Facebook flaw that allowed attackers to unmask page admins
James Walker 20 December 2021 at 12:10 UTC Updated: 20 December 2021 at 12:11 UTC High-impact privacy bug in Facebook's…

portswigger.net

You can follow me on Facebook or Twitter if you like to get connected with me.
