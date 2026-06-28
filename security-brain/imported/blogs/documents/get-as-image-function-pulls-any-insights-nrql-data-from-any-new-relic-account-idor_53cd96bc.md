---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2018-10-09_get-as-image-function-pulls-any-insightsnrql-data-from-any-new-relic-account-ido.md
original_filename: 2018-10-09_get-as-image-function-pulls-any-insightsnrql-data-from-any-new-relic-account-ido.md
title: Get as image function pulls any Insights/NRQL data from any New Relic account
  (IDOR)
category: documents
detected_topics:
- cloud-security
- idor
- command-injection
- automation-abuse
- api-security
tags:
- imported
- documents
- cloud-security
- idor
- command-injection
- automation-abuse
- api-security
language: en
raw_sha256: 53cd96bcfbe642ec2142a50b04b1e6a572e593aaf5bbb9712541943f9b1cb20d
text_sha256: c31caa519a0be0c716485e5629d2bbe562f5a2b61d98ff698bb5784a59076697
ingested_at: '2026-06-28T07:31:57Z'
sensitivity: unknown
redactions_applied: false
---

# Get as image function pulls any Insights/NRQL data from any New Relic account (IDOR)

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2018-10-09_get-as-image-function-pulls-any-insightsnrql-data-from-any-new-relic-account-ido.md
- Source Type: markdown
- Detected Topics: cloud-security, idor, command-injection, automation-abuse, api-security
- Ingested At: 2026-06-28T07:31:57Z
- Redactions Applied: False
- Raw SHA256: `53cd96bcfbe642ec2142a50b04b1e6a572e593aaf5bbb9712541943f9b1cb20d`
- Text SHA256: `c31caa519a0be0c716485e5629d2bbe562f5a2b61d98ff698bb5784a59076697`


## Content

---
title: "Get as image function pulls any Insights/NRQL data from any New Relic account (IDOR)"
page_title: "Get as image function pulls any Insights/NRQL data from any New Relic account (IDOR) - Jon's Personal Blog"
url: "https://jonbottarini.com/2018/10/09/get-as-image-function-pulls-any-insights-nrql-data-from-any-new-relic-account-idor/"
final_url: "https://jonbottarini.com/2018/10/09/get-as-image-function-pulls-any-insights-nrql-data-from-any-new-relic-account-idor/"
authors: ["Jon Bottarini (@jon_bottarini)"]
programs: ["New Relic"]
bugs: ["IDOR"]
bounty: "2,500"
publication_date: "2018-10-09"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5653
---

This writeup walks you through the full process as to how I found a pretty bad Insecure Direct Object Reference (IDOR) in [New Relic. ](https://www.hackerone.com/newrelic)

In New Relic, there is the ability to add a 3rd party integration to a product line called [New Relic Infrastructure](https://newrelic.com/products/infrastructure). Common integrations include AWS, Azure, and most recently Google Cloud Platform (GCP). In Google Cloud Platform there is also the ability to create dashboards:

![new relic dashboards](https://www.jonbottarini.com/wp-content/uploads/2018/09/pic1-1024x536.png)

Dashboards are pretty common in New Relic, but there was something unique about the dashboards that are within the integrations section; the dropdown options for each chart allow you to do the following actions, which are _not_ present in any of the other dashboard areas:

![](https://www.jonbottarini.com/wp-content/uploads/2018/09/pic2-1024x350.png)

The option that immediately stood out to me was the “Get as image” option. This option converts the NRQL query that generates the dashboard into an image – and this is where the vulnerability lies. For more info on the New Relic Query Language (NRQL) works, check out this link:

<https://docs.newrelic.com/docs/insights/nrql-new-relic-query-language/nrql-resources/nrql-syntax-components-functions>

The normal POST request to generate the dashboard image is as follows:
  
  
  {"query":{"account_id":1523936,"nrql":"SELECT count(*) FROM IntegrationError FACET dataSourceName SINCE 1 DAY AGO"},"account_id":1523936,"endpoint":"/v2/nrql","title":"Authentication Errors"}

The application failed to check and see if the `account_id` parameter belonged to the user making the request. The account number `1523936` belongs to me, but if I changed it to another number, I could pull data from another account.

So now that I had control over this value, I could change the account ID to any other account ID on New Relic. Since the account ID parameter is incremental, if I was malicious I could simply throw this request into Burp Intruder and highlight the account id value to increment by one on each request, enabling me to pull any data I wanted from any or all accounts on New Relic. The NRQL query could be modified as well, so instead of pulling the data that generated the original dashboard, I could instead change the request to something like this:
  
  
  {"query":{"account_id":_any_account_number_here_ ,"nrql":"SELECT * FROM SystemSample"},"account_id":_any_account_number_here_ ,"endpoint":"/v2/nrql","title":"Uh oh!"}
  

This query runs the SystemSample NRQL query on any account ID, which downloads the following photo:

![](https://www.jonbottarini.com/wp-content/uploads/2018/10/80381da8-f89b-4e1a-b9c1-ef3a0b7f66c1-1.png)

So this is _interesting_ , but it doesn’t really tell me any juicy info. I know that I’m hitting other accounts, but the information I’m retrieving back is useless – it just shows an empty chart! I played around with this for a little while, trying different NRQL queries until I discovered an interesting header that is in the response back from the server when you send this type of request:
  
  
  X-Image-Url: http://gorgon.nr-assets.net/image/{UNIQUE_ID}

![](https://www.jonbottarini.com/wp-content/uploads/2018/10/Screen-Shot-2018-10-07-at-9.17.33-PM-1024x581.png)

I realized that if you add `?type=` at the end of the URL it will show you different chart types, allowing you to exfiltrate more data than normal. If you enter a incorrect “`?type=`” value, it will show you all of the available chart options within the error message:
  
  
  {"code":"BadRequestError","message":"uhoh is not a valid Vizco chart type. Permitted Types: apdex area bar baseline billboard bullet empty event-feed funnel heatmap histogram json line markdown pie stacked-horizontal-bar scatter table traffic-light vertical-bar"}

Now I can use any of the above chart types of return _more_ information than I normally would from the NRQL query:
  
  
  X-Image-Url: http://gorgon.nr-assets.net/image/{UNIQUE_ID}?type=json
  

![](https://www.jonbottarini.com/wp-content/uploads/2018/10/80381da8-f89b-4e1a-b9c1-ef3a0b7f66c1-2.png)

Now we’re getting somewhere! Instead of the normal chart type, I’m now returning a JSON dump of the dashboard, downloaded as a photo. This is pretty great considering I can perform this JSON dump against any account – but I want to go one step further. How can I exfiltrate as much data as possible in each request? Just add a `&height=2000` at the end of the URL 🙂
  
  
  X-Image-Url: http://gorgon.nr-assets.net/image/{UNIQUE_ID}?type=json&height=2000

![](https://www.jonbottarini.com/wp-content/uploads/2018/10/80381da8-f89b-4e1a-b9c1-ef3a0b7f66c1-328x1024.png)

I reported this to the New Relic team and they fixed it shortly afterwards within a few days. I was awarded $2,500 for this bug. I asked them if they wanted to include any comment on this post about how they fixed the issue, and they provided the following:

> For some background, this report helped us identify a logic error with the validation code we have in place in our backend authentication proxy. A very specific combination of configuration options for an application would result in the validation checks not taking place.
> 
> Once we identified that issue, we were able to search for anywhere we were using that combination of configuration options to quickly mitigate the issue. That then led to a permanent fix of the logic issue, ensuring that the account validation always took place before the request was allowed to proceed.

The New Relic security team is one of the best ones out there – they award quickly and their time to resolution is fantastic. It’s really one of the main reasons I enjoy hunting for bugs on them so much!

[Follow me on Twitter](https://www.twitter.com/jon_bottarini) to stay up to date with what I’m working on and security/bug bounties in general 🙂
