---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-07-22_unauthenticated-access-to-mongodb-database-of-oracle-corporation.md
original_filename: 2021-07-22_unauthenticated-access-to-mongodb-database-of-oracle-corporation.md
title: Unauthenticated Access To MongoDB Database of Oracle Corporation
category: documents
detected_topics:
- command-injection
tags:
- imported
- documents
- command-injection
language: en
raw_sha256: 6b11423dd59c8d50e22135148c8cdf7bc5d880887fcf65311131fa2fe8e4ad5d
text_sha256: 666525411e053138c26eba182fc87c4924daaeb50d2667f6192982ca30a4c2c6
ingested_at: '2026-06-28T07:32:07Z'
sensitivity: unknown
redactions_applied: false
---

# Unauthenticated Access To MongoDB Database of Oracle Corporation

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-07-22_unauthenticated-access-to-mongodb-database-of-oracle-corporation.md
- Source Type: markdown
- Detected Topics: command-injection
- Ingested At: 2026-06-28T07:32:07Z
- Redactions Applied: False
- Raw SHA256: `6b11423dd59c8d50e22135148c8cdf7bc5d880887fcf65311131fa2fe8e4ad5d`
- Text SHA256: `666525411e053138c26eba182fc87c4924daaeb50d2667f6192982ca30a4c2c6`


## Content

---
title: "Unauthenticated Access To MongoDB Database of Oracle Corporation"
url: "https://pratikkhalane91.medium.com/unauthenticated-access-to-mongodb-database-of-oracle-corporation-d825c271267a"
authors: ["Pratikkhalane (@KhalanePratik)"]
programs: ["Oracle"]
bugs: ["Missing authentication", "Exposed administrative interface"]
publication_date: "2021-07-22"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3488
scraped_via: "browseros"
---

# Unauthenticated Access To MongoDB Database of Oracle Corporation

Unauthenticated Access To MongoDB Database of Oracle Corporation
Pratikkhalane
Follow
2 min read
·
Jul 22, 2021

119

2

Hello everyone, today I will be talking about one of the critical bugs which I found in the Oracle Corporation. Now, let’s start with the recon process

Step 1 :

1)There are multiple tools by which you can get subdomains, a few of them are given below…

i) Findomain

ii) Subfinder

iii) knock.py

2) To get the live host from the subdomain list, we can use tools such as

i)httprobe

ii) httpx

Now I prefer to use findomain for getting my results quickly. So the command would look something like this….

Command : findomain -t oracle.com| httpx -title -status-code | tee oracle.txt

Step 2 :

You need to gather some more endpoints to find P1 bugs and for that, you can use Waybackurls and Gau.

Step 3 :

Get Pratikkhalane’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Now, I was looking for admin portals to get unauthenticated access and for that, I searched for some endpoints.

Endpoints :

i)dev.
ii)stag.
iii)admin.
iv)internal.
v)stag-dev.
vi)stag-admin.
vii)internal-dev.
viii)_dev.

There are more endpoints that you can find out by opening the URLs one by one from waybackurls, gau, and then add the endpoints to your list. I got my endpoint which started with stag-dev. There were 2 links that opened the MongoDB database. I changed the DNS to IP to see what kind of changes can be seen over here and I found out that it was working on the 8086 port.

Press enter or click to view image in full size
MongoDB Database

After reporting this issue to Oracle Corporation, I’m honored on their Hall of Fame page.

Press enter or click to view image in full size
Oracle Hall Of Fame

They removed the whole website and blocked all of the access to the MongoDB database.

Timeline

Reported: June 15
Mitigated: June 16
Acknowledged in the hall of fame: July 21
Take Away

Always try to find new endpoints using different tools and make a list of them.

Stay tuned for more writeups.
