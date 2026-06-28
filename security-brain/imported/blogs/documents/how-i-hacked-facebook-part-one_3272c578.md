---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-12-11_how-i-hacked-facebook-part-one.md
original_filename: 2020-12-11_how-i-hacked-facebook-part-one.md
title: 'How I hacked Facebook: Part One'
category: documents
detected_topics:
- otp
- csrf
- sso
- command-injection
tags:
- imported
- documents
- otp
- csrf
- sso
- command-injection
language: en
raw_sha256: 3272c578cf4c79c2e6b7301a506a298a9e82f208c1b1ef2bd2d05fbf29cc5b32
text_sha256: ce0d7f76967ea831e0a01497887ac6b1d759389c4aa245966849482308a8b0f8
ingested_at: '2026-06-28T07:32:04Z'
sensitivity: unknown
redactions_applied: false
---

# How I hacked Facebook: Part One

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-12-11_how-i-hacked-facebook-part-one.md
- Source Type: markdown
- Detected Topics: otp, csrf, sso, command-injection
- Ingested At: 2026-06-28T07:32:04Z
- Redactions Applied: False
- Raw SHA256: `3272c578cf4c79c2e6b7301a506a298a9e82f208c1b1ef2bd2d05fbf29cc5b32`
- Text SHA256: `ce0d7f76967ea831e0a01497887ac6b1d759389c4aa245966849482308a8b0f8`


## Content

---
title: "How I hacked Facebook: Part One"
url: "https://infosecwriteups.com/how-i-hacked-facebook-part-one-282bbb125a5d"
authors: ["Alaa Abdulridha (@alaa0x2)"]
programs: ["Meta / Facebook"]
bugs: ["Missing authentication", "Authentication bypass", "Account takeover"]
bounty: "7,500"
publication_date: "2020-12-11"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4073
scraped_via: "browseros"
---

# How I hacked Facebook: Part One

Alaa Abdulridha
 highlighted

How I hacked Facebook: Part One
Alaa Abdulridha
Follow
4 min read
·
Dec 11, 2020

1.3K

4

We’ve been in this pandemic since March and once the pandemic started I was having plenty of free time, And I need to use that time wisely, So I’ve decided to take the OSWE certification and I finished the exam on 8 of August, after that, I took a couple of weeks to recover from the OSWE exam, then in the med of September, I said you know what? I did not register my name in the Facebook hall of fame for 2020 as I do every year. okay, let’s do it.

I never found a vulnerability on one of Facebook subdomains, and I took a look at some writeups and I saw one writeup in one of Facebook subdomains which got all my attention It was a great write up you can check it out [HTML to PDF converter bug leads to RCE in Facebook server.]

So after reading this write-up now I took a good idea about how many vulnerabilities I could find in such a huge web app.

So my main target was https://legal.tapprd.thefacebook.com and my goal was RCE or something similar.

I ran some fuzzing tools just to get the full endpoints of this web app and I took a 2 hours nap and watched a movie, Then I got back to see the results okay I got some good results.

Dirs found with a 403 response:

Dirs found with a 403 response:
/tapprd/
/tapprd/content/
/tapprd/services/
/tapprd/Content/
/tapprd/api/
/tapprd/Services/
/tapprd/temp/
/tapprd/logs/
/tapprd/logs/portal/
/tapprd/logs/api/
/tapprd/certificates/
/tapprd/logs/auth/
/tapprd/logs/Portal/
/tapprd/API/
/tapprd/webroot/
/tapprd/logs/API/
/tapprd/certificates/sso/
/tapprd/callback/
/tapprd/logs/callback/
/tapprd/Webroot/
/tapprd/certificates/dkim/
/tapprd/SERVICES/

Okay, I think this result is very enough to support my previous theory about how huge this application, Then I started to read the javascript files to see how the website works and what methods it uses ..etc

I noticed a way to bypass the redirection into the Login SSO, https://legal.tapprd.thefacebook.com/tapprd/portal/authentication/login and after analyzing the login page, I noticed this endpoint

/tapprd/auth/identity/user/forgotpassword

and after doing some fuzzing on the user endpoint I’ve noticed another endpoint which its /savepassword and it was expecting a POST request, Then after reading the javascript files I knew how the page work, there should be a generated token and xsrf token.. etc The idea that first came to me okay, Lets test it and see if it will work I tried to change manually using burp suite but I got an error, the error was execution this operation failed.

I said okay, this might be because the email is wrong or something? let’s get an admin email, Then I started to put random emails in a list to make a wordlist and after that, I used the intruder and I said let’s see what will happen.

I got back after a couple of hours I found the same error results plus one other result, This one was 302 redirect to the login page, I said wow, I’ll be damned if this worked Haha.

So let’s get back to see what I’ve done here, I sent random requests using intruder with a CSRF token and random emails with a new password to this endpoint /savepassword

Get Alaa Abdulridha’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

and one of the results was 302 redirect.

Press enter or click to view image in full size

Now I went to the login page and I put the login email and the new password and BOOM I logged in Successfully into the application and I can enter the admin panel :)

Press enter or click to view image in full size

I read the hacker report who found RCE before using the PDF and they gave him a reward of 1000$ only so I said okay, let’s make a good Impact here and a perfect exploit.

I wrote a quick and simple script to exploit this vulnerability with python you put the email and the new password and the script will change the password.

Press enter or click to view image in full size

The Impact here was so high because the Facebook workers used to login with their workplace accounts, Which mean they’re using their Facebook accounts access token, and maybe if another attacker wanted to exploit this it might give him the ability to gain access to some Facebook workers accounts .. etc

Then I reported the vulnerability and the report triaged.

And on 2 of October, I received a bounty of 7500$

I enjoyed exploiting this vulnerability so much, so I said that’s not enough, this is a weak script! let’s dig more and more.

And I found two more vulnerabilities on the same application, But we will talk about the other vulnerabilities in the Part two writeup :)

You can read the write-up on my website : https://alaa.blog/2020/12/how-i-hacked-facebook-part-one/

And you can follow me on twitter : https://twitter.com/alaa0x2

Cheers.
