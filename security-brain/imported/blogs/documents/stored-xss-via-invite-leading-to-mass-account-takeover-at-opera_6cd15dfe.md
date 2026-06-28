---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-06-20_stored-xss-via-invite-leading-to-mass-account-takeover-at-opera.md
original_filename: 2021-06-20_stored-xss-via-invite-leading-to-mass-account-takeover-at-opera.md
title: Stored XSS via Invite leading to Mass Account Takeover at Opera.
category: documents
detected_topics:
- xss
- idor
- command-injection
- rate-limit
tags:
- imported
- documents
- xss
- idor
- command-injection
- rate-limit
language: en
raw_sha256: 6cd15dfe09fee705aef894df16a6076bd2320bef14453cdb896d208ef99733f5
text_sha256: 51e97da111faf19f551f2013a36b77542a6e28e7da931de00161b5ffdbb0a76a
ingested_at: '2026-06-28T07:32:06Z'
sensitivity: unknown
redactions_applied: false
---

# Stored XSS via Invite leading to Mass Account Takeover at Opera.

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-06-20_stored-xss-via-invite-leading-to-mass-account-takeover-at-opera.md
- Source Type: markdown
- Detected Topics: xss, idor, command-injection, rate-limit
- Ingested At: 2026-06-28T07:32:06Z
- Redactions Applied: False
- Raw SHA256: `6cd15dfe09fee705aef894df16a6076bd2320bef14453cdb896d208ef99733f5`
- Text SHA256: `51e97da111faf19f551f2013a36b77542a6e28e7da931de00161b5ffdbb0a76a`


## Content

---
title: "Stored XSS via Invite leading to Mass Account Takeover at Opera."
url: "https://sm4rty.medium.com/stored-xss-via-invite-leading-to-mass-account-takeover-at-opera-a85ed257dd12"
authors: ["Samrat Gupta (@Sm4rty_)"]
programs: ["Opera"]
bugs: ["Stored XSS"]
publication_date: "2021-06-20"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3555
scraped_via: "browseros"
---

# Stored XSS via Invite leading to Mass Account Takeover at Opera.

Stored XSS via Invite leading to Account Takeover at Opera.
Sm4rty
Follow
3 min read
·
Jun 20, 2021

341

Press enter or click to view image in full size

Hey Guys!! I am Samrat Gupta aka Sm4rty, a Security Researcher and a Bug Bounty Hunter. I hope everyone is safe in the Current Covid-19 Pandemic Situation. I am back with another Blog. Hope you will learn something new today.

So, It is a story of Stored XSS which I recently found at yoyogames.com which is one of the domains of the Opera BugBounty Program. Let’s get started.

What is Stored XSS?

Stored XSS, also known as persistent XSS, is the more damaging of the two i.e. Reflected or DOM-based. It occurs when a malicious script is injected directly into a vulnerable web application is stored in the server, which can therefore be more impactful.

How I found Stored XSS at Opera?

It was a month before I was hunting at Opera. I picked the domain yoyogames.com which was in the scope of the Opera Program at BugCrowd.

Press enter or click to view image in full size

At first, I begin with initial Recon i.e. subdomain enumeration, port scanning, screenshot, and running Nuclei. Then I thought of exploring the features as a normal user.

Press enter or click to view image in full size

In the application, I found a function where user can create a publisher. So, I randomly tried an XSS payload </h4><script>alert(document.cookie)</script> at the Name parameter of the publisher. As Expected, Nothing happened and XSS didn’t trigger.

Press enter or click to view image in full size

Then I further explored the application and found a feature, Where I was able to invite other users to access the publisher which I just created. So, I created a second account on the website.

From the First Account, I just invited the second Account to the publisher. And From Second Account, As I clicked ‘accept’ on Invitation.

Get Sm4rty’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

BOOM!! XSS Triggered.

Again I tried the same steps and Instead of accepting the Invite I clicked on ‘decline’ and say what XSS triggered again.

Press enter or click to view image in full size

So, I got too excited and Just reported it to the Program. But unfortunately, I was a bit late. Before me, someone had already reported the vulnerability and All I got was a duplicate. But still, I learned a lot.

Press enter or click to view image in full size
Key Takeaways:
When the XSS payload doesn’t trigger at one place, It doesn’t mean that It is not vulnerable.
Try every endpoint where the parameter is reflected.
Don’t Give up at one attempt, Try to dig deeper.

Here is the POC link: https://youtu.be/uoIaAlF1CG0

Thanks for Reading. Any Suggestions are always welcomed!!

Support me if you like my work! Buy me a coffee and Follow me on Twitter.
