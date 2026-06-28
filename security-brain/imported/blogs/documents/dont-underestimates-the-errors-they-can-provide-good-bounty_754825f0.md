---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2019-06-07_dont-underestimates-the-errors-they-can-provide-good-bounty.md
original_filename: 2019-06-07_dont-underestimates-the-errors-they-can-provide-good-bounty.md
title: Don’t underestimates the Errors They can provide good $$$ Bounty!
category: documents
detected_topics:
- xss
- command-injection
- mfa
- automation-abuse
- information-disclosure
- api-security
tags:
- imported
- documents
- xss
- command-injection
- mfa
- automation-abuse
- information-disclosure
- api-security
language: en
raw_sha256: 754825f06ffa808acdec987771014acef4844cabd9456108f87d02a43af2e40f
text_sha256: 3dd794be883380efb21ee8fd61911e11a47cbb976f219df297dd7cf56b68fa65
ingested_at: '2026-06-28T07:31:59Z'
sensitivity: unknown
redactions_applied: false
---

# Don’t underestimates the Errors They can provide good $$$ Bounty!

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2019-06-07_dont-underestimates-the-errors-they-can-provide-good-bounty.md
- Source Type: markdown
- Detected Topics: xss, command-injection, mfa, automation-abuse, information-disclosure, api-security
- Ingested At: 2026-06-28T07:31:59Z
- Redactions Applied: False
- Raw SHA256: `754825f06ffa808acdec987771014acef4844cabd9456108f87d02a43af2e40f`
- Text SHA256: `3dd794be883380efb21ee8fd61911e11a47cbb976f219df297dd7cf56b68fa65`


## Content

---
title: "Don’t underestimates the Errors They can provide good $$$ Bounty!"
url: "https://medium.com/@noob.assassin/dont-underestimates-the-errors-they-can-provide-good-bounty-d437ecca6596"
authors: ["Aditya Sharma (@Assass1nmarcos)"]
programs: ["Mamba"]
bugs: ["Information disclosure", "Internal path disclosure"]
bounty: "200"
publication_date: "2019-06-07"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5226
scraped_via: "browseros"
---

# Don’t underestimates the Errors They can provide good $$$ Bounty!

Don’t underestimates the Errors They can provide good $$$ Bounty!
Aditya Sharma
Follow
2 min read
·
Jun 7, 2019

231

3

Today I am gonna tell you how I got $$$ bounty. On that day i was founding any good bug bounty program which have a wider Scope. So my search Ends on Mamba Bug Bounty Program . So as we all know the first Step is sharpen the Axe before cutting the tree 😐 i mean just start Recon On my target https://mamba.ru :). So after 1 hour i take a sight on its Subdomains.

There is a subdomain like https://bot.mamba.ru. That looks like Dummy bot Chat Subdomain 🎃 as you can see below.

Press enter or click to view image in full size
Vulnerable Subdomain
What can i do there ??? Lets chat to the bot Lmfao 😆.

While sending message on bot Chat i intercepted and tried to inject XSS but nothing happened

Lets Move on To new target its Just Bot Chat :( …..No try to a host header injection… But the result is nothing .

And then accidentally I removed the Host Header From the Request and boooomm…In Error I got Source Code Path Disclosure Which is because of Server Side misconfig. If that was properly configured i got 400 bad request But i got 401 error with sensitive information as you can see below (i hide the path)

Press enter or click to view image in full size
Sensitive Path Disclosure on https://bot.mamba.ru

Hence I reported The bug to mamba security Team. They Responded me after 1 day Informing me That they are rewarding me $200 for this bug 🙏.

So don’t Underestimate the Errors

Timeline:

Get Aditya Sharma’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Wed, May 22, 2019 at 4:08 PM: Bug Reported

Thu, May 23, 2019 at 11:20 PM: Mamba Security Team Replied “Valid Issue”

Thu, May 23, 2019 at 11:33 PM:Bug Patched & Bounty Rewarded.

Sat, May 25, 2019 at 10:20 AM: Request Of Public Disclosure.

Sat, May 25, 2019 at 05:20 PM: Agreed to publicly Disclosure.

P.S.: Sorry If there is any grammatical Mistakes my English is not good enough and although This is my First Blog .

Thanks For Reading

#keepHunting
