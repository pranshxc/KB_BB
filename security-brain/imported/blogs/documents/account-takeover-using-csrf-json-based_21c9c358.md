---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2019-07-04_account-takeover-using-csrfjson-based.md
original_filename: 2019-07-04_account-takeover-using-csrfjson-based.md
title: Account Takeover Using CSRF(json-based)
category: documents
detected_topics:
- api-security
- xss
- cors
- csrf
- command-injection
- otp
tags:
- imported
- documents
- api-security
- xss
- cors
- csrf
- command-injection
- otp
language: en
raw_sha256: 21c9c35859543f0bd4ed80ab8b315b498d0bbb01e2d06b58eac7fc99b9769a9a
text_sha256: b4307c29e3cbd0657e3ebe5f100c78e90b94e9acc49e075c69da49dba5f597b1
ingested_at: '2026-06-28T07:31:59Z'
sensitivity: unknown
redactions_applied: false
---

# Account Takeover Using CSRF(json-based)

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2019-07-04_account-takeover-using-csrfjson-based.md
- Source Type: markdown
- Detected Topics: api-security, xss, cors, csrf, command-injection, otp
- Ingested At: 2026-06-28T07:31:59Z
- Redactions Applied: False
- Raw SHA256: `21c9c35859543f0bd4ed80ab8b315b498d0bbb01e2d06b58eac7fc99b9769a9a`
- Text SHA256: `b4307c29e3cbd0657e3ebe5f100c78e90b94e9acc49e075c69da49dba5f597b1`


## Content

---
title: "Account Takeover Using CSRF(json-based)"
page_title: "Exploiting a Chain of Vulnerabilities for Account Takeover | by shub rathore | Medium"
url: "https://medium.com/@shub66452/account-takeover-using-csrf-json-based-a0e6efd1bffc"
authors: ["shub rathore (@shub66452)"]
bugs: ["CSRF", "Account takeover"]
bounty: "1,000"
publication_date: "2019-07-04"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5167
scraped_via: "browseros"
---

# Account Takeover Using CSRF(json-based)

Exploiting a Chain of Vulnerabilities for Account Takeover
shub rathore
Follow
4 min read
·
Jul 4, 2019

242

1

Hey All,
I’m sil3nt_4unt3r, a bug hunter on HackerOne and Bugcrowd.This blog is my first foray into the world of writing,

INFO:-

Admin = full privileges

2. H-User = Some Privileges

3. L-User = Low Privileges

4. Guest = Very-Low Privileges

5. Program-Name = Redacted.com

6. The application is using json in the backend to transfer the data

I recently participated in a private Bugcrowd program with four user roles: Admin, H-User, L-User, and Guest. As part of my testing approach, I started by logging in with the admin account to explore the application’s functionalities.

During this exploration, I noticed that any changes made to site information triggered API requests to the server, following a pattern like https://redacted.com/api/*. While testing account settings, specifically the location field, I decided to delve deeper through fuzzing techniques. Interestingly, I discovered that the API endpoint lacked additional CSRF (Cross-Site Request Forgery) protection. While the API key served as a basic protection layer, it wasn't enough to fully secure the endpoint.

Press enter or click to view image in full size
API request

To exploit the CSRF vulnerability in the API endpoint, I required an any user API key. However, I identified an interesting functionality: a shared file and chat endpoint (https://redacted.com/office/[unique-Key]/story). Uploading a file and sharing it with everyone offered a potential path forward.

Here’s how I executed the attack:

Shared File with L-User: I uploaded a file and shared it with everyone using the aforementioned endpoint.
Switched Account: I then switched my login to an L-user account.
Triggered Notification: Upon logging in as the L-user, a notification appeared in the sidebar indicating a document shared by the admin. Opening the notification likely triggered an API request.
Intercepted Traffic with Burp: Anticipating a potential data leak in API requests related to the notification, I started Burp Suite listeners and refreshed the page.
Filtered Requests: I set a Burp filter for requests containing “story*” to narrow down the relevant traffic.
Identified Vulnerable Endpoint: After analyzing captured requests, I identified a vulnerable endpoint: /API/officename/[id]/storyPost/[L-user-office-id]/comments. This endpoint appeared to leak data belonging to the admin and potentially other users.
Further Fuzzing: Further exploration through fuzzing techniques revealed another endpoint leaking sensitive information, including user IDs, usernames, emails, API keys, office keys, and potentially more.
Press enter or click to view image in full size
Leak other user info

With the identified vulnerability, I proceeded to craft a CSRF exploit. JSON-based CSRF attacks can be achieved through two primary methods: Flash and XMLHttpRequest (XHR). Since the server relied on PUT requests for data updates, the Flash method wasn’t applicable.

Get shub rathore’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Focusing on XHR, two key factors contribute to its successful exploitation: Cross-Origin Resource Sharing (CORS) misconfiguration and the presence of XSS. Fortunately, I had already discovered a stored XSS vulnerability within the program.

Leveraging the XSS, I constructed a CSRF exploit file. This file, when sent to the admin as a link, could potentially trigger the identified vulnerability upon clicking. The impact of this action could have resulted in unauthorized modification of the admin’s user data, including email, password, and username.

Press enter or click to view image in full size
Press enter or click to view image in full size
Press enter or click to view image in full size

Impact:-

The identified CSRF vulnerability held significant implications. By exploiting this vulnerability, it was possible to gain the ability to modify various user data, including passwords, usernames, and email addresses. This impact extended not only to the admin account but potentially to all users across the main domain and its subdomains.

BugBountyTips:-

My experience highlights the importance of fuzzing group communication functionalities, such as file sharing and chat endpoints. Fuzzing these areas can potentially uncover leaks of sensitive data, like user tokens, usernames, or API keys.

In my case, fuzzing the /api/story* endpoint on a specific platform revealed a significant vulnerability. This endpoint facilitated group chat, note sharing, and file sharing among various user roles (admin, H-user, L-user, and guest).

Responsible Disclosure and Collaboration

I’d like to express my appreciation to the company’s co-founder for their exceptional approach. When the platform itself wasn’t responsive to my initial inquiries, the co-founder directly contacted me to clarify the situation. This collaborative approach is crucial for responsible vulnerability disclosure and improving platform security.

Report submitted 9 May 2019

Report Trigger 16 May 2019

Rewarded bounty xxxx$ on 27 May 2019

Bug Resolved 29 May 2019
