---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-10-07_insecure-comments.md
original_filename: 2022-10-07_insecure-comments.md
title: Insecure Comments
category: documents
detected_topics:
- idor
- access-control
- command-injection
- api-security
tags:
- imported
- documents
- idor
- access-control
- command-injection
- api-security
language: en
raw_sha256: dcb821a1c1c8e853227ad57ef2f05d2ae2cb9b65c02bca6a4d4239903bd3d620
text_sha256: 85971bf670e7f4a08d262c9b5a5ffb131d617fe10ec6f481816529779a19a729
ingested_at: '2026-06-28T07:32:14Z'
sensitivity: unknown
redactions_applied: false
---

# Insecure Comments

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-10-07_insecure-comments.md
- Source Type: markdown
- Detected Topics: idor, access-control, command-injection, api-security
- Ingested At: 2026-06-28T07:32:14Z
- Redactions Applied: False
- Raw SHA256: `dcb821a1c1c8e853227ad57ef2f05d2ae2cb9b65c02bca6a4d4239903bd3d620`
- Text SHA256: `85971bf670e7f4a08d262c9b5a5ffb131d617fe10ec6f481816529779a19a729`


## Content

---
title: "Insecure Comments"
url: "https://mearegtu.medium.com/insecure-comments-73399193f804"
authors: ["Meareg"]
programs: ["Microsoft"]
bugs: ["IDOR", "Broken authorization"]
publication_date: "2022-10-07"
added_date: "2022-10-08"
source: "pentester.land/writeups.json"
original_index: 2073
scraped_via: "browseros"
---

# Insecure Comments

Insecure Comments
Meareg | ማዕረግ | 𐩧𐩴oמארג | 𐩣
Follow
5 min read
·
Oct 7, 2022

10

Hi All,

This is my blog regarding to impersonating and publishing a comment on behalf of any Microsoft Word and PowerPoint users. Interestingly, Excel and Visio are secure, they handle the comments in a different way (secure way).

I report the vulnerability to Microsoft but it is classified as ‘by-design’. Personally, I strongly believe this is a vulnerability with huge risks.

What an attacker can do with it?

Create a comment on a document behalf of any Microsoft 365 users — without their awareness
Adding users as an author on a document without their involvement

Attackers can use the above security loopholes for successful phishing campaigns and tampering with the integrity of a document.

Introduction

A comment has 3 components:

1. An author (a person who initiates the conversation - usually the logged-in user or a person with the document shared)

2. A message/body of the comment

3. The document - the main body which the comment attached on it

This is an example of Microsoft Word. Here is a scenario where a user abel@msobb*.onmicrosoft.com will impersonate and comment on behalf of another user in the same tenant. It should be noted that it also works cross-tenant.

Document Name: September
Author: Abel John 
Comment Body: PoC Document 

The above user Abel is comment on a document — ‘September.docx’:

Press enter or click to view image in full size
Fig 0x00 — Abel commenting on his document

Let’s see the API call:

POST /we/OneNote.ashx?perfTag=PutChanges_1
Host: euc-word-edit.officeapps.live.com
Press enter or click to view image in full size
Fig 0x01- Vulnerable endpoint

These are important parameters the name of the author and the string which starts with ‘S::abel@msobb….onmicrosoft.com::3b64……27a’

"Abel John",
4668585..,
"Abel John",
.
"S::abel@msobb….onmicrosoft.com::3b64……27a" -> 
S::<author_email>::Object ID of the user
Press enter or click to view image in full size
Fig 0x03 — Original request without tampering parameters

From the above section, I hope it is clear how the API calls responsible for commenting on a Word document work. Now, let’s see how an attacker can tamper to add a comment on behalf of any user within a tenant. In order to, achieve this we need the victim’s email address, first & last name, and object ID.

Note — we can find this information easily from Microsoft Team external user search feature.

Here is an example, of how Abel John (attacker) can impersonate and comment on behalf of Chris Brown (victim).

Replace the display name from ‘Abel John’ with ‘Chris Brown (CFO)’, email address, and Object ID.

"Chris Brown (CFO)", 
4668585..,
"Chris Brown (CFO)",
.
"S::chris@msobb....onmicrosoft.com::74a75f...........90e" -> 
S::<victim_email>::Object ID of the victim
Press enter or click to view image in full size
Fig 0x04 — Tampered request

After replacing with the victim’s detail and refresh the page, I am able to successfully comment behalf of the victim user.

Press enter or click to view image in full size
Fig 0x05 — Who is the author?

[Optional Step ] Adding another comment

Get Meareg | ማዕረግ | 𐩧𐩴oמארג | 𐩣’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Repeat the above process and replace the victim email on the membership parameter

Press enter or click to view image in full size
Fig 0x06 — Membership

The result from UI perspective:

Press enter or click to view image in full size
Fig 0x07 — Replay on a comment

You can see the details of the document on OneNote, in the ‘Activities’ section ‘Chris Brown’ is commenting on the document. His details are used to comment on the document without his involvement.

Press enter or click to view image in full size
0x08 — Recent activities on the document

More importantly, ‘Chris Brown’ is now the author of the document without his awareness as it is seen in the version history.

Press enter or click to view image in full size
0x09 — Version History
Press enter or click to view image in full size
0x10 — Chris Brown is now author of the document

Another Example

A user abel@msobb???.onmicrosoft.com (display name labeled Author #2 — Abel John), creates a document (labeled — Document Name #1) and added a new comment (labeled — Message Body #3).

Press enter or click to view image in full size
Fig 0x01 — Original comment before manipulating the request

Note:

Anyone can edit the comment if this document is shared with edit right. However, this document is not shared with anyone.

Closer look of the API call & interesting parameters:

Press enter or click to view image in full size
Fig 0x02 — Underlying API call
...
"Properties":[
  "-180",
  469777582,
  "Abel John",
  469780650,
  "PoC\n",
  469780707,
  "S::abel@msobbXXXX.onmicrosoft.com::3b6XXXXX-XXXX-XXXXX-bd12-10XXXXXXXXX",
  469780708,
  "AD",
  469780740,
  "[]",
  469780777,
  "",
  ....

Now let’s impersonate and comment behalf of other users. In order to, exploit this vulnerability we need email address (UPN), display name and object ID. All this information can be found using Microsoft Teams external search feature.

For this example, I will use Microsoft Security Response Center email address and object ID.

Note — you can impersonate any user within or outside of your tenant.

...
"Properties":[
  "-180",
  469777582,
  "Microsoft Security Response Center",(Display name we want to impersonate)
  469780650,
  "PoC\n",
  469780707,
  "S::secxxxxxx@xxxxxxx.com::2XXXXX-XXXX-XXXXX-bd12-10XXXXXXXXX",(S::UPN::Object ID of the user we want to impersonate)
  469780708,
  "AD",
  469780740,
  "[]",
  469780777,
  "",
  ....

Replace the above parameters

Display Name from Abel John -to-  Microsoft Security Response Center
S::abel@msobbxxx.onmicosoft.com::ObjectID -to- S::secxxx@xxxxxxx.com::ObjectID
Press enter or click to view image in full size
Fig 0x03 — Edited request

We successfully impersonate and comment behalf of Microsoft Security Response Center user:

Press enter or click to view image in full size
Fig 0x04 — Output of the above request
Press enter or click to view image in full size
Fig 0x05 — Download & examine the file — still the author of the comment is MSRC

Microsoft Reason

Microsoft believes this issue is by design and refers to this online resource. It says ‘anyone with edit access to your file can edit your comment’ but in my PoC the victim is not involved at all.

Note: Keep in mind that it's possible for others to edit your comments. Comments in an Office document are stored in the file, so anyone with edit access to your file can edit your comment.

Timeline

Aug 05–2022 — Reported and received Case ID

Aug 10–2022 — Microsoft Classify the issue as ‘by design’

Aug 10–2022 — Explain and send more PoC

Aug 12–2022 — Microsoft decide ‘by design’

Aug 12–2022 — Draft sent for public disclosure

Sep 13- 2022- Microsoft Approved Publication
