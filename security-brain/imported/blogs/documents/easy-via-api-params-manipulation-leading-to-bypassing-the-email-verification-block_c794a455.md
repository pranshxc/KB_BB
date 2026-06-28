---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-03-18_easy-via-api-params-manipulation-leading-to-bypassing-the-email-verification-blo.md
original_filename: 2023-03-18_easy-via-api-params-manipulation-leading-to-bypassing-the-email-verification-blo.md
title: Easy $$$ via API params manipulation leading to bypassing the email verification
  block
category: documents
detected_topics:
- api-security
- command-injection
- password-reset
- otp
tags:
- imported
- documents
- api-security
- command-injection
- password-reset
- otp
language: en
raw_sha256: c794a455f346934af6273ab2ca288098c36ac34d64c8a91716e2062e1d7381cf
text_sha256: 0e9c33c72270fea1321d60d9b26a04ce72e1ee7d92cc3b22aa13dfa044cdb583
ingested_at: '2026-06-28T07:32:19Z'
sensitivity: unknown
redactions_applied: true
---

# Easy $$$ via API params manipulation leading to bypassing the email verification block

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-03-18_easy-via-api-params-manipulation-leading-to-bypassing-the-email-verification-blo.md
- Source Type: markdown
- Detected Topics: api-security, command-injection, password-reset, otp
- Ingested At: 2026-06-28T07:32:19Z
- Redactions Applied: True
- Raw SHA256: `c794a455f346934af6273ab2ca288098c36ac34d64c8a91716e2062e1d7381cf`
- Text SHA256: `0e9c33c72270fea1321d60d9b26a04ce72e1ee7d92cc3b22aa13dfa044cdb583`


## Content

---
title: "Easy $$$ via API params manipulation leading to bypassing the email verification block"
url: "https://medium.com/@bag0zathev2/easy-via-api-params-manipulation-leading-to-bypassing-the-email-verification-block-a45dad2db60c"
authors: ["Fares Walid (@SirBagoza)"]
bugs: ["Mass assignment", "Email verification bypass"]
publication_date: "2023-03-18"
added_date: "2023-03-23"
source: "pentester.land/writeups.json"
original_index: 1358
scraped_via: "browseros"
---

# Easy $$$ via API params manipulation leading to bypassing the email verification block

Top highlight

Easy $$$ via API params manipulation leading to bypassing the email verification block
Fares Walid (SirBugs)
Follow
3 min read
·
Mar 18, 2023

335

2

Press enter or click to view image in full size

Hi Boyzz, Hope you are doing well today !! ❤
The talk today is about 1 of my last findings !!
Where I manipulated the API parameters to control the response of the server to me !!
Since I am not permitted to disclose any information about the website yet, and the report is not disclosed cuz It’s a priv8 program .. We are gonna call the website: target.com

First of all .. On the signup request/endpoint in our affected API, I see here in the sign-up request some parameters normally signing me up !!

POST /endpoints/users/register HTTP/2
Host: dashboard.target.com
Cookie: ***REDACTED-SUSPECT-TOKEN***User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:109.0) Gecko/20100101 Firefox/111.0
Accept: application/json
Referer: <https://dashboard.target.com/register?_gl=1*1exXxXxXxXxXxXxXx
Content-Type: application/json
Content-Length: 765
Origin: <https://dashboard.target.com>

{"email_address":"xXxXxXxXx@yopmail.com","password":"xXxXxXxXxXx","is_trial":true,"ga_client_id":"1571714364.1679015602","ga_document_referrer":"<https://www.target.com/","grecaptcha_token":"03AFY_a8VcsIMfvamIr5EgfVHmkeTGDKTlYRLtjFvQ4v2pf5Bb46sS_V2K1fip9gfaqluHmhCBwdGtnThqLgeT-hRu4_8GV39AzUbFKWvStLJNKDdvNRpp1rewGNapK3eOAp_vT5Xv4CYdYsopUpJioeWf4CZDIvw4E58iuYzbKV-fXXEv7ixKAylIGagvipfD5Pf-Ee_4yPLgZJylbEOxdpN-IblC2KvdK404uNo7WK8WwenBL8vVn5rpnqLqBQIJ16qMkfETixC_QKchU8YIreTuUXnnBsMp4bn1-n-Dpn2O-9IfFswxa1ZjK_qLB0gpy-BcYpjJqpfvbsMCEHOMFZMCRdlB4YMnajM4rYu8cCB_gnTajdoUso6Am3T8YThj9aYjGUEP8e0jyaBWYLqMBMbgGRXkIss6FXMRk7-oFi80in4PiacEV7bvZHSimIotTlEjk0Ou6fZ1uxy_sBVYTqPMiqLRAgJlh-SrGHkix55wIGtbVkLSZaLnBF6RuywfwSOHg>"}

But what actually got my looks, is the response here .. Cuz it was:

Press enter or click to view image in full size

Now I though if i can manipulate the parameter called email_verified , and I may be able to change Its value to true on sending the request itself.

I quickly Intercepted the request and added “email_verified”:true, in the post data while signing-up

Now guess what .. It worked totally fine !!

my email is confirmed even I didn’t activate or clicked the activation link !!

Get Fares Walid (SirBugs)’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

As we know when we are asked for a verification we face a page that saying “please verify to continue or something like this blablabla”

But my dashboard is now on and everything is working fine !!

Submitted as Medium, Changed as low Severity.
But anyway I enjoyed it and of course I got a small bounty alhamdulillah ❤

Thank you all for reading and for your time ❤ I wish you had some fun with me and liked this write-up inshallah ❤
as soon as I get something interesting to write about it, I am gonna share it too :D

Have fun and keep digging ❤
My Twitter ❤

Follow me on my github, Recently I am making and posting some new tools that I am making that could really help you guys ❤
My Github ❤
