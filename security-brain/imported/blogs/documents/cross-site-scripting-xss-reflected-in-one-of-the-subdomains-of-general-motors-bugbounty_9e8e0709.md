---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-12-03_cross-site-scripting-xss-reflected-in-one-of-the-subdomains-of-general-motorsbug.md
original_filename: 2020-12-03_cross-site-scripting-xss-reflected-in-one-of-the-subdomains-of-general-motorsbug.md
title: Cross Site Scripting (XSS) Reflected in one of the subdomains of “General Motors”(Bugbounty)
category: documents
detected_topics:
- xss
- idor
- sqli
- command-injection
- rate-limit
tags:
- imported
- documents
- xss
- idor
- sqli
- command-injection
- rate-limit
language: en
raw_sha256: 9e8e07093c77a80ed6413d94f43932f84550ff1fde4b0519afb25ee67bcdf5f7
text_sha256: 9a61d1b97098c0f76856815abb8421e28802c6d86147d6853067d751d9d3c4b6
ingested_at: '2026-06-28T07:32:04Z'
sensitivity: unknown
redactions_applied: false
---

# Cross Site Scripting (XSS) Reflected in one of the subdomains of “General Motors”(Bugbounty)

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-12-03_cross-site-scripting-xss-reflected-in-one-of-the-subdomains-of-general-motorsbug.md
- Source Type: markdown
- Detected Topics: xss, idor, sqli, command-injection, rate-limit
- Ingested At: 2026-06-28T07:32:04Z
- Redactions Applied: False
- Raw SHA256: `9e8e07093c77a80ed6413d94f43932f84550ff1fde4b0519afb25ee67bcdf5f7`
- Text SHA256: `9a61d1b97098c0f76856815abb8421e28802c6d86147d6853067d751d9d3c4b6`


## Content

---
title: "Cross Site Scripting (XSS) Reflected in one of the subdomains of “General Motors”(Bugbounty)"
page_title: "Cross Site Scripting (XSS) Reflected in one of the subdomains of 'General Motors'(Bugbounty) - SecurityTrooper"
url: "https://securitytrooper.com/en/cross-site-scripting-xss-reflected-in-one-of-the-subdomains-of-general-motorsbugbounty"
final_url: "https://securitytrooper.com/en/cross-site-scripting-xss-reflected-in-one-of-the-subdomains-of-general-motorsbugbounty"
authors: ["-"]
programs: ["General Motors"]
bugs: ["Reflected XSS"]
publication_date: "2020-12-03"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4092
---

[0](https://securitytrooper.com/en/cross-site-scripting-xss-reflected-in-one-of-the-subdomains-of-general-motorsbugbounty#respond)

# Cross Site Scripting (XSS) Reflected in one of the subdomains of “General Motors”(Bugbounty)

Posted on [December 6, 2020](https://securitytrooper.com/en/cross-site-scripting-xss-reflected-in-one-of-the-subdomains-of-general-motorsbugbounty "1:24 am") by [adm1n](https://securitytrooper.com/en/author/adm1n "View all posts by adm1n")

In this post I show you how I found a Cross Site Scripting (XSS) Reflected in one of the subdomains of “General Motors”.

![Resultado de imagen](https://upload.wikimedia.org/wikipedia/commons/thumb/4/4e/Logo_of_General_Motors.svg/150px-Logo_of_General_Motors.svg.png)

The first thing to make clear is that a company that is affiliated to a **BugBounty** program (**hackerone.com**) is allowed to analyze it. Remember that if they are not affiliated to these programs and we attack them, we can get into trouble, and we must warn them before publishing these vulnerabilities. 

Another thing is that belonging to these programs means that the chances of finding some type of vulnerability are very low.

For this reason, it is advisable to search within their subdomains to increase the chances of finding any of the vulnerabilities in the OWASP Top 10:

![Resultado de imagen de top 10 owasp 2017](https://sdtimes.com/wp-content/uploads/2017/11/OWASP.png)

In this case, I used the Sublist3r script (https://github.com/aboul3la/Sublist3r) to list the gm.com subdomains.

![](https://securitytrooper.com/wp-content/uploads/2018/04/2018-04-02-12_47_02-Kali-Linux-2017.2-vbox-amd64-Instantánea-1-Corriendo-Oracle-VM-VirtualBox.png)

After weeks of searching, I will focus on the subdomain **supply.eur.gm.com**.

This subdomain caught my attention because it looks like an old website.

![](https://securitytrooper.com/wp-content/uploads/2018/04/2018-04-02-12_51_09-Webtool-For-Vendors-Login.png)

After making a lot of tests (users enumeration, directories listing, SQLi…) I found that it did not make a correct control of exceptions when forcing an error, moreover, this error showed me all the text contained in the URL.

![](https://securitytrooper.com/wp-content/uploads/2018/04/2018-04-02-12_52_45-JRun-Servlet-Error.png)

Taking advantage of this error, I generated an injection of JavaScript code by not correctly filtering the values entered in the URL.

Finally, I prepared two proofs of concept to send to the **BugBounty** program that **GM** has on the web **https://www.hackerone.com/**

[**POC 1]** Payload: <img%20src=a%20onerror=alert(“XSS”)>

![](https://securitytrooper.com/wp-content/uploads/2018/04/xss.png)

[**POC 2**] Payload: <img onerror=javascript:window.location.replace(‘http:www.google.com’) src=”x”>

![](https://securitytrooper.com/wp-content/uploads/2018/04/redirectgm.gif)

These XSS vulnerabilities type allow an attacker to, for example, redirect a legitimate sub-domain to a cloned website to achieve a phishing attack.

Unfortunately, the compensation for the work done by GM was zero, and this often happens.

__[Uncategorized](https://securitytrooper.com/en/category/uncategorized)
