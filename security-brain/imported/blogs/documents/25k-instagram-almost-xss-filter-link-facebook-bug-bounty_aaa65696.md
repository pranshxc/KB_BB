---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-09-20_25k-instagram-almost-xss-filter-link-facebook-bug-bounty.md
original_filename: 2020-09-20_25k-instagram-almost-xss-filter-link-facebook-bug-bounty.md
title: $25K Instagram Almost XSS Filter Link — Facebook Bug Bounty
category: documents
detected_topics:
- xss
- command-injection
tags:
- imported
- documents
- xss
- command-injection
language: en
raw_sha256: aaa65696c959c1a77fc9044dba3deaa79fc71bbaa68cb9da0122b0b47ac634a1
text_sha256: ad95c3974871151b2fd01f659ca7431f9c8904dab00660a5fa6d0e598b9b429c
ingested_at: '2026-06-28T07:32:03Z'
sensitivity: unknown
redactions_applied: false
---

# $25K Instagram Almost XSS Filter Link — Facebook Bug Bounty

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-09-20_25k-instagram-almost-xss-filter-link-facebook-bug-bounty.md
- Source Type: markdown
- Detected Topics: xss, command-injection
- Ingested At: 2026-06-28T07:32:03Z
- Redactions Applied: False
- Raw SHA256: `aaa65696c959c1a77fc9044dba3deaa79fc71bbaa68cb9da0122b0b47ac634a1`
- Text SHA256: `ad95c3974871151b2fd01f659ca7431f9c8904dab00660a5fa6d0e598b9b429c`


## Content

---
title: "$25K Instagram Almost XSS Filter Link — Facebook Bug Bounty"
url: "https://medium.com/@alonnsoandres/25k-instagram-almost-xss-filter-link-facebook-bug-bounty-798b10c13b83"
authors: ["Andres Alonso (@al0nnso)"]
programs: ["Meta / Facebook"]
bugs: ["Stored XSS"]
bounty: "25,000"
publication_date: "2020-09-20"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4249
scraped_via: "browseros"
---

# $25K Instagram Almost XSS Filter Link — Facebook Bug Bounty

Top highlight

$25K Instagram Almost XSS Filter Link — Facebook Bug Bounty
Andres Alonso
Follow
3 min read
·
Sep 20, 2020

1.8K

5

Hii, I’m Andres Alonso, Brazilian 14 years old. Today I am going explain how I accidentally found a critical stored XSS when I was making an Instagram integrated app.

Sometimes I work on my app to make Instagram filters by mobile, to make a functionality of my app I needed to understand how the Spark AR facebook filter creator app generates the filter links to test the filter on the smartphone.

Press enter or click to view image in full size
Press enter or click to view image in full size

When I generate the filter link the first request sent sets the name, file type, and size of the filter .arexport file.

Normally the default name of the preview is preview.arexport and not can be changed by the Spark AR app, because this I wanted to see more closely.

When I changed the name the filter test notification changed too, so with this, I tried to make more, I tried to make a code injection XSS or something in the Instagram app but without success.

so this changed when I had the idea to see in the desktop app, the filter not load obviously and the name not is shown in the page…

Press enter or click to view image in full size

but not, when I searched the name of the filter on the page I found two meta tags with the filter name in the content

Press enter or click to view image in full size

so with this, I tried an XSS with the allowed characters, I couldn’t use the open of an HTML code but I can use the double quotes to close the content.

Press enter or click to view image in full size

All my tentatives to make an XSS fail because the meta tag is so limited and I can only close the double quotes, but I tried to make an open redirect, to make this I encoded the URL in HTML encoding to bypass the filter.

http:&#x2F;&#x2F;www.evilzone.com

and put in this payload to redirect to the URL

0;url=http:&#x2F;&#x2F;www.evilzone.com"HTTP-EQUIV="refresh"any=".arexport

and… THIS WORKS the user is redirect to the another page… but where's the XSS?

Get Andres Alonso’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

If you use “javascript:” before the url the script will be executed

but… only on specific browsers with specific versions

and i reported the Open Redirect citing a possible xss in some browsers

Press enter or click to view image in full size

After the report, the Facebook Security Team rated this as can be escalated to an XSS.

Press enter or click to view image in full size

I believe it happened because I can’t open the HTML code, but I can close this so with this I found some payloads that change the charset of the page and add code with another charset type bypassing the filter:

<meta charset="x-imap4-modified-utf7">&ADz&AGn&AG0&AEf&ACA&AHM&AHI&AGO&AD0&AGn&ACA&AG8Abg&AGUAcgByAG8AcgA9AGEAbABlAHIAdAAoADEAKQ&ACAAPABi

I have to thank Facebook for make a little push in my report escalating to an XSS

Thank you for reading the article to the end and if you want you can follow me on instagram or twitter!
