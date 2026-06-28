---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-02-25_my-p1-account-takeover.md
original_filename: 2023-02-25_my-p1-account-takeover.md
title: My P1 — Account Takeover
category: documents
detected_topics:
- idor
- command-injection
- password-reset
- api-security
tags:
- imported
- documents
- idor
- command-injection
- password-reset
- api-security
language: en
raw_sha256: c134152826d2d5661babca05e2b47750701b1be2013ca8c6c25ec10553870a6d
text_sha256: 9367336a6655c0b71f9bf07e20a01ceaff875958858cc91b61306430bef68474
ingested_at: '2026-06-28T07:32:18Z'
sensitivity: unknown
redactions_applied: false
---

# My P1 — Account Takeover

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-02-25_my-p1-account-takeover.md
- Source Type: markdown
- Detected Topics: idor, command-injection, password-reset, api-security
- Ingested At: 2026-06-28T07:32:18Z
- Redactions Applied: False
- Raw SHA256: `c134152826d2d5661babca05e2b47750701b1be2013ca8c6c25ec10553870a6d`
- Text SHA256: `9367336a6655c0b71f9bf07e20a01ceaff875958858cc91b61306430bef68474`


## Content

---
title: "My P1 — Account Takeover"
url: "https://medium.com/@metikalakullai.gtl/my-p1-account-takeover-3293fc59e10"
authors: ["Kullai (@Kullai12)"]
bugs: ["Account takeover", "IDOR", "Password reset"]
publication_date: "2023-02-25"
added_date: "2023-02-28"
source: "pentester.land/writeups.json"
original_index: 1473
scraped_via: "browseros"
---

# My P1 — Account Takeover

My P1 — Account Takeover
Kullai
Follow
3 min read
·
Feb 25, 2023

434

5

Hi, all This is Kullai (Security Researcher). Today I will share one of my interesting findings It’s My First P1 Let's start ….

While I am hunting on one target named example.com (all will name redacted.com). There is an invite Functionality on their website. By using that functionality, I can take over the victim's account. Interesting Right Let's dive….

“Any mistakes in my English ignore it.”

Press enter or click to view image in full size

How did I find this?

By using this Invite functionality, I am able to invite the users.

Suppose User-A is an attacker and User-B is an attacker friend.

User-A invited User-B and User-B accepted and Now User-A and User-B are in the same Group.

Press enter or click to view image in full size
hackerKullai(User-A)

Now User-A will tell User-B to reset the password. (User-A is admin, User-A has privileges to send the reset password mail to User-B).

Press enter or click to view image in full size

Now User-B will get the Reset password link in his mail.

He just opens the link and he will not change the password.

You can see I updated the email of user-B

Now the whole drama begins User-A will change the Email of User-B to the victim's email.

Press enter or click to view image in full size
user-B email changed to victim’s email.

After changing to the victim’s email, User-B will change the password.

Get Kullai’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Here The User-B password should be changed but in my case Victim password is updating.

I am like wtf is happening!!!! Without victims' interaction, I am able to change the password and able to login with new credentials which were changed by User-B.

I literally named this one Myself as Account Takeover via confusion (I have no idea another takes this name. But yes, I wanted to put this name to this one :))

Impact:

Without Interaction, I can takeover anyone's account Just by knowing their Email ID.

Time Line:

Reported through mail: 20 Feb 2023, 10:21 PM

Accepted Bug and Invited to their Private program: 21 Feb, 18:28

Press enter or click to view image in full size
Accepted & invited to Bugcrowd.
P1

Rewarded & resolved on 24 Feb 2023

They paid their highest pay and resolved.

Follow me for more content:

LinkedIn | Twitter | Instagram

Thanks for reading!!

Your Kullai :)
