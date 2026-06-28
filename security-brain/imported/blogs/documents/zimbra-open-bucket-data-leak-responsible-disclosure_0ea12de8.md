---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-08-26_zimbra-open-bucket-data-leak-responsible-disclosure.md
original_filename: 2022-08-26_zimbra-open-bucket-data-leak-responsible-disclosure.md
title: Zimbra Open Bucket Data Leak – Responsible Disclosure
category: documents
detected_topics:
- cloud-security
- access-control
- command-injection
- api-security
tags:
- imported
- documents
- cloud-security
- access-control
- command-injection
- api-security
language: en
raw_sha256: 0ea12de822b4d750c687ee498047977c27a74342e65d408f51af9704ac328c7d
text_sha256: 7002307e31b030ce112a1989448ad27067f05136d8f382f84cb2b3e078abc37d
ingested_at: '2026-06-28T07:32:13Z'
sensitivity: unknown
redactions_applied: false
---

# Zimbra Open Bucket Data Leak – Responsible Disclosure

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-08-26_zimbra-open-bucket-data-leak-responsible-disclosure.md
- Source Type: markdown
- Detected Topics: cloud-security, access-control, command-injection, api-security
- Ingested At: 2026-06-28T07:32:13Z
- Redactions Applied: False
- Raw SHA256: `0ea12de822b4d750c687ee498047977c27a74342e65d408f51af9704ac328c7d`
- Text SHA256: `7002307e31b030ce112a1989448ad27067f05136d8f382f84cb2b3e078abc37d`


## Content

---
title: "Zimbra Open Bucket Data Leak – Responsible Disclosure"
page_title: "Zimbra Open Bucket Data Leak – Responsible Disclosure – BackBox.org Membership"
url: "https://members.backbox.org/zimbra-open-bucket-data-leak-responsible-disclosure/"
final_url: "https://members.backbox.org/zimbra-open-bucket-data-leak-responsible-disclosure/"
authors: ["Raffaele Forte (@raffaele_forte)"]
programs: ["Zimbra"]
bugs: ["AWS misconfiguration"]
publication_date: "2022-08-26"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 2258
---

# Zimbra Open Bucket Data Leak – Responsible Disclosure

August 26, 2022/in [Sharing Board](https://members.backbox.org/category/sharing-board/)

Authors: Raffaele Forte, BackBox Team

**# WHOIS**

Hundreds of millions use Zimbra, an all-in-one business productivity suite for micro, small, medium & enterprise in-office and remote work teams.

The Zimbra Inc company was acquired by Synacor Inc on 18 August 2015. It is based in Buffalo, New York with offices in London, Pune, Singapore and Tokyo. They deliver cloud-based software and services for leading global video, content, entertainment, internet and communications providers, device manufacturers, governments and enterprises.

**# INTRODUCTION**

In August of this year (2022), following the usual monitoring of potential data breaches and data leaks through our platform, [ADEngine](https://members.backbox.org/adengine-dark-web-monitoring-and-data-leak-detection/), we identified a severe security incident related to an exposed AWS S3 bucket belonging to Zimbra.

[![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20845%20321'%3E%3C/svg%3E)](https://members.backbox.org/wp-content/uploads/2022/08/Screenshot-2022-08-25-at-17-20-41-ADEngine-Homepage.png)

**# DESCRIPTION**

An S3 bucket is typically considered “public” if any user can list and download the content of the bucket, and “private” if the access to bucket’s content is restricted.

In this case the bucket was “public” and, due to an incorrect access configuration, it was possible for anyone to download any content without any kind of restriction.

The S3 bucket, by default, has a predictable and publicly accessible URL:

  * https://s3.amazonaws.com/files.zimbra.com/
  * https://files.zimbra.com.s3.amazonaws.com/

It is also possible to use their third level domain, reachable at the following url:

  * https://files.zimbra.com/

Zimbra uses S3 to store server backups, company documents, user logs, and publicly visible content such as web site pages, images and PDF documents.

To test the exposure of the bucket a user can just enter the URL in their web browser. A private or restricted bucket will typically respond with “Access Denied”. A public bucket instead will list the first 1,000 objects that have been stored:

**[![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20845%20321'%3E%3C/svg%3E)](https://members.backbox.org/wp-content/uploads/2022/08/Screenshot_2022-08-14_20-19-13.png)**

After having discovered the exposure of the S3 and its content, we promptly contacted Zimbra and notified their security team. After sending more than one email, about a week later, we got a response from Zimbra, thanking us for the report. Despite their response and interest, in their email they tried to minimize the issue.

Here follows a snippet of their email response:

> “My apologies for the delay in response to you. We have had to check with the team responsible for this data to understand the purpose for this bucket. I have been informed this is captured backup data for public information and therefore there is no issue with this data being publicly available.”

Surprised by the response, we again stressed the severity of the situation.

The security risk from a public bucket is simple. A list of files and the files themselves – if available for download – can reveal sensitive information. The worst case scenario is that a bucket has been marked as “public”, exposes a list of sensitive files, and no access controls have been placed on those files.

That bucket in particular contains a very rich collection of data, with many elements that seem to be private at a first glance, or that at least should not be exposed.

**[![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20845%20281'%3E%3C/svg%3E)](https://members.backbox.org/wp-content/uploads/2022/08/Screenshot_2022-08-14_19-43-03.png)**

Meanwhile it was clear that they weren’t fully aware of the content in the S3 bucket and that, apparently, their users were storing more than marketing data. Indeed, we noticed that they put some restrictions and access control in place after we’ve notified persistently and some files were no longer accessible.

The following is the snippet of the follow up email exchange and their response:

> “I have made our marketing team aware of your findings and it was confirmed to me that this was backups of public information. I believe they are removing the data as it was older backup data.”

Our analysis revealed that Zimbra’s exposed AWS S3 bucket had been publicly accessible for a very long time.

**[![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20845%20321'%3E%3C/svg%3E)](https://members.backbox.org/wp-content/uploads/2022/08/Screenshot_2022-08-25_17-18-27.png)**

In the past months, perhaps years, it has been possible to download files of different kind without any restrictions. In particular, we refer to users data such as emails, passwords, configurations, archives, system logs and much more.

**[![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20845%20321'%3E%3C/svg%3E)](https://members.backbox.org/wp-content/uploads/2022/08/Screenshot_2022-08-23_10-40-28.png)**

Today the situation seems to have partially changed, some files have been restricted (not all) but the problem persists. Zimbra team doesn’t seem to have an interest in pursuing a full fix nor do they admit or understand the severity.

In situations where the bucket is public, but the files are locked down, sensitive information can still be exposed through the file names themselves, such as the names of customers or how frequently a particular application is backed up.

[![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20845%20321'%3E%3C/svg%3E)](https://members.backbox.org/wp-content/uploads/2022/08/Screenshot_2022-08-14_19-41-49.png)

**# BUSINESS IMPACT**

We do not know if this data has been breached and exfiltrated in the past. It is not unlikely that such data is available on the darkweb or in the hands of malicious actors that may use them to carry out attacks, not only against Zimbra, but also against its users or 3rd parties, such as suppliers. The worst case scenario we can think of is that the attackers, with this information and data, may have already gained direct access to the Zimbra servers and the organization may not be aware of it.

**# CONCLUSIONS**

The purpose of this publication is to put pressure on Zimbra in order to fix the problem that is still potentially exploitable by malicious actors and, above all, to inform users of a potential and concrete threat. This is a responsible disclosure.

Zimbra should in turn guarantee loyalty and transparency to its users by informing them directly of the incident, instead of trying to deliberately underestimate the importance of what we have reported.

**# VULNERABILITY HISTORY**

Aug 14th, 2022: Vendor notification

Aug 19th, 2022: Vendor acknowledged the vulnerability

Aug 19th, 2022:: Vendor partially fixed the issue

Aug 20th, 2022: New vendor notification

Aug 26th, 2022: Article published

##### Share this entry

  * [Share on Facebook](https://www.facebook.com/sharer.php?u=https://members.backbox.org/zimbra-open-bucket-data-leak-responsible-disclosure/&t=Zimbra%20Open%20Bucket%20Data%20Leak%20%E2%80%93%20Responsible%20Disclosure)
  * [Share on X](https://twitter.com/share?text=Zimbra%20Open%20Bucket%20Data%20Leak%20%E2%80%93%20Responsible%20Disclosure&url=https://members.backbox.org/?p=1317)
  * [Share on Pinterest](https://pinterest.com/pin/create/button/?url=https%3A%2F%2Fmembers.backbox.org%2Fzimbra-open-bucket-data-leak-responsible-disclosure%2F&description=Zimbra%20Open%20Bucket%20Data%20Leak%20%E2%80%93%20Responsible%20Disclosure&media=)
  * [Share on LinkedIn](https://linkedin.com/shareArticle?mini=true&title=Zimbra%20Open%20Bucket%20Data%20Leak%20%E2%80%93%20Responsible%20Disclosure&url=https://members.backbox.org/zimbra-open-bucket-data-leak-responsible-disclosure/)
  * [Share on Tumblr](https://www.tumblr.com/share/link?url=https%3A%2F%2Fmembers.backbox.org%2Fzimbra-open-bucket-data-leak-responsible-disclosure%2F&name=Zimbra%20Open%20Bucket%20Data%20Leak%20%E2%80%93%20Responsible%20Disclosure&description=Authors%3A%20Raffaele%20Forte%2C%20BackBox%20Team)
  * [Share on Vk](https://vk.com/share.php?url=https://members.backbox.org/zimbra-open-bucket-data-leak-responsible-disclosure/)
  * [Share on Reddit](https://reddit.com/submit?url=https://members.backbox.org/zimbra-open-bucket-data-leak-responsible-disclosure/&title=Zimbra%20Open%20Bucket%20Data%20Leak%20%E2%80%93%20Responsible%20Disclosure)
  * [Share by Mail](mailto:?subject=Zimbra%20Open%20Bucket%20Data%20Leak%20%E2%80%93%20Responsible%20Disclosure&body=https://members.backbox.org/zimbra-open-bucket-data-leak-responsible-disclosure/)

https://www.backbox.org/wp-content/uploads/2018/09/website_backbox_text_black.png 0 0 admin https://www.backbox.org/wp-content/uploads/2018/09/website_backbox_text_black.png admin2022-08-26 08:40:002022-08-27 10:21:21Zimbra Open Bucket Data Leak – Responsible Disclosure
