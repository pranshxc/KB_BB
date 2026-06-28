---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2018-11-19_how-i-hacked-netflix-users-use-it-free-forever.md
original_filename: 2018-11-19_how-i-hacked-netflix-users-use-it-free-forever.md
title: How I Hacked Netflix users & Use it free forever
category: documents
detected_topics:
- access-control
- xss
- command-injection
- automation-abuse
- race-condition
- api-security
tags:
- imported
- documents
- access-control
- xss
- command-injection
- automation-abuse
- race-condition
- api-security
language: en
raw_sha256: 4c62feee1946c679544f6fde59dc9ea97105704b7f18303a1acbba4cf6713f8a
text_sha256: bc1630207ee87d7545c5ab865835a705b1a8a826cc1ebc81b965fc976b226b74
ingested_at: '2026-06-28T07:31:58Z'
sensitivity: unknown
redactions_applied: false
---

# How I Hacked Netflix users & Use it free forever

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2018-11-19_how-i-hacked-netflix-users-use-it-free-forever.md
- Source Type: markdown
- Detected Topics: access-control, xss, command-injection, automation-abuse, race-condition, api-security
- Ingested At: 2026-06-28T07:31:58Z
- Redactions Applied: False
- Raw SHA256: `4c62feee1946c679544f6fde59dc9ea97105704b7f18303a1acbba4cf6713f8a`
- Text SHA256: `bc1630207ee87d7545c5ab865835a705b1a8a826cc1ebc81b965fc976b226b74`


## Content

---
title: "How I Hacked Netflix users & Use it free forever"
url: "https://medium.com/@vignesh4303/how-i-hacked-netflix-users-use-it-free-forever-9febb1427262"
authors: ["Blueberryinfosec (@bbinfosec)"]
programs: ["Netflix"]
bugs: ["Cookie injection", "Privilege escalation"]
publication_date: "2018-11-19"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5572
scraped_via: "browseros"
---

# How I Hacked Netflix users & Use it free forever

How I Hacked Netflix users & Use it free forever-
Bbinfosec
Follow
7 min read
·
Nov 19, 2018

51

2

Pre Note : The following blogpost is about netflix vulnerability which was closed as won’t Fix and disclosing it under standard terms.I decided to disclose it since the team decided as wont fix.

Note : Title might be misleading.For better explanation i kept the title.

Bug :

Cookie injection,Reuse of cookie will lead to privilege escalation and bypass of Basic Netflix plans.

Abstract :

What is cookie & what is cookie injection?

Cookies are small files which are stored on a user’s computer. They are designed to hold a modest amount of data specific to a particular client and website, and can be accessed either by the web server or the client computer. This allows the server to deliver a page tailored to a particular user, or the page itself can contain some script which is aware of the data in the cookie and so is able to carry information from one visit to the website (or related site) to the next.

Cookie Injection :

The majority of web applications are based on an authentication mechanism that enables to define user privileges. This mechanism is based on sessions. It defines cookies which validity period depends on the parameters. If the controls are only based on these cookies, the application is likely to be vulnerable, since cookies are saved on local machines. Hence, it is easy to modify their values or manually create new cookies.

The basic rule of security would be handling up secure cookies and cookies should expire whenever session is closed out .

Cookie Security Some basic rules :

Cookies should not be reused.
Cookies should be randomized.
Cookies should expire on post logout.
Cookies should have proper server side validations.
Cookies should have proper attributes like no cache,no store,etc.
Send The Cookie To Only Your Application
Don’t Share Cookie With Sub Domains
Require a Secure Connection
Protect Against XSS Exploits

Bug Bounty rules & out of scope :

Most of the bug bounty programs leave/skip cookie injection since its basically client side attack ,i.e it’s carried based on user interaction.

For instance netflix bug bounty exceptions clearly states that it as out of scope .

Whats the bug :

Netflix permits reuse of cookies and their cookies wont expire even when user session gets logged out.Reuse of cookies would leave you to gain access to any paid netflix user account without their credentials.

Steps to replicate/reproduce-Noob Way :

You might need any cookie editor of your favorite browser
Go to your friends account export his/her cookie ,save it as json
Now come to your computer import the json.

Steps to reproduce PT way[If request does not use HTTP ONLY,There are few areas where httponly is not implemented] :

Send a xss hook of a vulnerable website[e.g beef]
Capture the victims cookie.
Import & enjoy the free netflix.

Alternatively it might be weird ask your paid friend to send cookies for u and capture http cookies in any proxy tool[like Burp] repeat the request.

How Cookies Work

Cookies are simply key/value pairs that let us get around HTTP being a stateless protocol. When a developer has data they wish to last for more than one connection they can use cookies to store that data on the client side. While this tends to get handled by the programming language being used it is accomplished using HTTP headers.

When the server wants to set a cookie it passes back a header named “Set-Cookie” with the key-value pair and some options.

On subsequent requests the client will send along its own header to let the server know the name and value of its stored cookies. The server will not continue to send back the cookies, it will only send them if there is a change.

You can see all the headers for yourself using the LiveHeaders plugin for Firefox.

The Problem

This data is completely in control of the client- it is trivial to change the values of a cookie. That means that, just like post and get data, all cookie data must be validated in some way. At the same time you’ll want to avoid storing sensitive information, such as passwords, as cookies are stored in cleartext and anyone with access to the computer later can easily pick those up (I know of at least one security forum that was hacked in this way). It is also important to note that HTTP does not encrypt the headers in any way. If the connection isn’t over SSL then it will not be protected from snooping eyes.

Session cookies are no different than any other cookie- their value is just a simple ID. Those IDs are susceptible to all of the same limitations as other cookies. The real power behind sessions happens server side, where the ID is used to pull out data stored on the server. This has many benefits over storing data directly into the cookie itself- data can’t be manipulated by the user, large amount of data can be stored without having to send it back and forth with each request, and you can store data you otherwise wouldn’t want the client to have access to.

How To Bypass HTTPONLY[Source Nateixm] :

Before entering the heart of the matter, it is important to distinguish the difference between a simple Cookie and a HttpCookie since is really two completely different concepts. Basically a cookie is data sent by a web server and stored in a text file through a web browser, it can also be manipulated with JavaScript code or HTTP headers during the replies from a web server.

An HttpOnly Cookie has the distinction of being only accessible via HTTP(s), access to this element is restricted to all non-HTTP connection such as JavaScript. HttpOnly cookies are commonly used to store authentication information in order to protect them against XSS Attacks, this article aims to show you how it is possible to circumvent this protection, and also how to deal with this kind of attack.

First Example

Set-Cookie: <name>=<value>[; <max -Age>=<age>]
[; expires=<date>][; domain=<domain_name>]
[; path=<some_path>][; secure][; HttpOnly]
</some_path></domain_name></date></age></max></value></name>
set-Cookie: wordpress_f8bee1a788233546681a64908c37c3a0=admin|134982|876946033fb3e2e16f2810d55945ddb4ce29; Expires=Wed, 09 Jun 2021 10:18:14 GMT; domain=www.test.org; path=/; Secure

If we execute the following JavaScript code : <script>alert(document.cookie)</script> Your browser will return and display the cookie

Get Bbinfosec’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Second Example

Set-Cookie: wordpress_f8bee1a788233546681a64908c37c3a0=admin|134982|876946033fb3e2e16f2810d55945ddb4ce29; Expires=Wed, 09 Jun 2021 10:18:14 GMT; domain=www.test.org; path=/; Secure; HttpOnly

Now if we execute once again the following JavaScript code : <script>alert(document.cookie)</script>

The result will be a dialog box displaying a blank message, in fact the flag HttpOnly Cookies makes inaccessible JavaScript. How-ever, it is possible in some cases to bypass this protection and extract the contents of these cookies.

Some Notes & References why httponly wont address the issue :

https://medium.com/@yassergersy/xss-to-session-hijack-6039e11e6a81

Why HttpOnly Won't Protect You
Before going in depth criticizing the HttpOnly session protection mechanism I better explain what it is and why it is…

www.gnucitizen.org

POC how to steal httponly session cookies with XSS using apache cookie overflow (CVE-2012-0053)
The basis of this attack is a known Apache vulnerability ( CVE-2012-0053) which leaks all cookies (including HttpOnly…

blog.x1622.com

SecurityFocus
SecurityFocus is designed to facilitate discussion on computer security related topics, create computer security…

www.securityfocus.com

Cookie Stealing script : https://pastebin.com/17M79Mu3 if its Apache.

Few Updates After Feedback from my friends :

There is HTTP ONLY attribute to secure up the session ,why i need to bother it about :
A cookie flagged Secure is only sent to the server if the connection is secure (i.e. HTTPS). That is, a man-in-the-middle attacker can't capture them by intercepting a plain HTTP connection to your site.
A cookie flagged HttpOnly is not accessible to scripts. That is, an XSS vulnerability on your site wouldn't allow an attacker to directly exfiltrate a HttpOnly cookie via Javascript's document.cookie.
Additional to it If a website is enabled with TRACE httponly it can be beated.
HttpOnly restricts all access to document.cookie in IE7, Firefox 3, and Opera 9.5 (unsure about Safari)
HttpOnly removes cookie information from the response headers in XMLHttpObject.getAllResponseHeaders() in IE7. It should do the same thing in Firefox, but it doesn't, because there's a bug.
XMLHttpObjects may only be submitted to the domain they originated from, so there is no cross-domain posting of the cookies.
Some additional references :

a)https://fscked.org/talks/ActiveHTTPSCookieStealing.pdf

b)https://blog.codinghorror.com/protecting-your-cookies-httponly/

c)Grease monkey script : https://greasyfork.org/en/scripts/17580-netflix-import-cookie/code

2.If you were sending up xss hook via beef you cannot steal up whole user session :

Once you own the browser ,we can do anything :)

Attack chain & Its impacts :

Alice sends vulnerable request to catch bob’s cookies and reuses it forever.Since cookies does not expire at browser side it can be used forever.

Impacts :

Privilege escalation
Bypass of limited users plan
You can buy netflix as one user and share it to as many users u can.

Why it cannot be controlled :

Users can be tracked via login sessions whereas we cannot track users based on cookies

How you can secure yourself :

Dont fall for false popups.
Always check on your concurrent login.
More importantly Never reuse your passwords & Never keep weak passwords.

Proof Of Concept :

Sample Cookies which you can test :

https://pastebin.com/Wq5MW5RG

Disclosure Timeline :

9th November 2018 : Issue reported to Netflix through bug crowd.
13th November 2018 : Closed as out of scope.
13th November 2018 : Explained attack chain with proof video.
14th November 2018 : Contacted Bug crowd support
15th november 2018 : Wont fix confirmed by bug crowd team
19th November 2018 : Public Disclosure through medium blog
