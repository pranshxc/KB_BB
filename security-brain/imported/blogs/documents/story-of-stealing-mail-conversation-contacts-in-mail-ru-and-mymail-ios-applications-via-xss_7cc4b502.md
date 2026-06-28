---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-06-30_story-of-stealing-mail-conversation-contacts-in-mailru-and-mymail-ios-applicatio.md
original_filename: 2020-06-30_story-of-stealing-mail-conversation-contacts-in-mailru-and-mymail-ios-applicatio.md
title: Story of stealing mail conversation, contacts in mail.ru and myMail iOS applications
  via XSS
category: documents
detected_topics:
- xss
- sqli
- command-injection
- mobile-security
tags:
- imported
- documents
- xss
- sqli
- command-injection
- mobile-security
language: en
raw_sha256: 7cc4b502153627b958dd4c266ff613209cda3fe5ba90090ed4c934d30eb877ba
text_sha256: 1258831bfb2849e2667cc5f8fd4800e23ca4dbc6c4343cc099583a981129b262
ingested_at: '2026-06-28T07:32:02Z'
sensitivity: unknown
redactions_applied: false
---

# Story of stealing mail conversation, contacts in mail.ru and myMail iOS applications via XSS

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-06-30_story-of-stealing-mail-conversation-contacts-in-mailru-and-mymail-ios-applicatio.md
- Source Type: markdown
- Detected Topics: xss, sqli, command-injection, mobile-security
- Ingested At: 2026-06-28T07:32:02Z
- Redactions Applied: False
- Raw SHA256: `7cc4b502153627b958dd4c266ff613209cda3fe5ba90090ed4c934d30eb877ba`
- Text SHA256: `1258831bfb2849e2667cc5f8fd4800e23ca4dbc6c4343cc099583a981129b262`


## Content

---
title: "Story of stealing mail conversation, contacts in mail.ru and myMail iOS applications via XSS"
url: "https://medium.com/kminthein/story-of-stealing-mail-conversation-contacts-in-mail-ru-and-mymail-ios-applications-via-xss-1e49c4ed560"
authors: ["kminthein / weev3 (@kyawminthein99)"]
programs: ["Mail.ru"]
bugs: ["Stored XSS"]
bounty: "1,000"
publication_date: "2020-06-30"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4460
scraped_via: "browseros"
---

# Story of stealing mail conversation, contacts in mail.ru and myMail iOS applications via XSS

Story of stealing mail conversation, contacts in mail.ru and myMail iOS applications via XSS
kminthein
Follow
4 min read
·
Jun 30, 2020

230

1

In June 2020, I found a stored XSS bug that could allow an attacker to steal user email conversations, contacts in mail.ru and myMail iOS applications (version 12.2.1). Mail.ru is one of the biggest organization in Russian and registered over 100 Millions active accounts.

The Story of the Bug

The bug occurs due to lack of validation in SVG image file. An example of SVG XSS is

<?xml version="1.0" standalone="no"?>
<!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 1.1//EN" "http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd">
<svg version="1.1" baseProfile="full" xmlns="http://www.w3.org/2000/svg">
<polygon id="triangle" points="0,0 0,50 50,0" fill="#009900" stroke="#004400"/>
<script type="text/javascript">
alert("XSS");
</script>
</svg>

When a user viewed above SVG file, XSS is pop-up as shown in below.

Press enter or click to view image in full size
Finding valuable file

I stared hating to report without showing an impact and also XSS in attachment is most likely to close as informative in mail application. So, I stared digging around the application file structure.

Get kminthein’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

First, I just thinking about dumping /etc/passwd as PoC but in iPhone /etc/passwd is just a sandbox feature and so I have to retrieve something. Luckily, I have jailbroken iPhone 5 and so I can view every file and folder within iPhone. Application data in iOS file structure stored in /private/var/mobile/Containers/Shared/AppGroup/followed by random folder as shown in below.

Press enter or click to view image in full size

I asked myself, how I can know which folder contains mail.ru application data. The folders name will not be same in every iPhone(folder itself and some files inside that folder will remain the same) and I realized that I need to get folder path via XSS. So, I used alert(location.href); in SVG file and send a mail to myself, after that I got folder location.

Press enter or click to view image in full size

Then I browse to that folder and saw few SQLite database files + some folders.

Press enter or click to view image in full size

After downloading and viewing each file in that folder, I realized that mail_cache.sq3 file contains email conversation, contacts, payment information and almost everything.

Press enter or click to view image in full size
Press enter or click to view image in full size
Email Conversations
Press enter or click to view image in full size
Contacts

So, I choose to retrieve this SQLite database to my server. If I can get this database, it is enough to show the impact of this XSS bug and I can reported with a nice PoC to mail.ru. I start writing my PoC script, viewed crafted SVG file in my iPhone(which has no jailbreak) and yes I can verify the file exists by popping the contents of the file.

Press enter or click to view image in full size
Defeating errors and writing a workable PoC

So, I stared to write a PoC in order to upload whole SQLite database to my server but I got a lot of errors and only some small portions of the file is send to my server. After fixing errors over 4 hrs, I can upload whole SQLite database file to my server with below SVG file.

Press enter or click to view image in full size
PoC script for dumping mail_cache.sq3

The script firstly read mail.ru folder location, read the mail_cache.sq3 folder and then upload the whole file to attacker controlled server. Then I send this SVG file to user who used mail.ru and my.com applications. If user viewed attacker crafted SVG file, his SQLite database(containing email conversations, contacts ..etc.) will send to attacker and attacker can view email conversations, contacts ..etc as shown in below.

Conclusion

I quickly reported to the program and Mail.ru rewarded $1000 as a bounty. Thanks for your reward :).

Press enter or click to view image in full size

The program manager said, this is not Stored XSS vulnerability and the bug is Cross application scripting (CAS). For my understanding, the vulnerability that can execute JavaScript in iOS is called XSS. May be I was wrong or ..

Press enter or click to view image in full size

After they fixed the bug, I request them to disclose about my report and they confirmed they will disclose the bug in few weeks so I have a permission to write about the bug in Medium :).
