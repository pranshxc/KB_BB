---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-02-02_idor-inside-the-session-storage.md
original_filename: 2023-02-02_idor-inside-the-session-storage.md
title: IDOR - Inside the Session Storage
category: documents
detected_topics:
- access-control
- idor
- command-injection
tags:
- imported
- documents
- access-control
- idor
- command-injection
language: en
raw_sha256: aff3fe77207deab30bb1f8eda88db341877da7266c705402dd6eaf12312a2ee8
text_sha256: 91d5f11f2d486720256f629ff7e216abf006a6bdcfa24cbbe926bc948e9c6a6b
ingested_at: '2026-06-28T07:32:17Z'
sensitivity: unknown
redactions_applied: false
---

# IDOR - Inside the Session Storage

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-02-02_idor-inside-the-session-storage.md
- Source Type: markdown
- Detected Topics: access-control, idor, command-injection
- Ingested At: 2026-06-28T07:32:17Z
- Redactions Applied: False
- Raw SHA256: `aff3fe77207deab30bb1f8eda88db341877da7266c705402dd6eaf12312a2ee8`
- Text SHA256: `91d5f11f2d486720256f629ff7e216abf006a6bdcfa24cbbe926bc948e9c6a6b`


## Content

---
title: "IDOR - Inside the Session Storage"
url: "https://shahjerry33.medium.com/idor-inside-the-session-storage-88af485fc899"
authors: ["Jerry Shah (@Jerry)"]
bugs: ["IDOR"]
publication_date: "2023-02-02"
added_date: "2023-02-16"
source: "pentester.land/writeups.json"
original_index: 1587
scraped_via: "browseros"
---

# IDOR - Inside the Session Storage

IDOR - Inside the Session Storage
Jerry Shah (Jerry)
Follow
4 min read
·
Feb 2, 2023

461

3

Summary

IDOR stands for Insecure Direct Object Reference which is a vulnerability that falls under the broken access control category. In brief, this vulnerability arises when an application uses user-supplied input to access an object directly. Using insecure direct object reference vulnerability it is possible to gain horizontal privilege escalation and in some cases it can lead to vertical privilege escalation as well.

Description

I have found this vulnerability in one of the private program which went duplicate. The application was storing the user_id in the session storage of the application and this user id was bound to the user’s account. It was a very simple and straight forward bug where no access control check was being performed on the user_id of the user’s account. Simply changing the value led to horizontal privilege escalation. I was able to use another user’s account where I was able to manipulate the available funds.

What is session storage ?

Session storage is a web storage API that allows data to be stored in a web browser for a single session. Session storage is similar to local storage but the only difference is that, that the data is cleared when the browser is closed or the particular session is ended.

Session storage can be used to store user data, such as form data, during a user’s session, improving the user experience by reducing the need to send requests to a server.

Anatomy of IDORs and Session Storage

Unlike normal IDORs, the IDORs with session storage are different in nature as they do not make permanent changes at times however the severity is still the same.

Press enter or click to view image in full size
Anatomy

Normal IDORs

In normal IDORs behaviour you can change the victim’s profile settings permanently unless the victim visits his/her profile and revert the change.

IDORs in sessionStorage

In this kind of IDORs the changes are not made on the permanent basis as the attack is being performed via sessionStorage. As soon as the browser is closed or the particular session ends the changes you made (for e.g. horizontal privilege escalation) will be reverted due to the nature of sessionStorage.

Get Jerry Shah (Jerry)’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

How I found this vulnerability ?

I went to target website, where you can see the balance (right side)
Press enter or click to view image in full size
Target Website

2. I right clicked > Inspect > Storage > Session Storage > http://target.com

Press enter or click to view image in full size
Inspect
Press enter or click to view image in full size
Session Storage

3. Then I changed the user_id to victim’s user_id and reloaded the page

Press enter or click to view image in full size
Changing user_id
Press enter or click to view image in full size
Reloading the page

4. I entered to the victim’s account

Press enter or click to view image in full size
Victim’s Account

Why this happened ?

In my opinion,

This happened because the user_id was bound to the user’s account and no access check was performed on it which led to this vulnerability.

Impact

Any user is able to access the account’s of another user’s which can lead to horizontal privilege escalation and in some case it might lead to vertical privilege escalation as well.

Calculated CVSS

Vector String : CVSS:3.0/AV:N/AC:L/PR:N/UI:N/S:C/C:L/I:L/A:L

Score : 8.3 (High)

Mitigation

Access check should be performed and verification of all the referenced objects should be done. An authentication and authorization check should also be performed. Apart from it the ids should be made alpha-numeric in order to prevent it from guessing.

Press enter or click to view image in full size
