---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-09-22_super-admin-panel-without-credentials-.md
original_filename: 2021-09-22_super-admin-panel-without-credentials-.md
title: Super Admin panel without Credentials 😎
category: documents
detected_topics:
- command-injection
tags:
- imported
- documents
- command-injection
language: en
raw_sha256: 61219cb6f8c677223167d10fee5a98425701c5682de6a1aefeeb5d0ec970ad1a
text_sha256: 9d258c15fefc56a923096b680dcb805078605085d60c43bcde0b855bbc35e88d
ingested_at: '2026-06-28T07:32:07Z'
sensitivity: unknown
redactions_applied: false
---

# Super Admin panel without Credentials 😎

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-09-22_super-admin-panel-without-credentials-.md
- Source Type: markdown
- Detected Topics: command-injection
- Ingested At: 2026-06-28T07:32:07Z
- Redactions Applied: False
- Raw SHA256: `61219cb6f8c677223167d10fee5a98425701c5682de6a1aefeeb5d0ec970ad1a`
- Text SHA256: `9d258c15fefc56a923096b680dcb805078605085d60c43bcde0b855bbc35e88d`


## Content

---
title: "Super Admin panel without Credentials 😎"
url: "https://rizwansiddiqu1.medium.com/super-admin-panel-without-credentials-c2022a23bb35"
authors: ["Rizwan_siddiqui (@Rizwan_SiDdiqu1)"]
bugs: ["Authentication bypass"]
publication_date: "2021-09-22"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3293
scraped_via: "browseros"
---

# Super Admin panel without Credentials 😎

Super Admin panel without Credentials 😎
rizwansiddiqu1
Follow
2 min read
·
Sep 21, 2021

306

2

As-Salaam-Alaikum.

Get rizwansiddiqu1’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

I am back with another writeup I hope you Guys are hunting and earning bounty. This Time I was able to access Super Admin panel without Credentials 😎 . let’s start

Scenario

I was hunting vdp program let’s call it vdp.com. There is hug scope 82k subdomain after using httpx it come to 6k subdomain. I was just scrolling and checking each subdomain one by one after some time I just open this subdomain https://selectwifi.vdp.com. I have one problem whenever I hunt on any program I always use burp in the background To see how the URL open and what change happens behind the seen I open that URL and I see this login page.

Press enter or click to view image in full size
login page

There is no signup page only the login page is there. I just wait here and think about what can I do here. I use waybackurls and gau nothing find. After that, I use gospider tool they give me a bunch of URL some js files some CSS files i was just scrolling and found this URL http://admin.selectwifi.vdp.com/dashboard-super.html I open that URL, and I see super Admin panel. But it redirects to me the login page after some time seeing burp suit and thinking why they redirect me to the login is there any validation on the client-side or on the server-side. After figuring it out. it validate on the client-side by js file which I found on gospider. I just simply disable javascript in my browser And I am able to use the full super Admin panel .there are a lot more things like the staff page announcement page that there I can make an announcement for all staff members.

Raju.
Step to Reproduce
First of all Disable javascript in your browser.
Go to this URL: https://admin.selectwifi.vdp.com/dashboard-super.html
Enjoy full Super Admin Panel.
Takeaway

If u see the login page and there are no signup options use gospider tool or waybackurls.
