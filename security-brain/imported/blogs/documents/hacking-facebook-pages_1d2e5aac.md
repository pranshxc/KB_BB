---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2015-08-26_hacking-facebook-pages.md
original_filename: 2015-08-26_hacking-facebook-pages.md
title: Hacking Facebook Pages
category: documents
detected_topics:
- access-control
- sso
- command-injection
- otp
- automation-abuse
- api-security
tags:
- imported
- documents
- access-control
- sso
- command-injection
- otp
- automation-abuse
- api-security
language: en
raw_sha256: 1d2e5aac6daf2dc0807c3606a81741a98bd2d77952fc1ab30220a6dea5802b93
text_sha256: a842729883d5219724ebc61f21a40e9cfa6be059fee56432c49fb5bfae38b335
ingested_at: '2026-06-28T07:31:55Z'
sensitivity: unknown
redactions_applied: false
---

# Hacking Facebook Pages

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2015-08-26_hacking-facebook-pages.md
- Source Type: markdown
- Detected Topics: access-control, sso, command-injection, otp, automation-abuse, api-security
- Ingested At: 2026-06-28T07:31:55Z
- Redactions Applied: False
- Raw SHA256: `1d2e5aac6daf2dc0807c3606a81741a98bd2d77952fc1ab30220a6dea5802b93`
- Text SHA256: `a842729883d5219724ebc61f21a40e9cfa6be059fee56432c49fb5bfae38b335`


## Content

---
title: "Hacking Facebook Pages"
page_title: "Hacking Facebook Pages - The Zero Hack"
url: "https://thezerohack.com/hacking-facebook-pages"
final_url: "https://thezerohack.com/hacking-facebook-pages"
authors: ["Laxman Muthiyah (@LaxmanMuthiyah)"]
programs: ["Meta / Facebook"]
bugs: ["Broken authorization", "Privilege escalation", "Broken Access Control"]
bounty: "2,500"
publication_date: "2015-08-26"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 6335
---

# Hacking Facebook Pages

[![Laxman Muthiyah](https://secure.gravatar.com/avatar/b86030f152800e9eb32868123706a65f29e57b9c2cf221b504460ae27f64d655?s=96&d=mm&r=g)](https://thezerohack.com/author/laxmanm1 "Laxman Muthiyah")

By [Laxman Muthiyah](https://thezerohack.com/author/laxmanm1)

__

__March 2, 2021

__

[ Hacks / Security](https://thezerohack.com/bug-bounty-hacks)

__

Share

[__Facebook](https://www.facebook.com/sharer.php?u=https%3A%2F%2Fthezerohack.com%2Fhacking-facebook-pages "Facebook")[ __Twitter](https://twitter.com/intent/tweet?text=Hacking+Facebook+Pages&url=https%3A%2F%2Fthezerohack.com%2Fhacking-facebook-pages&via=laxmanmuthiyah "Twitter")[ __Pinterest](https://pinterest.com/pin/create/button/?url=https://thezerohack.com/hacking-facebook-pages&media=https://thezerohack.com/wp-content/uploads/2015/08/page-hack-2-2.png&description=Hacking+Facebook+Pages "Pinterest")[ __WhatsApp](https://api.whatsapp.com/send?text=Hacking+Facebook+Pages %0A%0A https://thezerohack.com/hacking-facebook-pages "WhatsApp")

__

A security vulnerability in Facebook business manager endpoint allows a third party application to hack Facebook account page with limited permissions and the victim will permanently lose admin access to the page.

By default, Facebook application interface does not allow third-party applications to add or modify page admin roles (page roles like a manager, editor, analyst etc.). Third-party applications are allowed to perform all the operations like post statuses on your behalf, publish photos, etc. except adding admin roles because if an application is allowed to add or remove admins then it could add some user as an admin to the page and remove the actual owner permanently.

On the other hand, there is an endpoint for business pages called userpermissions that allows one to add or remove business page admin roles who are already handling the Facebook business.

The following request would make target user as admin of the page.

_Request :-_

_POST / <page_id>/userpermissions HTTP/1.1_

_Host : graph.facebook.com_

_Content-Length: 245_

_role=MANAGER &user=<target_user_id>&business=<associated_business_id>&access_token=<application_access_token>_

__

_Response:-_

_true_

After a few minutes of testing, I got to know that removing the business parameter from the request didn’t throw any error and allow us to add anyone as new page admin and delete the actual page admin on the non-business page where the application has manage_pages permission.

That’s it! Whatever the application may be, if it is having the manage_pages permission of the admin then it could hack all of your Facebook account pages in a fraction of seconds.

### **Final Proof of Concept of**Page Takeover** :- **

_Request :-_

_POST / <page_id>/userpermissions HTTP/1.1_

_Host : graph.facebook.com_

_Content-Length: 245_

_role=MANAGER &user=<target_user_id>&access_token=<application_access_token>_

_true_

____

### **Removing Victim:**

_Request :-_

_Delete / <page_id>/userpermissions HTTP/1.1_

_Host : graph.facebook.com_

_Content-Length: 245_

_user= <target_user_id>&access_token=<application_access_token>_

__

_Response:-_

_true_

_That’s all! Target page is hacked!_

__

Reported this vulnerability to the Facebook security team and it is completely fixed now. They rewarded me $2500 USD as a part of their bug bounty program.Even though they placed a fix for this vulnerability, please be aware of the permissions you grant to any applications.

Permissions dialog box would look like this

[![Manage pages permission dialog box](data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==)](//thezerohack.com/wp-content/uploads/2015/08/Capture.jpg)

If manage_pages is requested please note that this app would be able to manage your pages (post statuses, publish photos etc..).

People need not worry, we can still modify the permissions you have granted to other apps [here](https://www.facebook.com/settings?tab=applications).

### **Facebook reply after few emails**

[![](data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==)](//thezerohack.com/wp-content/uploads/2015/08/Capture1.jpg)

### **Acknowledgement of Fix**

****[![](data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==)](//thezerohack.com/wp-content/uploads/2015/08/Capture3.jpg)

__

Share

[__Facebook](https://www.facebook.com/sharer.php?u=https%3A%2F%2Fthezerohack.com%2Fhacking-facebook-pages "Facebook")[ __Twitter](https://twitter.com/intent/tweet?text=Hacking+Facebook+Pages&url=https%3A%2F%2Fthezerohack.com%2Fhacking-facebook-pages&via=laxmanmuthiyah "Twitter")[ __Pinterest](https://pinterest.com/pin/create/button/?url=https://thezerohack.com/hacking-facebook-pages&media=https://thezerohack.com/wp-content/uploads/2015/08/page-hack-2-2.png&description=Hacking+Facebook+Pages "Pinterest")[ __WhatsApp](https://api.whatsapp.com/send?text=Hacking+Facebook+Pages %0A%0A https://thezerohack.com/hacking-facebook-pages "WhatsApp")

__

[![Laxman Muthiyah](https://secure.gravatar.com/avatar/b86030f152800e9eb32868123706a65f29e57b9c2cf221b504460ae27f64d655?s=96&d=mm&r=g)](https://thezerohack.com/author/laxmanm1 "Laxman Muthiyah")

[Laxman Muthiyah](https://thezerohack.com/author/laxmanm1)

Security researcher • Web developer • Aspiring entrepreneur — fueled by curiosity and exploration.

[__](https://www.facebook.com/laxmanmuthiyah "Facebook")[__](https://www.linkedin.com/in/laxman-muthiyah-2a0a1797/ "Linkedin")[__](https://twitter.com/laxmanmuthiyah "Twitter")

### Related Stories

[ ](https://thezerohack.com/apple-vulnerability-bug-bounty "How I Found A Vulnerability To Hack iCloud Accounts and How Apple Reacted To It")

[Hacks / Security](https://thezerohack.com/bug-bounty-hacks)

### [How I Found A Vulnerability To Hack iCloud Accounts and How Apple Reacted To It](https://thezerohack.com/apple-vulnerability-bug-bounty "How I Found A Vulnerability To Hack iCloud Accounts and How Apple Reacted To It")

[Laxman Muthiyah](https://thezerohack.com/author/laxmanm1) - June 20, 2021

[ ](https://thezerohack.com/how-i-might-have-hacked-any-microsoft-account "How I Might Have Hacked Any Microsoft Account")

[Hacks / Security](https://thezerohack.com/bug-bounty-hacks)

### [How I Might Have Hacked Any Microsoft Account](https://thezerohack.com/how-i-might-have-hacked-any-microsoft-account "How I Might Have Hacked Any Microsoft Account")

[Laxman Muthiyah](https://thezerohack.com/author/laxmanm1) - March 2, 2021

[ ](https://thezerohack.com/hack-instagram-again "How I Hacked Instagram Again")

[Hacks / Security](https://thezerohack.com/bug-bounty-hacks)

### [How I Hacked Instagram Again](https://thezerohack.com/hack-instagram-again "How I Hacked Instagram Again")

[Laxman Muthiyah](https://thezerohack.com/author/laxmanm1) - August 25, 2019

[ ](https://thezerohack.com/hack-any-instagram "How I Could Have Hacked Any Instagram Account")

[Hacks / Security](https://thezerohack.com/bug-bounty-hacks)

### [How I Could Have Hacked Any Instagram Account](https://thezerohack.com/hack-any-instagram "How I Could Have Hacked Any Instagram Account")

[Laxman Muthiyah](https://thezerohack.com/author/laxmanm1) - July 14, 2019

[ ](https://thezerohack.com/hack-instagram "8 Ways To Hack Someone’s Instagram Account and Its Prevention Measures")

[Hacks / Security](https://thezerohack.com/bug-bounty-hacks)

### [8 Ways To Hack Someone’s Instagram Account and Its Prevention Measures](https://thezerohack.com/hack-instagram "8 Ways To Hack Someone’s Instagram Account and Its Prevention Measures")

[Laxman Muthiyah](https://thezerohack.com/author/laxmanm1) - September 15, 2018

[ ](https://thezerohack.com/hack-facebook-password "11 Hacker Ways To Hack Facebook Account Without Password")

[Hacks / Security](https://thezerohack.com/bug-bounty-hacks)

### [11 Hacker Ways To Hack Facebook Account Without Password](https://thezerohack.com/hack-facebook-password "11 Hacker Ways To Hack Facebook Account Without Password")

[Laxman Muthiyah](https://thezerohack.com/author/laxmanm1) - December 19, 2017

#### 23 Comments

  1. ![](https://thezerohack.com/wp-content/uploads/fv-gravatar-cache/mystery96.png) Anonymous August 28, 2015 At 12:39 am

great sir 🙂

Reply

  2. ![](https://thezerohack.com/wp-content/uploads/fv-gravatar-cache/mystery96.png) [Administrator](https://www.blogger.com/profile/15478979207955766681) August 28, 2015 At 6:51 pm

great

Reply

  * ![](https://secure.gravatar.com/avatar/c5893c876c22b05b9aa3c24eb95f2e6012b6bb1cccd243f9038546eb7a0f2581?s=50&d=mm&r=g) [laxmanm1](https://www.blogger.com/profile/17424230469765578368) September 2, 2015 At 10:11 am

🙂

Reply

  3. ![](https://thezerohack.com/wp-content/uploads/fv-gravatar-cache/mystery96.png) [Gets Adsene](https://www.blogger.com/profile/02390542891289587260) August 28, 2015 At 7:03 pm

Can i get full video for hack facebook page

Reply

  4. ![](https://thezerohack.com/wp-content/uploads/fv-gravatar-cache/mystery96.png) [Gets Adsene](https://www.blogger.com/profile/02390542891289587260) August 28, 2015 At 7:13 pm

<http://infoknown.com/testingfb/hacked.php>

can i get Hacked.php file or script 

Reply

  5. ![](https://thezerohack.com/wp-content/uploads/fv-gravatar-cache/mystery96.png) [Admin](https://www.blogger.com/profile/16487432340031634958) September 1, 2015 At 8:15 pm

you deserve more than 2.500 $

Reply

  6. ![](https://secure.gravatar.com/avatar/5085b98cd69cb80ab4df6203bc549b0767307c915563230ad622b79bd3d8b9f8?s=50&d=mm&r=g) [Zuck](https://facebook.com/) September 2, 2015 At 1:32 pm

:p Great job son

Reply

  7. ![](https://thezerohack.com/wp-content/uploads/fv-gravatar-cache/mystery96.png) Anonymous September 3, 2015 At 12:28 pm

The video could be more usefull if you slow down. And perhaps add some text about what you&#39re doing.

Keep up the good work! Enjoy, the bounty 😉

Reply

  8. ![](https://secure.gravatar.com/avatar/afbfcbcf0cdf3821c1846ba87b7d19559b3d798a5f1d0975b86981e51cdc79f5?s=50&d=mm&r=g) [NathanPowellx47](https://www.blogger.com/profile/02428448446965653927) September 8, 2015 At 9:25 pm

Nice one 🙂

Reply

  9. ![](https://secure.gravatar.com/avatar/9361ec880d6300a89f5c9005389ade4e6c0cfb9b3e6c527c298bf0111c9ee3d9?s=50&d=mm&r=g) [hùng nguyễn hoàng minh](https://www.blogger.com/profile/15444817638477617276) September 30, 2015 At 5:25 pm

:)) too great, you are very professional, but I can get acquainted

Reply

  10. ![](https://thezerohack.com/wp-content/uploads/fv-gravatar-cache/mystery96.png) [Farouk Dz1](https://www.blogger.com/profile/15817009264178738545) April 29, 2016 At 8:46 am

Post a vid nigg

Reply

  11. ![](https://secure.gravatar.com/avatar/809dd0099d580c0f1c097ffdb3f9b9d61be6af06ef366eea0ea849501418010f?s=50&d=mm&r=g) [Unknown](https://www.blogger.com/profile/07740711078953035050) July 22, 2016 At 1:32 am

I CANT UNDERSTAND HELP ME

Reply

  12. ![](https://thezerohack.com/wp-content/uploads/fv-gravatar-cache/mystery96.png) Chan Theara November 20, 2016 At 8:42 pm

Can you get me any videos for hack Facebook account?

Reply

  13. ![](https://thezerohack.com/wp-content/uploads/fv-gravatar-cache/mystery96.png) [al](http://al.com/) November 23, 2016 At 4:44 pm

Some pages deserve to be hacked. Great job jackass

Reply

  14. ![](https://thezerohack.com/wp-content/uploads/fv-gravatar-cache/mystery96.png) Xmart boy December 25, 2016 At 12:37 am

Nice one

Reply

  15. ![](https://secure.gravatar.com/avatar/37e9855b4cc6abd2ed96f790c52e7cc5ddb78e26887a4bddbaf17a3131dff0b2?s=50&d=mm&r=g) Samantha Cameron March 1, 2017 At 7:57 pm

Could you help please my business page was hacked a month ago after 3 cases with Facebook certified lawyers letters they don’t seem to be bothered even no I have lost my livelihood and income 

Reply

  16. ![](https://secure.gravatar.com/avatar/0ed1b31d7c45bfd50a1ee8fa8517c362769f708a8dfa6e8c3ea433588b5b58ca?s=50&d=mm&r=g) [Jasminder Oberoi](http://www.lightchasers.in) April 16, 2017 At 4:44 pm

Hi a great and useful information. My FB page has been hacked recently and despite repeat reporting to FB, I am yet to hear from them. Can you help me with the way forward.

Reply

  17. ![](https://secure.gravatar.com/avatar/a0ed681fb3f9e278ac92088dccd10c32cf467643b1ebf8cb765214c880e6a6da?s=50&d=mm&r=g) sydney carleton September 4, 2017 At 9:32 pm

Can someone help me to hack this profile, the bastard has just hacked another account of mine and deleted it altogether. If anyone can help. <https://www.facebook.com/profile.php?id=100004216817397>

Reply

  18. ![](https://thezerohack.com/wp-content/uploads/fv-gravatar-cache/mystery96.png) Subash Ghimire September 9, 2017 At 8:43 am

Fake

Reply

  19. ![](https://secure.gravatar.com/avatar/bdd42916b59ffade7fc4bbfc0ab17e47ebf57352914ea9f4c6e9725edbbb655e?s=50&d=mm&r=g) Stephen Farnsworth March 1, 2018 At 9:02 pm

This is still live, and pretty sure I just got hit with it.

Reply

  20. ![](https://secure.gravatar.com/avatar/87cdf7e6ad287e1124e4232181f8fafd24a269dc56a69797787cef4d5eef03b6?s=50&d=mm&r=g) Lewis Adam April 1, 2018 At 11:18 pm

HELLO

Reply

  21. ![](https://secure.gravatar.com/avatar/3e5aef747c4d74ac0134c46d0dd2c574cc8e20e4b62bd47fb2b868a747900144?s=50&d=mm&r=g) SweetCheeks May 6, 2018 At 3:10 am

“WATCH THIS VIDEO”…..THERE IS NO VIDEO! LOL!

Reply

  22. ![](https://thezerohack.com/wp-content/uploads/fv-gravatar-cache/mystery96.png) Taylor August 8, 2018 At 10:03 am

nice

Reply

### Leave A Reply [Cancel reply](/hacking-facebook-pages#respond)

Comment:

Please enter your comment!

Name:*

Please enter your name here

Email:*

You have entered an incorrect email address!

Please enter your email address here

Website:

Save my name, email, and website in this browser for the next time I comment.

### Stay on top - Get the latest updates in your inbox

Subscribe
