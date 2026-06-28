---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-11-12_evading-filters-to-perform-the-arbitrary-url-redirection-attack.md
original_filename: 2020-11-12_evading-filters-to-perform-the-arbitrary-url-redirection-attack.md
title: Evading Filters to perform the Arbitrary URL Redirection Attack
category: documents
detected_topics:
- idor
- command-injection
- otp
- rate-limit
- automation-abuse
tags:
- imported
- documents
- idor
- command-injection
- otp
- rate-limit
- automation-abuse
language: en
raw_sha256: 40d4b5b8ef3806ff1374c190b8dd72e6b173c10df32581e1a6f20b15401ad14b
text_sha256: 4d5ee79f2fbbdf8374b5e36055ff7866dfc6984f212d5d48021a385d91097c9e
ingested_at: '2026-06-28T07:32:03Z'
sensitivity: unknown
redactions_applied: false
---

# Evading Filters to perform the Arbitrary URL Redirection Attack

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-11-12_evading-filters-to-perform-the-arbitrary-url-redirection-attack.md
- Source Type: markdown
- Detected Topics: idor, command-injection, otp, rate-limit, automation-abuse
- Ingested At: 2026-06-28T07:32:03Z
- Redactions Applied: False
- Raw SHA256: `40d4b5b8ef3806ff1374c190b8dd72e6b173c10df32581e1a6f20b15401ad14b`
- Text SHA256: `4d5ee79f2fbbdf8374b5e36055ff7866dfc6984f212d5d48021a385d91097c9e`


## Content

---
title: "Evading Filters to perform the Arbitrary URL Redirection Attack"
url: "https://medium.com/bugbountywriteup/evading-filters-to-perform-the-arbitrary-url-redirection-attack-cce628b9b6a0"
authors: ["Harsh Bothra (@harshbothra_)"]
bugs: ["Open redirect"]
publication_date: "2020-11-12"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4142
scraped_via: "browseros"
---

# Evading Filters to perform the Arbitrary URL Redirection Attack

Evading Filters to perform the Arbitrary URL Redirection Attack
Harsh Bothra
Follow
3 min read
·
Nov 12, 2020

418

3

Press enter or click to view image in full size

Arbitrary URL Redirection Attack often is popularly known as an Open Redirection attack, which is a common web vulnerability that allows an attacker to redirect the victim user to an attacker-controlled domain. This attack can leveraged to steal sensitive information such as tokens, perform social engineering, and other attacks.

The Arbitrary URL Redirection Attack mostly happens at the endpoint where the application accepts user-supplied URL and redirects it upon the execution of the vulnerable function. Some of the common parameters are ?return=,?returnURI=,?forwardedTo=, ?redirect=, ?redirectURI=, ?url=,?forward= and other such parameter that seems to load or redirect user to another endpoint.

If you enjoy reading my articles, do follow on Twitter: https://www.twitter.com/harshbothra_

Hi Fellow Hackers and Bug Bounty Hunters, In this article, I will be sharing about one of my recent findings where I was able to perform an Arbitrary URL Redirection Attack by evading the filters.

Modern frameworks by default implement security checks to validate and avoid Open Redirect Attacks. Often various filters such as validating if a third party URL or IP is used, validating if HTTPS:// protocol is used and if found, the application block the redirection from happening.

Recently, I encountered a similar situation while testing a private application say target.com. While checking for the various vulnerabilities from my application security checklist, I was looking for URL Redirection next.

The general approach I follow to test this attack is the following:

Approach — 1:
Log in to the application and navigate to any authenticated page say My Profile.
The URL generally looks like this: https://www.target.com/my-profile/
Now, log out from the application, and often some application throws a redirection parameter which redirects to the /my-profile page.
The URL looks like the following: https://www.target.com/login?forward=/my-profile
Now, in this case, the forward parameter is a potential attack vector to test for the Arbitrary URL Redirection attack.
Approach — 2:
Use the parameter enumeration tool such as ParamSpider & Arjun
Test the suspicious parameter against the Arbitrary URL Redirection attack.
Approach — 3:
Run gau & waybackurls on the target application and save them to a file.
Run Open Redirection GF Patterns on the saved file from step-1 and store the output to another file.
These URLs are suspected and potential endpoints for the Arbitrary URL Redirection attack.

In this case, for the application I was testing, I used Approach — 1 and I found the following potential endpoint for Open Redirection:

https://www.target.com/login?forward=/account/address

However, the forward parameter was validating if a URL is supplied and was blocking the redirection from happening. After further investigation I came to know that:

The application is filtering HTTPS protocol.
The application is filtering the Host & IP Address.

However, the application was allowing the use of the HTTP protocol. After thinking for a while, I used the following payload as a bypass:

Get Harsh Bothra’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

http://2899905732 : 2899905732 is the Integer IP representation of google.com’s IP: 142.250.64.100

The final payload looked like the following:

https://www.target.com/login?forward=http://2899905732

I navigated to the above URL and logged in with valid credentials. Upon the login, the application redirected to google.com resulting in a successful Arbitrary URL Redirection Attack.

Takeaways
Try all possible approaches to look at every single vulnerability.
If something is not working or is blocked, try to look for possible alternatives.
Try all possible ways to evade the filters to get success.
Learn along the way and apply your knowledge everywhere.

If you enjoyed reading the article do clap and follow on Medium and Twitter:

Twitter: https://www.twitter.com/harshbothra_

LinkedIn: https://www.linkedin.com/in/harshbothra

Website: https://harshbothra.tech

Talks: https://www.youtube.com/playlist?list=PLYn5_MxRvV-fxPL90I-uebXQzQBXfIaY0

Slides: https://speakerdeck.com/harshbothra
