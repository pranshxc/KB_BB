---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-06-09_xss-in-gmail-dynamic-email-amp-for-email.md
original_filename: 2023-06-09_xss-in-gmail-dynamic-email-amp-for-email.md
title: XSS in GMAIL Dynamic Email (AMP for Email)
category: documents
detected_topics:
- xss
- command-injection
- automation-abuse
tags:
- imported
- documents
- xss
- command-injection
- automation-abuse
language: en
raw_sha256: 93d92cd72033c9355c0a6b9bc4da34688d583f00dea1c27e4ee0b62d7b75448b
text_sha256: 813c422c574547862cdf46d96ecce762e5fbef5b123c64e50458c723ed51119e
ingested_at: '2026-06-28T07:32:22Z'
sensitivity: unknown
redactions_applied: false
---

# XSS in GMAIL Dynamic Email (AMP for Email)

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-06-09_xss-in-gmail-dynamic-email-amp-for-email.md
- Source Type: markdown
- Detected Topics: xss, command-injection, automation-abuse
- Ingested At: 2026-06-28T07:32:22Z
- Redactions Applied: False
- Raw SHA256: `93d92cd72033c9355c0a6b9bc4da34688d583f00dea1c27e4ee0b62d7b75448b`
- Text SHA256: `813c422c574547862cdf46d96ecce762e5fbef5b123c64e50458c723ed51119e`


## Content

---
title: "XSS in GMAIL Dynamic Email (AMP for Email)"
url: "https://asdqw3.medium.com/xss-in-gmail-dynamic-email-amp-for-email-3872d6052a0d"
authors: ["asdqw3"]
programs: ["Google"]
bugs: ["XSS", "HTML injection"]
bounty: "$6,000"
publication_date: "2023-06-09"
added_date: "2023-10-03"
source: "pentester.land/writeups.json"
original_index: 1063
scraped_via: "browseros"
---

# XSS in GMAIL Dynamic Email (AMP for Email)

XSS in GMAIL Dynamic Email (AMP for Email)
asdqw3
Follow
5 min read
·
Jun 9, 2023

204

2

I found a XSS vulnerability on GMAIL that I reported to Google VRP on January 2023. This issue occurs due to improper HTML parsing in GMAIL Dynamic email (AMP for Email).

بسم الله الرحمن الرحيم

AMP for Email

AMP for email allows senders to include AMP components inside rich engaging emails, making modern app functionality available within email. The AMP email format provides a subset of AMPHTML components for use in email messages, that allows recipients of AMP emails to interact dynamically with content directly in the message. (https://amp.dev/about/email)

How does it works?

An AMP email message MUST

start with the doctype <!doctype html>.
contain a top-level <html ⚡4email> tag (<html amp4email> is accepted as well).
contain <head> and <body> tags (They are optional in HTML).
contain a <meta charset="utf-8"> tag as the first child of their head tag.
contain a <script async src="https://cdn.ampproject.org/v0.js"></script> tag inside their head tag.
contain amp4email boilerplate (<style amp4email-boilerplate>body{visibility:hidden}</style>) inside their head tag to initially hide the content until AMP JS is loaded.
Example valid AMP for Email message

Specifying CSS in an AMP document

All CSS in any AMP document must be included in a <style amp-custom> tag within the header or as inline style attributes.

Custom CSS in an AMP for Email document
Discovery

As far as I know, there are two XSS vulnerabilities in GMAIL AMP which were publicly disclosed, one of them was discovered by Michał Bentkowski, you can read the writeup here https://research.securitum.com/xss-in-amp4email-dom-clobbering/ and the other one was discovered by Adi “Adico” Cohen, you can read the writeup here https://www.adico.me/post/xss-in-gmail-s-amp4email, after reading both of the writeups multiple times, I decided to give a try to explore GMAIL AMP through their playground, in the hope of finding a bypass or new XSS vector.

My first attempt was trying Adico’s payload and check what is the HTML parser do after the fix. Adico managed to find the XSS by injecting </style> closing tag into the CSS selector by encoding the letter y to \000079

Press enter or click to view image in full size
source: https://www.adico.me/post/xss-in-gmail-s-amp4email

When it sent to GMAIL, \000079 was decoded back to letter y, in the result it turn to a valid </style> close tag, then break the <style amp-custom> tag and add <img> element to the document <body>.

Press enter or click to view image in full size
source: https://www.adico.me/post/xss-in-gmail-s-amp4email

Then, I test with following payload:

It parsed into:

“<>” characters inside a string were encoded to \00003c & \00003e

\000069 decoded to letter i, but \00003c & \00003e not decoded to back to “<” & “>”

Get asdqw3’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Also noticed that div>span was fine, > character does not encoded to \00003e, so my assumption regarding Google’s fix was that they only encoded <> characters if the character present in string between “ ” or ‘ ’, make sense since the “greater than” sign (>) in the css selector is a valid symbol which used as element to element selector.

Then I tried sending “<>” characters in different locations until I found a promising spot. We are allowed to put any characters into a CSS rule set right after the property:value declaration.

source: https://www.thecodesmith.co/css/css-rulesets

For example, we are allowed to write any text or HTML tag like following:

As expected, </style> closing tag is not allowed.

Again, I tried multiple html tag combinations, then I found following snippets that surprising me when it parsed in GMAIL:

Press enter or click to view image in full size

When it sent to GMAIL, it’s parsed as follow:

Press enter or click to view image in full size

Seems like the parser still parse the </style even if it doesn’t have a closing bracket >. Also, noticed that the parser auto generated closing tag for each html tag, so what if we include <style> tag? will the parser generate the closing tag too?

The answer is YES!

Press enter or click to view image in full size
Press enter or click to view image in full size

Then I quickly tried basic <img> XSS payload, however nothing appears in the body element. It seems like they added another filter to prevent the XSS.

I tried every single html tags, no one works but <meta>. I was able to inject <meta> tag with http-equiv = refresh.

Press enter or click to view image in full size
Press enter or click to view image in full size

Final payload:

<style amp-custom>style>a{font-family:’asdqwe’</style</head><body><style/>
<meta http-equiv=”refresh” content=”10;url=data:text/html,<h1>HELLO!!</h1><script>alert()</script>”/></style>

Press enter or click to view image in full size
Press enter or click to view image in full size

After 10 seconds

Press enter or click to view image in full size
Press enter or click to view image in full size

Unfortunately, there are strict CSP rules in place on GMAIL, so the XSS not executed. Tried few times to find the bypass but no luck.

I found this bug in January 2023 and immediately report it to Google VRP and awarded a bounty of $6000 ($5000 + $1000 bonus).

Thanks
