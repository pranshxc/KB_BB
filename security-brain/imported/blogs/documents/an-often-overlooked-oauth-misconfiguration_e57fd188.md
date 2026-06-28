---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-11-01_an-often-overlooked-oauth-misconfiguration.md
original_filename: 2020-11-01_an-often-overlooked-oauth-misconfiguration.md
title: An often overlooked Oauth misconfiguration.
category: documents
detected_topics:
- oauth
- access-control
- command-injection
- otp
- csrf
tags:
- imported
- documents
- oauth
- access-control
- command-injection
- otp
- csrf
language: en
raw_sha256: e57fd18869856bf63b7b3aab5abb3675029801f9684afd6ecb1f2ae433540e1e
text_sha256: 4961e472dc3b729e200d683e3d6fd90b2fa9c30c5447eacf88229da059bea5ad
ingested_at: '2026-06-28T07:32:03Z'
sensitivity: unknown
redactions_applied: false
---

# An often overlooked Oauth misconfiguration.

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-11-01_an-often-overlooked-oauth-misconfiguration.md
- Source Type: markdown
- Detected Topics: oauth, access-control, command-injection, otp, csrf
- Ingested At: 2026-06-28T07:32:03Z
- Redactions Applied: False
- Raw SHA256: `e57fd18869856bf63b7b3aab5abb3675029801f9684afd6ecb1f2ae433540e1e`
- Text SHA256: `4961e472dc3b729e200d683e3d6fd90b2fa9c30c5447eacf88229da059bea5ad`


## Content

---
title: "An often overlooked Oauth misconfiguration."
url: "https://dragon-sec.medium.com/an-often-overlooked-oauth-misconfiguration-7d2d441eae1f"
authors: ["VipItHunter (@VipItHunter1)"]
bugs: ["OAuth"]
publication_date: "2020-11-01"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4165
scraped_via: "browseros"
---

# An often overlooked Oauth misconfiguration.

An often overlooked Oauth misconfiguration.
VipItHunter
Follow
2 min read
·
Nov 2, 2020

29

1

Good afternoon.

Today I will not tell you about typical vulnerabilities in oauth: there is no csrf check, you can change the redirect_uri, and so on. You can easily find all this on the Internet, because many articles have been written about this.

I want to tell you about a feature that I very often meet in popular private programs. I want to say right away that you should have at least a basic understanding of oauth.

Sorry in advance for my english.

So, let’s say you have oauth on your project.

Press enter or click to view image in full size

As you can see, this project uses authorization via ok.ru (a popular Russian social network).

Get VipItHunter’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Let’s now look at the request:

Press enter or click to view image in full size

As you can see, the developer made two mistakes here that will have a significant impact.

The developer made an intermediate link like https://www.example.com/auth/ok/
The developer did not add the csrf token to this request, because he thinks that state token will “protect him”.

Next, I give you 5 minutes to think about what this misconfiguration can lead to?

*5 minutes pass :3*

So, if you are a seasoned hacker, then you know that 99.9% of companies do not pay for csrf login / logout, and ok.ru is among these companies.

The complete execution plan for this vulnerability.

1) The victim logs in under our ok.ru account
2) We load this link into an iframe https://www.example.com/auth/ok/ on the victim’s side. Since we have already opened access to this project to our account through oauth, confirmation is not required.
3) The victim is linked to our ok.ru account
4) We enter the vulnerable site through ok.ru

I will attach the full payload in my twitter. VipItHunter1

For this vulnerability to lead to account hijacking, the project must have 2 vulnerabilities.
1) Uses oauth with intermediate link and without csrf token
2) There are social networks like ok.ru that do not pay for csrf login/unlogin.

If you have any questions, please ask me on Twitter.
