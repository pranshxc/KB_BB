---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-07-31_how-i-escalate-my-self-stored-xss-to-account-takeover-with-the-help-of-idor.md
original_filename: 2021-07-31_how-i-escalate-my-self-stored-xss-to-account-takeover-with-the-help-of-idor.md
title: How I escalate my Self-Stored XSS to Account Takeover with the help of IDOR
category: documents
detected_topics:
- xss
- idor
- command-injection
- csrf
tags:
- imported
- documents
- xss
- idor
- command-injection
- csrf
language: en
raw_sha256: eb6711cd1c55c536993f88a64c4429674935c783bc774796d2144599f9c55a77
text_sha256: 0a539101960eb8c77bb205f532dc0e4f451379d9786f7b434aa095ca0afb53e1
ingested_at: '2026-06-28T07:32:07Z'
sensitivity: unknown
redactions_applied: false
---

# How I escalate my Self-Stored XSS to Account Takeover with the help of IDOR

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-07-31_how-i-escalate-my-self-stored-xss-to-account-takeover-with-the-help-of-idor.md
- Source Type: markdown
- Detected Topics: xss, idor, command-injection, csrf
- Ingested At: 2026-06-28T07:32:07Z
- Redactions Applied: False
- Raw SHA256: `eb6711cd1c55c536993f88a64c4429674935c783bc774796d2144599f9c55a77`
- Text SHA256: `0a539101960eb8c77bb205f532dc0e4f451379d9786f7b434aa095ca0afb53e1`


## Content

---
title: "How I escalate my Self-Stored XSS to Account Takeover with the help of IDOR"
url: "https://gonzx.medium.com/how-i-escalate-my-self-stored-xss-to-account-takeover-with-the-help-of-idor-f20733ecdbe9"
authors: ["Jefferson Gonzales (@gonzxph)"]
programs: ["HackerEarth"]
bugs: ["Self-XSS", "IDOR", "Account takeover"]
publication_date: "2021-07-31"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3459
scraped_via: "browseros"
---

# How I escalate my Self-Stored XSS to Account Takeover with the help of IDOR

How I escalate my Self-Stored XSS to Account Takeover with the help of IDOR
Jefferson Gonzales
Follow
2 min read
·
Jul 31, 2021

204

1

Good day to all Security Researchers and Bug Hunters again Im Jefferson Gonzales and today I will share my writeup about my findings on HackerEarth and how I got a SWAG from them, so without wasting your time lets begin

First step is recon, so I collected all the subdomains of HackerEarth then I check it all manually and one of their subdomain caught my attention, sorry but I can’t disclose the subdomain, so lets name it test.hackerearth.com

Get Jefferson Gonzales’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

In test.hackerearth.com you can Signin and Signup, first I signup and redirect me to Dashboard area, then I hunt for CSRF but I found nothing then I try to change my Name to XSS payload and to my surprise XSS triggered, Im very excited to report it but I found out its a Self XSS. How I know? its very simple in test.hackerearth.com theirs no function to view other users profile only you can see your profile thats why its a Self XSS

I hunt another vulnerability to escalate my Self XSS to critical impact, then I review my burp suite history and I found this POST request when I change my name

POST /api/sprint/v1/setup-profile/ HTTP/2
Host: test.hackerearth.com
Origin: https://test.hackerearth.com
Referer: https://test.hackerearth.com/auth/setup-profile
Te: trailers
Connection: close

first_name=</script><svg/onload=alert(1)>&last_name=Tanga&email=attacker@gmail.com

As you can see my email was also there in the POST request, what if I change that to victims email?

So I created a new account, and I change the email on the POST request that I got earlier with my new account

POST /api/sprint/v1/setup-profile/ HTTP/2
Host: test.hackerearth.com
Origin: https://test.hackerearth.com
Referer: https://test.hackerearth.com/auth/setup-profile
Te: trailers
Connection: close

first_name=</script><svg/onload=alert(1)>&last_name=Tanga&email=victim@gmail.com

Press enter or click to view image in full size

then Viola! the XSS triggered on my new account, all you need is the email of your victim to takeover any accounts on test.hackerearth.com

After the issue was fixed

Reported date: July 4, 2021
Initial reply: July 5, 2021
Issue fixed: July 23, 2021

You can contact me on

https://twitter.com/gonzxph

https://www.linkedin.com/in/gonzxph
