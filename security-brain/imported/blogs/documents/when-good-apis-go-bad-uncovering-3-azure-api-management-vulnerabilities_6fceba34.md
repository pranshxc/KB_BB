---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-05-04_when-good-apis-go-bad-uncovering-3-azure-api-management-vulnerabilities.md
original_filename: 2023-05-04_when-good-apis-go-bad-uncovering-3-azure-api-management-vulnerabilities.md
title: 'When Good APIs Go Bad: Uncovering 3 Azure API Management Vulnerabilities'
category: documents
detected_topics:
- cloud-security
- supply-chain
- ssrf
- path-traversal
- api-security
- command-injection
tags:
- imported
- documents
- cloud-security
- supply-chain
- ssrf
- path-traversal
- api-security
- command-injection
language: en
raw_sha256: 6fceba34a452f51e909c9cf2db6c5c3660e8f878b64f58d821829348886af964
text_sha256: c0410286d0f7a202de3fd52221c9422f3e99a1c297254693ba41c258c1a25879
ingested_at: '2026-06-28T07:32:20Z'
sensitivity: unknown
redactions_applied: false
---

# When Good APIs Go Bad: Uncovering 3 Azure API Management Vulnerabilities

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-05-04_when-good-apis-go-bad-uncovering-3-azure-api-management-vulnerabilities.md
- Source Type: markdown
- Detected Topics: cloud-security, supply-chain, ssrf, path-traversal, api-security, command-injection
- Ingested At: 2026-06-28T07:32:20Z
- Redactions Applied: False
- Raw SHA256: `6fceba34a452f51e909c9cf2db6c5c3660e8f878b64f58d821829348886af964`
- Text SHA256: `c0410286d0f7a202de3fd52221c9422f3e99a1c297254693ba41c258c1a25879`


## Content

---
title: "When Good APIs Go Bad: Uncovering 3 Azure API Management Vulnerabilities"
page_title: "Uncovering 3 Azure API Management Vulnerabilities – When Good APIs Go Bad - Blog | Tenable®"
url: "https://ermetic.com/blog/azure/when-good-apis-go-bad-uncovering-3-azure-api-management-vulnerabilities/"
final_url: "https://www.tenable.com/blog/uncovering-3-azure-api-management-vulnerabilities-when-good-apis-go-bad"
authors: ["Liv Matan (@terminatorLM)"]
programs: ["Microsoft (Azure)"]
bugs: ["SSRF", "Unrestricted file upload", "Path traversal", "Cloud"]
publication_date: "2023-05-04"
added_date: "2023-05-06"
source: "pentester.land/writeups.json"
original_index: 1188
---

#  Uncovering 3 Azure API Management Vulnerabilities – When Good APIs Go Bad

[![Liv Matan](/sites/default/files/pictures/2024-03/Liv-Matan.jpg) ]()

By [Liv Matan](/profile/liv-matan)

[ ](https://www.linkedin.com/shareArticle?mini=true&url=https%3A%2F%2Fwww.tenable.com%2Fblog%2Funcovering-3-azure-api-management-vulnerabilities-when-good-apis-go-bad&title=Uncovering%203%20Azure%20API%20Management%20Vulnerabilities%20%E2%80%93%20When%20Good%20APIs%20Go%20Bad) [ ](https://www.reddit.com/submit?url=https%3A%2F%2Fwww.tenable.com%2Fblog%2Funcovering-3-azure-api-management-vulnerabilities-when-good-apis-go-bad&title=Uncovering%203%20Azure%20API%20Management%20Vulnerabilities%20%E2%80%93%20When%20Good%20APIs%20Go%20Bad) [ ](https://twitter.com/intent/tweet?urlhttps%3A%2F%2Fwww.tenable.com%2Fblog%2Funcovering-3-azure-api-management-vulnerabilities-when-good-apis-go-bad&text=Uncovering%203%20Azure%20API%20Management%20Vulnerabilities%20%E2%80%93%20When%20Good%20APIs%20Go%20Bad) Subscribe 

![Tenable Cloud Security](/sites/default/files/images/articles/Blog-Cloud_Banners_8_7.png)

Learn how now-patched Azure API Management service vulnerabilities revealed by our research team enabled malicious actions.

The Tenable Cloud Security research team recently discovered three vulnerabilities in the Azure API Management service. These included two SSRF (server-side request forgery) vulnerabilities and a file upload path traversal on an internal Azure workload. The vulnerabilities were achieved through URL formatting bypasses and an unrestricted file upload functionality in the API Management developer portal.

By abusing the SSRF vulnerabilities, attackers could send requests from the service’s CORS Proxy and the hosting proxy itself, access internal Azure assets, deny service and bypass web application firewalls.

With the file upload path traversal, attackers could upload malicious files to Azure’s hosted internal workload – and to self-hosted developer portals.

**Responsible Disclosure**

The three vulnerabilities, which MSRC has now fully patched, exploit Azure’s API Management service. We want to thank MSRC for their cooperation. In a recent call, we worked together with MSRC to make sure the vulnerabilities have been fully remediated.

## Technical Analysis

### What is the Azure API Management service?

The Azure API Management service is a fully managed platform that enables organizations to create, manage, secure and analyze their APIs across all environments. It provides a central hub for publishing APIs to external and internal developers, partners and employees with ease. With Azure API Management, organizations can scale their API program with confidence, ensuring that their APIs are available, secure and performing well.

#### #1 - Full SSRF on Azure API Management CORS Proxy

**When you think the vulnerability you found is a duplicate – but it’s actually a bypass.**

The SSRF vulnerability involving the CORS Proxy was first reported to Microsoft by another cloud security company on November 12, 2022, and fixed a few days later, on November 16. You can find more details here: [Microsoft resolves four SSRF vulnerabilities in Azure cloud services](https://msrc.microsoft.com/blog/2023/01/microsoft-resolves-four-ssrf-vulnerabilities-in-azure-cloud-services/).

The research team reported its findings to Microsoft on December 21, 2022. A month later, on January 17, 2023, the cloud security company that initially reported the same vulnerability posted a blog announcing that the vulnerability had been reported and fixed.

At first, we assumed our report was a duplicate report. However, looking closely at the timeline, we realized that the vulnerability we discovered bypasses the fix Microsoft had deployed for the vulnerability reported by the other cloud security company.

**Technical details**

API management includes the ability to define schemas for the structure of data exchanged through the API. Organizations can use these schemas to ensure compatibility between API clients and servers, and to validate the structure of data. You can create and manage schemas using the Azure API Management portal or REST API.

Azure has implemented "Import from URL," a feature in Azure API Management that enables customers to retrieve a schema from a URL and use it in their API. Once you have specified the URL of the schema, the Azure API Management CORS Proxy retrieves the schema from the specified URL by sending it an HTTP request:

![](/sites/default/files/inline/images/image1_2.png)

The CORS Proxy allows for seamless cross-domain communication by intercepting, modifying and adding CORS headers.

This functionality rang a bell - welcome, server-side request forgery (SSRF)!

SSRF is a vulnerability that allows an attacker to send a crafted request from a vulnerable server to a targeted external or internal server or service.

The intent of the Azure functionality is to send requests to external servers to fetch schemas. The API management service sends such requests by the CORS Proxy (apimanagement-cors-proxy-prd.azure-api.net) as follows:

![](/sites/default/files/inline/images/image3_0.png)

Notice the two headers: Ocp-Apim-Method and Ocp-Apim-Url.

What if we try to access internal resources by manipulating the Ocp-Apim-Url value?

In this scenario, when we tried the first basic payload, http://localhost, the CORS Proxy yielded a 403 Forbidden response, indicating the presence of a defense mechanism. against SSRF:

![](/sites/default/files/inline/images/image6_1.png)

After a few test cases, we quickly realized the server has a blacklist containing:

_http://localhost_

 _http://127.0.0.1_

You can overcome this defense with a lot of different URL formatting bypasses (octal, decimal and hexadecimal ips, different CDIRs and more). We chose to bypass the blacklist by inputting a DNS that resolves to localhost - localtest.me.

The CORS Proxy resolves localtest.me → 127.0.0.1 and returns the desired response:

![](/sites/default/files/inline/images/image9.png)

We managed to get a full SSRF with a reflected response on the CORS Proxy of the Azure API Management service. This enabled us to send the SSRF with a chosen HTTP verb/method – in this case, the Ocp-Apim-Method HTTP header.

We also found that we could send custom headers by just adding them to the request (the CORS Proxy proxies the http headers to the target server).

**Accessing internal services**  
While trying to access other ports, we got another “403 Forbidden” response. 403 was returned from the server only when we tried to access the following ports: 300, 3000 and 30000. When inputting a non-existent port, such as “300000000”, we again received a “403 Forbidden” response. We were able to infer that a regex is checking if the “Ocp-Apim-Url” header value contains the string “300”.

We understood that if a regex exists specifically for those ports, some important services must be listening on those ports. The regex works on the input from the “Ocp-Apim-Url” value. Therefore, to bypass this check, we were able to input a valid external server in our control, then redirect the CORS Proxy to our desired SSRF internal location - for example, _http://localhost:30001_.

Finally, we were able to access Azure internal services via the redirect bypass in the following ports:

30001 - Authenticated view of the developer portal

30004 - Azure’s Management API

30005 - Azure’s Kudu API management

30006 - Unpublished developer site (Unauth)

Accessing port 30005  
After inputting our redirect server in the Ocp-Apim-Url input, we got a visit from the CORS Proxy that successfully followed our redirect to: _http://localhost:30005/test_  
Redirect server:

![](/sites/default/files/inline/images/image12_0.png)

Request and response:

![](/sites/default/files/inline/images/image2_2.png)

We accessed the internal Kudu service! [EmojiDeploy](https://www.tenable.com/blog/Emoji-Deploy-Smile-Your-Azure-web-service-just-got-Rced) anyone?  
![](/sites/default/files/inline/images/image14.png)

**Accessing port 30001 using the same technique**  
Request and response:

![](/sites/default/files/inline/images/image15.png)

At this point in the research we decided to stop investigating to avoid possible harm to internal services and infrastructure.

#### #2 - Full SSRF on the Azure API Management hosting proxy

When configuring API in the service, users can configure the frontend, backend, inbound and outbound processing:

![](/sites/default/files/inline/images/image4_3.png)

We will focus our discussion on the inbound processing part. The "set-backend-service" policy is used to dynamically configure the backend service URL for an API. The policy sets the backend URL to the value specified in the "base-url" parameter. This allows for greater flexibility and ease of management, as the backend URL can be changed in the policy rather than having to update the API configuration directly.

![](/sites/default/files/inline/images/image10_0.png)

So who exactly is configuring and setting our request modifications according to the policies that we set in the inbound and outbound processing? We assumed a proxy must be in place.

When researching the functionality, we noticed that the policies were set with the API Management proxy, _https://apimanagement.hosting.portal.azure.net_ /, in the inbound and outbound processing. When a request is sent from the frontend that the user specifies, the request will be sent to the inbound processing proxy and then to the specified backend.

SSRF can be exploited by abusing the set-backend-service policy and setting it to the desired SSRF location, e.g. _http://localhost_.

![](/sites/default/files/inline/images/image5_2.png)

Since we had control over the frontend and inbound processing policies, we could send the SSRF with an HTTP verb/method and custom headers of our choosing.

We were able to access an internal HTTP port 80 for a POC:

![](/sites/default/files/inline/images/image17.png)

At this point in the research we decided to stop investigating to avoid possible harm to internal services and infrastructure - based on discussion with Microsoft, local APIs that serve sensitive data or allow administration required authentication.

#### #3 - Unrestricted file upload path traversal in the API Management developer portal

We also investigated the Azure developer portal for the API Management service and discovered an unrestricted file upload to its server. The developer portal’s authenticated mode lets you upload static files and images to display on your dedicated portal. The developer portal’s [self-hosting](https://learn.microsoft.com/en-us/azure/api-management/developer-portal-self-host) feature intrigued us, as well, for its ability to essentially expand the impact of any vulnerability. In short, our finding affects not only Azure itself but also end-users who have deployed the developer portal themselves.

![](/sites/default/files/inline/images/image13.png)

On a portal “publish,” the files are uploaded to a dedicated Azure blob and the developer portal filesystem, which is inaccessible to Azure users and hosted by Azure. Users can access the files through the developer portal under the path specified and, by default, under
  
  
  /content/x.png.

We found that Azure does not validate the file type and path of the files uploaded. Authenticated users can traverse the path specified when uploading the files, upload malicious files to the developer portal server and possibly execute code on it using DLL hijacking, iisnode config swapping or any other relevant attack vector.

While researching the developer portal, to test the attack locally, we cloned our own self-hosted API management instance, <https://github.com/Azure/api-management-developer-portal>.

We were able to successfully traverse and drop unwanted files in our system.

For example, the usual and intended location of the files after uploading them would be:
  
  
  C:\Users\Liv\Desktop\api-management-developer-portal\dist\website\content

By default, the path specified in the Azure APIM when uploading files is:
  
  
  /content/x.png

We could simply traverse this path as follows and drop a maliciousFile.exe in the Desktop:
  
  
  C:\Users\Liv\Desktop\api-management-developer-portal\dist\website\../../../maliciousFile.exe

![](/sites/default/files/inline/images/image7_0.png)

The developer portal is published with the maliciousFile.exe:

![](/sites/default/files/inline/images/image8_0.png)

The malicious file is on the desktop of the server! The directory traversal worked:

![](/sites/default/files/inline/images/image16_0.png)

At this point in the research we decided to stop investigating to avoid possible harm to internal services and infrastructure.

Conclusion  
As a central hub for publishing APIs, the Azure API Management service is an attractive target for attackers seeking to use it as a conduit for malicious activities. While Microsoft works hard to secure the service, persistent researchers can sometimes breach its defenses and bring vulnerabilities to light. The first vulnerability we uncovered teaches us to never assume a fixed vulnerability won’t recur. The second vulnerability underscores the importance of exercising caution with regard to proxies. The third vulnerability highlights how sensitive API portals can be when it comes to malicious file uploads.  
We commend the Microsoft Security Response Center (MSRC) for their prompt remediation of the discovered vulnerabilities and exceptional collaboration throughout the reporting and mitigation process.

## Tenable Cloud Security is Here to Help

Feel free to contact the Tenable Cloud Security research lab with any questions or concerns you have about [cloud security](https://tenable.com/cloud-security/solutions/azure).

[@terminatorLM](https://twitter.com/terminatorlm)  
[@NoamDahan](https://twitter.com/noamdahan)  
[@arieitan](https://twitter.com/arieitan)

## Author

## Learn more

[![Liv Matan](/sites/default/files/pictures/2024-03/Liv-Matan.jpg) ]()

### [Liv Matan](/profile/liv-matan)

##### Senior Security Researcher, Tenable

Liv is a Senior Security Researcher at Tenable, specializing in cloud, application and web security. As a bug bounty hunter, Liv has found vulnerabilities in popular software platforms, including Azure, Google Cloud, AWS, Facebook and GitLab. Liv was recognized by Microsoft as a Most Valuable Securi... 

[Read more](/profile/liv-matan)

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

  * Tenable Cloud Security
