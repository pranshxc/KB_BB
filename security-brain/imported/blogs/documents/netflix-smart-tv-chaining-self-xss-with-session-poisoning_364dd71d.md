---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-03-11_netflixsmart-tv-chaining-self-xss-with-session-poisoning.md
original_filename: 2023-03-11_netflixsmart-tv-chaining-self-xss-with-session-poisoning.md
title: '[Netflix][Smart TV] — Chaining Self-XSS with Session poisoning.'
category: documents
detected_topics:
- xss
- command-injection
- automation-abuse
- csrf
- api-security
tags:
- imported
- documents
- xss
- command-injection
- automation-abuse
- csrf
- api-security
language: en
raw_sha256: 364dd71dc7ac02f75c8f2d2f1441cb8eecc29032fc5378641bfe88767b0c574d
text_sha256: 64f3d57cdc9a6b015b816e71c29a5b60f46e0da317b0ed091973d38135ecd87a
ingested_at: '2026-06-28T07:32:19Z'
sensitivity: unknown
redactions_applied: false
---

# [Netflix][Smart TV] — Chaining Self-XSS with Session poisoning.

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-03-11_netflixsmart-tv-chaining-self-xss-with-session-poisoning.md
- Source Type: markdown
- Detected Topics: xss, command-injection, automation-abuse, csrf, api-security
- Ingested At: 2026-06-28T07:32:19Z
- Redactions Applied: False
- Raw SHA256: `364dd71dc7ac02f75c8f2d2f1441cb8eecc29032fc5378641bfe88767b0c574d`
- Text SHA256: `64f3d57cdc9a6b015b816e71c29a5b60f46e0da317b0ed091973d38135ecd87a`


## Content

---
title: "[Netflix][Smart TV] — Chaining Self-XSS with Session poisoning."
url: "https://ltsirkov.medium.com/netflix-smart-tv-chaining-self-xss-with-session-poisoning-3eb7c78c7914"
authors: ["Lyubomir Tsirkov (@lyubo_tsirkov)"]
programs: ["Netflix"]
bugs: ["Self-XSS", "Cookie injection", "Session management issue"]
publication_date: "2023-03-11"
added_date: "2023-03-23"
source: "pentester.land/writeups.json"
original_index: 1391
scraped_via: "browseros"
---

# [Netflix][Smart TV] — Chaining Self-XSS with Session poisoning.

[Netflix][Smart TV] — Chaining Self-XSS with Session poisoning.
Lyubomir Tsirkov
Follow
7 min read
·
Mar 11, 2023

69

1

I’d like to share my experience of discovering an interesting vulnerability on Netflix while using their TV application.

Through my participation in Netflix’s Bug Bounty program, I was able to identify a vulnerability rated as P3(Medium), known as Self-XSS, which was made more impactful through the use of a cookie injection technique.

Exploiting this vulnerability could lead to unauthorized access to a user’s account under specific circumstances.

By chaining both vulnerabilities, an attacker could send a specifically crafted URL to unauthenticated users containing only UUID as a GET param which represents malicious JavaScript injected beforehand and attached to that UUID.

Example: www.netflix.com/?flwssn=4f1b268f-2933-4bbc-9855-6b497ee7159e

Once the URL is opened, the victim will be assigned a specific cookie named “flwssn” that contains the unique identifier (UUID) value obtained from the GET parameter “flwssn=4f1b268f-2933–4bbc-9855–6b497ee7159e”. This UUID value represents the exploit code. The exploit code will be executed when the victim, who is unauthenticated, clicks on the login button.

It’s worth noting that the working timeframe of the exploit was 10 minutes. However, I discovered a technique to extend the timeframe of the exploit, which I have outlined in the post. This allows for a longer window of opportunity for an attacker to potentially gain unauthorized access to the victim’s account.

This vulnerability was discovered while browsing through the Netflix application on my smart TV, which highlights the importance of constant vigilance when using any services.

Thanks to Netflix for allowing me to publish this report. The vulnerability was handled through their bug bounty program in BugCrowd.

This vulnerability has been patched and the fix is rolled out.

Technical Details

Instead of watching a movie on Netflix before going to sleep, I decided to explore the Netflix application on my Smart TV. I discovered a feature that allowed me to log in using a “Sign-in code”.

This feature, called “Sign in on this TV from a web browser” works by generating a code on the TV, which you then enter on your web browser/phone to authenticate the TV.

Press enter or click to view image in full size
Netflix APP

Curious about the functionality of this feature, I decided to put it to the test. I opened my phone’s web browser, navigated to the URL “www.netflix.com/tv8”, and entered the code generated on my Smart TV.

This directed me to the next page.

Upon inspecting the login process, I immediately noticed the display of my TV’s device name “LG Tv”, indicating that there is user-controllable input reflected on that page. To test this further, I took the following steps:

1. [TV] I cleared the cache of the Netflix application.
2. [TV] I changed the device name of my TV to “<script>alert(1);</script>”.
3. [TV] I generated a new sign-in code.
4. [Phone Browser] I accessed www.netflix.com/tv8 as an unauthenticated user.
5. [Phone Browser] I typed the code from the TV to www.netflix.com/tv8 endpoint.

As I suspected, the outcome was:

Press enter or click to view image in full size

It was obvious that the device name wasn’t properly sanitized which allowed me to inject JavaScript. The payload was stored on their backend upon generating the TV code and was triggered in case you login using Sign-in code via your Web browser.

It’s important to mention that the script will be executed only if you type the code from the TV in www.netflix.com/tv8 as unauthenticated user.

For authenticated users, JavaScript will not be executed as the TV device name is only displayed on the login page in an unauthenticated state.

At this point, I was unable to exploit other users as the payload can only be triggered by visiting www.netflix.com/tv8 and entering the code from a TV manually, and the form is protected against CSRF as well.

I deemed it to be a self-XSS vulnerability with limited impact, but I considered it worth investigating further to see if I could escalate the exploit.

Note: At this stage I already reported the issue to Netflix despite the low impact.

Get Lyubomir Tsirkov’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

While investigating the request for submitting code to the www.netflix.com/tv8 endpoint, I identified a cookie named “flwssn”.

Press enter or click to view image in full size

Usually, upon typing the code from the TV to “www.netflix.com/tv8” endpoint, your “flwssn” value will be connected to the TV in case you type a valid code.

Flwssn value is usually UUID, but if you set it to a custom value it’s also accepted and reflected back to the user(As shown on the screenshot above).

The cookie held information about the TV for which the code was submitted. This means that “flwssn=4f1b268f-2933–4bbc-9855–6b497ee7159e” represents my TV. If this cookie is opened in another browser and assigned manually, the login form containing my device name will be presented, resulting in a Self-XSS vulnerability.

Nice, however, in order to have some impact, I had to find a way to assign it to the victim browser automatically.

After spending some time thinking how to do that, I simply discovered that by adding “flwssn” as a GET param will assign it automatically to the victim once the URL is opened.

Acting quickly, I entered the code from my TV into the www.netflix.com/tv8 endpoint and obtained the flwssn(UUID) value from the request. With this information, I crafted the following request:

https://www.netflix.com/?flwssn=4f1b268f-2933-4bbc-9855-6b497ee7159e

Once I opened it in an incognito window and navigated to www.netflix.com/login, I was prompted with alert(1).

Press enter or click to view image in full size

To summarize:

If an attacker can trick the user into visiting somehow that URL:

https://www.netflix.com/?flwssn=4f1b268f-2933-4bbc-9855-6b497ee7159e

The victim will be assigned with “flwssn” cookie that contains the value “4f1b268f-2933–4bbc-9855–6b497ee7159e” which is representing our exploit code. Once the cookie is assigned, the victim will be provided with malicious JavaScript every time he visits /login page until the TV code and cookie expire.

To trick the user into visiting that URL I could simply:
- Sending the URL directly to the victim. There is nothing suspicious within the URL.

The issue I faced was that the payload was only valid for a 10-minute window. This means that the attack could only occur within that time frame. This is because the code displayed on the TV screen is only active for 10 minutes before a new one is generated, making the previous code invalid and deleting the payload from the cookie. This limits the potential impact of the attack as it can only occur within a 10-minute window.

However, as I previously stated, when making a request to www.netflix.com/tv8 and entering the code, it is possible to input any “flwssn” value to that cookie and have the malicious payload assigned to it. This allows for the extension of the cookie’s validity.

In summary, every time a new code appears on the screen, by resending the request to the tv8 endpoint with the same “flwssn” value and the new code, it is possible to extend the payload’s validity.

Another method that I found to be effective is to poison a previously generated “flwssn” cookie.

If you are able to obtain someone’s flwssn, which is assigned to a user upon their first visit to www.netflix.com, and it is not “httpOnly” and has a scope of .netflix.com, you can generate a code from your TV and assign the victim’s “flwssn” on the /tv8 endpoint.

The next time the victim visits the login page, they will be presented with malicious Javascript.

As previously mentioned, this exploit only affects unauthenticated users. It will NOT work for those who are already logged in, as the payload is only displayed on the login page. This significantly reduces the potential impact of the exploit.

Regarding authenticated users: An additional method that I found to be effective is to send the following request to the victim:

www.netflix.com/SignOut?flwssn=<maliciousuuid>.

This will logout the victim and assign them with a new cookie. However, this also deletes the payload from the provided UUID. But, it is possible to regain payload by sending a request to www.netflix.com/tv8 as I already mentioned.

It’s worth mentioning that, in addition to the XSS vulnerability, once the victim is assigned the flwssn cookie of the attacker’s TV, the next time they log in, their account will automatically be logged in on the attacker’s TV.

Impact

The vulnerability allows an attacker to craft a seemingly harmless URL that contains a GET parameter “flwssn” containing a UUID value representing malicious JavaScript. The external JavaScript can be loaded as well. If the user authenticates themselves, it could result in compromising their credentials.

However, exploiting this vulnerability requires a constant increase of the Time To Live (TTL) of the cookie “flwssn”/TV Code, which is possible by resending the request to /tv8. This can be demonstrated manually as a proof of concept (PoC).

The vulnerability affects unauthenticated users.

Additionally, a second issue was identified which allows an attacker to set a custom FLWSSN for the end-user by simply sending it as a GET parameter. This allows to chain both vulnerabilities and increase the impact.
