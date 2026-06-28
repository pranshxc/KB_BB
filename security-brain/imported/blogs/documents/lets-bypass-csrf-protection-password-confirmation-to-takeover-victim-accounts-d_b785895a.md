---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-06-12_lets-bypass-csrf-protection-password-confirmation-to-takeover-victim-accounts-d.md
original_filename: 2020-06-12_lets-bypass-csrf-protection-password-confirmation-to-takeover-victim-accounts-d.md
title: Let’s Bypass CSRF Protection & Password Confirmation to Takeover Victim Accounts
  :D
category: documents
detected_topics:
- csrf
- xss
- command-injection
- password-reset
- otp
- automation-abuse
tags:
- imported
- documents
- csrf
- xss
- command-injection
- password-reset
- otp
- automation-abuse
language: en
raw_sha256: b785895a27fe76231a1bc66f7e21b796b45a56d2307af0509872d9a96eff04fe
text_sha256: 99042eee837367eea33b019f3d69bb46d9bab1a9fe87e6ec4219135cc990d8e6
ingested_at: '2026-06-28T07:32:02Z'
sensitivity: unknown
redactions_applied: true
---

# Let’s Bypass CSRF Protection & Password Confirmation to Takeover Victim Accounts :D

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-06-12_lets-bypass-csrf-protection-password-confirmation-to-takeover-victim-accounts-d.md
- Source Type: markdown
- Detected Topics: csrf, xss, command-injection, password-reset, otp, automation-abuse
- Ingested At: 2026-06-28T07:32:02Z
- Redactions Applied: True
- Raw SHA256: `b785895a27fe76231a1bc66f7e21b796b45a56d2307af0509872d9a96eff04fe`
- Text SHA256: `99042eee837367eea33b019f3d69bb46d9bab1a9fe87e6ec4219135cc990d8e6`


## Content

---
title: "Let’s Bypass CSRF Protection & Password Confirmation to Takeover Victim Accounts :D"
url: "https://medium.com/bugbountywriteup/lets-bypass-csrf-protection-password-confirmation-to-takeover-victim-accounts-d-4a21297847ff"
authors: ["Harsh Bothra (@harshbothra_)"]
bugs: ["CSRF"]
publication_date: "2020-06-12"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4506
scraped_via: "browseros"
---

# Let’s Bypass CSRF Protection & Password Confirmation to Takeover Victim Accounts :D

Top highlight

Let’s Bypass CSRF Protection & Password Confirmation to Takeover Victim Accounts :D
Harsh Bothra
Follow
3 min read
·
Jun 12, 2020

1.5K

3

Press enter or click to view image in full size

Cross-Site Request Forgery (CSRF) is hardly seen with new frameworks but is yet exploitable like old beautiful days. CSRF, a long story short is an attack where an attacker crafts a request and sends it to the victim, the server accepts the requests as if it was requested by the victim and processes it. To mitigate this there are multiple protection mechanisms that are getting deployed and one we are going to deal with is Anti-CSRF Token.

Hi Fellow Hackers & Security Enthusiasts, Today I am going to write how I was able to Bypass CSRF Protection to Execute a successful CSRF attack and further with help of Client-Side Validation Bypass, I was able to perform a Full Account Takeover by changing Password. Before starting with the attack scenario, let’s see more about the Anti-CSRF Tokens and Probable Bypasses.

If you enjoy reading my articles, do follow on Twitter: https://www.twitter.com/harshbothra_

Anti-CSRF Tokens are a way that allows the server to uniquely distinguish who actually requests the resource/action to be performed saving against CSRF attacks. However, due to weak implementation in the application, there are several ways to bypass Anti-CSRF Tokens such as:

Remove Anti-CSRF Token
Spoof Anti-CSRF Token by Changing a few bits
Using Same Anti-CSRF Token
Weak Cryptography to generate Anti-CSRF Token
Guessable Anti-CSRF Token
Stealing Token with other attacks such as XSS.
Converting POST Request to GET Request to bypass the CSRF Token Check. (This is what we will see for this article)

P.S.: There may be other bypasses available. I mentioned some I remembered on the Top of my Head. If you know any other, Please drop in Responses to help the Readers or maybe leave a note so that I can update this list with proper credits. :)

So let’s call the target as target.com. After fiddling across with the application, I found /editprofile endpoint which has the request like this:

POST /editprofile HTTP/1.1
Host: target.com
<redacted>
username=test&description=<some_text>&phone=1231231231&anti_csrf=<token>

Since you can observe that the anti_csrf token is present and the server is validating if the Token is missing or forged. So basically no luck. Then I simply changed the Request Method from POST to GET & removed anti_csrf parameter and forged request looked like:

GET /editprofile?username=test&description=<some_text>&phone=1231231231 HTTP/1.1
Host: target.com
<redacted>

And we were able to bypass it successfully. CSRF exploited.

But, wait, it has low severity because we are still not able to do much other than changing some profile information. After looking for more stuff, I checked Password Reset Functionality but again it was asking for the Current Password before being able to change the password. So the original Password change request looks like this:

POST /changepassword HTTP/1.1
Host: target.com
<redacted>
current_password=***REDACTED***

So, I simply removed the current_password field and it successfully reset the password.

Get Harsh Bothra’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

So now we have two things:

Way to Bypass and Perform Bypass
Way to Bypass Current Password on Password Change

Now, we can simply chain the issues to change the password of victim user using CSRF, the forged request will look like:

GET /changepassword?new_password=***REDACTED*** HTTP/1.1
Host: target.com
<redacted>

Simply use Burp Suite to generate a CSRF PoC or you may use your own way to do it and send it to the victim. Once the victim navigates to the attacker's crafter URL, his password will be changed.

Initial Severity of Medium is now HIGH.

Takeaways:
Never Ignore Low-Hanging Vulnerabilities as they can be used to increase the impact to a good extent.
Ways to bypass CSRF protection.
Never Giving up on learning something new.

If you enjoyed reading the article do clap and follow on Medium and Twitter:

Twitter: https://www.twitter.com/harshbothra_

LinkedIn: https://www.linkedin.com/in/harshbothra

Website: https://harshbothra.tech
