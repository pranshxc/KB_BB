---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-03-04_30-minute-heist-how-i-bagged-a-1500-bounty-in-just-few-minutes_2.md
original_filename: 2023-03-04_30-minute-heist-how-i-bagged-a-1500-bounty-in-just-few-minutes_2.md
title: '30-Minute Heist: How I Bagged a $1500 Bounty in Just few Minutes!'
category: documents
detected_topics:
- access-control
- command-injection
- automation-abuse
- business-logic
tags:
- imported
- documents
- access-control
- command-injection
- automation-abuse
- business-logic
language: en
raw_sha256: 8d0d38b62a3f80d903dea72511d58f31f0e83ce8899a6d85d9633c0eac1321f5
text_sha256: e861bf4d56ccf0104f7a9919915d956cc8d38a2b7d40ca0afb038f0cd75ae708
ingested_at: '2026-06-28T07:32:19Z'
sensitivity: unknown
redactions_applied: false
---

# 30-Minute Heist: How I Bagged a $1500 Bounty in Just few Minutes!

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-03-04_30-minute-heist-how-i-bagged-a-1500-bounty-in-just-few-minutes_2.md
- Source Type: markdown
- Detected Topics: access-control, command-injection, automation-abuse, business-logic
- Ingested At: 2026-06-28T07:32:19Z
- Redactions Applied: False
- Raw SHA256: `8d0d38b62a3f80d903dea72511d58f31f0e83ce8899a6d85d9633c0eac1321f5`
- Text SHA256: `e861bf4d56ccf0104f7a9919915d956cc8d38a2b7d40ca0afb038f0cd75ae708`


## Content

---
title: "30-Minute Heist: How I Bagged a $1500 Bounty in Just few Minutes!"
url: "https://medium.com/@thelinuxboy/30-minute-heist-how-i-bagged-a-1500-bounty-in-just-few-minutes-48753eb2028e"
authors: ["Charlie : The Hacker"]
bugs: ["Broken Access Control", "Logic flaw"]
bounty: "1,500"
publication_date: "2023-03-04"
added_date: "2023-03-06"
source: "pentester.land/writeups.json"
original_index: 1429
scraped_via: "browseros"
---

# 30-Minute Heist: How I Bagged a $1500 Bounty in Just few Minutes!

30-Minute Heist: How I Bagged a $1500 Bounty in Just few Minutes!
Charlie : The Hacker
Follow
4 min read
·
Mar 4, 2023

244

1

Press enter or click to view image in full size

Hey fam,

It’s me, Charlie, the hacker, but my real name is Rajiv. After taking a break from my stock trading career, I decided to resume hunting for vulnerabilities in a few programs. So, I started exploring HackerOne and Bugcrowd to find targets.

After reporting a few bugs, I received an invitation to participate in a private program on Bugcrowd. Only 18–20 people were invited to hunt on this 100% new program.

I love hunting for logical bugs the most because they are unique and there’s less chance of duplicates. Although they may be rewarded or marked as N/A, there’s still less chance of duplicates. In just 30 minutes on that private program, I found a bug that earned me around $1500.

Here’s a brief of what I did, and I’m still hunting for more.

As I mentioned earlier, I like hunting for logical bugs. When searching for these types of bugs, I start by creating two accounts with different email addresses. Additionally, I use multiple tabs and browsers to aid in my search for logical bugs.

So I did the same thing in my private program I created two different accounts with email address and opened both the accounts in two different browsers, now the private program on which I’m hunting for is something like the company provide a platform to host meetings and to manage all the employees by giving them different kind of permission and benefits directly from the owner/admin account.

Get Charlie : The Hacker’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

So there is a option of creating or you can say host a business and manage all the employee at the same place like who want to start his shift or any meeting of employee, owner can also decide break of any employee directly from owner account.

Press enter or click to view image in full size

So here is what I did for my bug and I can’t reveal program name so I’m using REDACTED

TITLE : Unauthorized person can edit details of business after employment access level change.
Summary of my bug :

While hunting on the platform, I found that if admin give permission of admin to someone and admin changed back his employment access level to his original access level then that employee can do any change to the organization even if he’s not authorized. This is kind of Broken Access Control on the application

Steps To Reproduce :
Signup and create a business profile in redacted.com
Invite any second user in the business as a normal employee access level
Now accept invitation of second user in second browser and now as a employee you can’t change anything in the business like business name and settings (its a feature).
You can only see some limited access
Now go to admin account in browser 1 and change the employment level access of second user to System administrator.
Now refresh the page of user-2, you can now see some extra admin features in this access level, you can also change all the details in the business but you can’t invite anyone.
So now go to main admin account again and change the access level to the old employee access level.
Now the user is set back to his original access level.
Don’t refresh the page of user-2 browser and try to change the business name and save.
You can see in the admin account, name is changed and you can see unauthorized person from the business employee changed the business name

> Here access level means, we can change role as admin of any other user in few given roles with some extra allowance features.

Impact :

This will leads to business admin in major risk like changing in all other things in the business, which will create various impact in the organization and in the business.

In this bug there is no time out session stuff in the second user account page and there is a broken access control and user can do any changes in the business without any such authorisation.

Thanks for reading my write-up ! If you like then keep it in your story and tag us on instagram (
Charlie : The Hacker
 *@thelinuxboy*)
