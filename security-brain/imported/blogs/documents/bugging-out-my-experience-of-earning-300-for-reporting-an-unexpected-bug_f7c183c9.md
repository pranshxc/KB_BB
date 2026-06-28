---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-03-10_bugging-out-my-experience-of-earning-300-for-reporting-an-unexpected-bug.md
original_filename: 2023-03-10_bugging-out-my-experience-of-earning-300-for-reporting-an-unexpected-bug.md
title: 'Bugging Out: My Experience of Earning $300 for Reporting an Unexpected Bug'
category: documents
detected_topics:
- idor
- command-injection
- otp
- rate-limit
tags:
- imported
- documents
- idor
- command-injection
- otp
- rate-limit
language: en
raw_sha256: f7c183c921596efd8b6a55a9e388a97e3a66df54deb5533d6caced26aa8bf136
text_sha256: aa62e3a1d28a7d3e4445cfbc271b16d1b4a9fcf9f8a9fed3502e0a11ceb81943
ingested_at: '2026-06-28T07:32:19Z'
sensitivity: unknown
redactions_applied: false
---

# Bugging Out: My Experience of Earning $300 for Reporting an Unexpected Bug

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-03-10_bugging-out-my-experience-of-earning-300-for-reporting-an-unexpected-bug.md
- Source Type: markdown
- Detected Topics: idor, command-injection, otp, rate-limit
- Ingested At: 2026-06-28T07:32:19Z
- Redactions Applied: False
- Raw SHA256: `f7c183c921596efd8b6a55a9e388a97e3a66df54deb5533d6caced26aa8bf136`
- Text SHA256: `aa62e3a1d28a7d3e4445cfbc271b16d1b4a9fcf9f8a9fed3502e0a11ceb81943`


## Content

---
title: "Bugging Out: My Experience of Earning $300 for Reporting an Unexpected Bug"
url: "https://medium.com/@thelinuxboy/bugging-out-my-experience-of-earning-300-for-reporting-an-unexpected-bug-ec9f9b0054bc"
authors: ["Charlie : The Hacker"]
bugs: ["Subdomain takeover"]
bounty: "300"
publication_date: "2023-03-10"
added_date: "2023-03-23"
source: "pentester.land/writeups.json"
original_index: 1394
scraped_via: "browseros"
---

# Bugging Out: My Experience of Earning $300 for Reporting an Unexpected Bug

Top highlight

Bugging Out: My Experience of Earning $300 for Reporting an Unexpected Bug
Charlie : The Hacker
Follow
3 min read
·
Mar 10, 2023

24

Press enter or click to view image in full size

Hey fam,

It’s me Charlie : The Hacker, but my real name is Rajiv. As you read my recent Bounty of $1500 of BAC (kind of logical bug), I got one more Bounty of $300 on the same day of an Unexpected Bug I reported on the same private program.

Let me explain what was the bug, it kind of subdomain takeover type of bug, let me explain what was that and how I reported.

While exploring the private program, I found some of the endpoints where you have option to change/edit the unique business URL, so I tried and changed the URL 2–3 times and I noted all the URLs I changed, now it was the time to check that program allows me to takeover the recently deleted/ changed business URL. I created another account and used same old deleted business URL in this another account and you know what it was claimable. So this was the kind of low level bug, I tried to increase impact of this bug by something else related to it.

So I started with subdomain enumeration with some available github tools, I grabbed almost 500 domains, copied and opened all in my browser, it tooks me 2–3 min to open all links. Now I started checking all the links manually, I got 404 or 403 pages, tried to bypass but not possible then I found some crazy unique business URLs which was deleted before but I found while doing subdomain enumeration, so it means they all are claimable.

Now I created one more account and tried all the claimable unique business URL which I found during subdomain enumeration and you know what I can claim all the URLs I stopped and reported and Why it was unexpected reward for me ? Because they was not having any mechanism that we can claim the unique business URL instant or after few days or not ! Also there is no confirms email that we can claim same or old username till few days then it will be free to claim by anyone. So I didn’t expected any reward, then also I reported and I got bounty. So here is how I reported.

Get Charlie : The Hacker’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

I can’t reveal program name so I’m using REDACTED

Press enter or click to view image in full size
TITLE: Subdomain takeover or old business username claimable.

VRT : Server Security Misconfiguration > Misconfigured DNS > Basic Subdomain Takeover

Summary:

During subdomain takeover, I found some of the subdomain whose unique URL are claimable, even if it is recently deleted or old. This will leads to business url takeover of the business or organisation.

Steps To Reproduce :
Signup and login to redacted.com
Create a company then navigate edit company unique URL and Business name from Edit Business
From here https://redacted.com/my/#edit_company/<business_id>/edit-org-general
Now click on Unique URL, and edit the unique URL with old URL or any subdomain you found during enumeration.
You can see you can procceed after this step, it means that URL is claimed by you.
Also if someone delete the same unique URL, then anyone can claim it instantly.

I found some domain’s while doing subdomain enumeration, there are lots of au.redacted.com, na.redacted.com, etc all are claimable.

Impact:

It seems that the use of tokens and access checks will prevent this issue from causing a large amount of harm. It was basic subdomain takeover.

Thanks for reading my write-up ! If you like then keep it in your story and tag us on instagram (
Charlie : The Hacker
 | @thelinuxboy)
