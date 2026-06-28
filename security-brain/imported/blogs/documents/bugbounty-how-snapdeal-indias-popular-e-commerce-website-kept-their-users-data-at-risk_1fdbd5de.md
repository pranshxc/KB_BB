---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2019-12-19_bugbounty-how-snapdeal-indias-popular-e-commerce-website-kept-their-users-data-a.md
original_filename: 2019-12-19_bugbounty-how-snapdeal-indias-popular-e-commerce-website-kept-their-users-data-a.md
title: '#BugBounty — How Snapdeal (India’s Popular E-commerce Website) Kept their
  Users Data at Risk!'
category: documents
detected_topics:
- command-injection
tags:
- imported
- documents
- command-injection
language: en
raw_sha256: 1fdbd5de0c9efc8dffbc8f272f4fb032251c18caf0ded7d2fe1f91a75584aff4
text_sha256: 3975848f28cf2e22b733c276f920fdd364154a2b177770b0f1effc7aabd90dd4
ingested_at: '2026-06-28T07:32:00Z'
sensitivity: unknown
redactions_applied: false
---

# #BugBounty — How Snapdeal (India’s Popular E-commerce Website) Kept their Users Data at Risk!

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2019-12-19_bugbounty-how-snapdeal-indias-popular-e-commerce-website-kept-their-users-data-a.md
- Source Type: markdown
- Detected Topics: command-injection
- Ingested At: 2026-06-28T07:32:00Z
- Redactions Applied: False
- Raw SHA256: `1fdbd5de0c9efc8dffbc8f272f4fb032251c18caf0ded7d2fe1f91a75584aff4`
- Text SHA256: `3975848f28cf2e22b733c276f920fdd364154a2b177770b0f1effc7aabd90dd4`


## Content

---
title: "#BugBounty — How Snapdeal (India’s Popular E-commerce Website) Kept their Users Data at Risk!"
url: "https://medium.com/@nanda_kumar/bugbounty-how-snapdeal-indias-popular-e-commerce-website-kept-their-user-data-at-risk-3d02b4092d9c"
authors: ["Nanda Kumar (@nk00_nk)"]
programs: ["Snapdeal"]
bugs: ["Insecure storage of sensitive information"]
publication_date: "2019-12-19"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4879
scraped_via: "browseros"
---

# #BugBounty — How Snapdeal (India’s Popular E-commerce Website) Kept their Users Data at Risk!

#BugBounty — How Snapdeal (India’s Popular E-commerce Website) Kept their Users Data at Risk!
Nanda Kumar
Follow
2 min read
·
Dec 19, 2019

170

1

Press enter or click to view image in full size

Hi Guys,

This is my first blog after doing some bug-bounty for few months. This blog illustrates how I was able to access the user's data of snapdeal without their knowledge and interaction. While I was shopping on snapdeal website and during checkout, I came to a thought that — IS THIS IS SAFE TO ENTER YOUR DATA.

Get Nanda Kumar’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

That is how I started to do some recon and content discovery in snapdeal and I discovered an endpoint “https://www.snapdeal.com/monitoring”. So let’s not waste more time and get started how do I able to access snapdeal users account.

Press enter or click to view image in full size
Insecure Storage of Sensitive Information(CWE-922)

In that web directory, I started fuzzing with every link and option I see without realizing that it as cookies itself for the active users in the View Http Sessions.

Press enter or click to view image in full size
Active sessions

Next what enter into anyone sessions and stole their cookies and start messing with their cookies. Intercept the request of your logged-in account in the burp suite and change the username & cookies of your account to anyone. And voila I successfully get complete access to anyone's account.

Press enter or click to view image in full size
Successful access to anyone account
Report Details:

Type of Bug: Insecure Storage of Sensitive Information(CWE-922)

Timeline :

12-Dec-2019: Notified the snapdeal team in the mail but no reply.

19-Dec-2019: Notified the snapdeal team on twitter and later that day vulnerability got fixed.

Thanks for reading!
