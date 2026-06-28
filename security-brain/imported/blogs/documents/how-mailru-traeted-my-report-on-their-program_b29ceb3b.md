---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-09-03_how-mailru-traeted-my-report-on-their-program.md
original_filename: 2021-09-03_how-mailru-traeted-my-report-on-their-program.md
title: How @Mailru traeted my report on their program
category: documents
detected_topics:
- cloud-security
- command-injection
tags:
- imported
- documents
- cloud-security
- command-injection
language: en
raw_sha256: b29ceb3b83671e5c3bc6456504b1f9186a8d5ced774cb9374e5bcd326cfcd57b
text_sha256: 22ba7c2cf817ef039c8477d659c0032dc97fbff2efcdc2cd29731d9f0c6326c2
ingested_at: '2026-06-28T07:32:07Z'
sensitivity: unknown
redactions_applied: false
---

# How @Mailru traeted my report on their program

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-09-03_how-mailru-traeted-my-report-on-their-program.md
- Source Type: markdown
- Detected Topics: cloud-security, command-injection
- Ingested At: 2026-06-28T07:32:07Z
- Redactions Applied: False
- Raw SHA256: `b29ceb3b83671e5c3bc6456504b1f9186a8d5ced774cb9374e5bcd326cfcd57b`
- Text SHA256: `22ba7c2cf817ef039c8477d659c0032dc97fbff2efcdc2cd29731d9f0c6326c2`


## Content

---
title: "How @Mailru traeted my report on their program"
url: "https://aob-89072.medium.com/how-mailru-handled-with-my-report-on-their-program-5e1f587ecaa"
authors: ["Aý Oùb (@Yukusawa18)"]
programs: ["Mail.ru"]
bugs: ["AWS misconfiguration"]
bounty: "150"
publication_date: "2021-09-03"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3349
scraped_via: "browseros"
---

# How @Mailru traeted my report on their program

Aý Oùb
Follow
5 min read
·
Sep 3, 2021

32

2

How @Mailru traeted my report on their program

Hi My name is Ayoub, my Hackerone’s handle @yukusawa18. before I started I had a very nice experience with all other triagers on Mailru, but this time I had bad one.

on this story I’ll describe everything step-by-step about my report on Mailru’s Program and of course I’ll not share any sensitive informations.

I was looking on *.corp.mail.ru subdomains and I found one of their subdomain return with a 500 Internal server ERROR, and leaking a lot of informations because the debug mode was enabled.
January 21, 2021 I submitted a bug to MailRu #1083543 about debug mode was enabled on legium-back.corp.mail.ru
Press enter or click to view image in full size
the 1st bug submitted to Mailru

3. The report was about an S3 bucket That contains a lot of images, exactly PASSEPORTS; and the NAME of this bucket is : AWS_STORAGE_BUCKET_NAME = ‘legium-media’

please note that the S3 bucket contains legium on its name.

4. Feb 2nd, 2021 I was rewareded by 7.5k, informations disclosure.

5. Apr 20th, 2021 the bug is fixed and the S3 credentials are changed very well and I can’t access to the bucket anymore.

After two Months, I decided to re-check the response and the informations founded on the legium-back.corp.mail.ru subdomain.

and by accidently I found that there’s also database credentials :

Press enter or click to view image in full size
the database credentials found on https://legium-back.corp.mail.ru
the 1st problem I got, where I can find the ip to connect to this database, I looked too much until I found it by reading all js files on : https://legium-back.corp.mail.ru
I found a subdomain on a js file : https://legium-back.corp.mail.ru/static/api.js
Press enter or click to view image in full size
as you see on this response there’s api2.legium.io

4. api2.legium.io doesn’t work, so by accidently delete the number 2, and visit api.legium.io, it worked very well

5. the next move is try to see if the api.legium.io has a 5432 port or not. and to my surprise I found that the port is open.

6. I accessed to the database using psql tool, https://www.postgresql.org/docs/13/app-psql.html

B
EFORE THE TRIAGE :

I reported the bug June 23, 2021 3:59am.
after hours of my report the team deleted the two subdomains : https://legium.corp.mail.ru and https://legium-back.corp.mail.ru as you can see on the screenshot I visited them 1 hour or 2 hour before I reported the bug.
Press enter or click to view image in full size
the legium.corp.mail.ru is still accessible.

3. also I can ACCESS to the admin panel too, but they hide it before the triage so I cannot add an account and access to the admin panel

Press enter or click to view image in full size
here I told them that they changed the hide the admin panel.
Press enter or click to view image in full size
here I can access to the admin panel a few hours before reporting the bug.

A
FTER THE TRIAGE :

the bug triaged on : june 24, 2021 09:32:30 +01
Press enter or click to view image in full size
Kpebetka changed the status to triaged

2. Almost every hacker hacked on @Mailru team knows that 99% of reports if they have a wrong scope, the triager changed it before the triage.

Get Aý Oùb’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

3. after 8 or 9 days, a new triager come and change the scope from EXT.A where *.corp.mail.ru to :

Press enter or click to view image in full size
here the triager changed the scope to “acquisitions”

4. after that I asked why the scope is changed, I found informations on *.corp.mail.ru

Press enter or click to view image in full size

5. the team wanted to punish me more and changed the scope again, Oh for god seek, they don’t know what the scope is until now, after 14 days.

Press enter or click to view image in full size

6. MailRu decided that My report isn’t eligible for bounty because the ip was only for testing haha :

Press enter or click to view image in full size
the IP is used only for testing

7.I found 325 MB of data on the database exactly on table “case_case” containing a lot of agreements, (testing IP).

8. I added some comments to complain about this decision :

Press enter or click to view image in full size
these are all impacts

9.and a few days later I got this :

Press enter or click to view image in full size
they rewarded me with 150$

10. I also started complaining about this and told them that I accessed informations related to famous persons on russia but his answer was like :

Press enter or click to view image in full size
still telling that it’s only a test db. I give him evidences that isn’t a test db.

11. telling me that MailRu and Legium has no relation :

Press enter or click to view image in full size
read the title of https://legium.corp.mail.ru

and here it’s the translation :

Press enter or click to view image in full size

1.if there’s no relations about MailRu and Legium Why I got payed for S3 bucket “legium-data” that not belongs to Mailru.

2. and Why there was https://legium.corp.mail.ru and https://legium-back.corp.mail.ru

3. and why there’s https://skillbox.legium.io that’s belongs to Mailru.

4.and If you are not parnters why you fixed the bugs, and Adding 403 to the admin panel before the triage.

5.let’s say that the ip isn’t belong to MailRu, Why I found it on https://legium-back.corp.mail.ru

What the you think Guys, Am I wrong or the team ?
