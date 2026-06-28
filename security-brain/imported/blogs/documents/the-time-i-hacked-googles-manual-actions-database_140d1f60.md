---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-03-13_the-time-i-hacked-googles-manual-actions-database.md
original_filename: 2023-03-13_the-time-i-hacked-googles-manual-actions-database.md
title: The Time I Hacked Google’s Manual Actions Database
category: documents
detected_topics:
- access-control
- api-security
- sso
- command-injection
- rate-limit
- automation-abuse
tags:
- imported
- documents
- access-control
- api-security
- sso
- command-injection
- rate-limit
- automation-abuse
language: en
raw_sha256: 140d1f60252d3bc2bc918de2cf25359104256c304609e2c4ae1a301cc831e51d
text_sha256: 88e70d025fc62b05ae5147907f6db423eafdbb34fe3cef2e78c389e864ae8143
ingested_at: '2026-06-28T07:32:19Z'
sensitivity: unknown
redactions_applied: false
---

# The Time I Hacked Google’s Manual Actions Database

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-03-13_the-time-i-hacked-googles-manual-actions-database.md
- Source Type: markdown
- Detected Topics: access-control, api-security, sso, command-injection, rate-limit, automation-abuse
- Ingested At: 2026-06-28T07:32:19Z
- Redactions Applied: False
- Raw SHA256: `140d1f60252d3bc2bc918de2cf25359104256c304609e2c4ae1a301cc831e51d`
- Text SHA256: `88e70d025fc62b05ae5147907f6db423eafdbb34fe3cef2e78c389e864ae8143`


## Content

---
title: "The Time I Hacked Google’s Manual Actions Database"
page_title: "The Time I Hacked Google's Manual Actions Database - Tom Anthony"
url: "https://www.tomanthony.co.uk/blog/googles-manual-actions-hack/"
final_url: "https://www.tomanthony.co.uk/blog/googles-manual-actions-hack/"
authors: ["Tom Anthony (@TomAnthonySEO)"]
programs: ["Google"]
bugs: ["Broken Access Control", "Broken authorization"]
bounty: "5,000"
publication_date: "2023-03-13"
added_date: "2023-03-15"
source: "pentester.land/writeups.json"
original_index: 1385
---

> **Short version:**
> 
> In 2013, Google released a tool to view the manual actions (penalties) they were applying to your own site. I discovered the API endpoint did _no authorisation checks_ , and thus I had access to the full manual actions database.  
>  
> I reported the issue to Google, who took the tool down for a couple of days to fix it, and paid me a $5000 bug bounty reward. Google didn’t block me from writing a blog post at the time, but I didn’t think they were going to be happy about it, so I’ve waited until now (10 years later!) to write this up.

August 9th 2013 was a Friday. I remember being at work and hearing that the evening before Google had [released a viewer for manual actions](https://searchengineland.com/google-launches-manual-spam-actions-viewer-streamlines-reconsideration-process-169100). Before this, as crazy as it may seem nowadays, you simply didn’t know if Google were penalising you or not. 

![](https://www.tomanthony.co.uk/blog/wp-content/uploads/2023/03/manual-actions-viewer.jpg)

So the tool was a big deal, and the SEO agency I worked at were very interested in reviewing all our customers’ reports (all good!). We were able to access these reports as we had access to these customers’ Google Webmaster Tools (as it was then called) accounts.

I decided to inspect (on my own time) the API calls behind the scenes. I initially checked if it leaked additional info about penalties – it didn’t.

So I then decided to sanity check that I couldn’t access reports for sites that I shouldn’t have access to.

The payload that went to the API looked like this:

![](https://www.tomanthony.co.uk/blog/wp-content/uploads/2023/03/payload1.png)

I’ve highlighted the obviously interesting part. Utilising my elite level hacking ðŸ˜‰ skills I replayed the request but updated the it to look like this:

![](https://www.tomanthony.co.uk/blog/wp-content/uploads/2023/03/payload2-1.png)

Shockingly — **IT WORKED**. I could put any domain name there and I could view the penalties associated with that domain. It appeared there was no authorisation being done at all — a serious and surprising oversight by Google.

![](https://www.tomanthony.co.uk/blog/wp-content/uploads/2023/03/manual-actions-tool.jpg)

In the hands of a black-hat SEO, these were the key to the castle, as you could now target negative SEO attacks at your competitors to amplify existing penalties they had. It would have been very difficult for victims of such a targeted attack to recover.

I immediately reported the issue to Google. I reported it to both their bug bounty program (my introduction to bug bounty), and I emailed the infamous Matt Cutts (who replied in less than 15 minutes and was very grateful and very nice about the whole thing). Within a few hours they had pulled the tool down, blaming a ‘snag’:

![](https://www.tomanthony.co.uk/blog/wp-content/uploads/2023/03/manual-actions-viewer2.jpg)

It came back online after the weekend, but without any explanation of why it had been taken down. I have since spoken about this at conferences, but never written about it publicly.

Google paid me $5000 under their bug bounty program, and thus I was introduced to the world of bug bounties. I went on to [hack Google’s core search functionality](https://www.tomanthony.co.uk/blog/google-xml-sitemap-auth-bypass-black-hat-seo-bug-bounty/), and found Zoom didn’t rate limit their numeric meeting passwords in my efforts to [join Boris Johnson’s cabinet meeting](https://www.tomanthony.co.uk/blog/zoom-security-exploit-crack-private-meeting-passwords/).

Thanks for reading! You can follow me on Twitter here: [@TomAnthonySEO](https://twitter.com/TomAnthonySEO/).
