---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2019-01-27_a-short-tale-of-account-verification-bypass.md
original_filename: 2019-01-27_a-short-tale-of-account-verification-bypass.md
title: A short tale of Account verification bypass
category: documents
detected_topics:
- jwt
- access-control
- command-injection
- password-reset
- otp
tags:
- imported
- documents
- jwt
- access-control
- command-injection
- password-reset
- otp
language: en
raw_sha256: 571de49391856f6ca3ba8973685b80e0fb2c918168bdb943ad589abf0543566d
text_sha256: a06b341fd0547dbfe837bfebdbe565be95177b94be0ca1e1af3c9f4918cbaf6a
ingested_at: '2026-06-28T07:31:58Z'
sensitivity: unknown
redactions_applied: false
---

# A short tale of Account verification bypass

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2019-01-27_a-short-tale-of-account-verification-bypass.md
- Source Type: markdown
- Detected Topics: jwt, access-control, command-injection, password-reset, otp
- Ingested At: 2026-06-28T07:31:58Z
- Redactions Applied: False
- Raw SHA256: `571de49391856f6ca3ba8973685b80e0fb2c918168bdb943ad589abf0543566d`
- Text SHA256: `a06b341fd0547dbfe837bfebdbe565be95177b94be0ca1e1af3c9f4918cbaf6a`


## Content

---
title: "A short tale of Account verification bypass"
url: "https://medium.com/@satboy.fb/a-short-tale-of-account-verification-bypass-22045b38a8b1"
authors: ["Satyendra Kumar"]
bugs: ["Email verification bypass", "Broken authorization"]
publication_date: "2019-01-27"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5446
scraped_via: "browseros"
---

# A short tale of Account verification bypass

A short tale of Account verification bypass
BugDisclose
Follow
2 min read
·
Jan 27, 2019

151

2

Hi
folks, This is Satyendra an occasionally bug hunter by mood. I think the time is most important and coming up to the point without wasting your time.
So, once I was testing a private program in the hope to get some bucks for coffee. I saw scopes of the program and collected some subdomains etc etc..and started with the main domain.
Well, I visited the main domain and scrolled the whole page for checking which types of shits the main page having and I found 2 action buttons login and signup + an email newsletter and some company info blah blah blah…

I decided to explore more and clicked on the signup button to create an account and after entering all the required details I submit the signup form and got a popup to verify email and I said, ok boss, let me verify.
I opened the mailbox and copy the verification link because of that time I was wondering about what kind of information is contained by the link. I was looking closely into the verification link which had a parameter and contained some code string like xxx.yyy.zzz, I decided to know about this encoding and started digging deeper about the encoding in Google.

Finally, I got the clue about the string that is a JWT means JSON WEB TOKEN.

According to Google —
JSON Web Token (JWT) is an open standard (RFC 7519) that defines a compact and self-contained way for securely transmitting information between parties as a JSON object. This information can be verified and trusted because it is digitally signed.

Get BugDisclose’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

My next target was to crack the encoding and simply I googled JWT found a web application in the first result of google. https://jwt.io/ which is basically used for JWT decoding.

Press enter or click to view image in full size
Example

Here common sense comes into play — I pasted my JWT code into jwt.io and the result was something look like -
{
blah blah blah……
“name”: “yourname”,
“email”: redacted@gmail.com
blah blah blah…….
}

Simply I went for new signup and again I got a new verification email but this time I didn’t verify email simply I changed email ID in the previous JWT in jwt.io and copied the new generated JWT from jwt.io

I used that crafted JWT in the verification parameter and hit enter the result was nice! successfully bypassed verification because of the server was not validating JWT correctly with signature and server only validate to the email encoded in the JWT.

Keypoint —
Always analyze encodings and encryptions and try to understand the implemented mechanism.

Hope you guys learn something from this writeup.
Happy Hacking
Thank You :)
