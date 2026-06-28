---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2017-11-15_how-i-pwned-a-company-using-idor-blind-xss.md
original_filename: 2017-11-15_how-i-pwned-a-company-using-idor-blind-xss.md
title: How I Pwned a company using IDOR & Blind XSS
category: documents
detected_topics:
- password-reset
- mobile-security
- idor
- xss
- command-injection
- otp
tags:
- imported
- documents
- password-reset
- mobile-security
- idor
- xss
- command-injection
- otp
language: en
raw_sha256: a530dd61aa94a7457e30810e011a744cd6cb32c3694ade3485195715175b04dd
text_sha256: bdbd4d810549df4ac3f88c3c7c496dbe0af66b093223a610e3ee89ba10b1d379
ingested_at: '2026-06-28T07:31:56Z'
sensitivity: unknown
redactions_applied: false
---

# How I Pwned a company using IDOR & Blind XSS

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2017-11-15_how-i-pwned-a-company-using-idor-blind-xss.md
- Source Type: markdown
- Detected Topics: password-reset, mobile-security, idor, xss, command-injection, otp
- Ingested At: 2026-06-28T07:31:56Z
- Redactions Applied: False
- Raw SHA256: `a530dd61aa94a7457e30810e011a744cd6cb32c3694ade3485195715175b04dd`
- Text SHA256: `bdbd4d810549df4ac3f88c3c7c496dbe0af66b093223a610e3ee89ba10b1d379`


## Content

---
title: "How I Pwned a company using IDOR & Blind XSS"
url: "https://www.ansariosama.com/2017/11/how-i-pwned-company-using-idor-blind-xss.html"
final_url: "https://www.ansariosama.com/2017/11/how-i-pwned-company-using-idor-blind-xss.html"
authors: ["Osama Ansari (@AnsariOsama10)"]
bugs: ["IDOR", "Blind XSS"]
publication_date: "2017-11-15"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 6054
---

###  How I Pwned a company using IDOR & Blind XSS 

[ November 15, 2017  ](https://www.ansariosama.com/2017/11/how-i-pwned-company-using-idor-blind-xss.html "permanent link")

This post is about exploiting Blind XSS and IDOR to gain access to company's Slack, Facebook Workplace and other services used by the company.  
  
Special Thanks to Inti De Ceukelaire without his disclosure this would not have been possible.  
  
And also thanks to my friend Harsh Jaiswal for giving some ideas.  
  
Most of the people from infosec community must have read the disclosure by Inti De Ceukelaire regarding [Ticket Trick](https://medium.freecodecamp.org/how-i-hacked-hundreds-of-companies-through-their-helpdesk-b7680ddc2d4c), if you have not read I would suggest reading that first. ( <https://medium.freecodecamp.org/how-i-hacked-hundreds-of-companies-through-their-helpdesk-b7680ddc2d4c> )  
  
After reading the article, first thing came to my mind was exploiting this on a company as it had similar functionality on Support Tickets.  
  
The company's website had a Support Portal. We could create a Ticket by sending an email.  
  
Exploiting Ticket Trick to gain access to company's Slack or Facebook Workplace was not possible as Slack and Facebook included a random token while sending verification or forgot password emails.  
  
But there was a Blind XSS in company's internal domain from where they managed the tickets and an IDOR to View any user's ticket using both the vulnerabilities, I was able to access the company's Slack, Facebook Workplace.  
  
  

###  **IDOR to View Any Support Ticket:**

**  
**There was a GET request in the Mobile application which allowed to view support tickets of any user by changing the Ticket ID.  
  
GET /api/param?param=XXXXXXXXXXXXXXXXXXXXX HTTP/1.1  
Host: company.com  
Connection: close  
Accept: application/json, text/javascript  
X-Requested-With: XMLHttpRequest  
User-Agent: Mozilla/5.0  
Accept-Language: en-IN,en-US;q=0.8  
Cookie: x  
  
The Ticket ID, however, included 12-13 random numbers, so bruteforcing it would have taken a lot of time.  
  
So we still needed to find the Ticket ID.  
  
The IDOR was reported 1 month back was not fixed :P  
  

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEh1SipHOYw84-oEyoS0Ux9j-ux7GsmTp1ydB2ygVIpdwvBCLnlXs88YwCBD2jS8AFTxxwBKsIGvOak3VkIoqxTDtiHmzbdEa-6QL-D3Qqk332wXhczPmEIGS851ybjRzQV3pnKrooGZl6M/s640/Screenshot_5.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEh1SipHOYw84-oEyoS0Ux9j-ux7GsmTp1ydB2ygVIpdwvBCLnlXs88YwCBD2jS8AFTxxwBKsIGvOak3VkIoqxTDtiHmzbdEa-6QL-D3Qqk332wXhczPmEIGS851ybjRzQV3pnKrooGZl6M/s1600/Screenshot_5.png)

  
  

###  **Blind XSS:**

**  
**

We could create a support ticket by sending an email to support@company.com.  
  
The company then manages the Tickets from an internal domain.  
  
The input fields sent from the email was not sanitized on their internal domain.  
  
I created a ticket by sending an email with XSS payload.  
When the ticket was viewed by support staff XSS was triggered on their internal domain.  
  
I had used [**XSS Hunter**](https://xsshunter.com/) to test this Blind XSS, XSS Hunter also captures the DOM of the entire page where the XSS is executed.  
  
The DOM contained all recently created Ticket IDs.  
  
The Blind XSS was also reported a month back and was marked as Not Applicable as the domain where XSS was executed was an internal domain and not mentioned in the scope.  
  

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjas_3YznHEJDHlKPaUcZ53aV3-PBZ2EpkDMOYA24ElFHQc4PyCSvQ8wbcd-NhIJBNhngDMdKU_RG3ZEujtucoyi_XVZe5qmwVejGxLm74_O0OX4VKeno8Iac-Gma0pvFB0Ay8cahfR-tc/s640/Screenshot_6.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjas_3YznHEJDHlKPaUcZ53aV3-PBZ2EpkDMOYA24ElFHQc4PyCSvQ8wbcd-NhIJBNhngDMdKU_RG3ZEujtucoyi_XVZe5qmwVejGxLm74_O0OX4VKeno8Iac-Gma0pvFB0Ay8cahfR-tc/s1600/Screenshot_6.png)

  
  

###  **Chaining both the issues:**

**  
**

I sent a password reset link to support@company.com at https://company.slack.com/forgot.  
This resulted in the creation of a ticket by no-reply-randomtoken@slack.com.  
  
Immediately after sending the password reset link to Slack, I sent an email to support@company.com with Blind XSS Payload.  
  
After some time the Blind XSS was executed, I received the DOM of the page.  
  
The DOM contained Ticket ID of the email sent from no-reply-randomtoken@slack.com.  
  

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEju6Hl96ey_uXs46L2pnu3D3w-DuRMvq1UIb7YR4oMarMEbetUpKYr8qUdYnS2hCUlP1GRxYpbDx_TK0TJzyjEgnyY9IV-fsNqpLF0HMe4g1pLkl7rjk1DwJcF-_no-vwwA3dlvb2XyXDY/s640/Screenshot_4.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEju6Hl96ey_uXs46L2pnu3D3w-DuRMvq1UIb7YR4oMarMEbetUpKYr8qUdYnS2hCUlP1GRxYpbDx_TK0TJzyjEgnyY9IV-fsNqpLF0HMe4g1pLkl7rjk1DwJcF-_no-vwwA3dlvb2XyXDY/s1600/Screenshot_4.png)

  
  
Using the IDOR, I was able to View the Ticket which surprisingly contained registration links of 8 Slack Channels of the Company.  
  
Similarly, Company's Facebook Workplace could have been accessed.  
  
This was also marked Not Applicable by the company but was rewarded with the company's minimum bounty amount.

Share 

  * Get link
  * Facebook
  * X
  * Pinterest
  * Email
  * Other Apps

### Labels

[POC](https://www.ansariosama.com/search/label/POC)

Labels: [POC](https://www.ansariosama.com/search/label/POC)

Share 

  * Get link
  * Facebook
  * X
  * Pinterest
  * Email
  * Other Apps

### Comments

  1. ![](//www.blogger.com/img/blogger_logo_round_35.png)

[nullptr](https://www.blogger.com/profile/11186103388271684699)[28 December 2017 at 20:26](https://www.ansariosama.com/2017/11/how-i-pwned-company-using-idor-blind-xss.html?showComment=1514521566956#c18224343725982600)

Salaam Bhai. Really amazing hack !Motivates me much 

Reply[Delete](https://www.blogger.com/comment/delete/7193605477876967525/18224343725982600)

Replies

Reply

  2. ![](//blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj8klhd1b6TKvx_UvddIkRpjBsY215t1TJYwIGwoKXzrDYkL6YxbBODDsbNJq-5tpBrSl8HrZIq7gliQzKSMuf3lEtMkUYHTcWCCr11aFD_dSJ7jK5dEgvIjwwF8l450g/s45-c/favicon.jpg)

[Hx01](https://www.blogger.com/profile/10354433670421325200)[9 April 2018 at 12:14](https://www.ansariosama.com/2017/11/how-i-pwned-company-using-idor-blind-xss.html?showComment=1523301270460#c270036046384856683)

Great Find! 

Reply[Delete](https://www.blogger.com/comment/delete/7193605477876967525/270036046384856683)

Replies

Reply

  3. ![](//blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhVDxLIqjJ_htWALCZhOVaa7dwLmiVN2dOt5FvbLMmYhgysBvqWwhqerN81Nd1XkEgc9mk_Mf-B91hBq7OGz9ttMeVDb_AC0NPpVyG95JyWwSLZGQ-nR7FyGMeTormxT7o/s45-c/FB_IMG_1557218112861.jpg)

[Chirag Gupta ](https://www.blogger.com/profile/00894480133192122391)[9 January 2019 at 08:29](https://www.ansariosama.com/2017/11/how-i-pwned-company-using-idor-blind-xss.html?showComment=1547051379514#c5949645644680526426)

Awesome

Reply[Delete](https://www.blogger.com/comment/delete/7193605477876967525/5949645644680526426)

Replies

Reply

Add comment

Load more...

#### Post a Comment

[](https://www.blogger.com/comment/frame/7193605477876967525?po=7967240451760352182&hl=en-GB&saa=85391&origin=https://www.ansariosama.com&skin=notable)
