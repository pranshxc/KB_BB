---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-02-08_chaining-bugs-to-get-my-first-bug-bounty.md
original_filename: 2023-02-08_chaining-bugs-to-get-my-first-bug-bounty.md
title: Chaining Bugs to get my First Bug Bounty
category: documents
detected_topics:
- csrf
- oauth
- sso
- command-injection
- password-reset
- otp
tags:
- imported
- documents
- csrf
- oauth
- sso
- command-injection
- password-reset
- otp
language: en
raw_sha256: 5e58b340c2676b9f61e94cbbe4faac85c1d70da419e769e7c43d4543bc72fb6c
text_sha256: 01fc0138af431fa12c05725bf0d2c9c6bcc0489842b3e7db5a629b087aa5418c
ingested_at: '2026-06-28T07:32:18Z'
sensitivity: unknown
redactions_applied: false
---

# Chaining Bugs to get my First Bug Bounty

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-02-08_chaining-bugs-to-get-my-first-bug-bounty.md
- Source Type: markdown
- Detected Topics: csrf, oauth, sso, command-injection, password-reset, otp
- Ingested At: 2026-06-28T07:32:18Z
- Redactions Applied: False
- Raw SHA256: `5e58b340c2676b9f61e94cbbe4faac85c1d70da419e769e7c43d4543bc72fb6c`
- Text SHA256: `01fc0138af431fa12c05725bf0d2c9c6bcc0489842b3e7db5a629b087aa5418c`


## Content

---
title: "Chaining Bugs to get my First Bug Bounty"
url: "https://infosecwriteups.com/chaining-bugs-to-get-my-first-bug-bounty-7e94afb704e7"
authors: ["ag3n7 (@ag3n7apk)"]
bugs: ["CSRF", "Open redirect", "Clickjacking", "Account takeover"]
publication_date: "2023-02-08"
added_date: "2023-03-02"
source: "pentester.land/writeups.json"
original_index: 1560
scraped_via: "browseros"
---

# Chaining Bugs to get my First Bug Bounty

FIRST BUG BOUNTY
Chaining Bugs to get my First Bug Bounty
ag3n7
Follow
4 min read
·
Feb 8, 2023

154

2

Openredirection + clickjacking + csrf -> Account Takeover

Press enter or click to view image in full size
Bounty

Hola Hackers,

This writeup is about my first bug bounty in which the submission was duplicate, even though they rewarded me for chaining the bugs and reported it with an effective approach of a real-life attack scenario.

Let’s Start

First we will discuss about the bugs which I chained together.

Open Redirection
Open redirection vulnerabilities arise when an application incorporates user-controllable data into the target of a redirection in an unsafe way. An attacker can construct a URL within the application that causes a redirection to an arbitrary external domain.

Clickjacking
Clickjacking is an interface-based attack in which a user is tricked into clicking on actionable content on a hidden website by clicking on some other content in a decoy website

CSRF
Cross-site request forgery (also known as CSRF) is a web security vulnerability that allows an attacker to induce users to perform actions that they do not intend to perform. It allows an attacker to partly circumvent the same origin policy, which is designed to prevent different websites from interfering with each other.

source: https://portswigger.net/

Now we can go to the target website, we can call it example.com by respecting their privacy.

While browsing through the website using burp suite, I found some open-redirection vulnerabilities, pages vulnerable to clickjacking, page without csrf token and also some other related things.

Most of the vulnerabilities I found on the website were out of scope, so I tried again. The csrf vulnerable page was a password reset page, when I saw it first I thought I can exploit it directly but when I checked the required inputs it requires current password also. After some discussions, I found that if there is password confirmation, then we can’t exploit the csrf directly. So I tried to find other methods to exploit it.

I checked the login page which is vulnerable to clickjacking, and I already have some openredirection also. So I tried to chain it together to a real-life attack scenario.

The summary of the attack was that we redirected to the clickjacking vulnerable login page via openredirection and then the user enters their username and password, it directly passed to the password reset form using javascript which successfully changes the password of the victim to the attacker’s password.

Press enter or click to view image in full size
fake login page creation

Here we used example.com, we can use the original login page here and host it somewhere and redirect it through their own website.

Press enter or click to view image in full size
fake login page

source: https://github.com/shifa123/clickjackingpoc

And when the user enters the credentials, it is directly sent to the password reset form via javascript. We can use the csrf poc generated from burp suite while performing a password reset here and combining it with the page makes everything simple and the password reset will happen at one click after entering the credentials

Get ag3n7’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Program flow:

First goto https://www.example.com/?option=oauthredirect&redirect_url=https://example.com here this redirect to example.com
If we host a fake login page using clickjacking on the login page, we will get the email and current password
login
Then we can sent this to password change form, https://www.example.com/etcetc?etc=abcd&Target=PasswordResetForm&params=test which is vulnerable to csrf attack
When the victim enters email and current password and then click on login, the password will get resetted to attacker given password
Press enter or click to view image in full size
Fake webpage and auto-submitting code snippet
successful
Password Changed Successfully
password reset form

If I left that csrf and clickjacking vulnerabilities when I saw it is out of scope and reported the openredirect only, will not make me satisfied.

So that thought helped me to do this.

Lessons Learnt:
Stay Motivated
Don’t rush yourself
Try to understand things
Don’t Leave Too Early

“Like people says, taste the success once… tongue want more.” — Kapil Dev, 83

:D

Thank You For Reading ….

Happy Hacking and Hunt More !!

Team InitCrew ❤

Follow me on :

Twitter: https://twitter.com/ag3n7apk

Linkedin: https://www.linkedin.com/in/abhijith-pk-ag3n7/
