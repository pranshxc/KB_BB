---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-12-02_hacking-on-a-plane-leaking-data-of-millions-and-taking-over-any-account.md
original_filename: 2022-12-02_hacking-on-a-plane-leaking-data-of-millions-and-taking-over-any-account.md
title: 'Hacking on a plane: Leaking data of millions and taking over any account'
category: documents
detected_topics:
- idor
- command-injection
- password-reset
- api-security
- supply-chain
tags:
- imported
- documents
- idor
- command-injection
- password-reset
- api-security
- supply-chain
language: en
raw_sha256: c6214f96cfdf878e71cefb52b3f4f24b9b501617c7f5f802cb482965948659db
text_sha256: 601e7137e9419dcd9a35326aa20e8baae57fb8c632a3e765e2063f4e6f95fbbd
ingested_at: '2026-06-28T07:32:16Z'
sensitivity: unknown
redactions_applied: false
---

# Hacking on a plane: Leaking data of millions and taking over any account

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-12-02_hacking-on-a-plane-leaking-data-of-millions-and-taking-over-any-account.md
- Source Type: markdown
- Detected Topics: idor, command-injection, password-reset, api-security, supply-chain
- Ingested At: 2026-06-28T07:32:16Z
- Redactions Applied: False
- Raw SHA256: `c6214f96cfdf878e71cefb52b3f4f24b9b501617c7f5f802cb482965948659db`
- Text SHA256: `601e7137e9419dcd9a35326aa20e8baae57fb8c632a3e765e2063f4e6f95fbbd`


## Content

---
title: "Hacking on a plane: Leaking data of millions and taking over any account"
page_title: "Hacking on a plane: Leaking data of millions and taking over any account · Joseph Thacker"
url: "http://rez0.blog/hacking/2022/12/02/hacking-on-a-plane.html"
final_url: "https://josephthacker.com/hacking/2022/12/02/hacking-on-a-plane.html"
authors: ["rez0 (@rez0__)"]
bugs: ["IDOR"]
publication_date: "2022-12-02"
added_date: "2022-12-05"
source: "pentester.land/writeups.json"
original_index: 1824
---

# Hacking on a plane: Leaking data of millions and taking over any account

02 Dec 2022 • [ hacking ](/category/hacking.html)

![](https://i.imgur.com/6u4iy7e.png) _Hacking on a plane, by Midjourney AI_

This is a short write-up about how I could have accessed the personal and financial information for tens of millions of users as well as take over anyone’s account without user interaction.

## Boredom leads to greatness

While on a 14-hour flight last week, after about 8 hours, I got tired of watching shows and reading books. I don’t usually want to pay for WiFi, but I decided to check the price. If there is a flight to splurge on, it’s a 14-hour one.

When I pulled up my phone, I saw WiFi was provided by a specific provider for which I faintly recalled there being a bug bounty program on BugCrowd. Before putting my credit card information and home address into an application, I often take a cursory glance at the security of the system.

It allows you to register an account without putting in credit card data. So I created a test account, and browsed around to a couple pages before checking burp. The following request stood out to me due to the response containing all of my account information. Also, like any good bug hunter, the user_name field stood out as a potential IDOR.
  
  
  GET /edge/apidecorator/v3/customer?data_types=PERSONAL,PMTINSTRUMENTS,GROUP_ATTRIBUTES
  &requester=INTERNET&tracking_id=uxdId-_A25AE4339A5309CCFA508534B9933
  &user_name=testingz20221118213555&uxd_id=uxdId-__A25AE4339A5309CCFA508534 HTTP/1.1
  Host: internet.com
  

The thing about the username is that it’s unguessable due to the timestamp. I decided to test it anyways by creating another account and using that username. I assumed that it wouldn’t work or would restrict access. There’s no way it would be that easy…

Tada! 🎉 It worked!

I still thought the impact was limited due to the `user_name` format, so I tried changing `user_name` to `email_address` since that was in the response… and it worked also.

I tried `customer_id` since the IDs are integers. It would increase the impact from a targeted vulnerability (by email address) to disclosing all users by simply incrementing through all the IDs. That also worked!

## But wait, there’s more!

I happened to check my personal email for an account. I assumed I had signed up for wifi in the past before getting into security. Sure enough, I had an older account. And because I was already going to disclose a critical bug, I decided to check for another bug with that second account.

The password reset functionality used two requests. The first request was to `POST /edge/apidecorator/v2/customer/authenticate/` and validated the user’s auth. After that, a PUT request to `/edge/apidecorator/v2/customer/` had this body:
  
  
  {
  "resetPassword": {
  "password": "password123!"
  },
  "user": "testingz20221118213555",
  "uxdId": "uxdId-GET /edge/apidecorator/v3/customer?data_types=PERSONAL,PMTINSTRUMENTS,GROUP_ATTRIBUTES&requester=INTERNET&tracking_id=uxdId-_A25AE4339A5309CCFA508534B99332B0_1668735922_0avmL6L5q&user_name=testingz20221118213555&uxd_id=uxdId-__A25AE4339A5309CCFA508534B99332B0_1668735922_0avmL6L5q HTTP/1.1__A25AE4339A5309CCFA508534B99332B0_1668735922_0avmL6L5q"
  }
  

I changed the `user` field to the username of my old account and was then able to login with the new password! Woah, it appeared to be a remote ATO without user interaction.

I asked my friend Sam Curry if I could change his password as a test, just to be sure I wasn’t making a silly mistake. Nearly all hackers have gotten confused thinking they had found an awesome bug only to realize they were actually only modifying their own account. Sure enough, it worked on his account as well!

## Impact

The impact of these two bugs was signifcant. It was access to first name, last name, address, and email of the user as well as last 4 digits, expiration date, billing name, and address of the credit cards. The customer IDs are in the tens of millions. Additionally, there was an account takeover vulnerability for all the accounts as well.

Given PCI and GDPR compliance, these bugs in the hands of an attacker could have been disastrous. META was just fined €265 million for mass exposing the data of users.

## Disclosure details

I looked around for a security contact with the vendor without much luck. Eventually I was pointed to the Aviation ISAC. They were super helpful. Since I found the bugs while on a flight, they sent me a contact at that airline. Even though it was third-party, the airline worked with me to get it fixed. With their superb help, this was the timeline:

  * Monday (November 21st) the airline was made aware of the issue and immediately proceeded to escalate and contact the appropriate groups for validation and remediation.
  * Tuesday (November 22nd) the impacted third-party was formally debriefed, proceeded to confirm the validity of the findings, and began immediately working on a resolution.
  * Wednesday (November 23rd) the third-party stated their resolution has already been tested and deployed before noon Eastern.

I was flying back home that day and was able to validate the fix in the air, which was neat. Thanks for taking the time to read the post. I hope you enjoyed it.

\- rez0

For more of my thoughts, bug bounty tips, and AI-generated hacker art, [follow me on twitter](https://twitter.com/rez0__).

[ cybersecurity ](/tags.html#cybersecurity) [ hacking ](/tags.html#hacking)

## Related Posts

  * ###  [ Claude Code Hacking Skills Video 20 Mar 2026 ](/hacking/2026/03/20/claude-code-hacking-skills.html)

  * ###  [ The Agentic Hacking Era: Ramblings and a Tool 06 Mar 2026 ](/hacking/2026/03/06/the-agentic-hacking-era.html)

  * ###  [ AI's Impact on Software and Bug Bounty 24 Feb 2026 ](/ai/2026/02/24/ai-s-impact-on-bug-bounty.html)
