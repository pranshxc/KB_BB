---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-05-22_i-helped-a-top-indian-health-benefits-management-platform-from-major-pii-leak-by.md
original_filename: 2023-05-22_i-helped-a-top-indian-health-benefits-management-platform-from-major-pii-leak-by.md
title: I helped a top Indian health benefits management platform from major PII leak
  by hacking their SQL Servers, AWS instance, DCs etc.
category: documents
detected_topics:
- mobile-security
- sso
- idor
- sqli
- command-injection
- path-traversal
tags:
- imported
- documents
- mobile-security
- sso
- idor
- sqli
- command-injection
- path-traversal
language: en
raw_sha256: 52b4e274bdc8cdfedcbe89f4cbd29988aef70a8f8d72330aedc258390ca86ca7
text_sha256: 45ffea42a8f32602d42e4c1e43b9c58b07b5a7df9f30c7755c05440420ac52ff
ingested_at: '2026-06-28T07:32:21Z'
sensitivity: unknown
redactions_applied: false
---

# I helped a top Indian health benefits management platform from major PII leak by hacking their SQL Servers, AWS instance, DCs etc.

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-05-22_i-helped-a-top-indian-health-benefits-management-platform-from-major-pii-leak-by.md
- Source Type: markdown
- Detected Topics: mobile-security, sso, idor, sqli, command-injection, path-traversal
- Ingested At: 2026-06-28T07:32:21Z
- Redactions Applied: False
- Raw SHA256: `52b4e274bdc8cdfedcbe89f4cbd29988aef70a8f8d72330aedc258390ca86ca7`
- Text SHA256: `45ffea42a8f32602d42e4c1e43b9c58b07b5a7df9f30c7755c05440420ac52ff`


## Content

---
title: "I helped a top Indian health benefits management platform from major PII leak by hacking their SQL Servers, AWS instance, DCs etc."
page_title: "Here, with this article, I’m going to show how I was able to avoid a majot PII leak by India's Top Health Benefits Management Platform | InfoSec Write-ups"
url: "https://nav1n.medium.com/i-helped-a-top-indian-health-benefits-management-platform-from-major-pii-leak-by-hacking-their-sql-b42caeca9729"
authors: ["nav1n (@nav1n0x)"]
bugs: ["SQL injection"]
publication_date: "2023-05-22"
added_date: "2023-05-22"
source: "pentester.land/writeups.json"
original_index: 1129
scraped_via: "browseros"
---

# I helped a top Indian health benefits management platform from major PII leak by hacking their SQL Servers, AWS instance, DCs etc.

I Helped Prevent a Major PII Leak for India’s Top Health Benefits Management Platform by Ethically Hacking Their SQL Servers and IT Infrastructure
nav1n👨🏻‍💻⚠️
Follow
11 min read
·
May 22, 2023

349

9

Hello all,

Here, with this article, I’m going to show how I was able to alert a major Indian health benefits management platform to protect the contact data, Personally Identifiable Information (PII), insurance claim details, and other sensitive information of thousands of their customers.

This article also highlights the negative aspects of Indian private bug bounty programs, such as how they handle bug reports and their tendency to avoid payment by claiming that the reported issue is a duplicate or already internally known bug.

D
espite the company’s decision not to reward me for my findings and close the report by labeling it as an internally known bug, I am still happy knowing that I was able to prevent a significant data leak.

Press enter or click to view image in full size

A few weeks ago, I learned about a public bug bounty program offered by an Indian private insurance and health benefits management platform through a follower on Twitter. They reached out for assistance with a vulnerability they had encountered and informed me about the program.

I have always been hesitant to participate in Indian bug bounty programs because, in my experience, the majority of them turn out to be fake and fail to fulfill their promises of payment as stated in their scope. Additionally, critical reports are often dismissed as duplicates or internally known issues.

However, a couple of programs like, Ola and PayTm are somehow exception to this.

Considering that the organization is a major player in the industry and has an intriguing business model, I made the decision to focus solely on hunting for high and critical issues, while intentionally avoiding any low-hanging vulnerabilities.

Initial Reckoning

The scope of the bug bounty program includes their main domain (*.target.com) as well as their Android and iOS apps.

To gather as many subdomains as possible, I conducted subdomain enumeration. Despite their wildcard scope, I was only able to find 10 subdomains after running httpx.

Interestingly, each of the web apps had a mobile version page, such as m.app.target.com, m.target.com, and m.app2.target.com. It seems that it’s hard to find a web developer who can create a fluid UI in India ;)

Press enter or click to view image in full size

Well, having a two different code-base for a same web-app UI that runs separately on desktop browser or mobile browser is a major failure in the first-place.

I started browsing the apps using my desktop and mobile phones, I normally do this to see how the app’s response in different browsers. I realized that, the mobile version runs on desktop browser in a mobile mode.

This highlights the poor design of the UI. Any competent UI designer knows how to redirect to the full version of a page if the mobile version of the UI is accessed on a desktop browser, or vice versa.

Attacking Mobile Version Apps

With initial recon done, I found the apps are designed using .net framework. One of the endpoints that caught my attention has a search feature to search insurance claims using ClaimID, UserID, Email, MobileNumber or PolicyNumbers. This page as well had an option to login to the portal, also uses SSO using Google.

WayBackURLs

In my reconnaissance methodology, I use WayBackURLs as a crucial step. At the beginning of the recon process, I utilize WayBackURLs with the -dates flag to check for any old cached pages. I usually run WayBackURLs on the subdomains I have, whether individually or in a bulk list. By using the -dates flag, I have found it particularly helpful in identifying a lot of SQL injections, and I applied the same approach in this case.

Tip: Developers may sometimes overlook hidden pages, which can become vulnerable over time if they are not updated along with the rest of the site’s

Since WayBackURLs generates a substantial number of archived URLs, I focus my testing on specific areas of interest such as password reset forms, login forms, and user registration forms. To narrow down the results, I employ the ‘grep’ command with filters such as ‘password,’ ‘Pass,’ ‘Password,’ and ‘pass’ to extract URLs that contain the keyword ‘password’.

Grep filtered around 50 archived pages that has “Pass”, “pass”, “Password” and “password” in the urls.

Press enter or click to view image in full size

Among them, I noticed two pages with the URLs “https://target.com/Login.aspx/GetEncryptedPass" and “https://target.com/Login.aspx/ReAuthWithPass".

When I visited these pages, they redirected me to a login page. Interestingly, when I accessed the same pages on my mobile device, my mobile browser displayed a “Password-reset” page instead of the login page, as seen on the desktop browser. To further investigate, I accessed the mobile version page from my desktop browser using the URL “https://m.target.com/Login.aspx/GetEncryptedPass" and found the same password-reset page.

This clearly indicates that the app utilizes different pages for mobile (m.xxxx.com) and regular desktop browsers. It is also possible that the developers created this mobile page but forgot to remove it after an update.

ParamSpider

I wanted to check if there is any reference to this page, so another way I could verify is by using ParamSpider to search for any archived versions of the pages saved elsewhere. I ran ParamSpider, but unfortunately, I couldn’t find any reference to this specific mobile page.

HTTrack

I use HTTrack as well during my reconnaissance to download websites for offline testing. In this case, I downloaded the entire site using HTTrack to examine the links used in the pages.

However, despite thorough searching, I couldn’t find any page or hyperlink within the entire site that referenced /Login.aspx/GetEncryptedPass. This confirms that it is indeed a dead link or page that the developer forgot to remove.

Upon inspecting the page source, I discovered a few parameters used in the password reset form, while the remaining content of the page seemed to be regular in nature.

{"param":"xxxx","key":"xxxx"}

I launched Burp Suite and proceeded to navigate the site. I inputted a random username and date of birth into the field, and subsequently submitted the form. Next, I began analyzing the HTTP requests within Burp Suite.

After a while, I encountered a POST request that included the same parameters I had previously identified. To prevent any potential sensitive information from being disclosed, I have made changes to the POST request below:

  POST /Login.aspx/GetEncryptedPass HTTP/1.1
  Content-Type: application/json; charset=UTF-8
  X-Requested-With: XMLHttpRequest
  Referer: https://m.target.com/
  Cookie: ASP.NET_SessionId=***; ***; _**__***_ses.12.1fef=*; __**__***_id.**.; loginattempt=9
  Content-Length: 73
  Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
  Accept-Encoding: gzip,deflate,br
  Host: m.target.com
  Connection: Keep-alive

  {"param":"AbcXYZ","key":"ABC1234'"}

I sent the request to the repeater tab and processed it, but I received an error indicating that the session had expired or was not found. After conducting a small reconnaissance, I discovered that each request was sent with specific cookies. These cookies included “ASP.NET_SessionId” + “____ses.12.1fef=” + “***_id.” + “loginattempt=x” (I have hidden the cookie names for security reasons). These cookies are valid for a maximum of three attempts. After the third failed attempt or request, all cookies, including ASP.NET_Session_Id, are reset, and a fresh cookie needs to be sent.

To overcome this issue, I made a new request using my browser and obtained the new cookies. I copied them from the cookie editor and sent them through Burp Repeater again. This time, I received an HTTP 200 OK response, but there were no changes in the response page; it remained a blank page.

Discovery of Time Based JSON Stacked Query SQL Injection

My first try with this app is time-based SQL injection attempt. So I sent:

{"param":"AbcXYZ'; waitfor delay '0:0:6' --","key":"ABC1234"}

The response was normal, no delay. I again sent same payload for another parameter “key”:

{"param":"AbcXYZ","key":"ABC1234'; waitfor delay '0:0:6' -- "}

And, guess what, the server delayed the response by 7.599 seconds. I made multiple requests with a new payload and session cookie, and I consistently received a delayed response that matched the payload time plus an additional 1 second.

Press enter or click to view image in full size

Now I know the web app is vulnerable to Time-based JSON Stacked Query SQL Injection.

SQLMap

Since time-based SQL injection is sometimes considered ‘high’ rather than ‘critical,’ I decided to increase the severity by running SQLMap to obtain detailed database structure and more.

Get nav1n👨🏻‍💻⚠️’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

I copied the request file to my Kali machine and executed SQLMap with the -p key. However, SQLMap failed to detect any time-based injection, even after trying different tamper scripts.

Reluctant to report it as a blind time-based SQL injection, I began searching for alternative solutions. During my research, I came across a thread on stackoverflow.com suggesting the direct injection of JSON stacked queries as data in a POST request. Although I had never attempted this method before, I decided to give it a try.

To mitigate failures due to session expiration, I added the option -ignore-code=403 to my SQLMap query after encountering a few failures where the server responded with a 403 error.

sqlmap -u 'https://m.target.com/Login.aspx/GetEncryptedPass' 
  --data  {"param":"AbcXYZ","key":"ABC1234'; waitfor delay '0:0:6' -- "} 
  --random-agent --ignore-code=403 --current-user --current-db 

Within a few minutes, SQLMap successfully identified the injection point. Using SQLMap, I executed a full exploit and obtained the following information: the host name, current user, and current database.

Press enter or click to view image in full size

The database server was experiencing significant lag, resulting in delays in response times. To mitigate potential blocks and improve the injection process, I increased the delay and utilized hex flags.

With the initial steps completed, my next objective was to retrieve the list of databases and search for any information that could potentially escalate the severity of the vulnerability.

I run the SQLMap again with following script:

sqlmap -u 'https://m.target.com/Login.aspx/GetEncryptedPass' 
--data  {"param":"AbcXYZ","key":"ABC1234'; waitfor delay '0:0:6' -- "} 
--random-agent --ignore-code=403 --dbs --hex 

After retrieving the list of databases, I became aware of the potential personally identifiable information (PII) that could be exposed.

The production database contained a vast amount of customer information, including PII of the company’s clients, client details of major insurance companies, information regarding client health, contact details such as phone numbers and email addresses, as well as login credentials of thousands of users.

This sensitive data was distributed across different databases, increasing the scope and magnitude of the potential data breach.

Not only did the company compromise their own data, but they also put at risk the data of their major insurance partner, a well-known group company “AB.” This includes the personally identifiable information (PII) of insurance holders, employee information, and even the entire database backup.

The extent of the data breach poses a significant risk to the privacy and security of the affected individuals and raises concerns about the overall data protection practices of both the company and their insurance partner.

At this critical point, I discovered a database that contained highly sensitive information, including AWS instance login credentials, domain controller administrator passwords, and exchange credentials. This discovery raised serious concerns about the security of their infrastructure.

With the ability to run an OS shell, there was a potential risk of gaining unauthorized access to their entire infrastructure and potentially wreaking havoc.

Considering the severity of this vulnerability, it is imperative that immediate action is taken to address and rectify these security flaws. The consequences could be catastrophic if this information fell into the hands of malicious actors or competitors.

Reporting

After submitting the detailed proof of concept (PoC) along with supporting evidence such as screenshots, screen recordings, and step-by-step instructions in a well-structured PDF, I sent it to the email address designated for the information security team.

Within moments, I received an automated reply confirming the receipt of my report, assuring me that the security team had received it, and stating that they would take appropriate action. The email also mentioned that I could expect a response within five working days.

True to their word, after the designated time period, I received a response from the infrastructure security team. The email from the security team contained the following message:

Hi Navin

Thank you for reporting the issue with us, but after evaluating your issue we have treated it as an internal known issue, as per internal policy known issues are not eligible for any monetary/reward.

Keep up the good work and we look forward to more reports from you in the future!

Thanks & Regards

Infra Security.

Press enter or click to view image in full size

The following morning, upon checking my email, I immediately started my desktop computer and launched Burp Suite to verify if the SQL injection issue still persisted. To my surprise, the time-based SQL injection was no longer effective, and the endpoint I had previously discovered had been removed.

I couldn’t help but feel astonished by the response I received from the security team. It became apparent that the endpoint I had found had been present since at least 2020 or even earlier, indicating a longstanding vulnerability.

They seemed to have had no prior knowledge of its existence until my report prompted them to investigate and quietly fix it, perhaps to avoid potential repercussions from higher management.

Given this experience, I made a personal decision never to participate in any Indian bug bounty programs again, with the exception of PayTM and Ola, which have had better reputations in the community.

Later that day, I took to Twitter to share my experience, and to my surprise, many of my followers responded with similar stories of encountering similar incidents in various bug bounty programs in India.

https://twitter.com/nav1n0x/status/1647478867123134465
Criticality of the data I found

The data that I discovered during my ethical hacking activities was of critical importance and had the potential to cause significant harm if it were to be leaked.

Considering the nature of the information, I couldn’t help but ponder the consequences the company would face if such a data breach occurred in the US or EU, where stricter regulations and penalties are in place.

While India is also making progress in terms of data protection laws and regulations, the value placed on data breaches and their repercussions may still be comparatively lower.

This realization led me to contemplate the need for companies like the one I encountered to face more significant consequences for their negligence. In an attempt to express my frustration and draw attention to these issues, I decided to write a lengthy blog post detailing my experience.

Additionally, I reached out to the security team multiple times in response to their initial reply, seeking further clarification or confirmation that they were aware of the issue before my report. Unfortunately, I did not receive any further communication from them. This lack of response further solidified my decision to refrain from participating in any future bug bounty programs within India.

In conclusion, I wanted to express my gratitude to you for taking the time to read about my experiences.

N.
