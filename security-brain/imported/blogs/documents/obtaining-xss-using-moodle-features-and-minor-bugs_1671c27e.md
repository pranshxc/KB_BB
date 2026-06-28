---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2019-04-09_obtaining-xss-using-moodle-features-and-minor-bugs_2.md
original_filename: 2019-04-09_obtaining-xss-using-moodle-features-and-minor-bugs_2.md
title: Obtaining XSS Using Moodle Features and Minor Bugs
category: documents
detected_topics:
- sso
- xss
- command-injection
- otp
- automation-abuse
- cors
tags:
- imported
- documents
- sso
- xss
- command-injection
- otp
- automation-abuse
- cors
language: en
raw_sha256: 1671c27ef2b59e1fca5c94376d0983609b834eae9c5df07ef20c5b830e4cf722
text_sha256: 18bb26b5e1e18f3954e179fcce908b967423c59c19bec57ea68511d4b3cd2497
ingested_at: '2026-06-28T07:31:59Z'
sensitivity: unknown
redactions_applied: true
---

# Obtaining XSS Using Moodle Features and Minor Bugs

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2019-04-09_obtaining-xss-using-moodle-features-and-minor-bugs_2.md
- Source Type: markdown
- Detected Topics: sso, xss, command-injection, otp, automation-abuse, cors
- Ingested At: 2026-06-28T07:31:59Z
- Redactions Applied: True
- Raw SHA256: `1671c27ef2b59e1fca5c94376d0983609b834eae9c5df07ef20c5b830e4cf722`
- Text SHA256: `18bb26b5e1e18f3954e179fcce908b967423c59c19bec57ea68511d4b3cd2497`


## Content

---
title: "Obtaining XSS Using Moodle Features and Minor Bugs"
url: "https://medium.com/@daniel.thatcher/obtaining-xss-using-moodle-features-and-minor-bugs-2035665989cc"
authors: ["Daniel Thatcher (@_danielthatcher)"]
programs: ["Moodle"]
bugs: ["Login CSRF", "XSS"]
publication_date: "2019-04-09"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5321
scraped_via: "browseros"
---

# Obtaining XSS Using Moodle Features and Minor Bugs

Obtaining XSS Using Moodle Features and Minor Bugs
Daniel Thatcher
Follow
6 min read
·
Apr 9, 2019

141

3

Moodle allowed users to embed arbitrary HTML in their own dashboards, which are only visible to themselves, creating a situation which is equivalent to self-XSS. In this blog post I describe how it was possible to exploit this by setting a second session cookie with a restricted path, initially in combination with login CSRF, and then by using Moodle’s builtin impersonation functionality, to target other users. While much of the previous exploitation of self-XSS only allows the attacker to obtain read-only access to the DOM, this technique allows JavaScript to be run as the victim user, as with any regular XSS.

The following video shows how an administrator can be targeted to give an attacker shell access to the Moodle server. In this video, an administrator follows a link sent to them by an attacker. The next time the administrator logs in to their account in the same browser, a malicious plugin which gives the attacker a shell on the web server is uploaded using JavaScript.

Targeting an administrator to upload a malicious plugin
Introduction

A while ago I came across some interesting techniques for exploiting self-XSS in combination with other issues, so when I noticed the following in a Moodle security announcement I was very interested:

Authenticated user[sic] are allowed to add HTML blocks containing scripts to their Dashboard and this is normally not a security issue because personal dashboard is visible to this user only.

While this is more of a feature than it is stored self-XSS, it does create an equivalent situation as users are able to insert arbitrary HTML and JavaScript which is run in the context of the target domain, but should only ever be rendered in their browser.

The login form also had no CSRF protection, making it possible to use the techniques I mentioned to obtain read-only access to any page a victim user is able to view. This did not allow anything of great interest to be leaked from a Moodle installation with minimal extra configurations (perhaps due to my lack of knowledge of Moodle), so I looked for ways to turn this into full XSS where I could run arbitrary JavaScript as a victim user.

Double Session Cookies

The method I came up with takes advantage of the way that PHP and browsers treat multiple cookies with the same name.

PHP

I found that if two session cookies are sent in a request to Moodle, the first session cookie which appears in the Cookie header is used, while the second is ignored. So, in the request below, the session cookie highlighted in bold is used to identify the logged in user, while the other session cookie of the same name is ignored:

GET /my/ HTTP/1.1
...
Cookie: MoodleSession=0ab0af2b5369369af1fae6b097cf64f7; MoodleSession=***REDACTED-SUSPECT-TOKEN***This is a result of PHP’s behaviour for handling multiple cookies, which leads to only the first cookie being present in the $_COOKIE superglobal.

Browsers

Chrome and Firefox¹ will generate a request containing duplicate cookies, such as the one above, when different values of the same cookie are set with different paths. So, say there are two cookies are set in the browser:

a cookie named MoodleSession with a path of / containing a session identifier associated with Alice’s account; and
a cookie named MoodleSession with a path of /my/ containing a session identifier associated with Bob’s account.

This will lead to only Alice’s session cookie being sent in requests to paths outside of /my/, and both session cookies being sent in requests to /my/, which is the path of the user’s dashboard in Moodle. It appears that both Chrome and Firefox will send cookies with more restrictive paths first, so Bob’s session cookie will be the one sent first, and hence used by Moodle, when the browser requests /my/. A user of this browser will see all of the site as though they are logged in as Alice, apart from /my/, which will show Bob’s dashboard.

Exploiting

The combination of CSRF on the login form and the double session cookie behaviour gives us all we need to target other users with JavaScript embedded on our dashboard. The setup I’m using is a Moodle installation located at http://moodle.lab.local, which contains an administrator account named admin, and a low privileged account which the attacker has access to, named attacker. There is also a server belonging to the attacker at attacker.lab.local. All the files used are available in this GitHub repository.

1. Setup

First the attacker embeds a script such as the one from the GitHub repository, part of which is shown below, in their dashboard. This is most easily done by adding a new HTML block and using an intercepting proxy such as BurpSuite.

The first stage of the moodle.js script.

This script will check if a cookie named poisoned is set in the browser. If it is not, it will set this cookie, and requests a session cookie belonging to the attacker account from the cookie.php script² which it then puts in the MoodleSession cookie with a path of /my/. The script then causes a logout from the attacker account, which does not invalidate the newly set session cookie as it involves requests to path outside of /my/.

Get Daniel Thatcher’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

If the poisoned cookie is present then the script will execute the final XSS payload, which I will discuss later.

2. Attack

The attacker now targets their victim user, in this case the owner of the admin account, with a simple login CSRF payload such as the one below which logs the victim in to the attacker account.

Login CSRF to force a user to be logged in to the ‘attacker’ account.

This will cause the victim to view the dashboard of the attacker account, and the script from the previous subsection to be run in their browser. The victim will then have the poisoned cookie and a session cookie belonging to the attacker account set in their browser with a path of /my/, following which they will be logged out.

The next time the victim logs in to the admin account in the same browser, they will be able to browse all of the Moodle installation apart from their dashboard, including the admin panel, as normal. However, the request to /my/ to load their dashboard will return the dashboard of the attacker account with the included script. This script performs the second stage of the attack due to the presence of the poisoned cookie in the browser.

3. Final payload

Popping an alert box or loading in DOOM doesn’t obviously show impact here as it will show up on the dashboard of the attacker account rather than the admin account. Since we can still make requests to the admin panel as the admin account, I decided to upload a malicious plugin using JavaScript. This plugin gives the attacker a reverse shell using the version.php file.

Targeting an administrator using login CSRF (same video as before)

The JavaScript to do this can be found here. It is long and ugly, as well as a bit noisy, and I won’t go through it. It essentially pulls down the plugin.zip file from the attacker’s server³, and replicates the requests that would be sent if the plugin were to be uploaded through the web interface.

Using the Impersonation Functionality

Initially, Moodle only fixed the CSRF on the login form, though this still allowed the issue to be exploited using Moodle’s impersonation functionality instead. Rather than exploiting login CSRF, an attacker would have to convince an administrator to impersonate their account, causing the administrator to view the attacker’s dashboard. The exact same scripts are then used to exploit this issue.

Targeting an administrator using the impersonation functionality
Disclosure Timeline

2018–08–18: Issue reported to Moodle with details of exploiting using login CSRF.

2018–08–25: Details of exploiting using impersonation functionality added to issue.

2018–10–25: Asked to create a separate ticket for the exploitation using the impersonation functionality.

2018–11–12: Login CSRF patched (Moodle versions 3.1.15, 3.3.9, 3.4.6, 3.5.3). CVE-2018–16854 and MSA-18-0020 assigned.

2019–03–11: Moodle now sets the forceclean parameter to true when in an impersonated session to prevent user controlled JavaScript from being included in user’s dashboards (Moodle versions 3.1.17, 3.4.8, 3.5.5, 3.6.3). CVE-2019–3847 and MSA-19-0004 assigned.

Footnotes

¹ Other browsers untested.

² The attacker’s server must return the header Access-Control-Allow-Origin: * or equivalent along with the result of this script to allow the value to be read by JavaScript cross-domain on line 10.

³ Again this needs to be returned with the Access-Control-Allow-Origin: * header.
