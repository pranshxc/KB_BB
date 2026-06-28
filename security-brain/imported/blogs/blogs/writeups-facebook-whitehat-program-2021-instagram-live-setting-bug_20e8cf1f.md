---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-05-20_writeups-facebook-whitehat-program2021-instagram-live-setting-bug.md
original_filename: 2021-05-20_writeups-facebook-whitehat-program2021-instagram-live-setting-bug.md
title: 'Writeups: Facebook Whitehat program(2021): Instagram Live setting bug'
category: blogs
detected_topics:
- mobile-security
- command-injection
- business-logic
tags:
- imported
- blogs
- mobile-security
- command-injection
- business-logic
language: en
raw_sha256: 20e8cf1fc00084474fce57107ecaca447da8f05fe413af809fb19268baa433f1
text_sha256: df23490632d995b9c51476f5d2719d4ba65de5b3258fc32a19d70567806ca5d9
ingested_at: '2026-06-28T07:32:06Z'
sensitivity: unknown
redactions_applied: false
---

# Writeups: Facebook Whitehat program(2021): Instagram Live setting bug

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-05-20_writeups-facebook-whitehat-program2021-instagram-live-setting-bug.md
- Source Type: markdown
- Detected Topics: mobile-security, command-injection, business-logic
- Ingested At: 2026-06-28T07:32:06Z
- Redactions Applied: False
- Raw SHA256: `20e8cf1fc00084474fce57107ecaca447da8f05fe413af809fb19268baa433f1`
- Text SHA256: `df23490632d995b9c51476f5d2719d4ba65de5b3258fc32a19d70567806ca5d9`


## Content

---
title: "Writeups: Facebook Whitehat program(2021): Instagram Live setting bug"
url: "https://infosecwriteups.com/writeups-facebook-whitehat-program-2021-instagram-live-setting-bug-500-usd-d2d076b3f8bb"
authors: ["Takashi Suzuki"]
programs: ["Meta / Facebook"]
bugs: ["Logic flaw"]
bounty: "537"
publication_date: "2021-05-20"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3638
scraped_via: "browseros"
---

# Writeups: Facebook Whitehat program(2021): Instagram Live setting bug

Writeups: Facebook Whitehat program(2021): Instagram Live setting bug
Takashi Suzuki
Follow
3 min read
·
May 20, 2021

75

About me:
Takashi Suzuki - Security Researcher - LinkedIn
I started to learn information security 8 years ago. Since then, I have been addicted to hacking. My curiosity for…

www.linkedin.com

HackerOne profile - kamikaze
Hall of Fame on facebook, google, mozilla, dell, redhat, DJI.... …

hackerone.com

Title

Instagram live’s archived setting turns on automatically after IG user ends live video even if IG user turned off archive setting previously

Description:

Instagram app turns on Live archive setting when a user ends IG live & starts live again.

It is a problem because archived live can be seen in creator studio’s calendar by other FB page user.

In creator studio’s calendar, other users who can access to IG account(i.e. page advertiser) can see IG public content & archived content, but not deleted content.

If IG user goes IG live second time while IG user turned off IG live’s archive setting in first time’s IG live, IG user assume that second time’s live video will also be deleted from IG app & ended live video will not appear in creator studio’s calendar where other users (i.e. page advertiser) can see ended live video.

If this issue is intended, Question & Problem will arise:

Should IG user turns off live’s archive setting whenever IG user ends IG live? If IG user goes IG live a second time while IG user forgot to check archive setting, ended IG live video will automatically be saved in creator studio’s calendar.

Why IG app automatically turns on live’s archive setting without the user’s consent? IG user may assume second live’s archive setting will also be turned off.

Prepared set:

Tested device: iOS 14.4 & iPadOS 14.4

Tested app: Instagram iOS version 177.0

1 IG creator/business account(Victim User) which is connected to FB business page

Get Takashi Suzuki’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

1 FB account(Attacker user) who can access to IG account(i.e. page advertiser) in FB creator studio

Step to reproduce:
Victim IG user turns off live’s archive setting from IG mobile app(Settings -> Privacy -> Story -> Save Live to Archive)
Press enter or click to view image in full size

2. Victim IG user starts IG live

3. Victim IG user ends IG live and delete IG live

4. Repeat Step 2 & Step 3

5. Repeat Step 1, you will notice “Save Live to Archive” was turned on automatically.

Press enter or click to view image in full size

6. Attacker FB user goes to creator studio’s calendar page.

Press enter or click to view image in full size
Result:

IG live video is archived even if IG user turned off IG live’s archive in Step 1 because archive setting was turned on automatically.

Expected result:

When IG user ends IG live, IG mobile app should not turn on IG live archive setting without user’s consent because other FB user who can access IG account in creator studio can see ended Live video.

Timeline:

Reported: March 4, 2021

Triaged: March 6, 2021

Fixed: March 12, 2021

Bounty Awarded: March 31, 2021

Press enter or click to view image in full size
