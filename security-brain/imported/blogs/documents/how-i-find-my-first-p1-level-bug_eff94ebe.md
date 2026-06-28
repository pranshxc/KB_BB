---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-10-13_how-i-find-my-first-p1-level-bug-.md
original_filename: 2020-10-13_how-i-find-my-first-p1-level-bug-.md
title: How I find my first P1 level Bug. $$$
category: documents
detected_topics:
- xss
- command-injection
- mfa
tags:
- imported
- documents
- xss
- command-injection
- mfa
language: en
raw_sha256: eff94ebe62b30e49de5cd963727490276134a47a44e0daa56eea45b03698208e
text_sha256: b2587959171f2a6d702076afeffb17ef1d5df4b2855af150ff180c9ed1cbdc74
ingested_at: '2026-06-28T07:32:03Z'
sensitivity: unknown
redactions_applied: false
---

# How I find my first P1 level Bug. $$$

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-10-13_how-i-find-my-first-p1-level-bug-.md
- Source Type: markdown
- Detected Topics: xss, command-injection, mfa
- Ingested At: 2026-06-28T07:32:03Z
- Redactions Applied: False
- Raw SHA256: `eff94ebe62b30e49de5cd963727490276134a47a44e0daa56eea45b03698208e`
- Text SHA256: `b2587959171f2a6d702076afeffb17ef1d5df4b2855af150ff180c9ed1cbdc74`


## Content

---
title: "How I find my first P1 level Bug. $$$"
page_title: "How I found my first P1 level Bug. $$$ | by Harsh | Medium"
url: "https://medium.com/@merry6607/how-i-find-my-first-p1-level-bug-5a6dd9587203"
authors: ["Harsh"]
bugs: ["XSS"]
publication_date: "2020-10-13"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4200
scraped_via: "browseros"
---

# How I find my first P1 level Bug. $$$

How I found my first P1 level Bug. $$$
Harsh
Follow
2 min read
·
Oct 13, 2020

83

Hello Hunters,

This is my second blog, Today I will share a write-up about how I was able to See the user sensitive information on a Private Program on BugCrowd.

Before reading this report go check out my first report.

How I By-pass the login page and 2FA authentication…..
Hello everyone !

medium.com

Lets Start …

I can't disclose the program name so assume it as www.examle.com

I was Testing for XSS on this website so I started testing on different parameters.
So what I did is open my burp capture the request and spider the host, I saw many parameters over there.
Testing on the huge parameter will actually take a lot of time so I tested on 10–12 parameters but no results for me.
So next I try to do a store XSS on first name and last field, but I was not able to write the script on first and last name, So what I did is capture the request in burp and change the first name and last name and dang my script was stored but unfortunately, the script is not getting executed.
So i thought to send the capture request of first name and last name to intruder and I just select those parameters.
So I have a payload list I just fire the payload list.
Dang I see my Payloads are getting executed with 200 response and a huge number of length.
So I just sort the length and check the response for the highest length. But still I was not able to get any XSS pop up
I was checking each response but no results.
Suddenly I saw the URL on the browser it is like https://something/api/xyz18/id
I was able to see my user id number specified to me over there. I found something Juicy over there so I just change the I’d up down and
BINGO
Press enter or click to view image in full size

12. I was able to see other user data which can be easily used by an attacker to scam user

What I did is checking more Id no. didn’t dig much on user information. Reported the report to bugcrowd got positive response from them.

My first P1 level bug.

What we learn:

Get Harsh’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

We should check everything even small small things sometimes the bug is Infront of our eyes but we never notice on small points.

I hope you like this post.

That’s all for today guys.

#BugBounty #Cybersecurity #Hacking #Hunting #Secure #KeepHacking
