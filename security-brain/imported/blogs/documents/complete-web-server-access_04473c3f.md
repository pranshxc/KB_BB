---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2019-06-15_complete-web-server-access.md
original_filename: 2019-06-15_complete-web-server-access.md
title: Complete Web Server Access
category: documents
detected_topics:
- command-injection
- file-upload
- api-security
tags:
- imported
- documents
- command-injection
- file-upload
- api-security
language: en
raw_sha256: 04473c3f41b7c6be0889ef71ed1d1245630bbe2d0fd736653ebf5a3b4630cb63
text_sha256: 0b127f880f4271de8ef970d3a2e4bd3c0807eb84d9acbbb53fd0de1763a2f947
ingested_at: '2026-06-28T07:31:59Z'
sensitivity: unknown
redactions_applied: false
---

# Complete Web Server Access

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2019-06-15_complete-web-server-access.md
- Source Type: markdown
- Detected Topics: command-injection, file-upload, api-security
- Ingested At: 2026-06-28T07:31:59Z
- Redactions Applied: False
- Raw SHA256: `04473c3f41b7c6be0889ef71ed1d1245630bbe2d0fd736653ebf5a3b4630cb63`
- Text SHA256: `0b127f880f4271de8ef970d3a2e4bd3c0807eb84d9acbbb53fd0de1763a2f947`


## Content

---
title: "Complete Web Server Access"
url: "https://medium.com/@saadahmedx/complete-web-server-access-46d19279a2b"
authors: ["Saad Ahmed (@XSaadAhmedX)"]
bugs: ["Unrestricted file upload", "RCE"]
bounty: "500"
publication_date: "2019-06-15"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5213
scraped_via: "browseros"
---

# Complete Web Server Access

Complete Web Server Access
Saad Ahmed
Follow
2 min read
·
Jun 16, 2019

116

2

Hi guy I am back with another POC that I found in PRIVATE program on bugcrowd let get started. So let assume the SITE name private.com I was testing the main website and after crawling I come to know that the server is WINDOWS

I didn’t find any thing on the main website so started to find It’s subdomains after spending alot of time i found a interesting helpdesk.private.com. I created a account on it there is only one functionality that you can report some issue you faced in the website

Get Saad Ahmed’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

I was testing the browser functionality where you can upload only IMG files. The website only accepting only IMG files & then I see the source

var allowedImageExtensionList=[“.bmp”, “.gif”, “.jpeg”, “.jpg”, “.png”]

This is JS client side validation so Iused FIREFOX extension using that I turn of the JS. Since this is a WINDOWS server i upload .ASPX shell and get access to website after getting access to the website I saw that I have ROOT access & able to control all the website on that server. But I found few different websites on that server & I am confused I dont know why.

So I made a quick report the reported that issue to the team & got this response which clear my confusion :D

Press enter or click to view image in full size

I hope you guys like it please comment below if you want to give suggestion
./LOGOUT
