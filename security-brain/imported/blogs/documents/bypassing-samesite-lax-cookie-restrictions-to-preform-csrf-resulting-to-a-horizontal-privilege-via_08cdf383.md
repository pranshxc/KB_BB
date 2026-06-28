---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-02-13_bypassing-samesitelax-cookie-restrictions-to-preform-csrf-resulting-to-a-horizon.md
original_filename: 2023-02-13_bypassing-samesitelax-cookie-restrictions-to-preform-csrf-resulting-to-a-horizon.md
title: Bypassing SameSite=lax cookie restrictions to preform CSRF resulting to a horizontal
  privilege escalation via poor email verification mechanism
category: documents
detected_topics:
- password-reset
- csrf
- sso
- access-control
- xss
- command-injection
tags:
- imported
- documents
- password-reset
- csrf
- sso
- access-control
- xss
- command-injection
language: en
raw_sha256: 08cdf3834b7bc8ffa75c31ce17d2741225f9dc71b340c89500090161e934cf02
text_sha256: 5b5784a74ff72c176ae39d665d41febc07ce17156a711bca70e2898b19d933f9
ingested_at: '2026-06-28T07:32:18Z'
sensitivity: unknown
redactions_applied: false
---

# Bypassing SameSite=lax cookie restrictions to preform CSRF resulting to a horizontal privilege escalation via poor email verification mechanism

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-02-13_bypassing-samesitelax-cookie-restrictions-to-preform-csrf-resulting-to-a-horizon.md
- Source Type: markdown
- Detected Topics: password-reset, csrf, sso, access-control, xss, command-injection
- Ingested At: 2026-06-28T07:32:18Z
- Redactions Applied: False
- Raw SHA256: `08cdf3834b7bc8ffa75c31ce17d2741225f9dc71b340c89500090161e934cf02`
- Text SHA256: `5b5784a74ff72c176ae39d665d41febc07ce17156a711bca70e2898b19d933f9`


## Content

---
title: "Bypassing SameSite=lax cookie restrictions to preform CSRF resulting to a horizontal privilege escalation via poor email verification mechanism"
url: "https://medium.com/@deadoverflow/bypassing-samesite-lax-cookie-restrictions-to-preform-csrf-resulting-to-a-horizontal-privilege-1dfc8fb17b0a"
authors: ["Imad Husanovic (@deadoverflow_)"]
bugs: ["CSRF"]
publication_date: "2023-02-13"
added_date: "2023-02-22"
source: "pentester.land/writeups.json"
original_index: 1536
scraped_via: "browseros"
---

# Bypassing SameSite=lax cookie restrictions to preform CSRF resulting to a horizontal privilege escalation via poor email verification mechanism

Bypassing SameSite=lax cookie restrictions to preform CSRF resulting to a horizontal privilege escalation via poor email verification mechanism
Imad Husanovic
Follow
6 min read
·
Feb 13, 2023

155

4

Subscribe to my educational hacking YouTube channel: https://youtu.be/tqSK50xo9yE?si=0yVngoL53LTWPesM

Same site lax cookie restrictions are always annoying when hunting for CSRF bugs. When I was starting out with hacking, CSRF attacks were always something I’d hunt for. In most cases XSS, CSRF and all these client side vulnerabilities are easy to hunt for, just paste some XSS vectors and hope you see an alert pop up. This is amazing if you are starting out with your journey but kind of disappointing if you have 1+ years experience in hacking and still use this technique. Same applies for CSRF attacks. You can construct a basic CSRF if, for example the page uses forms that aren’t protected with a csrf token or simply try out some weird ideas in general. So here goes a story of how I found a CSRF bug on a website that uses same site lax cookie restrictions as well as csrf tokens to protect their forms and I was able to escalate this into a serious bug, so here it goes…

So I started researching one of the most popular websites in my country used for selling items and much more like cars, technical equipment and so much more. Users can register an account and search for what they are looking for and or upload their own items so other people can get in contact with them regarding something they’ve uploaded. When I firstly logged in I realized that Chrome automatically assigned Same-Site=lax to session cookie

So right of the bat I knew this isn’t going to be easy since my plan was to hunt for client side security issues. On top of that the session cookie was also HttpOnly! So yeah I continued to research how the web app was handling other data. I found out that every form uses csrf token and all of my XSS attempts were failing, everything was encoded and escaped properly. I started to take a look into email and phone number verification forms and realized that these forms aren’t protected with csrf tokens. I mean, yeah why should you use csrf token on a form that doesn’t have any sensitive action apart from telling the server that someone is requesting a verification link. However I realized something. So the request looked like this:

Press enter or click to view image in full size

This was a POST request to the /email_verify endpoint and it included the email that I used to create my account.

So I just asked myself: What if I change that email address to some other email. When I did that I was shocked! I received the email verification link on the email address I supplied. Email that was associated with the account was pinklad@wearehackerone.com but I received email verification to deadoverflow@gmail.com just because I changed the email parameter in the /email_verify POST request. Wow! This was indeed odd behavior by the web app. But this isn’t even the crazy part. When I visited my profile again, I noticed that my email was changed! Now my email is deadoverflow@gmail.com. What the hell? Did I just change the email address of my account by manipulating the email parameter in the /email_verify request? The answer is yes, I did! But I was still far from exploiting this for horizontal privilege escalation. As I mentioned, the website was using Same-Site=lax, so sending the POST request to /email_verify from another origin would result in a redirect to login. So yeah, I was stuck. In the meantime I realized that phone number verify would also result in phone number overwrite on the currently logged in account if the number parameter was manipulated in /tel_verify POST request.

Get Imad Husanovic’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

So I spent next 2 days just trying to figure out something that I could use to link with this bug and hopefully result in a horizontal privilege escalation. But then, I just thought to myself: Why don’t I try out some weird ideas that I had? One of them was to send a GET request to /email_verify with a query parameter email=attacker@example.com. And it worked!! I changed the email address of my account from pinklad@wearehackerone.com to attacker@example.com just because I opened a link!

Press enter or click to view image in full size

So that was it. I found a bug that allowed me to overwrite the email of the victim’s account just by opening the link. But only users whose email or phone number isn’t verified can fall for being victims of this bug. Again, normal users who are just looking to sell something or buy, aren’t going to pay attention to the fact that their email is not verified. So I crafted a simple exploit:

Press enter or click to view image in full size

So once the victim opens a link he will be greeted with a button, and upon clicking on it, few things will happen.

The new window will open and firstly email address will be overwritten. Then the phone number and finally user will be redirected to youtube.com. (I just could’ve updated the email without the button interaction but I just added to change both, email and phone number)

Once the victim opens the link:

Press enter or click to view image in full size

What has actually happened:

Now the attacker can request a password reset for the email pinklad0x00@wearehackerone.com, get the password and log himself into the victims account. And just like that, the attacker stole the victims account!

To summarize, it may seem hard to hunt for bugs or even escalate some bugs that you may label as “unusable”! But just keep in your head that coming up with ways to exploit something, trying out and failing is still security research. Even if you don’t find the bug it is still a research! Just keep that in mind. Getting yourself familiar with the web app by trying out things you came up with and seeing how the application responds can help you with finding bugs later. It’s also amazing to read other peoples write ups because they can help you to learn new techniques and expand your knowledge. As seen here, even the web applications that seem protected and all safe, can still screw up with something simple. So do not lose hope and continue hacking!
