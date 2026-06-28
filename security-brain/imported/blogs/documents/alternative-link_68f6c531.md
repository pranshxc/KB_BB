---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-02-26_alternative-link.md
original_filename: 2021-02-26_alternative-link.md
title: Alternative link
category: documents
detected_topics:
- password-reset
- idor
- xss
- sqli
- command-injection
- otp
tags:
- imported
- documents
- password-reset
- idor
- xss
- sqli
- command-injection
- otp
language: en
raw_sha256: 68f6c531a79aca237c6bb899e6a790002499fe454ab517aa415f1eacb7949406
text_sha256: 1e44c85918e96d4ee402c3c0c904608fe280d7e1405246681b2deae7d1325806
ingested_at: '2026-06-28T07:32:05Z'
sensitivity: unknown
redactions_applied: true
---

# Alternative link

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-02-26_alternative-link.md
- Source Type: markdown
- Detected Topics: password-reset, idor, xss, sqli, command-injection, otp
- Ingested At: 2026-06-28T07:32:05Z
- Redactions Applied: True
- Raw SHA256: `68f6c531a79aca237c6bb899e6a790002499fe454ab517aa415f1eacb7949406`
- Text SHA256: `1e44c85918e96d4ee402c3c0c904608fe280d7e1405246681b2deae7d1325806`


## Content

---
title: "Alternative link"
page_title: "Password Reset Token Leak via X-Forwarded-Host | by Saajan Bhujel | InfoSec Write-ups"
url: "https://infosecwriteups.com/password-reset-token-leak-via-x-forwarded-host-4ed3e33dca31"
authors: ["Saajan Bhujel (@saajanbhujel)"]
bugs: ["Host header injection", "Account takeover", "Password reset"]
bounty: "1,000"
publication_date: "2021-02-26"
added_date: "2022-10-17"
source: "pentester.land/writeups.json"
original_index: 3867
scraped_via: "browseros"
---

# Alternative link

Top highlight

Password Reset Token Leak via X-Forwarded-Host
Saajan Bhujel
Follow
4 min read
·
Feb 26, 2021

1.3K

16

Hi everyone,

I am Saajan Bhujel.

Student of Bachelor of Commerce(B.Com) and also I am a Bug Bounty Hunter.

Press enter or click to view image in full size

This is my 1st blog, if you find any spelling mistakes, so please bear with me for the next few minutes. And this blog is about a vulnerability that, I was able to find in the Hackerone’s private program which allows me to take over any user’s account. But before starting this blog I would like to give a piece of small basic information about the Host header.

What is the HTTP Host header?

The HTTP Host header is a mandatory request header as of HTTP/1.1. It specifies the domain name that the user wants to access.

For example, if a user visits https://example.com, then their browser will make a request containing a Host Header as below:

GET / HTTP/1.1

Host: example.com

Now let’s start the blog….

Some days ago I got a notification in Hackerone that said that I had been invited into a private program. So I accept that invitation and start hunting on that Private Program. And in the starting of hunting on that private program, I spend 5–6 days finding Cross-Site-Scripting(XSS), IDOR, SQL injection, Flaw on the login page, Information Disclosure, and Subdomain takeover but still, I was not able to find anything.

After taking some hours of break, again I start hunting on that domain but this time I got an interesting functionality which I did not saw at last time. And that interesting functionality is Password Reset functionality. So I thought to myself let's play with this Password Reset functionality.

I can’t disclose the name of the target because it's a private program. So, Let’s suppose that the target is site.com. And their password reset functionality is something like this:

And I noticed that whenever we enter our email and click on reset password. we got an email for changing the password with a password reset token link.

Get Saajan Bhujel’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Password Reset Token link looks like this:

https://site.com/action-token?key=eyJhbGciOiJIUzI1NiIsI***REDACTED-SUSPECT-TOKEN***This time I decided to intercept the password reset request and I also started my ngrok server.

The original request is something that looks like this:

Press enter or click to view image in full size

Then I added another header “X-Forwarded-Host” with my ngrok server domain in the original request. So now the modified request is something that looks like this:

Press enter or click to view image in full size

Now this time I got an email for changing the password but with my ngrok server domain. And the password reset token link looks like this:

https://95saf4ct71g.ngrok.io/action-token?key=wia2lkI***REDACTED-SUSPECT-TOKEN***You also can see, I am successfully able to change the Host by simply adding the header “X-Forwarded-Host” in the password reset request.

Then I noticed that If I enter the victim’s email in the password reset page and also intercept that request and if I add another header “X-Forwarded-Host” with my malicious domain. Then victim will get an email of the password reset token link with my malicious domain. And when the victim clicks on that link he will redirect to my website and his all token will leak to me. Then I can change the victim’s password by using his leaked token. Yeah, the Impact of this vulnerability is a full account takeover.

So now I can fully take over anyone’s account who has an account on site.com by resetting their password.

So without wasting any time, I successfully submitted this vulnerability with full proof of concept and then, Hackerone’s private program rewarded me with $1000.

Thank you for reading this blog, and I hope you learn something.

Enjoy your day!….
