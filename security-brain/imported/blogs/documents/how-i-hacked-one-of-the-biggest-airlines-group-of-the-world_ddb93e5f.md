---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-04-05_how-i-hacked-one-of-the-biggest-airlines-group-of-the-world.md
original_filename: 2022-04-05_how-i-hacked-one-of-the-biggest-airlines-group-of-the-world.md
title: How I hacked one of the biggest airlines group of the world
category: documents
detected_topics:
- idor
- command-injection
- otp
- api-security
- cloud-security
tags:
- imported
- documents
- idor
- command-injection
- otp
- api-security
- cloud-security
language: en
raw_sha256: ddb93e5f48250b49aaf50b9ddf2a391e6e1218e78f56054a528a598d8b3013b2
text_sha256: 48eb628d721987752baab4e86fa43227f8af03fb091a28fee03b960d97a245ff
ingested_at: '2026-06-28T07:32:11Z'
sensitivity: unknown
redactions_applied: false
---

# How I hacked one of the biggest airlines group of the world

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-04-05_how-i-hacked-one-of-the-biggest-airlines-group-of-the-world.md
- Source Type: markdown
- Detected Topics: idor, command-injection, otp, api-security, cloud-security
- Ingested At: 2026-06-28T07:32:11Z
- Redactions Applied: False
- Raw SHA256: `ddb93e5f48250b49aaf50b9ddf2a391e6e1218e78f56054a528a598d8b3013b2`
- Text SHA256: `48eb628d721987752baab4e86fa43227f8af03fb091a28fee03b960d97a245ff`


## Content

---
title: "How I hacked one of the biggest airlines group of the world"
page_title: "How I hacked one of the biggest airlines group in the world :: Tarek Bouali - Ethical Hacker"
url: "https://tarekbouali.com/posts/how-i-hacked-one-of-the-biggest-airlines-group-of-the-world/"
final_url: "https://tarekbouali.com/posts/how-i-hacked-one-of-the-biggest-airlines-group-of-the-world/"
authors: ["Tarek Bouali (@iambouali)"]
bugs: ["IDOR", "Account takeover"]
publication_date: "2022-04-05"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 2746
---

# [How I hacked one of the biggest airlines group in the world](https://tarekbouali.com/posts/how-i-hacked-one-of-the-biggest-airlines-group-of-the-world/)

![](https://tarekbouali.com/images/gScgE34d.jpg)

About a year ago, when I started my first forays into **HackerOne** , I discovered one of the most impactful bugs I’ve ever come across. It was January 2021, when I received a private invitation to a **VDP (Vulnerability Disclosure Program)** , it was from an airlines group. So I decided to try hacking in that program, because at that time I didn’t give much priority to bounties, due to I wanted to learn and earn my first points on the platform.

After a few minutes investigating the scope of the page, I realized that they were using a unified login system for most of the companies that were in the scope, mostly airline websites, among others. I decided to analyze the “**Forgot your password?** ” endpoint, first. So I entered my email and waited for the email where I would receive the link to change the password.

At the moment I received a link with the following format:

`https://████████/password/?key=████████`

After that, I went to the change password link, typed the new password twice, and captured the request.

The request to change the password had this format:

I quickly realized that there was a numeric value (user ID) in the path, possibly autoincrementing, that could be susceptible to being used in a potential **IDOR (Insecure direct object reference)**. And I wasn’t on the wrong track.

So, I decided to do a simple test, wich consisted in opening the following endpoint in the browser:

`https://████████/api/members/314159/profile`

To my surprise, my email was displayed in plain text. So I decided to iterate the numerical value and … wow! I was able to list thousands of emails without any type of authentication.

Listing emails with Burp Suite:

![](https://tarekbouali.com/images/NKzR9jL.png)

I wrote the report and just sent it quickly. The report was triaged as high impact vulnerability.

I moved forward to the **API** , trying to access more sensitive data. I had a gut feeling that I was close to finding something much more interesting.

Then I decided to try changing the password to another user by modifying their in ID request path. It didn’t seem like a bad idea, right? So I created a new user account, to use its ID and see if I could find an IDOR with more impact. Well, with two accounts it is easier.

So I tried with:

I received in response:

I kept trying options:

`{"credentials":{"token":"MyNewPassword"}, "resetToken":{"token":""}}`

Same error.

After several unsuccessful tests, I decided to fully removing `resetToken`:

Then, I got a wonderful:

`HTTP/1.1 204`

I can say now, that moment felt so good inside that was without doubt one of the most amazing experience I ever had. After that, I decided to check it out if I had really changed the password to my auxiliary account and… yes! It was absolutly changed! I had a full account takeover in front of my eyes wich could be exploited on a large scale! 🚀

![](https://c.tenor.com/Qjzn2f-rtdoAAAAC/thats-awesome.gif)

After that I prepared the report, I sent it and asked very innocently if the report was suitable for a bounty due to its criticality. Being my first steps in HackerOne I still didn’t know quite well which programs would pay and which wouldn’t. This case was a VDP, so didn’t.

But, after the triage analyzed it and assigned the impact, the airlines group team decided to move the report to another private program they had, a Bug Bounty program. They assigned for it a **CVSS of 10.0** , so I was paid the maximum possible bounty according to their table.

![](https://tarekbouali.com/images/OK9TdkD.png)

Amazingly, I was able to change the password of all or any user in the airline group. On all their different pages, was possible to save credit cards and other sensitive information. **Therefore, a potential attacker had access to such sensitive information, such as credit cards, of thousands or millions of users!**

This was one of my first bounties on HackerOne and one of the most impactful bugs I’ve found so far. For this very reason, I decided to publish it, even though I can’t say the name of the company.

Happy hacking, everyone!
