---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-03-27_my-first-bug-open-redirect-at-epic-games-500-bounty.md
original_filename: 2023-03-27_my-first-bug-open-redirect-at-epic-games-500-bounty.md
title: My First Bug, Open redirect at Epic Games → $500 Bounty
category: documents
detected_topics:
- sso
- command-injection
tags:
- imported
- documents
- sso
- command-injection
language: en
raw_sha256: 8c894be39237c8145966a2096a2464fe331422a3a9e5c0cbb79f80677e56afc2
text_sha256: 07847bd4312da061cbadb8613a6470a8a82020a9448f3cd304968b4ace8ffd81
ingested_at: '2026-06-28T07:32:19Z'
sensitivity: unknown
redactions_applied: false
---

# My First Bug, Open redirect at Epic Games → $500 Bounty

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-03-27_my-first-bug-open-redirect-at-epic-games-500-bounty.md
- Source Type: markdown
- Detected Topics: sso, command-injection
- Ingested At: 2026-06-28T07:32:19Z
- Redactions Applied: False
- Raw SHA256: `8c894be39237c8145966a2096a2464fe331422a3a9e5c0cbb79f80677e56afc2`
- Text SHA256: `07847bd4312da061cbadb8613a6470a8a82020a9448f3cd304968b4ace8ffd81`


## Content

---
title: "My First Bug, Open redirect at Epic Games → $500 Bounty"
page_title: "Epic Games Open Redirect Bypass: How I Earned My First $500 Bounty | by Professor Software Solutions | Medium"
url: "https://medium.com/@bughuntar/my-first-bug-open-redirect-at-epic-games-500-bounty-d0c03de60fa7"
authors: ["Professor the Hunter (@bughuntar)"]
programs: ["Epic Games"]
bugs: ["Open redirect"]
bounty: "500"
publication_date: "2023-03-27"
added_date: "2023-03-31"
source: "pentester.land/writeups.json"
original_index: 1335
scraped_via: "browseros"
---

# My First Bug, Open redirect at Epic Games → $500 Bounty

Epic Games Open Redirect Bypass: How I Earned My First $500 Bounty
Professor Software Solutions
Follow
2 min read
·
Mar 28, 2023

155

2

Press enter or click to view image in full size
Introduction:

I’m a security researcher specializing in bug bounty programs, and I’ve been active on platforms like HackerOne since 2022. I also share bug bounty tips and insights on Twitter, where you can follow me at @bughuntar.

Journey into Bug Bounty

I first heard about bug bounty programs in January 2022. Intrigued, I started diving into cybersecurity concepts and bug hunting. Initially, I began by practicing on vulnerable machines. However, I quickly realized that this approach didn’t quite meet my expectations in terms of real-world application. Seeking more practical experience, I decided to start testing real-world websites, which led to my first discovery: an open redirect vulnerability at Epic Games.

This marked the beginning of my serious bug bounty journey, which I officially kicked off in April 2022.

The Bug: Open Redirect Bypass

The vulnerability I discovered was an open redirect. At first glance, the issue didn’t seem to be a direct open redirect, but after some testing, I managed to bypass the security measures in place.

Get Professor Software Solutions’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Here’s how I came across the vulnerability:

I was learning about open redirects and experimenting with different payloads.
During my practice, I came across a URL from Epic Games, which appeared to be vulnerable to redirection manipulation.
After several tests, I found that the redirect would only work if I used four backslashes (////) before the host in the redirectUrl parameter. The payload that successfully bypassed the filter was:
&redirectUrl=////evil.com
This was an unexpected behavior, but it demonstrated how an attacker could redirect a user to a potentially malicious site.
Example URLs

Valid Redirect Link:

https://www.redacted.com/id/login?lang=en-US&noHostRedirect=true&redirectUrl=https%3A%2F%2Fstore.redacted.com%2F

Exploited Open Redirect Link:

https://www.redacted.com/id/login?lang=en-US&noHostRedirect=true&redirectUrl=////evil.com
Conclusion

Discovering my first bug was an exciting and validating moment. I was thrilled with the outcome and took a moment to reflect on the journey, expressing my gratitude by saying, “Alhamdulillah.” It’s a great reminder of how persistence and continuous learning pay off in the world of bug bounty hunting.

Final Thoughts

This experience has been a motivating milestone in my cybersecurity journey. As I continue learning and growing in the field, I hope to share more discoveries and insights with the bug bounty community.

Follow Me

Stay connected and updated on my bug bounty journey, cybersecurity tips, and more! You can find me on the following platforms:

Website: https://bughuntar.com
Facebook: https://facebook.com/bughuntar
Twitter: https://twitter.com/bughuntar
Telegram: https://t.me/bughuntar
YouTube: https://youtube.com/bughuntar
Medium: https://bughuntar.medium.com
LinkedIn: https://www.linkedin.com/in/SoftwareDeveloperSagor

Feel free to reach out for tips, discussions, or collaboration opportunities!
