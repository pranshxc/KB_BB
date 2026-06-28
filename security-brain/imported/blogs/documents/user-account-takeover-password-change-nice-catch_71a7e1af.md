---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2019-03-14_user-account-takeover-password-change-nice-catch.md
original_filename: 2019-03-14_user-account-takeover-password-change-nice-catch.md
title: User Account Takeover [Password Change]— Nice Catch!
category: documents
detected_topics:
- command-injection
- password-reset
tags:
- imported
- documents
- command-injection
- password-reset
language: en
raw_sha256: 71a7e1af6c70e0c81c9f61b14521d6b497a725d905d5927579dbd95608626f56
text_sha256: 5df2a042587c86438ce196096b53d1441c7dad93378c6aff09847ac3332cf9e8
ingested_at: '2026-06-28T07:31:59Z'
sensitivity: unknown
redactions_applied: false
---

# User Account Takeover [Password Change]— Nice Catch!

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2019-03-14_user-account-takeover-password-change-nice-catch.md
- Source Type: markdown
- Detected Topics: command-injection, password-reset
- Ingested At: 2026-06-28T07:31:59Z
- Redactions Applied: False
- Raw SHA256: `71a7e1af6c70e0c81c9f61b14521d6b497a725d905d5927579dbd95608626f56`
- Text SHA256: `5df2a042587c86438ce196096b53d1441c7dad93378c6aff09847ac3332cf9e8`


## Content

---
title: "User Account Takeover [Password Change]— Nice Catch!"
url: "https://medium.com/@rohitcoder/user-account-takeover-password-change-nice-catch-2293f4d272b2"
authors: ["Rohit kumar (@rohitcoder)"]
bugs: ["Account takeover", "Password reset"]
publication_date: "2019-03-14"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5359
scraped_via: "browseros"
---

# User Account Takeover [Password Change]— Nice Catch!

User Account Takeover [Password Change]— Nice Catch!
Rohit kumar
Follow
2 min read
·
Mar 14, 2019

245

2

Press enter or click to view image in full size
Image Credits: Record Future

Ever thought how you are implementing and passing data from the form to your queries? You are doing it dynamically?

Summary: In this writeup, I will explain how I was able to change the user account password without providing the old password. This writeup will be short. I will not take much time.

About Target: Target was From a private program. So, let’s assume the target is site.com

Reproduction steps:
Login into your site.com account.
Navigate to https://www.site.com/users/[user_id]/edit
Now, you will see a form which allows you to edit your account details and there is also another option to change your current password which requires your old password but this can be bypassed easily.
Now, for bypassing this change password feature. Just edit your account details and then submit this request and meanwhile intercept it.
Now you will notice some $_POST fields which will be like

user[first_name] // For changing first name
user[last_name] // For changing last name

Get Rohit kumar’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

This post request is making an array of the user which is having some key values (first_name,last_name). That means it is making a dynamic SQL query at the backend.

For changing the password just add a new key here user[password] and pass your value.

Check this Request

Notice I added user[password]
Bingo! password changed!

Having any question? Comment below or you can send message me on facebook.com/rohitcoder

Thanks,
@rohitcoder
