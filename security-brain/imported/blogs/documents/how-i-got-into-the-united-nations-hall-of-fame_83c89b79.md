---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-08-14_how-i-got-into-the-united-nations-hall-of-fame.md
original_filename: 2022-08-14_how-i-got-into-the-united-nations-hall-of-fame.md
title: How I got into the United Nations’ Hall of Fame
category: documents
detected_topics:
- command-injection
- rate-limit
- automation-abuse
tags:
- imported
- documents
- command-injection
- rate-limit
- automation-abuse
language: en
raw_sha256: 83c89b793a3e7ddbd06f99959ca64ee5a8b1adcc0fbcea4fd58713582ae331fd
text_sha256: 5d324bdabb656dae274d4c5132ff2c991e6787808b4f6331a08325a07d407dcf
ingested_at: '2026-06-28T07:32:13Z'
sensitivity: unknown
redactions_applied: false
---

# How I got into the United Nations’ Hall of Fame

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-08-14_how-i-got-into-the-united-nations-hall-of-fame.md
- Source Type: markdown
- Detected Topics: command-injection, rate-limit, automation-abuse
- Ingested At: 2026-06-28T07:32:13Z
- Redactions Applied: False
- Raw SHA256: `83c89b793a3e7ddbd06f99959ca64ee5a8b1adcc0fbcea4fd58713582ae331fd`
- Text SHA256: `5d324bdabb656dae274d4c5132ff2c991e6787808b4f6331a08325a07d407dcf`


## Content

---
title: "How I got into the United Nations’ Hall of Fame"
page_title: "How I got into United Nations' Hall of fame | by cryptoknight028 | Aug, 2022 | Bug Zero | Bug Zero"
url: "https://blog.bugzero.io/how-i-get-into-united-nations-hall-of-fame-6975e3d3cc45"
authors: ["Ameya Andhare (@cryptoknight028)"]
programs: ["United Nations"]
bugs: ["Missing authentication"]
publication_date: "2022-08-14"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 2313
scraped_via: "browseros"
---

# How I got into the United Nations’ Hall of Fame

How I got into the United Nations’ Hall of Fame
cryptoknight028
Follow
2 min read
·
Aug 14, 2022

61

2

Hi,

I am Ameya, an Independent cyber security researcher from India. Today I am sharing how I got my Hall of Fame from the United Nations Office of Information and Communications Technology.

So it was a normal day, I was doing my normal lectures (due to covid-19 lectures being online). So I was scrolling my Twitter in the background. I came to see that someone got the United Nations’ hall of fame for submitting a valid bug.

So I thought, I should try. I opened up their Responsible Disclosure. So I choose one domain https://unep.org. Firstly, I gathered all the subdomains.

And I started checking manually each subdomain. So I found one subdomain redacted.unep.org (taking redacted as demo subdomain). On that domain, I found phpmyadmin portal at https://redacted.unep.org/phpadmin/.

But it requires a username and password. I tried default credentials but no luck. Then I tried to do directory brute-force using ‘dirb’ tool for fuzzing.

Surprisingly I found endpoint https://redacted.unep.org/dbadmin/setup returning 200 OK response status. I opened it and I directly get into phpmyadmin portal without login.

Get cryptoknight028’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

So it was a broken authentication vulnerability at that endpoint.

Impact: It's possible for an attacker to configure the servers without the information of the application administrator. I can even download the database of the site.

Press enter or click to view image in full size
United nation HOF

Thank you for reading this article!

Bug Zero is a bug bounty, crowdsourcing platform for security testing. The platform is the intermediatory entity that enables client organizations to publish their service endpoints so that bug hunters (security researchers / ethical hackers) registered in the platform can start testing the endpoints without any upfront charge. Bug hunters can start testing as soon as a client organization publishes a new program. Bug Zero also offers private bug bounty programs for organizations with high-security requirements.

Press enter or click to view image in full size
https://bugzero.io/signup

Bug Zero is available for both hackers and organizations.

For organizations and hackers, register with Bug Zero for free, and let’s make cyberspace safe.
