---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2019-07-28_chaining-cache-poisoning-to-stored-xss.md
original_filename: 2019-07-28_chaining-cache-poisoning-to-stored-xss.md
title: Chaining Cache Poisoning To Stored XSS
category: documents
detected_topics:
- xss
- command-injection
- rate-limit
- api-security
tags:
- imported
- documents
- xss
- command-injection
- rate-limit
- api-security
language: en
raw_sha256: 8576c3dc4c64a4bac14698ca411f36e5451f7594a934e6c48259940f2aeea6fd
text_sha256: 9760b1aee05681913305a4bb2a03be9c96a84085b1e80af6cb2455ca18ef4d74
ingested_at: '2026-06-28T07:32:00Z'
sensitivity: unknown
redactions_applied: false
---

# Chaining Cache Poisoning To Stored XSS

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2019-07-28_chaining-cache-poisoning-to-stored-xss.md
- Source Type: markdown
- Detected Topics: xss, command-injection, rate-limit, api-security
- Ingested At: 2026-06-28T07:32:00Z
- Redactions Applied: False
- Raw SHA256: `8576c3dc4c64a4bac14698ca411f36e5451f7594a934e6c48259940f2aeea6fd`
- Text SHA256: `9760b1aee05681913305a4bb2a03be9c96a84085b1e80af6cb2455ca18ef4d74`


## Content

---
title: "Chaining Cache Poisoning To Stored XSS"
url: "https://medium.com/@nahoragg/chaining-cache-poisoning-to-stored-xss-b910076bda4f"
authors: ["Rohan aggarwal (@nahoragg)"]
bugs: ["Web cache poisoning", "Stored XSS"]
publication_date: "2019-07-28"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5118
scraped_via: "browseros"
---

# Chaining Cache Poisoning To Stored XSS

Top highlight

Chaining Cache Poisoning To Stored XSS
Rohan Aggarwal
Follow
3 min read
·
Jul 28, 2019

1K

3

One of the benefits of being a developer is that you can guess how stuff is working at the server end. You can try to debug how the developer might have coded a certain functionality or how he might have configured his application, especially in the case where the application is built in some framework or CMS.

For example, many developers using Rails framework use Scaffold to quickly generate major pieces of application like model, views and controller in a single operation. Besides this, Scaffold also creates JSON API endpoint for each route automatically which is most of the time overlooked by the devs or they forgot to remove this JSON endpoint while pushing to production.

So a dev who removed sensitive information from a normal route, might forget to remove the same from JSON endpoint of that route. Checking such misconfiguration might leak some sensitive data in a rails application. Therefore, having knowledge about the application technology really gives you differential findings than others.

Recently, I came across a Drupal application in a bug bounty program on Hackerone. Since I’ve used drupal before, I started looking for some common misconfigurations related to drupal. And within 10 minutes, I found one.

If you’ve developed on drupal before, you might know that it has it’s own internal caching system which is enabled by default. Easiest way to find whether caching is enabled is to look for x-drupal-cache header in the response. So you give unique key(endpoint + parameters) in request and in response you get x-drupal-cache: MISS header but if you request again with that same key and you get x-drupal-cache: HIT header in the response, caching is enabled. To learn more about how caching works and its exploitation, read this by albinowax.

After I came to knew that caching is enabled, one of the ways I can exploit is by poisoning the cache with XSS payload. But to do that I need to find an HTTP header that gets reflected in the response. Since drupal just like any other PHP framework sometimes supports X-Original-URL and X-Rewrite-URL headers because of Zend, I tried injecting these headers in request but sadly the application wasn’t accepting. What to do now? If nothing works, try brute-forcing.

So I used a burp suite extension called Param Miner which will brute force common headers. After few seconds I got a hit. It found a header named style which was getting reflected in response. I quickly checked whether it’s vulnerable to XSS and it was.

After that, I knew I can easily chain cache poisoning to stored XSS. I created a unique key & added style header with XSS payload and fired the request.

Press enter or click to view image in full size

The response with XSS payload is cached for the above unique request. Now whenever someone visits www.redacted.com/?q=admin&liec4897=1, our poisoned response will be served by drupal resulting in Stored XSS.

Get Rohan Aggarwal’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

That’s it. A simple drupal misconfiguration leads to Stored XSS.

TIMELINE

Jun 14, 2019 — Report Submitted

Jun 15, 2019 — Triaged

Jul 12, 2019 — Resolved

Jul 13, 2019 — Rewarded

If you found this post useful in any way, make it useful for others as well by sharing. More coming.

Check if a website is scam or legit WebSafely.net
