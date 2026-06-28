---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2018-12-10_my-first-bug-bounty-writeup.md
original_filename: 2018-12-10_my-first-bug-bounty-writeup.md
title: My first bug bounty writeup
category: blogs
detected_topics:
- xss
- command-injection
- automation-abuse
tags:
- imported
- blogs
- xss
- command-injection
- automation-abuse
language: en
raw_sha256: f640f49e1cd5da21c63a839191f4563d70a8ba82238efb6792001246ffc6480f
text_sha256: e71e7a9da0cab33c1b1a1c192b884f6097ad39228415524bf7960365b69e1b95
ingested_at: '2026-06-28T07:31:58Z'
sensitivity: unknown
redactions_applied: false
---

# My first bug bounty writeup

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2018-12-10_my-first-bug-bounty-writeup.md
- Source Type: markdown
- Detected Topics: xss, command-injection, automation-abuse
- Ingested At: 2026-06-28T07:31:58Z
- Redactions Applied: False
- Raw SHA256: `f640f49e1cd5da21c63a839191f4563d70a8ba82238efb6792001246ffc6480f`
- Text SHA256: `e71e7a9da0cab33c1b1a1c192b884f6097ad39228415524bf7960365b69e1b95`


## Content

---
title: "My first bug bounty writeup"
url: "https://medium.com/@sampanna/self-xss-in-indeed-com-e0c99c104cba"
authors: ["Sampanna Chimoriya"]
programs: ["Indeed"]
bugs: ["XSS", "HTML injection"]
publication_date: "2018-12-10"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5537
scraped_via: "browseros"
---

# My first bug bounty writeup

My first bug bounty writeup
Sampanna Chimoriya
Follow
3 min read
·
Dec 10, 2018

44

This is the writeup for my first bug bounty so I am really sorry if I have made some mistake. This blog will not very technical as it wasn’t very hard to discover and exploit. This post is just to prove to people who want to get in bugbounty that you can get into bugbounty and actually succeed.

I visited Indeed.com bug bounty page and was happy to see that *.indeed.com was in scope. So I visited indeed.com and searched for manager in what field and google.com and searched. I tried various text and various characters to try and receive some error. After some minutes of typing various text, I saw an option to set an alert for a job.When I clicked the link I was redirected to

Create job alerts! | Indeed.com
Edit description

subscriptions.indeed.com

and immediately I tried <a href=https://www.google.com>Google</a> and input an email address and clicked Create job. I saw Click Here so I was really happy and when clicked redirected me to Google.com.Then I tried to inject <script>alert(1)</script> and it didn’t work. But when I tried <img src=x onerror=javascript:alert(document.domain);> I received alert and I was also able to steal cookies.

Get Sampanna Chimoriya’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

I am writing this because it took me more than 2 months for me to properly explain and get it fixed because of the various mistakes I made along the way and want to help people not fall in the same trap.

The first mistake I made was that reported it as self html injection because I didn’t try to test to receive an alert because I was just too happy that I actually found a bug. So my report was closed as N/A because it was just a simple html injection . So, I learned that even if you have found a bug try and stay calm and try to increase it’s threat.
I made the report again but I was immediately denied as my first report was closed so it wasn’t even checked properly. So, understand that you have to properly explain with proper techniques and don’t expect that they will understand what you wanted.
I respectfully wrote a detailed explanation that it wasn’t a simple html injection and javascript can be executed. They were happy that I decided to write the report again and asked to do so in the future if I think they didn’t understand it properly. If you think you report was not properly understood then respectfully explain it properly because they want to fix and work with you but you must be patient and clear.
I had received a message that they acknowledged my report and submitted the report to developer team and I would be informed about the fix. But after 18 days I didn’t receive a message so I respectfully messaged them and I received a message that they are working on it and was fixed after some days of the message. So I just want to say that understand that it might take more than you think it might but don’t think they don’t want to fix it or get discouraged
Before I found this vulnerability I had reported two vulnerability which had closed and I actually lost 2 points meaning I had -2 points. So when I submitted this report I got 5 points so my point became 3. I just wrote this because even though I had minus points and I worked hard and learned more and actually found a bug. If I can do it ofcourse anyone can do it.

So never feel discouraged and always check robots.txt file. I also wanted to ask a question if anyone can help me how can I receive reward in Nepal since paypal is not allowed in Nepal so I haven’t been able to receive my reward. Any help is appreciated
