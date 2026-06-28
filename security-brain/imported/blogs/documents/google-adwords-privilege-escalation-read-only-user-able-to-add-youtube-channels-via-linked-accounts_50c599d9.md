---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2019-05-21_google-adwordsprivilege-escalation-read-only-user-able-to-add-youtube-channels-v.md
original_filename: 2019-05-21_google-adwordsprivilege-escalation-read-only-user-able-to-add-youtube-channels-v.md
title: 'Google Adwords(Privilege Escalation): Read-only user able to add YouTube channels
  via Linked accounts'
category: documents
detected_topics:
- access-control
- command-injection
- api-security
tags:
- imported
- documents
- access-control
- command-injection
- api-security
language: en
raw_sha256: 50c599d9c2dbc6aa0376ea9f3e698966ed59278b90f5775b57edef1629370704
text_sha256: bfb0e0b4969efe03e65c221aa44218af8c1c44116cc84f0790ec940c64d1a493
ingested_at: '2026-06-28T07:31:59Z'
sensitivity: unknown
redactions_applied: false
---

# Google Adwords(Privilege Escalation): Read-only user able to add YouTube channels via Linked accounts

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2019-05-21_google-adwordsprivilege-escalation-read-only-user-able-to-add-youtube-channels-v.md
- Source Type: markdown
- Detected Topics: access-control, command-injection, api-security
- Ingested At: 2026-06-28T07:31:59Z
- Redactions Applied: False
- Raw SHA256: `50c599d9c2dbc6aa0376ea9f3e698966ed59278b90f5775b57edef1629370704`
- Text SHA256: `bfb0e0b4969efe03e65c221aa44218af8c1c44116cc84f0790ec940c64d1a493`


## Content

---
title: "Google Adwords(Privilege Escalation): Read-only user able to add YouTube channels via Linked accounts"
page_title: "Google Adwords(Privilege Escalation):  Read-only user able to add YouTube channels via  Linked accounts"
url: "https://whitehatfamilyguy.blogspot.com/2019/06/google-adwordsprivilege-escalation-read.html"
final_url: "https://whitehatfamilyguy.blogspot.com/2019/06/google-adwordsprivilege-escalation-read.html"
authors: ["Family guy"]
programs: ["Google"]
bugs: ["Privilege escalation", "Broken authorization"]
publication_date: "2019-05-21"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5251
---

###  Google Adwords(Privilege Escalation): Read-only user able to add YouTube channels via Linked accounts 

[ March 07, 2017  ](https://whitehatfamilyguy.blogspot.com/2019/06/google-adwordsprivilege-escalation-read.html "permanent link")

[![](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRB0TpCljgxGmAvCfXOo_aYkDphpbERInLdK6fw9pk5zYOOR3F_UQ)](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRB0TpCljgxGmAvCfXOo_aYkDphpbERInLdK6fw9pk5zYOOR3F_UQ)

**_STEWIE NOT DOG, HUNT SOME BUGS MY BOY!!!!_**

  

Google AdWords , is Google's advertising system in which advertisers bid on certain keywords in their searchable ads. Since advertisers have to pay for these clicks, Google makes money from search.

[![](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTgGvqFsIFSoGBwWC9azLnJSLhsxV0QHkYDszOn5o7mhMZMoAQh)](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTgGvqFsIFSoGBwWC9azLnJSLhsxV0QHkYDszOn5o7mhMZMoAQh)

  

_ISSUE_ : A user with read only access to the adwords account was able to link Youtube channels to the adwords account.

[![](https://media.giphy.com/media/anY8RifJ0lgdy/giphy.gif)](https://media.giphy.com/media/anY8RifJ0lgdy/giphy.gif)

[](https://media1.giphy.com/media/anY8RifJ0lgdy/giphy.gif)

**Reported: 5th April**

  

**Steps to reproduce:**

1\. Go to https://adwords.google.com create a test adwords account.

From settings, Account access add another userA with Read-only access

(Here's the access right is allocated as read only users)

Now

3\. Go to user A mail account and accept the invitation to join the adwords account.

4\. from user A adwords account go to settings then Linked accounts and then youtube, with below description:

YouTube channels

Link a YouTube channel to your AdWords account to gain greater insights about your customers.

  

5\. Add a youtube channel and accept the same via your youtube account.

the channel is added to the adwords account.

  
the check was missing while linking the youtube accounts,a request was send and post approval the accounts were linked. same worked for account unlinking, user with read only access can unlink admin's linked youtube account.

**  
**

**Bounty: 17th April**

Thanks Google VRP for the fix and reward.

  
[](https://media3.giphy.com/media/26gJzHT5BZZuQYbmw/source.gif)

[![](https://media3.giphy.com/media/26gJzHT5BZZuQYbmw/source.gif)](https://media3.giphy.com/media/26gJzHT5BZZuQYbmw/source.gif)

  

[](https://media3.giphy.com/media/26gJzHT5BZZuQYbmw/source.gif)

  

  

Share 

  * Get link
  * Facebook
  * X
  * Pinterest
  * Email
  * Other Apps

Share 

  * Get link
  * Facebook
  * X
  * Pinterest
  * Email
  * Other Apps

### Comments

#### Post a Comment

[](https://www.blogger.com/comment/frame/181979799605168940?po=6459649838084456112&hl=en&saa=85391&origin=https://whitehatfamilyguy.blogspot.com&skin=notable)
