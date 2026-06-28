---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2015-09-24_open-redirect-in-linkedin-and-yahoo.md
original_filename: 2015-09-24_open-redirect-in-linkedin-and-yahoo.md
title: Open Redirect in Linkedin and Yahoo
category: documents
detected_topics:
- mobile-security
- command-injection
- automation-abuse
tags:
- imported
- documents
- mobile-security
- command-injection
- automation-abuse
language: en
raw_sha256: 35738dda909c088eee1bfccbce386a8e3a08522c0e8fbbbcce742a5bdf5c76f2
text_sha256: 0057ddbb1c970c8f5f0757ebc4b06277baf09b6c774cdee350a3b7400c954085
ingested_at: '2026-06-28T07:31:55Z'
sensitivity: unknown
redactions_applied: false
---

# Open Redirect in Linkedin and Yahoo

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2015-09-24_open-redirect-in-linkedin-and-yahoo.md
- Source Type: markdown
- Detected Topics: mobile-security, command-injection, automation-abuse
- Ingested At: 2026-06-28T07:31:55Z
- Redactions Applied: False
- Raw SHA256: `35738dda909c088eee1bfccbce386a8e3a08522c0e8fbbbcce742a5bdf5c76f2`
- Text SHA256: `0057ddbb1c970c8f5f0757ebc4b06277baf09b6c774cdee350a3b7400c954085`


## Content

---
title: "Open Redirect in Linkedin and Yahoo"
url: "https://medium.com/@r0t1v/open-redirect-in-linkedin-and-yahoo-a3ffd2a9cc48"
authors: ["Vitor “r0t” Oliveira (@r0t1v)"]
programs: ["LinkedIn", "Yahoo! / Verizon Media"]
bugs: ["Open redirect"]
publication_date: "2015-09-24"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 6331
scraped_via: "browseros"
---

# Open Redirect in Linkedin and Yahoo

Open Redirect in Linkedin and Yahoo
Vitor “r0t1v” Oliveira
Follow
3 min read
·
Sep 24, 2015

8

At our company we had a pentesting job to a Node.js web application. After some research I found https://nodesecurity.io, a great website with node.js vulnerabilities. Since the web app from our client was using express.js, the next thing was to look for vulnerabilities to express.js.

And this is what I found, https://nodesecurity.io/advisories/serve-static-open-redirect, a vulnerability found by Pierre-Élie Fauché:

“When using serve-static middleware version < 1.7.2 and it’s configured to mount at the root it creates an open redirect on the site.

For example: If a user visits http://example.com//www.google.com/%2e%2e they will be redirected to //www.google.com/%2e%2e, which some browsers interpret as http://www.google.com/%2e%2e.”

P.S: This vulnerability doesn’t work in Google Chrome but works in Firefox and Opera.

I tested in my client’s app and it was vulnerable.

After a couple of days me, @fabiopirespt and @fjreis decided to search for top websites using express.js and we found 2 websites from Yahoo and the mobile website from Linkedin.

Time to test them!

We started with Linkedin’s mobile website:

https://touch.www.linkedin.com

Get Vitor “r0t1v” Oliveira’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Issuing the request in burp suite we found that it was not working with two slashes (as Pierre describes in his vulnerability), so we tested with 4 slashes and this is what we got:

Press enter or click to view image in full size
Request and Response from touch.www.linkedin.com

Open redirect, yey!

Proof of Concept

Android: https://vimeo.com/126193891
iOS: https://vimeo.com/126193892

Report timeline:
April 28, 2015 — Bug reported to Linkedin
April 28, 2015 — Confirmation from Linkedin’s security team
May 28, 2015 — Pinged Linkedin team
May 28, 2015 — Bug fixed
September 24, 2015 — Public disclosure

Now the story with Yahoo is more fun. We found two websites from Yahoo using express.js:

developer.yahoo.com and publish.yahoo.com

Press enter or click to view image in full size
Request and Response from developer.yahoo.com
Press enter or click to view image in full size
Request and Response from publish.yahoo.com
Proof of Concept

Android: https://vimeo.com/126305222
iOS: https://vimeo.com/126320994
Android: https://vimeo.com/126305223

Since Yahoo is using HackerOne and open redirects are out of scope, we contacted Yahoo by email.

Report timeline:
May 28, 2015 — Bug reported to Yahoo
May 28, 2015 — Yahoo’s security team tells to report in HackerOne
May 28, 2015 — Bug reported to HackerOne
May 28, 2015 — Response from HackerOne: “Thank you for your submission to Yahoo! We are aware of this functionality on our site and it is working as designed. Open redirects have been out of scope since January 1st, 2014. Please continue to send us vulnerability reports!”
September 24, 2015 — Public disclosure

Both websites are still vulnerable.
