---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2019-01-02_how-i-was-able-to-harvest-other-vine-users-ip-address.md
original_filename: 2019-01-02_how-i-was-able-to-harvest-other-vine-users-ip-address.md
title: How I was able to Harvest other Vine users IP address
category: documents
detected_topics:
- idor
- command-injection
- information-disclosure
- api-security
tags:
- imported
- documents
- idor
- command-injection
- information-disclosure
- api-security
language: en
raw_sha256: 3f4c4d1b844bec81cf78e34cfdcebed8b47c7965b986e9fb0af40887b7a0b930
text_sha256: 05952477408d9c34330e2a581f2bfe41ef9518e47c1eb6982516a9ed7412fcfb
ingested_at: '2026-06-28T07:31:58Z'
sensitivity: unknown
redactions_applied: false
---

# How I was able to Harvest other Vine users IP address

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2019-01-02_how-i-was-able-to-harvest-other-vine-users-ip-address.md
- Source Type: markdown
- Detected Topics: idor, command-injection, information-disclosure, api-security
- Ingested At: 2026-06-28T07:31:58Z
- Redactions Applied: False
- Raw SHA256: `3f4c4d1b844bec81cf78e34cfdcebed8b47c7965b986e9fb0af40887b7a0b930`
- Text SHA256: `05952477408d9c34330e2a581f2bfe41ef9518e47c1eb6982516a9ed7412fcfb`


## Content

---
title: "How I was able to Harvest other Vine users IP address"
page_title: "How I was able to Harvest other Vine users IP address - Bug Bounty POC"
url: "https://bugbountypoc.com/how-i-was-able-to-harvest-other-vine-users-ip-address"
final_url: "https://bugbountypoc.com/how-i-was-able-to-harvest-other-vine-users-ip-address/"
authors: ["Prial Islam Khan (@prial261)"]
programs: ["Vine"]
bugs: ["IDOR"]
bounty: "5,040"
publication_date: "2019-01-02"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5493
---

# How I was able to Harvest other Vine users IP address

by  [Prial Islam](https://bugbountypoc.com/author/prial261/ "Posts by Prial Islam") · January 2, 2019

**Hello** [BugBountyPoc](https://bugbountypoc.com) viewers,This is [**Prial**](https://www.facebook.com/prial261) again . Today I will share about another Information disclosure Vulnerability which was leaking users IP address . Last time I disclosed a POC on How I was able to get all vine users sensitive Information including **Phone no** / **IP Address** / **Emails** and Many more what was reported to twitter and they patched it and rewarded me 7560$ . Those who missed it you can get the [POC Here](https://bugbountypoc.com/vine-user-private-information-disclosure/) and Orginal [Report Here](https://hackerone.com/reports/202823) .

When I testing vine API Endpoints I noticed a Endpoint what uses in Vine Repost mechanism which have a Parameter Named **“ipAddress”** with some plain Number value Like :- **2130706433**. We all know Ip Addresses look like :- [127.0.0.1](http://127.0.0.1/) . But the value of the **“ipAddress”** looks invalid . Then when I tried to search about it on google I came to know that the value is valid . Actually it was Converted to **IP Address to Long/Decimal** format . So I used a Online Converter tools and was able to get the real Ip . ( [Online Converter I used](http://www.smartconversion.com/unit_conversion/IP_Address_Converter.aspx) )

##

**Vulnerable Endpoint :** https://vine.co/api/timelines/users/<POST ID>

##

**Reproduce :**

  * TO reproduce this issue victim User have to repost any vine in his timeline and a lot of vine users reposted many Vine post in their timeline .
  * So Copy a Reposted Vine POST ID and place it in the Endpoint and visit it . Example : <https://vine.co/api/timelines/users/1293308695089926144>
  * Now when I visited the link I got a response like below (The contents was removed by twitter security team ) :-

“repost”: { “username”: “██████”, “verified”: 0, “vanityUrls”: [], “created”: “█████”, “repostId”: ████████, “avatarUrl”: “██████”, “userId”: ████, “user”: { “username”: “█████████”, “verified”: 0, “vanityUrls”: [], “avatarUrl”: “█████████”, “userId”: ████, “private”: 0, “location”: █████████ }, “flags|platform_lo”: 1, “postId”: ███, “ipAddress”: 2130706433 , “flags|platform_hi”: 1 }

  * As you can see the IP address value is converted now Just Use my give online tool to again convert it to valid ip address value .

I reported this issue in **Jan 26th** and they paid me**5040$** for reporting this on **Feb 25th** . Main Report :- <https://hackerone.com/reports/201300>

![](https://scontent-sit4-1.xx.fbcdn.net/v/t1.0-9/19875190_1622467124431510_6099535669972850510_n.png?oh=40183365d8075a93e9faf20302849dfa&oe=5A4C22A9)

This is for today . Hope you guys will like it .

Thanks for Reading .
