---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2024-08-20_ssrfing-the-web-with-the-help-of-copilot-studio.md
original_filename: 2024-08-20_ssrfing-the-web-with-the-help-of-copilot-studio.md
title: SSRFing the Web with the help of Copilot Studio
category: documents
detected_topics:
- ssrf
- supply-chain
- oauth
- cloud-security
- sso
- access-control
tags:
- imported
- documents
- ssrf
- supply-chain
- oauth
- cloud-security
- sso
- access-control
language: en
raw_sha256: 95ae2225813063558f75375f4bbfe85e41fedecd5966c2543134a0c94e6a230e
text_sha256: bfaa2bcb985cd75de35190bfc985c835daaab1f7e9027cdb772fe9390b2f7dff
ingested_at: '2026-06-28T07:32:37Z'
sensitivity: unknown
redactions_applied: false
---

# SSRFing the Web with the help of Copilot Studio

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2024-08-20_ssrfing-the-web-with-the-help-of-copilot-studio.md
- Source Type: markdown
- Detected Topics: ssrf, supply-chain, oauth, cloud-security, sso, access-control
- Ingested At: 2026-06-28T07:32:37Z
- Redactions Applied: False
- Raw SHA256: `95ae2225813063558f75375f4bbfe85e41fedecd5966c2543134a0c94e6a230e`
- Text SHA256: `bfaa2bcb985cd75de35190bfc985c835daaab1f7e9027cdb772fe9390b2f7dff`


## Content

---
title: "SSRFing the Web with the help of Copilot Studio"
page_title: "Critical SSRF vulnerability in Microsoft Copilot Studio"
url: "https://www.tenable.com/blog/ssrfing-the-web-with-the-help-of-copilot-studio"
final_url: "https://www.tenable.com/blog/ssrfing-the-web-with-the-help-of-copilot-studio"
authors: ["Evan Grant (@stargravy)"]
programs: ["GitHub (Copilot)"]
bugs: ["SSRF"]
publication_date: "2024-08-20"
added_date: "2024-08-22"
source: "pentester.land/writeups.json"
original_index: 58
---

#  SSRFing the Web with the Help of Copilot Studio

By [Evan Grant](/profile/evan-grant)

[ ](https://www.linkedin.com/shareArticle?mini=true&url=https%3A%2F%2Fwww.tenable.com%2Fblog%2Fssrfing-the-web-with-the-help-of-copilot-studio&title=SSRFing%20the%20Web%20with%20the%20Help%20of%20Copilot%20Studio) [ ](https://www.reddit.com/submit?url=https%3A%2F%2Fwww.tenable.com%2Fblog%2Fssrfing-the-web-with-the-help-of-copilot-studio&title=SSRFing%20the%20Web%20with%20the%20Help%20of%20Copilot%20Studio) [ ](https://twitter.com/intent/tweet?urlhttps%3A%2F%2Fwww.tenable.com%2Fblog%2Fssrfing-the-web-with-the-help-of-copilot-studio&text=SSRFing%20the%20Web%20with%20the%20Help%20of%20Copilot%20Studio) Subscribe 

![Tenable Research has discovered a critical SSRF vulnerability in Microsoft Copilot Studio](/sites/default/files/images/articles/Tenable%20Research%20has%20discovered%20a%20critical%20SSRF%20vulnerability%20in%20Microsoft%20Copilot%20Studio.jpeg)

Tenable Research discovered a critical information-disclosure vulnerability in Microsoft’s Copilot Studio via a server-side request forgery (SSRF), which allowed researchers access to potentially sensitive information regarding service internals with potential cross-tenant impact.

## Introduction

In this blog, we take a look at a server-side request forgery (SSRF) vulnerability in Copilot Studio that leveraged Copilot’s ability to make external web requests. Combined with a useful SSRF protection bypass, we used this flaw to get access to Microsoft’s internal infrastructure for Copilot Studio, including the Instance Metadata Service (IMDS) and internal Cosmos DB instances. Before we jump into that, we’ll cover a bit of background.

![Tenable Research has discovered a critical SSRF vulnerability in Microsoft Copilot Studio](/sites/default/files/inline/images/Tenable%20finds%20critical%20SSRF%20vulnerability%20in%20Microsoft%20Copilot%20Studio.gif)

## Background

Recently we were looking into a couple of SSRF vulnerabilities in the APIs for Azure AI Studio and Azure ML Studio, which happened to be patched before we could report them. Thus, we looked into another area of the studios and determined that there was a bypass for SSRF protections in a separate, but similar API, which [we then reported](https://www.tenable.com/security/research/tra-2024-22) to Microsoft’s Security Response Center (MSRC). 

An SSRF vulnerability occurs when an attacker is able to influence the application into making server-side HTTP requests to unexpected targets or in an unexpected way. 

For instance, a common feature in many modern applications which deal with data analysis or machine learning is to integrate data from external services. In order to do so, the application needs to make HTTP requests to connect to those external service APIs. If an attacker is able to control the target of those requests, they could point the request to a sensitive internal resource for which the server-side application has access, even if the attacker doesn’t, revealing potentially sensitive information.

In the context of cloud applications, a common target is the IMDS, which, depending on the cloud platform, can yield useful, potentially sensitive information for an attacker ([Azure](https://learn.microsoft.com/en-us/azure/virtual-machines/instance-metadata-service), [AWS](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/configuring-instance-metadata-service.html), and [Google](https://cloud.google.com/compute/docs/metadata/overview) all have their own versions of this), localhost, or other internal infrastructure. For this reason, many features which could potentially lead to SSRF vulnerabilities will block the feature from targeting IMDS and non-routable IPs, but where there are restrictions, [there are bypasses](https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/Server%20Side%20Request%20Forgery/README.md). 

In the case of Azure AI Studio and Azure ML Studio, while the feature we attacked would block requests targeting localhost/127.0.0.1, we could point the request to an attacker-controlled server, which would then use an HTTP 301 (or 302) redirect to redirect the server’s request back to localhost/127.0.0.1. In this way, we were able to bypass their restriction, and obtain sensitive information, such as other hosts and endpoints on the network, from 127.0.0.1:4191 (a Linkerd related metrics endpoint).

With that background out of the way, let’s take a look at Microsoft’s Copilot Studio. 

## Copilot Studio HttpRequestActions

Microsoft’s Copilot Studio is built on top of its Power Platform, and as a result is a pretty cool product which lets you build custom Copilots – conversational applications which let you perform a wide variety of large language model (LLM) and generative AI tasks leveraging data ingested from your Microsoft 365 environment or any other data your Power Platform environment has access to.

When creating a new Copilot, you are able to define [Topics](https://learn.microsoft.com/en-us/microsoft-copilot-studio/guidance/topics-overview), which let you specify key phrases which a user could say to your Copilot that could lead to the AI responding in specific ways, or taking certain actions. When first exploring this feature we noticed that one of the actions that can be performed, when triggered by a key phrase, is an HTTP request.

![Tenable Research has discovered a critical SSRF vulnerability in Microsoft Copilot Studio](/sites/default/files/inline/images/Copilot%20Studio%20HttpRequestActions.png)

This was immediately exciting. Any time a cloud service presents the option to perform HTTP requests on your behalf there is some testing to be done. Better yet, this HttpRequestAction (so named in the topic code editor view) allows control over HTTP request headers, which will come in handy for testing against the IMDS, since it requires special request headers.

For an initial test, and to get an idea of how the request made by the Copilot looks, we can add a header to the HttpRequestAction and make a request to our Burp Collaborator instance. 

![Tenable has discovered a critical SSRF vulnerability in Microsoft Copilot Studio](/sites/default/files/inline/images/Tenable%20Research%20discovered%20a%20critical%20vulnerability%20in%20Copilot%20Studio.png)

Burp Collaborator soon shows a request made from an Azure IP address which includes our test header, and a few headers we did not add which are associated with Azure services.

## Hitting IMDS

Now that we know we can make requests, we can try requesting some interesting cloud resources like the IMDS we mentioned earlier. Unfortunately, pointing the request to the url **http://169.254.169.254/metadata/instance?api-version=2021-02-01** and sending the request yields a System Error response. 

![Tenable Research has discovered a critical SSRF vulnerability in Copilot Studio](/sites/default/files/inline/images/Tenable%20discovered%20critical%20vulnerability%20in%20Microsoft%20Copilot%20Studio.png)

The same was true when we tried a few common SSRF protection bypass techniques like:

  * Using a decimal value for the IP address (169.254.169.254 == 2852039166)
  * Requesting a domain which resolves to 169.254.169.254 instead of requesting the IP address directly.

The next bypass we tried, which we had [recently used](https://www.tenable.com/security/research/tra-2024-22) against targets in Azure AI Studio and Azure ML Studio, and [again in Azure Health Bot](https://www.tenable.com/blog/compromising-microsofts-ai-healthcare-chatbot-service), was pointing the HttpRequestAction at a server we control, and sending a 301 redirect response that points to the restricted hosts.

Instead of receiving a System Error response like when requesting directly, using a controller we control to redirect requests to 169.254.169.254 resulted in a 400 error, which is progress. To make requests to IMDS, we need to be able to set the metadata header to “true”, which we were able to do using the tools in Copilot Studio. However there was the issue of an X-Forwarded-For header being added automatically. According to Microsoft [documentation](https://learn.microsoft.com/en-us/azure/virtual-machines/instance-metadata-service?tabs=linux):

_In order to ensure that requests are directly intended for IMDS and prevent unintended or unwanted redirection of requests, requests:_

  * _Must contain the header Metadata: true_
  *  _Must not contain an X-Forwarded-For header_

We needed to get rid of the X-Forwarded-For header if we wanted to be able to access the metadata service. Oddly enough, the Topic code editor allowed us to create multiline header values, which would allow us to insert newlines into any given header. 

![Tenable Research discovered a critical SSRF vulnerability in Microsoft Copilot Studio](/sites/default/files/inline/images/Tenable%20discovered%20a%20critical%20vulnerability%20in%20Copilot%20Studio.png)

If we added a metadata header, as well as some extra newlines at the end of the “true” value, we could push the X-Forwarded-For header to be part of the HTTP request body which would be ignored by the IMDS.

![Tenable Research has discovered a critical vulnerability in Microsoft Copilot Studio](/sites/default/files/inline/images/Tenable%20discovered%20a%20critical%20SSRF%20vulnerability%20in%20Copilot%20Studio.png)

  
Combining this with the 301 redirect to 169.254.169.254, we were able to retrieve the instance metadata in a Copilot chat message:

![Tenable Research has discovered an SSRF vulnerability in Microsoft Copilot Studio](/sites/default/files/inline/images/Tenable%20discovered%20a%20critical%20vulnerability%20in%20Microsoft%20Copilot%20Studio.png)

While this information isn’t too sensitive on its own, we were also able to retrieve [managed identity access tokens](https://learn.microsoft.com/en-us/entra/identity/managed-identities-azure-resources/how-to-use-vm-token) from the IMDS. We could then leverage this authentication token to access other internal resources. 

For example, redirecting Copilot to request **http://169.254.169.254/metadata/identity/oauth2/token?api-version=2018-02-01 &resource=https://management.azure.com/** would grant us an access token which lets us check whether this instance’s managed identity has access to any other Azure resources.

## Discovering a Cosmos DB instance

It wasn’t immediately clear whether the access we’d already found was particularly impactful, whether it was limited to our environment, or if it impacted shared infrastructure and other tenants. With an access token for <https://management.azure.com/> we can check to see if we have gained access to other Azure resources.

A good first check is to see which Azure subscriptions are associated with the identity by making a request to**https://management.azure.com/subscriptions.** This revealed that the identity was associated with two subscriptions. Next we requested **https://management.azure.com/subscriptions/ <subscription-id>/resources** to check for Azure resources we could potentially access.

On one of the two subscriptions we see a response like the following:

![Tenable Research has discovered a critical SSRF vulnerability in Microsoft Copilot Studio](/sites/default/files/inline/images/Tenable%20has%20discovered%20a%20critical%20vulnerability%20in%20Copilot%20Studio.png)

This tells us that there is a Cosmos DB resource available to us. Requesting details on the resource shows us the URLs for the Cosmos DB endpoints, and showed that we could access the Cosmos DB master keys which would grant us read/write permissions. 

Fortunately, this Cosmos DB instance is only accessible to IP addresses which belong to Microsoft infrastructure. Unfortunately, that range happened to include our Copilot.

## Using Copilot to access the internal Cosmos DB

A quick review of some puzzle pieces we had and needed to put together:

  * A URL for an internal Cosmos DB instance, accessible only to internal Azure infrastructure
  * The master keys for that Cosmos DB instance
  * The ability to make HTTP requests from Copilot, with control over request headers.

  
To access Cosmos DB we needed to provide Copilot with the document endpoint URL, which we obtained from management.azure.com, and appropriate authorization and x-ms-data headers, [according to Microsoft’s documentation](https://learn.microsoft.com/en-us/rest/api/cosmos-db/access-control-on-cosmosdb-resources?redirectedfrom=MSDN). 

Using the sample node.js code in the documentation above, along with the Cosmos DB keys, it was possible to generate a valid authorization token, along with the associated x-ms-date header. After providing all of the pieces to Copilot and sending the request we saw a valid response, indicating that we could leverage the SSRF vulnerability in Copilot to gain read/write access on this internal Cosmos DB instance.

![Tenable Research has discovered a critical SSRF vulnerability in Microsoft Copilot Studio](/sites/default/files/inline/images/Tenable%20has%20discovered%20a%20critical%20SSRFvulnerability%20in%20Copilot%20Studio.png)

## Wrapping up

We tested this from multiple tenants and confirmed that, while no cross-tenant information appeared immediately accessible, the infrastructure used for this Copilot Studio service was shared among tenants. Any impact on that infrastructure could affect multiple customers. While we don’t know the extent of the impact that having read/write access to this infrastructure could have, it’s clear that because it’s shared among tenants, the risk is magnified.  
  
We also determined we could access other internal hosts, unrestricted, on the local subnet to which our instance belonged (10.0.x.0/24).

Once reported, Microsoft responded quickly and began addressing the issue. Microsoft assigned this issue [CVE-2024-38206](https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2024-38206) and communicated their evaluation to Tenable as a Critical Information Disclosure issue.

## Author

## Learn more

### [Evan Grant](/profile/evan-grant)

##### Evan Grant

Array 

[Read more](/profile/evan-grant)

## Learn more

## Related articles

Research

![Download pumping: New npm deception technique for supply chain attacks image](/sites/default/files/images/articles/Download%20pumping%20is%20a%20new%20npm%20deception%20technique%20for%20supply%20chain%20attacks.png)

May 28 2026

#### Download pumping: New npm deception technique for supply chain attacks

By [Ron Popov](/profile/ron-popov)

[ ](/blog/how-cyberattackers-inflate-malicious-package-npm-download-counts)

Cyber Exposure Alerts

![Mini Shai-Hulud: Frequently asked questions about the TeamPCP npm and PyPI… image](/sites/default/files/images/articles/Mini%20Shai-Hulud.png)

May 21 2026

#### Mini Shai-Hulud: Frequently asked questions about the TeamPCP npm and PyPI…

By [Research Special Operations](/profile/research-special-operations)

[ ](/blog/mini-shai-hulud-frequently-asked-questions)

AI Security

![Bring out your dead: How agentic AI for cybersecurity helps you rid your cloud… image](/sites/default/files/images/articles/How%20agentic%20AI%20for%20cybersecurity%20helps%20you%20rid%20your%20cloud%20of%20forgotten%2C%20risky%20assets.png)

May 14 2026

#### Bring out your dead: How agentic AI for cybersecurity helps you rid your cloud…

By [Brinton Taylor](/profile/brinton-taylor)

[ ](/blog/agentic-ai-cloud-security-zombie-assets)

  * Cloud
