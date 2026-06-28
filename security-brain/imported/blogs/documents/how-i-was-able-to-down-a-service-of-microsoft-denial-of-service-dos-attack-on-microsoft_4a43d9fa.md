---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-05-21_how-i-was-able-to-down-a-service-of-microsoft-denial-of-service-dos-attack-on-mi.md
original_filename: 2022-05-21_how-i-was-able-to-down-a-service-of-microsoft-denial-of-service-dos-attack-on-mi.md
title: How I was able to down a service of Microsoft ? Denial of Service (DOS) Attack
  on Microsoft.
category: documents
detected_topics:
- command-injection
- rate-limit
tags:
- imported
- documents
- command-injection
- rate-limit
language: en
raw_sha256: 4a43d9fa5eab7f4584459c959aeab7fb7c0e881e802fa9ada685f31210ec4c37
text_sha256: b26f7e036fe182cc109fe0c56354b3afd4a11f1ca644fd73c6ba2bda3e7793ca
ingested_at: '2026-06-28T07:32:11Z'
sensitivity: unknown
redactions_applied: false
---

# How I was able to down a service of Microsoft ? Denial of Service (DOS) Attack on Microsoft.

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-05-21_how-i-was-able-to-down-a-service-of-microsoft-denial-of-service-dos-attack-on-mi.md
- Source Type: markdown
- Detected Topics: command-injection, rate-limit
- Ingested At: 2026-06-28T07:32:11Z
- Redactions Applied: False
- Raw SHA256: `4a43d9fa5eab7f4584459c959aeab7fb7c0e881e802fa9ada685f31210ec4c37`
- Text SHA256: `b26f7e036fe182cc109fe0c56354b3afd4a11f1ca644fd73c6ba2bda3e7793ca`


## Content

---
title: "How I was able to down a service of Microsoft ? Denial of Service (DOS) Attack on Microsoft."
page_title: "How I was able to down the service of Microsoft? Denial of Service (DOS) Attack on Microsoft. | by Harsh Banshpal | System Weakness"
url: "https://medium.com/@harshbanshpal/how-i-was-able-to-down-a-service-of-microsoft-denial-of-service-dos-attack-on-microsoft-ec9d599ab3f8"
authors: ["Harsh Banshpal (@harshbanshpal)"]
programs: ["Microsoft"]
bugs: ["DoS"]
publication_date: "2022-05-21"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 2621
scraped_via: "browseros"
---

# How I was able to down a service of Microsoft ? Denial of Service (DOS) Attack on Microsoft.

How I was able to down the service of Microsoft? Denial of Service (DOS) Attack on Microsoft.
Harsh Banshpal
Follow
3 min read
·
May 21, 2022

85

1

Thank you for taking the time to read about “How I was able to down service of Microsoft? Denial of Service (DOS) Attack on Microsoft“

Press enter or click to view image in full size
Application Level DOS Attack on Microsoft

Hello Readers, I’m Harsh Banshpal [ @harsh_ban_ ] , hope you are doing great, So without wasting time lets start…

What is a Denial of Service (DOS) Attack?
A Denial-of-Service (DoS) attack is an attack meant to shut down a machine or network, making it inaccessible to its intended users. DoS attacks accomplish this by flooding the target with traffic or sending it information that triggers a crash.

Now, you are aware of the DOS attack if you didn’t know about it!

While doing my research on Microsoft I encountered a chat service https://biz4afrika.microsoft.com/chat. I tried some possible attacks, but I found a “no rate limit” issue.

Unsatisfied

So, I took a tea break and start thinking about what should I have to try next?
Then, I tried to send a long string payload message & the message was not delivered.

Something is fishy !!

Then, I opened the burp suite & analyzed the request on the repeater tab & saw 502 Bad Gateway status code 😃

Press enter or click to view image in full size
Hacker Mode On !

Then, I send that request to intruder tab & started the attack for multiple time.

Get Harsh Banshpal’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

After that I opened https://biz4afrika.microsoft.com/chat in another browser & try to send a message & boom the message was not delivered.

Press enter or click to view image in full size

Then, I stopped the attack immediately & reported the vulnerability to Microsoft.

Bug Reported — 21 January, 2022

Bug Fixed — 2 March, 2022

Reward —Hall of Fame

(Security Researcher Acknowledgments for Microsoft Online Services)

Bounty — Out of Scope

Hope, you learnt something !

Video POC: https://youtu.be/mXMW-O4yuxE

Thanks to Khushi Agrawal & Saransh Saraf for the help.

You can connect with me on-

Linkedin: https://www.linkedin.com/in/harshbanshpal/

Instagram: https://www.instagram.com/harsh_ban_/

Twitter: https://twitter.com/harshbanshpal
