---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2018-10-18_add-comment-on-a-private-oculus-developer-bug-report.md
original_filename: 2018-10-18_add-comment-on-a-private-oculus-developer-bug-report.md
title: Add comment on a private Oculus Developer bug report
category: documents
detected_topics:
- idor
- access-control
- command-injection
- otp
- graphql
- api-security
tags:
- imported
- documents
- idor
- access-control
- command-injection
- otp
- graphql
- api-security
language: en
raw_sha256: 6bd0f9d99ca84370336fc9a68e0f35f2b8b8d300884d5d43fc463dc9fbfe38e9
text_sha256: b250b4f1021543b03629dc9119a47ff33191f2676c88746ea3524fd5c15c125e
ingested_at: '2026-06-28T07:31:58Z'
sensitivity: unknown
redactions_applied: false
---

# Add comment on a private Oculus Developer bug report

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2018-10-18_add-comment-on-a-private-oculus-developer-bug-report.md
- Source Type: markdown
- Detected Topics: idor, access-control, command-injection, otp, graphql, api-security
- Ingested At: 2026-06-28T07:31:58Z
- Redactions Applied: False
- Raw SHA256: `6bd0f9d99ca84370336fc9a68e0f35f2b8b8d300884d5d43fc463dc9fbfe38e9`
- Text SHA256: `b250b4f1021543b03629dc9119a47ff33191f2676c88746ea3524fd5c15c125e`


## Content

---
title: "Add comment on a private Oculus Developer bug report"
url: "https://medium.com/bugbountywriteup/add-comment-on-a-private-oculus-developer-bug-report-93f35bc80b2c"
authors: ["Sarmad Hassan (@JubaBaghdad)"]
programs: ["Meta / Facebook"]
bugs: ["IDOR", "Broken authorization"]
publication_date: "2018-10-18"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5639
scraped_via: "browseros"
---

# Add comment on a private Oculus Developer bug report

Add comment on a private Oculus Developer bug report
Sarmad Hassan (Juba Baghdad)
Follow
4 min read
·
Oct 18, 2018

301

Hello guys, This time I would like to share with you how I was able to Add comments on private bug report on Oculus Developer support, so let’s get started. :)

What is Oculus

Oculus VR is an American technology company founded by Palmer Luckey, Brendan Iribe, Jack McCauley, Michael Antonov, Nate Mitchell in July 2012 in Irvine, California, and now it is owned by Facebook for more details see this link.

Story of Finding

I already tested oculus couple months ago but didn’t find any bug on it, then in 17 Sep. I decided to test it again, so While poking around Oculus Developer domain, I noticed an option called Report a Bug, where users can submit their bugs ( not security bugs) to oculus support team.

Press enter or click to view image in full size
This is how the support Dashboard looks like, you can see other users public bugs.

When I saw this option I decided to test it, but before we do that let’s see how the option works, so let’s analyze it :)

Analyzing Phase

While analyzing this option I noticed below things:

Users can submit their bugs with two ways, public bugs and private bugs.
In public bugs, any one can add comments or reply to other comments.
In private bugs, no one can add comments except the owner of the bug and the support team.
Private bugs don’t appears in the dashboard from other users perspective.
Press enter or click to view image in full size
You can make your bug private by checking on “Keep Private option” as shown above
Testing Phase

I created public bug and added comment to my bug after that I replied to my comment and Intercepted the request with burpsuite to see what kind of parameters we have in this option, the request was like below:

POST /graphql?locale=user HTTP/1.1
Host: graph.oculus.com

access_token=My-Acces-Token&variables={“input”:{“client_mutation_id”:”1",”comment_parent_id”:”556190998150906",”external_post_id”:”548709645565708",”message”:”what ever”}}&blablabla

as you can see above, we have two interesting parameters:

Get Sarmad Hassan (Juba Baghdad)’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

1- ”comment_parent_id” ==> refers to my bug ID (you can find any public bug ID from the URL link as https://developer.oculus.com/bugs/bug/your-bug-ID/).

2- ”external_post_id” ===> refers to the ID of the comment (my comment) that I replied to it.

when I saw the above request two plans came to my mind :)

Plan A : I wanted to add comments on other users private bugs by replacing my bug ID with their bug ID, it didn’t works :(

Plan B: I wanted to add comments on other users private bugs by replacing external_post_id value to other users value which is their comment ID in their private bug, I created two test accounts in order to reproduce this and it works like a charm and I bypassed their protection because they were checking only on the bug ID not external_post_id (comment ID). I knew that plan B will work when I was in the plan A stage, don’t ask my how !!, I just felt it.

Press enter or click to view image in full size
Attacker bypassed oculus protection and added comment on victim private bug.
Bug Limitation

There was only one limitation in this bug, the question is how attacker can get other users comments ID from their Private bugs since their bugs set as private and as I mentioned before no one can see private bugs except the owner of the bug and the support team!!! it is really a good question, yes it is hard to find that but not impossible, let’s say someone was able to disclose other users comments IDs or attacker can make a list for random comments IDs and can perform a random attack and will add his comment on random private bugs, who know? everything is possible :), also I can say fixing this kind of bugs is always the right thing to do.

I reported this bug directly to Facebook Security Team and accepted it as valid bug.

I would like to thanks Facebook Security Team for the Bounty.

Timeline:
Sep. 17, 2018 — Initial Report
Sep. 19, 2018 — Report Triaged
Oct. 05, 2018 — Bug Fixed
Oct. 05, 2018 — Fix Confirmed
Oct. 10, 2018– Bounty awarded

PoC Video:

Takeways:

1- Try to check your target from time to time as always.

2- Understand how the web app. work and what permissions you have.

3- Be creative :).

Thank you

Sarmad Hassan (JubaBaghdad)
