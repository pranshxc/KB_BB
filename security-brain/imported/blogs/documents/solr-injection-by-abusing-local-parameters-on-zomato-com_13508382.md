---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2019-07-27_solr-injection-by-abusing-local-parameters-on-zomatocom.md
original_filename: 2019-07-27_solr-injection-by-abusing-local-parameters-on-zomatocom.md
title: Solr Injection by abusing Local Parameters on Zomato.com
category: documents
detected_topics:
- sqli
- command-injection
- api-security
- cloud-security
tags:
- imported
- documents
- sqli
- command-injection
- api-security
- cloud-security
language: en
raw_sha256: 135083822817d9e560e81913d79e6926539b02ac3d42769d631270bfd85c1f2b
text_sha256: 021d21ec7299a398df9e14dd395dac966ca3fe6c0ea8329ac533c568f57193a5
ingested_at: '2026-06-28T07:32:00Z'
sensitivity: unknown
redactions_applied: false
---

# Solr Injection by abusing Local Parameters on Zomato.com

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2019-07-27_solr-injection-by-abusing-local-parameters-on-zomatocom.md
- Source Type: markdown
- Detected Topics: sqli, command-injection, api-security, cloud-security
- Ingested At: 2026-06-28T07:32:00Z
- Redactions Applied: False
- Raw SHA256: `135083822817d9e560e81913d79e6926539b02ac3d42769d631270bfd85c1f2b`
- Text SHA256: `021d21ec7299a398df9e14dd395dac966ca3fe6c0ea8329ac533c568f57193a5`


## Content

---
title: "Solr Injection by abusing Local Parameters on Zomato.com"
url: "https://medium.com/@ronak_9889/solr-injection-by-abusing-local-parameters-on-zomato-com-a5cb7bef10d5"
authors: ["Ronak Patel (@ronak_9889)"]
programs: ["Zomato"]
bugs: ["Solr injection"]
bounty: "700"
publication_date: "2019-07-27"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5119
scraped_via: "browseros"
---

# Solr Injection by abusing Local Parameters on Zomato.com

Solr Injection by abusing Local Parameters on Zomato.com
Ronak Patel
Follow
3 min read
·
Jul 27, 2019

115

3

Hi All,

This article is about bug which i discovered on Zomato.com last month. Honestly, I couldn’t provide exploitation details to the Zomato security team while submitting bug but i had a strong gut feelings about injection at the vulnerable endpoint. Although, I haven’t done technically much from my side but still i think Solr Injection is not much known in our community. Hence, I decided to share my thought processing while i was finding this bug and illustrating it step by step.

I always prefer to test application by first going through functionalities directly visible on webpages and observing each request generated using Burp.

While opening main page www.zomato.com, it contains link for the Order food as visible in below screenshot.

Press enter or click to view image in full size

Upon clicking link for the Order food, it will navigate to the link as illustrated in below screenshot. This page contains the search functionality to allow users to search for restaurants and cuisines in your location.

Press enter or click to view image in full size

While searching for the restaurant, it generated request to the endpoint

“https://www.zomato.com/php/delivery_live_suggest.php?q=restaurant &delivery_subzone_id=number&

I observed this request and initially thought to check for the sql injection vulnerability manually on the parameter delivery_subzone_id parameter.

Get Ronak Patel’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

I started including single quotes, double quotes and random strings on parameter delivery_subzone_id. What i observed is that server is responding to the our injection of Double quotes on parameter.

As shown in below screenshot, server threw 500 internal server error with the odd number of double quotes and normal 200 Okay response with the even number of double quotes. This is the strong indication that our double quotes are being injected on query.

Press enter or click to view image in full size
Even number of double quotes injected
Press enter or click to view image in full size
Odd number of double quotes injected

Now, second step was to find out which technology or database or which kind of query it could be in backend where our input is being injected.I though it as a sql and tried various payloads and techniques to further find out backend technology and create exploit as explained by Gerben Javado on below awseome article for manual sql testing but i couldn’t get any sign of sql injection in response.

Manual SQL injection discovery tips
According to bugbountyforum.com's AMA format one of the most popular questions is How do you test for Server Side…

gerbenjavado.com

At this stage, i thought to move ahead and not report this behavior as i couldn’t find working exploit to create poc but then i went ahead and reported issue to the Zomato security team with the above findings.

Zomato security team investigated and resolved issue within two hours and awarded me with the bounty of 500$ and 200$ as a bonus for the uniqueness of the bug. They updated me that it was Solr Injection. Solr is a search platform built by apache.

Further, i did research and found below article on solr injection which is very well explained so i am not repeating same technical details here and instead embedding link below.

Abusing the Solr local parameters feature - LocalParams injection
Solr is an open source search platform built by the Apache project. You can read more about it at the Solr site, but…

javahacker.com

I hope this article was worth reading.
