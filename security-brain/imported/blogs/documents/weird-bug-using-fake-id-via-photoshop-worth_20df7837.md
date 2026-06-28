---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2024-02-17_weird-bug-using-fake-id-via-photoshop-worth-.md
original_filename: 2024-02-17_weird-bug-using-fake-id-via-photoshop-worth-.md
title: weird bug using fake id via photoshop worth $***
category: documents
detected_topics:
- xss
- command-injection
- otp
- automation-abuse
- business-logic
- cloud-security
tags:
- imported
- documents
- xss
- command-injection
- otp
- automation-abuse
- business-logic
- cloud-security
language: en
raw_sha256: 20df78372b7c385d81725a6173e36b80bcdc18e7b8c6e794ff7a96d0b6926278
text_sha256: eb7712d4acd4b587dd5a169ec339860ab1482b3f8a6ab1a3e7e012131c339717
ingested_at: '2026-06-28T07:32:31Z'
sensitivity: unknown
redactions_applied: false
---

# weird bug using fake id via photoshop worth $***

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2024-02-17_weird-bug-using-fake-id-via-photoshop-worth-.md
- Source Type: markdown
- Detected Topics: xss, command-injection, otp, automation-abuse, business-logic, cloud-security
- Ingested At: 2026-06-28T07:32:31Z
- Redactions Applied: False
- Raw SHA256: `20df78372b7c385d81725a6173e36b80bcdc18e7b8c6e794ff7a96d0b6926278`
- Text SHA256: `eb7712d4acd4b587dd5a169ec339860ab1482b3f8a6ab1a3e7e012131c339717`


## Content

---
title: "weird bug using fake id via photoshop worth $***"
url: "https://hamzadzworm.medium.com/weird-bug-using-fake-id-via-photoshop-worth-1fe5dbd04497"
authors: ["Abdelkader Mouaz (@hamzadzworm)"]
bugs: ["Logic flaw", "HTML injection"]
publication_date: "2024-02-17"
added_date: "2024-02-27"
source: "pentester.land/writeups.json"
original_index: 424
scraped_via: "browseros"
---

# weird bug using fake id via photoshop worth $***

weird bug using fake id via photoshop worth $***
Hamzadzworm
Follow
4 min read
·
Feb 17, 2024

522

8

Hi all i hope you are doing well, iam hamzadzworm(abdelkader mouaz) today i will share an issue that i found

I really love logic bugs its funny to find them more then getting rewards, i was invited to a private program at hackerone it was very secure and 0 reports resolved on it so it was like a challenge for me

i tried to inejct js codes on first name last name and all inputs.. to get a blind xss ….etc

but it didnt work because website dosent allow you to inject tags on inputs

Press enter or click to view image in full size

i keep digging untile i found there is support page that asks you to sent your id card it was a great place for me to find an issue

if you sent your real id card with your real name it will be accepted and nothing will happen

so i sent a fake id card from google images to see what will happen:

Press enter or click to view image in full size

i got an email from the support and i notices that both of names: account and name in id card was received in email so this mean that there is a function that take name from photo and send it to email

this is time to think out of the box : ), i editied the id card photo and put an html tag on the name in card so html was injected in photo name to see what will happen

and that was result:

Press enter or click to view image in full size

there is the name of account that i couldnt put htmli codes on it and there is the second name that as you see in email they automatically check it

so here i was able to inject html code in first name of photo

and its taken automatically to be reflected in email

untile now eveything is good but its still self htmli i changed my email to another email to check if htmli will be received on it but when i change it i got redirected to verification email step to be able to sent my id again

Get Hamzadzworm’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

i go back and confirmed my email then go to sent my id card and saved request in burpsuite repeater

after that i changed my email again to another email , it request verification to be able to do any action in account like send id card

i go back to the saved request of send id card that i saved and sent request again and approve document mail was sent to the new email without verification and htmli was on it so i changed this from self htmli to an htmli that can be exploited against other emails

i injected an <a href> in photo name to see if link will received in email and thats what happen:

Press enter or click to view image in full size

link was injected and it was like that:

website.com/token…… = {redirect to my website}

so this was stored open redirection via there main domain its great untile now

i keep thinking how to make impact higher and how i can be able to exploit it against an already existed users

i go back to change email and intercepted request of change email, when i try an already existed user email i got an error so i tried it with alias:

victim@email.com = victim+1@email.com

but they blocked me so i encoded {+1} to make it: {%2B1}

victim+1@email.com = victim%2B1@email.com

and document approve email was sent to an already existing user

result:

Press enter or click to view image in full size
Press enter or click to view image in full size

i will share in my next write up another weird issue where i found an admin panel with default creds i got duplicated for report but i keep testing inside the panel and i found a critical issue inside it which was accepted even when admin with default creds was duplicated

i hope you enjoyed it waiting to see your comments about it and have a great day all -.-
