---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-09-29_the-art-of-idor-7-idors-in-edm0d0.md
original_filename: 2020-09-29_the-art-of-idor-7-idors-in-edm0d0.md
title: 'The Art of IDOR: 7 IDORs in Edm0d0'
category: documents
detected_topics:
- idor
- command-injection
- automation-abuse
- supply-chain
tags:
- imported
- documents
- idor
- command-injection
- automation-abuse
- supply-chain
language: en
raw_sha256: ee764458a7c697732feb7bdffcf9346a6e4357c51f2fd3edd3f4693865328ad2
text_sha256: 08612e4f05a791965e0ecf1246c175b72e4c59af2be1acda6c96e335c8ad84e0
ingested_at: '2026-06-28T07:32:03Z'
sensitivity: unknown
redactions_applied: false
---

# The Art of IDOR: 7 IDORs in Edm0d0

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-09-29_the-art-of-idor-7-idors-in-edm0d0.md
- Source Type: markdown
- Detected Topics: idor, command-injection, automation-abuse, supply-chain
- Ingested At: 2026-06-28T07:32:03Z
- Redactions Applied: False
- Raw SHA256: `ee764458a7c697732feb7bdffcf9346a6e4357c51f2fd3edd3f4693865328ad2`
- Text SHA256: `08612e4f05a791965e0ecf1246c175b72e4c59af2be1acda6c96e335c8ad84e0`


## Content

---
title: "The Art of IDOR: 7 IDORs in Edm0d0"
url: "https://medium.com/@pratyush1337/the-art-of-idor-7-idors-in-edm0d0-b86d683c8de9"
authors: ["Pratyush Anjan Sarangi"]
programs: ["Edmodo"]
bugs: ["IDOR"]
publication_date: "2020-09-29"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4230
scraped_via: "browseros"
---

# The Art of IDOR: 7 IDORs in Edm0d0

Top highlight

The Art of IDOR: 7 IDORs in Edm0d0
Pratyush Anjan Sarangi
Follow
5 min read
·
Sep 29, 2020

280

1

Three duplicates and four rewards!

Press enter or click to view image in full size
IDOR — — — — >$$$

Hi! Guys Hope so everyone is doing well and are safe staying at home as the world is fighting against this COVID-19 pandemic. This time this will be a very long post as I will be describing all the seven bugs in detail and I will include Images and Videos as required for the bug description.

This time I started hunting bugs to get another shaker from Edmodo as there is nothing much to do and nowhere else to go. My primary focus was to find one IDOR to receive the goodies pack with the shaker this time, but it was not destined. Instead, I got a surprise. You will know it in the end ;)

So let’s begin with the IDORs Bug. Simple IDORs won’t need much explanation but if it’s a bit complicated than I will go for the proper explanation :)

1st IDOR Bug:

I have discovered an IDOR Vulnerability in which I can access any quiz files from anyone’s account. I was also able to save changes to their documents.

Video POC:

2nd IDOR Bug:

I have found another IDOR Vulnerability in which I can Assign Badges from Anyone’s Account to my group. I have created A Teacher Account, i.e., Sam Anjan. I have created a Group Hacker in that account and then created a new badge of my own. There is a Function in which I can add my badge that I created, but if I change the badge_id to random Numeric id, then it will reveal the Badge info and assign it, my group.

Burp-suite Interception:

Press enter or click to view image in full size

Image POC:

Press enter or click to view image in full size
Badge_details
Press enter or click to view image in full size
Badge_IDOR Exploitation

Video POC:

3rd IDOR Bug:

I have found another IDOR Vulnerability in which I can Add Schedule to anyone’s account. I have created two accounts, i.e., Sam Anjan and Sam Victim, both are teachers. I have added one schedule in my Sam anjan’s account, and I will edit it and change the user_id to sam victim’s. If I manipulate the user_id to any random number, then I can create new schedules wildly for anyone in Edmodo. Let’s Check out if you think where can I find user_id. Let’s follow Just Like That :)

Burp-suite Interception:

Press enter or click to view image in full size

Video POC:

4th IDOR Bug:

I have found an IDOR in which I can randomly add any student to my class, and I can reset their password and other details. The issue is with the invite by email functional module. This issue is limited to Student Access level, and it cannot exploit anyone having Teacher’s Access level.

Burp-suite Interception:

Press enter or click to view image in full size
student_Account_takeover

Image POC:

Press enter or click to view image in full size
Student Acc Takeover scenario

Video POC:

5th IDOR Bug:

Get Pratyush Anjan Sarangi’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

I have found a LOGICAL flaw in the library functional Module….and though it’s IDOR, but it’s due to a logical flaw. I have created two Teacher accounts, i.e., Sam Anjan and Sam victim. I have added a few files to both accounts library. But the issue is that if we put the file_id and library_id correctly, then we can exploit it cross Account. This is to confirm that I haven’t added the 2nd Teacher’s account as a co-account in my 1st account.

Burp-Suite Interception:

Press enter or click to view image in full size
Logical_IDOR to exploit files in other accounts

Image POC:

Press enter or click to view image in full size
Logical_IDOR Exploitation

Video POC:

6th IDOR Bug:

I have found another IDOR Vulnerability in which I can Assign grades to any random student. I have created two accounts, i.e., Sam anjan[Teacher] and Student_User[Student].Student_User is enrolled under a different class, i.e., the sam victim Teacher I created earlier. This student account is not under Sam Anjan Teacher. Now, as I have created an assignment for my own, and I can grade myself, but if I change the submitter_id than I assign Grade to any random student or Teacher. Let’s check out.

To VERIFY this, the student was getting a Notification…..so This is Verified :)

This is a good example of Abusing the functionality.

Burp-suite Interception:

Press enter or click to view image in full size
grade_idor to info disclosure
Press enter or click to view image in full size

Image POC:

Press enter or click to view image in full size
Grade_IDOR Exploitation

Video POC:

7th IDOR Bug:

I have found an IDOR in which I can enumerate and see all the names of classes and assign them. I have created a student account, and then via the Student planer, I can create New Task. While creating the Task, if I change the group_id, than it assigns and shows the name of other registered user’s classes.

Burp-Suite Interception:

Press enter or click to view image in full size
Student_planner IDOR

Image POC:

Press enter or click to view image in full size
Student_planner Exploitation

Video POC:

Yes, They have rewarded a few of my reports for the security issues and impact of the bugs. My primary focus was always to check the Response Tab of Burpsuite for any type of info disclosure. Many times I have observed that the API actually sents sensitive data in response but in client-side(Browser) it gets filtered. So, Always check the Raw response from the web-server.

Press enter or click to view image in full size
Rewards from Edmodo for IDORs

Timeline:

Feb. 20, 2020— Initial Report
Mar. 10, 2020 — Report Triaged
Mar. 10, 2020 — Bug Fixed and Rewarded
