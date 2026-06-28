---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-07-28_pre-access-to-victims-account-via-facebook-signup.md
original_filename: 2020-07-28_pre-access-to-victims-account-via-facebook-signup.md
title: Pre-Access to Victim’s Account via Facebook Signup
category: documents
detected_topics:
- password-reset
- oauth
- command-injection
- otp
- automation-abuse
- mobile-security
tags:
- imported
- documents
- password-reset
- oauth
- command-injection
- otp
- automation-abuse
- mobile-security
language: en
raw_sha256: c7cac81999e343949e2f821a0b264dca70f7f93c17891096ece71d282d4b7da2
text_sha256: 564b4e47df2a7d360cc3da200ead6467c743ffe826787023e722f8e9154efefc
ingested_at: '2026-06-28T07:32:02Z'
sensitivity: unknown
redactions_applied: false
---

# Pre-Access to Victim’s Account via Facebook Signup

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-07-28_pre-access-to-victims-account-via-facebook-signup.md
- Source Type: markdown
- Detected Topics: password-reset, oauth, command-injection, otp, automation-abuse, mobile-security
- Ingested At: 2026-06-28T07:32:02Z
- Redactions Applied: False
- Raw SHA256: `c7cac81999e343949e2f821a0b264dca70f7f93c17891096ece71d282d4b7da2`
- Text SHA256: `564b4e47df2a7d360cc3da200ead6467c743ffe826787023e722f8e9154efefc`


## Content

---
title: "Pre-Access to Victim’s Account via Facebook Signup"
url: "https://medium.com/@akshanshjaiswal/pre-access-to-victims-account-via-facebook-signup-60219e9e381d"
authors: ["Akshansh Jaiswal (@Akshanshjaiswl)"]
bugs: ["OAuth", "Account takeover"]
bounty: "500"
publication_date: "2020-07-28"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4378
scraped_via: "browseros"
---

# Pre-Access to Victim’s Account via Facebook Signup

Pre-Access to Victim’s Account via Facebook Signup
Akshansh JaisWal
Follow
4 min read
·
Jul 28, 2020

563

Hey, everyone, I hope you are doing fine. Around a few months back I have found this issue.

This is a case of pre account takeover in case a user has no account on the website and the attacker creates an account before the victim so in my case when attacker signup via Facebook on the main application and on Facebook attacker was registered using phone number so they got the option to add victim email-id in signup flow and later if victim sign-in and access via password reset the attacker will have access to the same account.

So as you might have noticed that Facebook allows you to add an email address to your account and without verifying it you can still use it into sign-in to Facebook

Press enter or click to view image in full size
Email not verified

and use it in third-party apps integrations. This thing in itself is not an issue but can be used as a chaining action.

So suppose any third party app where you see an account creation via

Press enter or click to view image in full size

Now when you click on Sign-up/login with Facebook opens in a pop-up and asks whether you want to allow and when you click to allow an access token is generated as

https://example.com/auth2/access_token=Eposkdskdpo.........
Request Method: POST

which application responds to reads info as

{"email":"example@example.com","name":"hey","id":"fb-id"}

Now based upon the token sent server will now generate user cookies and the user will now be able to use the application but here comes a small flaw that can be caused during development is email verification, by default if the application is requesting user’s email as input it will verify that user email is verified or not

Press enter or click to view image in full size
the email is returned only if verified

So in a case where the user has used the mobile number to sign-up , when they tries to signup the application response will be

{"id":"facebookidnumber","name":"Myname"}

So ideally at this situation, the application should not proceed with user registration and redirect to home page or say email not present but in some cases like below

As the above application directs the user to signup flow where it basically allows users to create an account by email where you can add any email input. Also, there’s a small trick you can apply to bypass if application checks for email is to manually tamper response to

{"id":"facebookidnumber","name":"Myname","email":"victimemail@victim.com"}

Now if the application allows it you can proceed with the sign-up flow and create an account using victim email-id so now when a victim will go for account creation they will get a message

Account already exists

And if the victim realizes even if someone has logged in and victim changes password nothing will change as Sign-in is via Facebook is available where now the attacker has access to the victim’s account because the application has used Facebook id as variable to match the user account.

Get Akshansh JaisWal’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

I also want to add a step to reproduce as I found that it might be a little confusing :

As attacker go on Facebook register an account using the phone number
Now on an application where you see “Sign-In with Facebook” try to create an account
After account creation verify by changing the name or profile picture then login with email by password reset and see same settings
Now again login via Facebook to see that you still have access to that account

But here are some catch/scenarios required which surely prevents it or make it complex:

1. Victim should not have created a normal and facebook account and sign-in before
2. If Application alerts users about sign-in via facebook and allows social sign-in remove then impact goes very down 
3. Most of applications when facing no-email would redirect to home page with response {"statusCode":400,"error":"invalid_grant","message":"Bad Request","error_description":"Bad credentials"}

But I have found this issue in some programs and been rewarded also the rewards depended upon complexity to reach account and user not know did someone made an account on his behalf before. So this was a case of Pre-Account takeover still be active on many applications so do test this scenario if you find a Facebook signup.

Press enter or click to view image in full size

Special Thanks: Yash for proof-reading

Thanks for reading please provide feel free to give your feedback for the writeup.

Feel free to connect with me on Twitter, Linkedin, Website
