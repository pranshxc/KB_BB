---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-06-17_from-bug-bounty-hunter-to-risk-analyst-my-cybersecurity-journey-at-deloitte.md
original_filename: 2023-06-17_from-bug-bounty-hunter-to-risk-analyst-my-cybersecurity-journey-at-deloitte.md
title: 'From Bug Bounty Hunter to Risk Analyst: My Cybersecurity Journey at Deloitte'
category: documents
detected_topics:
- oauth
- sqli
- command-injection
- path-traversal
- otp
- rate-limit
tags:
- imported
- documents
- oauth
- sqli
- command-injection
- path-traversal
- otp
- rate-limit
language: en
raw_sha256: f1349ab333511223e61af6f683f0a9e5bc201813912d64a9cfd3e75ee3c4cffc
text_sha256: c2159828fd046737a6cc69061103cdac358a15cc4f10e2d0d332395987880e7d
ingested_at: '2026-06-28T07:32:22Z'
sensitivity: unknown
redactions_applied: false
---

# From Bug Bounty Hunter to Risk Analyst: My Cybersecurity Journey at Deloitte

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-06-17_from-bug-bounty-hunter-to-risk-analyst-my-cybersecurity-journey-at-deloitte.md
- Source Type: markdown
- Detected Topics: oauth, sqli, command-injection, path-traversal, otp, rate-limit
- Ingested At: 2026-06-28T07:32:22Z
- Redactions Applied: False
- Raw SHA256: `f1349ab333511223e61af6f683f0a9e5bc201813912d64a9cfd3e75ee3c4cffc`
- Text SHA256: `c2159828fd046737a6cc69061103cdac358a15cc4f10e2d0d332395987880e7d`


## Content

---
title: "From Bug Bounty Hunter to Risk Analyst: My Cybersecurity Journey at Deloitte"
url: "https://hunter-55.medium.com/from-bug-bounty-hunter-to-risk-analyst-my-cybersecurity-journey-at-deloitte-56e7835619e4"
authors: ["himanshu pdy (@himanshu_pdy)"]
programs: ["Deloitte"]
bugs: ["Account takeover"]
publication_date: "2023-06-17"
added_date: "2023-06-27"
source: "pentester.land/writeups.json"
original_index: 1041
scraped_via: "browseros"
---

# From Bug Bounty Hunter to Risk Analyst: My Cybersecurity Journey at Deloitte

From Bug Bounty Hunter to Risk Analyst: My Cybersecurity Journey
himanshu pdy
Follow
3 min read
·
Jun 17, 2023

38

1

Hello Folks !!! This story is about my journey as Risk Analyst (1.5 years). I traversed from the realm of bug bounty hunting to the role of a Risk Analyst.

As you know i only write if it’s unique finding or if my approach gives some better result. Here is my Twitter and Linkedin.

During my time, i worked for multiple clients. Since i already had experience in bug bounty hunting, i was working in one of the critical aspect. I worked with multiple 3rd parties payment aggregators.

During my time i found multiple issues for my client applications. But in this blog i’ll talk about only high and critical ones. In Banking System, sometimes the company has to give access to employee portal (critical data) to third parties. It is very important to secure the entry points for such functions or operations.

NOTE :- ALL ISSUES ARE CLOSED !!!

Account Takeover Of Main Employee Portal :-

Application was allowing 3rd party to access the main employee portal to perform some limited actions. Now, there were 2 api’s in order to get access to employee portal.

The first api was using encryption unique key to generate oauth token and the second api was simply using that oauth token to get access to employee portal.

Now as a security guy, i focused on 1st api (oauth genration token using unique encrypted key).

So the 1st api was using userid, channelname and encuniquekey to generate token.

first thing i noticed, there was no csrf token present, so we can do rate limit. But it’s a low issue. Let’s keep it for future use.

I focused on the encuniquekey variable. I tried multiple hash/algorithm to break it but it was secure enough. So i started playing with the while variable itself.

I tried using * command, since it is interacting with the database. I tried sql injection, path traversal, etc. but noting worked. I tried inserting random character but got error. I tried observing whether it is sequential or not, but it was properly implemented.

Then i tried removing other parameter just to see what variables are mandatory. So I removed channelname, and we gor 200 OK response.

Get himanshu pdy’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Then i removed userid and i got error. That means userid is mandatory.

Now i removed the encuniquekey variable and i got success.

WELL!!!! We found a BUG.

The logic was not 100% secure. It was only checking the encuniquekey if it is present in the request. If not, it was giving us the token.

Now this was for my given user id. Now, if you remember we found rate limit issue earlier, we can use that and can perform MASS ACCOUNT TAKEOVER!!!

Press enter or click to view image in full size

2. Multiple High, Medium and low issues found.

I will not be discussing it in detail, but here is a screenshot of the issues that i found for one of my client.

Press enter or click to view image in full size
Press enter or click to view image in full size

Overall I had fun with the company and enjoyed my time.

As always, here’s the mindset or you can say tip for hacking/ bug bounty.

The most important thing to remember is that while testing you will think that application is very secure, but try to remove all parameters one by one so that you can minimise your attack surface area to specific variables.

Everyone usually test all the parameters in a request (whole request) and they try 1–2 things and move onto next request, which result in missing the security vulnerability. By this method you might find new issues.

As you know i only write if it’s unique finding or if my approach gives some better result. Here is my Twitter and Linkedin.

Thank you for your time, “milte hai next writeup mai” …. Happy Hacking.
