---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-10-27_a-250-css-injection-my-first-finding-on-hackerone.md
original_filename: 2022-10-27_a-250-css-injection-my-first-finding-on-hackerone.md
title: A 250$ CSS Injection — My First Finding on Hackerone!
category: documents
detected_topics:
- sso
- xss
- command-injection
tags:
- imported
- documents
- sso
- xss
- command-injection
language: en
raw_sha256: 01b0a06631e0a124ae4d18a9fb564a80cf28c777f5c00079174089b9d9a26f1b
text_sha256: 6cd388675ee14b1364252543f794946475992743bc0b710f19772dd543f92376
ingested_at: '2026-06-28T07:32:15Z'
sensitivity: unknown
redactions_applied: false
---

# A 250$ CSS Injection — My First Finding on Hackerone!

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-10-27_a-250-css-injection-my-first-finding-on-hackerone.md
- Source Type: markdown
- Detected Topics: sso, xss, command-injection
- Ingested At: 2026-06-28T07:32:15Z
- Redactions Applied: False
- Raw SHA256: `01b0a06631e0a124ae4d18a9fb564a80cf28c777f5c00079174089b9d9a26f1b`
- Text SHA256: `6cd388675ee14b1364252543f794946475992743bc0b710f19772dd543f92376`


## Content

---
title: "A 250$ CSS Injection — My First Finding on Hackerone!"
url: "https://medium.com/@dsonbacker/a-250-css-injection-my-first-finding-on-hackerone-8863ad253560"
authors: ["Dsonbacker"]
bugs: ["CSS injection"]
bounty: "250"
publication_date: "2022-10-27"
added_date: "2022-10-28"
source: "pentester.land/writeups.json"
original_index: 1980
scraped_via: "browseros"
---

# A 250$ CSS Injection — My First Finding on Hackerone!

A 250$ CSS Injection — My First Finding on Hackerone!
Dsonbacker
Follow
2 min read
·
Oct 28, 2022

312

2

This is my first story on medium, to tell the story of how I found a CSS injection and exploited it, within a hackerone public program. I hope you learn a new attack vector on any real-world site you test.

Press enter or click to view image in full size

When opening the page I realized that there was a function to change the country’s flag, so I went to analyze how this feature works. And for him to change the country flag, all he had to do was make a GET request to this endpoint:

https://redacted.com/search?q=a&country=BR

So I decide to change the value of the “country” parameter to some random value, and BOOOM!! the value has been reflected. The site calls the country parameter inside the style attribute and adds it after “.svg)”

<div class="language" style="background-image: url(/BR.svg)"><div>

When I saw this, I started testing various techniques to exploit an XSS unfortunately without effect, but after a while, I remembered when I created CSS, I used “/*” to comment the “.svg)”, so I put this at the end of the load useful and thus gain control of the entire style of that element.

Get Dsonbacker’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

POC:

https://redacted.com/search?q=a&country=);width:100vw;height:100vh;background-image:url(//myserver/minions.png);/*

This flaw can be used in phishing attacks, but to steal user information the victim must use an old browser. Unfortunately, I can’t get out of the “style” attribute. So I decided to report it as a low failure, and within a week they triaged it, fixed it, and paid 250$ for the failure.

Lessons Learned:

This endpoint had been available for quite some time and many hackers just passed tools like Dalfox at this point, and since Dalfox found no flaw, they concluded that the feature was safe. So I hope you’ve learned never to trust the tool 100% and always analyze the context for reflection.

Bye-Bye, Happy Hacking!
Thank you for reading!
