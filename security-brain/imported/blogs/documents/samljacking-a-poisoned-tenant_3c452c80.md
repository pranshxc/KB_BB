---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-08-17_samljacking-a-poisoned-tenant.md
original_filename: 2023-08-17_samljacking-a-poisoned-tenant.md
title: SAMLjacking a poisoned tenant
category: documents
detected_topics:
- automation-abuse
- oauth
- sso
- saml
- command-injection
- password-reset
tags:
- imported
- documents
- automation-abuse
- oauth
- sso
- saml
- command-injection
- password-reset
language: en
raw_sha256: 3c452c80afbdea7232becdf292b9b7651b9e9ec87fd41bab5d5d9156f6aedbd1
text_sha256: cd2371a4bf49b97b49e7b5600c8da62e54f2ec7b0901d497427417bf130bfe49
ingested_at: '2026-06-28T07:32:25Z'
sensitivity: unknown
redactions_applied: false
---

# SAMLjacking a poisoned tenant

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-08-17_samljacking-a-poisoned-tenant.md
- Source Type: markdown
- Detected Topics: automation-abuse, oauth, sso, saml, command-injection, password-reset
- Ingested At: 2026-06-28T07:32:25Z
- Redactions Applied: False
- Raw SHA256: `3c452c80afbdea7232becdf292b9b7651b9e9ec87fd41bab5d5d9156f6aedbd1`
- Text SHA256: `cd2371a4bf49b97b49e7b5600c8da62e54f2ec7b0901d497427417bf130bfe49`


## Content

---
title: "SAMLjacking a poisoned tenant"
page_title: "SaaS Attack: How to SAMLjack a poisoned tenant"
url: "https://pushsecurity.com/blog/samljacking-a-poisoned-tenant/"
final_url: "https://pushsecurity.com/blog/samljacking-a-poisoned-tenant/"
authors: ["Luke Jennings"]
bugs: ["SAMLjacking", "SAML", "SSO", "OAuth", "Supply chain attack", "Cloud"]
publication_date: "2023-08-17"
added_date: "2023-09-05"
source: "pentester.land/writeups.json"
original_index: 850
---

## 

In this article, we’re going to demo combining two of our favorite new SaaS attack techniques to make a simple, but effective attack chain.

We published the [SaaS attack matrix](https://github.com/pushsecurity/saas-attacks) on GitHub, which is an open-source research project to demonstrate the multitude of attacks that are possible against SaaS-native and hybrid SaaS organizations. On release day it contained 38 different techniques. 

However, we know it’s not just individual attack techniques and the phases of the cyber kill chain that matter - it’s also how you chain attacks together. Two lower risk vulnerabilities chained together could be a critical issue.

In this article, we’re going to demonstrate that by combining two of our favorite new SaaS attack techniques, poisoned tenants and SAMLjacking, you can make a simple, but effective attack chain.

## What is a poisoned tenant?

[Poisoned tenants](https://github.com/pushsecurity/saas-attacks/blob/main/techniques/poisoned_tenants/description.md) involve an adversary registering a tenant for a SaaS app they control and tricking target users to join it, often using built-in invite functionality. The end goal is to have some target users actively using a tenant you (as the adversary) control.

## What the hell is SAMLjacking?

[SAMLjacking](https://github.com/pushsecurity/saas-attacks/blob/main/techniques/samljacking/description.md) is where an attacker makes use of SAML SSO configuration settings for a SaaS tenant they control in order to redirect users to a malicious link of their choosing during the authentication process. This can be highly effective for phishing as the original URL will be a legitimate SaaS URL and users are expecting to provide credentials.

## What’s the benefit of combining them?

A poisoned tenant on its own could be an epic supply chain attack if you get really lucky. Imagine discovering an organization was wanting to migrate to Slack and then catching some key teams with a Slack poisoned tenant and gradually getting the whole organization migrated over. You’d have a goldmine of information as an administrator of the platform.

However, it might be hard to trick a whole organization into using an attacker controlled slack instance without anyone realizing, but it could be a lot easier to successfully invite e.g. a marketing team into using/adopting a new marketing app that helps them do SEO. This might be easier to perform, but it doesn't really give the attacker valuable data in the poisoned tenant of the marketing app, so it seems a bit pointless.

On the other hand, what about SAMLjacking? It’s a great technique on its own, but you still need to get users to login to the app. Sure, you’ll be sending them a legitimate SaaS URL with a valid TLS certificate etc and so it’s going to pass the sniff test for many people and also bypass email security appliances and similar security tools. However, you’re still effectively phishing them for credentials, the one thing we train users to be most suspicious about, so there is still a possibility they will spot the attack. 

But what if you could combine these techniques so that a poisoned tenant didn’t need to be a big, juicy target to be useful and a SAMLjacking attack didn’t even necessarily require phishing someone directly? What if the attack could be successful just from a target accessing their own bookmarks or open tabs for an app they already use?

In a combination scenario, a user doesn't need to be phished for SAMLjacking. One day they go back to their tab and it's logged out and they get SAMLjacked while logging back in. They don't have to click a link in an email. That’s what we are talking about here, so let’s consider an example of this making use of the SaaS-based wiki, Nuclino.

## An example attack - Nuclino

Before moving on, I’d just like to point out that this isn’t a vulnerability with [Nuclino](https://www.nuclino.com/) per se and it won’t be limited to Nuclino either. I’ve used Nuclino as an example because it’s a great wiki platform we use at Push Security, so I’m familiar with it. 

It also allows custom SAML authentication, both as part of its free trial and as part of its lowest tier paid plan. This should be commended as many SaaS apps don’t support SAML or other forms of SSO, and many of those that do charge a huge premium via enterprise plans to gain access to it. We love you Nuclino, sorry!

We'll take a walkthrough of how the attack chain works now. However, if you'd like to jump straight to a demo of the attack then checkout the video here:

Next, we'll do a full walkthrough of the attack.

### Step 1 - Setup a poisoned tenant and invite target users

The first step for an adversary is to set up their poisoned tenant and then make use of the invite functionality to target some employees of the target organization. With Nuclino, you can either do this by sending sharing links directly to the target or invite them through the Nuclino app, and it will send out legit email invitations on your behalf.

![Nuclino team invite](https://images.ctfassets.net/y1cdw1ablpvd/10AKFD5hMvE2PYWZ3LaulV/f323a8614df7a1c4f65f4207a5acc6a6/image8.png)Sharing link method of inviting new users 

![Nuclino email invite](https://images.ctfassets.net/y1cdw1ablpvd/hqwOoJ3oacQLReve31WOU/ac949d7c0c440fba6e5bc382afce3e62/image3.png) Email invite method of inviting new users

![Nuclino legit email invite](https://images.ctfassets.net/y1cdw1ablpvd/2jPY0vvPllYE7A5mkZqQSc/9eb51364f71b9f4b0e1011214df7c4ac/image2.png)Example legit email a target user will receive from Nuclino when invited to join a workspace

### Step 2 - Target responds to the invitation or later signs up for Nuclino

The interesting thing here is that whether the target signs up for Nuclino directly from the joining link or they sign up for an account separately in future, they get mapped to the workspace they have been invited to by default.

![Nuclino account creation poisoned tenant](https://images.ctfassets.net/y1cdw1ablpvd/2mOASAKuRVDJBG9Kxj49gT/63cc74501f0b68a093a179fe9181b40c/image7.png)Account creation process the target user is prompted with on joining the workspace

### Step 3 - Configure a malicious SAML server

Once the adversary has a critical mass of users on their poisoned tenant, they can later engage the SAMLjacking attack. 

To do this, they need to configure a custom SAML server. You can point this to a fake authentication provider they control that mirrors the appearance of the SSO provider the target users are accustomed to using in order to capture credentials.

![Nuclino custom SAML settings](https://images.ctfassets.net/y1cdw1ablpvd/6ruhgorFea9H78bVp94Ux/558f3d93c65410580607f16048520820/image1.png)Custom SAML server settings pointing to a malicious SAML server

If you toggle the setting to require SSO, existing users will be sent emails prompting them to link their accounts to SSO. That leads to two possible paths to a user compromise.

## Paths to user compromise 

### The first possibility

This compromise occurs when the target sees the email that SSO has been configured and clicks the link in order to link their account to SSO. A smart adversary may improve the social engineering quality with an email sent out in advance informing users that the internal security team has requested Nuclino be linked to SSO. This makes the target expect the email and consider it legitimate. 

Even though the email is an official email from Nuclino and the link contained is an official Nuclino URL, it will immediately redirect to the malicious SAML server that has been configured, where credentials can then be captured.

![Nuclino legit SSO linking email](https://images.ctfassets.net/y1cdw1ablpvd/5joyiKTydkVP0754d1qlgi/5d036ae41c778f4d0f4f38bb539f91e4/image5.png)SSO linking email sent by Nuclino to existing users

### Second compromise possibility

If the user ignores the email, the other potential outcome occurs when their session expires and they need to login again to regain access. This is similar to a watering hole attack. When their session expires, the target’s open tabs or bookmarks will redirect back to the workspace specific login page, which will now look like this:

![Workspace login page post SSO configuration](https://images.ctfassets.net/y1cdw1ablpvd/1z3d7ItA95c1zDcXC4ufQa/d76037c7502ae405443c9824408f3ed2/image4.png)Workspace login page post SSO configuration

Clicking the button to login with SSO will immediately redirect to the malicious SAML server and launch the attack. Alternatively, if the target attempts to login without SSO, the login will fail with an error message telling them to login with SSO.

Either way, once the SAMLjacking has taken effect, they’ll be faced with a familiar-looking SSO login page from a trusted source at a point they are expecting to enter their credentials - something even the most paranoid of users could easily fall for unknowingly. 

![Fake Google SSO login page the target user is redirected to](https://images.ctfassets.net/y1cdw1ablpvd/OqmMgyW9UVuvu6NI31mYQ/22b2de1e4ab8d4a48a6b239ce00186dd/image6.png)Fake Google SSO login page the target user is redirected to

## Impact

At this point, having compromised multiple user’s Google credentials, an adversary has a lot of options available:

  * Access all data in Google apps like GMail, Google Drive etc

  * Access other SaaS apps that use SSO with the same Google account

  * Access other SaaS apps that use [passwordless logins](https://github.com/pushsecurity/saas-attacks/blob/main/techniques/passwordless_logins/description.md)

  * Access other SaaS apps via email [account recovery](https://github.com/pushsecurity/saas-attacks/blob/main/techniques/account_recovery/description.md)

Essentially, this can potentially lead to a compromise of every SaaS application accessible by the compromised user - all from the use of a poisoned tenant for an app with no particularly sensitive data or permissions.

### Conclusion

We have seen how two new SaaS-focused attack techniques can be combined into one more effective attack chain. This shows how a successful poisoned tenant attack for even a low risk app can still be a significant threat when combined with a SAMLjacking attack. 

This demonstrates even the least sensitive edge cases of SaaS sprawl can represent a vector to laterally move to compromise much more valuable assets. History taught us that protecting core production assets was not enough. Adversaries often achieved compromises via test systems and unsecured development resources. What we are seeing now is that this parallel exists in the SaaS-native world too. Therefore, we need to be protecting all SaaS resources with greater vigilance than their standalone sensitivity would indicate.

So what can be done about it? Well, like much in security, there is no silver bullet solution to this issue. SaaS apps are here to stay and are designed to be flexible, easy to sign up for and use. The key first step is always to get good visibility into the SaaS sprawl across your organization. If certain employees or teams start making use of a new SaaS app (or a new tenant for an existing one), that’s probably something your security team should be aware of so they can make sure it’s legitimate and being used as securely as possible.
