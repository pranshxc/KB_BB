---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-06-01_information-disclosure-and-reflected-xss-on-tokopedia.md
original_filename: 2020-06-01_information-disclosure-and-reflected-xss-on-tokopedia.md
title: Information disclosure and reflected XSS on Tokopedia
category: documents
detected_topics:
- xss
- access-control
- ssrf
- command-injection
- path-traversal
- rate-limit
tags:
- imported
- documents
- xss
- access-control
- ssrf
- command-injection
- path-traversal
- rate-limit
language: en
raw_sha256: 39874a8815bdcc521806cbb0c6e71d028feed113a7277ff83c6d1f08d09cc041
text_sha256: a0dcb4e4e4510367cca0f3af9b02661cc05420bcb97da21f369c684760b720a4
ingested_at: '2026-06-28T07:32:02Z'
sensitivity: unknown
redactions_applied: false
---

# Information disclosure and reflected XSS on Tokopedia

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-06-01_information-disclosure-and-reflected-xss-on-tokopedia.md
- Source Type: markdown
- Detected Topics: xss, access-control, ssrf, command-injection, path-traversal, rate-limit
- Ingested At: 2026-06-28T07:32:02Z
- Redactions Applied: False
- Raw SHA256: `39874a8815bdcc521806cbb0c6e71d028feed113a7277ff83c6d1f08d09cc041`
- Text SHA256: `a0dcb4e4e4510367cca0f3af9b02661cc05420bcb97da21f369c684760b720a4`


## Content

---
title: "Information disclosure and reflected XSS on Tokopedia"
page_title: "The forgotten content : information disclosure and reflected XSS on Tokopedia | by accalon | InfoSec Write-ups"
url: "https://medium.com/bugbountywriteup/information-disclosure-and-reflected-xss-on-tokopedia-1b3a00ec64c6"
authors: ["wis4nggeni"]
programs: ["Tokopedia"]
bugs: ["Reflected XSS", "Information disclosure"]
publication_date: "2020-06-01"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4537
scraped_via: "browseros"
---

# Information disclosure and reflected XSS on Tokopedia

The forgotten content : information disclosure and reflected XSS on Tokopedia
accalon
Follow
4 min read
·
Jun 1, 2020

344

1

Tl;dr : how i found a ‘should be deleted’ content that disclose some sensitive information and vulnerable to reflected XSS on Tokopedia’s website. Blocked by login/pay wall? Read for free here : (https://c2a.github.io/information-disclosure-and-reflected-XSS-on-Tokopedia).

…

Greetings.

On my previous write-up about subdomain takeover on Tokopedia, I mentioned that i also found another interesting subdomain, one of them is accounts-REDACTED.tokopedia.com.

Because of the interesting subdomain name, i decided to dig some more in this particular subdomain. Well, the front page only shows 410 Gone http code and nothing else, so it means that the resource on this subdomain has been intentionally removed and it should be purged.

I didn’t stop there, i used some tools for directory brute-force, dirbuster, dirsearch, etc. and all the brute-forced path returns 410 Gone, except this one path, accounts-REDACTED.tokopedia.com/docs/, which returns different response, a 200 OK http code.

I opened the path on my browser, but it returns 410 Gone.

Press enter or click to view image in full size

I’m pretty sure it’s not a false-positive. After double checking, turns out that it’s served on different port. Port 80 (http) returns 200 OK, while port 443 (https)returns 410 Gone, and my browser automatically redirect to https if i don’t specify it directly.

So i open the path using http protocol and i noticed that the /docs/ path on port 80 is an API documentation using Swagger UI, an open source project to visually render documentation for an API defined with the OpenAPI (Swagger) Specification.

Press enter or click to view image in full size

Surprisingly, it contains some sensitive API like retrieving user data, and other sensitive PII like National Identity Number, etc. and it was meant for third party partner of Tokopedia. It even contains the client ID and Client secrets for Authorization.

BUT, after i check it out, the API isn’t working anymore. Actually, on my previous experience hunting on Tokopedia, they‘re using GraphQL now, different from this one i found. I checked the changelog, and last update from their staffs are from around Juny 2019. I was late, 2 months late and they’ve changed their web architecture. The 410 Gone status code makes sense now, this resource was supposed to be deleted, but still there somehow.

Press enter or click to view image in full size

So i started hunting for CVE in this particular version of Swagger UI. I actually found one XSS CVE, but after i try it, yet another disappointment, it’s not working.

It got me really curious, why is it not working? because this version supposed to be vulnerable. After some more digging, i think they’ve customized this swagger UI, they even put some credit of their staff’s name on the partially exposed source code. So maybe, this swagger UI is different from the official version.

Get accalon’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

BUT I‘M NOT GIVING UP — Well, actually i did take a break from this case for about 2 weeks.

After that I started to dug more. I noticed that this documentation is open, means anyone can modify or update the documentation without having to login or register. I actually accidentally deleted the whole documentation once, but fortunately i can download the past data from the changelog and import it again.

I found this interesting URL from import functionality :

http://accounts-REDACTED.tokopedia.com/docs/index.php?url=file.yaml

I tried to look for LFI and SSRF on the url parameter, nothing works. But i noticed that the file name is reflected on the html page, so i tried to insert XSS payload, yet another disappointment, no pop up appear.

But when I did inspect element to check the reflected result, turns out that the XSS is actually fired, but blocked by Chrome’s XSS auditor. It works perfectly on another browser like Firefox etc.

Press enter or click to view image in full size

The final payload looks like this:

http://accounts-REDACTED.tokopedia.com/docs/index.php?url=[‘<script>alert(document.cookie)</script>’]

I tried this on the latest version of Swagger UI, but it’s not working, and I can’t find any CVE documenting this vulnerability on older version. So maybe I’m right, their version is already customized (or maybe nobody assign a CVE yet? or I missing something here ¯\_(ツ)_/¯ ).

Anyway I reported this to their security team and got response 20 minutes later told me that this report is verified with medium severity. Pretty good response time.

Thanks.

Timeline:

August 29 2019: Report sent.
August 29 2019: Security team verified the report, valid with Medium Severity.
September 17 2019: Bug fixed, they asked me to re-test the bug.
November 20 2019: $$$ awarded.

NB: Pardon me for the excessive use of Memes, we need more smile in this hard situation. Stay safe and wash your hands! :D
