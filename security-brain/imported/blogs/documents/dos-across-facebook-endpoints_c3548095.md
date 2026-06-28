---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2019-03-19_dos-across-facebook-endpoints.md
original_filename: 2019-03-19_dos-across-facebook-endpoints.md
title: DoS Across Facebook Endpoints
category: documents
detected_topics:
- command-injection
- automation-abuse
- api-security
tags:
- imported
- documents
- command-injection
- automation-abuse
- api-security
language: en
raw_sha256: c3548095269f070ae7a1f6d3c088b8352bb132177fd3b617c815fd0973292fb0
text_sha256: 0ac082ba96986c242593468112a0e6cede93d475c5afc9f523f482a11a71be51
ingested_at: '2026-06-28T07:31:59Z'
sensitivity: unknown
redactions_applied: false
---

# DoS Across Facebook Endpoints

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2019-03-19_dos-across-facebook-endpoints.md
- Source Type: markdown
- Detected Topics: command-injection, automation-abuse, api-security
- Ingested At: 2026-06-28T07:31:59Z
- Redactions Applied: False
- Raw SHA256: `c3548095269f070ae7a1f6d3c088b8352bb132177fd3b617c815fd0973292fb0`
- Text SHA256: `0ac082ba96986c242593468112a0e6cede93d475c5afc9f523f482a11a71be51`


## Content

---
title: "DoS Across Facebook Endpoints"
url: "https://medium.com/@maxpasqua/dos-across-facebook-endpoints-1d7d0bc27c7f"
authors: ["Max Pasqua"]
programs: ["Meta / Facebook"]
bugs: ["DoS"]
bounty: "750"
publication_date: "2019-03-19"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5352
scraped_via: "browseros"
---

# DoS Across Facebook Endpoints

DoS Across Facebook Endpoints
Max Pasqua
Follow
3 min read
·
Mar 19, 2019

114

A while back I read a report by a friend of mine, Kassem, where he was able to completely block a user from using Facebook Messenger with a long string of text. After reading this I decided to look through some Facebook endpoints to see if it was still viable. After a day or two of looking I found 7 different endpoints vulnerable to this type of attack. At first I thought I hit a gold mine with this type of attack but within a couple of weeks 6/7 bugs got flagged as a dupe of the original report I made.

Thanks for reporting this issue to us. After investigating the issue, we have realized that this is a duple of your other report #2444785898871880. As such, this report will not be eligible for a bounty. I’m going to close this one and keep the conversation in the original report.

Since the root cause was that Facebook wasn’t limiting the length on parameters they all sadly got classified into one bug. This bug will be the one shown next.

Break Facebook Pages for Admins, Editors, and Moderators

This bug allowed a malicious user with at least Moderator privileged to permanently break an entire page for the Admins, Editors, and Moderators.

This bug was a little weird as I ran into it by accident trying to test for other things, after firing big payloads at the endpoint I kept getting 500 errors, after enough 500 errors the page would completely break

This bug required a page to have the appointments function setup, the quickest way to get appointments is creating a button as seen in the video and hitting booking option to set up appointments through Facebook. After that test the button and put in an appointment and then go to the inbox to complete the rest of the bug

Proof of Concept

1) Once in the inbox of the victims page hit the create appointment button in the bottom right

2) Put in some text in the box and intercept the request sent to burp suite

3) Send the request to the intruder, highlight the text in the notes_for_customer parameter for the intruder position, set the attack type to battering ram, and go to options and turn off Make unmodified base request

4) Copy the text of a large string(Around 20–60mb) to your clipboard and go to payloads and hit paste until you have about 10 requests to be sent

5) Start the attack and you should start seeing 500 errors. After they all go through the page should be broken

Get Max Pasqua’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Video

The other bugs reported use a similar attack type in the bug shown above but with different sized payloads to make it work, as they weren't as impactful I wont be making a full write up about them but if you’re interested in any of them feel free to message me on Facebook to ask.

Other Bugs

Timeline

Submitted- January 14th, 2019

Team asked for clarification - January 14th, 2019

More details provided- January 14th, 2019

Team asked for clarification again- January 17th, 2019

More details provided- January 17th, 2019

Team asked to reproduce it on a whitehat test account- January 23rd, 2019

Whitehat ID’s provided - January 23rd, 2019

Short Term Fix- February 18th, 2019

Bounty Awarded($500)- Short Term Fix- February 21st, 2019

Question about bounty amount- February 21st, 2019

Facebook team awards another ($250) as they were originally supposed to reward $750 total for the vulnerability but forgot to- March 11th, 2019

On a side note some of these vulnerability’s still work as the fix isn't working in full effect right now, I’ve been asked by the security team to include that anyone trying to emulate and report the same issues detailed here will be marked as duplicate!
