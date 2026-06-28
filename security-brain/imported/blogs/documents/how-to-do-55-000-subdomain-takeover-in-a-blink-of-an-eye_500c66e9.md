---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2018-09-10_how-to-do-55000-subdomain-takeover-in-a-blink-of-an-eye.md
original_filename: 2018-09-10_how-to-do-55000-subdomain-takeover-in-a-blink-of-an-eye.md
title: How to do 55.000+ Subdomain Takeover in a Blink of an Eye
category: documents
detected_topics:
- api-security
- sso
- command-injection
- automation-abuse
tags:
- imported
- documents
- api-security
- sso
- command-injection
- automation-abuse
language: en
raw_sha256: 500c66e9ad0c8f6787431c564b1180cbe5f6a9783bec7f0289809af2ea0f8c9e
text_sha256: 0c9b113a83b69ae328c51ae6c86759de0fef35a74724f0482734b884601a440c
ingested_at: '2026-06-28T07:31:57Z'
sensitivity: unknown
redactions_applied: false
---

# How to do 55.000+ Subdomain Takeover in a Blink of an Eye

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2018-09-10_how-to-do-55000-subdomain-takeover-in-a-blink-of-an-eye.md
- Source Type: markdown
- Detected Topics: api-security, sso, command-injection, automation-abuse
- Ingested At: 2026-06-28T07:31:57Z
- Redactions Applied: False
- Raw SHA256: `500c66e9ad0c8f6787431c564b1180cbe5f6a9783bec7f0289809af2ea0f8c9e`
- Text SHA256: `0c9b113a83b69ae328c51ae6c86759de0fef35a74724f0482734b884601a440c`


## Content

---
title: "How to do 55.000+ Subdomain Takeover in a Blink of an Eye"
url: "https://medium.com/@thebuckhacker/how-to-do-55-000-subdomain-takeover-in-a-blink-of-an-eye-a94954c3fc75"
authors: ["BuckHacker (@thebuckhacker)"]
programs: ["Shopify"]
bugs: ["Subdomain takeover"]
publication_date: "2018-09-10"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5707
scraped_via: "browseros"
---

# How to do 55.000+ Subdomain Takeover in a Blink of an Eye

How to do 55.000+ Subdomain Takeover in a Blink of an Eye
buckhacker
Follow
6 min read
·
Sep 11, 2018

327

3

TL;DR In this article we will describe a process that allowed us to identify more then 55.000 subdomains vulnerable to Subdomain Takeover on Shopify platform.

Background

First of all we would like to mention that this is not a specific issue that can be found just on Shopify, this is common to several others cloud service providers. In the past weeks / days we contacted several different cloud providers regarding this problem and we were impressed with the Shopify Security Guys: fast response, super aware of the problem and great communications. Really kudos to them, they really know how to deal with the cybersecurity research community.

First of all what is Shopify? Let’s take a look at the Wikipedia description.

Press enter or click to view image in full size
Shopify of Wikipedia

Basically, it is a cloud service provider that allows you to create an e-commerce website in a super easy way.

Now if you are already familiar with the Subdomain Takeover vulnerability on Shopify you can directly jump to the end of this article where we show how to do it on a large scale.

Subdomain Takeovers on Shopify

During a BugBounty Program or a Pen Testing activity, if you encounter one of the two following web pages, you can have a Subdomain Takeover.

Press enter or click to view image in full size
If you see this page you have a potential SubDomain Takeover
Press enter or click to view image in full size
Another example of vulnerable page

Let’s see what are the steps to be sure about it.

First of all you can do a Subdomain Takeover on Shopify with two types of DNS records:

Mapping with application name (CNAMES pointing to myshopname.myshopify.com)
Mapping with DNS (CNAMES pointing to shops.myshopify.com)

There could be also other methods too (maybe legacy), which we’ll investigate in the near future.

Case #1 Mapping with application name

In this example we setup a CNAME for shop.buckhacker.com pointing to buckhacker.shopify.com

nslookup on shop.buckhacker.com

Now if the shop name buckhacker is not claimed on Shopify we could claim it and perform the Subdomain Takeover.

How we can check if a shop name is claimed or not ?

During the account registration phase you are forced to choose your shop name. If you go on this page you can easy figure out if the shop name is available:

Example of not available shop name
Example of available shop name

If you take a look with Burp what is happening behind you can see a request to a rest API that can gives to you two types of responses:

#1 Unavailable ({“status”:”unavailable”,”message”:null,”host”:”buckhacker.myshopify.com”})

#2 Available ({“status”:”available”,”message”:null,”host”:”buckhacker2.myshopify.com”})

You can develop a script that checks if a domain is available or not. To save you time we release a simple script on our GitHub page.

At this point if we found that the shop name is available we need simply to connect it in the Shopify portal. Let’s take a look how to do it.

Once you login in the shopify website go to the left menu on “Online Store” and then “Domains”:

Domains Settings on the left menu

Now click on “Connect existing domain”:

In the next form write down the vulnerable domain:

Press enter or click to view image in full size

Click on “Next” and then “Verify Connection”

Press enter or click to view image in full size

Now if you performed all steps correctly you will be redirected to the following page:

Press enter or click to view image in full size

If you reached this point you have successfully performed a subdomain takeover.

Get buckhacker’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

This case is more rare to find because you choose the shop name in the account creation procedure. So in order to have it available the user needs to delete the whole account or change it. During our investigation we identified that 2% of the websites were affected by this misconfiguration.

Case #2 Mapping with DNS

In the second case the subdomain is a CNAME pointing to shops.myshopify.com.

Let’s look at this example that we created for this case:

This is the most common case of subdomain takeover on Shopify. Basically in this case we can create a shop with any available name and just connect it from the Shopify portal as described in the previous case.

Here some screenshots that illustrate the process:

Connecting sales.buckhacker.com to my shop

Here the confirmation:

Successful connection of the vulnerable subdomain

Another confirmation:

Another confirmation
Large scale exploitation

We already told in previous articles how the project Sonar and the FDNS dataset is fantastic to identify vulnerabilities.

Press enter or click to view image in full size
FDNS Dataset

The FDNS dataset provides, among other things, CNAMES records. Basically we can look inside this dataset all the subdomains with a CNAME pointing to shop.myshopify.com or myshopname.shopify.com and then perform the subdomain takeover check.

Press enter or click to view image in full size
subdomains of buckhacker.com in the FDNS Dataset

All this could be done with our simple script and one line of bash:

zcat $FDNS_DATASET | strings | grep shopify.com | cut -d “\”” -f 8 | grep -v “shopify.com” | while read subdomain; do python3 ShopifySubdomainTakeoverCheck.py $subdomain; done

First of all we need to explain why we have developed a new script to check for Subdomain Takeovers on Shopify when there are many already available. Most of the other scripts currently available, are detecting a Subdomain Takeover just based on the Shopify error message page, but, this could result in a lot of cases a false positive. We identified many pages with the “vulnerable” error message page, but just a small percentage of them was vulnerable to a Subdomain Takeover. Our simple script is performing three checks: page error message, CNAME and then, if needed, performs the REST API request (as described at the beginning of the blog post). We’ll hope in the next future Subdomain Takeover tools will implement similar techniques to reduce the number of false positives.

If you use the script on all the FDNSv2 datasets (from the beginning of 2017 and with some additional tuning) the results are impressive: more then 55.000 subdomains are vulnerable to Subdomain Takeover.

Now you can use this data and check if your BugBounty / Costumers domain names are present in this list.

It is crystal clear that you can use this technique also on other cloud service providers.

Conclusions

We think this research could give a glimpse as to how large and underestimated the Subdomain Takeover phenomena is. We think, with cloud computing, we are in a new era of vulnerability research, instead of looking in process heap and stack we need to think in a large scale, for example by looking at DNS records mapping. Maybe we need to think about cloud platforms, and even the Internet itself, as a one big operating system.

Hope you enjoyed this article; feedback is welcome !

Timeline
21 August 2018 — Report to Shopify via HackerOne Program
21 August 2018 — First initial feedback from Shopify
23 August 2018 — Second feedback from Shopify
10 September 2018 — Publication
