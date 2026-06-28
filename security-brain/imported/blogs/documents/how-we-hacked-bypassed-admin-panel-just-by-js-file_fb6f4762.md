---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-05-06_how-we-hacked-bypassed-admin-panel-just-by-js-file.md
original_filename: 2022-05-06_how-we-hacked-bypassed-admin-panel-just-by-js-file.md
title: How We hacked (bypassed) Admin Panel just by JS file
category: documents
detected_topics:
- command-injection
- otp
- rate-limit
- information-disclosure
- cloud-security
- mobile-security
tags:
- imported
- documents
- command-injection
- otp
- rate-limit
- information-disclosure
- cloud-security
- mobile-security
language: en
raw_sha256: fb6f476267ca4549a552e6240cae1289d3bd70415e7ab81c04ac59696d58cfd8
text_sha256: cbec91f2cd0ad4a6c6963ec448231e8db92b5de91cd4e1f0f686be1f8fd57a0d
ingested_at: '2026-06-28T07:32:11Z'
sensitivity: unknown
redactions_applied: true
---

# How We hacked (bypassed) Admin Panel just by JS file

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-05-06_how-we-hacked-bypassed-admin-panel-just-by-js-file.md
- Source Type: markdown
- Detected Topics: command-injection, otp, rate-limit, information-disclosure, cloud-security, mobile-security
- Ingested At: 2026-06-28T07:32:11Z
- Redactions Applied: True
- Raw SHA256: `fb6f476267ca4549a552e6240cae1289d3bd70415e7ab81c04ac59696d58cfd8`
- Text SHA256: `cbec91f2cd0ad4a6c6963ec448231e8db92b5de91cd4e1f0f686be1f8fd57a0d`


## Content

---
title: "How We hacked (bypassed) Admin Panel just by JS file"
url: "https://medium.com/@z.x/how-we-hacked-bypassed-admin-panel-just-by-js-file-eaa773b5cdb4"
authors: ["Zhenwar Hawlery (@zhenwarx)", "moSec (@moe1n1)"]
bugs: ["Information disclosure"]
publication_date: "2022-05-06"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 2660
scraped_via: "browseros"
---

# How We hacked (bypassed) Admin Panel just by JS file

How We hacked (bypassed) Admin Panel just by JS file
Zhenwarx
Follow
4 min read
·
May 6, 2022

613

7

Press enter or click to view image in full size

Hello world!

I hope you are doing well.

Before starting the topic, I would like to introduce myself and my friend (@moSec), We are Whitehat hackers and Bug Bounty Hunters from Kurdistan who enjoying finding security flaws in web applications and mobile applications.

F
irst, I prefer to tell you about the website because that was an wanted project scan by a Kurdish Company. As they create professional websites for bossiness/people/companies/government.

Let me tell you the challenge here! because it was not just a normal Admin Panel bypass for us. The company manager called us to meet him because he already know us as a professional team in the hacking websites field. We were in trip and enjoying, after 4 days we came back to home and met the company manager as he liked, he asked us to scan one of their projects but as I remember he said that it’s a professional website that created by expert team, and it’s somehow impossible to find even a single bug (they thought that the program language they are using is very secured) but that was not something important for we just wanted the project to test (LOL).

Let’s short the words and start the topic and see where was that bug 🐞

So the team gave as a mobile application that was created by Flutter and a website domain, at the time we worked on the project (21 Dec 2021) it was so hard to capture requests of the APPs that were created by Flutter. So we didn’t waste of time on the mobile app and decided to work on the website as it was the back-end of the mobile APP.

Normally, we just tried to find the Admin Panel because the main domain was just a single page to download the Application.

After brute forcing the subdomains we found that the website had a subdomain like that [(admin.project.com) — We use project.com as the domain name of the project in this write-up]. As always we first visited the subdomain that seemed to be sensitive.

Press enter or click to view image in full size
Finding subdomains by Amass Tool

And when we visited the subdomain we just got that Login Portal

Log in Portal

The first input field was a mobile number (so the admin can log in by his phone number) and the second field was Password. The portal was very good as it was seem but that was all?

1- Couldn’t brute force the password (301 Too Many request).

2- Directory fuzzing not result.

3- There wasn’t any sign up form to try some bypass ways.

4- The website was new so there was not any related URLs/info about it.

So what we can do now?

Get Zhenwarx’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Of course and as always! taking a look at the source code is a nice part of finding bugs! and when we took a look at the page there was just one line of the codes that was deserve to focus on and that was a Javascript ( 💙) file.

Press enter or click to view image in full size
The source code of the Login Portal

That was the beginning as well as hard and also the most enjoyable part of the security flaws because you should read the JS file line by line to understand the codes and know how the website working, it’s too much hard but still very enjoyable! :)

After opening the JS file, First we took a look at it normally just be searching for sensitive words such as (admin, config, password, token, email, .conf) and happily when we tried token we found this juicy piece of code:

Press enter or click to view image in full size
a piece of code in the source code

([“TOKEN”,”hxcdjskhck643782bcdshcdsjk231cbdns”,”fullname”,a,”phone”,b,”city”,c,”superadmin”,d,”permisions”,e,”password”,f],t.N,p))
s=3
return A.U(A.ck(null).cc(“https://project.app/RedactedAppBackend/dashboard/addAdmin.php",c,n),$async$uH)

Everyone knows that this is a POST request and also we have body parameters which are :

TOKEN=***REDACTED-SUSPECT-TOKEN***fullname
phone
superadmin
permissions
password

but what we can do with that? first we should knew that what will happening if we send a request for this POST data? after thinking of the end URL part which is addAdmin.php we knew that it will create another admin account:

RedactedAppBackend/dashboard/addAdmin.php

So we just sent a POST request to the data that we got from the JS file

Press enter or click to view image in full size
The Post Request

As you can see the Response is OKK so it meant we successfully created another admin account, and when we tried the phone number and the password that was the result:

Press enter or click to view image in full size
Admin Panel bypassed

We had full control of the Panel and successfully hacked it and got $$$ reward for it.

What is important for bug hunters:

1- Focus on the JS files.

2- Always start as you are the first person who found the page/endpoint.

3- Nothing is impossible.

What is important for developers:

Don’t put sensitive data in the client-side source codes such as Token!.
