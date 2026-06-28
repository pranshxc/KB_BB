---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2018-06-12_unvalidated-open-redirect-bolcom.md
original_filename: 2018-06-12_unvalidated-open-redirect-bolcom.md
title: Unvalidated Open Redirect Bol.com
category: documents
detected_topics:
- xss
- command-injection
- cloud-security
tags:
- imported
- documents
- xss
- command-injection
- cloud-security
language: en
raw_sha256: 6342e7b0f9ed2a532dea8d3d53d3dd5c084b1d6793b079d57bc8611a17b766e5
text_sha256: c6a75cd863e7a263cc67cae0a33f8165f6cbd9faaa3a1bfc6174dd804a82473e
ingested_at: '2026-06-28T07:31:57Z'
sensitivity: unknown
redactions_applied: false
---

# Unvalidated Open Redirect Bol.com

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2018-06-12_unvalidated-open-redirect-bolcom.md
- Source Type: markdown
- Detected Topics: xss, command-injection, cloud-security
- Ingested At: 2026-06-28T07:31:57Z
- Redactions Applied: False
- Raw SHA256: `6342e7b0f9ed2a532dea8d3d53d3dd5c084b1d6793b079d57bc8611a17b766e5`
- Text SHA256: `c6a75cd863e7a263cc67cae0a33f8165f6cbd9faaa3a1bfc6174dd804a82473e`


## Content

---
title: "Unvalidated Open Redirect Bol.com"
page_title: "Unvalidated Open Redirect at Bol.com | by Jonathan Bouman | Medium"
url: "https://medium.com/@jonathanbouman/unvalidated-open-redirect-bol-com-b270151380e6"
authors: ["Jonathan Bouman (@JonathanBouman)"]
programs: ["Bol.com"]
bugs: ["Open redirect"]
bounty: "100"
publication_date: "2018-06-12"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5843
scraped_via: "browseros"
---

# Unvalidated Open Redirect Bol.com

Unvalidated Open Redirect at Bol.com
Jonathan Bouman
Follow
2 min read
·
Jun 12, 2018

201

1

Press enter or click to view image in full size
Unvalidated Open Redirect, user action required

Are you aware of any (private) bug bounty programs? I would love to get an invite. Please get in touch with me: Jonathan@Protozoan.nl

Background
In my previous blog post we found a client stored XSS bug at Amazon.com

Today we’re going to have a look at Unvalidated Redirect bugs.

If we find an open redirect we may use it to redirect users to our phishing website. People will see the legit website url, think everything is ok, click the link and are redirected to our fake login page. This is a serious issue according to the OWASP.

Bol.com is one of the biggest ecommerce websites in The Netherlands. So I thought it would be a good idea to look around their website for this flaw.

Get Jonathan Bouman’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Attack vector
After a few hours of digging I ended up with the following link:
https://banen.bol.com/quiz/?reference_url=https://s3-eu-west-1.amazonaws.com/pentesting-target/blog2-bol.com.html&reference_type=Login%20en%20solliciteer%20direct

Press enter or click to view image in full size

The reference_url from the url is used in the button as link. The reference_type is used as text in the button. If we change the parameters to an malicious url and change the text to ‘login & apply for the job’ we have the perfect combination for a phishing website; see the header image for the result

Bonus
Another open redirect is found on the affiliates subdomain, no user action is required. The malicious url will redirect immediately to our phishing website.

https://partnerprogramma.bol.com/click/click?p=1&s=13759&t=p&pid=9200000056577975&f=PDL&name=s&url=https://s3-eu-west-1.amazonaws.com/pentesting-target/blog2-bol.com.html

Unvalidated Open Redirect no user actions required

Solution
A possible solution is to whitelist Bol.com as the only domain to be allowed in redirects, or introduce some sort of a hashing system that checks if the url used is previously approved.

Timeline
09–06–2018 Found bugs, informed Bol.com
10–06–2018 Bugs confirmed by Bol.com
11–06–2018 Bugs fixed by Bol.com, rewarded 2x €50 giftcards
12–06–2018 Validated fix, blog published
