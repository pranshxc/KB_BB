---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-01-05_privilege-escalation-from-being-a-normal-user-to-admin.md
original_filename: 2021-01-05_privilege-escalation-from-being-a-normal-user-to-admin.md
title: 'Privilege Escalation: From being a normal user to admin'
category: documents
detected_topics:
- access-control
- oauth
- idor
- command-injection
- mfa
- otp
tags:
- imported
- documents
- access-control
- oauth
- idor
- command-injection
- mfa
- otp
language: en
raw_sha256: 2598608279cb5b0622876e43a131e0dacf944864a0721a8f94536bc4dba6c86e
text_sha256: 70b89206d1ae108e81000e8811ed08ac8da8e04a78499727a62f9f799247f82a
ingested_at: '2026-06-28T07:32:04Z'
sensitivity: unknown
redactions_applied: false
---

# Privilege Escalation: From being a normal user to admin

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-01-05_privilege-escalation-from-being-a-normal-user-to-admin.md
- Source Type: markdown
- Detected Topics: access-control, oauth, idor, command-injection, mfa, otp
- Ingested At: 2026-06-28T07:32:04Z
- Redactions Applied: False
- Raw SHA256: `2598608279cb5b0622876e43a131e0dacf944864a0721a8f94536bc4dba6c86e`
- Text SHA256: `70b89206d1ae108e81000e8811ed08ac8da8e04a78499727a62f9f799247f82a`


## Content

---
title: "Privilege Escalation: From being a normal user to admin"
url: "https://parasarora06.medium.com/privilege-escalation-from-being-a-normal-user-to-admin-3f86896f1c93"
authors: ["Akshar Tank"]
bugs: ["Privilege escalation", "Broken Access Control"]
publication_date: "2021-01-05"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4029
scraped_via: "browseros"
---

# Privilege Escalation: From being a normal user to admin

Privilege Escalation: From being a normal user to admin
Paras Arora
Follow
2 min read
·
Jan 6, 2021

241

Press enter or click to view image in full size

Privilege Escalation: Privilege escalation happens when an attacker exploits a bug, design flaw, or configuration error in an application or operating system to gain elevated access to system resources that should normally be unavailable to any unauthorized user.

Reference:https://www.netsparker.com/blog/web-security/privilege-escalation/

Hi Infosec Community,

I hope everyone is fine and hitting hard on the applications, I encountered a privilege escalation issue so let’s discuss about it.

I was hunting on a private program and started with subdomain enumeration with Subfinder.

subfinder -d domain.com | httpx -o /output_file.txt

After that, I ran Waybackurls on output_file.txt.

cat output_file.txt | waybackurls > /wayback.txt

I was searching for various keywords in the wayback.txt file and finally got something really interesting having the keyword “admin”

https://www.domain.com/xxx/xxxx/page/login/?redirect_uri=https%3A%2F%2Fwww.domain.com%2Fadmin%2F&app_id=xx

Now I signed up for the account on domain.com/register to get an insight of the application and was exploring the application while keeping an eye on the above url which I found in the wayback.txt. I was exploring the features and there was nothing related to admin.

Get Paras Arora’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

So, out of curiosity, I opened a new tab adjacent to the current tab I was logged into, with a normal user account and pasted the above URL.

After the results displayed on my screen, I analyzed the resultant webpage for a while.

So, after hitting the URL which was redirecting to URL consisting of “admin” keyword and app_id of admin, my normal user account changed to the admin and I was able to access the functionalities which were unauthorized initially.

So, this is how I was able to get access to all the admin functionalities and achieved the higher privileged role on the web application.

Takeaways

Explore the application thoroughly
Always look for sensitive keywords like admin, api_key, token etc.
Look for urls having “admin” keyword in it
Be curious, you will definitely land up with a great finding
Open higher privileged account requests directly in the new tab adjacent to the tab in which normal user is logged in, sometimes you will get access to functionalities which are not authorized for user.

Twitter: https://twitter.com/parasarora06
