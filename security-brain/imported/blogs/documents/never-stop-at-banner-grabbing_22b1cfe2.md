---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2019-02-14_never-stop-at-banner-grabbing.md
original_filename: 2019-02-14_never-stop-at-banner-grabbing.md
title: Never Stop at Banner Grabbing
category: documents
detected_topics:
- command-injection
- information-disclosure
- api-security
tags:
- imported
- documents
- command-injection
- information-disclosure
- api-security
language: en
raw_sha256: 22b1cfe28a1ff99691fd0015396deecd608c9ca27500fc9bb24f1c9900dcb204
text_sha256: df86b141a12937b3de4a75ac1c35604759d265b309958ecbd745570347a14879
ingested_at: '2026-06-28T07:31:58Z'
sensitivity: unknown
redactions_applied: false
---

# Never Stop at Banner Grabbing

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2019-02-14_never-stop-at-banner-grabbing.md
- Source Type: markdown
- Detected Topics: command-injection, information-disclosure, api-security
- Ingested At: 2026-06-28T07:31:58Z
- Redactions Applied: False
- Raw SHA256: `22b1cfe28a1ff99691fd0015396deecd608c9ca27500fc9bb24f1c9900dcb204`
- Text SHA256: `df86b141a12937b3de4a75ac1c35604759d265b309958ecbd745570347a14879`


## Content

---
title: "Never Stop at Banner Grabbing"
page_title: "Never Stop at Banner Grabbing | I'm Gaurav Narwani"
url: "https://gauravnarwani.com/never-stop-at-banner-grabbing/"
final_url: "https://gauravnarwani.com/never-stop-at-banner-grabbing/"
authors: ["Gaurav Narwani (@gauravnarwani97)"]
bugs: ["Information disclosure"]
bounty: "241.93"
publication_date: "2019-02-14"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5414
---

[ ![](https://i0.wp.com/gauravnarwani.com/wp-content/uploads/2019/02/404-page-guide-wpk-1.jpg?fit=800%2C329&ssl=1) ](https://gauravnarwani.com/never-stop-at-banner-grabbing/)

# Never Stop at Banner Grabbing

[admin](https://gauravnarwani.com/author/admin/ "Posts by admin") / [February 14, 2019](https://gauravnarwani.com/never-stop-at-banner-grabbing/)

Hello guys, today we are going to talk about a very interesting vulnerability which I found on a private program. The vulnerability leaked the detailed server version when visiting an unusual error page. The details about this vulnerability are disclosed later after a small introduction to Web server fingerprinting. Please don’t forget to read the **Bug Bounty Tip** at the end of each post and also like, share and subscribe to the Blog.

## Web server fingerprinting

Web server fingerprinting also called **banner grabbing** is a critical task for the penetration tester. Knowing the version and type of a running web server allows testers to determine known vulnerabilities and the appropriate exploits to use during testing.

There are several different vendors and versions of web servers on the market today. Knowing the type of web server that is being tested significantly helps in the testing process and can also change the course of the test. This information can be derived by sending the web server specific commands and analysing the output, as each version of web server software may respond differently to these commands. By knowing how each type of web server responds to specific commands and keeping this information in a web server fingerprint database, a penetration tester can send these commands to the web server, analyse the response, and compare it to the database of known signatures. Please note that it usually takes several different commands to accurately identify the web server, as different versions may react similarly to the same command. Rarely do different versions react the same to all HTTP commands. So, by sending several different commands, the tester can increase the accuracy of their guess.

For example:

HTTP/1.1 200 OK  
**Server: Microsoft-IIS/5.0**  
Expires: Yours, 17 Jun 2003 01:41: 33 GMT  
Date: Mon, 16 Jun 2003 01:41: 33 GMT  
Content-Type: text/HTML  
Accept-Ranges: bytes  
Last-Modified: Wed, 28 May 2003 15:32: 21 GMT  
ETag: b0aac0542e25c31: 89d  
Content-Length: 7369

From the _Server_ field, one can understand that the server is likely to be**Microsoft-IIS/5.0**.

Each server has its own protocol behaviour and even though if the server name isn’t disclosed, by just looking at the protocols, the user can determine the server in the background.

## Case Study: Detailed server information disclosure

The application under test was a three-tier web application – Presentation tier (Front-End/User Interface), Application Tier (Functional Logic) and Data Tier (Databases) having various subdomains under the scope. As the program doesn’t allow information disclosure, the domain is named as example.com.

Let us consider a subdomain of the website example.com to be sub1.example.com. While testing for the site sub1.example.com it was found that banner grabbing was allowed and would leak the server to be**Microsoft-IIS/8.5**. Although banner grabbing is a bug but considered as P5 (Informative) on various platforms such as Hackerone and Bugcrowd. Reporting only banner grabbing would affect your average severity, therefore, more details were needed to be submitted along with the server version.

![](https://i0.wp.com/gauravnarwani.com/wp-content/uploads/2019/02/banner_sub.png?fit=1000%2C310&ssl=1)

Although dirb is a better tool for directory brute-forcing, a few directory brute-forcing payloads were used in the Intruder of Burp Suite to get the results much faster. The website had its own response to the page not found errors. It would redirect the user to a custom page not found page with a redirect response of 301. The 6000 payloads which were fired line by line would normally show a 301 response code redirecting to the 404 custom page. After approximately 2000 payloads fired, there was one payload which didn’t redirect to a custom 404 page, but a 404 page of the server.

The requested URL was as follows:

<https://sub1.example.com/General/admin>. (A full stop at the end)

![](https://i0.wp.com/gauravnarwani.com/wp-content/uploads/2019/02/sub2_version.png?fit=1000%2C182&ssl=1)

The page leaked Microsoft .NET Framework version as well as ASP.NET Version also the path of the website from its server.

A similar page was found in some other subdomains.

2nd URL:

<https://sub2.example.com/%252e%252e%5c%252e%252e%5c%2fetc%2fpasswd..%5c%2fetc%2fpasswd>

![](https://i0.wp.com/gauravnarwani.com/wp-content/uploads/2019/02/sub1_server.png?fit=1000%2C216&ssl=1)

3rd URL: <https://sub3.example.com/%252e%252e%5c%252e%252e%5c%2fetc%2fpasswd%2e%2e%5c%2fetc%2fpasswd>

![](https://i0.wp.com/gauravnarwani.com/wp-content/uploads/2019/02/sub2_version.png?fit=1000%2C182&ssl=1)

The server banner along with the leaked Microsoft .NET Framework version as well as ASP.NET Version was reported to the program.

The bug was triaged within a day and a bounty of **$241.93** was given for this bug.

**#BugBountyTip**

Payload running in lot of contexts. No script tags so grater chance of evasion from a WAF.

**javascript:”/*’/*`/*– ><html \” onmouseover=/*&lt;svg/*/onload=alert()//>**

Other payload from @LooseSecurity bypassing a lot of WAFs:

**< iframe src=”%0Aj%0Aa%0Av%0Aa%0As%0Ac%0Ar%0Ai%0Ap%0At%0A%3Aalert(0)”>**

Thats all for today. Please subscribe to my [**blog**](https://gauravnarwani.com/blog/). Connect with me on [**Linkedin**](https://linkedin.com/in/gauravnarwani97/).

## Gaurav Narwani

### Share this:

  * [Twitter](https://gauravnarwani.com/never-stop-at-banner-grabbing/?share=twitter "Click to share on Twitter")
  * [Facebook](https://gauravnarwani.com/never-stop-at-banner-grabbing/?share=facebook "Click to share on Facebook")
  * [LinkedIn](https://gauravnarwani.com/never-stop-at-banner-grabbing/?share=linkedin "Click to share on LinkedIn")
  * [WhatsApp](https://gauravnarwani.com/never-stop-at-banner-grabbing/?share=jetpack-whatsapp "Click to share on WhatsApp")
  * [Telegram](https://gauravnarwani.com/never-stop-at-banner-grabbing/?share=telegram "Click to share on Telegram")
  * [Print](https://gauravnarwani.com/never-stop-at-banner-grabbing/#print "Click to print")
  * 

### Like this:

Like Loading...

Posted in: [Bug Bounty](https://gauravnarwani.com/category/bugb/)
