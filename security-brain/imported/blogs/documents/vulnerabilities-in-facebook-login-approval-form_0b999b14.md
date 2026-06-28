---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2017-02-14_vulnerabilities-in-facebook-login-approval-form.md
original_filename: 2017-02-14_vulnerabilities-in-facebook-login-approval-form.md
title: Vulnerabilities in Facebook Login Approval Form
category: documents
detected_topics:
- access-control
- command-injection
- password-reset
- business-logic
tags:
- imported
- documents
- access-control
- command-injection
- password-reset
- business-logic
language: en
raw_sha256: 0b999b14c8437553b13d9f15d6a434c937eeb151a86e53d9e24017b4dcb7d365
text_sha256: 83232f245cf89d2becd633c2dc07644bb1f3ccf84fc537e8fd2ece4ff4efc56a
ingested_at: '2026-06-28T07:31:55Z'
sensitivity: unknown
redactions_applied: false
---

# Vulnerabilities in Facebook Login Approval Form

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2017-02-14_vulnerabilities-in-facebook-login-approval-form.md
- Source Type: markdown
- Detected Topics: access-control, command-injection, password-reset, business-logic
- Ingested At: 2026-06-28T07:31:55Z
- Redactions Applied: False
- Raw SHA256: `0b999b14c8437553b13d9f15d6a434c937eeb151a86e53d9e24017b4dcb7d365`
- Text SHA256: `83232f245cf89d2becd633c2dc07644bb1f3ccf84fc537e8fd2ece4ff4efc56a`


## Content

---
title: "Vulnerabilities in Facebook Login Approval Form"
url: "https://medium.com/@zahidali_93675/vulnerabilities-in-facebook-login-approval-form-dfa5fce92023"
authors: ["Zahid Ali"]
programs: ["Meta / Facebook"]
bugs: ["Broken authorization", "Logic flaw"]
bounty: "2,250"
publication_date: "2017-02-14"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 6225
scraped_via: "browseros"
---

# Vulnerabilities in Facebook Login Approval Form

V
ulnerabilities in Facebook Login Approval Form
Zahid Ali
Follow
4 min read
·
Feb 14, 2017

64

1

After multiple bugs found in facebook “Account Recovery Form” i found one another bug.

Description and Impact:

If victim fill up account recovery form with email (zapp@gmail.com) and if attacker do the same with same email (zapp@gmail.com) then he will redirect to the victim form and see the conversation between admin and victim on that form.

I reported this vulnerability to Facebook and got a reply from admin Aaron

=======================================

Hi Zahid,

The issue was previously reported by another Whitehat researcher back in February, so we are still tracking this issue over there.

Thanks,

Aaron
Security
Facebook

=======================================

After got this reply from facebook i tried to find another forms and i saw “Facebook Login Approval Form”

https://www.facebook.com/help/contact/259497704121855

Description and Impact:

If victim fill up account recovery form with email (zapp@gmail.com) and if attacker do the same with same email (zapp@gmail.com) then he will redirect to the victim form and see the conversation between admin and victim on that form.

Reproduction Steps:

Open the form → https://www.facebook.com/help/contact/259497704121855
Fill up form with victim’s email
After successfuly submit a form you will see the conversation between victim’s and facebook admin on support dashboard.

Here is the POC video

I got a reply from admin Brandon

=======================================

Hi Zahid,

Thank you for reporting this information to us. We are sending it to the appropriate product team for further investigation. We will keep you updated on our progress.

Brandon
Security
Facebook

=======================================

This bug was a long-term fix so i decided to test that form in another way and i found that this form is also vulnerable and i am able to violate privacy settings “who can look-up the user via the e-mail” which is turns on for (Friend’s Only).

They completely patched these bugs in main faceboo.com domain because of multiple bugs i found inside main domain. So i found these bugs in sub-domains https://m.facebook.com and https://touch.facebook.com.

Description and impact:

If a user sets privacy to “Who can look you up using the email you provided?” (Friends Only). Attacker was able to see which specific user ID that an email is linked with the help of that login approval form.

Reproduction steps:

1) Go to — →>> https://touch.facebook.com/help/contact/259497704121855

2) fill up form make sure that email id is linked to facebook and privacy of email is sets “Who can look you up using the email you provided?” (Friends Only).

3) fill up form with wrong info with victim’s email id

Now click on “Send additional Information”

Get Zahid Ali’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

and then type any message and send. After that you will see profile photo in the small box of support dashboard.

Copy image location and paste it on your browser or notepad inside that url you will see fb photo id. :)

https://scontent-sit4-1.xx.fbcdn.net/v/t1.0-9/13325647_10153735080289001_8921059986763774376_n.jpg?oh=3626368549c381fceace50fc76a31dbb&oe=5931F96C

copy fb photo id -> 10153735080289001

https://www.facebook.com/photo.php?fbid=(type that fb id here )

You will see the victim’s facebook profile. :)

Screen shots :

Press enter or click to view image in full size
Press enter or click to view image in full size
Press enter or click to view image in full size
Press enter or click to view image in full size
Press enter or click to view image in full size
Press enter or click to view image in full size
Press enter or click to view image in full size
Press enter or click to view image in full size
Press enter or click to view image in full size

I reported this bug to Facebook and got a reply from admin Ali

=======================================

Hi Zahid,

Thank you for reporting this information to us. We are sending it to the appropriate product team for further investigation. We will keep you updated on our progress.

Thanks,

Ali
Security
Facebook

=======================================

I got awarded 1500USD for that bug :)

And then after a couple of months in august 2016 i got a reply from admin Reginaldo about that long-term fix bug

=======================================

Hi Zahid,

W’re sill working on a fix and, as such, we would ask that you continue to withhold the details on this issue until we can finish fixing it.

However, given the long time frame already, we want to go ahead and send you a bounty of $750 in appreciation of your report. Details on getting the bounty will be sent shortly. Thanks again for sending this and we will let you know once we have an update on the fix!

Thanks,

Reginaldo
Security
Facebook

=======================================

Got awarded 750USD for that bug :)

Now they remove that login approval form and you cannot see support dashboard in account recovery forms. But still you can submit login approval form after login to your account. :)
