---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2019-03-16_disclosure-of-pending-roles-for-any-facebook-page.md
original_filename: 2019-03-16_disclosure-of-pending-roles-for-any-facebook-page.md
title: Disclosure of Pending Roles for any Facebook Page
category: documents
detected_topics:
- idor
- command-injection
- otp
tags:
- imported
- documents
- idor
- command-injection
- otp
language: en
raw_sha256: 96d204c8a623fbc4a923d5fda108bf9549e3075db09c0e86f30a77801ba8ef95
text_sha256: 0e98bee3a44530794a6d07bbad82f63753b356c1295eed7b335eec3491b45ae3
ingested_at: '2026-06-28T07:31:59Z'
sensitivity: unknown
redactions_applied: false
---

# Disclosure of Pending Roles for any Facebook Page

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2019-03-16_disclosure-of-pending-roles-for-any-facebook-page.md
- Source Type: markdown
- Detected Topics: idor, command-injection, otp
- Ingested At: 2026-06-28T07:31:59Z
- Redactions Applied: False
- Raw SHA256: `96d204c8a623fbc4a923d5fda108bf9549e3075db09c0e86f30a77801ba8ef95`
- Text SHA256: `0e98bee3a44530794a6d07bbad82f63753b356c1295eed7b335eec3491b45ae3`


## Content

---
title: "Disclosure of Pending Roles for any Facebook Page"
url: "https://medium.com/@avinash_/disclosure-of-pending-roles-for-any-facebook-page-ab6e4e219f8e"
authors: ["Avinash Kumar (@itsavinash_)"]
programs: ["Meta / Facebook"]
bugs: ["IDOR"]
bounty: "4,000"
publication_date: "2019-03-16"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5355
scraped_via: "browseros"
---

# Disclosure of Pending Roles for any Facebook Page

Disclosure of Pending Roles for any Facebook Page
Avinash Kumar
Follow
2 min read
·
Mar 16, 2019

372

1

Press enter or click to view image in full size

In this blog post i’ll explain a vulnerability named Insecure Direct Object Reference i found recently in Facebook which let me allowed to disclose pending roles for any Facebook Page.

Facebook Page’s Pending Roles:- User got invitation for a role on page but user doesn’t accepted it yet,invitation is still on pending status.

Description:-Recently Facebook launched a platform named Creators Studio,In which you can find a lot of tools which empowers you to post,monetise,manage,measure your page’s contents effectively.

So i started capturing every HTTP requests/responses inside this new platform.After sometime a GET request fascinated me:

Get Avinash Kumar’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

https://business.facebook.com/media/manager/page_admin_roles/?page_id=123450000&page_name=Your_page_name&fb_dtsg_ag=token&__user=100001234567&__a=1&__dyn=abcd1234xyz&__req=z&__be=1&__pc=PHASED%3ADEFAULT&dpr=1&__rev=4662096&jazoest=28106&__spin_r=4662096&__spin_b=trunk&__spin_t=1546532826 HTTP/1.1

You can reproduce the above request by clicking on Manage Page Roles button inside the Preferences tab.Anyone can clearly observe presence of parameter that we can control i.e page_id.So with help of Burp Suite’s repeater changing the value of parameter page_id with victim’s page_id and then after investigating the HTTP response you will be able to see the name and user id of invited user for a role in victim’s page(even you have no role on that page).

Impact: Any Attacker can be able to identify people invited to have a role on a particular facebook page(including celebrity’s pages).

Proof of Concept:

Responsible Disclosure Timeline:
3 Jan 2019: Report Sent
7 Jan 2019: Facebook Security Team asked for more clearer steps, Steps sent.
10 Jan 2019: Report Triaged
14 Jan 2019: Bug Fixed
6 Feb 2019: $4000 Bounty Rewarded

Thanks
