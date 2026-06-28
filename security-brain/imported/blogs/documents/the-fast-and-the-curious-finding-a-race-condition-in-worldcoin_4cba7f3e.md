---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2024-04-08_the-fast-and-the-curious-finding-a-race-condition-in-worldcoin.md
original_filename: 2024-04-08_the-fast-and-the-curious-finding-a-race-condition-in-worldcoin.md
title: 'The Fast and the Curious: Finding a Race Condition in Worldcoin'
category: documents
detected_topics:
- sso
- command-injection
- automation-abuse
- race-condition
- business-logic
- api-security
tags:
- imported
- documents
- sso
- command-injection
- automation-abuse
- race-condition
- business-logic
- api-security
language: en
raw_sha256: 4cba7f3e73067bc63328d68f295d8d20599ab98d6c952de8e38595959345df1d
text_sha256: eb1bb9f222d66761b5a3ded6592ce3e3fd26b895824edc780ff85e0951ef81e0
ingested_at: '2026-06-28T07:32:32Z'
sensitivity: unknown
redactions_applied: false
---

# The Fast and the Curious: Finding a Race Condition in Worldcoin

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2024-04-08_the-fast-and-the-curious-finding-a-race-condition-in-worldcoin.md
- Source Type: markdown
- Detected Topics: sso, command-injection, automation-abuse, race-condition, business-logic, api-security
- Ingested At: 2026-06-28T07:32:32Z
- Redactions Applied: False
- Raw SHA256: `4cba7f3e73067bc63328d68f295d8d20599ab98d6c952de8e38595959345df1d`
- Text SHA256: `eb1bb9f222d66761b5a3ded6592ce3e3fd26b895824edc780ff85e0951ef81e0`


## Content

---
title: "The Fast and the Curious: Finding a Race Condition in Worldcoin"
url: "https://medium.com/@gonzo-hacks/the-fast-and-the-curious-finding-a-race-condition-in-worldcoin-621c89bfbd61"
authors: ["Dane Sherrets (@DaneSherrets)"]
programs: ["Tools for Humanity (Worldcoin)"]
bugs: ["Race condition", "Web3 hacking"]
bounty: "3,000"
publication_date: "2024-04-08"
added_date: "2024-05-08"
source: "pentester.land/writeups.json"
original_index: 348
scraped_via: "browseros"
---

# The Fast and the Curious: Finding a Race Condition in Worldcoin

The Fast and the Curious: Finding a Race Condition in Worldcoin
Dane Sherrets
Follow
6 min read
·
Apr 7, 2024

128

Press enter or click to view image in full size

TL;DR

In August of 2023 I applied the “State Machine” research from James Kettle on the World ID SDK and identified a Race Condition that would have enabled an attacker to bypass the preset verification limit on a cloud-based implementation. Exploitation of this vulnerability would have devastating consequences for a project that relied on World ID for restricting the number of actions a user could take (e.g., if a project was using the SDK to say a user should only be able to cast 1 vote an attacker could exploit the vulnerability to cast 20 votes).

The Worldcoin team (and specifically the group at Tools for Humanity) communicated thoroughly during the reporting process and were a joy to work with. The report was triaged as “High” and awarded $3000 — you can view the actual HackerOne report here.

I have found similar bugs in the wild so I am also sharing a basic python script that can be used to to automate the process of testing for them.

Background

I have been interested in Worldcoin ever since it hit the Blockchain scene back in 2019. If you aren’t familiar with the project the basic gist is that it is a cryptocurrency project that aims to build a foundation for:

A) biometrically verifying unique humans

and

B) a distribution mechanism for Universal Basic Income (UBI).

Although most people probably just know about it as the company that builds an orb that will give you cryptocurrency if you stare into it (to be fair, that’s not technically how it works, but I’m not going to get into that here).

My instinct is to say I don’t love the idea of humans scanning their eyeballs and giving biometric data to a centralized entity; BUT I do think that Sybil-resistance is one of the most difficult problems the internet faces today and as we are quickly approaching a world where anyone can create hundreds of AI-powered bots it is going to become a critical problem to solve (it is worth noting that Sam Altman is one of the founders of Worldcoin).

Say whatever you want about Worldcoin but I don’t know of many other projects that are working on this issue in a meaningful way!

Before I started looking into Worldcoin I had assumed that it was purely a cryptocurrency distribution mechanism but as I dug deeper I found that they were building an SDK around biometric authentication. This means that other apps could use the Worldcoin SDK to confirm that 1 user = 1 human being. That might not sound like a big deal but that is a game changer for apps with use cases like: voting, airdropping, and bot protection.

For example, if I wanted to make an app that made it so a unique human could only vote 1 time on a given issue then I could make all of my users authenticate via the Worldcoin SDK which would essentially act as a Identity Provider (IDP) and enforcer for the limitation I preconfigured (i.e vote 1 time)

Press enter or click to view image in full size
Example use cases for World ID

As a cryptocurrency, Worldcoin of course has an SDK implementation of this that works for (EVM-compatible) Blockchains and also a Cloud based version that does not require integrating any blockchain. Both versions use some really cool merkle-tree based cryptography to create a tamper-proof log of transactions. Not going into that for this blog post as it isn’t relevant for the bug but it is worth reading up on if you are not familiar.

Get Dane Sherrets’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

To help Developers with testing the Worldcoin workflow, Worldcoin offers a simulator to test transactions and verifications. And if I create a Dev account I can create “Actions” (e.g. “vote on this proposal”) and set a maximum number of “Verifications” (e.g. “number of times a human can vote on a proposal). To look under the hood of how this all works I did most of my testing on this simulator and ran the requests through Burp Suite.

Press enter or click to view image in full size
Burp request for performing a single action

While I could change things like the “credential type” (either “orb” or “device” or “chain”) the requests were all very similar. I spent many hours trying to break the flow and signatures but was unable to do anything so I gave up for a few weeks.

Finding the Bug

Flashforward to DEF CON 31 and James Kettle presented his research on Smashing The State Machine. As soon as I read his blog I thought this might be interesting to try on Worldcoin but I didn’t actually think anything would come from it. I might have even forgotten to try this but after DEF CON I caught Covid so I was absolutely wrecked and stuck on my couch in front of a computer and decided to give it a shot. I opened up the Burp Repeater tab and made sure I downloaded the Burp update that had the “Send in Parallel” feature (for Burp Pro only) and gave it a shot on the Worldcoin flow I described earlier.

Specifically the steps looked like:

Capture the request and send it to repeater
Make a new “tab” for the request
Duplicate the original request ~20 times in the new “tab”
Send them all “In Parallel”
Press enter or click to view image in full size
Feature in Burp Pro that enables sending parallel requests that results in race condition

When I looked at the requests it worked! Where I should have only seen 2 verifications of “unique humans” I saw 20!

Press enter or click to view image in full size
The address ending in `7c6` should only be able to appear twice on this list… but because of race condition it appears 20+!

I only tested this on the “Cloud” version of the implementation as I was pretty sure it wouldn’t work on the “Blockchain” version as I assumed that would require a transaction to be finalized (and I confirmed this assumption was correct with the team).

Since the Worldcoin project is open source I can review the code and saw a red flag in the `canVerifyForAction` util:

Press enter or click to view image in full size

Specifically, the way `nullifier` is referenced in other parts of the codebase here allowed for a race condition as it just added to an array without a “lock” — which means parallel requests would all be treated equally.

The Worldcoin team addressed this by using the database to create an artificial lock so that even if two requests come in at the same time they will be treated properly. In this pull request you can see they now have new database tables for `nullifiers` and they have updated the `canVerifyForAction` code to reference the `nullifier` number of uses instead of just the length:

Press enter or click to view image in full size

When people think of a “Blockchain” or “Web3” project they often assume that any vulnerabilities will be limited to the blockchain or smart contract — this is often not the case. Today, Web3 still relies heavily on Web2 and this opens up a wide range of creative attack vectors. If you are a Javascript gigabrain and you haven’t tried bug hunting on Web3 projects then you are leaving money on the table!

Big thanks again to the Worldcoin (and Tools For Humanity) team for diligently fixing this issue and giving feedback on this disclosure. They constantly ship cool features and I plan on spending more time on their bug bounty program.

Since reporting this bug I have found similar High and Critical issues out in the wild. For hunters that want to test for these bugs but do not have Burp Suite Pro I wrote a quick and dirty python script that can be used as a starting point for building out future tests.

I am going to push myself to share more learnings in public. Follow me on twitter (@DaneSherrets ) if you would like to see more.
