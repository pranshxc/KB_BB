---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-10-13_code-flaws-leads-to-orgadmin-account-takeover.md
original_filename: 2022-10-13_code-flaws-leads-to-orgadmin-account-takeover.md
title: Code flaws leads to Org/Admin Account Takeover
category: documents
detected_topics:
- access-control
- xss
- command-injection
- cors
- cloud-security
tags:
- imported
- documents
- access-control
- xss
- command-injection
- cors
- cloud-security
language: en
raw_sha256: ed733ff6726f65bfa4f96bd3b27236bb258b07db39e30ab35263e3de8e2417ed
text_sha256: cfb8e3ddfcfaaf9a2462c6734063e2f04dd98675ee9b358abc361a8b4b983aa8
ingested_at: '2026-06-28T07:32:15Z'
sensitivity: unknown
redactions_applied: false
---

# Code flaws leads to Org/Admin Account Takeover

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-10-13_code-flaws-leads-to-orgadmin-account-takeover.md
- Source Type: markdown
- Detected Topics: access-control, xss, command-injection, cors, cloud-security
- Ingested At: 2026-06-28T07:32:15Z
- Redactions Applied: False
- Raw SHA256: `ed733ff6726f65bfa4f96bd3b27236bb258b07db39e30ab35263e3de8e2417ed`
- Text SHA256: `cfb8e3ddfcfaaf9a2462c6734063e2f04dd98675ee9b358abc361a8b4b983aa8`


## Content

---
title: "Code flaws leads to Org/Admin Account Takeover"
url: "https://mr23r0.medium.com/code-flaws-leads-to-org-admin-account-takeover-ad9515a96eab"
authors: ["Saransh Saraf (@mr23r0)"]
bugs: ["Privilege escalation", "Account takeover"]
publication_date: "2022-10-13"
added_date: "2022-10-17"
source: "pentester.land/writeups.json"
original_index: 2049
scraped_via: "browseros"
---

# Code flaws leads to Org/Admin Account Takeover

Code flaws leads to Org/Admin Account Takeover
Saransh Saraf aka (MR23R0)
Follow
3 min read
·
Oct 13, 2022

360

4

Hello Everyone, I’m Saransh Saraf and I’m back with another unique account takeover idea, so let’s just dive into it :)

Press enter or click to view image in full size
code flaws leads to account takeover

Let’s Start with the Application Design :

The Application was only allowing one Admin/Manager per one organization, but other viewers has to login in order to view the content. Note: After creating an account user cannot change the organization_name.

Design Flaw/ Insecure Design : While creating an account I saw a very weird parameter in the POST request

POST /some_ajax/create_event_flow HTTP/1.1
Host: portal.example.com
Connection: close
Content-Length: 663
sec-ch-ua: "Google Chrome";v="105", "Not)A;Brand";v="8", "Chromium";v="105"
Accept: application/json, text/javascript, */*; q=0.01
Content-Type: application/json; charset=UTF-8
X-Requested-With: XMLHttpRequest
sec-ch-ua-mobile: ?0
User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36
sec-ch-ua-platform: "Linux"
Origin: https://portal.example.com
Sec-Fetch-Site: same-origin
Sec-Fetch-Mode: cors
Se;c-Fetch-Dest: empty
Referer: https://portal.example.com/create_event_flow
Accept-Encoding: gzip, deflate
Accept-Language: en-GB,en-US;q=0.9,en;q=0.8
Cookie:
{"methodName":"onboard","params":{"some_params":{"some_name":"Account takeover","some_modules":[1]},"user_params":{"name":"User_name","email":"admin@mr23r0.rocks","password":"Password_Secret"},"community_params":{"name":"Organization_name","slug":"testthing-for-ato","c_id":683,"client_time_zone":"Asia/Calcutta"}}}

“c_id” noticed it? I hope so, let’s see what is happening in the backend

While trying to register, the application creates a entry with the email address and creates a row in the organization table (if it’s SQL)

Then our current request goes into the users table and makes a user with a predefined organization

INSERT INTO users (username, password, organization) VALUES ("Jack","123", "organization_name") WHERE c_id='683';

So I changed the “c_id” with the victim’s “c_id” and as expected it took me to the victim’s organization.

Note : The Application doesn’t supports multiple Admin/Manager in one organization.

So we got our first bug ;) Design flow but we can also call it “Horizontal privilege escalation”

Horizontal privilege escalation is when a user gains the access rights of another user who has the same access level as he or she does.

See when I do testing, primarily what I want to achieve is an Account takeover and testing is like a video game for me completing every level one by one… so I started looking for more vulnerabilities :)

Get Saransh Saraf aka (MR23R0)’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

And after 15 minutes of search I got it, found a stored cross site scripting on the “Organization_name” now the problem is how can I change the victim’s “Organization_name”

I tried to replicate the create an account request and BOOM!! we can send a POST request to “/some_ajax/create_event_flow” no authentication required and also if we put cross site scripting payload in “Organization_name” and change our “c_id” with the victim’s “c_id”, the victim’s “Organization_name” gets changed ;)

login page — dashboard

We got the victim’s active cookies — but no-one will accept account takeover with active cookies -_-

So I simply checked for “Session Fixation / No logout” and I got lucky the application was vulnerable :)

Last two vulnerability, the application was taking current password in order to change password but “the fun part :)” after intercepting the request I found that they’re not sending or checking the current password ;) and there wasn’t any authentication on change email operation….

Quick wrap up :

Create an account --> change the "c_id" and add the blind xss payload in the "organization_name"
copy the victim's cookies 
Login as the victim by using the cookies
change the password by using:
  i. Change Password
  ii. Change Email --> Recover password

So we’re back on the title question “What was that? Organization takeover or Admin Account takeover” either way the bug is triaged :)

I hope you’ve learned something new from this, see at bsidesahemdabad me and 
yashdharmani
 got a chance to share ideas with 
Yassine Aboukir
 and as summary we can say it’s all about understanding the backend logic and details.

If you like this please don’t forget to give this article a clap and connect with me on twitter and linkedin. if you want to dicuss an idea feel free to create a thread and mention me ;)

JavaScript is not available.
Edit description

twitter.com

Saransh Saraf — Information Security Analyst — Codewits Solutions Pvt. Ltd. | LinkedIn
I am a student of B.Sc and pursuing my adventures in the field of Cyber Security and Information Security. In my free…

www.linkedin.com
