---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2024-08-11_stored-xss-in-libreoffice.md
original_filename: 2024-08-11_stored-xss-in-libreoffice.md
title: Stored XSS in LibreOffice
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
raw_sha256: 3221d68c39475a6dfc0e94f45236126f206a763d797c82ec7171dde01e7912a6
text_sha256: 9a5e915a3d992e436b033b38490e81b551e9fc0498ff4e9396eee17ca4bd2428
ingested_at: '2026-06-28T07:32:37Z'
sensitivity: unknown
redactions_applied: false
---

# Stored XSS in LibreOffice

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2024-08-11_stored-xss-in-libreoffice.md
- Source Type: markdown
- Detected Topics: xss, command-injection, api-security
- Ingested At: 2026-06-28T07:32:37Z
- Redactions Applied: False
- Raw SHA256: `3221d68c39475a6dfc0e94f45236126f206a763d797c82ec7171dde01e7912a6`
- Text SHA256: `9a5e915a3d992e436b033b38490e81b551e9fc0498ff4e9396eee17ca4bd2428`


## Content

---
title: "Stored XSS in LibreOffice"
url: "https://bunny0417.medium.com/stored-xss-in-libreoffice-ed4ad22e0f56"
authors: ["Aayush kumar (@bunny_0417)"]
programs: ["LibreOffice"]
bugs: ["Stored XSS"]
publication_date: "2024-08-11"
added_date: "2024-08-14"
source: "pentester.land/writeups.json"
original_index: 80
scraped_via: "browseros"
---

# Stored XSS in LibreOffice

1

Stored XSS in LibreOffice
Aayush kumar
Follow
2 min read
·
Aug 11, 2024

34

1

Without wasting any time, let’s dive in. Over time, I’ve realized that bug bounty hunting is a blend of luck and hard work. You don’t always have to put in a ton of effort — sometimes, bugs just fall into your lap.

One day, I was randomly surfing YouTube and suddenly I got a mail saying that LibreOffice had launched their bug bounty program on Intigriti, which is now closed. I immediately checked the scope, but since I wasn’t familiar with binary exploitation at the time, I decided to focus on the web assets.

Get Aayush kumar’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

After about 20 minutes, I noticed an interesting feature that allowed users to upload extensions. Additionally, there was an option to add screenshots of the extensions you created. Suddenly, I remembered a HackerOne report (https://hackerone.com/reports/964550) where the researcher was able to trigger an alert by including an XSS payload in a file.

You can read more about it here:https://shahjerry33.medium.com/xss-via-exif-data-the-p2-elevator-d09e7b7fe9b9

So I uploaded the payload : PNG

Lol”><script>alert(prompt(‘Xss By Bunny0417’))</script>
/-{IDATx E K s 9xd$# J %IR$ ( s 9Ñ evnv > q ;;;S U . = = ܿ BCb QHyԑEYՑ s$s T : x 8 إ }2` 0P @ ( j ( D J d %[

You have to find the reflection point to see the payload working which i cannot disclose for obvious reasons.But after finding it I saw my payload working :)

This was my first 4 digit bounty :)

BB TIP : Always keep an eye on new programs you can use this website — https://bbradar.io/ and always try to read hacker-one disclosed reports. Remember you cant find something that you don’t know about. Best of luck for your journey.
