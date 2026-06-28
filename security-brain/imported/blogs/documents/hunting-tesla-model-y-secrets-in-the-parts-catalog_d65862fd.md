---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-02-22_hunting-tesla-model-y-secrets-in-the-parts-catalog.md
original_filename: 2020-02-22_hunting-tesla-model-y-secrets-in-the-parts-catalog.md
title: Hunting Tesla Model Y Secrets in the Parts Catalog
category: documents
detected_topics:
- api-security
- access-control
- command-injection
- otp
- automation-abuse
- cors
tags:
- imported
- documents
- api-security
- access-control
- command-injection
- otp
- automation-abuse
- cors
language: en
raw_sha256: d65862fdd8509a6ea80f2f0fa19db66787a1a32fe8592b28089d52806521e89a
text_sha256: 2f1d351889514577052753884f3e9a63fbdefcae1429f4d5c36f63aa1e699736
ingested_at: '2026-06-28T07:32:01Z'
sensitivity: unknown
redactions_applied: false
---

# Hunting Tesla Model Y Secrets in the Parts Catalog

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-02-22_hunting-tesla-model-y-secrets-in-the-parts-catalog.md
- Source Type: markdown
- Detected Topics: api-security, access-control, command-injection, otp, automation-abuse, cors
- Ingested At: 2026-06-28T07:32:01Z
- Redactions Applied: False
- Raw SHA256: `d65862fdd8509a6ea80f2f0fa19db66787a1a32fe8592b28089d52806521e89a`
- Text SHA256: `2f1d351889514577052753884f3e9a63fbdefcae1429f4d5c36f63aa1e699736`


## Content

---
title: "Hunting Tesla Model Y Secrets in the Parts Catalog"
url: "https://medium.com/@evan.connelly/hunting-tesla-model-y-secrets-in-the-parts-catalog-2f453f853dd8"
authors: ["Evan Connelly (@Evan_Connelly)"]
programs: ["Tesla"]
bugs: ["Broken authorization"]
publication_date: "2020-02-22"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4760
scraped_via: "browseros"
---

# Hunting Tesla Model Y Secrets in the Parts Catalog

Hunting Tesla Model Y Secrets in the Parts Catalog
Evan Connelly
Follow
5 min read
·
Feb 22, 2020

92

After buying a Model 3 in June of 2019, I began deep diving into understanding how my new car works. My interest largely being the infotainment system. Wanting to take that research to the next level and see if I could find ways to get past the security measures in place, I registered with Tesla as a hardware security researcher in August of 2019 and didn’t waste any time getting to work. I have found a few hardware security vulnerabilities that I’ve successfully gone through the bounty program with and hope to eventually write up and share.

While I’ve mostly focused on the hardware, I’d also occasionally try to find vulnerabilities on Tesla’s web properties. With the Model Y release approaching, my web research shifted to Model Y data exposure, wanting to see if I could find details on the new vehicle that were not yet public.

This led me back to the Tesla Parts Catalog, a site I had previously noticed something interesting in but that had not contained sensitive data in the past.

What did I find? By editing a cookie, a user was able to browse pages and data that would not normally be available. The parts catalog site allows “general public” logins from anyone with a Tesla account. While browsing the site, I noticed an interesting cookie. In testing, I found that editing the cookie would allow an unprivileged user to view things available to Tesla internally, but not the general public. In the past this was nothing of interest or sensitive. But, checking back after hearing that the Model Y would be released soon, I was able to view a multitude of information about the Model Y. As a huge Tesla enthusiast, it was exciting to get a sneak peak at parts and schematics on the Model Y that have not yet been made public.

Reproduction:

I signed into the EPC site with my Tesla account.

I noticed a cookie called EPCClaim.

Press enter or click to view image in full size

The value was base64 encoded and the plaintext is the below:

{“employeeId”:0,”firstName”:”General”,”lastName”:”Public”,”email”:”REDACTED@*****.com”,”countryCode”:”US”,”languageId”:null,”languageCode”:null,”currencyCode”:null,”isInternalUser”:false,”isBodyShopUser”:false,”isGeneralPublic”:true,”tabs”:false,”locationId”:null,”bodyShopId”:0,”bodyShopName”:null,”bodyShopCategory”:null,”permissions”:[]}

Hmm..permissions, what does that do? I checked the JS source and found some clues in https://epc.tesla.com/scripts/scripts.8c9383be.js.

{accountManagement:”ACCOUNT_MANAGEMENT”,bodyShopManagement:”BODY_SHOP_MANAGEMENT”,bodyShopAccountManagement:”BODY_SHOP_ACCOUNT_MANAGEMENT”,repairOrder:”REPAIR_ORDER”,orderPane:”ORDER_PANE”,admins:”ADMINS”,epcUser:”EPC_USER”,addToolingData:”ADD_TOOLING_DATA”,model3Catalog:”MODEL3_CATALOG”,modelYCatalog:”READONLY_CATALOG”,toolingCatalog:”TOOLING_CATALOG”,serviceToolingCatalog:”SERVICE_TOOLING_CATALOG”,returns:”RETURNS”,statements:”STATEMENTS”,creditmemos:”CREDIT_MEMO”,genealogy:”GENEALOGY”,generalAccountManagement:”GENERAL_ACCOUNT_MANAGEMENT”,orderModel3:”ORDER_MODEL3",orderModelX:”ORDER_MODELX”,orderRoadster:”ORDER_ROADSTER”,orderModelS:”ORDER_MODELS”,orderTooling:”ORDER_TOOLING”,orderServiceTooling:”ORDER_SERVICE_TOOLING”,orderModelSR:”ORDER_MODELSR”}

Specifically of interest when checking back though, modelYCatalog:”READONLY_CATALOG

Hmm..Model Y!

By editing the content of this cookie, it is possible to change what is displayed to the user.

Most permissions values would add options to the UI but their corresponding API endpoints were correctly restricted to authorized users with a bearer token and would not allow data to be accessed or written. What about the new Model Y option though?

{“employeeId”:0,”firstName”:”General”,”lastName”:”Public”,”email”:”REDACTED@*****.com”,”countryCode”:”US”,”languageId”:null,”languageCode”:null,”currencyCode”:null,”isInternalUser”:true,”isBodyShopUser”:false,”isGeneralPublic”:false,”tabs”:false,”locationId”:null,”bodyShopId”:0,”bodyShopName”:null,”bodyShopCategory”:null,”permissions”:”READONLY_CATALOG”}

I changed isGeneralPublic to false and isInternalUser to true. I added the Model Y permission value to the cookie based on values I found in the JS.

Encoded back into Base64 and set as the cookie value. I went back to https://epc.tesla.com/ with the edited EPCClaim cookie and to my surprise, I could now see Model Y as an option. Going through the catalog, it was showing Model Y parts.

I was able to see what seemed to be just about, if not every component used in the Model Y. A few things which I’m obviously not at liberty to share before the launch of the Model Y were a surprise to me and I’m excited to see this vehicle hit the market soon.

Timeline

30 Jan 2020 14:30:36 EST — Reported

Get Evan Connelly’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

30 Jan 2020 15:28:34 EST — Triaged

30 Jan 2020 16:34:27 EST — Model Y Content Taken Down

11 Feb 2020 18:44:27 EST — Bounty and Resolution

PART 2
It pays to take a second look

I went back to the EPC site, curious if I could find any other ways to get Model Y data. As I was looking through the EPC site, I noticed the search function. It is able to search all parts in the catalog for a given vehicle. In making searches I could see that it was filtering data based on the catalog being viewed. Searching while in the 3 catalog only finds parts for the Model 3, for example.

Wanting to see how that filtering was done, I inspected the network requests made while searching, looking to see if it would be possible to modify the API calls used and find data on the Model Y.

The API endpoint used for search suggestions is:

https://epcapi.tesla.com/api/searchSuggestions

The query parameters used are:

CatalogModel

countryCode

Term

For example, searching for “bumper” in the 3 catalog would call: https://epcapi.tesla.com/api/searchSuggestions?catalogModel=Model3&countryCode=US&term=bumper

The request is authenticated with a bearer token which is generated when logging into the EPC site and saved in local storage under the key EPCToken. I found that queries for Model Y data were not restricted and anyone with a valid bearer token (obtainable by logging into the site as the general public) was able to search for and find details of the parts in the Model Y by specifying CatalogModel=ModelY.

For example,

curl ‘https://epcapi.tesla.com/api/searchSuggestions?catalogModel=ModelY&countryCode=US&term=XYZ_Part_Name’ -H ‘Connection: keep-alive’ -H ‘Accept: application/json, text/plain, /’ -H ‘Authorization: Bearer REDACTED’ -H ‘Accept-Language: en-us’ -H ‘User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36' -H ‘Origin: https://epc.tesla.com’ -H ‘Sec-Fetch-Site: same-site’ -H ‘Sec-Fetch-Mode: cors’ -H ‘Referer: https://epc.tesla.com/’ -H ‘Accept-Encoding: gzip, deflate, br’ — compressed

The details returned in the response to these API Calls included the name of the matching items, the part numbers, titles, and notes on the items.

Additionally, systemGroupId gives the group of parts that the matching record is a part of. In testing, it was possible to request all parts within that group by calling the following endpoint: https://epcapi.tesla.com/api/catalogs/XXX/categories/0/subcategories/0/systemGroups/XXXXX?vin=

Through these unrestricted API endpoints, one could discover the details of many of the parts used in the Y. Based on public data on the Model 3 which is most similar in parts to the Y, it would be possible to find the right keywords to search for most parts and see if they are the same or different from the Model 3, as well as specific details on the parts in some cases, based on the titles and notes returned in the searches. By identifying one part from each group then searching by systemGroup, it is possible to identify even more parts and details on each part.

Timeline

19 Feb 2020 12:53:43 EST — Reported

19 Feb 2020 14:15:49 EST — Model Y Catalog Taken Offline

19 Feb 2020 17:06:47 EST — Bounty and Resolution

I was impressed with how quickly Tesla acted to fix both issues and also in the speed in which they issued awards.
