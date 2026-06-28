---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-01-25_the-unexpected-bounty-a-story-of-zendesk-takeover-on-redactedcom.md
original_filename: 2020-01-25_the-unexpected-bounty-a-story-of-zendesk-takeover-on-redactedcom.md
title: 'The unexpected bounty: A story of Zendesk takeover on REDACTED.com'
category: documents
detected_topics:
- xss
- idor
- command-injection
- rate-limit
- api-security
tags:
- imported
- documents
- xss
- idor
- command-injection
- rate-limit
- api-security
language: en
raw_sha256: 2480414ad8ca838254a6f98f9fdb6e6f96bd1fbc10a8cbd1d745369c82a1e505
text_sha256: 9738a4bd272cd8abbde23e79e9389d13297396608a4a5e407e3d3f6e275f5ed4
ingested_at: '2026-06-28T07:32:01Z'
sensitivity: unknown
redactions_applied: false
---

# The unexpected bounty: A story of Zendesk takeover on REDACTED.com

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-01-25_the-unexpected-bounty-a-story-of-zendesk-takeover-on-redactedcom.md
- Source Type: markdown
- Detected Topics: xss, idor, command-injection, rate-limit, api-security
- Ingested At: 2026-06-28T07:32:01Z
- Redactions Applied: False
- Raw SHA256: `2480414ad8ca838254a6f98f9fdb6e6f96bd1fbc10a8cbd1d745369c82a1e505`
- Text SHA256: `9738a4bd272cd8abbde23e79e9389d13297396608a4a5e407e3d3f6e275f5ed4`


## Content

---
title: "The unexpected bounty: A story of Zendesk takeover on REDACTED.com"
page_title: "The Unexpected Bounty: A Story of Zendesk Takeover on REDACTED.com | by accalon | InfoSec Write-ups"
url: "https://medium.com/bugbountywriteup/the-unexpected-bounty-a-story-of-zendesk-takeover-on-redacted-com-f2aa96ce2026"
authors: ["wis4nggeni"]
bugs: ["Subdomain takeover"]
publication_date: "2020-01-25"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4813
scraped_via: "browseros"
---

# The unexpected bounty: A story of Zendesk takeover on REDACTED.com

The Unexpected Bounty: A Story of Zendesk Takeover on REDACTED.com
accalon
Follow
3 min read
·
Jan 25, 2020

259

Tl;dr : a good faith powered report of subdomain takeover that ends up with a bounty, even though the company itself doesn’t have a Bug Bounty Program. Blocked by login/pay wall? Read for free here : (https://c2a.github.io/The-Unexpected-Bounty-A-Story-of-Zendesk-Takeover).

…

Greetings.

It all started with a Linkedin Connection Request.

The Person‘s bio says that she work as a Talent Acquisition Specialist on a company, REDACTED.com. Me, after got a duplicate on my previous report about XSS on Google, decided to take a break from there and check this REDACTED.com instead.

After some subdomain enumerations, i found something interesting on support.REDACTED.REDACTED.com. When i tried to access the mentioned subdomain, i got the following page:

Press enter or click to view image in full size

It looks like the subdomain is pointing to a zendesk help center page which is not claimed or no longer exists. Using dig command, I got the CNAME record.

Press enter or click to view image in full size

After reading Zendesk documentation, i successfully register a new account and taken over the subdomain. I was also able to get stored XSS by enabling the SSL to stop the redirect, then make a guide html page with an xss payload.

I didn’t report it immediately, because they don’t have Bug Bounty Program and i can’t find any contact related to security on their website. Days later, i received a couple of tickets (around 10) from their customers, turns out this zendesk portal is still being used, and tickets from their customers is being forwarded to this portal from the main(another) website.

Press enter or click to view image in full size
hmm…

I decided to ask the Talent Acquisition Specialist from the Linkedin, where Could I report this vulnerability? She gave me an Email of their Security Team and I immediately report this vulnerability because my email flooded with tickets from their customers.

Get accalon’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

I was just being a good guy and sent this report without expecting anything in return because I know they didn’t have a Bug Bounty Program, and a simple “Thank You.” would be very enough.

But to my surprise, they decided to rewards me with bounty. Well, the unexpected money is the best money.

Press enter or click to view image in full size

This is the fastest bounty I’ve ever received so far (more or less a week after report sent), and also mark my first bounty in 2020.

Thanks.

Timeline:

January 17 2020: Report sent.
January 20 2020: Report validated with High severity.
January 23 2020: $$$ paid, limited disclosure request approved.

Follow Infosec Write-ups for more such awesome write-ups.

InfoSec Write-ups
A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub…

medium.com
