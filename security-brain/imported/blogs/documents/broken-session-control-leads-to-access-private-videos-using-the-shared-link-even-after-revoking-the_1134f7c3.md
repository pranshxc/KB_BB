---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-03-20_broken-session-control-leads-to-access-private-videos-using-the-shared-link-even.md
original_filename: 2022-03-20_broken-session-control-leads-to-access-private-videos-using-the-shared-link-even.md
title: 'Broken session control leads to access private videos using the shared link
  even after revoking the access for specific time!! — #GoogleVRP'
category: documents
detected_topics:
- access-control
- command-injection
- api-security
tags:
- imported
- documents
- access-control
- command-injection
- api-security
language: en
raw_sha256: 1134f7c3e9c8ca3911ba52707595a048e07ff57e73660ec3a749631d4a7ec446
text_sha256: 0940775d208d1fca0cfa0a187a360d7925e0023793c206c05225567f1009103d
ingested_at: '2026-06-28T07:32:10Z'
sensitivity: unknown
redactions_applied: false
---

# Broken session control leads to access private videos using the shared link even after revoking the access for specific time!! — #GoogleVRP

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-03-20_broken-session-control-leads-to-access-private-videos-using-the-shared-link-even.md
- Source Type: markdown
- Detected Topics: access-control, command-injection, api-security
- Ingested At: 2026-06-28T07:32:10Z
- Redactions Applied: False
- Raw SHA256: `1134f7c3e9c8ca3911ba52707595a048e07ff57e73660ec3a749631d4a7ec446`
- Text SHA256: `0940775d208d1fca0cfa0a187a360d7925e0023793c206c05225567f1009103d`


## Content

---
title: "Broken session control leads to access private videos using the shared link even after revoking the access for specific time!! — #GoogleVRP"
url: "https://naveenroy008.medium.com/broken-session-control-leads-to-access-private-videos-using-the-shared-link-even-after-revoking-the-84e31ac16fe4"
authors: ["Naveenroy"]
programs: ["Google"]
bugs: ["Broken Access Control"]
publication_date: "2022-03-20"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 2798
scraped_via: "browseros"
---

# Broken session control leads to access private videos using the shared link even after revoking the access for specific time!! — #GoogleVRP

Broken session control leads to access private videos using the shared link even after revoking the access for specific time!! — #GoogleVRP
nave1n0x
Follow
2 min read
·
Mar 20, 2022

6

1

A lot of people might know how to share the private video and can access that video but here the interesting thing is now this vulnerability can be used to see private video after revoking the access.

For example:

Let’s assume a scenario suppose you have uploaded a private video and share access to a specific people in a organization by entering their email or mistakenly shared the video to a person.

After sometime you are revoking the access to them by removing the mail. In between this suppose the viewer who gets access to the video captures the response of that video and saves it.

Get nave1n0x’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Now if they try to view the video they will see error. Now again using proxy if they inject the response they can still view the video and they can screen record the video also. This video can be viewed by them until the response gets expired. As far as I know it’s taking approximately 8 hours for the session to get expired.

Here when we give the access the private video it effects immediately but when we revoke the access to the video it is different it won’t effect immediately😂

Since as google said it’s a small window of attack , I have uploaded my poc on YouTube itself. Capture the response of my video so that even if I make it private also you will still have access to it for some time..!😛😂.

Final POC Video:

But, when I decided to send this issue to Google VRP the response didn’t make me happy and Yes, the report was closed as ‘Intended Behavior’ :(

So see y’all in a new write-up soon guys !!

Thanks for reading !!

Make sure to follow me on Twitter ;)

@Naveen
