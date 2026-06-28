---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-02-18_found-an-url-in-the-android-application-source-code-which-lead-to-an-idor.md
original_filename: 2023-02-18_found-an-url-in-the-android-application-source-code-which-lead-to-an-idor.md
title: Found an URL in the android application source code which lead to an IDOR
category: documents
detected_topics:
- mobile-security
- idor
- command-injection
- otp
- rate-limit
- information-disclosure
tags:
- imported
- documents
- mobile-security
- idor
- command-injection
- otp
- rate-limit
- information-disclosure
language: en
raw_sha256: 63e8314493b6bb46ac8c128e4228c043f31d0c21b68133d4ce22bb6ec625de02
text_sha256: 467868542fcbfa4fba389972df65442ca2bec45ce5bda4b29c5ef58c80d5d481
ingested_at: '2026-06-28T07:32:18Z'
sensitivity: unknown
redactions_applied: false
---

# Found an URL in the android application source code which lead to an IDOR

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-02-18_found-an-url-in-the-android-application-source-code-which-lead-to-an-idor.md
- Source Type: markdown
- Detected Topics: mobile-security, idor, command-injection, otp, rate-limit, information-disclosure
- Ingested At: 2026-06-28T07:32:18Z
- Redactions Applied: False
- Raw SHA256: `63e8314493b6bb46ac8c128e4228c043f31d0c21b68133d4ce22bb6ec625de02`
- Text SHA256: `467868542fcbfa4fba389972df65442ca2bec45ce5bda4b29c5ef58c80d5d481`


## Content

---
title: "Found an URL in the android application source code which lead to an IDOR"
url: "https://vengeance.medium.com/found-an-url-in-the-android-application-source-code-which-lead-to-an-idor-1b8768708756"
authors: ["Vengeance"]
bugs: ["Android", "Information disclosure", "IDOR"]
publication_date: "2023-02-18"
added_date: "2023-02-22"
source: "pentester.land/writeups.json"
original_index: 1513
scraped_via: "browseros"
---

# Found an URL in the android application source code which lead to an IDOR

Found an URL in the android application source code which lead to an IDOR
Vengeance
Follow
2 min read
·
Feb 18, 2023

166

2

I was testing the target which had its web application and mobile application in scope. Let’s say the target is example.com

Firstly, I tested its web application which had only one domain in its scope. I found some vulnerabilities in the target web application and reported them to the program (Most of them were duplicates 😅).

Then I moved on to mobile application testing. With the little knowledge and experience I had with android application testing, I used apktool to decompile the android apk file. Then I started diving deep into the source code to see if I can find any hardcoded keys, tokens, or anything useful.

After some time I found a URL in the source code which I had not seen while testing the web application. The URL was “https://example.com/getCustomerInfo?loginToken=”

Found URL in android application

To automate the process, Apkleaks can be used to scan APK files for URIs, endpoints & secrets.

Immediately I entered a random value in loginToken parameter and checked if I got any information. But the server responded with a 500 status code.

Get Vengeance’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Then I began to check burp history to see if any previous HTTP request or response contains any loginToken value. After some time I got an id parameter in the HTTP response with a numerical value. The response of /user/get-finance-user had an id parameter whose value can be used as a value of loginToken parameter.

Press enter or click to view image in full size
Response of /user/get-finance-user containing an id parameter value

After using the value from the id parameter as a value of loginToken parameter I got my information in the response.

Press enter or click to view image in full size
Personal information is displayed

Then I used the burp intruder to brute force the loginToken value and got all the available information of the customers.

Bruteforcing the loginToken value

So checking only the source code of an android application helped me to find a new endpoint through which I was able to find an IDOR vulnerability in the web application.

Even though you don't plan to test the mobile application, reviewing the source code can provide you with useful information.

Thanks for reading.

Twitter: Vengeance0x0
