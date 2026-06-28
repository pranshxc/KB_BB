---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-05-28_the-30000-bounty-affair.md
original_filename: 2023-05-28_the-30000-bounty-affair.md
title: The 30000$ Bounty Affair.
category: documents
detected_topics:
- sso
- command-injection
- automation-abuse
- api-security
tags:
- imported
- documents
- sso
- command-injection
- automation-abuse
- api-security
language: en
raw_sha256: 8c5d03f28921ffa6f332222c4c06486e844857c27c0d160ccb6d9849bcf7283b
text_sha256: ad3855f8a54bb817c606c6bb89ce4b84b178da220787319364538419b7e4e4cb
ingested_at: '2026-06-28T07:32:21Z'
sensitivity: unknown
redactions_applied: false
---

# The 30000$ Bounty Affair.

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-05-28_the-30000-bounty-affair.md
- Source Type: markdown
- Detected Topics: sso, command-injection, automation-abuse, api-security
- Ingested At: 2026-06-28T07:32:21Z
- Redactions Applied: False
- Raw SHA256: `8c5d03f28921ffa6f332222c4c06486e844857c27c0d160ccb6d9849bcf7283b`
- Text SHA256: `ad3855f8a54bb817c606c6bb89ce4b84b178da220787319364538419b7e4e4cb`


## Content

---
title: "The 30000$ Bounty Affair."
url: "https://medium.com/@gokulsspace/the-30000-bounty-affair-3f025ee6b834"
authors: ["Gokulsspace (@GokTest)"]
bugs: ["RCE", "Missing authentication", "Exposed Jenkins instance"]
bounty: "30,000"
publication_date: "2023-05-28"
added_date: "2023-05-29"
source: "pentester.land/writeups.json"
original_index: 1109
scraped_via: "browseros"
---

# The 30000$ Bounty Affair.

Top highlight

The 30000$ Bounty Affair.
Gokulsspace
Follow
5 min read
·
May 28, 2023

2K

28

It was one of the hottest day in the hottest district of Kerala, i.e, Palakkad. I was bug hunting all day and the sweat was soaking me all over. I was disturbed and fed up because I couldn’t find anything till noon. In the noon, I was particularly hunting this financial company’s different domains, let’s say redacted.com. This is a two part story!

PART 1:The Secrets on port 8081

As my undefined methodology on bug hunting, if I am having a bad day, I’ll just dig everything on Censys and Shodan! So I did the same thing here also. Just went to Censys and dug every IP addresses of redacted.com.

After digging for some time I saw this interesting IP address which have so many ports are open. 80,443,8081,8080 and so on.

So this IP was fishy particularly on ports 8080 and 8081. I noticed that this IP address is related with MongoExpress and Jenkins from the sidebar of censys. But I was still not sure about whether the IP belongs to redacted.com. So before exploring those ports and everything I went to https://www.sslshopper.com/ssl-checker.html just to check if the IP belongs to redacted.com. Interestingly it belongs to redacted.com and also associated with many other online properties of this particular company.

So I straight up opened the port 8081 first: https://ipaddress:8081

I felt that moment like the rain on a desert. THAT WAS AN EXPOSED MONGOEXPRESS PANEL WITHOUT ANY AUTHENTICATION.

Since I got free access to this panel I was able to do whatever I want including:

Configure existing dbs
Creating new db
Deleting existing db More and more.
Press enter or click to view image in full size

Due to some severe misconfiguration I was able to access following paths too.

http://ip:8081/db/config/

http://ip:8081/db/config/system.sessions
http://ip:8081/db/admin/system.users

http://ip:8081/db/admin/system.version

http://ip:8081/db/local/startup_log

And Most importantly I found the admin credentials from admin db in salt form and an attacker was able to edit it.
Press enter or click to view image in full size

So I reported to the company immediately by explaining everything and rated as CRITICAL. And read part 2 for some real twist:

PART 2: The Gem on port 8080

So as I explained on 1st part, I was checking all the ports on this Majestic IP address. And we have completed the mysteries on port 8081. Some of you may have thought that why I tested 8081 before 8080. Only one reason: 8080 was a 404 error page and thought it will be a dead end:

Press enter or click to view image in full size

So my friends, if you ever come across such a 404 page, DO NOT CLOSE THE TAB AND GO BEHIND ANOTHER INSTANCE. This happened on those days when I started fuzzing for directories irrespective of the status code whether it may be 200,404 or 403. Most of the times the Gems are inside these pages.

Get Gokulsspace’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

So I started fuzzing http:ip:8080/ by using my wordlist insearch of some juicy directories using ffuf. I was not expecting something big, but only one word was 200 OK. And that was /jenkins/script

I suggest all of you to add this path to your fuzzing list.

I immediately opened that path: http://ip:8080/jenkins/script

My heart beat started increasing. Port 8081 was an open door to MongoExpress, But 8080 was something more special. It was an open door to JENKINS. Unauthenticated me entered into this jenkins panel. There were many paths and information were available there, but not gonna talk about that now.

The main thing here is I got open access to this jenkins and more importantly the /script console was open. So the http://ip:8080/jenkins/script will take me into:

Press enter or click to view image in full size

So I remembered seeing random tweets on RCE on jenkins instances on twitter. So I took twitter and searched for it as well as I read previously available jenkins rce reports on HackerOne.

So I understood this is the moment and I acted immediately. All I needed to do was inject some simple commands on this /script console:

Some commands I tried out on this console were:

“ls /”.execute().text
“ps aux”.execute().text
println “whoami”.execute().text

These commands will produce proper outputs from inside. For example if you give the println “whoami”.execute().text on script console the out will be Jenkins.

That’s it. I immediately prepared all the pocs and everything and reported to the team as report no:2. I was hoping that they will accept both as critical. But they took RCE seriously and duplicated MongoExpress exposure since a fix will be effective on both instances. But the bounty was 2X of what I expected and they surprised me with this at the midnight:

Press enter or click to view image in full size

In short:

Use simple censys search like (target.com) and services.software.product=`jenkins`
Or shodan querries like this: Set-Cookie: mongo-express=” “200 OK”
Add /jenkins/script to your wordlist.

Major Takeaways:

Never believe a 404 page.
Censys and Shodan are real friends.

That’s all from me and share this if you found it helpful. I’ll be back with a new write up.

Press enter or click to view image in full size
