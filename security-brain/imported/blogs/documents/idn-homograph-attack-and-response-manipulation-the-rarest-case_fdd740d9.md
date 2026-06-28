---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-07-09_idn-homograph-attack-and-response-manipulation-the-rarest-case.md
original_filename: 2023-07-09_idn-homograph-attack-and-response-manipulation-the-rarest-case.md
title: IDN Homograph Attack and Response Manipulation - The Rarest Case
category: documents
detected_topics:
- password-reset
- command-injection
- api-security
- mobile-security
tags:
- imported
- documents
- password-reset
- command-injection
- api-security
- mobile-security
language: en
raw_sha256: fdd740d9915a12479737a63676ab0ad310d3d7f2d194e55da3236c90d1170157
text_sha256: 46d9ac4ca5554d922c229108ddb8cb41a87235737e945d87345c960d1dd5b528
ingested_at: '2026-06-28T07:32:24Z'
sensitivity: unknown
redactions_applied: false
---

# IDN Homograph Attack and Response Manipulation - The Rarest Case

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-07-09_idn-homograph-attack-and-response-manipulation-the-rarest-case.md
- Source Type: markdown
- Detected Topics: password-reset, command-injection, api-security, mobile-security
- Ingested At: 2026-06-28T07:32:24Z
- Redactions Applied: False
- Raw SHA256: `fdd740d9915a12479737a63676ab0ad310d3d7f2d194e55da3236c90d1170157`
- Text SHA256: `46d9ac4ca5554d922c229108ddb8cb41a87235737e945d87345c960d1dd5b528`


## Content

---
title: "IDN Homograph Attack and Response Manipulation - The Rarest Case"
url: "https://shahjerry33.medium.com/idn-homograph-attack-and-response-manipulation-the-rarest-case-85f64c272a1c"
authors: ["Jerry Shah (@Jerry)"]
bugs: ["IDN homograph attack", "HTTP response manipulation", "Account takeover", "Password reset"]
publication_date: "2023-07-09"
added_date: "2023-07-17"
source: "pentester.land/writeups.json"
original_index: 953
scraped_via: "browseros"
---

# IDN Homograph Attack and Response Manipulation - The Rarest Case

IDN Homograph Attack and Response Manipulation - The Rarest Case
Jerry Shah (Jerry)
Follow
7 min read
·
Jul 9, 2023

365

4

Press enter or click to view image in full size

Summary

IDN stands for Internationalized Domain Name which is a system that allows domain names to be written and displayed in different scripts and character sets. It enables the use of non-ASCII characters, such as letters with diacritical marks (é, á, č, ŭ, í, ó) in domain names. This makes it possible for users to register using the look-a-like name and navigate to websites or create an account with the existing user.

If SMTP server is vulnerable to IDN homograph attack then it will treat a and á as same characters which can lead to security risks like account take over while registration.

Description

I found an IDN homograph vulnerability on a private program on one of the platform where I registered with an email address pentest@gmail.com.eew1utlvg6yth0mjd8shb1z8kzqpww.burpcollaborator.net and then tried to registered with the same email by just changing a of gmail to á character of IDN pentest@gmáil.com.eew1utlvg6yth0mjd8shb1z8kzqpww.burpcollaborator.net which gave me an error saying email already registered, so I thought that this might be vulnerable to IDN homograph attack. Then I went to forgot password page and used pentest@gmáil.com.eew1utlvg6yth0mjd8shb1z8kzqpww.burpcollaborator.net email address to reset the password and got a password reset link on my burpcollaborator and then I tried to reset the password of the user pentest@gmail.com.eew1utlvg6yth0mjd8shb1z8kzqpww.burpcollaborator.net, but it gave some internal server error. So I chained IDN homograph attack with response status code manipulation and changed the password successfully and logged into victim’s account.

In the above email the link eew1utlvg6yth0mjd8shb1z8kzqpww.burpcollaborator.net works as SMTP server, so in case if you do not have your own SMTP server you can use burpcollaborator’s subdomain as your SMTP server for testing IDN homograph attacks.

Basic difference between Web Server and SMTP Server

Web Server

A web server is responsible for hosting and serving web pages over the internet. It handles HTTP/HTTPS requests and responses, serving web content to clients that access the website.

SMTP Server

SMTP server is responsible for sending and receiving email messages. It handles the delivery of emails between mail servers and is used by email clients (such as Outlook or Gmail) to send outgoing messages.

Anatomy of Burp Collaborator as SMTP Server

Firstly, Burp Collaborator does not act as SMTP server itself. It provides unique subdomains (e.g. in my case eew1utlvg6yth0mjd8shb1z8kzqpww.burpcollaborator.net) that can be used in various testing scenarios, including SMTP-related tests.

Now in the email pentest@gmail.com.eew1utlvg6yth0mjd8shb1z8kzqpww.burpcollaborator.net, Burp Collaborator subdomain (eew1utlvg6yth0mjd8shb1z8kzqpww.burpcollaborator.net) is appended for testing email-related vulnerabilities within web applications (IDN homograph attack in my case).

Here is the breakdown of the email:

Email Address: pentest@gmail.com.eew1utlvg6yth0mjd8shb1z8kzqpww.burpcollaborator.net

The email address consists of three parts: the username “pentest”, the domain “gmail.com” and the subdomain “eew1utlvg6yth0mjd8shb1z8kzqpww.burpcollaborator.net”, which acts as SMTP server

Burp Collaborator:

Burp Collaborator is a feature of Burp Suite. Burp Collaborator provides unique subdomains (e.g. in my case eew1utlvg6yth0mjd8shb1z8kzqpww.burpcollaborator.net) that can be used for testing various security vulnerabilities.

IDN Homograph Testing Scenario:

In this scenario, the Burp Collaborator subdomain (eew1utlvg6yth0mjd8shb1z8kzqpww.burpcollaborator.net) is used in conjunction with the email address pentest@gmail.com which suggests that the email address is being tested for potential vulnerabilities related to email handling within a web application.

NOTE: In real world scenario, you need to buy an IDN domain for e.g. gmáil.com or yáhoo.com or outloók.com. You can replace any character with IDN character to buy IDN homographed domain.

Anatomy of IDN Homograph Attack with SMTP Server

SMTP servers typically treats a and á as the same characters because they often rely on ASCII (American Standard Code for Information Interchange) character encoding, which does not differentiate between them. This can make SMTP servers vulnerable to IDN homograph attacks.

ASCII Character Encoding:

SMTP servers historically used ASCII, which represents characters using a 7-bit encoding scheme.
ASCII includes characters commonly used in the English language and lacks support for many non-English characters or diacritics, including accented (IDN) characters like á.
Due to the limited character set in ASCII, SMTP servers traditionally handled and processed only ASCII characters.

Punycode and Internationalized Domain Names (IDNs):

To enable the use of non-ASCII characters in domain names, the Internationalized Domain Name (IDN) system was introduced.
IDNs use a process called Punycode encoding to represent non-ASCII characters using a combination of ASCII characters so á will be treated as U+00E1 in ASCII table which will differentiate a and á in SMTP server.

SMTP Server Vulnerability:

SMTP servers that do not incorporate proper handling and verification mechanisms for IDN homographs can be vulnerable.
When processing email addresses, the SMTP server may not differentiate between the ASCII a and the non-ASCII á due to their visual similarity.

Vulnerability Insights:

There are certain things to note to identify whether the SMTP server is actually vulnerable or not.

If the SMTP server is vulnerable to IDN Homograph attack then you will receive the reset link where the IDN email will be showed as pentest@xn--gmil-6na.com.eew1utlvg6yth0mjd8shb1z8kzqpww.burpcollaborator.net

It is because the IDN code for á is xn-- so for gmáil.com it will be xn--gmil-6na.com

Press enter or click to view image in full size
https://www.punycoder.com/

In some cases you will still receive the password reset link even if you use IDN homographed email for victim’s account password reset (e.g. pentest@gmáil.com.eew1utlvg6yth0mjd8shb1z8kzqpww.burpcollaborator.net) but when you will be receiving the link, it would be a normal link (e.g. pentest@gmail.com.eew1utlvg6yth0mjd8shb1z8kzqpww.burpcollaborator.net) instead of IDN homographed link (e.g. pentest@xn--gmil-6na.com.eew1utlvg6yth0mjd8shb1z8kzqpww.burpcollaborator.net). So in this case the SMTP server is not vulnerable to IDN homograph attack.

Get Jerry Shah (Jerry)’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

How I found this vulnerability ?

I went to my target website and used an email pentest@gmail.com
Press enter or click to view image in full size
Sign-up Page

2. I started the burp collaborator client, clicked on copy to clipboard and appended the subdomain (give by collaborator) to the email (e.g pentest@gmail.com.eew1utlvg6yth0mjd8shb1z8kzqpww.burpcollaborator.net) and clicked on sign up

Press enter or click to view image in full size
Burp Collaborator Client
Press enter or click to view image in full size
Getting Subdomain
Press enter or click to view image in full size
Verification Link - Sent

3. I received a verification link on my burp collaborator client and I used it and logged into an account to complete further process (victim’s account).

Press enter or click to view image in full size
Verification Link - Received
Press enter or click to view image in full size
Registration

NOTE: I left the process incomplete and logged out of an account

4. I went to forget password page (as an attacker) and entered an email pentest@gmail.com.eew1utlvg6yth0mjd8shb1z8kzqpww.burpcollaborator.net and changed the a of gmail.com with IDN character’s á and sent a password reset email

Press enter or click to view image in full size
IDN character - á
Press enter or click to view image in full size
IDN Homograph Email
Press enter or click to view image in full size
Email Sent

5. I received the forgot password link of victim’s account (pentest@gmail.com.eew1utlvg6yth0mjd8shb1z8kzqpww.burpcollaborator.net) to my IDN homographed email address (pentest@gmáil.com.eew1utlvg6yth0mjd8shb1z8kzqpww.burpcollaborator.net)

Press enter or click to view image in full size
Email Received - 1
Press enter or click to view image in full size
Email Received - 2

NOTE : You can see the message in screenshot, it says “You -- or someone pretending to be you -- requested a password for your account.”

6. I used the password rest link to change the password of the victim’s account but it gave me an error

Press enter or click to view image in full size
Internal Server Error - 500

7. Then I intercepted the forgot password link request using burp > right clicked > Do Intercept > Response to request and changed status code from 500 Internal Server to 200 OK

Press enter or click to view image in full size
Forgot Password Request
Press enter or click to view image in full size
500 - Internal Server
Press enter or click to view image in full size
200 - OK

8. Then I used the password I wanted and changed the password of victim’s account (pentest@gmail.com.eew1utlvg6yth0mjd8shb1z8kzqpww.burpcollaborator.net)

Press enter or click to view image in full size
Changing Password
Press enter or click to view image in full size
New Password Set

9. As it was done using response manipulation, I wanted to confirm whether the password was really changed or not so I tried to login into the account and it was successful

Press enter or click to view image in full size
Logged in to Victim’s Account

NOTE: Here you can see the process is still pending because earlier as victim, I left the process incomplete.

Why this happened ?

In my opinion,

It happened because the SMTP server did not have proper handling and verification mechanisms for IDN homographs characters. When processing email address, the SMTP server was not able to differentiate between the ASCII a and the non-ASCII á due to their visual similarity which made this attack possible.

Press enter or click to view image in full size
The Process

Impact

This kind of vulnerability makes it possible for an attacker to take over anyone’s account on the target website and can steal all the PII data of the user.

CVSS Calculation

Score - 5.6 Medium

Vector String - CVSS:3.0/AV:N/AC:H/PR:N/UI:N/S:U/C:L/I:L/A:L

Mitigation

To mitigate the vulnerability of IDN homograph attacks, SMTP servers should implement measures to handle IDN domains properly, such as:

Incorporating Punycode decoding to accurately interpret and process IDN email addresses.
Enforcing strict email address validation to detect suspicious or potentially spoofed domains.
Regularly updating server configurations and security policies to stay updated with the latest best practices for handling IDN domains.
Press enter or click to view image in full size
