---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-06-20_how-did-i-find-information-disclosure-on-facebook-writeup.md
original_filename: 2020-06-20_how-did-i-find-information-disclosure-on-facebook-writeup.md
title: How did i find information Disclosure on Facebook-Writeup
category: blogs
detected_topics:
- command-injection
- information-disclosure
- api-security
tags:
- imported
- blogs
- command-injection
- information-disclosure
- api-security
language: en
raw_sha256: 923984f785e1ba30bd5f9471d3424b13c0bdde43ad1f058bf305233ed2162ba9
text_sha256: f08d4ce53e1e6679ff8ff6f37363a180c68d2c3dfe687c125c48b7343e58da36
ingested_at: '2026-06-28T07:32:02Z'
sensitivity: unknown
redactions_applied: false
---

# How did i find information Disclosure on Facebook-Writeup

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-06-20_how-did-i-find-information-disclosure-on-facebook-writeup.md
- Source Type: markdown
- Detected Topics: command-injection, information-disclosure, api-security
- Ingested At: 2026-06-28T07:32:02Z
- Redactions Applied: False
- Raw SHA256: `923984f785e1ba30bd5f9471d3424b13c0bdde43ad1f058bf305233ed2162ba9`
- Text SHA256: `f08d4ce53e1e6679ff8ff6f37363a180c68d2c3dfe687c125c48b7343e58da36`


## Content

---
title: "How did i find information Disclosure on Facebook-Writeup"
page_title: "How did i find information Disclosure on Facebook-Writeup - Alaa Abdulridha"
url: "https://alaa.blog/2020/06/how-did-i-found-information-disclosure-on-facebook-writeup/"
final_url: "https://alaa.blog/2020/06/how-did-i-found-information-disclosure-on-facebook-writeup/"
authors: ["Alaa Abdulridha (@Madrid89001310)"]
programs: ["Meta / Facebook"]
bugs: ["Information disclosure"]
bounty: "1,500"
publication_date: "2020-06-20"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4482
---

**Hello everyone, This is my first writeup about the bug that I found on Facebook back on 3/1/2018.**

So, I wasn’t interested in Facebook bug bounty program for a while since I was so busy with my highschool exams back in 2018, I just wanted to collect some information about some users, and to know the methods to do that.

However, I started to copy the usernames of some users and to move to the login page, then trying to do forget password and click I have no access to my email.

So I get after that in some users an option to try to recover the account using my trusted friends!

Okay so for example when I try that it sends me to this page :
  
  
  https://www.facebook.com/recover/trusted?cp=5bafbd0f%40mozej.com&ntplr=0

and it asks me to enter the names for 3 trusted friends.

so without sending the request to the burp suite, without thinking too much, I said ntplr=0 hmm?

Let’s try to put **1** so it will be **ntplr=1** 😀

guess what? yeah, it worked I can see the trusted friends now for an account in the Facebook, even if the account doesn’t use the trusted friends feature I’m able to see the most 5 friends the user talk to them using the messenger.

so I was like :

![](https://alaa.blog/wp-content/uploads/2020/06/freaking.gif)

![fbug](https://alaa.blog/wp-content/uploads/2020/06/fbBug-2018.png)

So as you can see in this screenshot, the **GET** parameter **[ntplr]** was vulnerable!, if you set it to 1 it will disclosure the target information for you, and I was able to write an exploit tool using python to retrieve any user trusted friends for me just by entering the user id, and it’s doing that just by replacing the user id in the session.

> **I have rewarded a bounty of 1500$ and my name in the Facebook hall of fame for 2018.**

So, my advice to you here, don’t give up, don’t listen to anyone that could frustrate your spirits, Always focus the smallest things here might matter for you .. I found this bug in 15 minutes only, you might say, whoa what the hick, how lucky this guy is! well guess what even if you’re lucky the vulnerability will not popup by itself to you while you’re playing or not trying, you’ll find it while you’re trying so here it’s not luck .. It’s just you trying your best.

so as I always say:

> surmount the peak

Thanks for reading 😀 .. if you have any question do not hesitate to ask me on Facebook

**With kind Regards.**

[![Alaa Abdulridha on Email](https://alaa.blog/wp-content/plugins/sexy-author-bio/public/assets/images/flat-circle/sabemail.png)](/cdn-cgi/l/email-protection#11707d70706270736378627951767c70787d3f727e7c)[![Alaa Abdulridha on Facebook](https://alaa.blog/wp-content/plugins/sexy-author-bio/public/assets/images/flat-circle/sabfacebook.png)](https://www.facebook.com/alaa0x2/)[![Alaa Abdulridha on Github](https://alaa.blog/wp-content/plugins/sexy-author-bio/public/assets/images/flat-circle/sabgithub.png)](https://github.com/Alaa-abdulridha)[![Alaa Abdulridha on Instagram](https://alaa.blog/wp-content/plugins/sexy-author-bio/public/assets/images/flat-circle/sabinstagram.png)](https://www.instagram.com/al_shwele)[![Alaa Abdulridha on Linkedin](https://alaa.blog/wp-content/plugins/sexy-author-bio/public/assets/images/flat-circle/sablinkedin.png)](https://www.linkedin.com/in/alaa0x2/)[![Alaa Abdulridha on Twitter](https://alaa.blog/wp-content/plugins/sexy-author-bio/public/assets/images/flat-circle/sabtwitter.png)](https://twitter.com/alaa0x2)

[Alaa Abdulridha](https://alaa.blog/author/alaaabdulridha/ "Alaa Abdulridha")

[![Alaa Abdulridha](https://alaa.blog/wp-content/uploads/2021/03/129218847_415123992955253_8935169515856501689_o-150x150.jpg)](https://alaa.blog/author/alaaabdulridha/)

My name is Alaa Abdulridha I'm Engineering Director at SerpApi, LLC and cybersecurity researcher I'm interested in web application pen-testing and game development, also I'm interested in some bug bounty programs, I like a lot of things such as reverse engineering, reading the others code to learn and then to find my own exploits and teaching it to you, Do you want to know more about me? [Click Here](https://alaa.blog/whoami/).
