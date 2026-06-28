---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-04-06_3k-bounty-for-elastic-search-takeover.md
original_filename: 2020-04-06_3k-bounty-for-elastic-search-takeover.md
title: $3K Bounty For Elastic-Search Takeover
category: documents
detected_topics:
- command-injection
- otp
- automation-abuse
- information-disclosure
- api-security
- supply-chain
tags:
- imported
- documents
- command-injection
- otp
- automation-abuse
- information-disclosure
- api-security
- supply-chain
language: en
raw_sha256: dda3e734e331af0e10a15de8a1c82825d2ad66f8e1aada00a84075d144a945d2
text_sha256: 1bfa1f91d83ac2446076cdfd01fe750293ed8bf328635514d986a09bb4c77fba
ingested_at: '2026-06-28T07:32:01Z'
sensitivity: unknown
redactions_applied: false
---

# $3K Bounty For Elastic-Search Takeover

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-04-06_3k-bounty-for-elastic-search-takeover.md
- Source Type: markdown
- Detected Topics: command-injection, otp, automation-abuse, information-disclosure, api-security, supply-chain
- Ingested At: 2026-06-28T07:32:01Z
- Redactions Applied: False
- Raw SHA256: `dda3e734e331af0e10a15de8a1c82825d2ad66f8e1aada00a84075d144a945d2`
- Text SHA256: `1bfa1f91d83ac2446076cdfd01fe750293ed8bf328635514d986a09bb4c77fba`


## Content

---
title: "$3K Bounty For Elastic-Search Takeover"
url: "https://medium.com/@D0rkerDevil/3k-bounty-for-elastic-search-takeover-70c0847d2e40"
authors: ["Ashish Kunwar (@D0rkerDevil)"]
bugs: ["Elasticsearch Takeover", "Information disclosure"]
bounty: "3,000"
publication_date: "2020-04-06"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4663
scraped_via: "browseros"
---

# $3K Bounty For Elastic-Search Takeover

Ashish Kunwar
Follow
3 min read
·
Apr 6, 2020

278

1

$3K Bounty For Elastic-Search Takeover

Hello, Everyone.

It was the end of year 2019 in , Me and My friend were Hunting on A Target (called it REDACTED.COM) , this program is a cypto based company which has a bugbounty program.

After automating the recon for almost 3 days on our VPS using our personal automation tools which we have created, so after 3 days we went on to takea look at the logs and found a pretty interesting thing

There was a subdomain , lets say “test.redacted.com” , has a port running on 9200 which is a elastic search service .

ABOUT

The definition from google describes elastic search as: “ES is a document-oriented database designed to store, retrieve, and manage document-oriented or semi-structured data. When you use Elasticsearch, you store data in JSON document form. Then, you query them for retrieval.”

Unlike Mysql which stores its information in tables elastic search uses something called types. Each type can have several rows which are called documents. Documents are basically a json blob that hold your data as shown in the example below:

{“id”:1, “name”:”test”, “password”:”test@password”}

So now i have found the elastic search , it was time to visit the url

http://test.redacted.com:9200/

and i found this

{  "name" : "4yXXXXX",  "cluster_name" : "docker-cluster",  "cluster_uuid" : "ulM_pLwNQbWXXXXXXXX",  "version" : {  "number" : "6.x.x",  "build_flavor" : "default",  "build_type" : "tar",  "build_hash" : "3bd3e59",  "build_date" : "2019-03-06T15:16:26.86xxxxxx",  "build_snapshot" : false,  "lucene_version" : "7.6.x",  "minimum_wire_compatibility_version" : "5.6.0",  "minimum_index_compatibility_version" : "5.0.0"  },  "tagline" : "You Know, for Search"}

#Note: i had to add the ‘X’ in some places for obvious reasons.

Once you know an endpoint has an exposed Elastic Search db try to find all the indexes(Databases) that are available. This can be done by hitting the “/_cat/indices?v” endpoint with a GET request.

http://tst.redacted.com:9200/_cat/indices?v

Get Ashish Kunwar’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

i m able to add my own indices along with their production indices.

To perform a full text search on the database you can use the following command “/_all/_search?q=email”. This will query every index for the word “email”. There are a few words that I like to search for which include:

username, user, email,password,token,secrete,key

If you want to query a specific index you can replace the “_all” with the name of the index you want to search against.

/_all/_search?q=email

http://test.redacted.com:9200/_all/_search?q=email

Now at the end you can simply dump the data using curl or use

elasticdump
Tools for moving and saving indices. Version 1.0.0 of Elasticdump changes the format of the files created by the dump…

www.npmjs.com

to do so.

Install —

sudo npm install elasticdump -g #install globally

command to dump the elastic db using elasticdump —

elasticdump — input=http://ip:9200/filename — output=filename.json — type=data

https://medium.com/bugbountywriteup/haystack-hackthebox-writeup-7dfd8a6fed5

With that said , we got the 3K$ btc on the 1st jan 2020 early morning.

If You have queries, just DM me or @Subhajit Saha
