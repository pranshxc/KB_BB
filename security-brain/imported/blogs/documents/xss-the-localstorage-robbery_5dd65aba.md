---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-04-12_xss-the-localstorage-robbery.md
original_filename: 2022-04-12_xss-the-localstorage-robbery.md
title: XSS - The LocalStorage Robbery
category: documents
detected_topics:
- xss
- command-injection
- file-upload
- otp
- csrf
tags:
- imported
- documents
- xss
- command-injection
- file-upload
- otp
- csrf
language: en
raw_sha256: 5dd65abad9ca6392da717ba813bcbe8f9066fd2ee966b7f61586f14b23a1c542
text_sha256: c66011b5e733a996349a812c96b411201b3cf7cb83ffbd19617588e6d8e1cfc2
ingested_at: '2026-06-28T07:32:11Z'
sensitivity: unknown
redactions_applied: false
---

# XSS - The LocalStorage Robbery

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-04-12_xss-the-localstorage-robbery.md
- Source Type: markdown
- Detected Topics: xss, command-injection, file-upload, otp, csrf
- Ingested At: 2026-06-28T07:32:11Z
- Redactions Applied: False
- Raw SHA256: `5dd65abad9ca6392da717ba813bcbe8f9066fd2ee966b7f61586f14b23a1c542`
- Text SHA256: `c66011b5e733a996349a812c96b411201b3cf7cb83ffbd19617588e6d8e1cfc2`


## Content

---
title: "XSS - The LocalStorage Robbery"
url: "https://shahjerry33.medium.com/xss-the-localstorage-robbery-d5fbf353c6b0"
authors: ["Jerry Shah (@Jerry)", "ethicalbughunter (@ethicalbughuntr)"]
bugs: ["XSS"]
publication_date: "2022-04-12"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 2723
scraped_via: "browseros"
---

# XSS - The LocalStorage Robbery

XSS - The LocalStorage Robbery
Jerry Shah (Jerry)
Follow
5 min read
·
Apr 12, 2022

241

4

Press enter or click to view image in full size

Summary :

In brief, stored (persistent) cross-site scripting (XSS) happens when an attacker injects malicious code into the target application and this content is permanently stored. Later, when victims visit a page with the stored malicious code, their browsers execute this code.

Description :

Me and my friend ethicalbughunter were hunting on a private program. This program had an import feature where we can upload document files like .csv or .docx and when we clicked that import function to choose the file from our desktop, it showed “All Supported Types” because we can only import document files. So we changed “All Supported Types” to “All Files” on our desktop and uploaded a file with .svg extension which contained XSS payload in xml script.

At first the file was simply uploaded and nothing happened, we were not able to find the path where the file was upload. So we repeated the same steps again and this time we intercepted the response of the file upload request where we were able to find the path. We visited the path and found a stored XSS.

After looking at the authentication flow we noticed that an authentication token is generated on every login and is unique for every account. The token was getting stored in LocalStorage and that token was also protecting the website from CSRF attacks. Now the question was how should we steal the token from localstorage ? because if we manage to do so we can probably craft different other attacks. So in our .svg file we added a line to steal a token from the localstorage prompt(alert(localStorage.getItem(“<item-name>”))); and uploaded the file. When we visited the path we were successfully able to steal the token from the localstorage.

What is local storage ?

Local storage is an object of web storage which is used to store data locally within the user’s browser. It was introduced by HTML5 and before HTML5 the application data had to be stored in cookies, included in every server request. Using web storage large amounts of data can be stored locally, without affecting website performance.

Compared to cookies, the storage limit is far larger (at least 5MB) and information is never transferred to the server. Web storage is per origin (per domain and protocol). All pages, from one origin, can store and access the same data.

Press enter or click to view image in full size
Browser Support

HTML web storage provides two objects for storing data on the client :

window.localStorage - stores data with no expiration date

The localStorage object stores the data with no expiration date. The data will not be deleted when the browser is closed and will be available the next day, week or year.

2. window.sessionStorage - stores data for one session (data is lost when the browser tab is closed)

The sessionStorage object is equal to the localStorage object, except that it stores the data for only one session. The data is deleted when the user closes the specific browser tab.

How we found this vulnerability ?

We found an import feature
Press enter or click to view image in full size
Import feature
Press enter or click to view image in full size
Import feature

2. We clicked on the “Start Import” button to upload a file and it showed me “All Supported Types”

Press enter or click to view image in full size
All Supported Types

3. We changed the “All Supported Types” to “All File” on my desktop to upload .svg file

Press enter or click to view image in full size
All Files

4. Then we uploaded the .svg file and intercepted the request using burp

Press enter or click to view image in full size
Intercepted Request

5. We chose an option Do intercept > Response to this request, to check where the file is being uploaded

Press enter or click to view image in full size
Intercepting the Response
Press enter or click to view image in full size
File Path

6. Then we visited the path and found the stored XSS and we were successfully able to steal the token from localStorage

Press enter or click to view image in full size
prompt(‘XSS-Attack’);
Press enter or click to view image in full size
prompt(document.domain);
Press enter or click to view image in full size
prompt(document.cookie);
Press enter or click to view image in full size
prompt(alert(localStorage.getItem(“IsvSessionToken”)));

Payload Used :

Get Jerry Shah (Jerry)’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

<?xml version=”1.0" standalone=”no”?>
<!DOCTYPE svg PUBLIC “-//W3C//DTD SVG 1.1//EN” “http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd">

<svg version=”1.1" baseProfile=”full” xmlns=”http://www.w3.org/2000/svg">
<polygon id=”triangle” points=”0,0.0,50.50,0" fill=”#009900" stroke=”#004400"/>
<script type=”text/javascript”>
prompt(‘XSS-Attack’);
prompt(document.domain);
prompt(document.cookie);
prompt(alert(localStorage.getItem(“IsvSessionToken”)));
</script>
</svg>

Note : You need to change the item name of the localStorage.

Why this happened ?

In my opinion, it happened because of three reasons

While uploading the file, the extension was not being checked
After the file was uploaded, Content-Type validation was not done
After the file was sent to the server, it was not being validated by the server

Impact :

An attacker can steal the authentication token of any user and can craft different attacks like csrf, session attacks, account take over etc.

The impact depends on what kind of information was being stored in localStorage.

Calculated CVSS :

Vector String : CVSS:3.0/AV:N/AC:L/PR:N/UI:R/S:C/C:H/I:L/A:N

Score - 8.2 (High)

Mitigation :

Website should allow non-executable extensions as well as content-type validation and server side check should be performed to mitigate this kind of issues.

Bounty Reward :

1250 USD

Collaboration was done with :

ethicalbughuntr

Press enter or click to view image in full size
