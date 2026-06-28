---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-07-26_easy-bounty-with-exposed-buckets-blobs.md
original_filename: 2021-07-26_easy-bounty-with-exposed-buckets-blobs.md
title: Easy Bounty With Exposed Buckets & Blobs
category: documents
detected_topics:
- cloud-security
- api-security
- command-injection
- otp
- rate-limit
tags:
- imported
- documents
- cloud-security
- api-security
- command-injection
- otp
- rate-limit
language: en
raw_sha256: 4447a18934b0ac2e98ecbd375ec7aeac6d32c8e5df0c9a039af41ed38587f89f
text_sha256: ae9370beb37fdc5c592c8adb9932531324a8eaf329a61dc31d1d03f016bba1b3
ingested_at: '2026-06-28T07:32:07Z'
sensitivity: unknown
redactions_applied: false
---

# Easy Bounty With Exposed Buckets & Blobs

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-07-26_easy-bounty-with-exposed-buckets-blobs.md
- Source Type: markdown
- Detected Topics: cloud-security, api-security, command-injection, otp, rate-limit
- Ingested At: 2026-06-28T07:32:07Z
- Redactions Applied: False
- Raw SHA256: `4447a18934b0ac2e98ecbd375ec7aeac6d32c8e5df0c9a039af41ed38587f89f`
- Text SHA256: `ae9370beb37fdc5c592c8adb9932531324a8eaf329a61dc31d1d03f016bba1b3`


## Content

---
title: "Easy Bounty With Exposed Buckets & Blobs"
url: "https://mrd0x.com/easy-bounty-with-exposed-buckets-and-blobs/"
final_url: "https://mrd0x.com/easy-bounty-with-exposed-buckets-and-blobs/"
authors: ["mr.d0x (@mrd0x)"]
bugs: ["Cloud storage misconfiguration"]
bounty: "1,450"
publication_date: "2021-07-26"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3480
---

A simple guide on finding exposed AWS S3 buckets and Azure Blobs.

# Introduction

Finding exposed buckets is my favorite way of getting a payout because it doesn’t really require technical sophistication (relatively speaking) and it’s almost guaranteed to be a high severity submission. Exposed buckets are something that even established companies still face a problem with. So let’s take advantage of that and get some high severity submissions.

# Grayhat Warfare

[Grayhat Warfare](https://buckets.grayhatwarfare.com/) is my go-to site when I want to find exposed buckets & blobs. The UI is simple enough that anyone can use it. The hard part comes down to being patient and persistent in your search. You also need to be creative in your search query so ‘password’ and .csv files usually won’t yield great results.

[ ![Grayhat-Warfare](/static/2c6b16307228311b78c4057b9d58ae5f/8c557/grayhat_warfare.png) ](/static/2c6b16307228311b78c4057b9d58ae5f/a9965/grayhat_warfare.png)

# Dorks

Another well-known and documented way is using search engine dorks (Google/Bing/DuckDuckGo etc). I’m not going to dive deep into it since there’s various dorks you can find online but again be creative and patient.
  
  
  Sample dorks:
  site:s3.amazonaws.com AND intext:"password"
  inurl:s3.amazonaws.com AND accounts

# Github

Sensitive data posted onto Github repos has been a hot topic for a while now. Many scanning tools were created for developers to prevent them from pushing API tokens, keys, passwords and other sensitive data. But that won’t stop developers from posting links to buckets and blobs.

Use Github to search for S3 buckets and/or Blobs. When using this method I suggest you don’t narrow your scope and focus purely on finding exposed buckets. If there’s leaked tokens and keys while you’re searching that’s even better!
  
  
  Sample Github queries:
  s3.amazonaws.com AND "private"
  s3.amazonaws.com AND "password"
  blob.core.windows.net AND "sql"
  blob.core.windows.net AND "key"

# Azure Blobs

Azure Blobs are sometimes overlooked due to the slight added complexity in discovering exposed blobs. Here’s how the link structure looks like:
  
  
  http://<storage-name>.blob.core.windows.net/<container>/<file>

To find exposed blobs you need to brute force the **storage name** and **container(s)** then we use the [Azure Storage REST API](https://docs.microsoft.com/en-us/rest/api/storageservices/) to list the files out for us.

## Storage Names - Naming Convention

To find valid storage names you simply do a DNS lookup and check the response.

[ ![Invalid-Response](/static/496f1d60aa8b10e7de0ac01d9d7c7aa8/8c557/nxdomain.png) ](/static/496f1d60aa8b10e7de0ac01d9d7c7aa8/6a6e9/nxdomain.png)

[ ![Valid-Response](/static/462bbdc1558eada3d002d5274e9d6ee7/a65ce/valid_dns_response.png) ](/static/462bbdc1558eada3d002d5274e9d6ee7/a65ce/valid_dns_response.png)

There are some common keywords used for the storage account names that should be tested for:
  
  
  #Try appending & prepending
  <company-name>.blob.core.windows.net
  <company-name>cloud.blob.core.windows.net
  <company-name>images.blob.core.windows.net
  <company-name>backup.blob.core.windows.net
  <company-name>backups.blob.core.windows.net
  <company-name>storage.blob.core.windows.net
  <company-name>cdn.blob.core.windows.net
  <company-name>assets.blob.core.windows.net
  <company-name>files.blob.core.windows.net
  <company-name>resources.blob.core.windows.net
  <company-name>documents.blob.core.windows.net
  <company-name>development.blob.core.windows.net
  <company-name>production.blob.core.windows.net
  <company-name>qa.blob.core.windows.net
  <company-name>prod.blob.core.windows.net
  <company-name>dev.blob.core.windows.net
  <company-name>stage.blob.core.windows.net
  <company-name>staging.blob.core.windows.net
  <company-name>web.blob.core.windows.net
  <company-name>website.blob.core.windows.net
  <company-name>test.blob.core.windows.net
  ...

Check out [this file](https://github.com/NetSPI/MicroBurst/blob/master/Misc/permutations.txt) for additional keywords.

## Containers

Once you have a valid storage account you need to find the container name. Again, this requires brute force and it should be done like this:
  
  
  https://example.blob.core.windows.net/<container>?restype=container&comp=list

Once you hit a valid container it should return the URLs for the blobs.

[ ![Blob-Files](/static/427f9e09f5eecf3e15368d5c461c34af/8c557/files.png) ](/static/427f9e09f5eecf3e15368d5c461c34af/17a7a/files.png)

You should use a large list to brute force containers. Find common container names using Grayhat Warfare or Google Dorks and generate your own wordlist.

# Additional Resources

If you want additional details about Azure Blobs then I suggest you check out Cyberark’s excellent [article](https://www.cyberark.com/resources/threat-research-blog/hunting-azure-blobs-exposes-millions-of-sensitive-files) that goes more in-depth.

I also found [this article](https://www.netspi.com/blog/technical/cloud-penetration-testing/anonymously-enumerating-azure-file-resources/) by NetSPI to be useful.

# Results

In less a week I made several submissions and the companies that did provide bounties were mostly generous.

[ ![Payout-One](/static/51ef8d7640658828ef66fba79b04ce6a/8c557/payout1.png) ](/static/51ef8d7640658828ef66fba79b04ce6a/b2cef/payout1.png)

[ ![Payout-Two](/static/26aa7ff148ee59b90db28a7b757f81e4/8c557/payout2.png) ](/static/26aa7ff148ee59b90db28a7b757f81e4/914ae/payout2.png)

[ ![Payout-Three](/static/87bda7ebf6e7fa915084a348d0952885/8c557/payout3.png) ](/static/87bda7ebf6e7fa915084a348d0952885/5205c/payout3.png)

And of course let’s not forget the swag.

[ ![Swag](/static/c030e7224bb8386811f4e2b7b6eaab13/6af66/swag.png) ](/static/c030e7224bb8386811f4e2b7b6eaab13/6af66/swag.png)
