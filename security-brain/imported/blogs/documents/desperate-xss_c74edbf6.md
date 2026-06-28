---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-07-31_desperate-xss.md
original_filename: 2023-07-31_desperate-xss.md
title: Desperate XSS
category: documents
detected_topics:
- xss
- command-injection
- otp
- csrf
tags:
- imported
- documents
- xss
- command-injection
- otp
- csrf
language: en
raw_sha256: c74edbf60ff50b742f509f8b7347cd9d7a7d5df469f00b96026bc19e65fb5b40
text_sha256: 20c85931137fd436a7892b5bf4d5814ad0d9d8b867f05e0a8b6f76029fc2e873
ingested_at: '2026-06-28T07:32:24Z'
sensitivity: unknown
redactions_applied: false
---

# Desperate XSS

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-07-31_desperate-xss.md
- Source Type: markdown
- Detected Topics: xss, command-injection, otp, csrf
- Ingested At: 2026-06-28T07:32:24Z
- Redactions Applied: False
- Raw SHA256: `c74edbf60ff50b742f509f8b7347cd9d7a7d5df469f00b96026bc19e65fb5b40`
- Text SHA256: `20c85931137fd436a7892b5bf4d5814ad0d9d8b867f05e0a8b6f76029fc2e873`


## Content

---
title: "Desperate XSS"
url: "https://medium.com/@ramkumarnadar47/desperate-xss-ce3619343f57"
authors: ["Ramkumar Nadar"]
bugs: ["Reflected XSS"]
publication_date: "2023-07-31"
added_date: "2023-08-08"
source: "pentester.land/writeups.json"
original_index: 892
scraped_via: "browseros"
---

# Desperate XSS

Desperate XSS
Ramkumar Nadar
Follow
3 min read
·
Jul 31, 2023

63

1

This application was quite secure and it had this mechanism wherein one request can be sent only once, this validation I think was done by the URL query parameter “OWASP_CSRFTOKEN”. This essentially means you can’t take the request to Repeater and play around with it rather you’re going to have to intercept the request in real-time and inject the payload in the Intercept tab.

Press enter or click to view image in full size

The value of the said token was reflected in the response under the context of a comment.

Having had the reflecting value, I tried and injected the payload appending the token, something to this effect:

.jsp?OWASP_CSRFTOKEN=2F8A-XXXX-XXXX-XXXX/*alert(1)*/

This logged me out of the application.

After a few trials and errors, I learnt that disturbing or changing the value of the token will most definitely throw me out of the application.

Then I got the idea to use the ampersand (&) and inject the value. Something to the below effect:

.jsp?OWASP_CSRFTOKEN=2F8A-XXXX-XXXX-XXXX&/*alert(1)*/

This time I got the reflection of the injected payload and I was not being logged out but the payload was not executing though. I thought the black listing was in play, so I tried many different payloads, but no luck.

Then I began to prepend the payload to try my luck out. Still no cigar.

Get Ramkumar Nadar’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

In my desperation, I injected a new parameter named “xss” and gave it the value of the payload, prepending it to the “OWASP_CSRFTOKEN”.

.jsp?xss=*/prompt("XSS")/*&OWASP_CSRFTOKEN=2F8A-XXXX-XXXX-XXXX

and it worked. Not straight away, but it did.

alert(1) was definitely not working. But prompt(“XSS”) worked before that I actually used another payload. I came under the impression that pop-up payload will just not work with this application, so I researched other ways and found out about this neat payload:

console.log(document.domain)

Using the above, you won’t get a pop-up. Rather, you will have to open the Console in the Developer Tools (Ctrl + Shift + I) in Chrome. If you find that the domain of your application is shown in the Console, it means that the above payload worked.

So above was just a brief explanation of the thought process involved. Let me illustrate the steps simply now;

This is the original request.
Press enter or click to view image in full size

2. Below marked is the injection point, where the payload was injected.

Payload: xss=*/prompt("XSS")/*&
Press enter or click to view image in full size

3. Payload was reflected under the context of a comment. Hence, I had to use the closing comment symbols (*/) and the opening comment symbols (/*). This leaves our prompt(“XSS”) uncommented and primed to execute.

Press enter or click to view image in full size

This got executed. And we have a reflected XSS in our hands which can be shared with the URL.

Thank you for reading!!!
