---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-12-28_unauthorized-sign-up-on-subdomain-of-subdomain-leading-to-organization-takeover-.md
original_filename: 2022-12-28_unauthorized-sign-up-on-subdomain-of-subdomain-leading-to-organization-takeover-.md
title: Unauthorized Sign-up on Subdomain of Subdomain leading to Organization takeover
  worth $2000
category: documents
detected_topics:
- rate-limit
- api-security
- idor
- command-injection
- otp
tags:
- imported
- documents
- rate-limit
- api-security
- idor
- command-injection
- otp
language: en
raw_sha256: 120ba629cdab009a7bc7513a134858149775bb436a7c7cab153b5bff4b6422aa
text_sha256: a430efb29fd6e7f9bc82f0261ca3c4e12bd8c1605c4121b630baa534772dfb72
ingested_at: '2026-06-28T07:32:16Z'
sensitivity: unknown
redactions_applied: false
---

# Unauthorized Sign-up on Subdomain of Subdomain leading to Organization takeover worth $2000

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-12-28_unauthorized-sign-up-on-subdomain-of-subdomain-leading-to-organization-takeover-.md
- Source Type: markdown
- Detected Topics: rate-limit, api-security, idor, command-injection, otp
- Ingested At: 2026-06-28T07:32:16Z
- Redactions Applied: False
- Raw SHA256: `120ba629cdab009a7bc7513a134858149775bb436a7c7cab153b5bff4b6422aa`
- Text SHA256: `a430efb29fd6e7f9bc82f0261ca3c4e12bd8c1605c4121b630baa534772dfb72`


## Content

---
title: "Unauthorized Sign-up on Subdomain of Subdomain leading to Organization takeover worth $2000"
url: "https://infosecwriteups.com/unauthorized-sign-up-on-subdomain-of-subdomain-leading-to-organization-takeover-worth-2000-a7199952d80b"
authors: ["Manav Bankatwala (@ManavBankatwala)"]
bugs: ["Exposed registration page"]
bounty: "2,000"
publication_date: "2022-12-28"
added_date: "2022-12-30"
source: "pentester.land/writeups.json"
original_index: 1724
scraped_via: "browseros"
---

# Unauthorized Sign-up on Subdomain of Subdomain leading to Organization takeover worth $2000

Unauthorized Sign-up on Subdomain of Subdomain leading to Organization takeover worth $2000
Manav Bankatwala
Follow
5 min read
·
Dec 28, 2022

374

2

Hello people, Here I am sharing another four digit write-up which is one of my very old finding. If you haven’t read my previous writeup about how I was able to bypass a strong rate limit mechanism on all the endpoints then here is the link to it:

Unique Rate limit bypass worth 1800$
Proving the organization statement wrong with OOS Rate limit bypass.

medium.com

Starting with the initial phase.

Lots of people were confused with the title when I initially posted about this bug. So here is the complete writeup and methodology that I used. At the time I discovered this bug I had just started my bug bounty journey after reading many E-books and write-ups.

I decided to choose a target randomly to which I got to know that only mentioned domains and subdomains were in scope. All the other subdomains were considered as Out of Scope. They also mentioned in their policy that *.target.com is out of scope but target.com was in scope. This is because the company was actually providing some kind of services to their clients which allows them to make their customize subdomains like client1.target.com,client2.target.com. Due to this they restricted to test on any of the subdomains. So what to do when this type of target crosses our brain? The first thought came into my mind was that maybe I should try to find any critical vulnerability on their subdomains as not so many researchers have checked due to their policy.

The first thing I did was to find subdomains but not with our normal method. Instead I used subdomain enumeration wordlist which contained words like app,development,dev,service,app-dev etc.

Very limited subdomains were extracted using this method and out of them, one subdomain was like services.target.com. On visiting this subdomain it showed a DNS error but still I don’t know how this got detected in subdomain enumeration phase. Next thing I tried to use google dork i.e. site:*.services.target.com where I found some results from domains like public.services.target.com etc.

You must have observed that the subdomain contains word “services” which may indicate that there are some more services running on this subdomain. Next thing I extracted subdomains for the domain “services.target.com”. Interestingly I found a subdomain “sserver.services.target.com”.

What content was present on this subdomain?

This page contains a normal login page and upon observing UI, I guessed that it was used to manage source codes and other things by directly giving access to the github account.

Press enter or click to view image in full size

So maybe this login portal was meant for employees and only employees are given credentials to access further. Now I was just wondering what to do next, Search for JS files, use github dorks for credentials leak etc. but nothing interesting came as this domain was not mentioned anywhere.

Here comes the interesting part!

I observed the URL which was “/sign-in?returnTo=%2F”. And tried to change the “sign-in” to other URLs like “register”, ”get-started” and simply “sign-up” showed me a signup page asking for email, username and password.

Press enter or click to view image in full size

Still I was in doubt that after clicking on register, it may show error that sign-up is not possible just like JIRA. But guess what? It allowed me to signup using my email and I was successful in signing into account.

Get Manav Bankatwala’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Now next task was to see what access we have and what sensitive information we can see. And I was not able to believe my eyes, They were using this server portal to manage all of their github codes. Even the private repositories. Any new users were given direct access to all the codes shared on this portal.

Press enter or click to view image in full size
Normally it was a private repository if directly accessed through github

Now when I tried to access the same repo from the portal, then it was easily accessible and I was able to see all the credentials as well as any secret files.

Press enter or click to view image in full size
Secrets file containing some secret tokens

All of their private repository were accessible and all of their secret API keys, and admin account credentials were visible. It was a complete organization takeover. As they were providing services to many clients, all of their client data was also accessible through these exposed credentials.

I immediately created a report and the team triaged and fixed this report within 40mins making the portal inaccessible from public view. Also they rotated any credentials exposed. They rewarded me with their highest payout for critical i.e. 2000$

TIP: Even if something is not in scope, give it a try. Don’t try aggressive testing but still look for any critical vulnerabilities.

Look even for subdomains of subdomain if you feel any suspicious subdomains running.

Look for any endpoints that may contain words like “services”, “internal” etc. and look for any open services available.

That’s it guys, I hope you liked it and do share if you found it helpful.

Follow me to get latest updates:

https://www.linkedin.com/in/manavbankatwala/

https://www.instagram.com/manav.bug/

https://twitter.com/manavbankatwala

From Infosec Writeups: A lot is coming up in the Infosec every day that it’s hard to keep up with. Join our weekly newsletter to get all the latest Infosec trends in the form of 5 articles, 4 Threads, 3 videos, 2 GitHub Repos and tools, and 1 job alert for FREE!
