---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2019-12-24_graphql-idor-leads-to-information-disclosure.md
original_filename: 2019-12-24_graphql-idor-leads-to-information-disclosure.md
title: GraphQL IDOR leads to information disclosure
category: documents
detected_topics:
- idor
- graphql
- xss
- command-injection
- path-traversal
- mfa
tags:
- imported
- documents
- idor
- graphql
- xss
- command-injection
- path-traversal
- mfa
language: en
raw_sha256: fd604f34f2b7e903eaaa08f9c0ea92b56a201744964d94100365dcc60783ab0a
text_sha256: 29765017a2b88292bb792774bfcef8e7d3760758ec78e20d2276937902529a00
ingested_at: '2026-06-28T07:32:00Z'
sensitivity: unknown
redactions_applied: true
---

# GraphQL IDOR leads to information disclosure

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2019-12-24_graphql-idor-leads-to-information-disclosure.md
- Source Type: markdown
- Detected Topics: idor, graphql, xss, command-injection, path-traversal, mfa
- Ingested At: 2026-06-28T07:32:00Z
- Redactions Applied: True
- Raw SHA256: `fd604f34f2b7e903eaaa08f9c0ea92b56a201744964d94100365dcc60783ab0a`
- Text SHA256: `29765017a2b88292bb792774bfcef8e7d3760758ec78e20d2276937902529a00`


## Content

---
title: "GraphQL IDOR leads to information disclosure"
url: "https://medium.com/bugbountywriteup/graphql-idor-leads-to-information-disclosure-175eb560170d"
authors: ["Eshan Singh (@R0X4R)"]
bugs: ["IDOR"]
publication_date: "2019-12-24"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4870
scraped_via: "browseros"
---

# GraphQL IDOR leads to information disclosure

GraphQL IDOR leads to information disclosure
Eshan Singh
Follow
3 min read
·
Dec 24, 2019

368

Press enter or click to view image in full size

Hello World!, I’m Eshan Singh aka R0X4R. I’m here to share my recent findings on GraphQL IDOR (Insecure Direct Object Reference), which leads to information disclosure. So, let’s start. I’m signing in…

What is GraphQL?

The GraphQL Foundation defines “GraphQL is an open-source data query and manipulation language for APIs, and a runtime for fulfilling queries with existing data.” Nowadays, GraphQL is being used in place of Rest-API’s.

Vulnerability

While doing recon for redacted.com (A private program and as per their privacy policies, I cannot disclose their name), I found that the web app is using GraphQL for their API Management.

Get Eshan Singh’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

So, I firstly tried Introspection Query to extract sensitive information. After passing the query I saw a field called Users, so I pass

Query: {__type (name: \”Users\”) {name fields{name type{name kind ofType{name kind}}}}}”}

the query to enumerate the Types` definition in the field “Users”, then I saw _type “Users” contains some fields i.e., Email, mobile_number, user_id, location, and api_key. So, I pass one more query to extract information those fields carried but I got 403 Unauthorised response.

Query: {Users{email,mobile_number,user_id,api_key}}
Source: https://imgflip.com/memetemplate/100827024/Sad-meme

So, I thought that this web app is not vulnerable, so I started hunting for XSS. I clicked on My Profile, then I edited my name and intercepted the request, then I saw something interesting; the web app extracts previous info of the user before requesting a new edit.

Request: {“operationName”:”CurrentUserData”,”variables”:{“id”:” — base64 encode — “},”query”:”query CurrentUserData($id: ID!) {\n User(id: $id) {\n id\n email\n name\n mobile_number\n apiHostUrl\n SiteAdminUrl\n pages(first: 50) {\n nodes {\n id\n faviconUrl\n name\n code\n manageUrl\n __typename\n }\n __typename\n }\n __typename\n }\n}\n”}

So, I sent that request to the repeater and in that request, there is a variable called “id”, which contains something in base64. So, I decode that base64 encoded string

Decode: oph:cloud:redacted::user/p5yhwx30
First Account: r0x4r@hhacker.com
Second Account: bcr_rox4r@hacker.com

“P5yhwx30” is my “id.” So, I created one more account on redacted.com and copied its “id: oph:cloud:redacted::user/d5mzk1m2”.

Source: https://winkgo.com/wp-content/uploads/2019/03/happy-memes-make-you-smile-more-02.jpg?ezimgfmt=ng:webp/ngcb3

Then I logged out from my second account and logged in with my first account. Now I pass the same query, but I changed my “id” with my second “id” and boom! I got the information.

Press enter or click to view image in full size
Source: https://me.me/i/oh-yeah-meme-creator-funny-oh-yeah-meme-generator-***REDACTED-SUSPECT-TOKEN***But there’s a problem waiting for me that how I get another user “id.” So, after enumerating, I found that the “id” of the other users is in their profile page source code. I just have to go to their profile and view the source of their profile page, then I searched for “var_userID,” and I got their “id.”

source: https://media1.tenor.com/images/17d912fad3b04c322b0c2678adeccf97/tenor.gif?itemid=10323706

Disclosure:

Reported to redacted.com on 15 Nov 2019

They rewarded me with 3 Digits bounty on 07 Dec 2019.

Thanks and regards!

Eshan Singh aka R0X4R

Signing out…
