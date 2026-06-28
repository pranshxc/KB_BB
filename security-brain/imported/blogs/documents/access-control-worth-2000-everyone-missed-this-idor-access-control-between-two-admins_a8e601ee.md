---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-06-28_access-control-worth-2000-everyone-missed-this-idoraccess-control-between-two-ad.md
original_filename: 2022-06-28_access-control-worth-2000-everyone-missed-this-idoraccess-control-between-two-ad.md
title: Access control worth $2000 (everyone missed this IDOR+Access control between
  two admins.)
category: documents
detected_topics:
- access-control
- automation-abuse
- api-security
- mobile-security
- idor
- command-injection
tags:
- imported
- documents
- access-control
- automation-abuse
- api-security
- mobile-security
- idor
- command-injection
language: en
raw_sha256: a8e601eef578deb1702896da406610fd60fcb42e3571e0a179afd18c21da2df4
text_sha256: 9b05be117d38d4509f3d119a5ec5c1a3dded9defa7691b293186331d645c7918
ingested_at: '2026-06-28T07:32:12Z'
sensitivity: unknown
redactions_applied: true
---

# Access control worth $2000 (everyone missed this IDOR+Access control between two admins.)

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-06-28_access-control-worth-2000-everyone-missed-this-idoraccess-control-between-two-ad.md
- Source Type: markdown
- Detected Topics: access-control, automation-abuse, api-security, mobile-security, idor, command-injection
- Ingested At: 2026-06-28T07:32:12Z
- Redactions Applied: True
- Raw SHA256: `a8e601eef578deb1702896da406610fd60fcb42e3571e0a179afd18c21da2df4`
- Text SHA256: `9b05be117d38d4509f3d119a5ec5c1a3dded9defa7691b293186331d645c7918`


## Content

---
title: "Access control worth $2000 (everyone missed this IDOR+Access control between two admins.)"
url: "https://medium.com/pentesternepal/access-control-worth-2000-everyone-missed-this-idor-access-control-between-two-admins-9745eaf15d21"
authors: ["dhakal_bibek (@dhakal__bibek)"]
bugs: ["IDOR", "Broken Access Control"]
bounty: "2,000"
publication_date: "2022-06-28"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 2507
scraped_via: "browseros"
---

# Access control worth $2000 (everyone missed this IDOR+Access control between two admins.)

Access control worth $2000 (everyone missed this IDOR+Access control between two admins.)
dhakal_bibek
Follow
9 min read
·
Jun 28, 2022

622

1

Tribute to 
Binit Ghimire

I was not about to write this write-up but, due to the death of our fellow hacker 
Binit Ghimire
 (The Internet Hero). I have made my mindset to share what I have gathered regularly. I promise you the readers, I “dhakal_bibek” will be more helpful. Also, for our Nepali community #everyone lets share what we could contribute as, we have lost a GEM of our country and our community needs helpful people like 
Binit Ghimire
 to survive.

You can read his writeups from below link:

Read what Binit writes @ WHOISpublish! | Binit Ghimire
I am a Tech Enthusiastic full-stack web developer, programmer and web/network penetration tester from Nepal.

publish.whoisbinit.me

Hello amazing peoples reading this write up, I am Bibek Dhakal back again with another write-up. This time I am about to explain my methodologies towards the access control vulnerabilities and how I found an interesting issue in one of my private programs. I have shared some of my tips regarding bugbounty which are used by top bugbounty hunters and are unknown to must of us. If you just want the steps to reproduce for the bug, and not the story of how it was found, go to the bottom on the Steps to Reproduce section.

I usually search for an access control vulnerabilities using both automation and manual way. For automation, I use Autorize Burp extension. And for manual process I use PWNfox (great tool if you tend to search for bugs using burp HTTP history and filter by search on burp).

Press enter or click to view image in full size
PWNfox

The Crane(Account Switching) tool for IDOR and access control in IOS

Most of the people where asking me about my IOS testing methodologies. I will make a complete separate write up regarding this but, for this time presenting you with a secret tool for creating containers.Let me present you the “Crane”, is the best tool for creating multiple containers just like pwnfox. Guys I have tried cloning the apps for testing purposes but, due to some reason the clone apps were not working. But, then I discovered the Crane tweak. Now, I can test for IDOR and access control vulnerabilities in any ios application using only one ios device...

Press enter or click to view image in full size
crane

Let’s begin the story. It all started when I was invited to a private program on Hackerone and lets just call it redirected.com. The program was pretty much fresh and there were few fellow hackers on the HOF of that program. First off all, I just opened the program as a normal guy, as in order to hack a program like a hacker you need to understand the program well. For me, hacking is not like going straight and using burp suite to hack into the target. I usually like to make a blue print of the program before using any tools. After 30 minutes of looking into the program and understanding how it works, I was ready to hack that program.

https://yankeeyank.tumblr.com/post/22155230326

I realized the program had a lot of user permissions and access control stuffs. I was like, “Let’s open the Autorize and start the process”. I ran the Autorize tool and within few minutes I found a bug and reported it.

https://www.reddit.com/r/reactiongifs/comments/2zk2ds/mrw_i_have_a_paper_due_the_following_morning/

I had also noticed that there was yet another endpoint which might be vulnerable and was a change password endpoint where the old password was not checked while changing the password. That day I was pretty much tired as I was doing the same thing in my office and home. Around 9:30 pm I just went to sleep after reporting an access control vulnerability which was discovered using Autorize.

Next day

Next day, I opened the mail to check any updates, to my surprise what I had consider a security vulnerability was actually a feature and was closed as N/A(Not Applicable).

https://www.funnyjunk.com/funny_pictures/3884590/Spongebob+feels/369

Actually it was a feature available to view for the user with the “Collateral Extended” role. I was very much serious at that point and fired up my burp and this time I was searching for access control bugs using a manual process.

I invited a user and provided an admin role to it. Now, there are two admin’s in that program. Now, I thought that there might be some access control between the same role users. At that time I was tired and hungry after getting a N/A from the team and also because I was hungry. I just went out with 
Ananda Dhakal
 by packing our guitar and some foods from mote dai ko pasal. We went to our regular spot and sang for a while. To my surprise, an idea hit in my brain.

I haven't looked at the password change functionality which was a PATCH request and was using the users id while changing the password. I was in a hurry and we went home.

Press enter or click to view image in full size

This time I was like lets pwn this. I intercepted the request to change the password and the request looked like below:

I sent the request to the repeater and changed the userID of one admin user to another admin’s id. The response was 412 Precondition Failed. I had send the PATCH request on repeater of burp suite. When ever I tried to send that request from repeater, it threw the same error.

412 error

Any request can contain a conditional header defined in HTTP (If-Match, If-Modified-Since, etc.) or the “If” or “Overwrite” conditional headers defined in this specification. If the server evaluates a conditional header, and if that condition fails to hold, then this error code must be returned. On the other hand, if the client did not include a conditional header in the request, then the server must not use this status code.

just googling this error, an Idea struck my mind:

Now, I started intercepting the request and changing each and every request with the user id of 169 to 221. -> we wont leave any request, even the OPTIONS one as, we dont want any 412 precondition failed errors: Also, we will do it from the burp intercept, and not using the repeater tab.

I was happy as It didn’t throw the 403 error. Now, I began to check the HTTP history of burp, and saw 3 three request. First one was OPTIONS request, after that there was a GET request and finally there was a PATCH request.

Get dhakal_bibek’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

First Request:

OPTIONS /api/v3/myhealth/users/221 HTTP/1.1
Host: XXXXxxxxxXXXXX
User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:100.0) Gecko/20100101 Firefox/100.0
Accept: */*
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Referer: https://xxxxXXXXXxxxx.com/
Authorization: Bearer ***REDACTED***
Origin: https://XXXXXXxxxxXXX.com
Connection: close

Second Request:

GET /api/v3/myhealth/users/221 HTTP/1.1
Host: XXXXxxxxxXXXXX
User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:100.0) Gecko/20100101 Firefox/100.0
Accept: */*
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Referer: https://xxxxXXXXXxxxx.com/
Authorization: Bearer ***REDACTED***
Origin: https://XXXXXXxxxxXXX.com
Connection: close
Sec-Fetch-Dest: empty
Sec-Fetch-Mode: cors
Sec-Fetch-Site: cross-site
If-None-Match: XXXXXXxxxxxxxxXXXXXX

Third Request:

PATCH /api/v3/myhealth/users/221 HTTP/1.1
Host: XXXXXXxxxXXXX.com
User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:100.0) Gecko/20100101 Firefox/100.0
Accept: */*
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Referer: https://XXXxxxxxxxxXXXX.com/
Content-Type: application/json
Authorization: Bearer ***REDACTED***
If-Match: XXXXXXXxxxxxxxXXXXXXX
Content-Length: 58
Origin: XXXXXXXxxxxxxxXXXXXX.com
Connection: close
Sec-Fetch-Dest: empty
Sec-Fetch-Mode: cors
Sec-Fetch-Site: cross-site
{"password":"XXXXXXXXXX"}

For the POC of this attack, I hacked into the test account of my fellow hacker who was in the same program to provide a valid POC as Hackeone triage always prefer a valid POC:

Press enter or click to view image in full size

Also, After that I reported 3 more findings and the program was paused:

Bug Timeline:

Reported: Apr 29th (2 months ago)

Triaged: May 2nd (2 months ago)

Bounty Awarded: May 2nd (2 months ago) ($2000)

Resolved: May 17th (about 1 month ago)

Steps To Reproduce:

1: From admin account, go to https://sectest.xxx.redirect.com/user-settings

2: Set old password as garbage → by default it doesn't check the old password, old password is not validated in the backend side.

3: The PATCH request mentioned above allowed malicious user to change other user’s password.

FIX:

Add proper access control in the API endpoints(server side) and validate the old password while setting the new password.

Impact

An admin can invite anyone, delete anyone but, he/she should not be able to login to the victims account and access their account .

The malicious admin can change the victim admin’s password and do bad stuffs on his behalf and the victim would be the one to take all the blame for the wrongdoings.

My handle:

1: hackerone: https://hackerone.com/dhakal_bibek?type=user

2: Twiter: https://twitter.com/dhakal__bibek

Some of my tips:

While hacking an application, think how the programmer could have coded and try to exploit their logic. Since we are in blackbox approach, if you want to kill your enemy then first thing to do is to think like your enemy and you will get an idea to hack your target

Sometimes I feel hacking as, “a war between automation and manual testing”. Automaters are automating things that are beyond our thinking, while manual testers are finding so-called unique flaws, which is improving the community’s knowledge. So we need to do both!!!

For an example, If you can earn $5000 just by spending $50 then, please give it a shot!!. From my side, It was a great experience for me to purchase the product and to search for bugs on their premium features. I have just found a high severity issue in the premium version of redirect.com at the time of writing this sentence. Bug is a “race condition to bypass invitation limitation”. Why high, cause in the pro version only 3 members are allowed and in the premium 10 members are allowed. Now, by exploiting this vulnerability an attacker is able to invite infinite number of members.

Remember, we are humans and humans can outnumber robots. I dont call it a hacking, I call it a war between AI and the humans. “We are hackers and if someday AI comes to take our job then, we should be the one testing for bugs on AI…” By :- 
dhakal_bibek

Instead of overlooking at the same stuff over and over again, get some fresh air and comeback with a new mindset to exploit those programmers. We are infiltrating the programmer’s mind. Also, stick on the same program for a long time. I love programmers as we are the outcome of vulnerable code.

Don’t give up so fast, I have made it here using 4 hackerone accounts. 3 of my accounts have a negative reputation with a 0 private program invitation. To be frank, this path is hard and tough. But, you can easily stand up if you make a different approach like: ios/android testing, smartwatch apps testing, memory corruption, source code analysis, and always try to search for bugs which could be out of reach for automated scanners. For web application security testing, try searching for bugs on their pro/premium/VIP services, thats what less then 10% hunters are doing…

Press enter or click to view image in full size
less then 1% hackers are searching for memory corruption.

Guys, donot forget to follow https://twitter.com/equat0rium in twitter as he is 16 years old hacker who is searching for memory corruption vulnerabilities. @equat0rium if you are reading this then, “Happy to get followed by you. It is one of my life goal to meet you in person.”

Also Do not forget to follow me in twitter, as I will be sharing some cool stuffs over there and I don’t usually write write-ups... Also I am not that good at explaining hacking stuffs in English…

Twiter: https://twitter.com/dhakal__bibek

Twiter: https://twitter.com/dhakal__bibek

Also, this mind peace YouTube channel has helped a lot for me to cool my stress and burnouts during my bug bounty journey. The music provided by mind peace is targeted for hackers/programmers.
