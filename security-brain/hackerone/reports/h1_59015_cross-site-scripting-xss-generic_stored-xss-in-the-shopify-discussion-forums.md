---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '59015'
original_report_id: '59015'
title: Stored XSS in the Shopify Discussion Forums
weakness: Cross-site Scripting (XSS) - Generic
team_handle: shopify
created_at: '2015-04-29T19:48:20.965Z'
disclosed_at: '2015-05-31T14:54:43.895Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 4
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# Stored XSS in the Shopify Discussion Forums

## Metadata

- HackerOne Report ID: 59015
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: shopify
- Disclosed At: 2015-05-31T14:54:43.895Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hi Shopify Security Team,
There is Stored XSS in the Shopify Discussion Forums.Under ecommerce.shopify.com, in  shopify-discussion The STORED XSS is present.
The Stored XSS can easily be produced Every time.
To Produce the XSS Vulnerability, I created a New Topic Under the shopify-discussions in the Forums.I entered this XSS PAYLOAD in TITLE
"><img src=x onerror=prompt(1)>
 
Now I entered demo content in the Message box,and clicked on create the topic, then topic has been created. It shows Our topic and below that shows two options
 EDIT POST and ATTACH IMAGE.
From this attach image option i attached the image  and uploaded to the topic.
When i clicked the Image to enlarge it the STORED XSS executed itself and pop up was generated.

Here are steps to Reproduce the Stored XSS Bug:
Enter the shopify-discussion under the Shopify Discussion Forums and create a new topic.
In title add xss payload: "><img src=x onerror=prompt(1)> and  in the message box and any demo content, and create the topic.
After the topic has been created it shows the two options EDIT POST and Attach image, upload any from the this options.
Now after the upload click the image to enlarge image,the XSS payload in the title will be executed.


Please find attached the Proof of Concept, i am attaching the screenshots.

Thank u
Regards,
Sukhjiwan Singh

## Extracted Security Notes

### Likely Vulnerability Class

*Leave this section for future enrichment.*

### Likely Root Cause

*Leave this section for future enrichment.*

### Potential Impact

*Leave this section for future enrichment.*

### Defensive Test Cases

*Leave this section for future enrichment.*

### Remediation Ideas

*Leave this section for future enrichment.*
