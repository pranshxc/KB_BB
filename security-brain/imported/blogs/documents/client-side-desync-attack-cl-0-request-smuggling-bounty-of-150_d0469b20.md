---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-10-26_client-side-desync-attack-cl0-request-smuggling-bounty-of-150.md
original_filename: 2022-10-26_client-side-desync-attack-cl0-request-smuggling-bounty-of-150.md
title: Client Side Desync Attack (CL.0 Request Smuggling) — Bounty of $150
category: documents
detected_topics:
- xss
- command-injection
- automation-abuse
tags:
- imported
- documents
- xss
- command-injection
- automation-abuse
language: en
raw_sha256: d0469b20a56fa63497edc6aceb850e44a3c7099ad7cf41513d1a3d3f734864f0
text_sha256: 9f47a32532027ec4b30ad303dd5489c194ae97d2ad8ed1e95b619afb253abc08
ingested_at: '2026-06-28T07:32:15Z'
sensitivity: unknown
redactions_applied: false
---

# Client Side Desync Attack (CL.0 Request Smuggling) — Bounty of $150

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-10-26_client-side-desync-attack-cl0-request-smuggling-bounty-of-150.md
- Source Type: markdown
- Detected Topics: xss, command-injection, automation-abuse
- Ingested At: 2026-06-28T07:32:15Z
- Redactions Applied: False
- Raw SHA256: `d0469b20a56fa63497edc6aceb850e44a3c7099ad7cf41513d1a3d3f734864f0`
- Text SHA256: `9f47a32532027ec4b30ad303dd5489c194ae97d2ad8ed1e95b619afb253abc08`


## Content

---
title: "Client Side Desync Attack (CL.0 Request Smuggling) — Bounty of $150"
url: "https://bpandasec.medium.com/client-side-desync-attack-cl-0-request-smuggling-bounty-of-150-327d3aeaeea6"
authors: ["Bodhendu Panda"]
bugs: ["HTTP request smuggling", "Client-Side Desync attack"]
bounty: "150"
publication_date: "2022-10-26"
added_date: "2023-05-08"
source: "pentester.land/writeups.json"
original_index: 1985
scraped_via: "browseros"
---

# Client Side Desync Attack (CL.0 Request Smuggling) — Bounty of $150

Client Side Desync Attack (CL.0 Request Smuggling) — Bounty of $150
Bodhendu Panda
Follow
3 min read
·
Apr 26, 2023

221

3

Hello everyone. I’m Bodhendu Panda, a cyber security geek. Today, let’s look at how I was able to find a client-side desync attack vulnerability on a public bug bounty platform.

Press enter or click to view image in full size
Press enter or click to view image in full size
Bounty of $150

Description
HTTP request parsing between a reverse proxy and the web application. An unauthenticated attacker may exploit this issue and poison requests of other users, which may lead to various consequences including account takeover.

Issue background:-
Client-side desync (CSD) vulnerabilities occur when a web server fails to correctly process the Content-Length of POST requests. By exploiting this behaviour, an attacker can force a victim’s browser to desynchronize its connection with the website, typically leading to XSS.

Steps to exploit the Vulnerability:-

I was hunting for a program, and let’s call the subdomain abc.example.com. I have observed that the website has two ports open (80,443).

Get Bodhendu Panda’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

So I have tried to exploit port 80, and I have noticed that on port 80, I was able to downgrade HTTP/2 to HTTP/1.1. As show in the below image.

Note: It is an CL.0 request smuggling; hence, turn off the auto-update content length from the burp repeater settings.

Now you can change the connection from closed to keep-alive.

Now it’s time to add another request to the repeater to perform request smuggling.

On sending the request in repeater, you can observe that I was able to fetch the response of the second request as well.

Accessing the `/admin` path directly returned a 404 response. However, when I included `/admin` as the path within a smuggled request (2nd request) and sent both requests (smuggled request and normal requst with path as /) using the Repeater’s group tab, I was able to successfully access the admin dashboard.

Press enter or click to view image in full size

Issue remediation:-
You can resolve this vulnerability by patching the server so that it either processes POST requests correctly, or closes the connection after handling them. You could also disable connection reuse entirely, but this may reduce performance. You can also resolve this issue by enabling HTTP/2.

Thank you for reading. I hope you have found the blog helpful. Have a nice day. Happy Hacking!!!. Subscribe to the blog for more walkthroughs, tricks and bug bounty writeups.
