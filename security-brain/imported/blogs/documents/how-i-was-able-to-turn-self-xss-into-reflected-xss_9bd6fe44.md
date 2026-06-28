---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2019-03-31_how-i-was-able-to-turn-self-xss-into-reflected-xss.md
original_filename: 2019-03-31_how-i-was-able-to-turn-self-xss-into-reflected-xss.md
title: How I was able to turn self xss into reflected xss
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
raw_sha256: 9bd6fe449cfd9a4f60defbee6396ce79df16eba475a2608c6a494a8fc0edc09b
text_sha256: 90ca7cb17cd54db2e6cf36db7654368f3caf2cd68c8b60b72af8ca66205cdbb0
ingested_at: '2026-06-28T07:31:59Z'
sensitivity: unknown
redactions_applied: false
---

# How I was able to turn self xss into reflected xss

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2019-03-31_how-i-was-able-to-turn-self-xss-into-reflected-xss.md
- Source Type: markdown
- Detected Topics: xss, command-injection
- Ingested At: 2026-06-28T07:31:59Z
- Redactions Applied: False
- Raw SHA256: `9bd6fe449cfd9a4f60defbee6396ce79df16eba475a2608c6a494a8fc0edc09b`
- Text SHA256: `90ca7cb17cd54db2e6cf36db7654368f3caf2cd68c8b60b72af8ca66205cdbb0`


## Content

---
title: "How I was able to turn self xss into reflected xss"
url: "https://medium.com/@heinthantzin/how-i-was-able-to-turn-self-xss-into-reflected-xss-850e3d5a2beb"
authors: ["Hein Thant Zin (@H3Lowr)"]
bugs: ["Reflected XSS"]
bounty: "300"
publication_date: "2019-03-31"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5339
scraped_via: "browseros"
---

# How I was able to turn self xss into reflected xss

How I was able to turn self xss into reflected xss
Hein Thant Zin
Follow
2 min read
·
Apr 1, 2019

202

1

Hello there ,

I’m Hein Thant Zin and just a noob bug hunter .Today , I would like to share about one of my recent finding in 
HackerOne
 ‘s private program.

Let’s say https://reacted.com

When I’m testing on this site , there is a function which you can transfer money to another account via wallet address.

https://reacted.com/manage/transfer

I put xss payload in this field and payload was automatically executed but nothing happened coz they filtered wallet adderss must start with ‘xyz’ and having 98 characters long .

So , I prepared my payload like that ,

xyzaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa<img src=x onerror=confirm(document.domain)>

Get Hein Thant Zin’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

then when I put above payload xss was fired :”) Me was like

But this is basically self xss which is not exploitable other users .So , how can i exploit other users ? I was thinking about it and about 15 minutes later , I noticed that they were provided to fill wallet address in two ways

Copy / Paste
Scanning QR image

What happens if an attacker encode his xss payload as QR image and send it to victim to transfer money ? I encoded my payload like that

Press enter or click to view image in full size

And then I scanned my qr code and payload was automatically executed then pop up alert . That is enough to exploit other users coz there is no need user action to execute payload and encoded QR image can’t visible as plaintext.

I quickly wrote report and reported to security team.They triaged my report and awarded $300 bounty for my finding. :”)

Thanks for reading…….
