---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-07-26_apple-hall-of-fame-for-a-small-misconfiguration-unauth-cache-purging.md
original_filename: 2021-07-26_apple-hall-of-fame-for-a-small-misconfiguration-unauth-cache-purging.md
title: Apple Hall Of Fame for a Small Misconfiguration || Unauth Cache Purging
category: documents
detected_topics:
- command-injection
tags:
- imported
- documents
- command-injection
language: en
raw_sha256: d845ef647000d10128469c8dc2aafcecca901309c43fe0bc6b881c93b62abc18
text_sha256: 13c9c9f9019982ee5f71734bb4eb20729dc3d8bff6bc411c5445eac532f1d6a3
ingested_at: '2026-06-28T07:32:07Z'
sensitivity: unknown
redactions_applied: false
---

# Apple Hall Of Fame for a Small Misconfiguration || Unauth Cache Purging

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-07-26_apple-hall-of-fame-for-a-small-misconfiguration-unauth-cache-purging.md
- Source Type: markdown
- Detected Topics: command-injection
- Ingested At: 2026-06-28T07:32:07Z
- Redactions Applied: False
- Raw SHA256: `d845ef647000d10128469c8dc2aafcecca901309c43fe0bc6b881c93b62abc18`
- Text SHA256: `13c9c9f9019982ee5f71734bb4eb20729dc3d8bff6bc411c5445eac532f1d6a3`


## Content

---
title: "Apple Hall Of Fame for a Small Misconfiguration || Unauth Cache Purging"
url: "https://sapt.medium.com/apple-hall-of-fame-for-a-small-misconfiguration-unauth-cache-purging-faf81b19419b"
authors: ["Prajit Sindhkar (@PrajitSindhkar)"]
programs: ["Apple"]
bugs: ["Unauthenticated cache purge"]
publication_date: "2021-07-26"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3477
scraped_via: "browseros"
---

# Apple Hall Of Fame for a Small Misconfiguration || Unauth Cache Purging

Apple Hall Of Fame for a Small Misconfiguration || Unauth Cache Purging
Prajit Sindhkar
Follow
3 min read
·
Jul 26, 2021

596

5

Hello guys👋👋 ,Prajit here from the BUG XS Team , recently I got acknowledgement for reporting a valid issue on Apple Program. So that bug is called Unauth Cache Purging. So let us take look at some of the important concepts which are important to understand the vulnerability.

What are Caches?

Caching is a process that stores multiple copies of data or files in a temporary storage location /cache, so they can be accessed faster. It temporarily saves data for software applications, servers, and web browsers, which ensures users need not download information every time they access a website or application.

Let me give you an example, so if you are visiting a website for the first time, it loads image, fonts, files, etc from the server. Now if this is being done each time you visit a website, it increases the request traffic to the server, so instead to avoid this situation, caches are used. So now whenever you are visiting a website for the first time it loads the image , fonts, etc and as well as copies these content in a file on your system. So now anytime if you visit the website again, rather than making request to server, it retrieves the information from the caches in your system itself. Hence this would be helpful to reduce traffic on server as well as on client side, website will load much faster.

Press enter or click to view image in full size
Cache Working Visual Representation-1
Press enter or click to view image in full size
Cache Working Visual Representation-2

Now, the above two images might have made it clear, what is cache, how are the used and why are the useful. Now let’s move on to the next concept…

What is Cache Purge Request?

Cache Purge means to delete the stored caches. So if you purge the cache, it means the next time you visit that website, it will generate the page by pulling info from the database (the original method). Then, it will recopy the page again to create a new cache.

The Cache Purge request, simply allows users to delete any cached resource. Now let use move to the main vulnerability…

Unauthenticated Cache Purge

Description: If the Purge request is available to any user, even those who are not authenticated, they can delete/invalidate the caches stored at certain resource. This can lead to increased bandwidth costs and degraded application performance. Allowing anonymous users to purge cache could be used to maliciously degrade performance.

Get Prajit Sindhkar’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

How to Perform: Simply give the curl command: curl -X PURGE https://target.com

If it is vulnerable it will look like this:

Vulnerable

If it is not vulnerable, it will look like this:

Not Vulnerable

Mitigation: Disallow cache purge requests or limit to authenticated users only.

Report/Reference: https://hackerone.com/reports/154278

Press enter or click to view image in full size

So this is all about this write-up, hope you liked it, if you found this informative, do not forget to clap👏 and do let me know if you have any doubts✌️.

Thanks For Reading😊

Profile Links:

Twitter: https://twitter.com/SAPT01

LinkedIn: https://www.linkedin.com/in/prajit-sindhkar-3563b71a6/

Instagram: https://instagram.com/prajit_01?utm_medium=copy_link

BUG XS Official Website: https://www.bugxs.co/
