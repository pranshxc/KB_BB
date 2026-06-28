---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-12-15_google-oauth-is-broken-sort-of.md
original_filename: 2023-12-15_google-oauth-is-broken-sort-of.md
title: Google OAuth is broken (sort of)
category: documents
detected_topics:
- oauth
- supply-chain
- sso
- saml
- command-injection
- otp
tags:
- imported
- documents
- oauth
- supply-chain
- sso
- saml
- command-injection
- otp
language: en
raw_sha256: 2637015b1b811bde6d17d55352c18cb583bd494fb0ee38ad03a62e4541c8cfff
text_sha256: 05e7e9ccba18203a83b574200e653c0d555eb8eae2c749e218f0bdc0f8621076
ingested_at: '2026-06-28T07:32:28Z'
sensitivity: unknown
redactions_applied: false
---

# Google OAuth is broken (sort of)

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-12-15_google-oauth-is-broken-sort-of.md
- Source Type: markdown
- Detected Topics: oauth, supply-chain, sso, saml, command-injection, otp
- Ingested At: 2026-06-28T07:32:28Z
- Redactions Applied: False
- Raw SHA256: `2637015b1b811bde6d17d55352c18cb583bd494fb0ee38ad03a62e4541c8cfff`
- Text SHA256: `05e7e9ccba18203a83b574200e653c0d555eb8eae2c749e218f0bdc0f8621076`


## Content

---
title: "Google OAuth is broken (sort of)"
page_title: "Google OAuth is Broken (Sort Of) ◆ Truffle Security Co."
url: "https://trufflesecurity.com/blog/google-oauth-is-broken-sort-of/"
final_url: "https://trufflesecurity.com/blog/google-oauth-is-broken-sort-of"
authors: ["Dylan Ayrey (@insecurenature)"]
programs: ["Google", "Zoom", "Slack"]
bugs: ["OAuth"]
bounty: "1,337"
publication_date: "2023-12-15"
added_date: "2024-01-02"
source: "pentester.land/writeups.json"
original_index: 622
---

[One leaked credential can silently compromise your entire SaaS stack. Find out the 6 critical risks you need to know.](https://trufflesecurity.com/library/guides/exposed-nhi-saas-worms-in-stack)

[](../)

TRUFFLEHOG

[CUSTOMERS](../customers)

COMPANY

RESOURCES

[LOG IN](https://trufflehog.org/)

[Contact Us](https://trufflesecurity.com/contact)

[One leaked credential can silently compromise your entire SaaS stack. Find out the 6 critical risks you need to know.](https://trufflesecurity.com/library/guides/exposed-nhi-saas-worms-in-stack)

[](../)

Dylan Ayrey

### [The Dig](../blog)

December 15, 2023

# Google OAuth is Broken (Sort Of)

# Google OAuth is Broken (Sort Of)

Dylan Ayrey

December 15, 2023

#### Today I’m publicizing a Google OAuth vulnerability that allows employees at companies to retain indefinite access to applications like Slack and Zoom, after they’re off-boarded and removed from their company’s Google organization. The vulnerability is easy for a non-technical audience to understand and exploit.

No changes have been pushed by Google to mitigate this risk at this time.

Here’s a timeline of events:

  * August 4th- Disclosure to Google, informed them hundreds of applications are likely affected

  * August 7th- The issue was triaged

  * October 5th- Google paid $1337 for the issue

  * November 25th- Bulk private disclosure to dozens of impacted applications (including Zoom and Slack)

  * December 16th- Public disclosure 134 days after notifying Google

## The backstory

Back in August, we [publicly disclosed](https://trufflesecurity.com/blog/discovering-a-vulnerability-in-forager-authz-hours-before-public-launch) that one of the beta testers of Truffle Security’s [Forager](https://trufflesecurity.com/blog/introducing-forager) tool had found our login was impacted by [Descope’s Microsoft OAuth vulnerability](https://www.descope.com/blog/post/noauth). At the time I remember being surprised to learn that Microsoft would send Email claims that were not created or validated by Microsoft, and that the email claim in general was not considered reliable.

This was counter-intuitive to me, because I had thought the entire purpose of OIDC was to establish reliable identity via a 3rd party like Microsoft. To illustrate this point, I went to take a screenshot of Google’s email claim, which at the time I had thought to be rock solid reliable. To my surprise, Google’s documentation in fact warned against using Email as an identifier:

  

![](https://framerusercontent.com/images/1QxQsB8mk3YBVqGDay47Dyb7is.png?width=1914&height=690)

_Google’s OIDC documentation_

  

That’s weird. Also the email-verified claim is weird too, though I have not actually found a way to generate an email claim from an unverified email. I did however find ample examples of abusing the email claim itself.

## Non-Gmail Google accounts

As it turns out, you can create Google accounts using existing email addresses, that don’t have to be Gmail. You could for example create a Google account with a Yahoo email address:

  

![](https://framerusercontent.com/images/aF4Y6OEUBga78upuFOTRhRD98nA.png?width=1018&height=886)

  

You may see where this is going, this new Google account, now has “[[email protected]](/cdn-cgi/l/email-protection)” set as its non-Gmail email, and can be used to send yahoo email claims:

  

![](https://framerusercontent.com/images/tLyqnEd9HyE6KYeSUGjAe2FUso.png?width=838&height=676)

_Yahoo OAuth_

  

The reason Google’s documentation tells you to not use email as a primary identifier, is because it’s actually possible for two different Google accounts to send the same email claim, if you edit your non-Gmail email in settings, and a new account is created with your old pre-edited email.

## Where it becomes a problem

The issue is, we can actually create Google accounts off of corporate Google organization, via email aliases, and email plus sign forwarding. In google **[[email protected]](/cdn-cgi/l/email-protection)** will be forwarded to **[[email protected]](/cdn-cgi/l/email-protection)** ‘s inbox.

This creates a window of opportunity to create a non-Gmail Google account with a plus sign email using your company’s Google organization email, that cannot be deleted or off-boarded by your organization:

  

![](https://framerusercontent.com/images/uMfXd0Eu5lxMH66JQBIjxg3x4Y.png?width=1066&height=1102)

  
This email address, will be parsed by many impacted organizations, and the domain at the end of it, will be used to decide if you can log in:

  

![](https://framerusercontent.com/images/JpLADe0pBEoALDGpgZJtgSxiKDc.png?width=1780&height=794)

_Joining Zoom with the account_

  

![](https://framerusercontent.com/images/0K8wvSxoq42MvHu4TQrsTxfRITw.png?width=1750&height=1262)

 _Joining Slack with the account_

  

Because these non-Gmail Google accounts aren’t actually a member of the Google organization, they won’t show up in any administrator settings, or user Google lists.

## The remediations

The remediations for this issue fall into 3 buckets:

  * What can Organizations do to protect themselves

  * What can service providers like Zoom and Slack do

  * What can Google do

##### ORGANIZATIONS

If you’re reading this thinking to yourself “Dang, I gotta stop disgruntled people from accessing our Slack until the end of time”, there’s good news. All you have to do is disable login with Google, and strictly enforce SAML. This actually works for most service providers, however some don’t offer this option, and you may also have some internally developed applications that are impacted and don’t support SAML.

##### SERVICE PROVIDERS

Google actually has a way for service providers to determine organization membership, sort of… One of the other OAuth claims, HD, sends you the domain of the Google organization the account is attached to. The HD claim is left off of accounts that aren’t members of Google orgs.

  

![](https://framerusercontent.com/images/KxpBOYFXiZjqoKG2Jf9SsK4iU.png?width=1450&height=900)

_The HD claim_

  

However, there is a major drawback to the HD claim: it’s just the domain, it’s not a unique identifier. This means if the Google organization gets deleted, and the domain abandoned, someone could snatch it up, and create a new Google org, and log into all your old services. Consider a case where company A gets acquired by company B, company B spins down company A’s services and does not renew its old domain. Someone on the internet could buy company A’s domain, and use it to log into company A’s old accounts.

Most of the service providers I tested did not use HD, they used the email claim.

One more remediation service providers can implement, is to not allow just-in-time account creation as a feature, generally, and to instead switch to invite only, or LDAP group only account provisioning.

##### GOOGLE

Google could take several steps to broadly fix this for everyone. One such step could be to just ban Google accounts created of existing google Organization domains. Interestingly enough, Google themselves banned google.com accounts:

  

![](https://framerusercontent.com/images/qzMQirhdWaypaRepuLcDLvroNXo.png?width=1112&height=894)

_Google protecting themselves_

  

It seems reasonable to ask them to extend the protection they affording themselves, to everyone else.  
  
Another solution they could implement, is banning plus signed Google accounts from signing up, banning Google email aliases from signing up, or just generally provide better administration settings for orgs to configure these things.

## Additional impact

One more thing I’ll call out is it is actually technically possible to get access to an organization’s Zoom and Slack given no initial access. This piggy backs off the vulnerability research others have [found in magic link sign-in flows](https://medium.com/intigriti/how-i-hacked-hundreds-of-companies-through-their-helpdesk-b7680ddc2d4c), that certain support and ticketing systems such as Zendesk, allow you to create a support ticket via email. Following this flow, you can create a Google account using a support ticket email address, potentially view the contents of the ticket to finish the account creation, and start using the support email address to Oauth into stuff. Keeping your “email to support” feature on your main domain isn’t safe, and you should consider configuring your zendesk support email with an alt email address.

## Final thoughts

Former employees retaining access to platforms like Slack and Zoom because of a loophole in Google’s OAuth system isn’t just an oversight; it’s a significant security lapse. Google has the power to push broad fixes to mitigate this, and the intent behind the public disclosure is to push them to make real changes, beyond minor cosmetic documentation changes. I appreciate Google’s promptness in triaging the issue, however following their own best practice of 90 days to remediate issues, on today, the 134th day, this issue is now public. Below is a video that goes into a few more details:

  

#### Today I’m publicizing a Google OAuth vulnerability that allows employees at companies to retain indefinite access to applications like Slack and Zoom, after they’re off-boarded and removed from their company’s Google organization. The vulnerability is easy for a non-technical audience to understand and exploit.

No changes have been pushed by Google to mitigate this risk at this time.

Here’s a timeline of events:

  * August 4th- Disclosure to Google, informed them hundreds of applications are likely affected

  * August 7th- The issue was triaged

  * October 5th- Google paid $1337 for the issue

  * November 25th- Bulk private disclosure to dozens of impacted applications (including Zoom and Slack)

  * December 16th- Public disclosure 134 days after notifying Google

## The backstory

Back in August, we [publicly disclosed](https://trufflesecurity.com/blog/discovering-a-vulnerability-in-forager-authz-hours-before-public-launch) that one of the beta testers of Truffle Security’s [Forager](https://trufflesecurity.com/blog/introducing-forager) tool had found our login was impacted by [Descope’s Microsoft OAuth vulnerability](https://www.descope.com/blog/post/noauth). At the time I remember being surprised to learn that Microsoft would send Email claims that were not created or validated by Microsoft, and that the email claim in general was not considered reliable.

This was counter-intuitive to me, because I had thought the entire purpose of OIDC was to establish reliable identity via a 3rd party like Microsoft. To illustrate this point, I went to take a screenshot of Google’s email claim, which at the time I had thought to be rock solid reliable. To my surprise, Google’s documentation in fact warned against using Email as an identifier:

  

![](https://framerusercontent.com/images/1QxQsB8mk3YBVqGDay47Dyb7is.png?width=1914&height=690)

_Google’s OIDC documentation_

  

That’s weird. Also the email-verified claim is weird too, though I have not actually found a way to generate an email claim from an unverified email. I did however find ample examples of abusing the email claim itself.

## Non-Gmail Google accounts

As it turns out, you can create Google accounts using existing email addresses, that don’t have to be Gmail. You could for example create a Google account with a Yahoo email address:

  

![](https://framerusercontent.com/images/aF4Y6OEUBga78upuFOTRhRD98nA.png?width=1018&height=886)

  

You may see where this is going, this new Google account, now has “[[email protected]](/cdn-cgi/l/email-protection)” set as its non-Gmail email, and can be used to send yahoo email claims:

  

![](https://framerusercontent.com/images/tLyqnEd9HyE6KYeSUGjAe2FUso.png?width=838&height=676)

_Yahoo OAuth_

  

The reason Google’s documentation tells you to not use email as a primary identifier, is because it’s actually possible for two different Google accounts to send the same email claim, if you edit your non-Gmail email in settings, and a new account is created with your old pre-edited email.

## Where it becomes a problem

The issue is, we can actually create Google accounts off of corporate Google organization, via email aliases, and email plus sign forwarding. In google **[[email protected]](/cdn-cgi/l/email-protection)** will be forwarded to **[[email protected]](/cdn-cgi/l/email-protection)** ‘s inbox.

This creates a window of opportunity to create a non-Gmail Google account with a plus sign email using your company’s Google organization email, that cannot be deleted or off-boarded by your organization:

  

![](https://framerusercontent.com/images/uMfXd0Eu5lxMH66JQBIjxg3x4Y.png?width=1066&height=1102)

  
This email address, will be parsed by many impacted organizations, and the domain at the end of it, will be used to decide if you can log in:

  

![](https://framerusercontent.com/images/JpLADe0pBEoALDGpgZJtgSxiKDc.png?width=1780&height=794)

_Joining Zoom with the account_

  

![](https://framerusercontent.com/images/0K8wvSxoq42MvHu4TQrsTxfRITw.png?width=1750&height=1262)

 _Joining Slack with the account_

  

Because these non-Gmail Google accounts aren’t actually a member of the Google organization, they won’t show up in any administrator settings, or user Google lists.

## The remediations

The remediations for this issue fall into 3 buckets:

  * What can Organizations do to protect themselves

  * What can service providers like Zoom and Slack do

  * What can Google do

##### ORGANIZATIONS

If you’re reading this thinking to yourself “Dang, I gotta stop disgruntled people from accessing our Slack until the end of time”, there’s good news. All you have to do is disable login with Google, and strictly enforce SAML. This actually works for most service providers, however some don’t offer this option, and you may also have some internally developed applications that are impacted and don’t support SAML.

##### SERVICE PROVIDERS

Google actually has a way for service providers to determine organization membership, sort of… One of the other OAuth claims, HD, sends you the domain of the Google organization the account is attached to. The HD claim is left off of accounts that aren’t members of Google orgs.

  

![](https://framerusercontent.com/images/KxpBOYFXiZjqoKG2Jf9SsK4iU.png?width=1450&height=900)

_The HD claim_

  

However, there is a major drawback to the HD claim: it’s just the domain, it’s not a unique identifier. This means if the Google organization gets deleted, and the domain abandoned, someone could snatch it up, and create a new Google org, and log into all your old services. Consider a case where company A gets acquired by company B, company B spins down company A’s services and does not renew its old domain. Someone on the internet could buy company A’s domain, and use it to log into company A’s old accounts.

Most of the service providers I tested did not use HD, they used the email claim.

One more remediation service providers can implement, is to not allow just-in-time account creation as a feature, generally, and to instead switch to invite only, or LDAP group only account provisioning.

##### GOOGLE

Google could take several steps to broadly fix this for everyone. One such step could be to just ban Google accounts created of existing google Organization domains. Interestingly enough, Google themselves banned google.com accounts:

  

![](https://framerusercontent.com/images/qzMQirhdWaypaRepuLcDLvroNXo.png?width=1112&height=894)

_Google protecting themselves_

  

It seems reasonable to ask them to extend the protection they affording themselves, to everyone else.  
  
Another solution they could implement, is banning plus signed Google accounts from signing up, banning Google email aliases from signing up, or just generally provide better administration settings for orgs to configure these things.

## Additional impact

One more thing I’ll call out is it is actually technically possible to get access to an organization’s Zoom and Slack given no initial access. This piggy backs off the vulnerability research others have [found in magic link sign-in flows](https://medium.com/intigriti/how-i-hacked-hundreds-of-companies-through-their-helpdesk-b7680ddc2d4c), that certain support and ticketing systems such as Zendesk, allow you to create a support ticket via email. Following this flow, you can create a Google account using a support ticket email address, potentially view the contents of the ticket to finish the account creation, and start using the support email address to Oauth into stuff. Keeping your “email to support” feature on your main domain isn’t safe, and you should consider configuring your zendesk support email with an alt email address.

## Final thoughts

Former employees retaining access to platforms like Slack and Zoom because of a loophole in Google’s OAuth system isn’t just an oversight; it’s a significant security lapse. Google has the power to push broad fixes to mitigate this, and the intent behind the public disclosure is to push them to make real changes, beyond minor cosmetic documentation changes. I appreciate Google’s promptness in triaging the issue, however following their own best practice of 90 days to remediate issues, on today, the 134th day, this issue is now public. Below is a video that goes into a few more details:

  

## [More from THE DIG](../blog)

Thoughts, research findings, reports, and more from Truffle Security Co.

[![](https://framerusercontent.com/images/gc8s3t3Vc2qmwhdmcd0kiE3Z9dw.png?width=1200&height=600)Jun 18, 2026Your PR scan is missing half the problem](./pr-scan-missing-half-the-problem)[![](https://framerusercontent.com/images/9clzmnPHl1RUTb35545Z0QjeaCo.png?width=1200&height=600)Jun 2, 2026Admin on Apache Org Exposed for 2.5 Years in Deleted PyPI Package](./admin-apache-exposed-deleted-pypi-package)[![](https://framerusercontent.com/images/WeB35OGPgqrFpsRGCxRbRHAFRZE.png?width=1200&height=600)May 22, 2026CISA's Leaked Admin GitHub Token Remained Live 2 Days After Krebs Reported It Leaked](./cisa-leaked-admin-github-token-remained-live-2-days)

# [T](../blog)he Dig

Thoughts, research findings, reports, and more from Truffle Security Co.

[![](https://framerusercontent.com/images/gc8s3t3Vc2qmwhdmcd0kiE3Z9dw.png?width=1200&height=600)Jun 18, 2026Your PR scan is missing half the problem](./pr-scan-missing-half-the-problem)[![](https://framerusercontent.com/images/9clzmnPHl1RUTb35545Z0QjeaCo.png?width=1200&height=600)Jun 2, 2026Admin on Apache Org Exposed for 2.5 Years in Deleted PyPI Package](./admin-apache-exposed-deleted-pypi-package)

STAY STRONG

DIG DEEP

[](../)

TRUFFLEHOG

[Open-source](../trufflehog)

[Enterprise](../trufflehog-enterprise)

[Analyze](../trufflehog-analyze)

[GCP Analyze](../trufflehog-gcp-analyze)

NEW!

[Forager](../trufflehog-forager)

[Security](../security)

[Integrations](../integrations)

[Pricing](../pricing)

[CUSTOMERS](../customers)

COMPANY

[About](../about)

[Careers](../careers)

[Press](../press)

[FAQ](../faq)

[Partners](../partners)

NEW!

[Contact us](../contact)

RESOURCES

[Blog](../blog)

[Newsletter](../newsletter)

[Library](../library)

[Events](../events)

[Videos](../videos)

[GitHub](https://github.com/trufflesecurity)

[Enterprise docs](https://docs.trufflesecurity.com/)

[Open-source docs](https://github.com/trufflesecurity/trufflehog#trufflehog)

[How to rotate](https://howtorotate.com/)

[Brand assets](../branding)

NEW!

DOING IT THE RIGHT WAY

[SINCE 2021](../partners)

[](https://github.com/trufflesecurity/)[](https://www.linkedin.com/company/trufflesecurity)[](https://www.youtube.com/@TruffleSecurity)[](https://twitter.com/trufflesec)

[#trufflehog-community](https://join.slack.com/t/trufflehog-community/shared_invite/zt-pw2qbi43-Aa86hkiimstfdKH9UCpPzQ)[#Secret Scanning](https://discord.gg/8Hzbrnkr7E)

© 2026 Truffle Security Co.

[Privacy policy](../privacy-policy)

[Terms and conditions](../terms-conditions)

[Data processing agreement](../data-processing-agreement)

[Acceptable use policy](../acceptable-use-policy)

STAY STRONG

DIG DEEP

[](https://github.com/trufflesecurity/)[](https://www.linkedin.com/company/trufflesecurity)[](https://www.youtube.com/@TruffleSecurity)[](https://twitter.com/trufflesec)

[#trufflehog-community](https://join.slack.com/t/trufflehog-community/shared_invite/zt-pw2qbi43-Aa86hkiimstfdKH9UCpPzQ)[#Secret Scanning](https://discord.gg/8Hzbrnkr7E)

© 2026 Truffle Security Co.

[Privacy policy](../privacy-policy)

[Terms and conditions](../terms-conditions)

[Data processing agreement](../data-processing-agreement)

[Acceptable use policy](../acceptable-use-policy)

infra
