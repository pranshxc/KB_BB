---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-02-02_abusing-facebooks-call-to-action-to-launch-internal-deeplinks.md
original_filename: 2022-02-02_abusing-facebooks-call-to-action-to-launch-internal-deeplinks.md
title: Abusing Facebooks `Call To Action` To Launch Internal Deeplinks
category: documents
detected_topics:
- mobile-security
- command-injection
- path-traversal
- csrf
tags:
- imported
- documents
- mobile-security
- command-injection
- path-traversal
- csrf
language: en
raw_sha256: 060d4da0e138caaca192003e0c93327e0ce6de9d9411b4714d96e310533394d2
text_sha256: 854cae6ca696cf0eb54bbfeaf8f1ea5ce3681be9eb221c2a9e7548c3c2ac8d05
ingested_at: '2026-06-28T07:32:09Z'
sensitivity: unknown
redactions_applied: false
---

# Abusing Facebooks `Call To Action` To Launch Internal Deeplinks

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-02-02_abusing-facebooks-call-to-action-to-launch-internal-deeplinks.md
- Source Type: markdown
- Detected Topics: mobile-security, command-injection, path-traversal, csrf
- Ingested At: 2026-06-28T07:32:09Z
- Redactions Applied: False
- Raw SHA256: `060d4da0e138caaca192003e0c93327e0ce6de9d9411b4714d96e310533394d2`
- Text SHA256: `854cae6ca696cf0eb54bbfeaf8f1ea5ce3681be9eb221c2a9e7548c3c2ac8d05`


## Content

---
title: "Abusing Facebooks `Call To Action` To Launch Internal Deeplinks"
page_title: "Abusing Facebooks Call To Action to launch internal deeplinks"
url: "https://www.ash-king.co.uk/blog/abusing-Facebooks-call-to-action-to-launch-internal-deeplinks"
final_url: "https://www.ash-king.co.uk/blog/abusing-Facebooks-call-to-action-to-launch-internal-deeplinks"
authors: ["Ashley King (@AshleyKingUK)"]
programs: ["Meta / Facebook"]
bugs: ["CSRF", "Android", "iOS"]
bounty: "4,000"
publication_date: "2022-02-02"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 2946
---

# Taking over the Call to Action button on Mobile Devices

__Ashley King __02/02/2022 __Meta

![](/assets/img/blog/fbcta.png)

#### Summary

Ever noticed that big blue button on the top of every Facebook page?

This feature, known as `Call to action` or `CTA` is designed for user engagement and allows a page to redirect their visitors to a website, an app, inbox etc. The documentation for this feature can be found `[here](https://developers.facebook.com/docs/graph-api/reference/page-call-to-action)`

After a few hours of playing around with the Graph API, I found it was possible for a page admin to abuse this feature and launch Facebook's own internal deeplinks when clicked by another user.

If the `CTA` is clicked from a mobile device, a malicious payload could be executed. However, when clicked from the web, it maintains its original functionality.

The impact for this type of vulnerability is that a page admin could perform _CSRF_ / user de-anonymization attacks against its visitors who engage with the `Call to Action` button.

Lets dive straight in!

#### Reproducing the security issue

To reproduce this vulnerability we will make use of [Facebooks Graph API](https://developers.facebook.com/docs/graph-api/).

1\. Create a new Facebook page and edit the Action Button

2\. Select "Use App", provide a valid URL and click save

3\. Take note of the `Call to action` _id_ found in the POST request we just made  
**Example payload:**  
`{ "input":{ "cta_type":"OPEN_APP", "fields_data":[ { "field_key":"external_link", "field_value":"https://ash-king.co.uk" } ], **"id":"1026998747874558",** "is_for_primary_cta":true, "source":"PAGES_COVER_AREA_SURFACE", "actor_id":"212956242612150", "client_mutation_id":"2" } }`

5\. Now we can use the Graph API to include our deeplink. Visit [https://developers.facebook.com/tools/explorer/?method=POST&path=XXX&version=v12.0&android_deeplink=fbinternal%3A%2F%2Fsupersecretfbinternallink&android_destination_type=APP_DEEPLINK](https://developers.facebook.com/tools/explorer/?method=POST&path=XXX&version=v12.0&android_deeplink=fbinternal%3A%2F%2Fsupersecretfbinternallink&android_destination_type=APP_DEEPLINK) having XXX as your `CTA` id

The actor (UserA) will need these permissions: 

  * pages_manage_cta
  * pages_manage_instant_articles
  * pages_show_list
  * pages_read_engagement
  * pages_manage_metadata
  * pages_read_user_content
  * pages_manage_ads

  

![](/assets/img/blog/setting_android_deeplink_cta.png)  
  
By running the above post request, we are updating our current `CTA` object to include an android deeplink with a destination type of "APP_DEEPLINK". 

5\. You will see a response of "Success". If we were to do a Graph API call on the `CTA` object again it will now look something like this:  
  
![](/assets/img/blog/android_deeplink_cta.png)

If we were to visit this page from another user via an android device, our internal deeplink will get executed when the visitor clicks the "Use App" button. This behavior can been seen here:  

Shortly after the bug was triaged, I revisited the documentation and noticed there were fields called `iphone_deeplink` and `iphone_destination_type` against the `CTA` object. By replaying the same post request as before using the iOS keys I was also able to launch internal links on an iOS device. 

![](/assets/img/blog/CTA-iOS.png)

## Timeline - Key dates

  * 28 Oct 2021 - Reported to Meta
  * 29 Oct 2021 - Triaged
  * 24 Jan 2022 - Confirmed vulnerability has been fixed
  * 26 Jan 2022 - Bounty issued (89 days in, meaning I missed out on the 10% bonus by 1 day...)
  * 02 Feb 2022 - Blog post went live
  * 17 Feb 2022 - Blog post taken down - see below update
  * 17 Feb 2022 - Facebook investigating further
  * 13 Oct 2022 - Clean up made on all CTA objects using an internal deeplink
  * 25 Oct 2022 - Confirmed the vulnerability has been fixed
  * ~~XX XXX 2022 - Additional bounty rewarded~~
  * 14 Dec 2022 - No addtional impact found

## Response From Meta Security Team

> After reviewing this issue, we have decided to award you a bounty of $4000. Below is an explanation of the bounty amount. Meta fulfills its bounty awards through Bugcrowd and HackerOne.  
>  
>  This issue could have allowed victim's to unintentionally open internal deeplinks.

## Update 17/02/2022

There seemed to be a bit of confusion as to whether this issue was fully resolved (after bounty). Whilst no one was able to create an internal deeplink via a Graph API request, any deeplink that was already in place could still be executed on the mobile devices. This was brought to Facebooks attention on 17th February in which this blog post was taken down. 

However, Facebook had confirmed after some internal checks there was no evidence that this vulnerability had been abused.

## Update 13/10/2022

> Hi Ash,  
>  
>  Thanks again for your report. We have made a lot of progress about this issue, and after further investigation we may also have found additional impact. We are in the process of removing the previously created call to action button, this should be done shortly. However even after your call to action button with internal deeplinks are deleted please wait until we finish the additional impact investigation too, this may take longer but you may receive additional reward from it.  
>  
>  Thanks, 

## Update 14/12/2022

> Hi Ash,  
>  
>  Thanks for reporting this issue,  
>  Sorry for the delay, we have confirmed with the team, we did not find additional impact from the report, unfortunately we will not be awarding additional bounty for this report.  
>  If you wish to publish a write-up, feel free to provide us a draft version of your write-up, so we can review for accuracy, but only if you want us to do so.  
>  
>  Thanks, 

Despite being told there "may" have been additional impact here, Meta finally responded confirming that there was no additional impact. Overall I was left hanging on this report and underpaid 2.5% time bonus.
