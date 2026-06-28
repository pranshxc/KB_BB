---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-08-31_unhiding-the-hidden_2.md
original_filename: 2020-08-31_unhiding-the-hidden_2.md
title: Unhiding the hidden
category: documents
detected_topics:
- csrf
- access-control
- command-injection
- password-reset
- otp
- api-security
tags:
- imported
- documents
- csrf
- access-control
- command-injection
- password-reset
- otp
- api-security
language: en
raw_sha256: 7a14fba225c6608d24eea1c7da48d36664cc8d92957a1504b53f214d2e27463f
text_sha256: e0d3905fd227dc30cbee85edd06947dbfeaf8151af391e693a84b19a5d9c342a
ingested_at: '2026-06-28T07:32:03Z'
sensitivity: unknown
redactions_applied: false
---

# Unhiding the hidden

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-08-31_unhiding-the-hidden_2.md
- Source Type: markdown
- Detected Topics: csrf, access-control, command-injection, password-reset, otp, api-security
- Ingested At: 2026-06-28T07:32:03Z
- Redactions Applied: False
- Raw SHA256: `7a14fba225c6608d24eea1c7da48d36664cc8d92957a1504b53f214d2e27463f`
- Text SHA256: `e0d3905fd227dc30cbee85edd06947dbfeaf8151af391e693a84b19a5d9c342a`


## Content

---
title: "Unhiding the hidden"
url: "https://medium.com/bugbountywriteup/unhiding-the-hidden-2ef44192c10b"
authors: ["I am Broot"]
bugs: ["Client-side enforcement of server-side security", "Broken authorization", "CSRF"]
bounty: "530"
publication_date: "2020-08-31"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4287
scraped_via: "browseros"
---

# Unhiding the hidden

Unhiding the hidden
First bug bounty experience — $530
I am Broot
Follow
4 min read
·
Aug 30, 2020

73

This blog aims to help developers understand how attackers can take advantage of security misconfigurations to gain unauthorized access to restricted functionalities. A pretty simple vulnerability (if I come to think of it now), but most of my time and effort went into finding the right point of interest.
As an unauthenticated user, I could access certain functionalities that are available only to internal administrators, some of which include — the creation of new users with administrative privileges, modify system entries and configurations, view and update logs, regenerate access tokens, etc.

Step 1: Reconnaissance

Let’s say I was targeting “domain.com”. An open-source subdirectory enumerating tool pointed me to an interesting subdomain, say “iambroot.domain.com”. I ran a quick network scan on the subdomain to check for interesting open ports — only port 443 and 80 were open.

Step 2: Blackbox

The subdomain “iambroot.domain.com” on port 443 loaded a basic login page with no other form field functionalities - No registration process, password reset, or contact form. Just a simple old login page which allows users to login using a valid username/password combination and a message to contact the administrator if the user faced issues during login. I tried some basic authentication bypass test cases and decided to move on to another target assuming I reached a dead end. But I spent some time checking the traffic (Burp logs) sent to/fro the subdomain before I did.

While going through Burp logs, one application response caught my eye!

Step 3: Unauthorized access to the administrator module

One of the responses sent back from the server when the “iambroot.domain.com” domain was accessed revealed a couple of very “fishy” parameters; something like this.

“admin”:“false”, “allowDeploy”:“false”, “allowManage”:“false”

I quickly refreshed the site and captured the same request in Burp and modified the values of the above parameters in the response as shown below.

“admin”:“true”, “allowDeploy”:“true”, “allowManage”:“true”

Boom!

A “hidden” administrator module appears on the screen. The module opened up 25+ administrator functionalities, but the problem was that the site redirected me back to the login page whenever any of the 25+ functionalities were accessed.

Step 4: Unauthorized access to administrator functionalities

One such administrator functionality was to create a new user but the application redirected me to the login page the moment I tried accessing the functionality. Since response modification worked once, I assumed it would work again, hence intercepted the same request to check the response sent by the server.

Get I am Broot’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

The response of the request looked something like the screenshot below. The application server was sending back a “401 Unauthorized” status code when any of the administrator functionalities were accessed which in turn triggered a request to the login page.

Press enter or click to view image in full size

I intercepted the same request and made some minor changes to the response, as seen in the below screenshot. Boom!

I could now view the administrator functionality without the application redirecting me to the login page.

Press enter or click to view image in full size

Using the same approach I could access all available functionalities present in the administrator module. But as expected, the application once again would redirect me to the login page when I tried submitting the form. By modifying the response, I could only bypass client-side validation; and the application’s server-side validation prevented me from successfully creating a new user.

So this was a dead end. All I could do was get read-only access to the administrator module and individual functionalities present in them. I could not submit forms or perform unauthorized operations in the application.

Impact, you may ask. Nothing! But on the positive side, I could view form submission requests before the server validated the request, consequently sending back a “401 Unauthorized” error message.

Step 5: Cross-Site Request Forgery (CSRF)

One more thing that I observed in the application requests was the absence of a request verification token, which could possibly lead to a CSRF attack. Now that I knew how the administrator form submission requests looked like, I crafted a sample CSRF payload which would create a new user when the “real” administrator is tricked into executing the payload.

Step 6: Responsible Disclosure

I emailed the company’s security team with my observations as part of their vulnerability disclosure program. They fixed the issues by —

Applying server-side validation on all requests, thereby preventing unauthenticated users from viewing the administrator module and its functionalities.
Adding a request verification token in the request headers.
Removing public access to the entire subdomain as it looked like the “iambroot.domain.com” subdomain was intended for internal usage only.

From literally nothing but a login page, I could access administrator functionalities and chain this with CSRF to show some damage.

If you would ask me — Check logs. Always. Check. Logs.

Feedback and insights on the blog are highly appreciated. Feel free to comment or reach out to me on Twitter.
