---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2024-08-13_breaking-the-barrier-admin-panel-takeover-worth-3500.md
original_filename: 2024-08-13_breaking-the-barrier-admin-panel-takeover-worth-3500.md
title: 'Breaking the Barrier: Admin Panel Takeover Worth $3500'
category: documents
detected_topics:
- password-reset
- otp
- idor
- ssrf
- command-injection
- rate-limit
tags:
- imported
- documents
- password-reset
- otp
- idor
- ssrf
- command-injection
- rate-limit
language: en
raw_sha256: 25b5b003803c77af6ad9abaa26a8d474f6734fa5ec0b9d22ea777c49b52f69cd
text_sha256: 986e56e22f32eac038e23fb2070e0e33cb27f7ad46102d3a5d413ff3ed9cf466
ingested_at: '2026-06-28T07:32:37Z'
sensitivity: unknown
redactions_applied: false
---

# Breaking the Barrier: Admin Panel Takeover Worth $3500

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2024-08-13_breaking-the-barrier-admin-panel-takeover-worth-3500.md
- Source Type: markdown
- Detected Topics: password-reset, otp, idor, ssrf, command-injection, rate-limit
- Ingested At: 2026-06-28T07:32:37Z
- Redactions Applied: False
- Raw SHA256: `25b5b003803c77af6ad9abaa26a8d474f6734fa5ec0b9d22ea777c49b52f69cd`
- Text SHA256: `986e56e22f32eac038e23fb2070e0e33cb27f7ad46102d3a5d413ff3ed9cf466`


## Content

---
title: "Breaking the Barrier: Admin Panel Takeover Worth $3500"
url: "https://medium.com/@noob.assassin/breaking-the-barrier-admin-panel-takeover-worth-3500-78da79089ca3"
authors: ["Aditya Sharma (@Assass1nmarcos)"]
bugs: ["Authentication bypass", "Password reset", "Information disclosure"]
bounty: "3,500"
publication_date: "2024-08-13"
added_date: "2024-08-14"
source: "pentester.land/writeups.json"
original_index: 76
scraped_via: "browseros"
---

# Breaking the Barrier: Admin Panel Takeover Worth $3500

Top highlight

Breaking the Barrier: Admin Panel Takeover Worth $3500
Aditya Sharma
Follow
3 min read
·
Aug 13, 2024

748

6

Hello Folks,

I’m back with another writeup where we successfully bypassed the Admin Panel while working on a Bugcrowd private program. This issue was discovered in collaboration with my friend Rajesh Ranjan (Also thanks to him for inviting me to collaborate on the program).

What is Admin Panel Bypass?

Admin panel bypass is a technique used by attackers to gain unauthorized access to an administrative interface of a website or application. This typically involves exploiting vulnerabilities, such as weak authentication mechanisms, exposed endpoints, or flawed password reset functionalities, to bypass the login process and access sensitive areas reserved for administrators. Once inside, attackers can manipulate the system, steal data, or cause significant damage. This type of vulnerability is critical because it can lead to complete control over the affected system.

Let’s assume the target is example.com. During our subdomain enumeration, we identified a subdomain named admin.example.com.

When you normally visit this subdomain, it redirects you to the login page at https://admin.example.com/manage/login. We decided to enumerate directories using FFUF and targeted https://admin.example.com/manage/. During this process, we discovered another endpoint: the "Forgot Password" page at https://admin.example.com/manage/forgotpassword.

Upon submitting the username admin and intercepting the request, we observed that the password reset token was leaked in the response.

Press enter or click to view image in full size
Picture 1: Interception of Forget Password request

The biggest hurdle we faced was figuring out how to use this password reset token to actually reset the admin user’s password. After some investigation (we read the full API documentation of the Web app), we identified the relevant parameter, which was passwordConfirm.

Get Aditya Sharma’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

We then crafted a request to the /api/employee/resetpassword endpoint, including the token in the request. Upon sending the request, we successfully reset the admin user's password.

Press enter or click to view image in full size
Picture 2: Resetting the Password of the Admin

After that, we attempted to log in to the admin panel https://admin.example.com/manage/login using the password we had set. As expected, we successfully gained access to the admin panel.

Press enter or click to view image in full size
Picture 3: Logged in to Admin Panel

This vulnerability was patched within an hour of submission by the program, and later, we were rewarded $3,500 for discovering this issue.

Press enter or click to view image in full size
Picture 4: Money in Wallet

Also some tips here:

Tip 1: Don’t be a Lazy lad, read the API documentation, in our case reading the documentation led us to know the passwordConfirm parameter for resetting the password via API(Look into picture 2)

Tip 2: Try to find additional impact with the first vulnerability. In our case, we were able to find a full internal SSRF leading to an AWS metadata leak, but it was marked as a duplicate because it can only be exploited if the admin panel, which was the original vulnerability we found.

If you have any queries let me know on X. Also open to collaborations.
