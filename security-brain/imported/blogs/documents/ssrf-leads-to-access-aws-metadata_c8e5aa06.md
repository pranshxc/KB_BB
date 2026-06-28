---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-08-27_ssrf-leads-to-access-aws-metadata.md
original_filename: 2022-08-27_ssrf-leads-to-access-aws-metadata.md
title: SSRF leads to access AWS metadata.
category: documents
detected_topics:
- ssrf
- idor
- xss
- command-injection
- path-traversal
- cloud-security
tags:
- imported
- documents
- ssrf
- idor
- xss
- command-injection
- path-traversal
- cloud-security
language: en
raw_sha256: c8e5aa069a9d8708103489d05948482172a58fa8c3c1d31e8a5dda75f77eee27
text_sha256: 4bafef12e9e3910505d7b20178aad2d02943a90d2f5fa81bb5f27ce6b1fa65df
ingested_at: '2026-06-28T07:32:13Z'
sensitivity: unknown
redactions_applied: false
---

# SSRF leads to access AWS metadata.

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-08-27_ssrf-leads-to-access-aws-metadata.md
- Source Type: markdown
- Detected Topics: ssrf, idor, xss, command-injection, path-traversal, cloud-security
- Ingested At: 2026-06-28T07:32:13Z
- Redactions Applied: False
- Raw SHA256: `c8e5aa069a9d8708103489d05948482172a58fa8c3c1d31e8a5dda75f77eee27`
- Text SHA256: `4bafef12e9e3910505d7b20178aad2d02943a90d2f5fa81bb5f27ce6b1fa65df`


## Content

---
title: "SSRF leads to access AWS metadata."
url: "https://infosecwriteups.com/ssrf-leads-to-access-aws-metadata-21952c220aeb"
authors: ["Akash Patil (@skypatil98)"]
bugs: ["SSRF"]
bounty: "50"
publication_date: "2022-08-27"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 2254
scraped_via: "browseros"
---

# SSRF leads to access AWS metadata.

SSRF leads to access AWS metadata.
Akash Rajendra Patil
Follow
4 min read
·
Aug 27, 2022

451

2

Press enter or click to view image in full size

Hi
Mates, I am Akash Patil (@skypatil98) from India. I am in the bug bounty field from the last 2.5 years. My previous blog is all about the IDOR leads to Changing the password of all users (ATO) which I found on a Private Program. If you haven’t read that blog you can read it by following this link. If there are any grammatical mistakes, leave on it. Without wasting any time we will start with the article.

So let’s get started! 😉

What is SSRF?

In the Server-Side Request Forgery (SSRF) attack, the attacker can induce functionality on the server to read or update internal resources. The attacker may be able to read server configuration such as AWS metadata, connect to internal services like http-enabled databases or perform post requests towards internal services which are not intended to be exposed. Learn more about SSRF.

Let’s consider the target as reducted.com because I can’t disclose the program name.

After that I checked every request on burp http history and So I use Burp Search to find the possible parameters like,

url={target}
file={target}
filename={target}
top 25 params

And found a url= that looks like this.

reducted.com/gadgets/proxy/?url=

1) Tried for open redirect

The URL was like https://reducted.com/gadgets/proxy/?url=https://evil.com

but failed :( It’s throwing an error

Press enter or click to view image in full size
2) Tried for XSS

The URL was like

https://reducted.com/gadgets/proxy/?url=javascript:alert(1);

https://reducted.com/gadgets/proxy/?url=http://14.rs

https://reducted.com/gadgets/proxy?url=http://brutelogic.com.br/poc.svg

Get Akash Rajendra Patil’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

but failed :(

Press enter or click to view image in full size
It’s throwing an error Method Not Allowed
3) Tried for LFI

URL was like https://reducted.com/gadgets/proxy/?url=file:///etc/passwd

Press enter or click to view image in full size
but failed :( error url schema is only HTTP or HTTPS.

I tried URL schemas to read internal and make the server perform that actions [file:///, dict://, ftp://, gopher://] but :( Failed!

Press enter or click to view image in full size
Press enter or click to view image in full size

So I Visited the URL but it was not loading the content a simple text file gets reflected and downloaded it was having nothing in it.

Reading AWS Metadata

After doing lots of other things I didn't get any result so I remember about the magic IP of AWS just for hit and try I replaced the URL parameter with the below IP which is the Magic IP used by the AWS.

Craft the URL like this:

https://reducted.com/gadgets/proxy/?url=http://169.254.169.254/latest/meta-data
Press enter or click to view image in full size

This downloaded a reducted.txt file and open it showed below information

Press enter or click to view image in full size
Press enter or click to view image in full size
AWS Metadata
Mitigation:
Whitelists and DNS Resolution
Input Validation
Response Handling
Disable Unused URL Schemas
Authentication on Internal Services

After seeing the bounty amount I was like..😭😭😭😭😭

References:

https://hackerone.com/reports/53088
https://sanderwind.medium.com/escalating-ssrf-to-rce-7c0147371c40
https://medium.com/@briskinfosec/ssrf-server-side-request-forgery-ae44ec737cb8
https://medium.com/geekculture/ssrf-vulnerability-from-a-developers-perspective-3d1562f29c7c
https://corneacristian.medium.com/top-25-server-side-request-forgery-ssrf-bug-bounty-reports-136928356eca

Thanks for reading. If you have any question you can DM me on Twitter 😊

From Infosec Writeups: A lot is coming up in the Infosec every day that it’s hard to keep up with. Join our weekly newsletter to get all the latest Infosec trends in the form of 5 articles, 4 Threads, 3 videos, 2 Github Repos and tools, and 1 job alert for FREE!
