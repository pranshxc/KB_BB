---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2019-03-03_a-simple-account-takeover-misusing-jwt-late-expiration.md
original_filename: 2019-03-03_a-simple-account-takeover-misusing-jwt-late-expiration.md
title: A simple Account takeover misusing JWT late expiration
category: documents
detected_topics:
- jwt
- access-control
- command-injection
- csrf
- business-logic
- api-security
tags:
- imported
- documents
- jwt
- access-control
- command-injection
- csrf
- business-logic
- api-security
language: en
raw_sha256: 35fcb7aa8c428f06885b9a1e4f6dff09a36253fdf1959db5eb40cda1c0b59be5
text_sha256: c052be1d06db2c3b8751d48485fa1a99410cdb86876c880e8df577219344fd8e
ingested_at: '2026-06-28T07:31:59Z'
sensitivity: unknown
redactions_applied: false
---

# A simple Account takeover misusing JWT late expiration

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2019-03-03_a-simple-account-takeover-misusing-jwt-late-expiration.md
- Source Type: markdown
- Detected Topics: jwt, access-control, command-injection, csrf, business-logic, api-security
- Ingested At: 2026-06-28T07:31:59Z
- Redactions Applied: False
- Raw SHA256: `35fcb7aa8c428f06885b9a1e4f6dff09a36253fdf1959db5eb40cda1c0b59be5`
- Text SHA256: `c052be1d06db2c3b8751d48485fa1a99410cdb86876c880e8df577219344fd8e`


## Content

---
title: "A simple Account takeover misusing JWT late expiration"
url: "http://obsidianterminal.blogspot.com/2019/03/a-simple-account-takeover-misusing-jwt.html"
final_url: "https://obsidianterminal.blogspot.com/2019/03/a-simple-account-takeover-misusing-jwt.html"
authors: ["Scalar (@mrprajapati_360)"]
bugs: ["Broken authorization", "Logic flaw"]
publication_date: "2019-03-03"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5381
---

###  Follow me on 

**Twitter: [Scalar360](https://twitter.com/Scalar360)  
**

**  
  
**

###  Blog Archive, Click to open... 

  * [ 2020 2 ](https://obsidianterminal.blogspot.com/2020/)

  * [ March 2020 2 ](https://obsidianterminal.blogspot.com/2020/03/)

  * [ 2019 3 ](https://obsidianterminal.blogspot.com/2019/)

  * [ July 2019 1 ](https://obsidianterminal.blogspot.com/2019/07/)

  * [ March 2019 2 ](https://obsidianterminal.blogspot.com/2019/03/)

  * [DOS access to a user's account (Application-Level ...](https://obsidianterminal.blogspot.com/2019/03/dos-access-to-users-account-application.html)
  * [A simple Account takeover misusing JWT late expira...](https://obsidianterminal.blogspot.com/2019/03/a-simple-account-takeover-misusing-jwt.html)

Show more Show less

Share 

  * Get link
  * Facebook
  * X
  * Pinterest
  * Email
  * Other Apps

[ March 03, 2019  ](https://obsidianterminal.blogspot.com/2019/03/a-simple-account-takeover-misusing-jwt.html "permanent link")

###  A simple Account takeover misusing JWT late expiration 

**_Hey Guys,_**  
  
This is my first write-up hope you all like this.  
  
  
_Wrote this because there is a good story to tell and currently getting bored._  

_  
_

  
The program not allow me to disclose any kind of information so, I am not disclosing name here but may be you will get it, If you hunted that one ; )  
  
I tried my best to make write-up less complicated because I am bounded by non-disclosure policy.  
  
  
I started hunting this program from 5th of feb but before that I would like to paint the situation. I was too busy in college works so, was not able to give proper time to bug bounty, was frustrated, got 4 duplicates and 2-3 bugs with low bounty. The month was not going well, for the change I started reading blogs about new techniques, mind set of approach and new methods of bug bounty. Collected all small points and started again.  
  
  
Selected this program hunted for 1 week and got 3 P4 and 1 P3 they don't give bounties for P4 even they gave me bounties for P4 and I will say thanks for their positive attitude but that can't pay my bad month.  
  
  
The program is built for users to monitor their AWS and the program is built by using AWS so, eventually I was testing Amazon 🤣🤣🤣.  
  
  
I loosed my all hope because I was testing this program from 16-17 days and got nothing good but the magic happened and I got a JWT issue and report it as soon a I can but the program found it as acceptable business issue. The issue was the JWT was not expiring till 15 minuets. So, after a admin is removed from the projects even he/she can make admin actions in project because the JWT do not expires immediately.  
  
  
After this all happened they give it won't fix tag and closed it, after that I decided this is the last night (when I found AC takeover) I am hunting this program and don't know why I started reading the report again and started summarising the whole situation going and going and going... vallah...! a idea bangs in my mind that how I can make this issue to Full account takeover.  
  
  
**_Summary:_**  
  
A assigned admin can be default admin even his/she is force fully remove from project by default admin, because application takes 15 min to destroy assigned admin's session as admin.If assigned admin is logged out then he/she can't do anything but if assigned admin is logged in during default admin removes him/her so, removed assigned admin can be default admin by following steps.  
  
  
_(there is so much admin admin in above sentence🤣.)_  
  
  
First I created 2 AC one default admin and one invited by default admin as 2nd admin.  
  
  
**_Vulnerability chain:_**  
  
1) JWT takes 15 minuets to expire.  
  
  
2) Application accepts that removed admin can send invitation again to email which is removed by default admin even attacker(removed admin) has no privilege to send invitation as he/she is removed as admin.  
(keep in mind this is happening because of JWT take 15 minuets to expire so, removed admin misuse to send invitation to own self and application accept it also.)  
  
  
3) As main action- Removed assigned admin send invitation to own self, till JWT expires.  
  
  
**_Scenario:_**  
  
Admin 1 ---- jon --> default admin  
Admin 2 ---- Tyrion --> assigned by jon  
  
1) Tyrion violate some rules so, jon remove Tyrion from project but if Tyrion is logged in during jon remove him, Tyrion's session will take 15 min to expire as admin.  
  
2)As any user get removed from project he/she gets a email that he/she is removed from project.  
  
3) As Tyrion will notify that he is removed from program, He will send invitation to own self on which e-mail he got removed by jon.  
  
4) Tyrion will remove Jon from project and will become one and only default admin because now no one can remove Tyrion as admin because only admin can remove admin and Tyrion is only admin in project.  
  
  
**_The key point:_**  
Removed admin get again full fledged admin access and his session is also restored. JWT take 15 min to expire but attacker restore it in 4 min and again have a true JWT.  
  
They do not accepted my 1st report because there was Vulnerability "but" no exploitation. I was not able to use JWT in a exploiting way but lateral thinking helps a lot in making vulnerability exploitable.  
  
I was able to hold my patients because I read a blog in which a guy spend 2+ weeks on a simple CSRF and make it a complex AC takeover and second reason [this](https://devco.re/blog/2016/04/21/how-I-hacked-facebook-and-found-someones-backdoor-script-eng-ver/)  
  
  
**_Till this date I learnt 4 principles of Bug Bounty:_**  
  
1) Give at least 1 day for recon and 2 weeks for finding to a program.  
  
2)Never loose hope and think, that I will end up with Chaos.  
  
3) Never get excited and report a small bug after finding it, think how can you make it better.  
(As you can see in this case I reported a JWT expiring issue and after lateral thinking on that I end up with a AC takeover.)  
  
4) Learning is more important than continuous hunting and running for money.  
  
  
Timeline:  
  
1) At night reported Vulnerability.  
  
2) After 5 hours of reporting received bounty as P1 at morning. 🤣  
  
  
  
  
  
-4.9.16.1.11  
  
  
  
  
  
  
  
  

Share 

  * Get link
  * Facebook
  * X
  * Pinterest
  * Email
  * Other Apps

### Comments

#### Post a Comment

[](https://www.blogger.com/comment/frame/1666996120398678746?po=8941436543034821111&hl=en-GB&saa=85391&origin=https://obsidianterminal.blogspot.com&skin=soho)

###  Popular Posts 

[ July 26, 2019  ](https://obsidianterminal.blogspot.com/2019/07/dos-in-imgix-cdns-image-processing.html "permanent link")

### [DOS in imgix CDN's image processing application by pixel flood ](https://obsidianterminal.blogspot.com/2019/07/dos-in-imgix-cdns-image-processing.html)

Share 

  * Get link
  * Facebook
  * X
  * Pinterest
  * Email
  * Other Apps

[ Post a Comment ](https://obsidianterminal.blogspot.com/2019/07/dos-in-imgix-cdns-image-processing.html#comments)

[ March 29, 2020  ](https://obsidianterminal.blogspot.com/2020/03/monthly-list-of-blogs-to-community-from.html "permanent link")

### [ Monthly List of blogs, To community from community [APRIL]](https://obsidianterminal.blogspot.com/2020/03/monthly-list-of-blogs-to-community-from.html)

Share 

  * Get link
  * Facebook
  * X
  * Pinterest
  * Email
  * Other Apps

[ 3 comments ](https://obsidianterminal.blogspot.com/2020/03/monthly-list-of-blogs-to-community-from.html#comments)

[![Image](https://1.bp.blogspot.com/zV4mfJxzcs4KVn3twtEv6ydyCvufLdRqBnZ1psVHE-x6lrctKdLE6t8-a7TtfrVD_fz9sXzEyF0=s400)](https://obsidianterminal.blogspot.com/2019/03/dos-access-to-users-account-application.html)

[ March 07, 2019  ](https://obsidianterminal.blogspot.com/2019/03/dos-access-to-users-account-application.html "permanent link")

### [DOS access to a user's account (Application-Level Denial-of-Service)](https://obsidianterminal.blogspot.com/2019/03/dos-access-to-users-account-application.html)

Share 

  * Get link
  * Facebook
  * X
  * Pinterest
  * Email
  * Other Apps

[ 1 comment ](https://obsidianterminal.blogspot.com/2019/03/dos-access-to-users-account-application.html#comments)

[ March 25, 2020  ](https://obsidianterminal.blogspot.com/2020/03/list-of-blogs-to-community-from.html "permanent link")

### [Monthly List of blogs, To community from community [MARCH] ](https://obsidianterminal.blogspot.com/2020/03/list-of-blogs-to-community-from.html)

Share 

  * Get link
  * Facebook
  * X
  * Pinterest
  * Email
  * Other Apps

[ Post a Comment ](https://obsidianterminal.blogspot.com/2020/03/list-of-blogs-to-community-from.html#comments)

###  Twitter 

[Tweets by Scalar360](https://twitter.com/Scalar360?ref_src=twsrc%5Etfw)
