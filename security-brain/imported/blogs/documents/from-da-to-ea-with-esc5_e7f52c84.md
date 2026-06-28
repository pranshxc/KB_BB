---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-05-17_from-da-to-ea-with-esc5.md
original_filename: 2023-05-17_from-da-to-ea-with-esc5.md
title: From DA to EA with ESC5
category: documents
detected_topics:
- access-control
- sso
- command-injection
- api-security
- cloud-security
tags:
- imported
- documents
- access-control
- sso
- command-injection
- api-security
- cloud-security
language: en
raw_sha256: e7f52c84dbf36355ccdce86a366803e47af35dcf2448f4e410269a2328eea1d2
text_sha256: 5087f9910fe0c29c1bbbe07f9359b2950af73fd0d68e519511d21425dd6c0173
ingested_at: '2026-06-28T07:32:21Z'
sensitivity: unknown
redactions_applied: false
---

# From DA to EA with ESC5

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-05-17_from-da-to-ea-with-esc5.md
- Source Type: markdown
- Detected Topics: access-control, sso, command-injection, api-security, cloud-security
- Ingested At: 2026-06-28T07:32:21Z
- Redactions Applied: False
- Raw SHA256: `e7f52c84dbf36355ccdce86a366803e47af35dcf2448f4e410269a2328eea1d2`
- Text SHA256: `5087f9910fe0c29c1bbbe07f9359b2950af73fd0d68e519511d21425dd6c0173`


## Content

---
title: "From DA to EA with ESC5"
page_title: "From DA to EA with ESC5 - SpecterOps"
url: "https://posts.specterops.io/from-da-to-ea-with-esc5-f9f045aa105c"
final_url: "https://specterops.io/blog/2023/05/16/from-da-to-ea-with-esc5/"
authors: ["Andy Robbins (@_wald0)"]
bugs: ["Active Directory Privilege Escalation", "Internal pentest"]
publication_date: "2023-05-17"
added_date: "2023-05-18"
source: "pentester.land/writeups.json"
original_index: 1147
---

[ Back to Blog  ](/blog)

[Research & Tradecraft](https://specterops.io/blog/category/research/)

# From DA to EA with ESC5

Author

[Andy Robbins](https://specterops.io/blog/author/andy-robbins/)

Read Time

9 mins

Published

May 16, 2023

##### Share

[ ](https://www.linkedin.com/shareArticle?mini=true&url=https%3A%2F%2Fspecterops.io%2Fblog%2F2023%2F05%2F16%2Ffrom-da-to-ea-with-esc5%2F&title=From+DA+to+EA+with+ESC5&source=SpecterOps) [ ](https://twitter.com/share?url=https%3A%2F%2Fspecterops.io%2Fblog%2F2023%2F05%2F16%2Ffrom-da-to-ea-with-esc5%2F&text=From+DA+to+EA+with+ESC5) [ ](mailto:?Subject=I%20thought%20you'd%20like%20this%20post:%20From DA to EA with ESC5&Body=https://specterops.io/blog/2023/05/16/from-da-to-ea-with-esc5/) [ ](https://specterops.io/blog/category/research/feed/)

There’s a new, practical way to escalate from Domain Admin to Enterprise Admin.

### ESC5

You’ve heard of ESC1 and ESC8. But what about ESC5? ESC5 is also known as “Vulnerable PKI Object Access Control”. [Will Schroeder](https://twitter.com/harmj0y) and [Lee Christensen](https://twitter.com/tifkin_)’s [whitepaper](https://specterops.io/wp-content/uploads/sites/3/2022/06/Certified_Pre-Owned.pdf) mentions three classes of objects when discussing ESC5:

  * The CA server’s AD computer object (i.e., compromise through S4U2Self or S4U2Proxy)
  * The CA server’s RPC/DCOM server
  * Any descendant AD object or container in the container(e.g., the Certificate Templates container, Certification Authorities container, theNTAuthCertificates object, the Enrollment Services Container, etc.)

I’m going to explain how the third item works and demonstrate how you can use it to jump domain trusts all the way up to Enterprise Admin.

### The ADCS LDAP Hierarchy

ADCS stores information about CAs and Certificate Templates in LDAP. You can see those objects by opening ADSI and connecting to the Configuration naming context. Then navigate down:

![](https://specterops.io/wp-content/uploads/sites/3/2023/05/1zkWpGQDTpsgUMwNz2i6b-g.png)

Configuration > Services > Public Key Services

Here’s a graph of that hierarchy, including the objects we are going to abuse:

![](https://specterops.io/wp-content/uploads/sites/3/2023/05/1EeBSsTyqNg3hI7GNoGZ-lA.png)

The “Certificate Templates” container stores templates that can be published to an ADCS CA. When you see this dialogue box, it’s literally just listing out for you the template objects that are in that container:

![](https://specterops.io/wp-content/uploads/sites/3/2023/05/1bfmWzT0NisA3wV-mQI4PkA.png)

The “Enrollment Services” container stores one pKIEnrollmentService object per CA. Those objects list the templates that have been “published” to the CA on their “certificateTemplates” property:

![](https://specterops.io/wp-content/uploads/sites/3/2023/05/1IZ85H91hcviUTaYvT6Q4mQ.png)

These are the two LDAP objects you need control of to execute ESC5 — one certificate template and the pKIEnrollmentService object. For the purposes of this blog, we are assuming the pKIEnrollmentService object is associated with a CA trusted to perform domain authentication and that it is either trusted as a root CA or chains up to a root CA.

Before I show you how to do the attack I need to lay some more foundation.

### The Curious Case of the Configuration Naming Context

The Configuration Naming Context (NC) is where Active Directory stores forest-wide configuration data that must be replicated throughout the AD forest. The Distinguished Name for the NC is CN=Configuration,DC=example,DC=local, where DC=example,DC=local is the DN of the forest root domain.

As you would imagine, if an object in Configuration is changed at the forest root, that change replicates DOWN to all domains in the forest.

But what you may not know is that the opposite is also true: if an object within Configuration changes in a child domain, that change replicates UP to the forest root. This is because every writable domain controller in the forest has a writable copy of the forest Configuration naming context.

[Jonas Bülow Knudsen](https://twitter.com/Jonas_B_K), [Martin Sohn Christensen](https://twitter.com/martinsohndk), and [Tobias Thorbjørn Munch Torp](https://www.linkedin.com/in/tobias-torp/) authored a [blog post](https://improsec.com/tech-blog/sid-filter-as-security-boundary-between-domains-part-4-bypass-sid-filtering-research) where they abused this mechanism to escalate from Domain Admin in a child domain to Enterprise Admin at the forest root by abusing GPO links to sites.

Here’s a lab where I have a forest root domain called ForestRoot.local and a child domain called ChildDomain.ForestRoot.Local:

![](https://specterops.io/wp-content/uploads/sites/3/2023/05/12b2yOiRnXAo3kWainwOkPg.png)

Look at the DN of the Public Key Services container when I connect to the child domain’s Configuration naming context, then look at the domain name for the Configuration naming context:

![](https://specterops.io/wp-content/uploads/sites/3/2023/05/191k8N_wT0mhLh5tEZqDaOg.png)

We are looking at the **domain local** copy of the **forest root** object.

Now let’s look at the security descriptor for this object:

![](https://specterops.io/wp-content/uploads/sites/3/2023/05/1OPueg_UsLvozHRl3ovhnfw.png)

As a Domain Admin in the Child domain, I have no control of this object. You can see that the button to Add an ACE here is grayed out. But you may also notice that the SYSTEM principal has full control of this object.

I’ll close MMC and re-open it, but this time using PsExec to launch MMC as the SYSTEM user:

![](https://specterops.io/wp-content/uploads/sites/3/2023/05/19UjvZueXqyaWJQ20IwygXQ.png)

I’ll again connect to the domain-local Configuration naming context, navigate to the Public Key Services container, and bring up its security descriptor:

![](https://specterops.io/wp-content/uploads/sites/3/2023/05/1LaV8S8dROZ-NXIoBy5KxXQ.png)

Now we can add ACEs. I’ll add an ACE to this object giving Bob — a user in the child domain — full control of this container:

![](https://specterops.io/wp-content/uploads/sites/3/2023/05/1r3wB3EppxqnShlT4jct7rg.png)

And now let’s look at the Public Key Services container, but this time on the forest root domain controller, connected to the forest root domain’s Configuration naming context:

![](https://specterops.io/wp-content/uploads/sites/3/2023/05/12ZuIrvLf0rxZryCevttfxA.png)

The ACE replicated up to the forest root from the child domain.

### Putting it all together

At a minimum we need the following abilities to execute ESC5 when abusing control of the PKI objects in LDAP:

  1. The ability to add new templates to the Certificate Templates container.
  2. Write access to the pKIEnrollmentService object associated with, or that chains up to a forest root CA, and associated with, or chains up to a CA trusted for NT authentication.

For this example I’m going to show you how to turn Domain Admin in the child domain into Enterprise Admin at the forest root. You saw before that as a Domain Admin in the child domain we have full control of the Public Key Services container.

We don’t have full control of the pKIEnrollmentService object, but can grant ourselves that control because that object has permissions inheritance enabled:

![](https://specterops.io/wp-content/uploads/sites/3/2023/05/1mbTa2zGS8n2gSsXh1ywxcw.png)

But the default templates have permissions inheritance disabled and we have no control of them as a Domain Admin in the child domain:

![](https://specterops.io/wp-content/uploads/sites/3/2023/05/1yjb49YvTvxruEaCKeGwMHQ.png)

Let’s look at the security descriptor for the Certificate Templates container itself:

![](https://specterops.io/wp-content/uploads/sites/3/2023/05/1uWfmBMUzlCXjaff2uQ2FBg.png)

We’ll use PsExec to launch mmc as the SYSTEM user on the child DC:

![](https://specterops.io/wp-content/uploads/sites/3/2023/05/1lXtbIS8CQ-1LIDNsS-1qow.png)

Then we will connect to the domain local Configuration naming context and navigate to the Certificate Templates container. We have full control now of this object which includes the ability to add child objects.

To exercise that privilege I will open certsrv.msc as the SYSTEM user, then duplicate an existing template:

![](https://specterops.io/wp-content/uploads/sites/3/2023/05/1j7HzsvjomuLflH9XmkT-kQ.png)

This will open the properties for our new template, where I will configure the template to enable us to execute ESC1 by:

  1. Granting enroll rights to a principal we control in the child domain.
  2. Including Client Authentication in the Application Policies.
  3. Allowing SANs in certificate requests.
  4. Not enabling manager approval or authorized signatures.

The new template is written to our local copy of the enterprise Configuration naming context, and then is replicated up to the forest root domain controller’s Configuration naming context:

![](https://specterops.io/wp-content/uploads/sites/3/2023/05/1fo_UFej1IGu16frcNZgfVA.png)

Now the template needs to be published to the CA. We can do that as the SYSTEM user on the child DC by abusing our full control of that object:

![](https://specterops.io/wp-content/uploads/sites/3/2023/05/187yrZS-BlfDcAo_aBunMEQ.png)

Certificates are “published” to a CA when they are listed on this object’s certificateTemplates property. All we have to do to “publish” the template to the CA is add the template to that list:

![](https://specterops.io/wp-content/uploads/sites/3/2023/05/1UJdjbYC78JAPs5i2jzbSAg.png)

If we pull up certsrv.msc on the forest root domain controller and inspect “Certificate Templates” for our CA, we can indeed see that this new evil template is now “published” and ready to use:

![](https://specterops.io/wp-content/uploads/sites/3/2023/05/1Dcg3w7mQhL_vtJ9uD0b1kg.png)

The stage is now fully set for us to perform ESC1 and turn DA in the child into EA at the forest root.

We use Certify to get a certificate, specifying our evil template and the enterprise admin we want to impersonate:

![](https://specterops.io/wp-content/uploads/sites/3/2023/05/1KP5IDxIrQeY66mcRNUBA0A.png) ![](https://specterops.io/wp-content/uploads/sites/3/2023/05/1Ua0KLEDkDMM2t2vpiY6d9w.png)

We transform the cert into a PFX with openssl:

![](https://specterops.io/wp-content/uploads/sites/3/2023/05/1xXN50HBbcRrXgUx3n-LJOw.png)

We put the PFX onto the child domain DC through the RDP channel, then use Rubeus to get a TGT for the enterprise admin user after demonstrating we’re not local admin on the forest root DC:

![](https://specterops.io/wp-content/uploads/sites/3/2023/05/1KsmquWisOURjeqTIzM6vZA.png)

We can prove our TGT is valid with wmic:

![](https://specterops.io/wp-content/uploads/sites/3/2023/05/18lLmrUETA5alZ8JtDJonWQ.png)

### Think in Graphs

I’m a visual person. If you’re like me, then thinking of this attack path in terms of a graph will help you understand all the moving pieces.

We start with the forest root domain and the relevant objects within its Configuration naming context. The teal node is the domain head, the orange nodes are containers, and the purple nodes are CA objects:

![](https://specterops.io/wp-content/uploads/sites/3/2023/05/1nwilvaHo0eT35a0sNH_s-w.png)

Now we add the child domain which has a two-way trust with the forest root domain:

![](https://specterops.io/wp-content/uploads/sites/3/2023/05/1roj3NbxpLibQmFxO1_9oxQ.png)

The child domain has its own domain-local copy of the forest root domain’s Configuration naming context:

![](https://specterops.io/wp-content/uploads/sites/3/2023/05/1uRa8INwfmr-dc98ALg3m-A.png)

Changes made to the domain-local objects in the child domain replicate up to their corresponding objects in the forest root domain:

![](https://specterops.io/wp-content/uploads/sites/3/2023/05/1P32XTtA_dYU-wZJ_znGg6g.png)

The SYSTEM user on the child domain’s domain controller has full control of some objects in the domain-local copy of the forest root domain’s Configuration naming context:

![](https://specterops.io/wp-content/uploads/sites/3/2023/05/1RK9kpddurgZDNxzc8LDHNw.png)

Full control of the Certificate Templates container means the ability to add new objects to that container. Any new templates added here replicate up to the forest root domain as well:

![](https://specterops.io/wp-content/uploads/sites/3/2023/05/11gNvncCmbf6tgT83_6GkXQ.png)

The CA is a root CA for the forest root domain, and the forest root domain contains its own users like the ForestRootDA user:

![](https://specterops.io/wp-content/uploads/sites/3/2023/05/18DLZuQgkWQzhJybyUL-pIg.png)

The red edges highlight the actual path taken from the child domain’s domain controller to the forest root domain admin:

![](https://specterops.io/wp-content/uploads/sites/3/2023/05/1qUH2Qfl4UYhIkLyM2xueNQ.png)

### Conclusion and Future Work

This post shows how an adversary can use ESC5 followed by ESC1 to turn DA in a child domain into EA at the forest root.

The next question I want answered: What if ADCS isn’t already deployed? Can we bootstrap the necessary LDAP objects and issuing CA to turn DA into EA if we have, for example, full control of the “Public Key Services” container but there are no CAs?

![](https://medium.com/_/stat?event=post.clientViewed&referrerSource=full_rss&postId=f9f045aa105c)

* * *

[From DA to EA with ESC5](https://posts.specterops.io/from-da-to-ea-with-esc5-f9f045aa105c) was originally published in [Posts By SpecterOps Team Members](https://posts.specterops.io) on Medium, where people are continuing the conversation by highlighting and responding to this story.

Post Views: 2,605

[ Andy Robbins ](https://specterops.io/blog/author/andy-robbins/)

Principal Security Researcher 

Andy Robbins is a Principal Security Researcher at SpecterOps. He is a co-creator of BloodHound. He specializes in Windows, Active Directory, Entra, and Azure tradecraft research and discovery.
