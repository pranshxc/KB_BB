---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-05-31_the-story-of-my-first-xxx-bug-bounty-from-facebook.md
original_filename: 2020-05-31_the-story-of-my-first-xxx-bug-bounty-from-facebook.md
title: The story of My First $xxx Bug Bounty From Facebook
category: documents
detected_topics:
- command-injection
- otp
- information-disclosure
- business-logic
- api-security
tags:
- imported
- documents
- command-injection
- otp
- information-disclosure
- business-logic
- api-security
language: en
raw_sha256: e68b4d3352165fdafeed1fe7484d8e3f124b02ff1d40f50791a070d85896a3c4
text_sha256: 8184df43a0aac1e700eec42ca1c9272529fa567e5c921dc039710ef1ed995604
ingested_at: '2026-06-28T07:32:02Z'
sensitivity: unknown
redactions_applied: true
---

# The story of My First $xxx Bug Bounty From Facebook

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-05-31_the-story-of-my-first-xxx-bug-bounty-from-facebook.md
- Source Type: markdown
- Detected Topics: command-injection, otp, information-disclosure, business-logic, api-security
- Ingested At: 2026-06-28T07:32:02Z
- Redactions Applied: True
- Raw SHA256: `e68b4d3352165fdafeed1fe7484d8e3f124b02ff1d40f50791a070d85896a3c4`
- Text SHA256: `8184df43a0aac1e700eec42ca1c9272529fa567e5c921dc039710ef1ed995604`


## Content

---
title: "The story of My First $xxx Bug Bounty From Facebook"
url: "https://medium.com/@sudipshah_66336/the-story-of-my-first-xxx-bug-bounty-from-facebook-565a212c94ad"
authors: ["Sudip Shah"]
programs: ["Meta / Facebook"]
bugs: ["Logic flaw", "Information disclosure"]
publication_date: "2020-05-31"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4543
scraped_via: "browseros"
---

# The story of My First $xxx Bug Bounty From Facebook

The story of My First $xxx Bug Bounty From Facebook
Sudip Shah
Follow
4 min read
·
May 31, 2020

265

2

I am a complete beginner & learner seeking for a way to get into bug bounties. I’ve been familiar with bug bounties for over 1 year but I couldn’t get any bounties from my reports. Most of my reports becomes closed as informative and duplicates only.

So after a lot of time and effort , I thought my aim in this lockdown is only to find valid bugs in Facebook . I reported 15 bugs to facebook initially but 7 of them were informative and rest of them(u do the math) were dupes. Then I found this bug ; Page Admin Disclosure.

How I was able to discover the flaw?

I was literally very sad on getting all the reports closed so I thought I’ll try sth new. I thought I’ll check once in the mbasic domain of facebook(m.facebook.com) . First I created a page , tried to check every functions available there. Then I saw sth unusual happening.
In the post options of the page , I saw the more option . When I clicked on the …More option. Though I was acting as Testing(the page) the post was uploaded by the page admin.

Press enter or click to view image in full size

When the Page tries to post any other features like Photos&videos,check in ,etc then the post won’t be posted by the page. It would be posted by the admin. This bug denoted the disclosure of the admin .

The steps I sent to facebook were like this:

Suppose USerA is admin of a Page . Go to m.facebook.com and login with UserA’s account.
2. Now , Go to your Page menu.Select Acting as [Page_name]
And post a text for example;”Hello World”

3. The text is posted by the page .

4 . Now Again Select Acting as [Page_name] option and try to post a photo or check in or
click on more options.
5. Then upload a photo or do checkin or more and Click on post
6. Then the post will be posted by UserA though we selected the option of
‘Acting as [Page_name]’

And then I submitted the bug:

I waited a lot for the response from the Team as I was panicked to know about the results of my bug.

Timeline:

Report Submission : April 5 , 2020

Pre-triage : April 7 ,2020

Triaged : April 8 ,2020

Get Sudip Shah’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Me panicking: April 16 , April 30 , 2020

Press enter or click to view image in full size

Confirmation of Fix: May 4 , 2020

Press enter or click to view image in full size

Panic attacks again: May22, May 28,2020

Press enter or click to view image in full size

Finally the bounty awarded: May 30,2020

Press enter or click to view image in full size

I don’t know how to explain my happiness about my first valid bug in my life to be in facebook . I was really very happy when I received the bounty notification. I was like

I still have a lot to learn and this motivated me to keep continuing the journey.

Thank you so much to everyone and special thanks to Ashok dai .

#facebookbugbounty

POC Link : https://drive.google.com/file/d/1QOUTXfBteinT9KIYaQ6zwEeNTMwa1v26/view?fbclid=IwAR13BaS45MmjvDRI48h***REDACTED-SUSPECT-TOKEN***The most insightful stories about Bug Bounty - Medium
Read stories about Bug Bounty on Medium. Discover smart, unique perspectives on Bug Bounty and the topics that matter…

medium.com

The most insightful stories about Facebook Bug Bounty - Medium
Read stories about Facebook Bug Bounty on Medium. Discover smart, unique perspectives on Facebook Bug Bounty and the…

medium.com

The most insightful stories about Web Applications - Medium
Read stories about Web Applications on Medium. Discover smart, unique perspectives on Web Applications and the topics…

medium.com

The most insightful stories about Infosec - Medium
Read stories about Infosec on Medium. Discover smart, unique perspectives on Infosec
