---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2017-10-17_how-i-hacked-all-the-redact-agents-accounts_2.md
original_filename: 2017-10-17_how-i-hacked-all-the-redact-agents-accounts_2.md
title: How I hacked all the [REDACT] Agents accounts
category: documents
detected_topics:
- access-control
- command-injection
- api-security
tags:
- imported
- documents
- access-control
- command-injection
- api-security
language: en
raw_sha256: fa458fbde494c91f338d859b5c42de06ca181b9eef55ffd0dc7d59fa9c0b5f7b
text_sha256: d1d2b9a8532c36380990de35f0a14c22e48b15132fc299adee3d910c8a9ab5bd
ingested_at: '2026-06-28T07:31:56Z'
sensitivity: unknown
redactions_applied: false
---

# How I hacked all the [REDACT] Agents accounts

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2017-10-17_how-i-hacked-all-the-redact-agents-accounts_2.md
- Source Type: markdown
- Detected Topics: access-control, command-injection, api-security
- Ingested At: 2026-06-28T07:31:56Z
- Redactions Applied: False
- Raw SHA256: `fa458fbde494c91f338d859b5c42de06ca181b9eef55ffd0dc7d59fa9c0b5f7b`
- Text SHA256: `d1d2b9a8532c36380990de35f0a14c22e48b15132fc299adee3d910c8a9ab5bd`


## Content

---
title: "How I hacked all the [REDACT] Agents accounts"
url: "https://medium.com/@neerajedwards/how-i-hacked-all-the-redact-agents-accounts-ec165b7c514a"
authors: ["Neeraj Sonaniya (@neeraj_sonaniya)"]
bugs: ["Default credentials"]
bounty: "100"
publication_date: "2017-10-17"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 6073
scraped_via: "browseros"
---

# How I hacked all the [REDACT] Agents accounts

How I hacked all the [REDACT] Agents accounts
Neeraj Sonaniya
Follow
4 min read
·
Oct 17, 2017

161

3

Disclaimer

The sole purpose of this article is educational and for testing of your own applications. This is not intended for piracy or any other non-legal use.

Introduction:

Since company doesn’t allow disclosure, i will keep company name [REDACT].

POS application is used by [REDACT] agents for Topup, SIM activation purpose. At the time when an agent register with [Redact], they need to verify their details, and hence have to give their documents like Aadhar card, Address Proof ID, Voter ID. After all verification [Redact] gives agent a USER ID and USER PASSWORD. The USER ID generally have 10 digit number’s, start with 068 , and hence the agent USER ID will look like this 068XXXXXXX. Where X is any number from 0 to 9.

So, now we have all the USER ID of all the agents, what next? The next step is to find password for those user ID’s of agents.

After some searching about password, i luckily found a person who work with same company as retailer, when i asked him his password for POS application, he told me the password which is `Zxq@1XXX`, At the same time i also found one other person using that application, and i got same password from him too.

So, what next?

Immediately after getting these informations i have downloaded POS application, and setup the proxy to capture the request from that app using Burpsuite.

Captured Request in Burpsuite:

Press enter or click to view image in full size

Here MacID is Device Media Access Control ID of device.

I immediately sent that request to Burpsuite intruder and changed the last 4 digits of UserID with default password for all the UserID’s

What I got in response:

Press enter or click to view image in full size

Response length → 9500 [Approx.] → SignIn success

Response length →330 → SignIn Failure

Failure Response

Approx 3000 ID’s have default password out of 9000

Get Neeraj Sonaniya’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

After that i immediately set burp intruder request to last 6 digit numbers. And found that approx 26,000 accounts out of 90,000 are vulnerable to this.

After that i immediately contacted to [Redact] via twitter/email but didn’t got any response. But i am really thankful to 
HackerOne
 who helped me to reach [Redact] via its Disclosure Assistance Program .

What detail’s I got :

→ Aadhar Card Numbers
→ Email addresses

→ Agent’s account Secret Keys
→ Permanent Address

→ Mobile Number
→ Customer Details to whom they recharged
→ Agent’s all documents in PDF file format, and many more.

What any bad guy can do with this details:

Can Login to any agent’s account and can get all the details about customer and agent
Can Download all the documents in PDF file format which are used for verification purpose.
Can sell those details to Black market.
Can Top up mobile [any network] from any agent’s account.

[Redact] rewarded me bounty of 100$, which is i think not a sufficient bounty for hacking all the agent’s above described details.

Press enter or click to view image in full size

All this i have written 2nd time, i was excited to share this find and i asked them nicely with a PRIVATE writeup that can i share, when i sent them writeup without disclosing the issue,after some time i got call from their Vice President of Security, he threaten me and asked that if i will disclose this publicly then i will file a complaint to Cyber Crime investigation department, we also have all the logs of brute-forcing the ID’s from your IP address.

The only thing which triggered me to share this is i asked him nicely with good intentions and he started yelling at me and started threatening me i felt bad because i actually helped them.

when i questioned them that bounty is too less as compared to the impact of issue reported by me, he false promised me, that we will make your career with our organization, when i messaged him, he didn’t replied to me (initially told me to be in touch with him).

I ethically wanted to help them and even helped them, but they don’t care and even India doesn’t care about information security of public, they don’t want to loose their prestige and hence don’t want to make disclosure of any vulnerability. They all want their work in free.

Neeraj Sonaniya

Whitehat security researcher
