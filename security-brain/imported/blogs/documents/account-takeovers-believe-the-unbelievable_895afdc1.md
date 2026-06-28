---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-07-09_account-takeovers-believe-the-unbelievable.md
original_filename: 2021-07-09_account-takeovers-believe-the-unbelievable.md
title: Account Takeovers — Believe the Unbelievable
category: documents
detected_topics:
- rate-limit
- command-injection
- password-reset
- api-security
tags:
- imported
- documents
- rate-limit
- command-injection
- password-reset
- api-security
language: en
raw_sha256: 895afdc1a18e53a80bcc77ed2b5939f3a085d5800e54829b42236b9713e1a075
text_sha256: 0f1b2f75f9cab0809250fac47a479272af2351057595bd7b9888d78e1e4db7ef
ingested_at: '2026-06-28T07:32:06Z'
sensitivity: unknown
redactions_applied: true
---

# Account Takeovers — Believe the Unbelievable

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-07-09_account-takeovers-believe-the-unbelievable.md
- Source Type: markdown
- Detected Topics: rate-limit, command-injection, password-reset, api-security
- Ingested At: 2026-06-28T07:32:06Z
- Redactions Applied: True
- Raw SHA256: `895afdc1a18e53a80bcc77ed2b5939f3a085d5800e54829b42236b9713e1a075`
- Text SHA256: `0f1b2f75f9cab0809250fac47a479272af2351057595bd7b9888d78e1e4db7ef`


## Content

---
title: "Account Takeovers — Believe the Unbelievable"
page_title: "Account Takeovers By Nikhil | InfoSec Write-ups"
url: "https://infosecwriteups.com/account-takeovers-believe-the-unbelievable-bb98a0c251a4"
authors: ["Nikhil (niks) (@niksthehacker)"]
bugs: ["Account takeover", "Session management issue", "Weak credentials", "Components with known vulnerabilities", "Password reset"]
bounty: "5,751"
publication_date: "2021-07-09"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3519
scraped_via: "browseros"
---

# Account Takeovers — Believe the Unbelievable

Account Takeovers — Believe the Unbelievable
Nikhil (niks)
Follow
7 min read
·
Jul 9, 2021

1.1K

1

I had set a goal for myself to look for only account takeover issues for a certain period of time. Fortunately, I did accomplish my goal and reported a lot of ATOs. In this blog, I will share few interesting ones. They may look like easy findings on the surface level. However, I had to invest a good amount of time in the recon. Only unauthenticated testing was allowed on most of these targets.

Session Prediction

This find is related to my previous writeup on account takeover, you can only understand this after reading the previous one here (https://blog.niksthehacker.com/unauthenticated-account-takeover-through-forget-password-c120b4c1141d)

So after login into the application using credentials, I was looking for another way to take over an account. I decided to look at how the session is created. For that, I looked into my burp history and I found that it creates hd_sessionID value for each login. The value itself is 4 digits of integer for e.g 5000 (what?😳), one more thing to add here, for each successful login this value increases by 1. So let's say if the current session id value is 5000, on the next login sessionID value will be 5001.

All you need to exploit this issue is D** Ids (refer to the previous article for it) and brute-force the sessionIDs.

So, I took the request in intruder and set the payload position to hd_sessionID.

Press enter or click to view image in full size

You have to fix a hd_userId to a D** Id of the account you want to take over and run the intruder.

Press enter or click to view image in full size

“5067" was the correct sessionID for this user. I have hidden few details for obvious reasons.

Credential Disaster

I was hunting on a program where almost 700 bugs were already been accepted and were running for 4+ years. Since the program is in additional incentives mode (called blitz), which motivated me to find bugs on it.

Since the program was in wildcard scope and the company deals with textbook rentals. I decided to focus on the main app (www.target.com) since not much has been reported on it. It was running a WordPress. By supplying /wp-admin/, I moved to WordPress admin.

Now, the first thing I tried to figure out is the valid username. I used forget password and figured a “test” username. Further, I tried a few passwords and one password worked “testtest” and I got access to admin. Further, an RCE could easily be achieved but there was a STOP and Report Rule instead of escalating it further. Also, they were using WordPress for multiple other products and services, these credentials worked for all.

Press enter or click to view image in full size

And since it was cvss 10, I got a $5000 additional bonus on finding.

Press enter or click to view image in full size
CVE-2018–9845

So while hunting the same (above) application, I stumbled across a live session where a tutor can teach a student, this was a paid feature (pay as you go) but the client wants to have more focus on this area which seems to be a core part of the app.

Press enter or click to view image in full size

While doing a quick inspect element on a text editor, I found that it's running an etherpad (https://github.com/ether/etherpad-lite). A quick google search helped me find out that it's vulnerable to several CVEs. I found this one interesting CVE-2018–9845, “Etherpad Lite before 1.6.4 is exploitable for admin access.” But I couldn’t find any relevant exploit, so I went ahead and looked at commit here (https://github.com/ether/etherpad-lite/commit/ffe24c3dd93efc73e0cbf924db9a0cc40be9511b)

Press enter or click to view image in full size

Wait What?

while browsing to /path/path2//ec2/admin/, I was getting the following prompt to enter username and password.

Press enter or click to view image in full size

For bypass, I just need to upper case Admin and got admin access LOL.

Press enter or click to view image in full size
In-Security Answers

This was one of the federal programs (another old program and wildcard). I did recon and found a sub-domain to hunt on (another login/forget pass). Before attempting anything, I wanted to collect valid usernames. I follow the password reset process, so, as expected, the application asking for a username at first. First thing, run an intruder to find valid usernames, I use this wordlist usually (https://github.com/danielmiessler/SecLists/blob/master/Usernames/Names/names.txt) for usernames.

Press enter or click to view image in full size

Now, I got plenty of valid usernames and the next screen of valid usernames is entering answers. Now, each username has its own security questions, but I focused on the username which is having the following security answer

Get Nikhil (niks)’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

“What is the first name of your spouse father’s” why? because I got another wordlist to brute force it (https://github.com/danielmiessler/SecLists/blob/master/Usernames/Names/malenames-usa-top1000.txt)

Alright, next I run another intruder attack on security answer with the first name user list.

Press enter or click to view image in full size

And I got the correct name from the list. Further, you just need to set the new password and security question for the user and take over their account.

Press enter or click to view image in full size

This issue could have also locked out users from resetting their passwords if someone sets a new security question to their account. Jeez!. There was Imperva WAF was implemented to prevent any abuse, but interestingly, it kicks off after 1K attempts have been made, so it was never an issue for me.

Forget Password? Let me change it for YOU

I am able to find these kinds of issues quite frequently nowadays. So, this is the case of another subdomain of the federal programs. Another application, another “login/forget password”.

I went through forget password and enter username and it gives an interesting error related to email, (I forget what was it). I run the intruder on it with usernames list and I was actually shocked that it discloses the email addresses of valid usernames (I hide the email for privacy)

Press enter or click to view image in full size

Interesting, but what we could do further. I thought about searching the breached passwords of the user here. So I quickly went through one of the applications having tons of collections of breached passwords (Thanks to Parth Malhotra for referring one), when I searched, I found just three results, in which just one result was returning with a plaintext password.

Press enter or click to view image in full size

Interesting, I attempted this username and password in the portal and logged in LOL.

Press enter or click to view image in full size

Similarly we can take over any account on this application if their password has been leaked in a breach and they reused the same password in the portal. I found quite many of them.

Weak Passwords? 2021?

While doing recon on the same target, I came across a subdomain that was running mailman (https://www.gnu.org/software/mailman/)

It has a couple of lists, but while going through /mailman/admin/{listname} , it was asking for a password=***REDACTED*** enter or click to view image in full size

while entering just “password” and clicking on let me in, I was able to access admin account, LOL!. This wasn’t the case of just one list, there were like 3–4 others having the same password.

Press enter or click to view image in full size
There is More….

On the same target I found another subdomain where the application registers the users for some kind of report. I quickly did a google search using:

site:subdomain.com

and found some interesting results:

Press enter or click to view image in full size

Interesting right? (PII). I clicked on the link and the application was disclosing the following info

So, all the users registration form information remains available on-site itself accessible through a unique link, while PII is disclosed but the interesting part for me was the password description, which is meant to be used as password hints. I found that users shared their password in this password description field which is stored in plain text on the website. To confirm this, I did credential stuffing on one of the accounts and it worked.

That’s it for now. See you in the next article. Stay Curious.

P.S, if you want to be part of synack red team, please dm me your profile on twitter (@niksthehacker), i will refer if you have what it takes to be a SRT.

Thank you 
Bhavuk Jain
 and 
Kainat Kamal
 for proofreading.
