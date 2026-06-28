---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-01-08_create-post-on-any-facebook-page.md
original_filename: 2021-01-08_create-post-on-any-facebook-page.md
title: Create post on any Facebook page
category: blogs
detected_topics:
- idor
- command-injection
- graphql
- api-security
tags:
- imported
- blogs
- idor
- command-injection
- graphql
- api-security
language: en
raw_sha256: 0a4eb7156b8985c07daae5c4d0032cf2d738212a0c81c29d4c0ec554b7b80f5e
text_sha256: 2ef9d14742a8ce4b3c27f7a615c6dde4686e0d098621436a8d1666f457d288fa
ingested_at: '2026-06-28T07:32:04Z'
sensitivity: unknown
redactions_applied: false
---

# Create post on any Facebook page

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-01-08_create-post-on-any-facebook-page.md
- Source Type: markdown
- Detected Topics: idor, command-injection, graphql, api-security
- Ingested At: 2026-06-28T07:32:04Z
- Redactions Applied: False
- Raw SHA256: `0a4eb7156b8985c07daae5c4d0032cf2d738212a0c81c29d4c0ec554b7b80f5e`
- Text SHA256: `2ef9d14742a8ce4b3c27f7a615c6dde4686e0d098621436a8d1666f457d288fa`


## Content

---
title: "Create post on any Facebook page"
page_title: "Create post on any Facebook page
  | 
  Dynamic World"
url: "https://www.darabi.me/2020/12/create-invisible-post-on-any-facebook.html"
final_url: "https://www.darabi.me/2020/12/create-invisible-post-on-any-facebook.html"
authors: ["Pouya Darabi (@Pouyadarabi)"]
programs: ["Meta / Facebook"]
bugs: ["IDOR"]
bounty: "30,000"
publication_date: "2021-01-08"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4014
---

#  Create post on any Facebook page 

[ 2020 ](https://www.darabi.me/search/label/2020) [ bounty ](https://www.darabi.me/search/label/bounty) [ bug ](https://www.darabi.me/search/label/bug) [ bugbounty ](https://www.darabi.me/search/label/bugbounty) [ bypass ](https://www.darabi.me/search/label/bypass) [ critical ](https://www.darabi.me/search/label/critical) [ facebook ](https://www.darabi.me/search/label/facebook) [ hack ](https://www.darabi.me/search/label/hack) [ roles ](https://www.darabi.me/search/label/roles) [ vulnerability ](https://www.darabi.me/search/label/vulnerability)  
__ Pouya  __[ 12:17 PM  ](https://www.darabi.me/2020/12/create-invisible-post-on-any-facebook.html "permanent link") __[ 1 comment ](https://www.darabi.me/2020/12/create-invisible-post-on-any-facebook.html#comment-form)

  

Create an invisible post on any Facebook page

  

  

![page vulnerability](https://cdn.darabi.me/cdn/2020/post_on_pages.jpg)

  

  

  

  

You may know that you can create many types of posts on your Facebook feed. one of them is called "invisible" (unlisted) which unlike other types cannot be seen on your feed, but like others, it has a link and id.

  

These types of posts are not shown on the feed timeline but are accessible via a direct link. the main impact of these types of posts is that the page admins cannot view or delete them since they don't have any links.

An attacker can use the post sharing feature to send it to others.

  

![Share Feature](https://cdn.darabi.me/cdn/2020/share.png)

  

At [Creative Hub](https://www.facebook.com/ads/adbuilder/) we can create ads and use collaboration to complete them. Facebook creates an invisible post on the selected page for previewing them to the users.

I intercepted the request and change the "page_id" to the victim's "page_id" and it saves without any error or issue.

![Permission Error Creative Hub](https://cdn.darabi.me/cdn/2020/request.png)

  

  

![Permission Error Creative Hub](https://cdn.darabi.me/cdn/2020/perm_error.jpg)

  

The permission here has been checked before generating the preview so you should definitely have the advertiser role. (above image)

  

Also, the _[Share Feature](https://www.facebook.com/business/help/1841051492794621?id=2060787407580250)_ (image below) has been added to Facebook's Creative Hub recently, therefore, I started digging deeper into it again.

After clicking on the share button the API will answer with a new shareable URL like this:

> https://www.facebook.com/ads/previewer/__PREVIEW_KEY__ 

  

![Creative Hub](https://cdn.darabi.me/cdn/2020/creativehub.jpg)

  

  

The gotcha is that the permission-check is missing before generating a preview post on the share page.

Changing page_id before saving the mockup in Graphql request and then getting back the sharable link for it, gives us the ability to create a post on any page. All we need to do is to find the post_id that exists on any ad preview endpoints.

Finally, we created an invisible post on the victim page without their knowledge!

  

POC:

  

  

Facebook fixed this vulnerability after I reported it but still, I was able to bypass the fix by using another approach.

> // This request will create a post page plus sending a notification to the mobile device
> 
> AsyncRequest.post('/ads/previewer/notify_mobile/__PREVIEW_KEY__',{})

The "send to mobile" feature creates a preview again without checking permission.

  

Bypass POC:

  

  

  

  

![Creative Hub](https://cdn.darabi.me/cdn/2020/post_bounty.png)

  

  

  
Timeline:

**November 6, 2020****– Report Sent**

**November 6, 2020********–****Triaged**

**November 11, 2020********–****Fixed**

**November 12, 2020****– Bypass Sent**

**November 12, 2020****– Triaged**

**November 20, 2020********–****Fixed**

**December 16, 2020****–****$30,000 Bounty awarded**  
  

  * [ __ ](https://www.facebook.com/sharer.php?u=https://www.darabi.me/2020/12/create-invisible-post-on-any-facebook.html&t=Create post on any Facebook page "Share on facebook")
  * [ __ ](https://twitter.com/intent/tweet?text=Create post on any Facebook page&url=https://www.darabi.me/2020/12/create-invisible-post-on-any-facebook.html "Share on Twitter")
  * [ __ ](https://pinterest.com/pin/create/button/?url=https://www.darabi.me/2020/12/create-invisible-post-on-any-facebook.html)
  * [ __ ](https://www.linkedin.com/shareArticle?mini=true&url=https://www.darabi.me/2020/12/create-invisible-post-on-any-facebook.html)

[ Older Post ](https://www.darabi.me/2020/06/image-removal-vulnerability-on-facebook.html "Older Post")
  *[
12:17 PM
]: 2021-01-08T12:17:00-08:00
