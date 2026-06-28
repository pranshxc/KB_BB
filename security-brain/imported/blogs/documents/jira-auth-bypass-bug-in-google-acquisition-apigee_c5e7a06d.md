---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-02-28_jira-auth-bypass-bug-in-google-acquisition-apigee.md
original_filename: 2021-02-28_jira-auth-bypass-bug-in-google-acquisition-apigee.md
title: Jira Auth Bypass bug in Google Acquisition (Apigee)
category: documents
detected_topics:
- api-security
- oauth
- command-injection
tags:
- imported
- documents
- api-security
- oauth
- command-injection
language: en
raw_sha256: c5e7a06d8928c36610fb4aaa7880ab1c40771d4a8e76af4cb4a75759696eeffc
text_sha256: d0e27762f1ddcbc94d86b849a486d409c4f59ed68b252fbe473d4d7e5c1dc770
ingested_at: '2026-06-28T07:32:05Z'
sensitivity: unknown
redactions_applied: false
---

# Jira Auth Bypass bug in Google Acquisition (Apigee)

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-02-28_jira-auth-bypass-bug-in-google-acquisition-apigee.md
- Source Type: markdown
- Detected Topics: api-security, oauth, command-injection
- Ingested At: 2026-06-28T07:32:05Z
- Redactions Applied: False
- Raw SHA256: `c5e7a06d8928c36610fb4aaa7880ab1c40771d4a8e76af4cb4a75759696eeffc`
- Text SHA256: `d0e27762f1ddcbc94d86b849a486d409c4f59ed68b252fbe473d4d7e5c1dc770`


## Content

---
title: "Jira Auth Bypass bug in Google Acquisition (Apigee)"
url: "https://jayateerthag.medium.com/jira-authenticated-dashboard-access-in-google-acquisition-apigee-ff20cfe11d99"
authors: ["Jayateertha Guruprasad (@JayateerthaG)"]
programs: ["Google"]
bugs: ["Authentication bypass"]
publication_date: "2021-02-28"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3856
scraped_via: "browseros"
---

# Jira Auth Bypass bug in Google Acquisition (Apigee)

Jira Auth Bypass bug in Google Acquisition (Apigee)
Jayateertha Guruprasad
Follow
2 min read
·
Feb 25, 2021

60

1

I was looking for blogs on GoogleVRP reports as well as noting down it’s popular aquisitions.

Then I found a blog (https://tutorgeeks.blogspot.com/2018/08/misconfigured-jira-setting-apigee.html ) which talks about unauthenticated Jira instance leaking dashboard name ,project title and user profile picture by applying filters.

It also mentions ,the website supports only logging in with @apigee.com email address,So I thought why not try logging in using Google OAUTH. I signed in using my Gmail account and got successfully logged in !!!

Now I visited https://apigeesc.atlassian.net/jira/dashboards?view%3Dpopular ,it was leaking dashboard names and project titles along with user display pictures.

Press enter or click to view image in full size

If you visit the link unauthenticated you can’t find these information ,so it’s a Auth Bypass bug I could login to internal Jira instance using OAUTH sign-in using Gmail account.

Now , I didn’t stop here , I ran a nuclei scan against the website with Jira templates.

I found a endpoint through which I can access the same information without authentication. (https://apigeesc.atlassian.net/rest/api/2/dashboard?maxResults=100)

Get Jayateertha Guruprasad’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

This provided JSON output even for unauthenticated users.

So ,I found a way to access dashboard using authenticated way(OAUTH login) and also unauthenticated way using rest API.

Impact:
1.Attacker is able to find employee details of apigee working in a specific
project/team.
2.Apigee’s new feature or severe bug in project title can be leaked.

3. Moreover when I was authenticated ,I was also able to create private dashboards.

I made a nice report explaining everything and reported to GoogleVRP.

The bug was accepted, rewarded ($xxx) and fixed.

References:

https://hackerone.com/reports/332586

https://tutorgeeks.blogspot.com/2018/08/misconfigured-jira-setting-apigee.html

Liked my article ? Follow me on twitter (@jayateerthaG) and medium for more content about bugbounty, Infosec, cybersecurity and hacking.
