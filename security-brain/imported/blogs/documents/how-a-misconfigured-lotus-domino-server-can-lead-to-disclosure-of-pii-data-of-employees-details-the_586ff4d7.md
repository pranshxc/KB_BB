---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-06-04_how-a-misconfigured-lotus-domino-server-can-lead-to-disclosure-of-pii-data-of-em.md
original_filename: 2023-06-04_how-a-misconfigured-lotus-domino-server-can-lead-to-disclosure-of-pii-data-of-em.md
title: How a misconfigured Lotus Domino Server can lead to Disclosure of PII Data
  of Employees, Configuration Details about the Active Directory, etc
category: documents
detected_topics:
- access-control
- automation-abuse
- idor
- command-injection
- rate-limit
- graphql
tags:
- imported
- documents
- access-control
- automation-abuse
- idor
- command-injection
- rate-limit
- graphql
language: en
raw_sha256: 586ff4d788ae7704b64b3300ad142d90f80c436ef9a4ea0e631a7afc4248e59e
text_sha256: 7f8e3d97bc96e48700c7236fac963ea3a8ee88257415b3cbbf557155e9506804
ingested_at: '2026-06-28T07:32:21Z'
sensitivity: unknown
redactions_applied: false
---

# How a misconfigured Lotus Domino Server can lead to Disclosure of PII Data of Employees, Configuration Details about the Active Directory, etc

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-06-04_how-a-misconfigured-lotus-domino-server-can-lead-to-disclosure-of-pii-data-of-em.md
- Source Type: markdown
- Detected Topics: access-control, automation-abuse, idor, command-injection, rate-limit, graphql
- Ingested At: 2026-06-28T07:32:21Z
- Redactions Applied: False
- Raw SHA256: `586ff4d788ae7704b64b3300ad142d90f80c436ef9a4ea0e631a7afc4248e59e`
- Text SHA256: `7f8e3d97bc96e48700c7236fac963ea3a8ee88257415b3cbbf557155e9506804`


## Content

---
title: "How a misconfigured Lotus Domino Server can lead to Disclosure of PII Data of Employees, Configuration Details about the Active Directory, etc"
url: "https://medium.com/@ar_hawk/how-a-misconfigured-lotus-domino-server-can-lead-to-disclosure-of-pii-data-of-employees-badad691dad"
authors: ["Aayush Vishnoi (@AayushVishnoi10)"]
bugs: ["Lotus Domino", "Security misconfiguration", "Information disclosure"]
publication_date: "2023-06-04"
added_date: "2023-06-05"
source: "pentester.land/writeups.json"
original_index: 1089
scraped_via: "browseros"
---

# How a misconfigured Lotus Domino Server can lead to Disclosure of PII Data of Employees, Configuration Details about the Active Directory, etc

How a misconfigured Lotus Domino Server can lead to Disclosure of PII Data of Employees, Configuration Details about the Active Directory, etc
Aayush Vishnoi
Follow
7 min read
·
Jun 3, 2023

167

2

Another misconfiguration found last week, because this has more content I thought of releasing last blog before this one so that I will get some more time to better relate the things and make it more digestible for you guys. I hope you will enjoy this one too…😃

Let’ Start
TL;DR

While working on a target, I found a web server running on Lotus Domino Server exposing the Web Server Configuration page allowing to modify the Database and Configuration of the forms. Furthermore, I was able to access other sensitive endpoints of Lotus Domino Server that leads to exposure of Active Directory Details, PII Data of Employees, ACLs, etc. The exposure of data allowing an attacker to understand the configuration of AD, ACLs, etc that can be used to attack the organization infrastructure in future.

[1] Let’s start with Reconnaissance — Understanding the target
Let’s take our target as redacted.com .
I always start with understanding the web application like what technology stack is being used, what are functions/features available such as Login, Sign-Up, Edit User profile, Upload profile picture, Comment, etc. This is the manual step I perform while below scanning/ enumeration is being performed by my recon script at the backend. Let’s take a deep dive into what my recon script will give after hitting so many APIs and endpoints.
The first phase of the script performs subdomain enumeration using multiple tools such subfinder, amass, findomain, assetfinder, puredns, alterx, etc. The script will perform both passive and active subdomain enumeration.
echo ("------Subdomain Enumeration Started-------")

# Passive Enumeration
$ subfinder -d redacted.com -o subfinder.txt
$ amass enum -d --passive redacted.com -o amass.txt
$ echo redacted.com | assetfinder --subs-only | tee assetfinder.txt
$ cat subfinder.txt amass.txt assetfinder.txt | sort -u | anew Psubdomains.txt

# Active Enumeration
$ puredns bruteforce subdomains-wordlist.txt redacted.com -r resolvers-wordlist.txt -w puredns.txt
$ cat subdomains.txt | alterx | anew alterx.txt

$ cat alterx.txt puredns.txt | sort -u | anew Asubdomains.txt

# Sorting and Collecting active and passive subdomains
$ cat Asubdomains.txt Psubdomains.txt | sort -u | anew subdomains.txt
From the above subdomain enumeration, I will have a file called subdomains.txt have all the subdomains. The second phase will start after subdomain enumeration which will sort the subdomains into alive and dead using httpx or httprobe.
# Checking Alive Subdomains
$ cat subdomains.txt | httpx -mc 200 | anew alive-subdomains.txt

# Checking subdomains with httprobe
$ cat subdomains.txt | httprobe | anew webs.txt
Now I have the subdomains having status code=200 and running on either http/https in alive-subdomains.txt and webs.txt files respectively. The third phase will then check for the titles, tech stack, etc used in each of the subdomains using httpx.
# Enumerating the Status Code, Technology Stack and Title of each subdomain
$ cat subdomains.txt | httpx -sc -title -td | anew httpx.txt
From the above file httpx.txt I will get the status code of each subdomains including 200 as well, I have to perform this step because subdomains with status code 302, 403 are also interesting subdomains that I always check. The script will have more phases such as port scanning, nuclei scans, directory fuzzing, content discovery, etc.
The starting point for this misconfiguration I got from third phase, I found a subdomain say https://notes.redacted.com with status code 302 and technology stack HCL Domino, HSTS, and Java.
httpx output

Why this subdomain caught my eye because I was reading about Lotus Domino Server and its misconfiguration 2–3 weeks back, so I wanted to try some exploitations and misconfigurations I have learned.

The script was performing all its operations in parallel I have started manually analyzing the subdomain. Let’s start with the subdomain analysis.

Lotus Domino can be used as a Web server and/or as an application server for the Lotus Notes application, the client side of a client-server collaborative application. Domino provides email, calendars, instant messaging (with additional HCL software voice- and video-conferencing and web-collaboration), discussions/forums, blogs, and an inbuilt personnel/user directory.

[2] Subdomain Analysis — Hacking the Subdomain
The subdomain https://notes.redacted.com was only hosting the default page of HCL Domino Server containing the links to Documentation and support page. This looks like a dead end for now.
Press enter or click to view image in full size
HCL Domino Default Page hosted on Subdomain
But as I said in previous blogs as well FUZZING is very important but you have to chose your wordlist wisely so that without hitting random endpoints on the target you get your results quickly and easily. (Choose wordlists based on the technology stack or CMS used in the web application.)
Press enter or click to view image in full size
FFUF Output
[2.1] Playing with Lotus Domino Endpoints — FUZZING THE WEB
Now, I have lotus domino server in front of me so its obvious I have to use the wordlists containing sensitive endpoints related to Lotus Domino Server. I found multiple interesting endpoints that are exposing huge amount of PII Data about the employees, server configurations, AD configurations, etc. Let’s see what each of these endpoints exposing the information:
Endpoint — /domcfg.nsf. This endpoint if accessible publicly then exposes the Web Server Configuration page. In this scenario, I have found that I can modify the Login Forms data and also change the Database.
Press enter or click to view image in full size
Web Server Configuration Page
Endpoint — /names.nsf. This endpoint if accessible publicly then exposes all the employees names available in the Active Directory basically the instance of Lotus Domino Server I am exploiting its using it for LDAP services as well so from there I was able to find out 😵 all the employees information such as email address, password used to access AD, host-name, ACLs(Access Control lists), permissions, computer name in AD, machine details, etc. The endpoint also contains all the Domain and Server Configuration files which can be used to modify the configuration of any user/employee or other things as well.
Press enter or click to view image in full size
Information about each employee exposed
Endpoint — /admin4.nsf. This endpoint if accessible publicly then exposes all the requests made by employees to ADMIN whether to grant some access, change a file, etc. So from this endpoint, I was able to dig all the requests available for Admin user and also have permissions to either accept or reject the request also can modify the details mentioned, it means without authentication/authorization I have administrative privileges.
Press enter or click to view image in full size
Press enter or click to view image in full size
Configuration Pages for AD and Domain Directory
Endpoint — /greet.nsf. If the application is using Lotus Domino Server for note-taking basically to have a place to kept all meeting notes, employee notes, etc. Through this endpoint I was able to find out the meeting notes with customers containing information about customer issues, feedback, etc.
Conclusion

Without wasting much time on the theory let’s understand what is the impact ad remediation part of it:

The misconfiguration exposes huge amount of sensitive information about the AD configuration, Domain configuration, Server configuration, Employees PII Data, etc. These information can be used to understand the structure of the AD and other configuration that aids the attacker to exploit it using AD vulnerabilities or other loop holes available.
The customer notes and other information about an organization customers can be used by their competitors which help them to make their strategies more powerful which will affect the organization in business revenue.
Whenever any of the third-party service or web servers exposing internal/sensitive paths then it means either the web server is deployed without changing the default settings or development mode of the application is not switched off. It means before deploying any application to the internet every settings should be properly reviewed to prevent such kind of misconfigurations.

Always FUZZ based on the technology stack and always dig deep, say you found /admin — 403, then try fuzzing for https://example.com/admin/FUZZ URL to check if any other endpoint accessible without admin login.

Recon Automation Script Snippet
Press enter or click to view image in full size
Reconnaissance Automation Script
It’s time to Say Good Bye 🙋‍♂

I’ll share more phases of my recon script in next blog because only these phases are required to setup the context for this blog.

Get Aayush Vishnoi’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Thanks for reading, hope you enjoyed and learned something from this blog.

If you have any questions, DM at https://twitter.com/AayushVishnoi10.
