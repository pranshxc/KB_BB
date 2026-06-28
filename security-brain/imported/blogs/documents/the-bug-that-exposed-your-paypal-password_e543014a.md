---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-01-08_the-bug-that-exposed-your-paypal-password.md
original_filename: 2020-01-08_the-bug-that-exposed-your-paypal-password.md
title: The Bug That Exposed Your PayPal Password
category: documents
detected_topics:
- rate-limit
- csrf
- xss
- command-injection
- otp
- api-security
tags:
- imported
- documents
- rate-limit
- csrf
- xss
- command-injection
- otp
- api-security
language: en
raw_sha256: e543014a362b45c8bf0b17f244f9e3974ab50dbbe0ee7ff729380c3eb67808bd
text_sha256: 33909a8c4817406266cdcf85c2d94d9c7ee4e60d9dcb4bc5906dbb4f1f4578bc
ingested_at: '2026-06-28T07:32:01Z'
sensitivity: unknown
redactions_applied: false
---

# The Bug That Exposed Your PayPal Password

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-01-08_the-bug-that-exposed-your-paypal-password.md
- Source Type: markdown
- Detected Topics: rate-limit, csrf, xss, command-injection, otp, api-security
- Ingested At: 2026-06-28T07:32:01Z
- Redactions Applied: False
- Raw SHA256: `e543014a362b45c8bf0b17f244f9e3974ab50dbbe0ee7ff729380c3eb67808bd`
- Text SHA256: `33909a8c4817406266cdcf85c2d94d9c7ee4e60d9dcb4bc5906dbb4f1f4578bc`


## Content

---
title: "The Bug That Exposed Your PayPal Password"
url: "https://medium.com/@alex.birsan/the-bug-that-exposed-your-paypal-password-539fc2896da9"
authors: ["Alex Birsan (@alxbrsn)"]
programs: ["Paypal"]
bugs: ["XSSI"]
bounty: "15,300"
publication_date: "2020-01-08"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4838
scraped_via: "browseros"
---

# The Bug That Exposed Your PayPal Password

Top highlight

The Bug That Exposed Your PayPal Password
And Credit Card Number Too
Alex Birsan
Follow
5 min read
·
Jan 8, 2020

4.7K

16

1

When hunting for security issues, the pursuit for uncharted assets and obscure endpoints often ends up taking the focus away from obvious, but still critical, functionality.

If you approach a target like you are the first person to ever perform a security assessment on it, and check everything thoroughly, I believe you are bound to find something new — especially if the code you are testing has been in continuous development for a while.

This is the story of a high-severity bug affecting what is probably one of PayPal’s most visited pages: the login form.

Initial discovery

While exploring PayPal’s main authentication flow, I noticed a javascript file containing what appeared to be a CSRF token and a session ID:

Press enter or click to view image in full size

This immediately drew my attention, because providing any kind of session data inside a valid javascript file usually allows it to be retrieved by attackers.

In what is known as a cross-site script inclusion (XSSI) attack, a malicious web page can use an HTML <script> tag to import a script cross-origin, enabling it to gain access to any data contained within the file.

Sure enough, a quick test confirmed the XSSI vulnerability and, although a javascript obfuscator was used to randomize variable names on each request, the interesting tokens were still placed in fairly predictable locations, making it possible to retrieve them with just a bit of extra work.

Press enter or click to view image in full size

However, a secret is only as good as the damage you can do with it. I immediately set out to find out what exactly _csrf and _sessionID were and if they could actually be used in a real attack.

Digging further

After countless attempts to replace regular CSRF tokens inside authenticated requests on PayPal’s platform with the value of _csrf, I came to the conclusion that a classic cross-site request forgery attack was not possible using this specific token. Similarly, a victim’s _sessionID was unfortunately not enough to impersonate them on PayPal’s site.

Next, I went back to the vulnerable script and followed the tokens to find what they were actually used for. This led to a deep dive into one of PayPal’s main protection mechanisms used to prevent brute force attacks, the security challenge. While this functionality is used in many places, I will be focusing on the main login form.

Press enter or click to view image in full size

The idea is pretty simple: After a few failed login attempts, you are required to solve a reCAPTCHA challenge before you can try again. The implementation, however, may raise some eyebrows.

Upon detecting a possible brute-force attempt, the response to the next authentication attempt is a page containing nothing but a Google captcha. If the captcha is solved by the user, an HTTP POST request to /auth/validatecaptcha is initiated.

Press enter or click to view image in full size

The familiar _csrf and _sessionID are present in the request body, as well as two other values, which we will get to a bit later.

Get Alex Birsan’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

The response to the captcha validation request is meant to re-introduce the user into the authentication flow. To this end, it contains a self-submitting form with all the data provided in the user’s latest login request, including their email and plain text password.

Press enter or click to view image in full size

I realized that, with the correct timing and some user interaction, knowing all the tokens used in this request was enough to get the victim’s PayPal credentials. In a real-life attack scenario, the only user interaction needed would have been a single visit to an attacker-controlled web page.

So I went back and tried to figure out what the missing parameters were. This was easier than expected:

The value of jse was not validated at all.
recaptcha was the token provided by Google upon solving a reCAPTCHA challenge. It was not tied to a specific session, so any valid token— for example, from an automated solving service — would be accepted.
Exploitation

Putting all this together, I created a proof of concept that demonstrated the whole process, except for integrating a captcha solving service.

First, the proof of concept would exploit the initial XSSI vulnerability to get a set of tokens which were valid in the victim’s session. It would then launch a few authentication requests with random credentials from the victim’s browser, simulating a brute force attempt, which would trigger the security challenge flow.

Once the victim logged in to PayPal using the same browser, the cached random credentials would be replaced by the user’s own email and password. The last step was obtaining a fresh reCAPTCHA token, after which the plain text credentials would be retrieved with a server-side request to the /auth/validatecaptcha endpoint and displayed on the page.

Press enter or click to view image in full size
The final page shown by my proof of concept code contained your email and password

I later found that the same vulnerable process was also used on some unauthenticated checkout pages, allowing plain text credit card data to be leaked using the same technique.

Disclosure

The proof of concept, along with all relevant information, was submitted to PayPal’s bug bounty program on the 18th of November 2019, and was validated by HackerOne 18 days later.

Following a quick acknowledgement by the PayPal team and a few additional questions, I was awarded a $15,300 bounty on the 10th of December. The reward amount corresponds with the bug’s 8.0 (High) CVSS score, which is the same score that I had initially suggested when submitting the report.

A patch was applied around 24 hours later, meaning that the bug was fixed only five days after PayPal became aware of it — quite an impressive turnaround time.

Fix and prevention advice

The /auth/validatecaptcha endpoint now requires an additional CSRF token, which cannot be leaked using cross-site script inclusion.

While this properly fixes the vulnerability, I believe that the whole thing could have been prevented when designing the system by following one of the oldest and most important pieces of infosec advice: Never store passwords in plain text.
