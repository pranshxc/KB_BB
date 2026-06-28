---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-03-09_escalating-from-logic-app-contributor-to-root-owner-in-azure.md
original_filename: 2022-03-09_escalating-from-logic-app-contributor-to-root-owner-in-azure.md
title: Escalating from Logic App Contributor to Root Owner in Azure
category: documents
detected_topics:
- access-control
- api-security
- cloud-security
- ssrf
- command-injection
- path-traversal
tags:
- imported
- documents
- access-control
- api-security
- cloud-security
- ssrf
- command-injection
- path-traversal
language: en
raw_sha256: 91d5713cb7eb1811fe7ce53a6b58d99d33204bd921906369e5fd6daf4ae0353a
text_sha256: 1fe3bc9135691221615789367495eb9be66b05c378e8fb2fd9e458e7ddf1639b
ingested_at: '2026-06-28T07:32:10Z'
sensitivity: unknown
redactions_applied: false
---

# Escalating from Logic App Contributor to Root Owner in Azure

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-03-09_escalating-from-logic-app-contributor-to-root-owner-in-azure.md
- Source Type: markdown
- Detected Topics: access-control, api-security, cloud-security, ssrf, command-injection, path-traversal
- Ingested At: 2026-06-28T07:32:10Z
- Redactions Applied: False
- Raw SHA256: `91d5713cb7eb1811fe7ce53a6b58d99d33204bd921906369e5fd6daf4ae0353a`
- Text SHA256: `1fe3bc9135691221615789367495eb9be66b05c378e8fb2fd9e458e7ddf1639b`


## Content

---
title: "Escalating from Logic App Contributor to Root Owner in Azure"
page_title: "Escalating from Logic App Contributor to Root Owner in Azure | NetSPI"
url: "https://www.netspi.com/blog/technical/cloud-penetration-testing/azure-logic-app-contributor-escalation-to-root-owner/"
final_url: "https://www.netspi.com/blog/technical-blog/cloud-penetration-testing/azure-logic-app-contributor-escalation-to-root-owner/"
authors: ["Josh Magri (@passthehashbrwn)"]
programs: ["Microsoft"]
bugs: ["Privilege escalation"]
publication_date: "2022-03-09"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 2838
---

[Technical](/blog/technical-blog/#post-container) / Cloud Pentesting 

# Escalating from Logic App Contributor to Root Owner in Azure

March 9, 2022

### [Josh Magri](/authors/josh-magri/)

  * [](https://www.facebook.com/sharer/sharer.php?u=https://www.netspi.com/blog/technical-blog/cloud-pentesting/azure-logic-app-contributor-escalation-to-root-owner/)
  * [](https://twitter.com/intent/tweet?text=Escalating from Logic App Contributor to Root Owner in Azure&url=https://www.netspi.com/blog/technical-blog/cloud-pentesting/azure-logic-app-contributor-escalation-to-root-owner/)
  * [](https://www.linkedin.com/shareArticle?mini=true&url=https://www.netspi.com/blog/technical-blog/cloud-pentesting/azure-logic-app-contributor-escalation-to-root-owner/&title=Escalating from Logic App Contributor to Root Owner in Azure)

![Escalating from Logic App Contributor to Root Owner in Azure](https://www.netspi.com/wp-content/uploads/2024/03/Blog-Feature-Images-14.webp)

In October 2021, I was performing an [Azure penetration test](/security-testing/azure-penetration-testing). By the end of the test, I had gained Owner access at the Root level of the tenant. This blog post will provide a short walkthrough of what I found and disclosed to the Microsoft Security Response Center (MSRC).

### What was the bug?

The short explanation is that having Contributor access to an Azure Resource Manager (ARM) API Connection would allow you to create arbitrary role assignments as the connected user. This was supposed to be limited to actions at the Resource Group level, but an attacker could escape to the Subscription or Root level with a path traversal payload.

### How did I find it?

It’s fair to say that I have spent a lot of time [hacking on Logic Apps](/blog/technical/cloud-penetration-testing/illogical-apps-exploring-exploiting-azure-logic-apps/), and I experience a lot of recency bias with the services that I’ve dug into. After I published my Logic App research, I started seeing Logic Apps popping up on my tests. 

To recap, Azure Logic Apps use API Connections to authenticate actions to services. In my blog, [Illogical Apps – Exploring and Exploiting Azure Logic Apps](/blog/technical/cloud-penetration-testing/illogical-apps-exploring-exploiting-azure-logic-apps/), I discuss how to tease unintended functionality out of Logic Apps to perform actions as the authenticated user. The examples I use involve listing out additional key vault keys or adding users to Azure AD. 

When we create an API Connection, it requires a user to authenticate it. That authentication will persist for the lifetime of the API Connection, unless changes are made to it which will invalidate the connection. You can view the connection dialog below.

![API Connection dialog](https://www.netspi.com/wp-content/uploads/030922_Logic-App-Priv-Esc_Tech-Blog_1.png)

In this environment there was an Azure Resource Manager API Connection authenticated as a user with User Access Administrator rights at the Root level. If you’re not familiar with Azure terminology, the User Access Administrator role allows for creating new role assignments, and the Root level is the highest tier in an Azure tenant. I had not looked at the ARM connector in my prior research, but I was confident we could abuse this level of access.

### Initial Recon

Generally, our goal is to escalate to the Owner role on a Subscription. This is similar to getting Domain Administrator (DA) on an [internal network penetration test](/security-testing/network-penetration-testing-internal) in the sense that it is a bit oversimplified, but very useful for demonstrating the severity of a finding. I started looking at the relevant ARM actions that I could use to achieve this. Consulting the [Microsoft documentation](https://docs.microsoft.com/en-us/connectors/arm/), “Create or update a resource group” looked like a good starting point. But looking at the parameters for the action, the Subscription and Resource Group parameters are required.

![Create or update a resource group](https://www.netspi.com/wp-content/uploads/030922_Logic-App-Priv-Esc_Tech-Blog_2.png)

While they’re required, we can insert custom values. If we make the Resource Group blank, will that work? No. Here’s why: API Connections are just wrappers around an API as the name would suggest. These APIs are defined by Swagger docs, and we can pull down the whole Swagger definition by using an ARM API Connection in a Logic App and making a request to the following resource:
  
  
  /subscriptions/{subscription}d/resourceGroups/{resourceGroupName}/
  Providers/Microsoft.Logic/Workflows/{LogicAppName}?api-version=
  2016-10-01&$expand=properties/swagger

Looking at the Swagger definition, the endpoint for this action is a PUT request to this path:
  
  
  /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/
  providers/{resourceProviderNamespace}/{shortResourceId}

So, we can reasonably assume that when we use a blank Resource Group name, a request is getting made to:
  
  
  /subscriptions/{subscriptionId}/resourceGroups//providers/
  [truncated]

And we get an error since this Resource Group does not exist. At this point, I verified that using a valid Subscription and Resource Group name, it was possible to create Role Assignments at the Resource Group level. This is because Role Assignments are created like any other resource in Azure. At a minimum I was able to (as a Contributor) give myself Owner rights on all the Resource Groups in a Subscription. Still not a bad privilege escalation, but we can do better.

You might have spotted where this is headed given the format of the path above. If we can include custom values for the Resource Group and Subscription, can we manipulate the final path to perform actions at different scopes? If we provide “..%2F” as the Resource Group name, then our path will match the right Swagger path, but the server will resolve the payload and our request will end up going to:
  
  
  /subscription/{subscriptionId}/providers/[truncated]

Now we can create Role Assignments at the Subscription level! Taking this one step further, we can traverse the Subscription path too, and create Role Assignments at the Root level (if the connected user has sufficient access).

### Unnecessary Optimizations

At this point I had a working exploit in my lab, and I went to reproduce it in the client environment. It went off without a hitch, and I was now a Subscription Owner. While I was setting up the Logic App, I noticed something that I hadn’t before: Since my lab environment is very small, when I clicked the Subscription dropdown menu, it was populated with Subscriptions that my account didn’t have access to. This meant that these Subscriptions were being fetched in the context of the API Connection user – but I hadn’t run a Logic App.

To track down the behavior, I fired up Burp Suite and found that a request was being made to the “dynamicInvoke” endpoint of the API Connection. The request payload looked like this:
  
  
  {"request":{"method":"get","path":"/subscriptions","queries":
  {"x-ms-api-version":"2016-06-01"},}}

And the response looked like this:
  
  
  "response":{"statusCode":"OK","body":{"value":[{"id":
  "/subscriptions/[REDACTED]","authorizationSource":"RoleBased",
  "subscriptionId":"[REDACTED]","displayName":"temp_sub","state":
  "Enabled","subscriptionPolicies":{"locationPlacementId":
  "Public_2014-09-01","quotaId":"PayAsYouGo_2014-09-01",
  "spendingLimit":"Off"}}]},

Another area that I’ve spent a lot of time looking at is Azure’s REST API. Given that the response JSON included a status code, I figured the request to the dynamicInvoke endpoint triggered the server into making a request in the context of the connected user. 

For those curious, my understanding is that the server makes a request to ``https://logic-apis-[region].token.azure-apim.net:443/tokens/logic-apis-[region]/[connectorname]/[connector-id]/exchange`` which returns a token to the server. 

You can verify this by sending malformed input in the path value to the dynamicInvoke endpoint and observing the output. I assume that the returned token is then used to access the relevant services as the connected user.

Anyways, we can just hit this endpoint directly to trigger our exploit instead of creating a Logic App. This is what the final payload looked like:
  
  
  {
  'request':{
  'method':'PUT','path':'/subscriptions/$subscriptionId/
  resourceGroups/..%2Fproviders/Microsoft.Authorization/
  roleAssignments%2F$guid',
  'queries':{'x-ms-api-version':'2015-07-01'},
  'body':{
  'properties':{
  'principalId': '$principalId',
  'roleDefinitionId': '/providers/
  Microsoft.Authorization/roleDefinitions/$roleDefinitionId'
  }}}
  

I also confirmed that trying to hit the Subscription directly (without the resourceGroups part) via this endpoint did not work, it would yield a 404 error. But if we included the path traversal payload, then a nice “201 Created” message was returned instead. This is important, because it is proof that this wasn’t an intended behavior. 

### Conclusion

To summarize, I was able to escalate from a Subscription Contributor to Root Owner by abusing an API Connection. The root cause of this behavior was that a path traversal payload would meet the Swagger API definition, and the payload would be resolved by the server resulting in a request to an unintended scope. 

This issue was responsibly disclosed to MSRC and [acknowledged by Microsoft](https://msrc.microsoft.com/update-guide/acknowledgement/) in March 2022. They remediated the issue by filtering the method value to block the paths that include the path traversal payload. 

I would still recommend that anyone using API Connections should evaluate what users are authenticated for each connection. If any of the authenticated users are privileged, there may a possibility for abuse.

## Explore More Blog Posts

[ ![](https://www.netspi.com/wp-content/uploads/2024/07/072924_TECH_GCPwn_Feature.webp) Cloud Pentesting Bypassing Microsoft Entra Conditional Access Policies via Nested App Authentication  June 22, 2026 Discover how attackers bypassed Microsoft Entra Conditional Access Policies using Nested App Authentication (NAA) flows in this technical vulnerability breakdown. Learn More ](https://www.netspi.com/blog/technical-blog/cloud-pentesting/bypassing-microsoft-entra-conditional-access-policies-via-nested-app-authentication/)[ ![](https://www.netspi.com/wp-content/uploads/2026/06/Feature-Image_Red-Plaid.jpg) Social Engineering I’m Just Asking Questions: Social Engineering as a Reporter  June 17, 2026 Dive into this real-world social engineering assessment where a fake anonymous tip and an adversary-in-the-middle framework tested the limits of an organization's security policies. Learn More ](https://www.netspi.com/blog/technical-blog/social-engineering/im-just-asking-questions-social-engineering-as-a-reporter/)[ ![](https://www.netspi.com/wp-content/uploads/2025/12/TB-Design-6_Feature-Image.png) CISO Perspectives Beyond the Hype: What Regulated Industries Need to Know Before Trusting AI Security Tooling  June 16, 2026 AI security tools can build an attack, but enterprise security teams in regulated industries need consistency, auditability, and predictable costs before they can trust one. Learn why the surrounding infrastructure is where most AI security vendors are still falling short. Learn More ](https://www.netspi.com/blog/executive-blog/ciso-perspectives/beyond-the-hype-what-regulated-industries-need-to-know-before-trusting-ai-security-tooling/)
