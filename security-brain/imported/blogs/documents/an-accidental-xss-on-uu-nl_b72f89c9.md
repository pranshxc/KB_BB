---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-02-11_an-accidental-xss-on-uunl.md
original_filename: 2021-02-11_an-accidental-xss-on-uunl.md
title: An Accidental XSS on uu.nl
category: documents
detected_topics:
- xss
- command-injection
- api-security
tags:
- imported
- documents
- xss
- command-injection
- api-security
language: en
raw_sha256: b72f89c957a97ea561642665d09c63bc179119631c75f1bc932b4830579865f9
text_sha256: fe1aa06aab459916afac8b801872d94802755e116e5dfaece2c2e39650336c50
ingested_at: '2026-06-28T07:32:04Z'
sensitivity: unknown
redactions_applied: false
---

# An Accidental XSS on uu.nl

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-02-11_an-accidental-xss-on-uunl.md
- Source Type: markdown
- Detected Topics: xss, command-injection, api-security
- Ingested At: 2026-06-28T07:32:04Z
- Redactions Applied: False
- Raw SHA256: `b72f89c957a97ea561642665d09c63bc179119631c75f1bc932b4830579865f9`
- Text SHA256: `fe1aa06aab459916afac8b801872d94802755e116e5dfaece2c2e39650336c50`


## Content

---
title: "An Accidental XSS on uu.nl"
url: "https://santoshdbobade.blogspot.com/"
final_url: "https://santoshdbobade.blogspot.com/"
authors: ["Santosh Bobade (@Santosh88267387)"]
programs: ["Utrecht University"]
bugs: ["XSS"]
publication_date: "2021-02-11"
added_date: "2022-11-08"
source: "pentester.land/writeups.json"
original_index: 3920
---

### [An Accidental XSS on uu.nl](https://santoshdbobade.blogspot.com/2021/02/an-accidental-xss-onuunl.html)

  * Get link
  * Facebook
  * X
  * Pinterest
  * Email
  * Other Apps

[ February 11, 2021  ](https://santoshdbobade.blogspot.com/2021/02/an-accidental-xss-onuunl.html "permanent link")

![Image](https://lh3.googleusercontent.com/blogger_img_proxy/AEn0k_vV67Zk2TNsaiJ7VaDlzRZ0D0rjlRfsm5r-1ahBZuGoip78rBQnDYV-AjpqVAT9Uf4-TND0r2bzrc9IAxxhsiWB4ngJGTgEdEzqGWpA4Yti0LQDSIJ7RYCL2VV6oyDZJkDtFSDUQGPk)

Hello guys, I hope you enjoyed my previous blog. Today I am talking about how I got an accidental XSS on uu.nl Let’s start 1)First I Enumerate subdomain of uu.nl and I selected www.*.uu.nl subdomain for testing. (sorry for not to a disclosed subdomain) 2)I used “waybackurls” and collected all URL’s of the target. I found an interesting URL: https://www.*.uu.nl/XXXXXX/?uuid=vulnerablepoint I checked out where it reflected, I saw it reflects in between title tag, now balanced the tag Payload: test</title><script>alert(document.domain)</script> Successfully reflected XSS done Hall Of Fame: I hope you enjoyed my writeup follow me on LinkedIn: https://www.linkedin.com/in/santosh-bobade-531094192/ Twitter: https://twitter.com/Santosh88267387?s=09 Thanks….! 

[](https://santoshdbobade.blogspot.com/2021/02/an-accidental-xss-onuunl.html)

[ 8 comments  ](https://santoshdbobade.blogspot.com/2021/02/an-accidental-xss-onuunl.html#comments)

[ Read more ](https://santoshdbobade.blogspot.com/2021/02/an-accidental-xss-onuunl.html "An Accidental XSS on uu.nl")
