---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2024-01-24_sysall-how-a-simple-loophole-in-google-kubernetes-engine-puts-clusters-at-risk-o.md
original_filename: 2024-01-24_sysall-how-a-simple-loophole-in-google-kubernetes-engine-puts-clusters-at-risk-o.md
title: 'Sys:All: How A Simple Loophole in Google Kubernetes Engine Puts Clusters at
  Risk of Compromise'
category: documents
detected_topics:
- cloud-security
- access-control
- oauth
- sso
- jwt
- xss
tags:
- imported
- documents
- cloud-security
- access-control
- oauth
- sso
- jwt
- xss
language: en
raw_sha256: 2bc8a850393e3772353471cda73e8b2b68969a4dd84c9f0eb9fd5d519dc1d5d5
text_sha256: 0ceaa0f02f112f5f281335ef5bf7276530c57bf5e6acc140330f58e4d9bd0716
ingested_at: '2026-06-28T07:32:30Z'
sensitivity: unknown
redactions_applied: false
---

# Sys:All: How A Simple Loophole in Google Kubernetes Engine Puts Clusters at Risk of Compromise

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2024-01-24_sysall-how-a-simple-loophole-in-google-kubernetes-engine-puts-clusters-at-risk-o.md
- Source Type: markdown
- Detected Topics: cloud-security, access-control, oauth, sso, jwt, xss
- Ingested At: 2026-06-28T07:32:30Z
- Redactions Applied: False
- Raw SHA256: `2bc8a850393e3772353471cda73e8b2b68969a4dd84c9f0eb9fd5d519dc1d5d5`
- Text SHA256: `0ceaa0f02f112f5f281335ef5bf7276530c57bf5e6acc140330f58e4d9bd0716`


## Content

---
title: "Sys:All: How A Simple Loophole in Google Kubernetes Engine Puts Clusters at Risk of Compromise"
page_title: "Sys:All Google Kubernetes Engine Risk | Orca Security"
url: "https://orca.security/resources/research-pod/sys-all-google-kubernetes-engine-risk/"
final_url: "https://orca.security/resources/research-pod/sys-all-google-kubernetes-engine-risk/"
authors: ["Roi Nisimi (@roinisimi)", "Ofir Yakobi"]
programs: ["Google (GKE)"]
bugs: ["Kubernetes", "Cloud", "Privilege escalation"]
publication_date: "2024-01-24"
added_date: "2024-01-25"
source: "pentester.land/writeups.json"
original_index: 504
---

[ Blog Home](https://orca.security/resources/blog/)

  * [ Research Pod ](https://orca.security/resources/category/research-pod/)

![Sys:All: How A Simple Loophole in Google Kubernetes Engine Puts Many Thousands of Clusters at Risk of Compromise](https://orca.security/wp-content/uploads/2024/01/sys-all-risk-blog-1980.png?w=1044)

# Sys:All: How A Simple Loophole in Google Kubernetes Engine Puts Clusters at Risk of Compromise

[ ![Avatar of Roi Nisimi](https://orca.security/wp-content/uploads/2023/01/roi-nisimi_avatar.png) Roi Nisimi  ](https://orca.security/resources/author/roi-nisimi/)

Published: Jan 24, 2024 

  * [ __](https://twitter.com/share?text=Sys%3AAll%3A%20How%20A%20Simple%20Loophole%20in%20Google%20Kubernetes%20Engine%20Puts%20Clusters%20at%20Risk%20of%20Compromise&url=https%3A%2F%2Forca.security%2Fresources%2Fblog%2Fsys-all-google-kubernetes-engine-risk%2F)
  * [ __](https://www.linkedin.com/sharing/share-offsite/?url=https%3A%2F%2Forca.security%2Fresources%2Fblog%2Fsys-all-google-kubernetes-engine-risk%2F)
  * [ __](https://www.facebook.com/sharer.php?u=https%3A%2F%2Forca.security%2Fresources%2Fblog%2Fsys-all-google-kubernetes-engine-risk%2F)
  * [ __](mailto:?Subject=Sys:All: How A Simple Loophole in Google Kubernetes Engine Puts Clusters at Risk of Compromise&body=https%3A%2F%2Forca.security%2Fresources%2Fblog%2Fsys-all-google-kubernetes-engine-risk%2F)

The Orca Research Pod has uncovered a dangerous loophole in Google Kubernetes Engine (GKE) that could allow an attacker with _any Google account_ to take over a misconfigured Kubernetes cluster, potentially leading to serious security incidents such as cryptomining, denial of service, and sensitive data theft.

The loophole, which we dubbed _Sys:All_ , stems from a likely widespread misconception that the system:authenticated group in Google Kubernetes Engine includes only verified and deterministic identities, whereas in fact, it includes any Google authenticated account (including outside the organization). This misunderstanding then creates a significant security loophole when administrators unknowingly bind this group with overly permissive roles.

With only minimal effort, our research team found 250,000 active GKE clusters in the wild, with hundreds of them containing secrets that enabled lateral movement and sensitive data access. You can read more about these discoveries in the blog ‘[How the Sys:All Loophole Allowed Us To Penetrate GKE Clusters in Production](https://orca.security/resources/blog/sys-all-google-kubernetes-engine-risk-example/)’.

Orca immediately reported the matter to Google. Although changing this behavior is impractical due to breaking design, the GKE product team said Google recognizes the severity of this misconfiguration, has been proactive with prevention measures and customer notifications, and continues to take action to ensure customers’ safety. In addition to blocking the binding of the system:authenticated group to the cluster-admin role in newer GKE versions (version 1.28 and up), Google now notifies potentially vulnerable customers and plans further architectural changes. You can read more on Google’s response and advice for users in their [security bulletin](https://cloud.google.com/anthos/clusters/docs/security-bulletins#gcp-2024-003). We would like to emphasize that even though these are improvements, it still leaves many other roles and permissions (other than cluster-admin) that can be assigned to the system:authenticated group.

In this blog, we demonstrate just how easy it is to exploit this loophole, how many GKE clusters we believe are vulnerable, and how organizations can protect themselves against this risk. 

[Attend Threat Briefing](https://www.brighttalk.com/webcast/18490/605535?bt_tok=%7B%7Blead.Id%7D%7D&utm_source=OrcaSecurity&utm_medium=brighttalk&utm_campaign=605535)

## Executive Summary:

  * The [Orca Research Pod](https://orca.security/about/orca-research-pod/) discovered _Sys:All –_ a dangerous loophole that stems from the system:authenticated group in Google Kubernetes Engine that could lead to security breaches.
  * In the context of GKE, the system:authenticated group includes any user with a valid Google account. A discovery that increases the attack surface around Google Kubernetes Engine clusters.
  * The group is bound to several unharmful API discovery roles by default, but it can accidentally get bound to other permissive roles because administrators may mistakenly believe this is safe – especially since this would be the case for similar Kubernetes groups in AWS and Azure.
  * Any external attacker can utilize this misconfiguration by using their own Google Oauth 2.0 bearer token for reconnaissance and exploitation, without leaving an identified trail. 
  * Although this is [intended behavior](https://cloud.google.com/kubernetes-engine/docs/best-practices/rbac#default-roles-groups), Google did block the binding of the system:authenticated group to the cluster-admin role in newer GKE versions ([version 1.28 and up](https://cloud.google.com/anthos/clusters/docs/security-bulletins#gcp-2024-003)). However, it’s important to note that this still leaves many other roles and permissions that can be assigned to the group.
  * A [Threat Briefing](https://www.brighttalk.com/webcast/18490/605535?bt_tok=%7B%7Blead.Id%7D%7D&utm_source=OrcaSecurity&utm_medium=brighttalk&utm_campaign=605535) detailing how an attacker could abuse this GKE security loophole, what we found on GKE clusters in the wild, as well as recommendations on how to protect your clusters, will be held on January 26th at 11 pm Pacific Time.

## What is Google Kubernetes Engine?

GKE is a managed implementation of Kubernetes, with additional features and integrations added by Google, one of them being a seamless OIDC-based authentication with Google as the IdP (Identity Provider). GKE provides an out-of-the-box container orchestration solution, allowing users to focus on deploying and managing their applications without worrying about the underlying infrastructure.

GKE is the only Kubernetes cloud managed solution from the top three CSPs (AWS, Azure and GCP) that by default supports cluster authentication and authorization through standard IAM. This means that principals can authenticate and authorize against the Kubernetes API server using nothing but their Google credentials. Hence, the [system:authenticated](https://kubernetes.io/docs/reference/access-authn-authz/authentication/) group in GKE includes anyone with a valid Google account.

This discovery is important because administrators can easily be mistaken (especially when migrating self-managed clusters) into thinking that the GKE system:authenticated group includes only verified and deterministic identities. This misunderstanding then creates a significant security loophole when administrators decide to bind this group with overly permissive roles.

## What is the Kubernetes system:authenticated group?

The [system:authenticated group](https://kubernetes.io/docs/reference/access-authn-authz/authentication/) in Kubernetes is a special group that includes all authenticated entities, including human users and service accounts. Anyone who successfully authenticates to the Kubernetes API server, regardless of the authentication method used, will be automatically included in this unique group. Thus, it will share the same roles and permissions of the group.

## Technical step-by-step exploitation overview

### Authentication in Kubernetes

Any request to the Kubernetes API server must first be authenticated before it can get authorized. In order to successfully [authenticate](https://kubernetes.io/docs/reference/access-authn-authz/authentication/) to a Kubernetes cluster one must provide a client certificate or a bearer token of pre-registered entities. But what happens when none of those are presented?

Kubernetes will still authenticate the request by identifying it with two special objects: the ‘system:anonymous’ user and the ‘system:unauthenticated’ group. The request will then be authorized according to the roles binded to both objects. This is the case when Kubernetes is configured to enable anonymous access – which is the default in GKE.

When one of the authentication strategies is presented and validated, Kubernetes will not only identify the request with its corresponding user / service account, but also with the unique ‘system:authenticated’ group. Again, the request will then be authorized and granted with the accumulated permissions of both the matching entity and ‘system:authenticated’.

![](https://orca.security/wp-content/uploads/2024/01/image8.png)

By default, these objects are [granted](https://kubernetes.io/docs/reference/access-authn-authz/rbac/) with discovery roles which authorize both unauthenticated and authenticated users to read information that is deemed safe to be publicly accessible.

![](https://orca.security/wp-content/uploads/2024/01/image9.png?w=1075)

But what’s more interesting than the above roles, which may assist hackers with basic reconnaissance activities, is the fact that these special objects can get misconfigured. Kubernetes administrators may decide to bind these groups to a broader range of roles, and as a result introduce a significant risk to their cluster.

In the context of this matter – GKE, in contrast to [Amazon Elastic Kubernetes Service](https://aws.amazon.com/eks/) (EKS) and [Azure Kubernetes Service](https://azure.microsoft.com/en-us/products/kubernetes-service) (AKS), exposes a far reaching threat since it supports both anonymous and full OpenID Connect (OIDC) access. Unlike AWS and Azure, GCP’s managed Kubernetes solution considers any validated Google account as an authenticated entity. Hence, system:authenticated in GKE becomes a sensitive asset administrators should not overlook.

**Note:** I would like to mention that AKS and EKS both support authentication through Azure AD and AWS IAM respectively, but are limited to defined clusters and entities. GKE on the other hand, opens its authentication gate to pretty much anyone on the internet.  
  
We will not discuss the mechanics of authenticating to AKS and EKS, nor authorization to Kubernetes through Google Cloud IAM, as these concepts are out of the scope of this blog post.

### How easy it is to obtain a Google Token

#### Setting up a cluster

We’ve created a temporary GKE cluster for this demonstration, keeping all basic settings as they are. As discussed earlier, Google Kubernetes Engine supports anonymous authentication by default, so we can immediately authenticate to this cluster and become authorized to perform actions that are defined in the system:public-info-viewer cluster role.

![](https://orca.security/wp-content/uploads/2024/01/image16.png?w=942)

We can see that this default role allows accessing some nonResourceURLs. We will use Postman to request two of these URLs in order to prove that we can indeed authenticate to the cluster and retrieve a successful response – without specifying any token or certificate. 

![](https://orca.security/wp-content/uploads/2024/01/image23.png?w=1118) ![](https://orca.security/wp-content/uploads/2024/01/image1.png?w=1200)

If we try to access other APIs that are associated with authenticated entities, such as system:discovery we can see that we are getting a 403 Forbidden response.

![](https://orca.security/wp-content/uploads/2024/01/image21.png?w=642) ![](https://orca.security/wp-content/uploads/2024/01/image18.png?w=1193)

#### Getting an Oauth 2.0 bearer token

Now in order to access the authenticated APIs, we need to include an access token or a certificate in the request. Since we know nothing about users and service accounts defined in this cluster, we can’t use a deterministic identity, but as we’ve learned we can always authenticate using a regular Google token and hope for the best.

An easy and fast way to obtain a Google token will be through the [OAuth 2.0 Playground](https://developers.google.com/oauthplayground/), where any registered Google account can acquire an Oauth 2.0 bearer token, authorized for a specific API scope. Among the available scopes is the ‘Kubernetes Engine API v1’.

By clicking the ‘Authorize APIs’ button and going through a standard Oauth authorization process, the playground application will deliver an authorization code that can be exchanged for an access token. 

![](https://orca.security/wp-content/uploads/2024/01/image6.png?w=450) ![](https://orca.security/wp-content/uploads/2024/01/image14.png?w=629)

If we now take this access token and use it in the request to the same cluster, we will be able to successfully authenticate as our Google account, and as a result be identified as system:authenticated. Our scope of permissions will not be entirely known, but the default discovery APIs are nearly 100% guaranteed.

Using this access token we’ve just fetched from Google playground as the ‘Authorization’ header, we can see that we are now able to access the same forbidden API from earlier, as well as other URLs.

![](https://orca.security/wp-content/uploads/2024/01/image15.png?w=1133) ![](https://orca.security/wp-content/uploads/2024/01/image22.png?w=1047)

### Compromising a Cluster

What we have shown you so far is mind boggling, but not risky. Accessing nonResourceURLs, which can be considered as metadata, can’t cause real damage to the cluster. The danger begins when Kubernetes administrators decide to authorize authenticated users with extended roles. 

Administrators might think that binding system:authenticated to a new role, to ease their managerial burden of tens or hundreds of users, is completely safe. Although this definitely makes sense at first glance, this could actually turn out to be a nightmare scenario, since system:authenticated on GKE literally includes **anyone with an internet connection**.

The system:authenticated group is innately equipped with an interesting role, system:basic-user, which grants access to objects in the authorization.k8s.io API group, an interface that can be used to determine what actions can be performed by a given user. This feature can help any authenticated user identify which permissions they have, and transparently all permissions attached to system:authenticated.

![](https://orca.security/wp-content/uploads/2024/01/image12.png?w=691)

As an example, the below screenshot demonstrates how the SelfSubjectRulesReview object – a review which returns the set of actions a user can perform within a namespace, can assist potential attackers understand what actions they can execute.

![](https://orca.security/wp-content/uploads/2024/01/image13.png?w=929)

In this case, the Kubernetes administrators decided to associate any authenticated user with the ability to read all resources across all apiGroups in the cluster. Again, something that can be somewhat useful when there is a real governance around the users which can authenticate to the cluster, but not on GKE. 

Our attacker can now, in the current settings, list all secrets in the cluster and hence achieve a real cluster compromise, acquiring all the passwords of the cluster, including service account tokens.

![](https://orca.security/wp-content/uploads/2024/01/image17.png?w=1200)

### Near-Zero Trails

By looking at the [audit logs](https://cloud.google.com/logging/docs/audit), we can find the potential malicious activity on our cluster. As an example, the event with the method name ‘io.k8s.authorization.v1.selfsubjectrulesreview.create’ is exactly the record of the POST API request we have demonstrated.

As you can see, under principalEmail – the variable representing the origin entity which executed the request, there is a 21 digit number (blurred in black), and not the actual Gmail / Google Workspace account who obtained the bearer token.

This number doesn’t change when refreshing or asking for a new token, so we can understand it is connected, one-to-one, to the Google account that has requested a token. And with some more research, it turns out this is the ‘sub’ claim in the JWT id token of the Google account which represents a human user, organization or a service.

Using this claim makes it hard to investigate the suspicious activity and keeps security teams in the dark since Google is the only one who can match this claim to the appropriate Google email address. Having a different claim for this audit log field, for instance the ‘email’ claim from JWT, would be better, but according to Google this isn’t a logging error, but a limitation caused by the fact that the token doesn’t export the ‘email’ information. 

![](https://orca.security/wp-content/uploads/2024/01/image3.png?w=1144)

### Why does GKE authenticate any Google account?

Previously, we had said that we will not discuss how IAM and Role-based access control (RBAC) interact in GKE, since it is out of the scope of this blog post. However it is necessary to go through the basics of it to understand the root cause of GKE supporting a broad OIDC authentication strategy.

In Google Kubernetes Engine, both Cloud IAM and Kubernetes RBAC are integrated to authorize users to perform actions if they have sufficient permissions at either level. This means that overall permissions for a user are additive between Cloud IAM and RBAC.

For example, a GCP user can be assigned with the IAM permission ‘container.pods.list’ in a particular project so they can list all pods on all namespaces, across all clusters on that same project. 

This is very different from AWS and Azure, where OIDC authentication is supported, but authorization is being determined only on the Kubernetes RBAC level. This intrinsic difference can help us understand the reason behind GKE’s authentication mechanics.

GCP administrators who wish to add new users to their project can do so by binding roles to their Gmail or Google Workspace account. Among these roles are IAM permissions that authorize users to perform actions on Kubernetes clusters.

So in practice, because of how GCP and other Google services are intertwined, any Google account is potentially a member of any GCP project, hence it is also a potential member of any GKE cluster. What will determine the account’s capabilities is its authorization.

## Testing this in the wild

We decided to test out how often this GKE misconfiguration is present. As a former offensive cybersecurity professional, you can rest assured the strategy presented below is far from inventing any wheel. Any basic-level hacker could have thought and executed this kind of methodology.

We wrote a short Python script that scanned for GKE clusters in a known CIDR and filtered the ones that had assigned custom roles to the system:authenticated group. Using this technique we successfully scanned over 250,000 active GKE clusters (estimated to be only 2% of the available GKE clusters) in a matter of one week, and the results confirmed our suspicions.

1,300 clusters (0.5%) were potentially vulnerable. 108 of them (8%) lead to an immediate compromise: allowing either cluster-admin access, cluster-wide listing of secrets or cluster-wide write/delete actions. Others allow read permissions over different native k8s resources, and read/all permissions over plenty of custom resources (which, depending the context, can be extremely impactful as well).

![](https://orca.security/wp-content/uploads/2024/01/image11.png?w=931) ![Cluster-Admin permissions available to anyone - we found tens of clusters like this](https://orca.security/wp-content/uploads/2024/01/image19.png?w=761)

**_Cluster-Admin_** _permissions available to anyone – we found tens of clusters like this_

![](https://orca.security/wp-content/uploads/2024/01/image4.png?w=762) ![](https://orca.security/wp-content/uploads/2024/01/image5.png?w=706) ![Listing all secrets in all namespaces of the cluster](https://orca.security/wp-content/uploads/2024/01/image2.png?w=834)

_Listing all_** _secrets_** _in all namespaces of the cluster_

![Listing all pods in the default namespace of the cluster](https://orca.security/wp-content/uploads/2024/01/image7.png?w=676)

_Listing all_** _pods_** _in the default namespace of the cluster_

![Base64 decoded secret poc: credentials to an atlassian product](https://orca.security/wp-content/uploads/2024/01/image20.png?w=788)

_Base64 decoded secret poc: credentials to an_** _atlassian_** _product_

What we’ve demonstrated above is just the tip of the iceberg. We managed to comprise several GKE clusters as “unauthorized” users. The consequences of incidents like this can range from crypto-mining campaigns to denial of service and all the way to sensitive data theft. Kubernetes connects its hosted containerized apps with various different types of critical data assets such as databases, code repositories and other 3rd-party vendors, which makes it a devastating tool at the hands of a malicious actor. 

For any [GKE clusters that we found to be vulnerable](https://orca.security/resources/blog/sys-all-google-kubernetes-engine-risk-example/) and were able to identify the owners, we immediately disclosed the vulnerability to the organization so they could remediate the risk. Also, it’s important to note that we didn’t take any steps that would actually damage these clusters. Although we always do our utmost, it isn’t always possible to identify the owners and notify them about a potential vulnerability, so we advise all organizations to follow the recommended actions described below to make sure they are not vulnerable.

## Final Notes

Despite the potential extreme consequences, Google considers this as intended behavior. We could argue against that, but on the other hand, also relate. In the end, this is an assigned permission vulnerability that can be prevented by the user. According to the [shared responsibility model](https://cloud.google.com/architecture/framework/security/shared-responsibility-shared-fate), customers are responsible for the configured access controls.

So yes, Google is indeed right. Organizations should take responsibility and not deploy their assets and permissions in a way that carries security risks and vulnerabilities. However, the scope of the system:authenticated group is a broadly misunderstood concept with acute consequences, which has been verified as [actionable and fruitful](https://orca.security/resources/blog/sys-all-google-kubernetes-engine-risk-example/). Maybe a response is still needed after all, especially in the popular era of Kubernetes.

This is not very different from the open S3 bucket [exploitation](https://www.bleepingcomputer.com/news/security/misconfigured-amazon-s3-buckets-expose-users-companies-to-stealthy-mitm-attacks/) phenomenon, which made Amazon take action – even if it took years. The only difference is that at this point, we don’t have any public record of a large-scale attack utilizing this attack vector, but this is most probably just a matter of time.

## Recommended Actions

In addition to upgrading to [GKE version 1.28](https://cloud.google.com/anthos/clusters/docs/security-bulletins#gcp-2024-003) or higher, the main way to block this attack vector is to strictly follow the [principle of least privilege](https://orca.security/platform/cloud-infrastructure-entitlement-management-ciem/). In that sense, assigning broad permissions to the system:authenticated group, whether it is deterministic or not, is a clear breach of this principle. Organizations should always aim for granularity in the

But what if you are an organization with tens or hundreds of GKE clusters managed by different teams and you have just learned of this loophole? How can you quickly find all vulnerable clusters, tighten permissions, and keep monitoring them to make sure they aren’t being misconfigured again?

This is where Orca helps. With a bird’s eye view of all your cloud assets, and an easy contextual technology to sift through the noise and highlight the important findings, defenders will immediately know which GKE clusters are vulnerable to this attack vector.

![Orca alert that notifies that a GKE cluster is vulnerable](https://orca.security/wp-content/uploads/2024/01/image10.jpg?w=1200)

_Orca alert that notifies that a GKE cluster is vulnerable_

In addition to warning about this particular GKE loophole, Orca helps organizations ensure that they configure [least privilege permissions](https://orca.security/platform/cloud-infrastructure-entitlement-management-ciem/), avoid [misconfigurations](https://orca.security/platform/cloud-security-posture-management-cspm/), and minimize the ability of an attacker to move laterally within the environment. This means that even if an attacker is able to breach the cloud environment, the actual damage they can do is very limited. 

For more information, attend our [Threat Briefing](https://www.brighttalk.com/webcast/18490/605535?bt_tok=%7B%7Blead.Id%7D%7D&utm_source=OrcaSecurity&utm_medium=brighttalk&utm_campaign=605535) where we’ll show how we discovered the GKE loophole, managed to penetrate several GKE clusters in production, and provide recommendations to further fortify your defenses.

## About Orca Security

Orca’s agentless-first [Cloud Security Platform](https://orca.security/platform/) connects to your environment in minutes and provides 100% visibility of all your assets on AWS, Azure, Google Cloud, Kubernetes, and more. Orca detects, prioritizes, and helps remediate cloud risks across every layer of your cloud estate, including vulnerabilities, malware, misconfigurations, lateral movement risk, API risks, sensitive data at risk, weak and leaked passwords, and overly permissive identities.

To find out more, schedule a [personalized demo](https://orca.security/demo/) of the Orca platform.

  * [ __](https://twitter.com/share?text=Sys%3AAll%3A%20How%20A%20Simple%20Loophole%20in%20Google%20Kubernetes%20Engine%20Puts%20Clusters%20at%20Risk%20of%20Compromise&url=https%3A%2F%2Forca.security%2Fresources%2Fblog%2Fsys-all-google-kubernetes-engine-risk%2F)
  * [ __](https://www.linkedin.com/sharing/share-offsite/?url=https%3A%2F%2Forca.security%2Fresources%2Fblog%2Fsys-all-google-kubernetes-engine-risk%2F)
  * [ __](https://www.facebook.com/sharer.php?u=https%3A%2F%2Forca.security%2Fresources%2Fblog%2Fsys-all-google-kubernetes-engine-risk%2F)
  * [ __](mailto:?Subject=Sys:All: How A Simple Loophole in Google Kubernetes Engine Puts Clusters at Risk of Compromise&body=https%3A%2F%2Forca.security%2Fresources%2Fblog%2Fsys-all-google-kubernetes-engine-risk%2F)

## Related articles

[ ![Risk-based Vulnerability Management](https://orca.security/wp-content/uploads/2025/02/orca-blog-risk-prioritization-featured.png?w=750) ](/resources/blog/risk-based-vulnerability-management/)

![](https://orca.security/wp-content/themes/orca-2023/assets/svg/featured-blue.svg) ![](https://orca.security/wp-content/themes/orca-2023/assets/svg/featured-white.svg)

Product Info

##  [Risk-Based Vulnerability Management for the Cloud: A 2026 Guide](/resources/blog/risk-based-vulnerability-management/ "Risk-Based Vulnerability Management for the Cloud: A 2026 Guide")

Jun 26, 2026 

[ ![Digital illustration of a data center cross-section showing an adversarial path indicated by glowing red arrows originating from a breached, orange-lit server rack and moving laterally toward a secured, cyan-lit server enclosure with a locked terminal.](https://orca.security/wp-content/uploads/2026/06/orca-blog-private-cloud-security-1.png?w=750) ](/resources/blog/private-cloud-security/)

![](https://orca.security/wp-content/themes/orca-2023/assets/svg/featured-blue.svg) ![](https://orca.security/wp-content/themes/orca-2023/assets/svg/featured-white.svg)

Cloud Security Learning

##  [Private Cloud Security: Top Risks and Best Practices (2026)](/resources/blog/private-cloud-security/ "Private Cloud Security: Top Risks and Best Practices \(2026\)")

Jun 26, 2026 

[ ![Digital illustration of a central AI microchip on a cloudy background, processing threats from the left—such as a cracked message bubble and a bug icon—and outputting cybersecurity solutions on the right, including prioritized alert windows and a remediation code terminal.](https://orca.security/wp-content/uploads/2026/06/orca-blog-what-is-generative-ai-in-cybersecurity-1.png?w=750) ](/resources/blog/what-is-generative-ai-in-cybersecurity/)

![](https://orca.security/wp-content/themes/orca-2023/assets/svg/featured-blue.svg) ![](https://orca.security/wp-content/themes/orca-2023/assets/svg/featured-white.svg)

Cloud Security Learning

##  [What Is Generative AI in Cybersecurity?](/resources/blog/what-is-generative-ai-in-cybersecurity/ "What Is Generative AI in Cybersecurity?")

Jun 25, 2026 

### Stay in the loop

Keep up to date with everything you need to know about cloud security and our latest research

By submitting my email address I agree to the use of my personal data in accordance with Orca Security [ Privacy Policy](https://orca.security/privacy-policy/).
