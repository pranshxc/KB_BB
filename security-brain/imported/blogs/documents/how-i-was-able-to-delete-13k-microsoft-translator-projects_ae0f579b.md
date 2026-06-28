---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2018-07-19_how-i-was-able-to-delete-13k-microsoft-translator-projects.md
original_filename: 2018-07-19_how-i-was-able-to-delete-13k-microsoft-translator-projects.md
title: How I was able to delete 13k+ Microsoft Translator projects
category: documents
detected_topics:
- sso
- idor
- command-injection
- otp
- csrf
- mobile-security
tags:
- imported
- documents
- sso
- idor
- command-injection
- otp
- csrf
- mobile-security
language: en
raw_sha256: ae0f579bf454885acefe9613ce230ef946b8cb1f2a7633fd073b6de0ff7f1929
text_sha256: 83e28620ed439065c5c590da12269a44971ae35ad9c9d7394106306a780cb781
ingested_at: '2026-06-28T07:31:57Z'
sensitivity: unknown
redactions_applied: false
---

# How I was able to delete 13k+ Microsoft Translator projects

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2018-07-19_how-i-was-able-to-delete-13k-microsoft-translator-projects.md
- Source Type: markdown
- Detected Topics: sso, idor, command-injection, otp, csrf, mobile-security
- Ingested At: 2026-06-28T07:31:57Z
- Redactions Applied: False
- Raw SHA256: `ae0f579bf454885acefe9613ce230ef946b8cb1f2a7633fd073b6de0ff7f1929`
- Text SHA256: `83e28620ed439065c5c590da12269a44971ae35ad9c9d7394106306a780cb781`


## Content

---
title: "How I was able to delete 13k+ Microsoft Translator projects"
page_title: "How I was able to delete 13k+ Microsoft Translator Projects"
url: "https://haiderm.com/how-i-was-able-to-delete-13k-microsoft-translator-projects/"
final_url: "https://haiderm.com/how-i-was-able-to-delete-13k-microsoft-translator-projects/"
authors: ["Haider Mahmood (@haiderinfosec)"]
programs: ["Microsoft"]
bugs: ["CSRF", "IDOR"]
publication_date: "2018-07-19"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5801
---

[ Appsec ](https://haiderm.com/category/application-security/ "View all posts in Appsec")

# How I was able to delete 13k+ Microsoft Translator projects

by [Haider Qureshi](https://haiderm.com/author/haiderm/ "View all posts by Haider Qureshi")|Published [July 19, 2018](https://haiderm.com/2018/07/19/ "1:06 pm")|2 comments

## Introduction

Sometime back I was hunting for Vulnerabilities in Microsoft Web services, as Microsoft has large online infrastructure, finding a vulnerability which could lead to [Microsoft hall of fame for security researchers ](https://technet.microsoft.com/en-us/security/cc308589.aspx)wasn’t difficult. While browsing around their online services, one of their services, [Microsoft hub translator ](https://hub.microsofttranslator.com/SignIn?returnURL=%2FHome%2FIndex)caught my attention.

Microsoft hub translator is **and I quote:** “ _Microsoft Translator Hub empowers businesses and communities to build, train, and deploy customized automatic language translation systems—-”._

I signed up and started looking for vulnerabilities and found critical level vulnerability through which I was able to delete All Microsoft hub translator 13000+ projects**.** As the vulnerability is fixed now, I’m sharing the technical details.

## Technical Details

Microsoft hub translator allows you to create customized automatic language translation system projects. I signed up and created a project solely for bug finding purposes, I had no idea about its functionality though. Created a project named it ‘huntingbugs’.

[![Microsoft Hall Of fame](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)](https://web.archive.org/web/20160304014038/https://haiderm.com/wp-content/uploads/2015/03/MicrosoftHallOfFame.jpg?b2a1e3)

As you could see, it allows ‘Edit’ and ‘Remove’ functionality, if you hit remove, it simply removes the project, nothing fancy here. So I fired up burp suite and started intercepting HTTP requests. Below is the “Remove” HTTP request.

### Remove Project HTTP Request
  
  
  POST /Projects/RemoveProject?projectId=12839 HTTP/1.1
  Host: hub.microsofttranslator.com
  User-Agent: Mozilla/5.0 (Windows NT 6.3; WOW64; rv:36.0) Gecko/20100101 Firefox/36.0
  Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
  Accept-Language: en-US,en;q=0.5
  Accept-Encoding: gzip, deflate
  Referer: https://hub.microsofttranslator.com/Projects/Index
  Cookie: RPSAuth=FABKARSt1lMxfQ39EcbVsLWT8hLbEL12RANmAAAEgAAACI6Hs92zqyRlCAGce1EqwSJmjJe21nXVHarrEJ9ROzjj21XAthl%2BUUjzX3XR5JeCB8WI0oMdmwQhyn30OIiubBYaeLeg21nqXT06UwzczFIDAjoqU%2BQpCg9SWaLSVSC3aKMZPT92NVjgySbIV8YYxPA4XMVMbU04mvNKv8v5vaGVMUNBtjHldxFqKYEWqI5P0UZetmtagzOK%2Bf2CRFbgb3Gak68RN6Mjj/xXt2ovC8pxYn2qb9MqSNxHC4Y3bA8n6vyZoJzM6Uu0zZpTUPIhv5L1PyHOO3FdXFELqttx2Yd2LEJNvxjkmON9KcYXIR%2BlUsHfimE901msD9XWB1SLG3zvm06oacncf1WGrdjEdnA2lOgUALlEhQzxHbGm6TryDMpq%2BbrTU/wG; RPSSecAuth=FABKARSt1lMxfQ39EcbVsLWT8hLbEL12RANmAAAEgAAACKDdutui3VqgCAE5DVaipcaF6WaWT%2B0L0ppLMAd7kigpYcQ89xhwiDiYN9yNhyVf86EW6KiiOs7FY2PCTFH2rM/uH3LYLIhTEYturZ5vOjVPBUP6QqqAtP9rvUCtv9%2Bakv9WNwY4gpZzQ4SXjtVpSMqyrV3RIN/emocWtNDmU5BPrnAZk50oAnoSf6aJX5IjaNcXc61Tv3BSO6m3GKLevxWnpSoyLzIajETwMSBe84fL5fWyUI0r3jXq7rW/rUh/Go/R4OzS2nL1okl512yFcZFZFXdsEq6k5M0lKP0L9ZTVtaW0WiZKXKgY%2B%2BPPtImjI5whKX2U4wbqgPiD1rxXwDogAlcrLKu6YGEHfVg01iG0GQ0UAF%2BhVQ4CptuuRm8tI8XE9zmo3%2Bhr; ANON=A=365DFF2DD45617971705DA33FFFFFFFF&E=1089&W=1; NAP=V=1.9&E=102f&C=h8ZS17Xmf0z4Q2T9Dj26e_Pijaca9G00g1PJCcXaI36L1P7jWHYOFQ&W=1; mstcid=[RemovedEmail]
  Connection: keep-alive
  Content-Type: application/x-www-form-urlencoded
  Content-Length: 0

POST request with no content and parameter in the URL (its kinda weird isn’t it?) the “**projectid** ” parameter in the above request is the ID of the individual project in the database, which in this case is “**12839** “, by observing the above HTTP request, a simple delete project query could be something like:-
  
  
  Delete project
  FROM projects 
  WHERE projectid=12839;

After forwarding the HTTP request, our project “**12839** ” got deleted, nothing out of the ordinary.

[![Microsoft Security Bug](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)](https://web.archive.org/web/20160304014038/https://haiderm.com/wp-content/uploads/2015/03/MicrosoftSecurityBug.jpg?b2a1e3)

## CSRF Vulnerability

Wait a minute, if you take a look at the Request, first thing to notice is there is no CSRF protection. This is prone to CSRF attack .In simple words, [CSRF vulnerability allows attacker to impersonate legit logged in user, performing actions on their behalf](https://haiderm.com/10-methods-to-bypass-cross-site-request-forgery-csrf/). Consider this:-

  * Legit user is logged in.
  * Attacker includes the URL in a page. (img tag, iframe, lots of possibilities here) “http://hub.microsofttranslator.com/Projects/RemoveProject?projectId=12839”
  * Victim visits the page, above request will be sent from their browser.
  * Requirement is that one should know the **ProjectID** number of logged in victim.
  * As it has no CSRF projection like antiCSRF tokens it results in the removal of the project.
  * Even if it has Anti-CSRF projection, here are ways to [bypass CSRF Token protections](https://haiderm.com/10-methods-to-bypass-cross-site-request-forgery-csrf/).

## The worst is yet to come

lets again take a look at HTTP project removal request. What if we fuzz around projectID, change its value, for testing this behavior, I created another account, logged in from a different browser and created two projects.

[![Microsoft Security Bulletin ](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)](https://web.archive.org/web/20160304014038/https://haiderm.com/wp-content/uploads/2015/03/MicrosoftSecurityBulletin.jpg?b2a1e3)

I got back to burp suite and started fuzzing around with projectID parameter value. I changed the ID parameter value from the same request posted above to the project ID value from the projects of second account and sent the request and refreshed the page.

[![Microsoft Hacking ](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)](https://web.archive.org/web/20160304014038/https://haiderm.com/wp-content/uploads/2015/03/MicrosoftHackingNews.jpg?b2a1e3)

## Got Pwned?

The project whose projectID I used in the HTTP request got deleted. Technically this vulnerability is called **[Indirect Object Reference](https://www.owasp.org/index.php/Testing_for_Insecure_Direct_Object_References_\(OTG-AUTHZ-004\)). **now if I just loop through the values starting from 0 to 13000 (last project), I’m able to delete all projects from the database. The vulnerability could have been avoided using simple checks, either the project that the user requested is owned by the same user, associating the project owner with the project is another way, but its Microsoft so….

## Happy Ending

Reported the vulnerability to Microsoft under their [Security Acknowledgement program](https://technet.microsoft.com/en-us/security/ff852094.aspx). Their initial response

[![Microsoft Hall of fame](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)](https://web.archive.org/web/20160304014038/https://haiderm.com/wp-content/uploads/2015/03/BugBounty.jpg?b2a1e3)

Microsoft Hall of fame

Rewarded me Microsoft Hall of fame for Security Researchers.

[![Microsoft Security Response Center](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)](https://web.archive.org/web/20160304014038/https://haiderm.com/wp-content/uploads/2015/03/HallOfFame.jpg?b2a1e3)

Microsoft Security Response Center

Contrary to previous experience with Microsoft Security acknowledgment program, they fixed the issue quickly in about two weeks.

  * [ appsec ](https://haiderm.com/tag/appsec/ "View all posts in appsec")
  * [ bugbounty ](https://haiderm.com/tag/bugbounty/ "View all posts in bugbounty")
  * [ CSRF ](https://haiderm.com/tag/csrf/ "View all posts in CSRF")
