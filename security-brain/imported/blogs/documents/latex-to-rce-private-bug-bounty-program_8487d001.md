---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2018-07-06_latex-to-rce-private-bug-bounty-program.md
original_filename: 2018-07-06_latex-to-rce-private-bug-bounty-program.md
title: Latex to RCE, Private Bug Bounty Program
category: documents
detected_topics:
- ssrf
- xss
- command-injection
- api-security
tags:
- imported
- documents
- ssrf
- xss
- command-injection
- api-security
language: en
raw_sha256: 8487d001adb94a8dc152345e03faf293e1e503ecff9a4e414719e19341a69bbb
text_sha256: a24e5a5be67873c1e76c1f2739db7a079d09e384178f51bc10f80924af49d07c
ingested_at: '2026-06-28T07:31:57Z'
sensitivity: unknown
redactions_applied: false
---

# Latex to RCE, Private Bug Bounty Program

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2018-07-06_latex-to-rce-private-bug-bounty-program.md
- Source Type: markdown
- Detected Topics: ssrf, xss, command-injection, api-security
- Ingested At: 2026-06-28T07:31:57Z
- Redactions Applied: False
- Raw SHA256: `8487d001adb94a8dc152345e03faf293e1e503ecff9a4e414719e19341a69bbb`
- Text SHA256: `a24e5a5be67873c1e76c1f2739db7a079d09e384178f51bc10f80924af49d07c`


## Content

---
title: "Latex to RCE, Private Bug Bounty Program"
url: "https://medium.com/bugbountywriteup/latex-to-rce-private-bug-bounty-program-6a0b5b33d26a"
authors: ["Yashar Shahinzadeh (@YShahinzadeh)"]
bugs: ["RCE"]
publication_date: "2018-07-06"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5818
scraped_via: "browseros"
---

# Latex to RCE, Private Bug Bounty Program

Latex to RCE, Private Bug Bounty Program
Yasho
Follow
2 min read
·
Jul 7, 2018

211

1

I had participated in a private bug bounty program about one year ago, I want to publish what I’ve learned from. The CMS was a journal site giving service to authors, editors and etc. I accomplished to get editor account by an XSS which I’m not going through with this story.

In the editor’s role, there were many options, interesting ones were “XML checker” and “Converting LaTex codes to PDF”. The first one lets which is not related to our topic, the second one seemed interesting.

Press enter or click to view image in full size
Converting LaTex code to PDF

A remote attacker can gain remote command execution thanks to LaTex code conversion, following links might be helpful:

https://tex.stackexchange.com/questions/262625/security-latex-injection-hack
https://0day.work/hacking-with-latex/
http://scumjr.github.io/2016/11/28/pwning-coworkers-thanks-to-latex/

So I crafted an exploit code shown below in order to read local files in the server:

Press enter or click to view image in full size

Resulted in :

Press enter or click to view image in full size
Get Yasho’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Bingo, I’d the /etc/passwd content. The payload to command execution:

Resulted in:

Press enter or click to view image in full size
Out of Band Technique

The PDF conversion was annoying, I wanted to escalate my privileged, so I automated the procedure by

Writing a code exploiting the flaw (LaTex to PDF)
Writing a server by python receiving the result, converting it to clear text, saving it.

The flow is shown below:

Press enter or click to view image in full size

Consequently:

Press enter or click to view image in full size

Afterward, I got conformable with this exploit, seeking the server, I got the database and Elastic-Search by SSRF and had fun.
