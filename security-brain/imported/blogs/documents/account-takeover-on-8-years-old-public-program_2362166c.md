---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2024-08-14_account-takeover-on-8-years-old-public-program.md
original_filename: 2024-08-14_account-takeover-on-8-years-old-public-program.md
title: Account takeover on 8 years old public program
category: documents
detected_topics:
- command-injection
- password-reset
- automation-abuse
- race-condition
tags:
- imported
- documents
- command-injection
- password-reset
- automation-abuse
- race-condition
language: en
raw_sha256: 2362166c70ecea9bcf73f037c73d509bbfee8bc3c081de9cc02287278127753b
text_sha256: 335e0974b6681fa572a254f98f8fbeedab76cb7fd7ccb18f1ce7df8028ac47d4
ingested_at: '2026-06-28T07:32:37Z'
sensitivity: unknown
redactions_applied: false
---

# Account takeover on 8 years old public program

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2024-08-14_account-takeover-on-8-years-old-public-program.md
- Source Type: markdown
- Detected Topics: command-injection, password-reset, automation-abuse, race-condition
- Ingested At: 2026-06-28T07:32:37Z
- Redactions Applied: False
- Raw SHA256: `2362166c70ecea9bcf73f037c73d509bbfee8bc3c081de9cc02287278127753b`
- Text SHA256: `335e0974b6681fa572a254f98f8fbeedab76cb7fd7ccb18f1ce7df8028ac47d4`


## Content

---
title: "Account takeover on 8 years old public program"
url: "https://medium.com/@pranshux0x/account-takeover-on-8-years-old-public-program-c0c0a30cfdd2"
authors: ["Priyanshu Shakya (@pranshux0x)"]
bugs: ["Account takeover", "Email verification bypass"]
publication_date: "2024-08-14"
added_date: "2024-08-26"
source: "pentester.land/writeups.json"
original_index: 72
scraped_via: "browseros"
---

# Account takeover on 8 years old public program

Account takeover on 8 years old public program
priyanshu shakya
Follow
2 min read
·
Aug 14, 2024

326

5

Press enter or click to view image in full size

Thanks to

0xacb ( https://x.com/0xacb) for his tool recollapse
Portswigger (https://x.com/PortSwigger) for their wonderful race condition tooling in burp and research .

This is the story of the account takeover that I found on 8 years old public program.

There is a main website www.example.com , you can create your account here and login into your account.

There is another website for developers developer.example.com, you can login into your developer account using your main account.

Understand the flow of login into developer.example.com

Go to developer.example.com
Click on sign in button
Select your account of main website (www.example.com).
Verify your email address popup will come if you don’t verify email of your main account. ( A link will be send to email address, you have to click on that link, to verify email address)
You will be logged in developer.example.com

I try to bypass this email verification process. This is how I bypass

Go to www.exampe.com create a account a with email just@gmail.com
Go to developer.exampe.com click on sign in button, select my account, email verification popup appears, click on send verification email.
A email verification email come into my inbox, open the verification link while proxying the traffic through burp and send the email verification request to repeater and drop the request
While proxying the traffic through burp go to www.example.com change my email to just1@gmail.com and send the email verification request also to repeater and drop the request.
Now I create a group in repeater and move both request to that group and send them in parallel.
Account created with verified email just1@gmail.com.
Now I have a account on developer.example.com with verified email just1@gmail.com

I report this bug that I am able to bypass email verification with these steps, they accept the bug as p4, reward $200.

Get priyanshu shakya’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Now I want account takeover somehow, so my thought process is that if we somehow create a developer account with victim email , then we can verify email with previous exploit and ATO will be done.

Now on www.example.com , I try to change my email to victim email victim@gmail.com, I got error something went wrong.

So I try to fuzz to the victim email with unicode characters. ( use recollapse tool if you want).

This email address got accepted victim@gmail.com%0f

Now on www.exampe.com , my email is victim@gmail.com%0f and victim email is victim@gmail.com, and we cannot access each other account, both accounts are different.

Now when I try to sign in on developer.example.com , with my email victim@gmail.com%0f, I go email verification prompt, I verified my email with previous exploit .

Boom! I sign into victim developer account.

Account takeover complete.

If you have any question reach out to https://x.com/pranshux0x
