---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-02-08_full-account-takeover-ato-a-tale-of-two-bugs-.md
original_filename: 2022-02-08_full-account-takeover-ato-a-tale-of-two-bugs-.md
title: Full Account takeover (ATO) — a tale of two bugs 🐛
category: documents
detected_topics:
- idor
- sso
- command-injection
- api-security
tags:
- imported
- documents
- idor
- sso
- command-injection
- api-security
language: en
raw_sha256: 2ca18305046ac823996ac9be1d2d1c801b113f8e746afcd58bab3998a04cf84e
text_sha256: e4266fb012cd43665d89d772dd5a3813092f90771f539b42a80a89d9841d77dc
ingested_at: '2026-06-28T07:32:09Z'
sensitivity: unknown
redactions_applied: false
---

# Full Account takeover (ATO) — a tale of two bugs 🐛

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-02-08_full-account-takeover-ato-a-tale-of-two-bugs-.md
- Source Type: markdown
- Detected Topics: idor, sso, command-injection, api-security
- Ingested At: 2026-06-28T07:32:09Z
- Redactions Applied: False
- Raw SHA256: `2ca18305046ac823996ac9be1d2d1c801b113f8e746afcd58bab3998a04cf84e`
- Text SHA256: `e4266fb012cd43665d89d772dd5a3813092f90771f539b42a80a89d9841d77dc`


## Content

---
title: "Full Account takeover (ATO) — a tale of two bugs 🐛"
url: "https://medium.com/@kojodaprogrammer/full-account-takeover-ato-a-tale-of-two-bugs-d1b3765ff1de"
authors: ["Kwadwo Amoako"]
bugs: ["IDOR", "Account takeover"]
publication_date: "2022-02-08"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 2928
scraped_via: "browseros"
---

# Full Account takeover (ATO) — a tale of two bugs 🐛

Full Account takeover (ATO) — a tale of two bugs 🐛
Kwadwo Amoako
Follow
3 min read
·
Feb 8, 2022

94

3

Hi everyone, I hope we’re all having a swell day. Before I jump into today's bug report, I’d like to express my sincerest gratitude for the engagement my previous write-up received. In this write-up, I’d be highlighting how I found and chained two seemingly low severity bugs, to achieve account takeover on a program that I cannot disclose due to an NDA- Let’s call this target, www.xyz.com.

An Account takeover (ATO) is when an attacker gains access to the data and privileges associated with a compromised account. The possibility of achieving this is largely dependent on the bugs present in the target application and the creativity of the hacker.

Now, let's start with the first bug, an API based Insecure Direct Object Reference (IDOR), which occurs when an application exposes a reference to an internal implementation object. In English 😅, it's when a part of an application allows you to request and receive information that you're not authorized to see.

In this attack, I intercepted and changed my ID in the body of the POST request,(POST /xyz.com/Account?handler=GetUserData) using, Burp Suite. After sending the request, I got the data of the victim as seen in figure 1.

Press enter or click to view image in full size
figure 1

As important as this bug was, I had to shelve it a little longer because who doesn’t love a good chained attack? Now on to the next bug.🎤

If you haven't been taking static code analysis seriously, I’m here to tell you that you’ve probably missed out on a couple of juicy bugs. Now let’s take a look at the block of code ( figure 2) which I found on the “User Account” page and try to figure out the next line of action….I promise I’ll wait. 😁

Press enter or click to view image in full size
Figure 2

In figure 2, we see a copy of the current user’s session on the browser. The session contains the user’s Id, rights and permission. These values are subsequently sent back to the API services for data, in the name of the current user.

Get Kwadwo Amoako’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Leveraging on the information provided in the first bug, as seen in Figure 1. I reloaded the “User Account” page, intercepted it and modified my IDs to the victim’s IDs.

The result — full access to the victim’s account. N.B — In this attack, I go by the name, Shaibu Abudu and the victim, Eric.

Figure 3

To show impact, I changed the victim's password.

As always, your feedback on this write-up will be very much appreciated.

Disclaimer: This write-up is for educational purposes only. I am in no way responsible for its misuse.

Contact :

LinkedIn
