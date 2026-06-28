---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-01-08_bypass-samesite-cookies-default-to-lax-and-get-csrf.md
original_filename: 2020-01-08_bypass-samesite-cookies-default-to-lax-and-get-csrf.md
title: Bypass SameSite Cookies Default to Lax and get CSRF
category: documents
detected_topics:
- api-security
- oauth
- command-injection
- csrf
tags:
- imported
- documents
- api-security
- oauth
- command-injection
- csrf
language: en
raw_sha256: a4d9523424ce8cb4d35d7edeaf6fd2edbb34a3d7629f923e6194e053e67be331
text_sha256: 8421de1c1b44ce6f96a404c94ee957e47afc4e534469bcf54f768071e14c5ddf
ingested_at: '2026-06-28T07:32:01Z'
sensitivity: unknown
redactions_applied: false
---

# Bypass SameSite Cookies Default to Lax and get CSRF

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-01-08_bypass-samesite-cookies-default-to-lax-and-get-csrf.md
- Source Type: markdown
- Detected Topics: api-security, oauth, command-injection, csrf
- Ingested At: 2026-06-28T07:32:01Z
- Redactions Applied: False
- Raw SHA256: `a4d9523424ce8cb4d35d7edeaf6fd2edbb34a3d7629f923e6194e053e67be331`
- Text SHA256: `8421de1c1b44ce6f96a404c94ee957e47afc4e534469bcf54f768071e14c5ddf`


## Content

---
title: "Bypass SameSite Cookies Default to Lax and get CSRF"
url: "https://medium.com/@renwa/bypass-samesite-cookies-default-to-lax-and-get-csrf-343ba09b9f2b"
authors: ["Renwa (@RenwaX23)"]
bugs: ["CSRF", "Samesite cookie bypass"]
publication_date: "2020-01-08"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4836
scraped_via: "browseros"
---

# Bypass SameSite Cookies Default to Lax and get CSRF

Top highlight

Bypass SameSite Cookies Default to Lax and get CSRF
Renwa
Follow
5 min read
·
Jan 8, 2020

431

1

Press enter or click to view image in full size
SameSite cookies, source:web.dev

SameSite Cookies the new cookie attribute that everyone is talking about, it can be used to prevent SOP bypasses and CSRF attacks. but first let's look what is it actually.

SameSite is a cookie attribute which you can tell the browser to when it should send the specific cookie in a cross origin request, it has 3 types:

SameSite None Will be sent in all cross origin requests it will be treated as normal (old) cookies
SameSite Lax Will be sent only in GET request in top window navigations such as <a> tag, window.open()..
SameSite Strict Will be sent only when the user types the website in the URL bar and presses enter

Learn more: https://web.dev/samesite-cookies-explained/

As from now Chrome 79 default cookies without SameSite will be treated as None cookies but this gonna change soon, From Chrome 80 which comes in February 4.
Cookies without SameSite attribute will be treated as Lax, that means cookies will be sent only in top window navigations and only GET requests. This might
be a good move to solve many POST CSRF attacks.

But there is something about those cookies they have a special feature called LAX+POST, from Chrome:

Chrome will make an exception for cookies set without a SameSite attribute less than 2 minutes ago. Such cookies will also be sent with non-idempotent (e.g. POST) top-level cross-site requests despite normal SameSite=Lax cookies requiring top-level cross-site requests to have a safe (e.g. GET) HTTP method.

That means if a cookie is been set or changed within 2 minutes the browser will sent the cookie in a POST request and it will be treated as None (only top window navigations) but after the 2 minutes it will become normal as Lax.

Press enter or click to view image in full size
Lax+POST

This has been used to not break the web and login flows but also bring us a new attack surface, it allow us to bypass SameSite Lax by default and get a CSRF. According to the policy if a cookie is not older than 2 minutes it will be sent, How this gonna be abused in real world applications?

1.
Some websites might change the session cookie from time to time then all we need is to open a new window pointing to the website, user’s session will be replaced by a newer one then we can have a CSRF attack.

2.
Cookie sessions will expire after some period and the user needs to get a new session:

The attacker will open a new window pointing to the login page
Victim will login to the site and will get a new session
Attacker then can perform CSRF attacks because the cookie is just been set (not older than 2 minutes)

3.
Most applications use GET request for logout function and in a top window GET request cookies with Lax will be sent that means we will have a logout CSRF that will make the cookie removed or changed.

Attacker will open a new window pointing to the logout page
Victim opens the logout page and his cookies will be changed or removed
Attacker will open a new window pointing to the login page and the user logs in
Attacker can perform CSRF attacks

4.
Getting the user to login again to a website is something not efficient and require a lot of interactions, but we have a saviour (Oauth), most of the websites today have 2nd way option login which uses other providers, so if we have Logout CSRF and Oauth login then we can bypass SameSite Lax by default with less interaction.

Attacker will open a new window pointing to the logout page
Victim open the logout page and his sessions will be removed
Attacker opens a new window pointing to the Oauth login page (example.com/login/oauth/facebook)
Victim will auto re-login to the application and a new session will be set
Attacker can perform CSRF attacks because the cookie is not older than 2 minutes

5.
Some applications might have an option to get a new session for some reasons, then we need somehow get the victim to click that (New Session) button or if the website uses some REST api we can just open a new window pointing to (example.com/user/new_session) then get CSRF

Get Renwa’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

LAX+POST (2 minute) is a temporary thing and will be removed in future depending on when developers change their login session flows to SameSite None Secure, or use another method for cross origin requests, another case is lowering the time to 10 seconds (This will still make it possible to abuse)

A while ago i made a small challenge based on this behaviour

It has 3 main functions:

Login Sets the cookie to (session=username)

Logout Sets the cookie to (session=)

Settings sends a POST request to settings.php to change the username (session=new username), if the session cookie is not present in the POST request the file will throw a CSRF error.

This challenge is based on 3rd scenario which the application uses GET request to logout function, what we need to do is sending a request to logout.html which changes the cookie to (session=), then the browser will know the cookie is changed and the 2 minute feature will work therefore for further requests within 2 minutes the session cookie will be sent along

We can’t use cross-origin requests to change the cookie, because of a new Chrome feature

Press enter or click to view image in full size

We need to open the logout.html in a new top window then submit the POST request to settings.php, solution:

https://renwax23.github.io/X/csrf-samesite/solution.html

Press enter or click to view image in full size
Solution source code

One click user interaction is required to open a new window.

Press enter or click to view image in full size

Challenge source code: https://github.com/RenwaX23/X/tree/master/csrf-samesite

To conclude SameSite is a great browser feature that can prevent wide range of client-side attacks but it’s not a bulletproof technique to depend on, this temporary Lax+POST will be a new way to bypass those cookies are sent without any SameSite attribute and also might be removed soon.

SameSite updates

Thanks

Renwa
