---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-07-07_interesting-privilege-escalation-in-an-old-private-program.md
original_filename: 2022-07-07_interesting-privilege-escalation-in-an-old-private-program.md
title: Interesting Privilege Escalation In an Old Private Program
category: documents
detected_topics:
- api-security
- idor
- access-control
- command-injection
tags:
- imported
- documents
- api-security
- idor
- access-control
- command-injection
language: en
raw_sha256: 85cff49664644cb39ca791e546b0cd0e526c7186d542013e036fe303eb356424
text_sha256: 0271dbd3759345218167fe3461f63b52d247875d12addd0d065767d6f366c5ab
ingested_at: '2026-06-28T07:32:12Z'
sensitivity: unknown
redactions_applied: false
---

# Interesting Privilege Escalation In an Old Private Program

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-07-07_interesting-privilege-escalation-in-an-old-private-program.md
- Source Type: markdown
- Detected Topics: api-security, idor, access-control, command-injection
- Ingested At: 2026-06-28T07:32:12Z
- Redactions Applied: False
- Raw SHA256: `85cff49664644cb39ca791e546b0cd0e526c7186d542013e036fe303eb356424`
- Text SHA256: `0271dbd3759345218167fe3461f63b52d247875d12addd0d065767d6f366c5ab`


## Content

---
title: "Interesting Privilege Escalation In an Old Private Program"
url: "https://ivreznap.medium.com/interesting-privilege-escalation-in-an-old-private-program-225d27253e13"
authors: ["Zunaid Mahmud (@SZ_Mahmud_7)"]
bugs: ["Privilege escalation"]
bounty: "900"
publication_date: "2022-07-07"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 2481
scraped_via: "browseros"
---

# Interesting Privilege Escalation In an Old Private Program

Interesting Privilege Escalation In an Old Private Program
Zunaid Mahmud
Follow
3 min read
·
Jul 7, 2022

212

1

Assalamu Alaikum, I am Zunaid Mahmud from Dhaka, Bangladesh and this is my first write up about a interesting privilege escalation I found recently.

Issue Background

So, the program was very old, but it has some really huge functionalities, and I think although all of the manual bug hunter’s actually love functionalities, but this was a nightmare in terms of “Functionalities”. It has 500+ user role/permission type and 2500+ tables to read/modify data with these user roles.

So, by the time I noticed the bug, I was already hunting on the program for 17 days and submitted some bugs.

The Issue

So, in this particular program, the website had a admin who has all of the accesses and permissions, there were some (a lot actually) user roles to manage different functions.

In beginning of the hunt, as always I wanted to change my user profile as a normal user. But it only can be changed by the organization admin. The request was submitted with a .do file with urlencoded from type.

Get Zunaid Mahmud’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

So, before night, I was searching for a IDOR issue on a particular page. That was also a profile page which contained the User Name, and a bio . The bio was updateable by normal user but User Name was not, so I updated the bio, captured the request for analyses, tried IDOR but there was no luck.

I noticed something interesting in the request history, there was a rest API request with PUT method and JSON body. Interestingly this was the endpoint which was updating the same profile table’s bio parameter. I immediately changed the bio parameter to name with some random value to change the name parameter. The response made me smile big enough to reach north pole to south pole.

In the response, the name parameter was changed, I quickly checked the profile with a reload, but surprisingly, the name was not changed. After a break, I was looking at the request to find out what was wrong, then I noticed the table name I was updating, it was live_profile. I googled with the table name along with company name and found out that, it was a different profile which was used for some kind of blogging page.

So basically, there was two type of profile in the organization, main profile was using data from sys_user table, and then the live_profile table is automatically crated base on sys_user table . So I searched that which users was permitted to write on live_profile table and found out a normal user can only update profile picture and bio parameters of live_profile table among other parameter . So if someone tries to change the name parameter, the system allowed them to make that change. which was the issue. I was able to change some other parameters also without having the required user role.

23 days to triage internally, 42 days to award a bounty 🐸.

Press enter or click to view image in full size

Happy Hunting guys!
