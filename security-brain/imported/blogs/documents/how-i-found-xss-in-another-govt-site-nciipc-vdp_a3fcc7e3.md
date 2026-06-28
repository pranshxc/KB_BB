---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2024-05-09_how-i-found-xss-in-another-govt-site-nciipc-vdp-.md
original_filename: 2024-05-09_how-i-found-xss-in-another-govt-site-nciipc-vdp-.md
title: 'How I Found XSS In Another Govt. Site :: NCIIPC VDP !!'
category: documents
detected_topics:
- sso
- idor
- xss
- command-injection
- rate-limit
tags:
- imported
- documents
- sso
- idor
- xss
- command-injection
- rate-limit
language: en
raw_sha256: a3fcc7e31205b1716095b64a29e6e45f65d322cecc4b5e5b5ec33be4ca92210f
text_sha256: bc02477e9f3501aad166a69e40e766e283bfceade64c637f302ee8c4b453f9d5
ingested_at: '2026-06-28T07:32:33Z'
sensitivity: unknown
redactions_applied: false
---

# How I Found XSS In Another Govt. Site :: NCIIPC VDP !!

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2024-05-09_how-i-found-xss-in-another-govt-site-nciipc-vdp-.md
- Source Type: markdown
- Detected Topics: sso, idor, xss, command-injection, rate-limit
- Ingested At: 2026-06-28T07:32:33Z
- Redactions Applied: False
- Raw SHA256: `a3fcc7e31205b1716095b64a29e6e45f65d322cecc4b5e5b5ec33be4ca92210f`
- Text SHA256: `bc02477e9f3501aad166a69e40e766e283bfceade64c637f302ee8c4b453f9d5`


## Content

---
title: "How I Found XSS In Another Govt. Site :: NCIIPC VDP !!"
url: "https://medium.com/@p.ra.dee.p_0xx01/how-i-found-xss-in-another-govt-site-nciipc-vdp-84d78c0319c2"
authors: ["Professor0xx01"]
programs: ["NCIIPC"]
bugs: ["XSS", "Components with known vulnerabilities"]
publication_date: "2024-05-09"
added_date: "2024-05-08"
source: "pentester.land/writeups.json"
original_index: 294
scraped_via: "browseros"
---

# How I Found XSS In Another Govt. Site :: NCIIPC VDP !!

How I Found XSS In Another Govt. Site :: NCIIPC VDP !!
Professor.0xx01
Follow
3 min read
·
May 10, 2024

94

Press enter or click to view image in full size

Hello Fellow Hunters !! Hope you all are well !!

Intro: I am p_ra_dee_p whom you all know as Professor0xx01. Today I am gonna to explain you my story about finding XSS Bug in an another govt. website. So, let’s jump into it……..

Bug :: Cross Site Scripting (XSS) :: MEDIUM

CVSS score : 5.4 :- CVSS:3.1/AV:N/AC:L/PR:L/UI:R/S:C/C:L/I:L/A:N

Let’s say the target is target.gov.in. I have already collected the domains during subdomain enumeration phase. While surfing different websites & seeing wappalyzer, one thing caught my eyes that the site it using rich text editor framework named “CKEditor”. (Which is known to me before)

CKEditor

After seeing that, i remembered that i have already tested this “CKEditor” — web text editor before in another hunting. See about my writeup about it : XSS IN CKEditor — By Professor0xx01.

So, let’s make start a directory enumeration using dirsearch & see if my guesses are right or not ..??

dirsearch -u https://target.com -x 404,403
Press enter or click to view image in full size

I got that endpoint but not the text editor accordingly………….!!

Then i moved to my another writeup (XSS IN CKEditor — By Professor0xx01.) & searched the endpoint as follows ,, to check wheather the CKEditor page actually exist or not…!!! And yayyyhhhhh………………… I got that juicy html page ………….!!!!!

Get Professor.0xx01’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

The Juicy endpoint :

https://<target>.gov.in/ckeditor/samples/plugins/htmlwriter/outputhtml.html 
Press enter or click to view image in full size

Now I quickly Inserted my XSS Payload to this page & Got the Alert () !!

Xss<!--{cke_protected} --!><img src=x onerror=alert(`Professor0xx01`)> -->Attack

Steps To Reproduce :

First click on source ….
Give the malicious payload …..
Then click again on source !!
You will got that alert ().
Press enter or click to view image in full size

Getting that alert(),, I feel like……………………………………. this 👇👇 !!

Then I made a report about that vulnerability/issue & mailed it to the NCIIPC Team !!

THANKS FOR READING !!

Hope you enjoyed it !! If you like, then clap & follow me for more insightful articles !!

That’s it for this article now !!

Happy Hunting ~~

Keep Growing & Keep Securing ~~
