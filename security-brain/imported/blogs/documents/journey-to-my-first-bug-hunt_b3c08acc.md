---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-08-13_journey-to-my-first-bug-hunt_2.md
original_filename: 2020-08-13_journey-to-my-first-bug-hunt_2.md
title: Journey to my First Bug Hunt$$$$
category: documents
detected_topics:
- xss
- command-injection
- otp
- csrf
- business-logic
- api-security
tags:
- imported
- documents
- xss
- command-injection
- otp
- csrf
- business-logic
- api-security
language: en
raw_sha256: b3c08accc05a2e90797597ca5b5b1045f0946f6b19b8e87a04f0d77b8a40e2a3
text_sha256: 2c9506d4262eab9851eb45eb5e3604d697aaf52961cb4eeb5f30bd74c6fff732
ingested_at: '2026-06-28T07:32:03Z'
sensitivity: unknown
redactions_applied: false
---

# Journey to my First Bug Hunt$$$$

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-08-13_journey-to-my-first-bug-hunt_2.md
- Source Type: markdown
- Detected Topics: xss, command-injection, otp, csrf, business-logic, api-security
- Ingested At: 2026-06-28T07:32:03Z
- Redactions Applied: False
- Raw SHA256: `b3c08accc05a2e90797597ca5b5b1045f0946f6b19b8e87a04f0d77b8a40e2a3`
- Text SHA256: `2c9506d4262eab9851eb45eb5e3604d697aaf52961cb4eeb5f30bd74c6fff732`


## Content

---
title: "Journey to my First Bug Hunt$$$$"
url: "https://medium.com/@balapraneeth98/journey-to-my-first-bug-hunt-6dc5e4552128"
authors: ["Bala Praneeth (@Begin_hunt)"]
bugs: ["CSRF"]
bounty: "900"
publication_date: "2020-08-13"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4327
scraped_via: "browseros"
---

# Journey to my First Bug Hunt$$$$

Journey to my First Bug Hunt$$$$
Bala Praneeth (Begin_hunt)
Follow
5 min read
·
Aug 13, 2020

206

2

Hey, folks hope you all are doing good.

Okay. Everyone wants to get their first bug and receive that amazing bounty and feel confident that you can hack. So here it is finally. I always wanted to write such an article and share it with the community. The journey of my first bug hunt.

Having a CS background I started learning information security in June 2020 and was super excited to get hands-on learning in security. But I was so stuck, confused and didn’t know where to start. So, as everyone does I asked “Google” How to get started in cyber-security. The number of answers I received was so vast and different from each other. After reading a ton of blogs about security still wasn’t sure what to do. Then the well-known portal LinkedIn comes to rescue. I did a simple search on security and tons of people popped up. I reached out and started to Network with random people on this platform. The community was so kind and helped me to get an idea of what security is like. The output from these professionals was either go for eJPT or OSCP. I researched about OSCP and was like

What the heck is it

The reviews of OSCP stated by the professionals were challenging. Therefore I decided to take up this journey of pursuing pen-testing. The downside is the fees for this exam

I started to read a few blogs of OSCP on medium and one of them stated in their blog about paying their OSCP fees through bug bounty. After listening to this I was amazed as the fees of OSCP is approx(1000$). Now my interest begins in bug bounty just for the obvious reasons that I can earn money and pay my fees.

Now at this point, I started to watch Katie’s(InsiderPhd) videos to get my first bug as here title was quite clear and the content is simply amazing. I came across business logic errors as she mentioned in her videos, was amazed by these tips and just by changing certain values of parameters, there is a possibility of a bug. Was super excited after looking at this and started to hunt. Went directly to the Paytm website started to change a few parameters and found nothing. But I found a price parameter which can be changed by Intercepting it by burp(total noob here).

The story
So selected a 500Rs recharge and intercepted it with a burp and changed the value to 10rs and forwarded it. To my surprise, the request went through and thought that I found a bug. Started to jump around, woke my parents(at 11 pm), and informed them. But I made a total fool of myself. The payment happened for 10rs as there is a package available. At this point, I felt disgusted and stupid.

The feeling of Regret

Okay back to the journey. Around the first month of July, I watched a video by Stok Fredrik which was on “How to get started in bug bounty”. An amazing vid. I noted down every point in his video and started to analyze it.

Get Bala Praneeth (Begin_hunt)’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

The take here is simple
1. Pick a bug
2. Learn about it
3. Hunt for it
This methodology changed my perspective from that day on. So, I started with XSS as my first bug and learned for 15 days and went hunting for it. But no luck.

I want to emphasize certain aspects here.
1. Take good care of yourself
2. Don’t be in a hurry to get a bug. You will eventually
3. Take some time off and relax
4. Don’t be stressed and lose motivation
5. Accept the change and focus on learning the concepts

After about a few days I realized that I have reached a saturation point and had to move on to learn another bug. Then CSRF came to my rescue (picked it randomly). Spent about another 30 days to learn about the bug and approaches to attack it.

Here are some best resource I found through my way
1. Port-swiggers content and labs
2. Medium Articles on CSRF
3. Hacktivity from HackerOne to understand the flow and approach to attack.

Hunting for Bugs

Later once I was comfortable I moved on to bug crowd for hunting. Honestly was scared that I might not get a bug as other researchers would have already submitted them. Tore my fear apart and started to hunt.

The way I found CSRF
1. Registered in Bugcrowd
2. Chose the program which is somewhere in the end. I thought that the researchers would jump in straight for the new programs.
3. Picked a target and enumerated it
4. I noticed that the site wasn’t using any special methods to transmit data(gave a hint. Unfortunately cannot disclose it).
5. Therefore crafted an HTML document with embedded links.
6. Made the victim click on it and at this point, a CSRF new token was leaked.
7. Got hold of the token and crafted the payload again, sent it to the victim, and boom. An application-wide CSRF was possible here and successfully exploited.
8. Reported it to the company and got paid 900$.

Press enter or click to view image in full size

The key take here is understanding the concepts that will help us to know where to attack which indeed helps us to get a bounty. The month research on learning CSRF was worth the time for me as it paid off.

Collaboration and networking is something that I always enjoy. Let’s connect

Twitter — https://twitter.com/Begin_hunt

Linkedin — https://www.linkedin.com/in/balapraneeth/

Happy hacking !!!
If you have reached this far, thank you for reading this article. Kindly feel free to point out any mistakes and do let me know where I can improve in writing and explaining in detail. Appreciate it!!. All the best. God bless
