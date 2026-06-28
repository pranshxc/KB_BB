---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2018-08-07_from-data-leak-to-account-takeover.md
original_filename: 2018-08-07_from-data-leak-to-account-takeover.md
title: From data leak to account takeover
category: documents
detected_topics:
- password-reset
- command-injection
- mfa
- otp
- rate-limit
- information-disclosure
tags:
- imported
- documents
- password-reset
- command-injection
- mfa
- otp
- rate-limit
- information-disclosure
language: en
raw_sha256: bef9be67d88f67f052537826417ceefc2d761273170a4c44e6f74d689f3b0b72
text_sha256: 319267b41e3926c9f2e1dd2ee39a5963b5265a3f227f194a7503b83271080bbd
ingested_at: '2026-06-28T07:31:57Z'
sensitivity: unknown
redactions_applied: false
---

# From data leak to account takeover

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2018-08-07_from-data-leak-to-account-takeover.md
- Source Type: markdown
- Detected Topics: password-reset, command-injection, mfa, otp, rate-limit, information-disclosure
- Ingested At: 2026-06-28T07:31:57Z
- Redactions Applied: False
- Raw SHA256: `bef9be67d88f67f052537826417ceefc2d761273170a4c44e6f74d689f3b0b72`
- Text SHA256: `319267b41e3926c9f2e1dd2ee39a5963b5265a3f227f194a7503b83271080bbd`


## Content

---
title: "From data leak to account takeover"
page_title: "From data leak to account takeover - DEV Community"
url: "https://dev.to/antogarand/from-data-leak-to-account-takeover-1kck"
final_url: "https://dev.to/antogarand/from-data-leak-to-account-takeover-1kck"
authors: ["Antony Garand (@AntoGarand)"]
bugs: ["Account takeover", "Information disclosure", "Password reset"]
publication_date: "2018-08-07"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5766
---

[![Antony Garand](https://media2.dev.to/dynamic/image/width=50,height=50,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.us-east-2.amazonaws.com%2Fuploads%2Fuser%2Fprofile_image%2F77692%2F42cc26a2-feb1-42cc-9dbe-7df4f85f9e48.jpg)](/antogarand)

[Antony Garand](/antogarand)

Posted on Aug 7, 2018 • Edited on Aug 13, 2018

![](https://assets.dev.to/assets/sparkle-heart-5f9bee3767e18deb1bb725290cb151c25234768a0e9a2bd39370c382d02920cf.svg) ![](https://assets.dev.to/assets/multi-unicorn-b44d6f8c23cdd00964192bedc38af3e82463978aa611b4365bd33a0f1f4f3e97.svg) ![](https://assets.dev.to/assets/exploding-head-daceb38d627e6ae9b730f36a1e390fca556a4289d5a41abb2c35068ad3e2c4b5.svg) ![](https://assets.dev.to/assets/raised-hands-74b2099fd66a39f2d7eed9305ee0f4553df0eb7b4f11b01b6b1b499973048fe5.svg) ![](https://assets.dev.to/assets/fire-f60e7a582391810302117f987b22a8ef04a2fe0df7e3258a5f49332df1cec71e.svg)

#  From data leak to account takeover 

[#security](/t/security) [#writeup](/t/writeup)

#  Introduction 

While browsing the web, I ended up finding a startup which recently launched its product. Like any normal person, I decided to perform a security audit to hopefully find vulnerabilities!

In this post, I will write about the journey, from the initial leak of my account information to complete arbitrary account takeover.

For the purpose of this post, all identifiable information was replaced with mocked data.

#  Information leak 

When accessing the app for the first time, you could create an account.  
Creating an account did let you access your own profile, which contains few typical profile fields such as a name, email and profile picture. 

The fields visible on the screen are not the only ones returned by the api though.  
When initially loading the page, a GET request would be made to the api to access our user information.  
This endpoint, `/api/user`, would also return what I believe is the whole stored document, including its private information.  

  
  
  {
  "user": {
  "_id": "UUID",
  "name": "My Name",
  "role": "Other",
  "email": "test@email.invalid",
  "emailVerified": false,
  "emailVerificationToken": "t3gauljva4dbu8zyn1xp6u",
  "password": "$2a$10$HsQX/kYcnyly.oaykq5RxuC/IOrpSOVQnaPM18.NNxfkU/AFYaTzG",
  "signupDate": "2018-07-11T20:39:31.070Z",
  // ...
  },
  "teamInfo": {/* ... */ }
  }
  

Already, you can see that the password hash is beeing leaked, which is quite the security issue!  
  
Leaking the hash lets hackers attempt to validate the password on their own machines, without any rate limits or logging mechanism in place. This makes it easier to bruteforce and impossible to detect!

#  Email validation 

From the previous information leak, you may have noticed the `emailVerificationToken` key on the user object.  
  
Having access to this token means I could validate any email, as long as I have access to the validation URL and the leaked token.

To try this out, I changed out the email for a valid one and received a genuine email validation link:  

  
  
  Thanks for signing up! To complete the sign-up process, please click the link below to verify your email:
  https://app.sample.com/verify/1234tokenhere
  

Now that I have the email validation link, I changed my email to one I did not control, such as `admin@application.com`.  
  
Once my user profile updated, all I had to do was leak the new email token and verify my new email!

#  Password recovery 

When forgetting your password, a typical scenario is to enter your email, which then receives a password reset link.  
From this password reset link, you can enter an arbitrary new password, and log into your account!

This application is not different, although it did not correctly protect its password reset tokens!  
  
While the field was not present in the previously returned JSON, I did notice it was added when I triggered the first password reset request.  
  
Like with the email verification link, I could therefore craft a valid password reset link myself!

#  Teams 

Until now, all we could do was only affecting our own user. Fortunately, looking closely at the previously leaked information, one may notice there is not only our own information returned, but also our team information!  
  
We can create and manage teams from the application, and all of the team data will be leaked as well.  

  
  
  {
  "user": { /* ... */
  },
  "teamInfo": {
  "owner": { /* ... */ },
  "name": "Sample team",
  "admins": [ /* ... */ ],
  "members": [ /* ... */ ]
  }
  }
  

The interesting part of the team leak is regarding the owner and members fields.  
  
When being added into a team, I could therefore leak the team owner and all of its member's password reset tokens!  
  
But this still limits the scope of the attack to members of our team, and we can do better than this.

When owning a team, we can invite team members via their emails, and there is no confirmation required from the invited user. 

This means that as a newly registered user, I can perform the following steps to overtake any account: 

  * Perform a password change request for my target
  * Create a new team
  * Invite my target
  * Leak the password reset token via my team information
  * Change my victim's password

As well as change and validate a new invalid email for this user, which would lock them out of their account.

#  Conclusion 

It is easy to send too much data to our front-end, but we need to be cautious about the sensible information which is stored.  
In this case, giving out too much information about a user led to a complete account takeover!

##  Top comments (5)

Subscribe

![pic](https://media2.dev.to/dynamic/image/width=256,height=,fit=scale-down,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2F8j7kvp660rqzt99zui8e.png)

Personal Trusted User

[ Create template ](/settings/response-templates)

Templates let you quickly answer FAQs or store snippets for re-use.

Submit Preview [Dismiss](/404.html)

[ ![kip13 profile image](https://media2.dev.to/dynamic/image/width=50,height=50,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.us-east-2.amazonaws.com%2Fuploads%2Fuser%2Fprofile_image%2F55199%2F65ba1104-0b37-407b-8326-46412fe2cc77.jpeg) ](https://dev.to/kip13)

[ kip  ](https://dev.to/kip13)

kip 

[ ![](https://media2.dev.to/dynamic/image/width=90,height=90,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.us-east-2.amazonaws.com%2Fuploads%2Fuser%2Fprofile_image%2F55199%2F65ba1104-0b37-407b-8326-46412fe2cc77.jpeg) kip  ](/kip13)

Follow

404 bio not found ... yet 

  * Joined 

Jan 25, 2018

• [ Aug 7 '18  ](https://dev.to/antogarand/from-data-leak-to-account-takeover-1kck#comment-4gp1)

  * [Copy link](https://dev.to/antogarand/from-data-leak-to-account-takeover-1kck#comment-4gp1)
  *  * Hide 
  *  *  * 

> Like any normal person, I decided to perform a security audit to hopefully find vulnerabilities!

Of course, the activity from any normal person !

7 likes Like  Reply

[ ![dploeger profile image](https://media2.dev.to/dynamic/image/width=50,height=50,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.us-east-2.amazonaws.com%2Fuploads%2Fuser%2Fprofile_image%2F80631%2F28cc809c-a845-460e-8ab9-9fa5e64d9990.jpeg) ](https://dev.to/dploeger)

[ Dennis Ploeger  ](https://dev.to/dploeger)

Dennis Ploeger 

[ ![](https://media2.dev.to/dynamic/image/width=90,height=90,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.us-east-2.amazonaws.com%2Fuploads%2Fuser%2Fprofile_image%2F80631%2F28cc809c-a845-460e-8ab9-9fa5e64d9990.jpeg) Dennis Ploeger  ](/dploeger)

Follow

I'm a Senior DevOps Architect and publish most of my projects as open source. I have a wife, a son and a real life in Hamm, Germany. In my part-time I enjoy making games, music and acting. (He/him) 

  * Location 

Hamm, Germany 

  * Work 

Senior DevOps Architect at KPS AG 

  * Joined 

Jun 25, 2018

• [ Aug 7 '18  ](https://dev.to/antogarand/from-data-leak-to-account-takeover-1kck#comment-4h35)

  * [Copy link](https://dev.to/antogarand/from-data-leak-to-account-takeover-1kck#comment-4h35)
  *  * Hide 
  *  *  * 

And that, kids, is why you have DTOs, that are exchanged with the API and DAOs, that get saved in the database.

Nice post! Thanks!

3 likes Like  Reply

[ ![michaelgv profile image](https://media2.dev.to/dynamic/image/width=50,height=50,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.us-east-2.amazonaws.com%2Fuploads%2Fuser%2Fprofile_image%2F36783%2Fd4c579fb-81fa-46d1-a5f4-1ccce1a0e6ff.png) ](https://dev.to/michaelgv)

[ Mike  ](https://dev.to/michaelgv)

Mike 

[ ![](https://media2.dev.to/dynamic/image/width=90,height=90,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.us-east-2.amazonaws.com%2Fuploads%2Fuser%2Fprofile_image%2F36783%2Fd4c579fb-81fa-46d1-a5f4-1ccce1a0e6ff.png) Mike  ](/michaelgv)

Follow

Full-time freelancer; Former Lead Engineer / Senior Management; speaker; 14 years in development; open for consulting and freelance opportunities. 

  * Location 

Canada 

  * Work 

Founder / CEO 

  * Joined 

Oct 11, 2017

• [ Aug 8 '18  ](https://dev.to/antogarand/from-data-leak-to-account-takeover-1kck#comment-4h59)

  * [Copy link](https://dev.to/antogarand/from-data-leak-to-account-takeover-1kck#comment-4h59)
  *  * Hide 
  *  *  * 

for those who don’t know what DTOs, and DAOs are:

[stackoverflow.com/a/14366441/8942017](https://stackoverflow.com/a/14366441/8942017)

1 like Like  Reply

[ ![gmartigny profile image](https://media2.dev.to/dynamic/image/width=50,height=50,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.us-east-2.amazonaws.com%2Fuploads%2Fuser%2Fprofile_image%2F59396%2Fa3e2cd08-87bc-4a11-832f-993c5843a943.jpg) ](https://dev.to/gmartigny)

[ Guillaume Martigny  ](https://dev.to/gmartigny)

Guillaume Martigny 

[ ![](https://media2.dev.to/dynamic/image/width=90,height=90,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.us-east-2.amazonaws.com%2Fuploads%2Fuser%2Fprofile_image%2F59396%2Fa3e2cd08-87bc-4a11-832f-993c5843a943.jpg) Guillaume Martigny  ](/gmartigny)

Follow

JavaScript spitter and video-games gatherer. 

  * Email 

[guillaume.martigny@gmail.com](mailto:guillaume.martigny@gmail.com)

  * Location 

France 

  * Education 

+5 

  * Work 

Lead Developer 

  * Joined 

Feb 25, 2018

• [ Aug 8 '18  ](https://dev.to/antogarand/from-data-leak-to-account-takeover-1kck#comment-4haf)

  * [Copy link](https://dev.to/antogarand/from-data-leak-to-account-takeover-1kck#comment-4haf)
  *  * Hide 
  *  *  * 

Nice post, I hope you warn the owner of said application. You could even ask for some compensation for your security check.

1 like Like  Reply

[ ![antogarand profile image](https://media2.dev.to/dynamic/image/width=50,height=50,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.us-east-2.amazonaws.com%2Fuploads%2Fuser%2Fprofile_image%2F77692%2F42cc26a2-feb1-42cc-9dbe-7df4f85f9e48.jpg) ](https://dev.to/antogarand)

[ Antony Garand  ](https://dev.to/antogarand)

Antony Garand 

[ ![](https://media2.dev.to/dynamic/image/width=90,height=90,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.us-east-2.amazonaws.com%2Fuploads%2Fuser%2Fprofile_image%2F77692%2F42cc26a2-feb1-42cc-9dbe-7df4f85f9e48.jpg) Antony Garand  ](/antogarand)

Follow

Security enthusiast, FullStack developer, challenge solver 

  * Joined 

Jun 9, 2018

• [ Aug 8 '18  ](https://dev.to/antogarand/from-data-leak-to-account-takeover-1kck#comment-4hb7)

  * [Copy link](https://dev.to/antogarand/from-data-leak-to-account-takeover-1kck#comment-4hb7)
  *  * Hide 
  *  *  * 

Of course!  
  
After finding the vulnerability, I responsibly disclosed it and waited until it was patched before publishing this post.

For those interested in such process, hackerone and bugcrowd are public bug bounty programs!

1 like Like  Reply

[Code of Conduct](/code-of-conduct) • [Report abuse](/report-abuse)

Are you sure you want to hide this comment? It will become hidden in your post, but will still be visible via the comment's permalink. 

Hide child comments as well

Confirm 

For further actions, you may consider blocking this person and/or [reporting abuse](/report-abuse)
