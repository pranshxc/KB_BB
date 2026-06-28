---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-09-11_how-i-found-my-first-aem-related-bug.md
original_filename: 2021-09-11_how-i-found-my-first-aem-related-bug.md
title: How I found my first AEM related bug.
category: documents
detected_topics:
- command-injection
- automation-abuse
- api-security
- mobile-security
tags:
- imported
- documents
- command-injection
- automation-abuse
- api-security
- mobile-security
language: en
raw_sha256: 32a891e96aa83f7325f4440c57c879d5da02870ea08c224472574531d749c45c
text_sha256: 4a1fe02f78a04b2c42fd67444abf8e8d35c38e887ba141dcf4a91d2aeb6cdff5
ingested_at: '2026-06-28T07:32:07Z'
sensitivity: unknown
redactions_applied: false
---

# How I found my first AEM related bug.

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-09-11_how-i-found-my-first-aem-related-bug.md
- Source Type: markdown
- Detected Topics: command-injection, automation-abuse, api-security, mobile-security
- Ingested At: 2026-06-28T07:32:07Z
- Redactions Applied: False
- Raw SHA256: `32a891e96aa83f7325f4440c57c879d5da02870ea08c224472574531d749c45c`
- Text SHA256: `4a1fe02f78a04b2c42fd67444abf8e8d35c38e887ba141dcf4a91d2aeb6cdff5`


## Content

---
title: "How I found my first AEM related bug."
url: "https://vedanttekale20.medium.com/how-i-found-my-first-aem-related-bug-5ea901aad3f4"
authors: ["Vedant Tekale (@_justYnot)"]
bugs: ["LFR"]
publication_date: "2021-09-11"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3325
scraped_via: "browseros"
---

# How I found my first AEM related bug.

How I found my first AEM related bug.
Vedant Tekale
Follow
4 min read
·
Sep 11, 2021

820

4

Hello all the amazing hackers and cyber security enthusiasts. My name is Vedant(Also known as Vegeta on Twitter😁) and I’m an aspiring bug bounty hunter and a cyber security enthusiast. Today I want to share with you a story about how I found my first AEM related bug :) First of all I want to tell you that I’m still learning about AEM and I found this issue just by applying whatever I’ve learnt so far. So without any further ado, let’s get started.

Press enter or click to view image in full size
Background:-

So before understanding the actual bug, you’ve to learn about few things. First, what is AEM? “Adobe Experience Manager (AEM), is a comprehensive content management solution for building websites, mobile apps and forms. And it makes it easy to manage your marketing content and assets.” Basically AEM is a CMS just like Wordpress and Drupal.

Moving on next is Querybuilder servlet, “AEM Query Builder is a framework developed by adobe to build queries (JCR XPath underneath) for a query engine (OAK Query Engine) which are simple to compose. A query can be described as simple set of predicates in key value form.” you can learn more about it here.

And last but not least, Dispatcher. “Dispatcher is Adobe Experience Manager’s caching and/or load balancing tool. Using AEM’s Dispatcher also helps to protect AEM server from attack” you can think of AEM dispatcher like a WAF.

The vulnerability:-

So in July I got lot’s of duplicates and informative bugs on Hackerone platform and I was a little frustrated because of that. Whenever I feel demotivated while hunting for bugs I remember this quote, “If your life just got harder, you’ve just leveled up” I decided to learn about some new bug types and after searching for a while I found this awesome talk from Mikhail Egorov where he talked about AEM related bugs. This was completely new for me so I decided to explore more and read all the write-ups I could find about AEM related vulnerabilities. I got a basic idea about some things and decided to apply what I learned so far. So I selected one program to hack on. I already had gathered subdomains and tried to find vulnerabilities in them multiple times but couldn’t find any, but this time it was different.

Get Vedant Tekale’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

I checked every subdomain and using wappalyzer I was checking for a subdomain which was using AEM and after a while I came across a subdomain which was built using AEM. Then I started fuzzing for finding querybuilder servlet and by exploiting it an attacker could read internal path. I was fuzzing manually because it’s very fun trying to bypass the dispatcher 😁. I tried the following payload and the site was always responding with a 404 error but I kept trying some payloads to bypass the dispatcher.

Press enter or click to view image in full size
Credits to Mikhail Egorov.

As you can see in above image we can use things like /a.css , /a.png etc to confuse the dispatcher to give us the access to querybuilder servlet. So after trying out similar payloads like this, one worked successfully! The final payload looked something like this,

Payload:-

‘ /bin/querybuilder.json.;%0aa.css?path=/etc&p.hits=full&p.limit=-1’

I could read the contents of directories like /etc, /home, /content etc. You can find such bugs using automation also, there are many nuclei templates for AEM related bugs, you can check them out here. I quickly reported this issue and after 2 days the issue was triaged! and after a week I was awarded with a $$ bounty for it :)

There are a lot more interesting AEM related vulnerabilities out there and AEM is really a vast topic but very fun to explore. I hope you learned something new reading this write-up and if you have any questions about it you can reach out to me here . If you enjoyed reading the write-up please do clap and share it with your friends. Thank you!
