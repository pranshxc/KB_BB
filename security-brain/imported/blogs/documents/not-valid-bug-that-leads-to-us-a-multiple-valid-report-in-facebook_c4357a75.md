---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-07-25_not-valid-bug-that-leads-to-us-a-multiple-valid-report-in-facebook.md
original_filename: 2021-07-25_not-valid-bug-that-leads-to-us-a-multiple-valid-report-in-facebook.md
title: Not valid bug that leads to us a multiple Valid Report in Facebook
category: documents
detected_topics:
- command-injection
- information-disclosure
- api-security
tags:
- imported
- documents
- command-injection
- information-disclosure
- api-security
language: en
raw_sha256: c4357a752bc76530450c2fa27f2503363be0278b8944dc7ede310542f63037f5
text_sha256: c2c1d3a09e2f2ef5aabd15165311f6ca43003b4b18ea471361411797fb2a6e23
ingested_at: '2026-06-28T07:32:07Z'
sensitivity: unknown
redactions_applied: false
---

# Not valid bug that leads to us a multiple Valid Report in Facebook

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-07-25_not-valid-bug-that-leads-to-us-a-multiple-valid-report-in-facebook.md
- Source Type: markdown
- Detected Topics: command-injection, information-disclosure, api-security
- Ingested At: 2026-06-28T07:32:07Z
- Redactions Applied: False
- Raw SHA256: `c4357a752bc76530450c2fa27f2503363be0278b8944dc7ede310542f63037f5`
- Text SHA256: `c2c1d3a09e2f2ef5aabd15165311f6ca43003b4b18ea471361411797fb2a6e23`


## Content

---
title: "Not valid bug that leads to us a multiple Valid Report in Facebook"
page_title: "Facebook Page admin disclosure. 2 reports of page admin disclosre | by Kent Jarold Abulag | Medium"
url: "https://medium.com/@Kntjrld/not-valid-bug-that-leads-to-us-a-multiple-valid-report-in-facebook-25a3fb8cb51"
authors: ["Kent Jarold Abulag (@wkemenhehehegsg)"]
programs: ["Meta / Facebook"]
bugs: ["Information disclosure"]
bounty: "1,000"
publication_date: "2021-07-25"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3482
scraped_via: "browseros"
---

# Not valid bug that leads to us a multiple Valid Report in Facebook

Facebook Page admin disclosure
Kent Jarold Abulag
Follow
3 min read
·
Jul 24, 2021

110

1

Press enter or click to view image in full size
Meta BBP

I’m here again to share my 2nd and 3rd valid report. It’s all about page admin disclosure in Facebook Lite. In my Initial report, Facebook security team says its not valid because my Initial report is admin disclosure through reaction. When I create a post and click "View Post" then tried to react in my own post or in any random comment in my new post, my personal account reflected to who’s reacted instead of my page. Facebook security team clarify that anyone can react in any public post/comment so its hard to identify that its from the admin of the page.

After a few days I found a bug that related to my last report. With all the same procedure, the comment section can disclose admins personal account. Without any sign that you're interacting to your page as your profile, your personal account interact to the page. So I open my last report to discuss my concern and they easily identify what It is.

Press enter or click to view image in full size
Steps to reproduce:

1. Create a post on a page using Facebook Lite
2. Instead of clicking "Close" click "View Post" and comment on anything.

Get Kent Jarold Abulag’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

When an admin clicks "View Post" they’re interacting to the page as followers so when they want to comment on something, their personal identity interacts with the page.

Timeline:

06 June 2021 : Initial report
09 June 2021 : Facebook security team says its not valid
12 June 2021 : Review Requested
16 June 2021 : Manage to reproduced and Triaged
24 June 2021 : Fixed
25 June 2021 : Rewarded $xxx

While waiting to fixed that report, I found again one interesting bug that could lead to admin disclosure. When a page admin taps any comment notification from the page using Facebook Lite, comments they make at that time would be posted with their personal identity. I wait to fix my current report before submitting a new report because they're currently working at this product. And after one week of waiting my report is fixed and I'm lucky that this bug is still exist. So I submit this as new report and it's triage in less than 24 hours. After 5 days they said that it's already fixed but I noticed that when a notification is direct to reply someone's comment, still personal profile of the admin interact to the page.

Steps to reproduce:

UserA = Page Admin
UserB = follower of the page
1. UserA create a post in page
2. UserB comment on that post
3. In Facebook Lite, UserA taps that comment notification from page.
4. UserA reply to UserB.

Timeline:

25 June 2021 : submit new report
25 June 2021 : Triaged
30 June 2021 : Fixed and Triaged (There’s some needed to fix)
20 July 2021 : Fixed
23 July 2021 : Rewarded $xxx
