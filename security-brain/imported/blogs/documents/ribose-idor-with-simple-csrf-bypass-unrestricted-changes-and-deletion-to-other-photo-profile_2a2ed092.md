---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2018-04-18_ribose-idor-with-simple-csrf-bypass-unrestricted-changes-and-deletion-to-other-p.md
original_filename: 2018-04-18_ribose-idor-with-simple-csrf-bypass-unrestricted-changes-and-deletion-to-other-p.md
title: Ribose — IDOR with Simple CSRF Bypass — Unrestricted Changes and Deletion to
  other Photo Profile
category: documents
detected_topics:
- sso
- idor
- command-injection
- path-traversal
- otp
- csrf
tags:
- imported
- documents
- sso
- idor
- command-injection
- path-traversal
- otp
- csrf
language: en
raw_sha256: 2a2ed09258d792878e3b8d486fb9f9dd06b65fbda3f1cedd117387c44f4d106b
text_sha256: 23cf39c469cd8c2f165fef58684f86c2d77176476110d66aec51f934ab950987
ingested_at: '2026-06-28T07:31:57Z'
sensitivity: unknown
redactions_applied: false
---

# Ribose — IDOR with Simple CSRF Bypass — Unrestricted Changes and Deletion to other Photo Profile

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2018-04-18_ribose-idor-with-simple-csrf-bypass-unrestricted-changes-and-deletion-to-other-p.md
- Source Type: markdown
- Detected Topics: sso, idor, command-injection, path-traversal, otp, csrf
- Ingested At: 2026-06-28T07:31:57Z
- Redactions Applied: False
- Raw SHA256: `2a2ed09258d792878e3b8d486fb9f9dd06b65fbda3f1cedd117387c44f4d106b`
- Text SHA256: `23cf39c469cd8c2f165fef58684f86c2d77176476110d66aec51f934ab950987`


## Content

---
title: "Ribose — IDOR with Simple CSRF Bypass — Unrestricted Changes and Deletion to other Photo Profile"
page_title: "Ribose - IDOR with Simple CSRF Bypass - Unrestricted Changes and Deletion to other Photo Profile | by YoKo Kho | Medium"
url: "https://medium.com/@YoKoKho/ribose-idor-with-simple-csrf-bypass-unrestricted-changes-and-deletion-to-other-photo-profile-e4393305274e"
authors: ["YoKo Kho (@YokoAcc)"]
programs: ["Ribose"]
bugs: ["IDOR"]
publication_date: "2018-04-18"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5910
scraped_via: "browseros"
---

# Ribose — IDOR with Simple CSRF Bypass — Unrestricted Changes and Deletion to other Photo Profile

Ribose - IDOR with Simple CSRF Bypass - Unrestricted Changes and Deletion to other Photo Profile
YoKo Kho
Follow
7 min read
·
Apr 18, 2018

134

3

بسم الله الرحمن الرحيم

Please kindly visit this simple paper directly to looking this release in simple:

[English Version] Ribose — IDOR with Simple CSRF Bypass — Unrestricted Deletion to other Photo Profile

I. ABSTRACT

Introducing ourselves in the use of social media platform is a thing that couldn’t be separate for every user. Realized if the needs of this can’t be separate from social media life (to fulfill the needs profile introduction), Ribose’s developer has provided so many feature that could be used such as uploading the profile photo, adding the first and last name, adding the contact information, and many more.

But the problem exists when one of that feature has a session problem that could allow the Attacker to illegally changes the information. In this case, Ribose doesn’t restrict yet the session to each authorized user to delete or upload the other photo profile. In other words, by using Attacker’s own session, they could delete or change all the profile photo that used by user at Ribose’s Platform.

Please kindly note that the issue has been fixed and the article has been released with the permission of Ribose.

II. INTRODUCTION

2.1. User ID at Ribose
Different with other common platform that using number or even username as a unique identity, Ribose giving (the very complex user ID to be guessed) the long user ID that generated automatically when someone signing up their ID into Ribose’s Platform. For example, when we create an account with me@firstsight.me as email, we got 0b03d802–3e29–4564-xxxx-x1x1x1x1x1x1 as user ID.

Generally, any user at this platform could see the other user ID since this parameter is not in the hidden situation. This conclusion could be seen in instant when we try to visit a user at Ribose.

Press enter or click to view image in full size
Figure 1: User ID of Team Ribose Account

From the picture above, we could see if Team Ribose’s User ID is eeeeeeee-ffff-gggg-zzzz-z1z1z1z1z1z1:

2.2. Deletion Action of Photo Profile
When a user would like to delete their own photo, automatically the system will send the “DELETE” HTTP Method to the server with the user ID and CSRF-Token that used by the system to identify if the process is executed by authorized user. Here are the sample of the “DELETE” request to deleting the photo profile.

DELETE /people/users/0b03d802-3e29-4564-xxxx-x1x1x1x1x1x1/avatar?_rr=indigolocal_3BFA8A3E8&_rv=52dde6a5 HTTP/1.1
Host: www.ribose.com
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.11; rv:56.0) Gecko/20100101 Firefox/56.0
Accept: application/json, text/javascript, */*; q=0.01
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Content-Type: application/x-www-form-urlencoded; charset=UTF-8
X-CSRF-Token: <very long CSRF Token overhere>
X-CSRF-Param: authenticity_token
X-Requested-With: XMLHttpRequest
Referer: https://www.ribose.com/
Content-Length: 1
Cookie: _r=<cookies_over_here>
DNT: 1
Connection: close

Table 1 Deletion Request of User’s Photo Profile

As we could see, in theory, it’s not possible for Attacker to delete other user’s photo profile without the knowledge of victim’s CSRF-Token that (should) restrict to each session. But in this situation, it’s possible. By (only) changing the sent user ID (highlighted in red) into the Victim’ user ID, then the deletion process still executed by the system.

2.3. Photo Upload Action at Photo Profile
By design at Ribose, this is not too different with the previous one. When a user would like to upload their own picture as their photo profile, automatically the system will send the “POST” HTTP Method to the server with the user ID, authenticity token, and CSRF-Token that used by the system to identify if the process is executed by authorized user. Here are the sample of the “POST” request to uploading the photo profile:

Press enter or click to view image in full size
Figure 2: Upload Request of User’s Photo Profile

Just like our previous statement, as could be seen, in theory, it’s not possible for Attacker to upload the picture into the other user’s photo profile without the knowledge of victim’s CSRF-Token and authenticity token that (should) restrict to each session. But in this situation, it’s possible. By (only) changing the sent user ID (highlighted in red) into the Victim’ user ID, then the upload process still executed by the system.

III. SUMMARY OF ISSUE

As it has been described before, the security problem in this report is the Attacker could use their own session to delete or change all of the user’s photo that exist at the system.

IV. PROOF OF CONCEPT

4.1. PoC of Unrestrited Deletion to Other Photo Profile
The proof of concept related this one is not too hard since most of the root cause and process has been explained earlier. But for completing the explanation, we still write the step by step to reproducing the issue.

4.1.1. Find out the user ID of the victim that would like to be set as a target. If we found any difficulties to find those one, then we just need to approve the automatic “Team Ribose” friend invitation and visit Team Ribose’s profile to see the other user’s profile.

Press enter or click to view image in full size
Figure 3: Automatic Connection Request by Team Ribose
Press enter or click to view image in full size
Figure 4: Team Ribose’s Connections (Friend List)

So basically, the Attacker just need to choose the list of the “victims” that could be seen at Team Ribose’s Profile. Of course, this method will reduce the Attacker’s time to guessing the very complex User ID that generated by Ribose.

Get YoKo Kho’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

4.1.2. The next step it, try to delete our own photo profile to get the “Deletion Request” that send by the application to server. In this case, we will get this as our deletion execution:

Press enter or click to view image in full size
Figure 5: Deletion Request of User’s Photo Profile

When the request has been send into the server, then the server will give a “success” response. Here are the sample of valid request from our own session to delete our own photo profile:

Press enter or click to view image in full size
Figure 6: Valid Session to Delete our own Photo Profile

4.1.3. After we get this valid request, then all we need to delete victim’s photo profile is just replacing our own user ID to victim’s user ID. Here is the photo deletion sample to victim with Attacker’s session:

Press enter or click to view image in full size
Figure 7: Deleting the Photo with Attacker’s User ID

As we could see from the picture above, the Attacker’s session has successfully to be used to delete the other photo profile.

4.2. PoC of Unrestrited Photo Changes to Other Photo Profile
As we could see from the previous explanation, the proof of concept related this issue is not too different with the previous one.

4.2.1. Since we know already about the Ribose’s User ID design, then we will move forward to the method that used by Ribose to change the photo profile.

4.2.2. Try to upload our own photo profile to get the “Upload Request” that send by the application to server. In this case, we will get this as our deletion execution:

Press enter or click to view image in full size
Figure 8: Upload Request of User’s Photo Profile

When the request has been send into the server, then the server will give a “success” response. Here are the sample of valid request from our own session to upload our own photo profile:

Press enter or click to view image in full size
Figure 9: Valid Session to Upload our own Photo Profile

4.2.3. After we get this valid request, then all we need to upload the picture into the victim’s photo profile is just replacing our own user ID to victim’s user ID. Here is the photo upload sample to victim with Attacker’s session.

Press enter or click to view image in full size
Figure 10: Uploading the Photo with Attacker’s User ID

As we could see from the picture above, the Attacker’s session has successfully to be used to upload the picture into the other photo profile.

V. RECOMMENDATION

Ensuring that every session is only functioning for its own account (couldn’t be used by other users) would surely be a recommendation that can be implemented to cover the existed vulnerability.

VI. RESPONSE

Ribose has responded the issue very fast and also offer the compensation of reward into another (cool) one (since at that time, there is a little issue about the swag).

They also fix the issue very fast (around one month) even the deploy need more time.

VII. ADDITIONAL INFORMATION

For completing the explanation, we upload the PoC Video that could be seen at Youtube:

Unrestricted Deletion to other Photo Profile: https://youtu.be/dxv6Uj9_xsw
Unrestricted Changes to other Photo Profile: https://youtu.be/ItlQg4lulnw
VIII. LESSON LEARNED

8.1. Always try to changing our User ID into another User ID (as long the victim’s ID are easily predicted or could be found) even the targeted application has implement the CSRF Token that commonly used for restrict the session.

In this case, Ribose has implement the unique User ID, CSRF Token (at header), and another custom header (CSRF Param) as a protection that looks hardcore to be bypassed. But, surprisingly, the design could be bypass by changing the User ID.

8.2. Generally, the things that we will do related the IDOR / CSRF bypass are:

Just changing the parameter without thinking about the CSRF Token even the CSRF Token itself is exist at the application;
Delete the CSRF Token (there is a possibility if the design could work without any CSRF Token even the application has implement it);
Change the Victim’s CSRF Token to the Attacker’s CSRF Token (there is also a possibility if the action that conducted by victim could be processed by Attacker’s CSRF Token);
And so many cool method that could be seen at: https://haiderm.com/10-methods-to-bypass-cross-site-request-forgery-csrf/
