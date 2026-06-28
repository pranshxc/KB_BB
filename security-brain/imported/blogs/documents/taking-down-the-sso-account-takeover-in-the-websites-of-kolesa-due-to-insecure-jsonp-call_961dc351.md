---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-09-28_taking-down-the-sso-account-takeover-in-the-websites-of-kolesa-due-to-insecure-j.md
original_filename: 2020-09-28_taking-down-the-sso-account-takeover-in-the-websites-of-kolesa-due-to-insecure-j.md
title: Taking down the SSO, Account Takeover in the Websites of Kolesa due to Insecure
  JSONP Call
category: documents
detected_topics:
- sso
- command-injection
- otp
- cors
- api-security
- cloud-security
tags:
- imported
- documents
- sso
- command-injection
- otp
- cors
- api-security
- cloud-security
language: en
raw_sha256: 961dc3518f56f17077831484b6b2a18f731ffb302afdc2b092376665fb334b29
text_sha256: 3a6f47b107c48b16c77d446766073e7d6aaafb6af553fd2e81201adcc2b31e39
ingested_at: '2026-06-28T07:32:03Z'
sensitivity: unknown
redactions_applied: false
---

# Taking down the SSO, Account Takeover in the Websites of Kolesa due to Insecure JSONP Call

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-09-28_taking-down-the-sso-account-takeover-in-the-websites-of-kolesa-due-to-insecure-j.md
- Source Type: markdown
- Detected Topics: sso, command-injection, otp, cors, api-security, cloud-security
- Ingested At: 2026-06-28T07:32:03Z
- Redactions Applied: False
- Raw SHA256: `961dc3518f56f17077831484b6b2a18f731ffb302afdc2b092376665fb334b29`
- Text SHA256: `3a6f47b107c48b16c77d446766073e7d6aaafb6af553fd2e81201adcc2b31e39`


## Content

---
title: "Taking down the SSO, Account Takeover in the Websites of Kolesa due to Insecure JSONP Call"
url: "https://medium.com/bugbountywriteup/taking-down-the-sso-account-takeover-in-3-websites-of-kolesa-due-to-insecure-jsonp-call-facd79732e45"
authors: ["Yashar Shahinzadeh (@YShahinzadeh)"]
bugs: ["Account takeover"]
publication_date: "2020-09-28"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4232
scraped_via: "browseros"
---

# Taking down the SSO, Account Takeover in the Websites of Kolesa due to Insecure JSONP Call

Taking down the SSO, Account Takeover in the Websites of Kolesa due to Insecure JSONP Call
Yasho
Follow
4 min read
·
Sep 28, 2020

364

1

Hello, this post is about how I could take-over any account of Kolesa’s websites using Single Sign-On. There was an insecure JSONP call which could break the security of the entire SSO mechanism.

What is JSONP?

JSONP is a method for sending JSON data to other domain.

Can load an external JavaScript object
Does not use the XMLHttpRequest object
Less secure
Bypassed SOP in browsers
Press enter or click to view image in full size
Example of JSONP request/response
Single Sign-On

Information gathering revealed that Kolesa websites use SSO, the authentication server was:

https://id.kolesa.kz
Press enter or click to view image in full size

The websites used SSO were:

https://market.kz
https://krisha.kz
https://kolesa.kz

The general workflow of how SSO works:

Press enter or click to view image in full size

In this authentication model since a domain can not set an authentication cookie for the others, an authentication token should be transferred between the authentication server and other domains. Considering the orange box in the image above, each site should save a cookie after verifying the authentication token. In addition, authentication server also saves its cookie, so after a couple of HTTP requests I found the authentication cookie name for each Kolesa website:

JSONP Call to Handle SSO

The JSONP call is used for further authentications. If a user has already logged-in in any of three websites, a JSONP call is made to authenticate the user in. The reason for this action is the ease of implementation. Since the origins of domains are different, the Kolesa websites should have implemented the Cross Origin Resource Sharing to transfer the authentication, but they’ve decided to use JSONP to avoid CORS setup.

Press enter or click to view image in full size

The point is, once a user is logged in for examplekosela.kz, they have a ccid cookie in id.kolesa.kz, an authentication token to transfer the authentication, and a ssid cookie in kosela.kz. After that, if the user wants to log-in in the other websites, it happens by just a click, since id.kosela.kz has authentication cookie, it immediately generates authentication token and the user will have the corresponded authentication cookie on the website.

Get Yasho’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Based on the picture above, phase 4 shows how the JSONP call is made and how the authentication token can be turned into authentication cookie in a domain. The cause of JSONP call:

Press enter or click to view image in full size

If the user has already been authenticated by id.kolesa.kz, the following response is expected:

HTTP/1.1 200 OK
Server: openresty/1.13.6.2
Date: Mon, 19 Aug 2019 16:43:26 GMT
Content-Type: text/javascript;charset=UTF-8
Connection: close
Expires: Thu, 19 Nov 1981 08:52:00 GMT
Cache-Control: no-store, no-cache, must-revalidate
Pragma: no-cache
Backend-Server: auth-be3.alaps.kz.prod.bash.kz
X-Bug-Bounty: Please report bugs and vulnerabilities to bugs@kolesa.kz
Content-Security-Policy: frame-ancestors 'self' http://webvisor.com https://webvisor.com
Strict-Transport-Security: max-age=31536000
Content-Length: 627
window.xdm = {
  sess: {
  is_authenticated: 1,
  token: 'xG3ROFWcb7pnXSnMr8MkaBvH01pLlCHqn0sPt0PVL6BBWYdQPdvA31tBi6dLB5njv5jhMW3y/cGBMRB9LC/69zv867wweaDhkxX6arGVzYDy2q+J52nkOQJ+62rR9wLPYJGyEpNGWeOBSp12vugXZUPq2RA6FMptbNkGQpJFjAclXSzduj7wJJgAUONMj3mkkElM1nWmIllrl5zDEz6s7077E4ibx//BvnfZ9AIC/9b2PB+QzVKOnSzzcr9wSXqta9TEDHvjopqbUd4UE2xSMRSj/zxPQlCba5632hcIXnzZB3A8fvahvf2Hm5ssuC+cwuKU8pAdE/qcGQSJKdhpYXxntGkQiLdEAliyCq+fahS4itb6HlFH/+H20RsZA+cjyaF7ntnW5tYY31vxJXovrR3oinaj9YDSzoCZYMDYPJMdk+HuZhRuxxEl8abuNlGD0aCt2GCPV7GY0J9Ma7AcPw=='
  }
};
(function ($) {
  "use strict";
$.xdm = window.xdm;
}(jQuery));

As it’s been seen there is an object named sess containing the two properties named is_authenticated and token. This object is responsible to transfer authentication. At this moment the user has authentication token but not authentication cookie of the current website, so the second call is made:

Press enter or click to view image in full size

The JavaScript code:

Press enter or click to view image in full size
Press enter or click to view image in full size
Vulnerable External JavaScript Object

The question is, an arbitrary origin can extract the authentication token? of course, it can because the JSONP call bypasses the Same Origin Policy.

Press enter or click to view image in full size

The vulnerability found, account takeover by a single click :)

The Exploitation Phase

The scenario is simple:

Setting up a page calling JSONP on behalf of any user
Tricking authenticated user to visit our malicious website
Sending authentication token by the user to our website
logging-in as the victim and doing bad stuff

The exploit code (client-side + server-side call):

Here is the video POC:
