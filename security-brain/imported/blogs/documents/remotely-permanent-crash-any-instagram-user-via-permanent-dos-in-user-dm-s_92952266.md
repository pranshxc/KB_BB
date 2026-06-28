---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-05-04_remotely-permanent-crash-any-instagram-user-via-permanent-dos-in-user-dms.md
original_filename: 2022-05-04_remotely-permanent-crash-any-instagram-user-via-permanent-dos-in-user-dms.md
title: Remotely permanent crash any Instagram user via permanent DoS in user DM's.
category: documents
detected_topics:
- command-injection
tags:
- imported
- documents
- command-injection
language: en
raw_sha256: 929522661995686a2be7b3df1527e098d5c356482b72073e9a9766ee5d3c7a90
text_sha256: df9c7fa38414770a8e6cdd2f8aa8fcc1ab3dcef3454551b621803bcb79783050
ingested_at: '2026-06-28T07:32:11Z'
sensitivity: unknown
redactions_applied: false
---

# Remotely permanent crash any Instagram user via permanent DoS in user DM's.

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-05-04_remotely-permanent-crash-any-instagram-user-via-permanent-dos-in-user-dms.md
- Source Type: markdown
- Detected Topics: command-injection
- Ingested At: 2026-06-28T07:32:11Z
- Redactions Applied: False
- Raw SHA256: `929522661995686a2be7b3df1527e098d5c356482b72073e9a9766ee5d3c7a90`
- Text SHA256: `df9c7fa38414770a8e6cdd2f8aa8fcc1ab3dcef3454551b621803bcb79783050`


## Content

---
title: "Remotely permanent crash any Instagram user via permanent DoS in user DM's."
page_title: "Remotely permanent crash any Instagram user via permanent DoS in user DM's"
url: "https://www.yesnaveen.com/remotely-permanent-crash-any-instagram"
final_url: "https://www.naveen.sh/2022/05/remotely-permanent-crash-any-instagram.html?m=1"
authors: ["Naveen (@NaveenHax)"]
programs: ["Meta / Facebook"]
bugs: ["DoS"]
bounty: "1,575"
publication_date: "2022-05-04"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 2665
---

###  Remotely permanent crash any Instagram user via permanent DoS in user DM's 

### 

### Description

Instagram has some unique accounts which don't have any strings in their usernames that are created by developers for testing purposes they are normally invisible to platform users hence no one can interact with those accounts visiting these profiles will result in an application crash which means the user will be kicked out of Instagram App so keeping this in mind I thought of escalating this issue to increase the impact which resulted in permanent DoS in user DM's.

###  
Impact

This attack requires zero user interaction and has the potential to literally permanent crash any Instagram user making it zero-click DoS.

This could have let a malicious user Remotely crash any Instagram platform user just by adding them to a malicious group which doesn't need to be accepted and once added the victim can no longer use the Instagram app.

  

### Proof of Concept

  * Capture group member adding request and change the targeted userID with a NULL username Instagram account userID.
  * Add a victim account to the group that has a NULL username account as a member.
  * The victim can no longer use Instagram App.

### Timeline

14 December 2021 - Report sent  
17 December 2021 - Triaged  
20 January 2022 - $1500 Bounty Rewarded By Meta

[ May 06, 2022  ](https://www.naveen.sh/2022/05/remotely-permanent-crash-any-instagram.html "permanent link")
