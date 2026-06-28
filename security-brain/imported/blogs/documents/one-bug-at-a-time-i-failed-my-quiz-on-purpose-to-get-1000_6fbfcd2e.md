---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-05-12_one-bug-at-a-time-i-failed-my-quiz-on-purpose-to-get-1000.md
original_filename: 2023-05-12_one-bug-at-a-time-i-failed-my-quiz-on-purpose-to-get-1000.md
title: 'One Bug at a Time: I failed my quiz on purpose to get $1,000!'
category: documents
detected_topics:
- idor
- command-injection
- password-reset
- api-security
tags:
- imported
- documents
- idor
- command-injection
- password-reset
- api-security
language: en
raw_sha256: 6fbfcd2eb955573b3bae510d23f150ee0e744deb84385db1b7f7f1f0c5ccaa97
text_sha256: 587f962ad0b0ce609976161270009b6bf8b6defea4392dde166e3b0b5f90f498
ingested_at: '2026-06-28T07:32:21Z'
sensitivity: unknown
redactions_applied: false
---

# One Bug at a Time: I failed my quiz on purpose to get $1,000!

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-05-12_one-bug-at-a-time-i-failed-my-quiz-on-purpose-to-get-1000.md
- Source Type: markdown
- Detected Topics: idor, command-injection, password-reset, api-security
- Ingested At: 2026-06-28T07:32:21Z
- Redactions Applied: False
- Raw SHA256: `6fbfcd2eb955573b3bae510d23f150ee0e744deb84385db1b7f7f1f0c5ccaa97`
- Text SHA256: `587f962ad0b0ce609976161270009b6bf8b6defea4392dde166e3b0b5f90f498`


## Content

---
title: "One Bug at a Time: I failed my quiz on purpose to get $1,000!"
url: "https://medium.com/@atomiczsec/one-bug-at-a-time-my-first-paid-bug-1-000-idor-4b89b63b2b4b"
authors: ["atomiczsec (@atomiczsec)"]
bugs: ["IDOR"]
bounty: "1,000"
publication_date: "2023-05-12"
added_date: "2023-05-15"
source: "pentester.land/writeups.json"
original_index: 1162
scraped_via: "browseros"
---

# One Bug at a Time: I failed my quiz on purpose to get $1,000!

One Bug at a Time: I failed my quiz on purpose to get $1,000!
Gavin K
Follow
3 min read
·
May 12, 2023

890

7

Hello all! Glad to see you back : ) Today I will be writing about my first paid bug, it has a funny story line so read along!

Here is the art for today’s story by rez0 : )

Press enter or click to view image in full size

So lets start with how I found this IDOR

Setup: I was in English class on my laptop which is not my main hacking device. I was peeking around on burp suite, waiting for class to start and decided to look at this specific company.
Recon: I first started with the scope of *.redacted.com, I did not know a lot about subdomain recon and what not which doesn't matter in this case. Also, In general most of the bugs I have found on platforms has been on the main application so don't forget to check that : ) I started browsing through every endpoint on the site, but there wasn't a lot of functionality I was seeing. Once I have browsed every possible link on the site I moved on to the second step.
Analyze: Once I had all of those endpoints, I started looking through my burp suite site map which looked something like this:

After looking through a couple of these folders I saw a weird lonely endpoint. The endpoints name was “/opt-out/”. I went to check the request in burp but nothing rendered so I visited the URL in my browser. I then came with a page that looked like an older version of the website that let me enter an email to “Opt-Out” of their mailing lists and what not. This is normal functionality, but I wanted to see what happens when I submit an email. At this point my teacher said “we have a quiz today guys!” but I knew I found something interesting, so I decided to fail my quiz on purpose and fill in random answers so I could keep hacking.

Get Gavin K’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

4. Exploit: Once submitted, I got redirected to a new subdomain which looked extremely old, this peaked my interest for multiple reasons:

Press enter or click to view image in full size

The new subdomain was something like: http://link.XXX-XXX.redacted.com/manage/optout/. When I entered in an email I got this page asking to “Opt Back In” or “Do Not Email”. I then looked at the URL and saw ?profile_id=54613e813b35d0f1328c4533 ….. OK, we are getting somewhere ;) Now I go to change the id by 1 digit to ?profile_id=54613e813b35d0f1328c4534 and BOOM! A new email pops up. Perfect, I can now Opt-Out any user on this platform which includes password reset requests. I can also enumerate emails on this huge platform.

5. Report: My report included all of the details above and at the time, I wasn't the best at writing reports but it did the job. I included the steps to get to this endpoint, 2 screenshots of different emails, and an entire video of each step.

Here is a timeline for reference:

Reported: 2021–10–28
Internal Discussion: 2021–11–02 20:24
Triaged & Bounty: 2021–12–03 13:30
Resolved: 2022–02–09
Press enter or click to view image in full size

6. Conclusion: I made $1,000 in class but consequently failed my quiz. In my opinion, it was worth it! Stay in school but maybe…. hack in school :)
