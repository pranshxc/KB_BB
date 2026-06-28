---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-06-15_another-fappening-on-the-horizon.md
original_filename: 2020-06-15_another-fappening-on-the-horizon.md
title: Another 'Fappening' on the Horizon?
category: documents
detected_topics:
- mfa
- command-injection
- otp
- api-security
- cloud-security
- mobile-security
tags:
- imported
- documents
- mfa
- command-injection
- otp
- api-security
- cloud-security
- mobile-security
language: en
raw_sha256: 0c879578ad72b1d6fe2ef0a07be159ae5c47c3ba79c2bc9cb0c081525e9b2968
text_sha256: 0ddbf6e91050d5ba79d1a7d373b3d337b242fd09bffc8271447ffa0a79c1921d
ingested_at: '2026-06-28T07:32:02Z'
sensitivity: unknown
redactions_applied: false
---

# Another 'Fappening' on the Horizon?

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-06-15_another-fappening-on-the-horizon.md
- Source Type: markdown
- Detected Topics: mfa, command-injection, otp, api-security, cloud-security, mobile-security
- Ingested At: 2026-06-28T07:32:02Z
- Redactions Applied: False
- Raw SHA256: `0c879578ad72b1d6fe2ef0a07be159ae5c47c3ba79c2bc9cb0c081525e9b2968`
- Text SHA256: `0ddbf6e91050d5ba79d1a7d373b3d337b242fd09bffc8271447ffa0a79c1921d`


## Content

---
title: "Another 'Fappening' on the Horizon?"
url: "https://www.sociosploit.com/2020/06/another-fappening-on-horizon.html"
final_url: "https://www.sociosploit.com/2020/06/another-fappening-on-horizon.html"
authors: ["Sociosploit"]
programs: ["Apple"]
bugs: ["Account takeover", "Phishing"]
publication_date: "2020-06-15"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4497
---

###  Another "Fappening" on the Horizon? 

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhjD4W2EBs3yzYnYfQuedO9QUlz1m9_-_unLjukWCix87PhukfRzGy2lvGuJVMm64VpKjRfpV3TaWSlEKXak1IWQnw0dxEJqmyekyPDKD8FMDNgyu3xofIU2F5BL5l5i_8YVx5p3oB-a5Y/s320/icloud-100708260-orig.jpg)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhjD4W2EBs3yzYnYfQuedO9QUlz1m9_-_unLjukWCix87PhukfRzGy2lvGuJVMm64VpKjRfpV3TaWSlEKXak1IWQnw0dxEJqmyekyPDKD8FMDNgyu3xofIU2F5BL5l5i_8YVx5p3oB-a5Y/s1600/icloud-100708260-orig.jpg)

So in case you aren't fully up-to-speed on useless hacker trivia, "The Fappening" (also sometimes referred to as "Celebgate") was a series of targeted end-user cyber attacks which occurred back in 2014 (which strangely feels like forever in tech years), that resulted in unauthorized access to the iCloud accounts of several prominent celebrity figures. Following these breaches, photographs (for many including personal sexually explicit or nude photos) of the celebrities were then publicly released online. Most evidence points to the attack vector being spear phishing email attacks which directed the victims to a fake icloud login site, and then collected the victim's credentials to subsequently access their real icloud accounts.  
  

###  Migration to MFA

In response to these events, Apple has made iCloud one of the very few social web services that implements compulsory MFA ("Multi-Factor Authentication"). But while they might be ahead of the industry in that regard, they are still falling behind many of the other tech giants in its adoption of strong cryptographic MFA -- specifically FIDO U2F.  

###  But not quite secure enough ¯\\_(ツ)_/¯...

Because of their failure to support FIDO U2F, it is still possible to create a fake (evil twin) website and fully compromise access to user accounts -- just like the attacks that resulted in "The Fappening". The only difference in the attack, is that the attacker would now need to (because of the MFA token expiry) replay the credentials acquired from the victim in real-time to the legitimate iCloud site...to then subsequently hijack the session and gain unauthorized access.  
  
To demonstrate this risk, we were able to put together a fairly simple proof of concept by doing the following:  
  

  1. Copied the recursive HTML source code for the iCloud login (to create the evil clone).
  2. Hosted the copied HTML on a Apache web server
  3. Configure basic handler using Python/Flask to receive the iCloud form POST request data and replay to the actual iCloud site using Selenium browser (would use headless for real attack, but to visually demonstrate, used a headed browser in POC)
  4. Modify the Action attribute of the HTML form, to have it POST to a Python Flask handler

###  **Persistence too :)**

Persistence (persistent bypass of 2FA) can be achieved by leveraging a post-authentication option in iCloud, in which the user is prompted (upon login and also at the time of log-off) to trust the browser that the session is running in. Neither of these prompts require re-entry of the second factor. This allows an attacker who has compromised an account via a Real-Time Replay Session Instantiation attack to be able to login at a later time in the future with only the compromised username and password (second factor no longer needed).

  

  

  

**Responsible Disclosure Notice** \- These issues were responsibly reported to Apple (in February 2020), and have since been triaged and closed. 

Share 

  * Get link
  * Facebook
  * X
  * Pinterest
  * Email
  * Other Apps

Share 

  * Get link
  * Facebook
  * X
  * Pinterest
  * Email
  * Other Apps

### Comments

#### Post a Comment

[](https://www.blogger.com/comment/frame/8665546106972354468?po=5294808309206295031&hl=en&saa=85391&origin=https://www.sociosploit.com&skin=notable)
