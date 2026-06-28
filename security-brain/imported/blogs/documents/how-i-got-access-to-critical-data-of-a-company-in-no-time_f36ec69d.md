---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-03-12_how-i-got-access-to-critical-data-of-a-company-in-no-time-.md
original_filename: 2020-03-12_how-i-got-access-to-critical-data-of-a-company-in-no-time-.md
title: How I got access to critical data of a Company in no time ?
category: documents
detected_topics:
- rate-limit
- command-injection
- information-disclosure
- api-security
tags:
- imported
- documents
- rate-limit
- command-injection
- information-disclosure
- api-security
language: en
raw_sha256: f36ec69df58cf69401341971f7090f1c4fccc60e47c1544791b0d061f1eeecd5
text_sha256: 3b4dc78dc6b8eef9f0c60f7811fec92dbb697a443e1cb9c59955d3b6cec4bcd6
ingested_at: '2026-06-28T07:32:01Z'
sensitivity: unknown
redactions_applied: false
---

# How I got access to critical data of a Company in no time ?

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-03-12_how-i-got-access-to-critical-data-of-a-company-in-no-time-.md
- Source Type: markdown
- Detected Topics: rate-limit, command-injection, information-disclosure, api-security
- Ingested At: 2026-06-28T07:32:01Z
- Redactions Applied: False
- Raw SHA256: `f36ec69df58cf69401341971f7090f1c4fccc60e47c1544791b0d061f1eeecd5`
- Text SHA256: `3b4dc78dc6b8eef9f0c60f7811fec92dbb697a443e1cb9c59955d3b6cec4bcd6`


## Content

---
title: "How I got access to critical data of a Company in no time ?"
url: "https://medium.com/@kaustubhk80/how-i-got-access-to-critical-data-of-a-company-in-no-time-6c396aee21c0"
authors: ["Kaustubh Kale"]
bugs: ["Information disclosure", "Lack of rate limiting", "Bruteforce"]
publication_date: "2020-03-12"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4716
scraped_via: "browseros"
---

# How I got access to critical data of a Company in no time ?

How I got access to critical data of a Company in no time ?
kaustubh kale
Follow
3 min read
·
Mar 12, 2020

117

1

Hi All,

I have been receiving bounties for quite a period of time now, but i hadn't described them as such in write-ups. However, one of the bugs I found triggered me to describe it in a write-up so as to spread awareness among companies on how the data can be so critical and yet so risky if fallen in wrong hands.

Get kaustubh kale’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Coming straight to the point, I have been following this company’s Private program for quite a while and I report bugs to them frequently. One of their primary domain is a gateway to connect for corporate meetings by entering unique Meeting ID’s which allow users to connect using Company’s software or through web console. You cannot connect to a meeting unless you have an invite or a valid Meeting ID.

Console to connect a meeting

As the console was accepting a unique number of digits to connect a meeting, the first thing struck my mind was to check Rate limiting and finding out the range of numbers for saving time. Instantly, I fired up Google to dork on the meeting ID’s for that company and Guess What ! I was able to get some ID’s through FAQ documents published on the company’s sub domain. I entered some ID’s randomly which were mentioned in those documents to check the response. This confirmed that the ID I entered was once a valid Meeting ID.

Response after entering Meeting ID

After watching the response I thought of assuming a Range of numbers to check if I could get some valid Meeting ID’s. I captured the request in Burp and attacked through intruder by Number’s Payload. Below is the response I got after the attack was executed. As the length of the ID’s changed, I got sure there might be a possibility of those being valid meeting ID’s.

Press enter or click to view image in full size
Response after carrying out attack

All the ID’s I had got were accepted as valid Meeting ID’s and I was able to bypass the console to connect multiple meetings at various locations. This was a very critical flaw and could be misused by anyone having wrong intentions which could hamper organizations reputation.

Press enter or click to view image in full size
Console after getting access to a Meeting

I had reported this bug to the Company’s Bounty Program where it was found to be a duplicate submission. However, this kind of vulnerability should be taken seriously as it may involve critical client data, users data which can be misused in various ways to harm the organization’s reputation.

Thank you all for taking out time to read this. Do give a Clap if you found it interesting !
