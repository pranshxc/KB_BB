---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2019-01-07_when-cookie-hijacking-html-injection-become-dangerous.md
original_filename: 2019-01-07_when-cookie-hijacking-html-injection-become-dangerous.md
title: When Cookie Hijacking + HTML Injection become dangerous
category: documents
detected_topics:
- xss
- command-injection
- otp
- csrf
tags:
- imported
- documents
- xss
- command-injection
- otp
- csrf
language: en
raw_sha256: e521f916a7d67f5aa24cd14067a66cb8cc04294a87c61f77c18dbd2ec4a7297a
text_sha256: fee2118e669aee369ce0c9a8bbddcbfbca893c29985319f7e9548865b9eabe53
ingested_at: '2026-06-28T07:31:58Z'
sensitivity: unknown
redactions_applied: false
---

# When Cookie Hijacking + HTML Injection become dangerous

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2019-01-07_when-cookie-hijacking-html-injection-become-dangerous.md
- Source Type: markdown
- Detected Topics: xss, command-injection, otp, csrf
- Ingested At: 2026-06-28T07:31:58Z
- Redactions Applied: False
- Raw SHA256: `e521f916a7d67f5aa24cd14067a66cb8cc04294a87c61f77c18dbd2ec4a7297a`
- Text SHA256: `fee2118e669aee369ce0c9a8bbddcbfbca893c29985319f7e9548865b9eabe53`


## Content

---
title: "When Cookie Hijacking + HTML Injection become dangerous"
url: "https://medium.com/bugbountywriteup/when-cookie-hijacking-html-injection-become-dangerous-3c649f7f6c88"
authors: ["Daniel V. (@d4niel_v)"]
bugs: ["Cookie hijacking", "HTML injection"]
publication_date: "2019-01-07"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5483
scraped_via: "browseros"
---

# When Cookie Hijacking + HTML Injection become dangerous

When Cookie Hijacking + HTML Injection become dangerous
Daniel "V" Morais
Follow
4 min read
·
Jan 8, 2019

221

Hello Friends,

This time, I’ll show how I got an html injection, and how I turned it into a dangerous vulnerability with the cookie hijacking vulnerability.

HTML Injection and Cookie Hijacking:

HTML injection is a type of injection issue that occurs when a user is able to control an input point and is able to inject arbitrary HTML code into a vulnerable web page. This vulnerability can have many consequences, like disclosure of a user’s session cookies that could be used to impersonate the victim, or, more generally, it can allow the attacker to modify the page content seen by the victims.

The Session Hijacking attack consists of the exploitation of the web session control mechanism, which is normally managed for a session token.

Discovery Phase:

This time I had to perform manual tests on each input on the customer information screen. I noticed that the inputs were not being validated as expected, but how to exploit this type of vuln, since it’s necessary to log into the account to “activate” the HTML code?

First attempt: Try to exploit the CSRF login vulnerability, where the attacker sends a customized code to the victim to log into the attacker’s own account. Something like this:

<html>
  <! - CSRF Login PoC ->
  <body>
  <script> history.pushState ('', '', '/') </ script>
  <form action = "https://private-company.com/account/signin" method = "POST">
  <input type = "hidden" name = "customerlogin" value = "attacker-email@gmail.com" />
  <input type = "hidden" name = "customerpassword" value = "attacker-password" />
  <input type = "submit" value = "Submit request" />
  </ form>
  </ body>
</ html>

The code above wasn’t successful because the company already handled the logins of its clients through tokens.

Second attempt:

Cookie Hijacking! the attack was successful because the token that managed users session didn’t expire after the logout function. The cookies continued in the browser until it was cleaned manually. I’ll show it below:

I logged in with a test account and then I clicked “logout”. Note in the screenshot below that cookies were still stored in the browser after the logout:
Press enter or click to view image in full size

2. Note the expiration of the cookie that manages client sessions is one year.

Get Daniel "V" Morais’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

3. I copied the cookies with a tool (edit this cookie), accessed the browser Mozilla Firefox, added the cookie manually with the values that were in the previous screenshot and… done! I was redirected to the victim’s profile.

Great results! Time to practice Html Injection and combine the vulns for more effective demonstration.

As previously explained, the parameter “customer_name” was vulnerable to html injection. To confirm the existence of the failure, I intercepted the request with burp suite and inserted an H1 tag in the name:

Press enter or click to view image in full size

After the payload, i sent a password recovery mail to my own account:

Press enter or click to view image in full size

Vulnerability successfully confirmed!

Possibilities:

As the name parameter was vulnerable to HTML Injection, it became possible to customize an html code to look like a form, which would be visible only to the user, right? Perhaps…

Let’s remember that there’s also a cookie hijacking vuln, where it allows the attacker to capture the cookies stored in the browser and log into the victim’s account. IF the application is accessed in public environments such as LAN houses, then there are several ways to exploit the vulnerability.

Victim logs into his account at a LAN house. After performing an operation on the company’s application, victim leaves the account throught logout function.
Attacker accesses the same public computer as the victim, captures the cookies and login into the victim’s account.
Attacker customizes a new HTML code and inserts in the vulnerable field.
Victim upon re-accessing the account (on another device) begins to see the “new page” that the attacker has customized.

Of course, this would require interaction of the victim itself, however, the famous phishing attacks would be much more effective.

That’s it, hackers! Hope you liked it.

Find me at Linkedin.
