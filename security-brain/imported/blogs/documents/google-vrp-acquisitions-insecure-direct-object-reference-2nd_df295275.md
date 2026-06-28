---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-11-10_google-vrp-acquisitions-insecure-direct-object-reference-2nd.md
original_filename: 2022-11-10_google-vrp-acquisitions-insecure-direct-object-reference-2nd.md
title: Google VRP (Acquisitions) — [Insecure Direct Object Reference] 2nd
category: documents
detected_topics:
- idor
- command-injection
tags:
- imported
- documents
- idor
- command-injection
language: en
raw_sha256: df2952750c4a8a979add6ee52912ecc13f96a88785e5cdb4009a604e745e71d9
text_sha256: 80fc9f81d3d2df9e9c57d4a43bf5b4f8668078bdcb7e051cb47d33ef2e49b967
ingested_at: '2026-06-28T07:32:15Z'
sensitivity: unknown
redactions_applied: false
---

# Google VRP (Acquisitions) — [Insecure Direct Object Reference] 2nd

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-11-10_google-vrp-acquisitions-insecure-direct-object-reference-2nd.md
- Source Type: markdown
- Detected Topics: idor, command-injection
- Ingested At: 2026-06-28T07:32:15Z
- Redactions Applied: False
- Raw SHA256: `df2952750c4a8a979add6ee52912ecc13f96a88785e5cdb4009a604e745e71d9`
- Text SHA256: `80fc9f81d3d2df9e9c57d4a43bf5b4f8668078bdcb7e051cb47d33ef2e49b967`


## Content

---
title: "Google VRP (Acquisitions) — [Insecure Direct Object Reference] 2nd"
url: "https://caesarevan23.medium.com/google-vrp-acquisitions-insecure-direct-object-reference-2nd-2ece9b185ade"
authors: ["Caesar Evan Santoso"]
programs: ["Google"]
bugs: ["IDOR"]
publication_date: "2022-11-10"
added_date: "2022-11-11"
source: "pentester.land/writeups.json"
original_index: 1931
scraped_via: "browseros"
---

# Google VRP (Acquisitions) — [Insecure Direct Object Reference] 2nd

Google VRP (Acquisitions) — [Insecure Direct Object Reference] 2nd
Caesar Evan Santoso
Follow
3 min read
·
Nov 10, 2022

128

2

Press enter or click to view image in full size
Google VRP

Hi All!, Yuuppp…It’s me again! XD. As the title suggests, I will share how I found the [Insecure Direct Object Reference] vulnerability in one of Google’s acquisitions (https://www.appsheet.com/).

Description

AppSheet is an application that provides a no-code development platform for application software, which allows users to create mobile, tablet, and web applications using data sources like Google Drive, DropBox, Office 365, and other cloud-based spreadsheet and database platforms.
https://www.appsheet.com/

Proof Of Concept

After I did some tests on the menu, I got one menu where this menu will send a template to send an Email and the template will enter our Google Docs or Drive.

App “B” (Attacker) & “C” (Victim)

Here I create 2 accounts where the account from the profile picture “B” is the Attacker, and “C” is the Victim.

Press enter or click to view image in full size
Attacker “B”
Press enter or click to view image in full size
Victim “C”

It can be seen in the image below that the last document named “Victim” is the last document of this Victim account.

Press enter or click to view image in full size
Request “Attacker” & “Victim”

To make it easier here I will share the ID differences in my two accounts

ID Attacker & Victim

And here is the Request from “Attacker”

Press enter or click to view image in full size
ID Attacker

And here is the Request of “Victim”

Press enter or click to view image in full size
ID Victim
Test IDOR & Spamming Docs Victim

Here I use Burpsuite’s Intruder and change the “ID” of the “Attacker ID” to the ID of the “Victim”.

Press enter or click to view image in full size
Intruder BurpSuite

It can be seen in the Response image below that it displays a successful response and there is also a response related to the Docs sent to the Victim’s Docs.

Press enter or click to view image in full size
FileName : DocId

And if I look at the Docs belonging to the “Victim” account it will get Spam from this

Press enter or click to view image in full size
Press enter or click to view image in full size
Questions & Answers
How do I find the ID ?
You can rely on Google Search to find these ID
Press enter or click to view image in full size

2. For “Version” do we have to follow the victim’s Version ?
No, you can use your own “Version” and do not have to follow the victim’s Version.

Timeline

> 27 Sep 2022 : Get IDOR and Report to Google
> 10 Okt 2022 : Nice Catch!
> 11 Okt 2022 : The VRP panel has decided to issue a reward of $XXX for my report
> 6 Nov 2022 : Fixed!

Press enter or click to view image in full size
Follow Me

https://www.linkedin.com/in/c3van/

Get Caesar Evan Santoso’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Sheeeeessshhhhhh!
