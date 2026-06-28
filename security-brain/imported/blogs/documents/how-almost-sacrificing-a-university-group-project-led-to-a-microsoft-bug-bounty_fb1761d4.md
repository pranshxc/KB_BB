---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2024-07-23_how-almost-sacrificing-a-university-group-project-led-to-a-microsoft-bug-bounty.md
original_filename: 2024-07-23_how-almost-sacrificing-a-university-group-project-led-to-a-microsoft-bug-bounty.md
title: How Almost Sacrificing a University Group Project led to a Microsoft Bug Bounty
category: documents
detected_topics:
- xss
- csrf
- command-injection
- password-reset
- mfa
- otp
tags:
- imported
- documents
- xss
- csrf
- command-injection
- password-reset
- mfa
- otp
language: en
raw_sha256: fb1761d4691182494afd94f1c1de4fc521caab0be4084fb8c45fcdc4d76f89ca
text_sha256: 839a90668e5cfd5840d7ce9c9b225442227724ecebc32f79aa83d7ea41bfdd2a
ingested_at: '2026-06-28T07:32:35Z'
sensitivity: unknown
redactions_applied: false
---

# How Almost Sacrificing a University Group Project led to a Microsoft Bug Bounty

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2024-07-23_how-almost-sacrificing-a-university-group-project-led-to-a-microsoft-bug-bounty.md
- Source Type: markdown
- Detected Topics: xss, csrf, command-injection, password-reset, mfa, otp
- Ingested At: 2026-06-28T07:32:35Z
- Redactions Applied: False
- Raw SHA256: `fb1761d4691182494afd94f1c1de4fc521caab0be4084fb8c45fcdc4d76f89ca`
- Text SHA256: `839a90668e5cfd5840d7ce9c9b225442227724ecebc32f79aa83d7ea41bfdd2a`


## Content

---
title: "How Almost Sacrificing a University Group Project led to a Microsoft Bug Bounty"
url: "https://medium.com/@pyrus369/how-almost-sacrificing-a-university-group-project-led-to-a-microsoft-bug-bounty-9801e0f8f006"
authors: ["Alex Bryant", "Aditya Dindi", "Eric Esquivel"]
programs: ["Microsoft (GroupMe)"]
bugs: ["XSS", "CSRF"]
publication_date: "2024-07-23"
added_date: "2024-07-30"
source: "pentester.land/writeups.json"
original_index: 144
scraped_via: "browseros"
---

# How Almost Sacrificing a University Group Project led to a Microsoft Bug Bounty

How Almost Sacrificing a University Group Project led to a Microsoft Bug Bounty
Pyrus
Follow
5 min read
·
Jul 23, 2024

107

1

Press enter or click to view image in full size

By: Alex Bryant, Aditya Dindi, and Eric Esquivel

Introduction

Eric and Aditya got together to work on their group project for their business class at university. Their team for the project included other people, and the way which a lot of university and high school students communicate is through a platform called GroupMe. GroupMe is a mobile and web group messaging app owned by Microsoft, with millions of registered users.

While looking around GroupMe, they got curious and 25 minutes later, wallah, an alert box appeared on their screens proving a Stored Cross-Site Scripting (XSS) vulnerability. Afterwards a close friend, Alex, joined and together they proceeded to escalate the vulnerability and successfully performed Cross-Site Request Forgery (CSRF) and postponed the group project.

What is XSS and CSRF?

Cross-Site Scripting (XSS) is a type of attack where malicious JavaScript is injected in web applications and it is executed on user’s browsers. There are 3 types of XSS attacks: Reflected, DOM, and Stored.

Reflected XSS is a vulnerability where the injected JavaScript reaches the back-end server and gets returned to the user without being filtered or sanitized.

Stored XSS occurs when user input is stored on the target server and then a victim retrieves the stored data where the malicious JavaScript is executed in their browser.

DOM XSS or Document Object Model XSS occurs when the injected JavaScript is used to change the page source through the DOM.

Cross-Site Request Forgery (CSRF) is an attack where an attacker is able to perform and execute requests on behalf of the authenticated victim.

How did we exploit this vulnerability?

When a message is sent in GroupMe, the recipient receives a “message request”. This is a preview message where the recipient can either accept or deny a message. When a message is accepted, it becomes a full chat where the users can send messages back and forth.

This is extremely important to know because when HTML and JavaScript was sent through as a message request, it was improperly being sanitized. As long as the user never accepts or denies the message request, an attacker is able to continuously send unsanitized HTML and JavaScript to the victim.

Figure 1: Sending the malicious JavaScript payload to the Victim-Account user
Figure 2: Receiving the malicious JavaScript payload message from the Attacker-Account user
Figure 3: Malicious JavaScript is executed on the Victim-Account’s Browser

Before knowing the specifics, Eric was able to pop an alert box on Aditya’s browser, but after Aditya accepted the message request to reply with his own payload, they were not able to perform XSS anymore as the full chat messages are properly sanitized. Alex quickly identified that the reason it worked the first time around was because it was a message request, and not a full chat where the sanitization was different. From here, we created additional accounts and made sure to not accept the messages so we could keep testing.

We quickly created 2 simple XSS payloads:

Redirect victims to different webpage like the signout page, for example.
Remove the accept box from the user’s screen as soon as they read the message request so that they couldn’t mitigate the threat.

However this wasn’t enough. We wanted to take this vulnerability further.

After looking around GroupMe some more, we found that when users enable/disable 2-Factor Authentication (2FA), or change their email, they automatically send their stored X-Access-Token through the web request and are not required to enter their password for verification.

Get Pyrus’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

We took advantage of this lack of verification and utilized a XSS payload to grab a user’s token value and performed CSRF by sending a POST request to the GroupMe web servers to change the account’s email address and disable 2FA. After that, we performed a password reset where an email will be sent to the email address we changed it to and completely take over the account.

Impact

We created a “master” XSS payload where we were able to perform all of the following in one single message leading to an instant account takeover:

Remove the accept message box
Change the user account’s email address to one of our choosing
Disable 2 factor authentication
Sign the user out of their account
Mitigations

Stored Cross-Site Scripting

Input filtering: Making sure that any user input is filtered for only expected or valid input
Utilizing Response Headers: Using appropriate response headers can help prevent Cross-Site Scripting by making sure HTTP / JavaScript is not executed when they are in the HTTP responses
Content Security Policy: CSP works by limiting the resources that a page can load

Cross-site Request Forgery

CSRF Tokens: A CSRF token is a value that is generated by the back-end server is shared and checked with the client when the client is performing an action
Conclusion

After finding and exploiting the unsanitised message requests, we were able to perform XSS to CSRF and send requests on behalf of the user as soon as they read our message, leading to immediate account takeover. Overall, there were some hiccups along the way during the review period, but we had a great experience finding and reporting this bug, and it has motivated us to stay curious and find more vulnerabilities like this one. (By the way, we got a 100 on our group project!)

Credits:

This bug was found by the three independent security researchers listed below:

- Alex Bryant | AlonTheSlay

https://www.linkedin.com/in/awb-alontheslay/

- Aditya Dindi | Pyrus

https://www.linkedin.com/in/adityadindi/

- Eric Esquivel | Agent007

https://www.linkedin.com/in/ericesquivel1/

Microsoft’s Online Acknowledgement Page:
https://msrc.microsoft.com/update-guide/acknowledgement/online

Figure 4: Our public acknowledgements
