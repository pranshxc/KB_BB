---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-04-05_weird-and-very-easy-authentication-bypass-found-with-google-dorking.md
original_filename: 2021-04-05_weird-and-very-easy-authentication-bypass-found-with-google-dorking.md
title: Weird and very easy authentication bypass found with Google dorking
category: documents
detected_topics:
- command-injection
- api-security
tags:
- imported
- documents
- command-injection
- api-security
language: en
raw_sha256: 43e2ed9a6bfcd7aad94e77e18d4dc72d6f79bdf2f28f861d3cfac4819b70e356
text_sha256: d6f02bdbbb3cd4e2adce0303649cb934d40a9a38342a9b7531ec0d11bcaa5b51
ingested_at: '2026-06-28T07:32:05Z'
sensitivity: unknown
redactions_applied: false
---

# Weird and very easy authentication bypass found with Google dorking

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-04-05_weird-and-very-easy-authentication-bypass-found-with-google-dorking.md
- Source Type: markdown
- Detected Topics: command-injection, api-security
- Ingested At: 2026-06-28T07:32:05Z
- Redactions Applied: False
- Raw SHA256: `43e2ed9a6bfcd7aad94e77e18d4dc72d6f79bdf2f28f861d3cfac4819b70e356`
- Text SHA256: `d6f02bdbbb3cd4e2adce0303649cb934d40a9a38342a9b7531ec0d11bcaa5b51`


## Content

---
title: "Weird and very easy authentication bypass found with Google dorking"
url: "https://infosecwriteups.com/weird-and-very-easy-authentication-bypass-found-with-google-dorking-c13230a038ed"
authors: ["GrumpinouT (@RVerwilghen)"]
bugs: ["Authentication bypass"]
publication_date: "2021-04-05"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3759
scraped_via: "browseros"
---

# Weird and very easy authentication bypass found with Google dorking

Weird and very easy authentication bypass found with Google dorking
GrumpinouT
Follow
3 min read
·
Apr 5, 2021

149

In this post, I will explain how I found an authentication bypass, and further explored the functionality of the website, to increase the impact of the submission.

The target had a wide scope and the main domain did not have that much functionality, so after a quick look around, I started enumerating subdomains, and Google dorking with the following search query inurl:redacted. During the Google dork I found the following domain: redacted.cloud. Then I narrowed my search query to inurl:redacted.cloud. One of the domains I found with this Google search, was a site that displayed something like “Loading data…”. I noticed the site was written in React.js, because of the well known React favicon.

After a few seconds, and before the data on the site was actually loaded, The browser redirected me to the companies login portal. Because I did not have a proper look at the site, I decided to open it again in a new tab, to have a proper look.

Get GrumpinouT’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

To my surprise, this time all data loaded and I did not get redirected to the login portal. I did not really understand why this behavior was happening, but after a little more trying, I concluded that all I had to do, to bypass the login, was open the site in a new tab. After the bypass, it’s time to explore what’s possible with this site. The site had a list of 1902 domains owned by the company, each with a a type, business owner, technical owner and legal entity field.

Via the site it was possible to edit the these fields, but it wasn’t possible to delete/add/edit domains. I decided to keep looking around, to find out if one of these actions are possible. I opened up Burp Suite, and had a look at the requests that were made when I edited the type field of a domain. The domain of which I was editing the type, was also sent in the request body, so I tried changing this to www.grumpinout.be.When I refreshed the page, my domain was present in the list.

The endpoint to edit/add a row was /update, so I tried the following endpoint /remove to try and delete my previously added row. Unfortunately, this didn’t work, but after that I tried /delete, and this time it worked! My domain was now removed from the list.

Via the site, I was able to download a list of all the domains, and one domain in that list was vulnerable for takeover.

The authentication bypass submission was marked as high severity, and fixed within 24 hours (the entire site and API were taken offline). For those of you who are interested in the bounty, I did not receive any since the program did not pay any bounties. The subdomain takeover was marked as medium.
