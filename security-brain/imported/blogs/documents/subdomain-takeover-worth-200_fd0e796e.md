---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2018-09-14_subdomain-takeover-worth-200.md
original_filename: 2018-09-14_subdomain-takeover-worth-200.md
title: Subdomain Takeover worth 200$
category: documents
detected_topics:
- command-injection
tags:
- imported
- documents
- command-injection
language: en
raw_sha256: fd0e796e21ef1c932be7344b3b00c77322d831cd1f6fb7a63d710c706c86f8d3
text_sha256: 640453bb189069df80e56d017bbd68dc5cac84db16d03b7db54f3830ac96705a
ingested_at: '2026-06-28T07:31:57Z'
sensitivity: unknown
redactions_applied: false
---

# Subdomain Takeover worth 200$

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2018-09-14_subdomain-takeover-worth-200.md
- Source Type: markdown
- Detected Topics: command-injection
- Ingested At: 2026-06-28T07:31:57Z
- Redactions Applied: False
- Raw SHA256: `fd0e796e21ef1c932be7344b3b00c77322d831cd1f6fb7a63d710c706c86f8d3`
- Text SHA256: `640453bb189069df80e56d017bbd68dc5cac84db16d03b7db54f3830ac96705a`


## Content

---
title: "Subdomain Takeover worth 200$"
page_title: "Subdomain Takeover worth 200. Hi! My name is Ali and i am security… | by Ali Razzaq | Medium"
url: "https://medium.com/@alirazzaq/subdomain-takeover-worth-200-ed73f0a58ffe"
authors: ["Ali Razzaq (@AliRazzaq_)"]
programs: ["Netlify"]
bugs: ["Subdomain takeover"]
bounty: "200"
publication_date: "2018-09-14"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5702
scraped_via: "browseros"
---

# Subdomain Takeover worth 200$

Ali Razzaq
 highlighted

Ali Razzaq
 highlighted

Subdomain Takeover worth 200
Ali Razzaq
Follow
2 min read
·
Sep 14, 2018

400

3

Hi! My name is Ali and i am security researcher from Pakistan.

In this article i will explain how i takeover a subdomain which is mapped on netlify. Netlify is platform for web developers to upload their web projects and showcase to world.Netlify allow web developers to add custom domain or subdomain to their projects.

So i was searching for sites on google using some my recent google dorks.I land to a page site.com/white_hat(i am not disclosing site due to some reasons,Don’t mind :D) and i saw their scope for testing. I just open findsubdomains.com and try to get some subdomains.

Get Ali Razzaq’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

I saw a subdoamin which was like this hootsuite.site.com and while opening it is just showing “Not Found”

Press enter or click to view image in full size

I just check the CNAME record of this subdomain because CNAME will tell you on which 3rd party site the subdomain is mapped.So i got this CNAME.

I register on netlify.com and upload the web project first.Then it ask me to add custom subdomain.

Press enter or click to view image in full size

So I just add the subdomain and click on verify.

Press enter or click to view image in full size

So on few clicks the subdomain was mine :D I fully takeover the site. I uploaded a screenshot on twitter :D

After 15 minutes of reporting i got reply from their CTO and he rewarded me 200$ for this takeover.

Press enter or click to view image in full size

I hope you enjoyed this takeover and this will help you to understand how you can claim subdomain if this was not claimed before.

Thanks for reading.Keep Sharing and Happy Hunting!
