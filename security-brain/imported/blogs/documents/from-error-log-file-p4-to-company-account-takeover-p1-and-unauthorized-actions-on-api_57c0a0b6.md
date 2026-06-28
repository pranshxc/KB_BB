---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-01-17_from-error_log-filep4-to-company-account-takeoverp1-and-unauthorized-actions-on-.md
original_filename: 2023-01-17_from-error_log-filep4-to-company-account-takeoverp1-and-unauthorized-actions-on-.md
title: From Error_Log File(P4) To Company Account Takeover(P1) and Unauthorized Actions
  On API
category: documents
detected_topics:
- idor
- access-control
- command-injection
- otp
- rate-limit
- information-disclosure
tags:
- imported
- documents
- idor
- access-control
- command-injection
- otp
- rate-limit
- information-disclosure
language: en
raw_sha256: 57c0a0b654a8d3a2a5dc40bcf7cf84e8c36dddf896e19d9e6930de50d94f7cb7
text_sha256: 9c1e97fcf081ea7a515963155df619a0a97f3d1ef6f8af26261d1d8eff1849e1
ingested_at: '2026-06-28T07:32:17Z'
sensitivity: unknown
redactions_applied: true
---

# From Error_Log File(P4) To Company Account Takeover(P1) and Unauthorized Actions On API

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-01-17_from-error_log-filep4-to-company-account-takeoverp1-and-unauthorized-actions-on-.md
- Source Type: markdown
- Detected Topics: idor, access-control, command-injection, otp, rate-limit, information-disclosure
- Ingested At: 2026-06-28T07:32:17Z
- Redactions Applied: True
- Raw SHA256: `57c0a0b654a8d3a2a5dc40bcf7cf84e8c36dddf896e19d9e6930de50d94f7cb7`
- Text SHA256: `9c1e97fcf081ea7a515963155df619a0a97f3d1ef6f8af26261d1d8eff1849e1`


## Content

---
title: "From Error_Log File(P4) To Company Account Takeover(P1) and Unauthorized Actions On API"
url: "https://medium.com/@mohanad.hussam23/from-error-log-file-p4-to-company-account-takeover-p1-and-unauthorized-actions-on-api-35e45e43273a"
authors: ["Muhanad Israiwi (@IsrewyMohand)"]
bugs: ["Information disclosure"]
publication_date: "2023-01-17"
added_date: "2023-03-08"
source: "pentester.land/writeups.json"
original_index: 1658
scraped_via: "browseros"
---

# From Error_Log File(P4) To Company Account Takeover(P1) and Unauthorized Actions On API

From Error_Log File(P4) To Company Account Takeover(P1) and Unauthorized Actions On API
Muhanad Israiwi
Follow
2 min read
·
Jan 18, 2023

309

2

Hi Everyone,My name is Muhanad Israiwi.
I’m Bug Bounty Hunter, I'm Student At Amman Arab University.

I was working On Program we can call it (Aex-Target),The Target has domain which we will can call it *.aex-target.com

What Basically I do every time I go hunting is Subdomain-Enumeration,Collect and Sort The result in one file

-Some Subdomain-Enumeration Tools:

Findomain,Sublist3r,Amass,Subfinder

Command For Sorting,Removing Duplicates and Saving Results In new_file.txt or you can use tool called anew from tomnomnom

cat file.txt | sort -u > new_file.txt

Using Httpx I filtered The Live Subdomains and Save it in Result.txt

Then I did Fuzzing On The Live Subdomains which is saved in Result.txt from before.

-Tools You Can Use For Directory Fuzzing
1-FFuf,Dirsearech,wfuzz Tools With World_List or any List You Have.

After Doing Fuzzing I found error_log File In one of the Subdomains which was like this
Vulnerable-File:https://aex-target.com/log.txt

Inside Of The File it was a lot of errors and dummy information,but I noticed Some Request Headers Locking Like This:

{
 Authorization: Token ***REDACTED***
 Accept: application/json
 singularityheader: appId=64xx
 Content-Type: application/json; charset=utf-8
 Content-Length: 23
}

After I found these Information I started searching inside log.txt for any API-Endpoints so I can use Request Header With It.

To do This I just Press CTRL+F and search for /api/ and I found API-Endpoint like This One
or you can use a command to extract Urls From The File.

Get Muhanad Israiwi’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

So,I Found API-Endpoint Locking Like This

https://xxxUpload.com/api/encodingjobs/1xx9788/

When I navigate To The API-Endpoint which is https://xxxUpload.com/api/encodingjobs/179788/
It Return

{“detail”:”Authentication credentials were not provided.”}
So You know what is that mean 😀 ,Let’s use the Request Headers to try to get Authenticated.

[+]Exploits

1-I tried sending This Request Using curl

I was able to view all the Encoding jobs Using The Authentication Token

curl “https://xxxUpload.com/api/encodingjobs/" -H “Authorization: Token ***REDACTED***”

But That’s not Enough to Be High impact,So I did an API-Endpoints Fuzzing Using Using Dirsearech with List Of API-Endpoints You can get it from here API-World_List .

I Discovered These Endpoints:
https://xxxUpload.com/api/groups/
https://xxxUpload.com/api/devices/
https://xxxUpload.com/api/networktypes/
https://xxxUpload.com/api/products/

I started Using The same curl request ,but changing the API-Endpoints with the new one I Found

Viewing All Devices Inside The Accounts
https://xxxUpload.com/api/devices/

Viewing All Groups Inside The Accounts
https://xxxUpload.com/api/groups/

Viewing All Products Inside The Accounts
https://xxxUpload.com/api/products/

Hope It was helpful and Good Write Up.😀
You can follow me,ask me on Linkedin,Twitter

Thanks For Reading.
