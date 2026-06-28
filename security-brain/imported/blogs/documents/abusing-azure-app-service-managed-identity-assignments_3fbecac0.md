---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-02-15_abusing-azure-app-service-managed-identity-assignments.md
original_filename: 2023-02-15_abusing-azure-app-service-managed-identity-assignments.md
title: Abusing Azure App Service Managed Identity Assignments
category: documents
detected_topics:
- api-security
- jwt
- access-control
- command-injection
- sso
- mfa
tags:
- imported
- documents
- api-security
- jwt
- access-control
- command-injection
- sso
- mfa
language: en
raw_sha256: 3fbecac0ce09eeef20407361da0cf1f03b4c43d9068939fc44fe958733a3180b
text_sha256: afb42bcfabe99f8551703df5a11a2058714d8374ab0e4f3b7b5104c767ba2dc4
ingested_at: '2026-06-28T07:32:18Z'
sensitivity: unknown
redactions_applied: false
---

# Abusing Azure App Service Managed Identity Assignments

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-02-15_abusing-azure-app-service-managed-identity-assignments.md
- Source Type: markdown
- Detected Topics: api-security, jwt, access-control, command-injection, sso, mfa
- Ingested At: 2026-06-28T07:32:18Z
- Redactions Applied: False
- Raw SHA256: `3fbecac0ce09eeef20407361da0cf1f03b4c43d9068939fc44fe958733a3180b`
- Text SHA256: `afb42bcfabe99f8551703df5a11a2058714d8374ab0e4f3b7b5104c767ba2dc4`


## Content

---
title: "Abusing Azure App Service Managed Identity Assignments"
page_title: "Abusing Azure App Service Managed Identity Assignments - SpecterOps"
url: "https://posts.specterops.io/abusing-azure-app-service-managed-identity-assignments-c3adefccff95"
final_url: "https://specterops.io/blog/2023/02/15/abusing-azure-app-service-managed-identity-assignments/"
authors: ["Andy Robbins (@_wald0)"]
programs: ["Microsoft (Azure)"]
bugs: ["Cloud"]
publication_date: "2023-02-15"
added_date: "2023-02-22"
source: "pentester.land/writeups.json"
original_index: 1524
---

[ Back to Blog  ](/blog)

[Research & Tradecraft](https://specterops.io/blog/category/research/)

# Abusing Azure App Service Managed Identity Assignments

Author

[Andy Robbins](https://specterops.io/blog/author/andy-robbins/)

Read Time

11 mins

Published

Feb 15, 2023

##### Share

[ ](https://www.linkedin.com/shareArticle?mini=true&url=https%3A%2F%2Fspecterops.io%2Fblog%2F2023%2F02%2F15%2Fabusing-azure-app-service-managed-identity-assignments%2F&title=Abusing+Azure+App+Service+Managed+Identity+Assignments&source=SpecterOps) [ ](https://twitter.com/share?url=https%3A%2F%2Fspecterops.io%2Fblog%2F2023%2F02%2F15%2Fabusing-azure-app-service-managed-identity-assignments%2F&text=Abusing+Azure+App+Service+Managed+Identity+Assignments) [ ](mailto:?Subject=I%20thought%20you'd%20like%20this%20post:%20Abusing Azure App Service Managed Identity Assignments&Body=https://specterops.io/blog/2023/02/15/abusing-azure-app-service-managed-identity-assignments/) [ ](https://specterops.io/blog/category/research/feed/)

### Intro

[Azure App Service](https://learn.microsoft.com/en-us/azure/app-service/overview) is a Platform-as-a-Service product that promises to improve web application deployment, hosting, availability, and security. Web Apps hosted by Azure App Service are organized into Azure App Service Plans, which are Virtual Machines that the Web Apps in that plan all run on. The individual Web Apps are isolated from one another by executing in their own containers on the shared Virtual Machine:

![](https://cdn-images-1.medium.com/max/1024/0*wiZoG_s2RB9uqdtw)

Like many AzureRM services, App Service allows you to assign [Managed Identities](https://learn.microsoft.com/en-us/azure/app-service/overview-managed-identity?tabs=portal%2Chttp) to the individual Web Apps. This feature creates a simple way for developers to let their applications access Azure resources without needing to worry about creating, storing, and updating credentials.

Managed Identities are great and admins should absolutely use them. But admins also need to understand the risks that come with Managed Identities and how to deal with those risks. In this blog post I will explain those risks, demonstrate how an attacker can abuse App Service Managed Identity assignments, and show you how to identify and deal with those risks yourself.

### Prior Work

[Karl Fosaaen](https://twitter.com/kfosaaen) wrote a great [blog post](https://www.netspi.com/blog/technical/cloud-penetration-testing/lateral-movement-azure-app-services/) in August of 2020 about Azure App Service abuses, including abusing managed identity assignments.

[Joshua Magri](https://twitter.com/passthehashbrwn) authored [Invoke-AppServicesCMD.ps1](https://github.com/NetSPI/MicroBurst/blob/master/Az/Invoke-AzAppServicesCMD.ps1) in 2021, which executes commands on Web App hosts through the Kudu API.

### Managed Identities, Service Principals, and JWTs

Admins can assign Managed Identities to Azure App Service Web Apps in one of two ways:

  1. As a system-assigned Managed Identity
  2. As a user-assigned Managed Identity

In either configuration, the result is the same: the Web App gains the ability to authenticate as an AzureAD Service Principal without needing to know that Service Principal’s ID or credential:

![](https://cdn-images-1.medium.com/max/1024/0*zD4qQhwxze8k0aqW)

To access Azure resources as this Service Principal, the Web App needs to retrieve a JSON Web Token (JWT), then use that JWT to authenticate to those Azure resources. Without a Managed Identity assignment, the Web App retrieves a JWT for a Service Principal in three steps:

  1. Retrieve the Service Principal’s Client ID and Secret, then submit those to the Security Token Service (STS) for the AzureAD tenant
  2. The STS authenticates the Service Principal by comparing the supplied client ID and secret to what’s currently stored on the Service Principal
  3. If the credentials are valid, the STS emits a JWT back to the Web App

![](https://cdn-images-1.medium.com/max/1024/0*XCVidKSDYWVcX84-)

But in a Managed Identity scenario, the steps are slightly different:

  1. The Web App requests a token from its local Managed Service Identity (MSI) endpoint
  2. The MSI service forwards this token request to the tenant STS
  3. The STS authenticates the Service Principal by inspecting the value of its managedIdentityResourceId attribute.
  4. If the calling Web App is listed in the Service Principal’s managedIdentityResourceId attribute, it emits a token back to the MSI
  5. The MSI emits the token back to the Web App

![](https://cdn-images-1.medium.com/max/1024/0*2ZKt1v_-cN8MZ-pt)

This presents a significant challenge to the attacker who wants to assume the identity of this Service Principal. Instead of relying on getting their hands on insecurely-stored credentials — and short of any MSI/IMDS-endpoint spoofing primitives — the attacker has no choice but to achieve code execution on the Web App container if they want to authenticate as the Service Principal.

### Extracting JWTs from the Azure App Service host

Azure App Service instances come in two flavors: Windows and Linux. When a Managed Identity assignment is created for this resource, the App Service instance can retrieve JWTs for the Managed Identity Service Principal via a [REST API](https://learn.microsoft.com/en-us/azure/app-service/overview-managed-identity?tabs=portal%2Chttp#connect-to-azure-services-in-app-code) accessible only to the App Service instance itself.

Every Azure App Service Web App comes with a “buddy site” running in the same container alongside it. The “buddy site” is running [Kudu](https://github.com/projectkudu/kudu), which allows for, among other things, command shell execution via various REST API endpoints.

With command execution on the instance we can get everything we need by reading two environment variables: IDENTITY_ENDPOINT and IDENTITY_HEADER. If the App Service is Windows, we can access a PowerShell web shell and read the environment variables that way:

![](https://cdn-images-1.medium.com/max/1024/0*_mFVdInjNeBGEeWD)

Same thing on Linux using the SSH web shell:

![](https://cdn-images-1.medium.com/max/1024/0*C9AXj5BSaIQNQfVQ)

With that information we make a very simple GET request to that endpoint, specifying the value for the identity header in that request as the “X-IDENTITY-HEADER” header:

On a Windows instance:

![](https://cdn-images-1.medium.com/max/1024/0*0bPCQ1AR-_4qiufF)

And on a Linux instance:

![](https://cdn-images-1.medium.com/max/775/0*vTfbOM5hwSGqSx5V)

These web applications are making calls to various Kudu API endpoints, and so you can achieve command execution on these containers even if you’re in a situation where you can’t use a web browser to access the Kudu interface.

For example, we can hit the /api/command endpoint with a simple PowerShell request and parse the output:

![](https://cdn-images-1.medium.com/max/589/0*6h-O92oWSZ-sLi-Y)

Here I’m passing a JWT in the $ARMToken variable, but you can also access these endpoints using FTP credentials stored on the App Service object:

![](https://cdn-images-1.medium.com/max/588/0*exHbn3UXKSAEzehU)

This is nothing new and these are well-documented features on the [Kudu GitHub repository](https://github.com/projectkudu/kudu/wiki/Kudu-architecture#authentication-and-authorization-model).

The only principals that can access the Kudu endpoints that allow for remote code execution are those with one of the following AzureRM roles scoped to the Azure App Service Web App or one of its parent objects:

  1. Owner
  2. Contributor
  3. Website Contributor

Of course, any principal with the “User Access Administrator” role will be able to grant themselves one of the above roles against the Web App, as well.

The above-mentioned roles are also the only built-in roles that allow a principal to fetch the FTP credentials stored on the Web App object.

If the web application itself has a remote-code execution vulnerability, an attacker will be able to extract the Web App’s Managed Identity JWT, as well. To demonstrate this I used a slightly modified version of [go-webshell](https://github.com/gb-sn/go-webshell) by [gb-sn](https://github.com/gb-sn) to execute the necessary PowerShell command to request and emit the JWT:

![](https://cdn-images-1.medium.com/max/1024/0*Xsgl8eD0pbaoGvql)

### Who Cares? What’s the big deal?

At this point you might be saying to yourself: “Who cares? These are features, not bugs. The product is working exactly as advertised’. And you’re right — there’s no flaw here, no vulnerability, nothing worth reporting to MSRC. The product is doing exactly what it’s designed to do.

The danger is not that these features exist or work the way they do. The danger is that these features can be abused as part of a greater attack path that may degrade the security posture of not just an individual Web App, but of the entire Azure environment.

Here is an example of a real set of attack paths we observed in a customer’s Azure environment:

![](https://cdn-images-1.medium.com/max/1024/0*fEKGs7o-Tzyiwy6r)

Starting from the left, this attack path works like this:

  1. The Azure App is associated with the Service Principal, meaning any credentials stored on the app are valid for authenticating as the Service Principal.
  2. The Service Principal is a member of an AzureAD security group.
  3. The AzureAD security group has the “Owner” role against an Azure subscription.
  4. The Azure subscription contains a resource group.
  5. The resource group contains a Virtual Machine.
  6. The Virtual Machine has a Managed Identity assignment to a Service Principal, meaning anyone with command execution on the VM can request a JWT for this Service Principal.
  7. The Service Principal has the “Virtual Machine Contributor” role scoped to another Virtual Machine.
  8. This Virtual Machine has a Managed Identity assignment to a different Service Principal.
  9. The Service Principal has the User Administrator role, giving it the ability to reset various users’ passwords, including the two shown in the graph.
  10. The Azure user has been added as an explicit owner over another Azure app.
  11. This Azure App authenticates as a particular Service Principal.
  12. This Service Principal has the Application Admin role, granting it the ability to add secrets to all apps and Service Principals in the tenant, including the two shown here.
  13. This Service Principal has the Privileged Role Admin role, allowing it to promote itself or anyone else to Global Administrator.

Seen in isolation, these individual configurations may seem totally harmless. But when analyzed and seen as part of an overall attack path — [when we think in graphs](https://github.com/JohnLaTwC/Shared/blob/master/Defenders%20think%20in%20lists.%20Attackers%20think%20in%20graphs.%20As%20long%20as%20this%20is%20true%2C%20attackers%20win.md) — the true risk of each configuration becomes clear.

### Prevention

There are several steps you should take, as a defender, to ensure these attack paths do not exist in your Azure environment:

### Step 1: Audit and Remove Privileges Held by Service Principals

Your first step should be to find any Service Principals that have been granted the most dangerous privileges in Azure. Audit both the active and eligible assignments for the following AzureAD admin roles:

  * Global Administrator
  * Privileged Role Administrator
  * Privileged Authentication Administrator
  * Partner Tier2 Support

You should also audit for any Service Principals that have been granted any of the following MS Graph app roles:

  * RoleManagement.ReadWrite.Directory
  * AppRoleAssignment.ReadWrite.All

If any Service Principal has been granted any of the above roles in AzureAD or MS Graph, you should immediately investigate that Service Principal for existing signs of misuse. You should also remove those role assignments from the Service Principals, if possible.

### Step 2: Audit Privileges Held by Other Principals

Unfortunately you may not be able to easily or immediately remove privileges that have been granted to a Service Principal. Your next step then will be to limit the exposure of those highly privileged Service Principals by auditing the users, groups, and Service Principals that have been granted any of the following AzureAD admin roles:

  * Application Administrator (including those scoped specifically to the Service Principal)
  * Cloud Application Administrator (including those scoped specifically to the Service Principal)
  * Directory Synchronization Accounts
  * Hybrid Identity Administrator
  * Partner Tier1 Support
  * Partner Tier2 Support

You should also audit the explicit owners of Service Principals you identified in Step 1 where you cannot easily or immediately remove privileges.

You should also audit other Service Principals that have been granted any of the following MS Graph app roles:

  * Application.ReadWrite.All
  * ServicePrincipalEndpoint.ReadWrite.All

Any user, group, or Service Principal that has been granted any of the above AzureAD admin roles, explicit ownership, or MS Graph app roles will be able to take over the Service Principals identified in Step 1. If possible, and if necessary, remove all of these privileges.

### Step 3: Audit Privileges Held Against the Web App

Unfortunately, you may not be able to immediately or easily remove privileges held by Service Principals associated with a Web App through a Managed Identity assignment. In that case, you can prevent the emergence of a privilege escalation opportunity by removing these Azure role assignments against the Web App where those principals have less privilege than the Service Principal associated with the Function App:

  * Owner
  * Contributor
  * Website Contributor
  * User Access Administrator

### Detection

Azure logs come in handy several different ways here:

### Detecting New, Dangerous Privileges Granted to Service Principals

Once you’ve verified that no Service Principals have the most dangerous privileges in AzureAD, you will want to put alerting in place to warn you if someone grants a Service Principal one of those dangerous privileges. When a Service Principal is granted an AzureAD admin role, the “Add member to role” log fires, telling you who granted what privilege to what principal:

![](https://cdn-images-1.medium.com/max/700/0*tXkStpZytiXuM6oc)

You should produce and triage an alert any time a Service Principal is granted one of the following most dangerous AzureAD admin roles:

  * Global Administrator (aka “Company Administrator”)
  * Privileged Role Administrator
  * Privileged Authentication Administrator
  * Partner Tier2 Support

Additionally, when a Service Principal is granted an MS Graph app role, the “Add app role assignment to Service Principal” log fires, telling you who gave what app role to what:

![](https://cdn-images-1.medium.com/max/700/0*UnBTkglCOQLbij3y)

You should produce and triage alerts any time a Service Principal is granted one of the following app roles against the MS Graph resource app:

  * RoleManagement.ReadWrite.Directory
  * AppRoleAssignment.ReadWrite.All

### Conclusion

Managed Identities are a fantastic mitigation against credential-theft attacks, and you should 100% absolutely be using them. But you must also remember that there are no silver bullets in security. In my opinion, Managed Identities eliminate huge amounts of risk, but they do create new types of risks that Azure admins must be aware of.

We will continue to study and share our findings around Managed Identities in Azure, along with other types of abuse primitives that attackers can use to execute attack paths.

![](https://medium.com/_/stat?event=post.clientViewed&referrerSource=full_rss&postId=c3adefccff95)

* * *

[Abusing Azure App Service Managed Identity Assignments](https://posts.specterops.io/abusing-azure-app-service-managed-identity-assignments-c3adefccff95) was originally published in [Posts By SpecterOps Team Members](https://posts.specterops.io) on Medium, where people are continuing the conversation by highlighting and responding to this story.

Post Views: 4,054

[ Andy Robbins ](https://specterops.io/blog/author/andy-robbins/)

Principal Security Researcher 

Andy Robbins is a Principal Security Researcher at SpecterOps. He is a co-creator of BloodHound. He specializes in Windows, Active Directory, Entra, and Azure tradecraft research and discovery.
