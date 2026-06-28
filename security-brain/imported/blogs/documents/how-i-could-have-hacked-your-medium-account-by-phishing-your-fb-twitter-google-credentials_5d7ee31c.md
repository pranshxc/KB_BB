---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-07-29_how-i-could-have-hacked-your-medium-account-by-phishing-your-fb-twitter-google-c.md
original_filename: 2021-07-29_how-i-could-have-hacked-your-medium-account-by-phishing-your-fb-twitter-google-c.md
title: How I could have hacked your medium account by phishing your FB, Twitter &
  Google credentials.
category: documents
detected_topics:
- oauth
- command-injection
- api-security
- cloud-security
tags:
- imported
- documents
- oauth
- command-injection
- api-security
- cloud-security
language: en
raw_sha256: 5d7ee31c365998c8fe963ed10f4f75b01acb046a5570f44e43611e4e3c2a32ec
text_sha256: 686c595907f0a43cd0ae22b92470c1519c7820756904d9c493a9c38dd1c9f53a
ingested_at: '2026-06-28T07:32:07Z'
sensitivity: unknown
redactions_applied: false
---

# How I could have hacked your medium account by phishing your FB, Twitter & Google credentials.

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-07-29_how-i-could-have-hacked-your-medium-account-by-phishing-your-fb-twitter-google-c.md
- Source Type: markdown
- Detected Topics: oauth, command-injection, api-security, cloud-security
- Ingested At: 2026-06-28T07:32:07Z
- Redactions Applied: False
- Raw SHA256: `5d7ee31c365998c8fe963ed10f4f75b01acb046a5570f44e43611e4e3c2a32ec`
- Text SHA256: `686c595907f0a43cd0ae22b92470c1519c7820756904d9c493a9c38dd1c9f53a`


## Content

---
title: "How I could have hacked your medium account by phishing your FB, Twitter & Google credentials."
url: "https://infosecwriteups.com/how-i-could-have-hacked-your-medium-account-by-phishing-your-fb-twitter-google-credentials-d53bf7096da7"
authors: ["Renganathan (@IamRenganathan)"]
programs: ["Medium"]
bugs: ["Open redirect", "OAuth"]
publication_date: "2021-07-29"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3467
scraped_via: "browseros"
---

# How I could have hacked your medium account by phishing your FB, Twitter & Google credentials.

How I could have hacked your medium account by phishing your FB, Twitter & Google credentials.
Renganathan
Follow
3 min read
·
Jul 29, 2021

285

1

Hi There,

Renganathan here.

This write-up is about the vulnerability that I found on Medium which will allow me to hack your medium account by phishing your FB, Twitter & Google credentials.

Press enter or click to view image in full size
Medium Login

YES :P

A few months ago I saw 
Pratik Dabhi
 was listed in the medium hall of fame. So I was motivated to hunt bugs on Medium. I enumerated the subdomains and stopped there because my methodologies in earlier days were very outdated and I was not good at recon.

So I thought of giving it a try again.

I started with collecting the interesting parameters with Waybackurls, ParamSpider & Gau. simultaneously I was manually exploring the site and also spider the medium with the Burp Suite.

Burp Suite Spidering

Then after some time, I was searching for the Open Redirection parameters like the below ones.

?next=
?url=
?target=
?rurl=
?dest=
?destination=
?redir=
redirect_uri=
?redirect_url=
?redirect=
/redirect/
cgi-bin/redirect.cgi?{}
/out/
/out?
?view=
/login?to=
?image_url=
?go=
?return=
?returnTo=
?return_to=
?checkout_url=

And then I noticed an awesome parameter which was:

redirect=

I was like

open redirection vro
Press enter or click to view image in full size
redirect=

But it was not just an open redirection. I changed the return path to attacker.com

Get Renganathan’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

When I clicked on Sign in with Twitter, I was redirected to attacker.com

This can lead to phish social media credentials.

TimeLine:

July 15, 2021 - Reported

July 18, 2021 - Patched by Internal Security Team

July 28, 2021 - Was asked how to get credited in humans.txt (Hall of fame)

Press enter or click to view image in full size
Was asked how to get credited in humans.txt (Hall of fame)

July 29, 2021 - Got listed in Medium Hall of fame.

Press enter or click to view image in full size

Thanks for reading :)
Stay Safe.

https://www.instagram.com/renganathanofficial/
