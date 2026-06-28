---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2019-03-06_3-xss-in-protonmail-for-ios.md
original_filename: 2019-03-06_3-xss-in-protonmail-for-ios.md
title: 3 XSS in ProtonMail for iOS
category: documents
detected_topics:
- xss
- command-injection
- path-traversal
- mobile-security
tags:
- imported
- documents
- xss
- command-injection
- path-traversal
- mobile-security
language: en
raw_sha256: 0dffe3fb837529cb44845ddc4d6a95f7c9f432d12ea797b6ba7c66d4dd74367c
text_sha256: b5c6718baf97253aecdfde7e368d9f11fd74a0b27bf6aa2ec3404dbeac7cf7f5
ingested_at: '2026-06-28T07:31:59Z'
sensitivity: unknown
redactions_applied: false
---

# 3 XSS in ProtonMail for iOS

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2019-03-06_3-xss-in-protonmail-for-ios.md
- Source Type: markdown
- Detected Topics: xss, command-injection, path-traversal, mobile-security
- Ingested At: 2026-06-28T07:31:59Z
- Redactions Applied: False
- Raw SHA256: `0dffe3fb837529cb44845ddc4d6a95f7c9f432d12ea797b6ba7c66d4dd74367c`
- Text SHA256: `b5c6718baf97253aecdfde7e368d9f11fd74a0b27bf6aa2ec3404dbeac7cf7f5`


## Content

---
title: "3 XSS in ProtonMail for iOS"
url: "https://medium.com/@vladimirmetnew/3-xss-in-protonmail-for-ios-95f8e4b17054"
authors: ["Vladimir Metnew (@vladimir_metnew)"]
programs: ["Apple"]
bugs: ["XSS"]
bounty: "1,000"
publication_date: "2019-03-06"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5375
scraped_via: "browseros"
---

# 3 XSS in ProtonMail for iOS

3 XSS in ProtonMail for iOS
No, these XSSs are not so scary.
Vladimir Metnew
Follow
3 min read
·
Mar 6, 2019

138

1

# I ❤️ DOMPurify

DOMPurify is a popular XSS sanitizer by Cure53.

cure53/DOMPurify
DOMPurify - a DOM-only, super-fast, uber-tolerant XSS sanitizer for HTML, MathML and SVG. DOMPurify works with a secure…

github.com

Any defensive research could be used in offensive purposes.

DOMPurify has great XSS tests with descriptions. These tests were sourced from real DOMPurify bypasses. Moreover, DOMPurify prevents XSS in all browsers and is aware of browser-specific behaviors. So, these XSS payloads are good.

# XSS Payloads

I’ve used XSS payloads from DOMPurify 😃

# XSS
Fires in applewebdata: origin on email opening —
<svg onload=alert()//

2. Fires on click in applewebdata: origin (🤦‍♀)

<a href="javascript:alert()">

3. Fires in data: origin after loading email’s remote content

<embed src="data:text/html;base64,PHNjcmlwdD5wcm9tcHQoIlByb3Rvbm1haWwgbmVlZHMgeW91ciBwYXNzd29yZCIpPC9zY3JpcHQ+"></embed>

iframe/embed with base64 encoded html payload

Need to note, that all 3 XSS are of different categories.
Even if I’ve found a 4th XSS, it’d be likely have been considered as a duplicate.

# Impact

It wasn’t possible to escalate these XSS into RCE/LFI. At least, I didn’t find such a way.

JS execution via email is already an issue.
Privacy violation: track when the user opens the email, disclose IP, leak other info.
Phishing via prompt(), alert()
“Useless” UXSS
Press enter or click to view image in full size
# applewebdata:// origin is useless

Initially, I thought that XSSs in applewebdata: should allow reading local files. There was CVE-2016–1764 (XSS in iMessage via javascript: URI) that allows reading local files. applewebdata: was also highlighted in browser security research (UXSS) — https://runic.pl/hitb-ios-browsers.pdf.

Local files reading would be pretty impactful for a mail app.

However, this flaw was patched in Webkit(?) and now applewebdata: allows only doing UXSS in this particular case.

Anyway, UXSS is better than no UXSS, at least some privileged context :(

Additionally, Webkit forbids requests to file:// origin. Thanks to Safiler, XSSs in HelpViewer and related researches in this field.

Bo0oM/Safiler
Safari local file reader. Contribute to Bo0oM/Safiler development by creating an account on GitHub.

github.com

# Reporting

The vulnerabilities were reported on Dec 12. At first, ProtonMail security team reacted quickly, but then they disappeared for a while.

Get Vladimir Metnew’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

There was a small miscommunication on their side. As I understand, they incorrectly estimated impact of these XSSs and somehow missed that 2 XSSs in applewebdata: are pretty impactful.

Later, ProtonMail iOS engineer Anatoly (thx!) noticed my tweets and the vulnerabilities were reviewed by ProtonMail team again.

# Timeline
Dec 11: Reported XSS in applewebdata: origin with no interaction via <svg onload=alert()//
Dec 11: Reported XSS via javascript: URI in applewebdata: origin
Dec 14: Response from ProtonMail Sec team
Dec 25: Found a XSS in data: origin via <embed src=[base64_paylaod]>`
Dec 25: Reminded the security team about findings
Dec 29: ProtonMail Sec team replied that these XSSs aren’t so scary, because they don’t allow reading emails
Jan 12: Made an accent on the fact that 2 XSS fires in applewebdata:
Jan 13: Made a PoC UXSS in applewebdata: to demonstrate that XSS context could be considered as privileged.
Jan 14: ProtonMail: no emails reading => not critical.
Feb 12–13: Made a few tweets regarding my findings in ProtonMail.
Feb 14 ProtonMail replied on Twitter.
Feb 15: Andy Yen emailed me via ProtonMail: ProtonMail team made an additional review of reported vulnerabilities + apology for the miscommunication.
Feb 15: The vulnerabilities patched in the stable.
Feb 27: ProtonMail agreed to disclose the report.
# Thanks to …
All my Twitter followers 💙
Anatoly from ProtonMail iOS team for noticing my tweets about the issues in ProtonMail 😉
ProtonMail SecTeam for their continuous work on ProtonMail’s security 🚀 and for making this disclosure possible
Andy Yen for the personal review of reported vulnerabilities. Such things generally mean that security is taken seriously.
🔜 😈

More disclosures soon.

Thanks for reading!
