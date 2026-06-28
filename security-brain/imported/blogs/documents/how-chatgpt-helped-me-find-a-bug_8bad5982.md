---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-04-11_how-chatgpt-helped-me-find-a-bug.md
original_filename: 2023-04-11_how-chatgpt-helped-me-find-a-bug.md
title: How ChatGPT helped me find a bug
category: documents
detected_topics:
- xss
- command-injection
- file-upload
- automation-abuse
- api-security
tags:
- imported
- documents
- xss
- command-injection
- file-upload
- automation-abuse
- api-security
language: en
raw_sha256: 8bad59821501107a497015347b79b27aa33d455722147407b653413e7e1e612d
text_sha256: 22fae64061bffef9754f9908577a4fc16af932dceb5bba858ba16d4c0323aa58
ingested_at: '2026-06-28T07:32:20Z'
sensitivity: unknown
redactions_applied: false
---

# How ChatGPT helped me find a bug

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-04-11_how-chatgpt-helped-me-find-a-bug.md
- Source Type: markdown
- Detected Topics: xss, command-injection, file-upload, automation-abuse, api-security
- Ingested At: 2026-06-28T07:32:20Z
- Redactions Applied: False
- Raw SHA256: `8bad59821501107a497015347b79b27aa33d455722147407b653413e7e1e612d`
- Text SHA256: `22fae64061bffef9754f9908577a4fc16af932dceb5bba858ba16d4c0323aa58`


## Content

---
title: "How ChatGPT helped me find a bug"
url: "https://abhishekgk.medium.com/how-chatgpt-helped-me-find-a-bug-b5a3795c722"
authors: ["Abhishekgk"]
bugs: ["XSS", "File upload"]
bounty: "200"
publication_date: "2023-04-11"
added_date: "2023-04-29"
source: "pentester.land/writeups.json"
original_index: 1274
scraped_via: "browseros"
---

# How ChatGPT helped me find a bug

How ChatGPT helped me find a bug
Abhishekgk
Follow
4 min read
·
Apr 11, 2023

471

8

Hello and welcome to my latest Medium writeup! I’m thrilled to share my thoughts and insights with you today on How I used chatgpt to find a bug easily. Since, the application is private program, I had to follow non-disclosure, and had to modify the burp poc, target details etc. For now, lets call the target redacted.com

I usually start my hacking with basic reconnaisance, gaining info on the targets functionalities, parameters, pages and reading JS code for sensitive info.

After manually scraping the target, to get endpoints in my burp, I always use these tools, to reduce manual work of reading through the JS codes:
1) Gospider ( which can be downloaded by “apt install gospider” )

2) Katana ( A tool by Project Discovery ).

After running these tools on the target, i got many hidden endpoints, one of them looks like this:

/api/REDACTED/upload.php

I then went back to my burp requests, and also checked the entire application to find a file upload feature, which sends request to the above api path. Unfortunately, there was no file upload feature in the application at all. There may be a chance that the application removed the file upload feature from the application, but forgot to restrict the api request to the path. I then decided to manually try to make a request to upload a file to the path. Since, i dont know how to construct a upload request from scratch, i asked chatgpt to generate the request for me. Please, do not ask chatgpt to generate any malicious files, As i mentioned earlier, the poc’s will be modified.

Press enter or click to view image in full size
chatgpt generated sample burp request.

I then, copied this request to my burp, modified it a little bit, to adjust it according to my target, and tried to send the request to check if it got uploaded.

Press enter or click to view image in full size
File successfully uplaoded.

And, I got the uploaded file path from the response, but the target, was not executing any payload i uploaded, instead it was just echoing out the content of the file i uploaded. I tried this with different file extensions, and still did not work. Finally i bruteforced the file content type using intruder, to know what file types are allowed. I came to know that only pdf files are accepted.

Get Abhishekgk’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

I almost decided to give up, as i thought there is no other way to show potential impact with uploading a pdf file, without uploading any malware in it.

Now, after few days I started to research on this topic, and interacting with chatgpt i came to know that xss via pdf file upload is possible, and it guided me through this link. This is an amazing link from portswigger. Adding Javascript code to the pdf content, was new to me.

You can also refer to this link, which also helped me in creating the pdf file.

Press enter or click to view image in full size
modifying pdf to add xss payload.

After submitting this payload to the target , i got the alert on the target file path

Press enter or click to view image in full size
xss executed.

I reported it to the company, and since the file was executed on a entirely different domain, and it did not affect the target which reduced the severity. However, the application allowing arbitrary file to get uploaded, was the main issue here, and i got rewarded for it.

reward for the issue.

Hope you got something new to learn from this writeup, as now, i have a new method for cross site scripting, which i can use in my everyday hunting , and pentesting.

Thank you
