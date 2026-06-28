---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2018-07-02_chaining-multiple-vulnerabilities-to-gain-admin-access.md
original_filename: 2018-07-02_chaining-multiple-vulnerabilities-to-gain-admin-access.md
title: Chaining Multiple Vulnerabilities to Gain Admin Access
category: documents
detected_topics:
- api-security
- sso
- idor
- command-injection
- password-reset
- mfa
tags:
- imported
- documents
- api-security
- sso
- idor
- command-injection
- password-reset
- mfa
language: en
raw_sha256: 320c36d860815a47551b43ec088c8a09433f7a99798358f371a39fa6caea5a75
text_sha256: 203c5098c44fa0e4f6ce38034055c099321f71ace45bb4178c123e5c8226e816
ingested_at: '2026-06-28T07:31:57Z'
sensitivity: unknown
redactions_applied: false
---

# Chaining Multiple Vulnerabilities to Gain Admin Access

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2018-07-02_chaining-multiple-vulnerabilities-to-gain-admin-access.md
- Source Type: markdown
- Detected Topics: api-security, sso, idor, command-injection, password-reset, mfa
- Ingested At: 2026-06-28T07:31:57Z
- Redactions Applied: False
- Raw SHA256: `320c36d860815a47551b43ec088c8a09433f7a99798358f371a39fa6caea5a75`
- Text SHA256: `203c5098c44fa0e4f6ce38034055c099321f71ace45bb4178c123e5c8226e816`


## Content

---
title: "Chaining Multiple Vulnerabilities to Gain Admin Access"
page_title: "Chaining Multiple Vulnerabilities to Gain Admin Access  — NahamSec"
url: "https://www.nahamsec.com/posts/chaining-multiple-vulnerabilities-to-gain-admin-access"
final_url: "https://www.nahamsec.com/posts/chaining-multiple-vulnerabilities-to-gain-admin-access"
authors: ["Ben Sadeghipour (@nahamsec)"]
bugs: ["IDOR", "Account takeover"]
publication_date: "2018-07-02"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5820
---

# Chaining Multiple Vulnerabilities to Gain Admin Access 

[Vulnerability Write-Ups](/posts/category/Vulnerability+Write-Ups)

Jul 2

Written By [Ben Sadeghipour](/posts?author=5d543d375042ad0001fc1bc2)

In April of this year I participated in a private program on HackerOne that was vulnerable to a series of IDOR that led to a complete takeover of an application. Unfortunately because this is a private program, I cannot disclose the name or company related information per their request. However I wanted to share the details on how I escalated my basic privileges from a regular “customer” account to an admin user.

## **RECON**

This stage was pretty easy: They had included all of their sites and subdomains in scope of the program and lucky for me there weren’t too many of them. However, there were two sites that caught my attention: app.site.com and admin.site.com, pretty standard, but we’ll talk about them later.

### **Understanding the Application**

When testing any application, I try to use it as it’s intended but I do have burp running in the background on another monitor just to see how and what requests are made. This helps tremendously to see how the application sends/receives data.

The core application seemed pretty small with not a whole lot to find, so naturally after a couple of hours of looking, I took a break… and to be very honest, I kind of gave up (yeah, yeah, it happens).

## **SECOND ATTEMPT**

On my second attempt, I wanted to be able to look at a different site, especially since the core application seemed to be a bit smaller than expected. At this point I had the options to fuzz the API or look at the other subdomains. Since there was an admin site, I wanted to see if there any ways to gain access to the admin panel, but I wasn’t able to see its content as it would just say “access denied”, but using a VPN I was lucky enough to be able to see its content. Later on when the challenge was over, I talked to some of the other hackers and found out they were not able to see the admin site either, but somehow my VPN provider allowed me to gain access to its content (I never investigated the reason why, but it worked out in my favor).

Once I visited the admin site, as expected, I was prompted to enter my credentials, but there was also a drop down menu that gave me two options: 1. Login 2. Register

When I tried the registration form on the admin site, the API would return an error that said “registration failed”. As expected it wasn’t going to be that easy to create an account, but something caught my attention.

### **Finding My First Two Vulnerabilities**

The registration form made a request to the same endpoint (/api/register) on the admin site as the one on the core app, however it was missing a piece: The original request on the admin site looked similar to the following:  

  
  
  POST /api/register HTTP/1.1 
  Host: admin.site.com
  
  {"firstName":null,"lastName":null,"login":"[email-address@site.com](mailto:email-address@site.com)","email":"email-address@site.com","password":"hunter2"}

Let’s compare that to core application:  

  
  
  POST /api/register HTTP/1.1
  Host: app.site.com
  
  
  

So it looks like there is a bit of information missing from the first request: securityQuestions. After adding the missing piece, I was able to create an account on the admin site but there was still a tiny hiccup: The admin site required you to authenticate using 2FA. This wasn’t too bad, I assumed there may be a way to bypass the 2FA but giving it a blank or random value. Fortunately for me, 123456 served as a valid authentication code (since I didn’t have a 2FA set, any number would’ve probably worked), but my problems didn’t really end there since my user has “read-only” privileges on a few pages, including profile settings and a few others that weren’t really that interesting, but it was a great starting point!

### **Focusing on Things That Were in My Control**

As I mentioned earlier, I only had access to a few pages. The admin site had a settings menu that allowed users to modify their email address, password, and 2FA settings. When I would attempt to change my information the site would respond with “Something went wrong”, but since I didn’t have 2FA set on my account, it allowed me to modify it by making an empty POST request:
  
  
  POST /api/users/newAuthenticationCode/46774
  HTTP/1.1 Host: admin.site.com
  

Which return a key:`  
`

When the page is loading, there’s another request made to /api/users/authenticationCode/YNFTHSAJVOR3RS6B that loaded my QR code. As you probably guessed it, I was able to swap my user_id (46774) and create a new authentication code for any users and I was able to use the QR code to register it on my device using any 2FA tools like Duo/Google Authenticator. 

## **FILING A DUPLICATE**

One of the only pages that I had access to was an empty “users” page that did not return any of the users on the site but it allowed you to search for them. This page would make a GET request similar to the one below:
  
  
  /api/users/search?page=&size=20&ascending=true&orderBy=Login&searchString=My_SEARCH_STRING&userRole=

Now there are a few things that were helpful later on:

  1. The application has different user roles, which I still don’t know how they work at this point.

  2. If you deleted the value for searchString, size, and page, then you would receive the entire database of users which included their UID, email, login_id, profile (which is the same as user role), and few other minor details.

I immediately reported it to the program, however, another hacker had already reported this exact vulnerability on the core application. That is totally okay, I can probably use this information later.

### **Something _Really_ Went Wrong**

Now that I had enough information, I wanted to try and see if I can finally gain more than read-only access. When a user would try to change their user details within the admin site, the application would make the following request:
  
  
  PUT /api/users HTTP/1.1
  Host: admin.site.com
  
  

Let’s break this down very quickly: I have a user with the ID 46774, registered with the email and login values as email-address@site.com, that’s activated, not locked, no failed login attempts, my authorities where ROLE_USER (read-only), with an 2FA activated.

Using this endpoint I wasn’t able to successfully change any user data when I would replace the id value with my other user’s id, or at least that’s what looked like. Since I really wanted to get an admin account, I decided to pull a list of all the current admin accounts in order to bruteforce for weak credentials. This is when I realized, regardless of the “Something went wrong” error, my other account’s information was actually changed. In other words: the application was returning an error even though it was successfully making the changes. When I filed this report, I asked permission to change the information belonging to one of the admin accounts and they allowed me to test the account with a specific user ID.

## **CHAINING BUGS**

So at this point, I have confirmed the ability to create a new authentication code and altering other user accounts by simply changing the id value. Since I was given a user_id (user_id:3), I created a new QR code for the 2FA and imported into Google authenticator, then I changed the email address and with a sample password reset I was able to get in!

### **Bonus Round**

Once I had become an admin, I was able to understand the application better. The users were broken in different “roles”: role_admin, role_user, developers, and etc. What was interesting is that some of the API endpoints that were available to admins were also accessible by regular users if you knew the routes.

### **A Happy Accident**

When I went back to revisit the application a few days later, I noticed I had accidently used my credentials from the core application (app.site.com) and it had allowed me to access the admin page with a read-only account again. After all, I really didn’t need to figure out how the registration worked on the admin page in order to access it! Looking through my burp site map, I noticed the following request I had made using the admin account I had taken over:
  
  
  POST /api/account/updateAdmin
  Host: admin.site.com
  
  

This is very similar as the request made to /api/users earlier in this blog post. However, I was able alter the “authorities” value using this endpoint and not the other. So by sending the same exact request, with different value for the user ID, on my read-only account that was registered on the core application:
  
  
  {"id":46754,"login":"[email-address2@site.com](mailto:email-address2@site.com)","firstName":null,"lastName":null,"email":"[email-address2@site.com](mailto:email-address2@site.com)","activated":true,"locked":false,"failedLoginAttempts":0,"authorities":["ROLE_ADMIN"],"passwordLastModifiedOn":1523930764000,"address":

I had once again, escalated my user from a read-only account to an admin.

## **LESSONS LEARNED**

  1. Recon doesn’t necessarily mean gathering subdomains and file/directory listing, it is also understanding what and how the application does what it’s supposed to do.

  2. Looks could be deceiving: What may seem like an unsuccessful attempt, may have partially worked. With that said, don’t rely on error messages and try to confirm things on your own.

  3. 2FA doesn’t mean a dead end: We are all human and we all make mistakes, so try and put yourself in the developers shoes and think of where/what could you have possibly done wrong.

  4. If you can’t find a bug on your first attempt, give it some time and go back to your target with a fresh new set of eyes… Sleeping usually helps a lot!

  5. Chain bugs for a bigger payout!

  6. It may take time at first, but don’t give up! 

[bug bounty](/posts/tag/bug+bounty)[idor](/posts/tag/idor)[hacking](/posts/tag/hacking)

[ Ben Sadeghipour ](/posts?author=5d543d375042ad0001fc1bc2)
