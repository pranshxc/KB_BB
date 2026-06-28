---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2024-08-07_unoauthorized-privilege-elevation-through-microsoft-applications.md
original_filename: 2024-08-07_unoauthorized-privilege-elevation-through-microsoft-applications.md
title: 'UnOAuthorized: Privilege Elevation Through Microsoft Applications'
category: documents
detected_topics:
- oauth
- access-control
- api-security
- sso
- command-injection
- otp
tags:
- imported
- documents
- oauth
- access-control
- api-security
- sso
- command-injection
- otp
language: en
raw_sha256: a6bf4432ab9190cbd5d30ca2f73374e1eaaf594a496c16a28ae00c69a32bc37e
text_sha256: 3274f58b9a8ff9d2233d957bfb0fa9179c4391713c104ae3c5b8b41d834e22bd
ingested_at: '2026-06-28T07:32:37Z'
sensitivity: unknown
redactions_applied: false
---

# UnOAuthorized: Privilege Elevation Through Microsoft Applications

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2024-08-07_unoauthorized-privilege-elevation-through-microsoft-applications.md
- Source Type: markdown
- Detected Topics: oauth, access-control, api-security, sso, command-injection, otp
- Ingested At: 2026-06-28T07:32:37Z
- Redactions Applied: False
- Raw SHA256: `a6bf4432ab9190cbd5d30ca2f73374e1eaaf594a496c16a28ae00c69a32bc37e`
- Text SHA256: `3274f58b9a8ff9d2233d957bfb0fa9179c4391713c104ae3c5b8b41d834e22bd`


## Content

---
title: "UnOAuthorized: Privilege Elevation Through Microsoft Applications"
page_title: "Privilege Elevation in Entra ID: UnOAuthorized | Semperis Research"
url: "https://www.semperis.com/blog/unoauthorized-privilege-elevation-through-microsoft-applications/"
final_url: "https://www.semperis.com/blog/unoauthorized-privilege-elevation-through-microsoft-applications/"
authors: ["Eric Woodruff (@ericonidentity)"]
programs: ["Microsoft (Entra ID / Azure AD)"]
bugs: ["Cloud", "Privilege escalation"]
publication_date: "2024-08-07"
added_date: "2024-08-14"
source: "pentester.land/writeups.json"
original_index: 93
---

[Back to blogs listing](/blog/)

# UnOAuthorized: Privilege Elevation Through Microsoft Applications

  * Identity Attack Catalog
  * Read 11 MIN

  * Application integration
  * Multitenant apps in Entra ID
  * Multiple credentials
  * Acting as Microsoft apps
  * Elevating privileges through Microsoft apps
  * Our findings
  * Privilege escalation and persistence
  * The fix
  * Detecting prior abuse
  * Protection for Semperis customers
  * Stopping attacks 
  * Related research and acknowledgements
  * Disclosure and timeline

**Eric Woodruff | Chief Identity Architect**

This article details a series of [Semperis](https://www.semperis.com/) security research team discoveries that resulted in the ability to perform actions in Entra ID beyond expected authorization controls, based on analysis of the OAuth 2.0 scope (permissions). Our most concerning discovery involved the ability to add and remove users from privileged roles, including the most powerful role in Entra ID: Global Administrator. We reported our findings to the Microsoft Security Response Center (MSRC), and we have worked with Microsoft to ensure that these discoveries have been resolved.

Although it is unknown if any organizations were compromised previously through this finding in the wild, a threat actor could have used such access to perform privilege elevation to Global Administrator and install further means of persistence in a tenant. An attacker could also use this access to perform lateral movement into any system in Microsoft 365 or Azure, as well as any SaaS application connected to Entra ID.

The discovery does require that the initiator holds the Application Administrator or Cloud Application Administrator role in Entra ID, which is considered privileged. In many enterprises, the unfortunate reality is that users assigned these roles are not treated as privileged, making them prime targets for an attacker.

Concerned organizations should understand how to detect whether their Microsoft applications might have been targeted, as documented later in this article.

## Application integration primer

To understand this attack vector, you need to understand the foundational components involved.

Customers of Microsoft 365 and Azure might be familiar with the systems and services with which they interact, including Microsoft Teams, SharePoint Online, Exchange Online, Azure Key Vault, and admin portals like the Azure portal and Microsoft 365 Admin Center, and the suite of other Microsoft services. What you might not be aware of are the hundreds of Microsoft applications that keep your Microsoft estate running. Outside of Microsoft itself, these applications might be referred to as first-party applications because they are not provided by a third-party ISV.

Entra ID is the identity platform and authorization engine of every Microsoft 365 and Azure environment. Customers that federate authentication to Okta, Ping Identity, or other identity providers with Microsoft services still must manage the authorization model that exists within their Microsoft estate. Entra ID is the underpinning authorization mechanism that allows these Microsoft applications to interact and operate with one another, using industry standards for modern authentication and authorization: OpenID Connect and OAuth 2.0.

Each Microsoft customer has its own Entra (previously known as Azure AD) tenant. In each tenant, every Microsoft application is represented by a security principal object known as a _service principal._ Users and groups are security principals we all might be most familiar with; you can assign roles and permissions to these principals. Just like users and groups, roles and permissions can be assigned to applications by way of their service principals. These roles and permissions are evaluated when interacting with Entra ID or other Microsoft 365 services.

## Multitenant applications in Entra ID

Entra ID typically considers all Microsoft applications, even those that have unique properties, to be multitenant applications.

With multitenant applications, the developer defines how the application should operate in the app registration. This includes actions such as defining the Microsoft Graph API permissions that the application needs, as well as the credential used by the application for accessing Microsoft Graph. Microsoft Graph is the unified API endpoint for several Microsoft services, including Entra ID.

When an organization consumes a multitenant application, the application is represented in the consuming tenant by a service principal (_Figure 1_).

![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201024%20524'%3E%3C/svg%3E)_Figure 1. Example application registration and its service principal relationship._

## The case of multiple credentials

Entra ID allows the assignment and use of two types of credentials for authentication: secrets (passwords) and keys (certificates). Either type of credential worked within the context of our discovery. Going forward, I will collectively refer to both secrets and keys simply as credentials.

Where things become interesting is that Entra ID permits storage of credentials in two places: in the app registration (which, as mentioned, the developer manages) and in the service principal. In the case of multitenant applications, the service principal is in the customer tenant and under control of the customer, who can then assign credentials to the service principal (_Figure 2_).

![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201024%20524'%3E%3C/svg%3E)_Figure 2. Diagram showing that Fabrikam tenant set a credential on the service principal._

To protect against the assignment or use of secrets on service principals, application developers can use a mechanism in Entra ID called _app instance property lock._ From our research and discussion with Microsoft, Microsoft leverages a different mechanism that can provide the same end result: not allowing authentication using a credential on a service principal.

Whether a credential is assigned to an app registration or service principal, both can be used to perform an OAuth 2.0 client credential grant flow to act as that application in Microsoft Graph (_Figure 3_).

![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201024%20519'%3E%3C/svg%3E)_Figure 3. OAuth 2.0 client credential grant flow in Entra ID._

During a client credential grant flow, the following steps occur:

  1. The application uses its client ID and credential to authenticate to Entra ID. An application effectively is anything that knows the client ID, tenant ID, and credential. So for the purposes of this abuse, although the named application might be a Microsoft application, the acting application is the attacker. 
  2. Entra ID validates the client ID and credential and responds with an access token. 
  3. The application requests data from Microsoft Graph, passing along the token. 
  4. Microsoft Graph validates the access token. 
  5. If the token is valid, Microsoft Graph provides the requested data or action.

Full details on this flow can be found in the Microsoft documentation [“Microsoft identity platform and the OAuth 2.0 client credentials flow.”](https://learn.microsoft.com/en-us/entra/identity-platform/v2-oauth2-client-creds-grant-flow)

Because Microsoft Graph is a REST API, actions such as GET can be used to request data from Entra ID, and actions such as POST and PATCH can be used to create or modify data in Entra ID.

If an application has the application permission **Group.Create** assigned to it and you have the credential for that application, you can create a group, and the Entra ID audit logs would show that the group was created by the service principal for that application.

As an example, suppose you have a third-party application named _Custom Application,_ which you use to access Microsoft Graph via the Microsoft Graph PowerShell SDK. The credentials that are passed as _$creds_ contain the application ID and the credential (_Figure 4_).

![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201024%20524'%3E%3C/svg%3E)_Figure 4. Connecting to Microsoft Graph as Custom Application._

If you were to perform actions using permissions consented to for this application—in this case, **Group.Create** —those actions show up in the Entra ID audit logs as being performed by the application. As you can see in _Figure 5,_ the application is the security principal responsible for the “Add group” operation.

![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201024%20524'%3E%3C/svg%3E)_Figure 5. Results of creating a group as Custom Application._

## Acting as Microsoft applications

In Entra ID, Microsoft historically has allowed customers to assign credentials to almost all Microsoft application service principals. In limited instances, these credentials can be used in OAuth 2.0 client credential grant flows to access Microsoft Graph, acting as the Microsoft application within the customer’s own tenant.

As with the custom application in the previous example, we assigned a credential to the service principal for the Microsoft application _Device Registration Service._ We were then able to authenticate and access Microsoft Graph as Device Registration Service (_Figure 6_).

![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201024%20524'%3E%3C/svg%3E)_Figure 6. Connecting to Microsoft Graph as Device Registration Service._

## Elevating privileges through Microsoft applications

Through our research, we discovered that select Microsoft application service principals were allowed to perform certain actions that were not defined in the list of authorized permissions. That is, we were allowed to perform certain privileged actions even though we did not appear to have permission to do so.

Within Microsoft Graph, the available permissions can be determined by examining the assigned _scopes_ —the OAuth 2.0 term for permissions.

In our example that _Figure 6_ shows, you can see that the scopes are empty for the Device Registration Service _(Figure 7_). That should mean that this application has no permission to do anything through the Graph API, and we should have received a 403 unauthorized response when attempting an unauthorized action.

![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201024%20524'%3E%3C/svg%3E)_Figure 7. Our empty scopes (permissions) for Device Registration Service._

Yet when we attempted to perform certain privileged actions, we were able to do so. In this example, _Figure 8_ and _Figure 9_ show a successful attempt to add a user to the Global Administrator role as Device Registration Service.

![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201024%20524'%3E%3C/svg%3E)_Figure 8. Adding a user to the Global Administrator role as Device Registration Service._ ![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201024%20524'%3E%3C/svg%3E)_Figure 9. Entra ID audit log results showing successful role management._

## Our findings

Through our research, we discovered the following abilities for each of the specified services. The scope of impact is within the targeted Entra tenant.

### Viva Engage (Yammer)

The ability to delete and permanently delete users, including privileged users such as Global Administrators. MSRC classified this ability as a medium severity vulnerability.

### Microsoft Rights Management Service

The ability to create users. MSRC classified this ability as low severity. The explanation for low severity was due to the created user objects not being privileged.

### Device Registration Service

The ability to modify membership of privileged roles, including the Global Administrator role. MSRC classified this ability as important severity, privilege elevation under Identity (Entra ID).

## Using the mechanism for privilege elevation and persistence

All our findings are concerning in that they bypass known authorization controls. However, the Device Registration Service finding is the focal point for privilege elevation and potential persistence from an attacker.

In an Entra tenant, Application Administrators, Cloud Application Administrators, Global Administrators, and users assigned as an Owner of an application can assign credentials to the service principal.

Application Administrator and Cloud Application Administrator are considered privileged roles by Microsoft, as noted in its documentation [“Microsoft Entra built-in roles.”](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#application-administrator) In many enterprises, third-party application integrations might provide other paths of privilege elevation and abuse if an Application Administrator or Cloud Application Administrator became compromised, whether or not the organization is aware that they are setting up these paths.

However, in a greenfield (new) Entra tenant, neither the Application Administrator nor Cloud Application Administrator have the rights in an Entra tenant to manage privileged role assignment.

It’s also important to note that these roles **do not** have the ability to consent to Microsoft Graph API permissions, which is a common misunderstanding by those working within Entra ID.

If an attacker aware of the flaw with Device Registration Service were to compromise a user assigned the role of Application Administrator or Cloud Application Administrator, the attacker could use that access to gain a foothold into the Global Administrator role or any other desired role.

Although it may seem a bit blunt for an attacker to persist with the Global Administrator role, persistence could be installed with these privileges by creating a new app registration and service principal with privileged application permissions. Likewise, an attacker could install new privileged application permissions into an existing single-tenant application or find an existing privileged application and install additional credentials. Organizations that are not continually monitoring for these sorts of changes and that do not have the maturity to determine known from malicious operations in Entra ID would likely remain unaware of the installation of persistent access or the temporary modification of role assignment in Entra ID.

## The fix and the hidden missing link

We appreciate the conversations we had with MSRC and the Microsoft Identity team during resolution of our findings. Our concern revolved primarily around the lack of scope (permission) within our access to Microsoft Graph.

During our conversation, Microsoft noted that it has other authorization mechanisms that exist behind the scenes for Microsoft applications. These mechanisms allowed us to perform the actions described in this article.

Microsoft rightfully highlighted that this capability is therefore not a material flaw within any of its authorization models. However, it acknowledged that externally, based on what we can view and have access to, the capabilities might appear to be in error. External to Microsoft, OAuth 2.0 scopes are absolute when interacting with Microsoft Graph, so without knowledge of other authorization systems, we can only infer.

Further, our research has resulted in many changes on the part of Microsoft in further restricting the ability to use credentials on Microsoft applications. Microsoft has been further implementing controls that restrict the ability to use credentials on service principals. We have observed that the list of service principals as which we can authenticate has continually dwindled

When we now attempt to authenticate as Device Registration Service, we receive an error from Microsoft Graph (_Figure 10_).

![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201024%20524'%3E%3C/svg%3E)_Figure 10. Failed authentication as Device Registration Service._

## Detection of prior abuse

The applications at the core of our findings are likely to exist in most Microsoft customer estates. We hold a strong position that this flaw has existed for at least as long as these applications have, which goes back several years.

The two methods of detection for this abuse are Entra ID audit logs and lingering credentials on the abused applications. Unfortunately, both methods have their limits. Audit logs provide value only for as long as they are retained, and an attacker could have removed the credential on initial abused applications after installing further persistence.

If an organization finds data that indicates that credentials have been assigned to Device Registration Service or discovers audit data for the Device Registration Service, it should have a high level of concern. We know of no valid reason for Device Registration Service to have a credential assigned to it.

### Lingering credentials

You can use Microsoft Graph to inspect affected service principals so that you can determine whether additional credentials have been added to them.

For these Graph queries, inspect the output to determine whether values have been set or whether the credential is returned as null.

The application ID is a globally unique value. These PowerShell commands and Microsoft Graph query will work in any Entra tenant.

#### Device Registration Service

##### Microsoft Graph PowerShell SDK

`((Get-MGServicePrincipal -Filter "AppId eq '01cb2876-7ebd-4aa4-9cc9-d28bd4d359a9'").KeyCredentials).count`

`((Get-MGServicePrincipal -Filter "AppId eq '01cb2876-7ebd-4aa4-9cc9-d28bd4d359a9'").PasswordCredentials).count`

##### Microsoft Graph query

`https://graph.microsoft.com/v1.0/servicePrincipals(appId='01cb2876-7ebd-4aa4-9cc9-d28bd4d359a9')?$select=keyCredentials,passwordCredentials`

### Audit log entries

Organizations can examine Entra ID audit log data that match certain patterns. Note that the ability to search audit log data will be feasible only as far back as the organization has stored those logs.

#### Hunting for actions by Device Registration Service

`AuditLogs`

`| where parse_json(tostring(InitiatedBy.app)).displayName == "Device Registration Service"`

#### Hunting for assignment of secrets to Device Registration Service

`AuditLogs`

`| where OperationName == "Add service principal credentials"`

`| where TargetResources[0].displayName == " Device Registration Service"`

## Protecting Semperis customers

For users of [Semperis Directory Services Protector (DSP)](https://www.semperis.com/active-directory-security/) or [Purple Knight](https://www.semperis.com/purple-knight/), we are releasing a security indicator, **Suspicious credentials on Microsoft service principal,** that will check for and report credentials assigned to Device Registration Services and Viva Engage. From an approach to layered identity security, organizations may also check their SIEM audit logs for markers.

## Stopping attacks targeting privileged applications

Privileged applications and their service principals in Entra ID are one of the most common means that attackers have for gaining a foothold and maintaining persistence in Entra ID and for moving into other cloud estates such as Microsoft 365, Azure, and multicloud and SaaS applications that integrate with Entra ID.

One of the best defenses organizations can take is ensuring that the Application Administrator and Cloud Application Administrator are treated as highly privileged as Global Administrators, and best practices such as privilege separation, privileged access workstations, and strong phishing-resistant authentication are treated as requirements, not options.

## Related research and acknowledgements

Research in the space of Entra ID applications and service principals is not a novel concept. Our research overlaps with [similar 2019 research by Dirk-jan Mollema](https://dirkjanm.io/azure-ad-privilege-escalation-application-admin/), which explored assigning credentials to service principals and leveraging OAuth 2.0 application permissions to perform functions that an Application Administrator should not be able to perform. Since then, the list of applications that can be used has dwindled and was further reduced in July 2024 as the result of Microsoft’s response to our findings.

## Disclosure and timeline

The discoveries described in this post were reported to MSRC as documented in the following timeline. As a complex discovery, it took some time to work through the findings with MSRC. We appreciate the expediency with which the Device Registration Service finding was resolved and the commitment on the part of Microsoft to further secure its applications based on our collaborative work.

  * January 11, 2024: MSRC cases created 
  * January 30, 2024: MSRC provided initial response of low severity 
  * February 6, 2024: Response provided to MSRC regarding severity assignment 
  * March 4, 2024: Device Registration Service reclassified as important severity 
  * March 4, 2024: Viva Engage classified as low severity 
  * March 4, 2024: Microsoft Rights Management Services classified as low severity 
  * March 4, 2024: Microsoft Rights Management Services case resolved and closed 
  * March 4, 2024: Device Registration Service case resolved and closed 
  * April 1, 2024: Viva Engage reclassified as medium severity 
  * April 17, 2024: Provided initial notice to MSRC regarding disclosure 
  * April 19, 2024: Viva Engage case resolved and closed 
  * June 5, 2024: Sent draft of disclosure article to MSRC 
  * June 13, 2024: Meeting with MSRC regarding cases and disclosure
  * August 7, 2024: Public disclosure

![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%200%200'%3E%3C/svg%3E)

### Sign Up for the Latest Semperis News
