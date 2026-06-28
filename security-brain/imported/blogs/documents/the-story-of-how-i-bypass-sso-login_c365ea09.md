---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-01-02_the-story-of-how-i-bypass-sso-login.md
original_filename: 2022-01-02_the-story-of-how-i-bypass-sso-login.md
title: The Story Of How I Bypass SSO Login
category: documents
detected_topics:
- sso
- command-injection
tags:
- imported
- documents
- sso
- command-injection
language: en
raw_sha256: c365ea0938084a72f707236b71ef19cc15125ea417bd3a4b7a08336a815013d9
text_sha256: 5a3afb9174e670b5fccd7c461fefc09dd8ffde549ab2af610f7e1114b42de454
ingested_at: '2026-06-28T07:32:09Z'
sensitivity: unknown
redactions_applied: false
---

# The Story Of How I Bypass SSO Login

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-01-02_the-story-of-how-i-bypass-sso-login.md
- Source Type: markdown
- Detected Topics: sso, command-injection
- Ingested At: 2026-06-28T07:32:09Z
- Redactions Applied: False
- Raw SHA256: `c365ea0938084a72f707236b71ef19cc15125ea417bd3a4b7a08336a815013d9`
- Text SHA256: `5a3afb9174e670b5fccd7c461fefc09dd8ffde549ab2af610f7e1114b42de454`


## Content

---
title: "The Story Of How I Bypass SSO Login"
url: "https://systemweakness.com/the-story-of-how-i-bypass-sso-login-6b93370196cf"
authors: ["zer0d"]
bugs: ["Authentication bypass"]
publication_date: "2022-01-02"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3038
scraped_via: "browseros"
---

# The Story Of How I Bypass SSO Login

The Story Of How I Bypass SSO Login
zer0dac
Follow
3 min read
·
Jan 2, 2022

110

1

Hello everyone,

I decided to tell you my stories about offensive security. This is the first story I share on my blog. Hope it will be a good start. In these stories, of course, I can not give the company names but I will tell you how it happened and I will use sometimes example pictures or censured pictures.

I found this bug in the Hackerone platform. I chose one target and started with the first step.

Always my first step is copying the whole domain addresses from the target page and pasting it to the txt file for my bash script. For more understanding, you may check the script from here: https://github.com/zer0da/subEnum

Press enter or click to view image in full size
Eg. photo

While the bash doing his job, I started to investigate the company as usual. What their jobs are, which technologies they are using etc.

After the bash had done his job, all the subdomains were found and written to the new txt file. After then I always start my python script to parse reachable subdomains. For more understanding, you may check the script from here: https://github.com/zer0da/SubChecker

Press enter or click to view image in full size
Eg. photo

Then I started to check subdomains to detect any unusual thing. Hacking sometimes requires some Spidey Sense to find that hole. On one page, I saw that the page requires SSO login but before that, for 1 millisecond I was able to see the page behind it.

Press enter or click to view image in full size
Censured pic.

I think that was a logical issue on the website. So, I started to examine from the burp proxy.

First I tried to change methods like GET to POST, TRACE, etc.

Press enter or click to view image in full size
Eg. photo

But it didn’t work.

Get zer0dac’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Hımmm I should think in a different way.

I opened another path of the website and copied its response which returns 200 OK and reachable. Then I intercepted the SSO login page response.

Press enter or click to view image in full size
Eg. photo
Eg. photo

After then I paste copied response to this response and forward it.

KABOOM!

The page was reachable by me and I shouldn’t have access. Bug found.

Press enter or click to view image in full size
