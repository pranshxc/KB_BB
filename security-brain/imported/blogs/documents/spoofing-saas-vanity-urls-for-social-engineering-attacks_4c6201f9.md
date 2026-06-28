---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-05-11_spoofing-saas-vanity-urls-for-social-engineering-attacks.md
original_filename: 2022-05-11_spoofing-saas-vanity-urls-for-social-engineering-attacks.md
title: Spoofing SaaS Vanity URLs for Social Engineering Attacks
category: documents
detected_topics:
- sso
- command-injection
- automation-abuse
tags:
- imported
- documents
- sso
- command-injection
- automation-abuse
language: en
raw_sha256: 4c6201f92d566059e07f6e379843b8cc89d77caf830abb54491f004582f711b0
text_sha256: bb2dffda6b9ad615f00a3322c45cebf8c6f4570238534f3255dd01a04fccac50
ingested_at: '2026-06-28T07:32:11Z'
sensitivity: unknown
redactions_applied: false
---

# Spoofing SaaS Vanity URLs for Social Engineering Attacks

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-05-11_spoofing-saas-vanity-urls-for-social-engineering-attacks.md
- Source Type: markdown
- Detected Topics: sso, command-injection, automation-abuse
- Ingested At: 2026-06-28T07:32:11Z
- Redactions Applied: False
- Raw SHA256: `4c6201f92d566059e07f6e379843b8cc89d77caf830abb54491f004582f711b0`
- Text SHA256: `bb2dffda6b9ad615f00a3322c45cebf8c6f4570238534f3255dd01a04fccac50`


## Content

---
title: "Spoofing SaaS Vanity URLs for Social Engineering Attacks"
url: "https://www.varonis.com/blog/url-spoofing"
final_url: "https://www.varonis.com/blog/url-spoofing"
authors: ["Tal Peleg"]
programs: ["Box", "Zoom", "Google"]
bugs: ["URL spoofing"]
publication_date: "2022-05-11"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 2646
---

Many SaaS applications offer what’s known as vanity URLs — customizable web addresses for landing pages, file-sharing links, etc. Vanity URLs allow you to create a personalized link that looks like this:
  
  
  **https://varonis.example.com/s/1234**

Instead of a more generic link such as this:
  
  
  **https://app.example.com/s/1234**

While vanity URLs provide a custom, easy-to-remember link, Varonis Threat Labs discovered that some applications do not validate the legitimacy of the vanity URL’s subdomain (e.g., **yourcompany**.example.com), but instead only validate the URI (e.g., **/s/1234**). As a result, threat actors can use their own SaaS accounts to generate links to malicious content (files, folders, landing pages, forms, etc.) that _appears_ to be hosted by your company’s sanctioned SaaS account. Achieving this is as easy as changing the subdomain in the link.

These spoofed URLs can be used for phishing campaigns, social engineering attacks, reputation attacks, and malware distribution.

In this article, we’ll showcase two Box link types, two Zoom link types, and two Google link types that we were able to spoof. We promptly disclosed these issues to all three vendors (see timelines below).

  * Example No. 1: Box file-sharing URLs
  * Example No. 2: Box public file-request URLs
  * Example No. 3: Zoom recording URLs
  * Example No. 4: Zoom webinar registration URLs
  * Example No. 5: Google Forms URLs
  * Example No. 6: Google Docs URLs

![](https://fast.wistia.com/embed/medias/7en1qdcac1/swatch)

## Why use vanity URLs?

Not only do vanity URLs feel more professional, but they also provide a sense of security for end-users. Most people are likelier to trust a link at **varonis.box.com** than a generic **app.box.com** link. However, if someone can spoof that subdomain, then trusting the vanity URL can backfire.

## Example No. 1: Box file-sharing URLs

Box, the popular cloud content management app, provides business-level plans which give the option to use a custom subdomain (e.g., **yourcompany**.box.com) to access and share documents. When a file in Box is shared, a generic link is created for the file, which looks like this: **app.box.com/s/ <shared link id>**.

We found that, in some cases, an attacker can prepend **any company name** to the generic URL and the link will still work. It will function just like the original link, but to the end-user, the URL in their browser will appear as **yourcompany****.app.box.com/s/ <shared link id>**, making the URL seem legitimate.

Here we added a malicious PDF to our test Box account (titled “polylablab”) and created a shared link:

![1 - Box - Banking Details](https://www.varonis.com/hs-fs/hubfs/1%20-%20Box%20-%20Banking%20Details.png?width=467&name=1%20-%20Box%20-%20Banking%20Details.png)

When we use this link in our phishing campaign, we can change the subdomain from **polylablab** to **varonis**(or any company name). Not only will the link still work, it’ll have a much greater chance of being trusted by the victim.

![2 - Box - Spoofed Banking Details](https://www.varonis.com/hs-fs/hubfs/2%20-%20Box%20-%20Spoofed%20Banking%20Details.png?width=600&name=2%20-%20Box%20-%20Spoofed%20Banking%20Details.png)

### **The risk**

A document, image, or binary file has a much higher probability of successfully infecting a user or tricking them into entering sensitive information when hosted on their own company’s “official” Box account versus being distributed through a generic file-sharing URL the user doesn’t recognize. If their company has sanctioned Box usage in the organization, **web****filters and cloud access security brokers won’t be able to block this phishing link**.

For increased deception, the attacker can also add password protection to the file to make it seem safer to the victim, or upload a custom logo and modify the color scheme in their malicious Box account to match the look and feel of the company they’re spoofing.

### **Mitigation**

Varonis Threat Labs was able to spoof Box file links with both **/s/** and **/file/** URL schemes. The Box team has applied a fix so that **/file/** URLs can no longer be spoofed at all. Box _will_ allow certain enterprise accounts to retain the ability to arbitrarily spoof **/s/** links.

A legitimate reason to allow spoofing would be a merger or acquisition. Box implemented a feature to allow for subdomain spoofing on a per Box deployment basis for shared links to remain valid, even after merging Box environments. This shrinks the risk surface of Box file-sharing abuse dramatically.

## Example No. 2: Box public file-request URLs

Box allows you to create a public form to request files and associated information from anyone, without granting them access to your Box account. For example, a healthcare organization might want to collect information from a new patient, or a manufacturing firm might want to collect CAD files from a vendor. The benefit of this is that the person submitting the information doesn’t need a Box account to access the form and upload content.

File-request links use the format **app.box.com/f/abcd1234**. Varonis Threat Labs was able to arbitrarily change the subdomain of our malicious file request form at **app.box.com** to **varonis.app.box.com** and the link still worked. Unfortunately, file-request forms cannot be branded, so their legitimacy is even more difficult to verify.

![3 - Box - File Request Form](https://www.varonis.com/hs-fs/hubfs/3%20-%20Box%20-%20File%20Request%20Form.png?width=600&name=3%20-%20Box%20-%20File%20Request%20Form.png)

### **The risk**

An attacker can easily change the URL to make it seem as if the form was generated by your company, making the victim more likely to share sensitive information. Additionally, public file-request links can be discoverable via Google (using the search operator inurl:box.com/f/), meaning that bad actors can find these file-request pages and attempt to upload malicious content or try and overflow your Box storage, causing a denial of service.

### **Mitigation**

Box has fixed this vanity URL spoofing issue, so it’s no longer possible to create your own file-request form and change the URL to an arbitrary subdomain.

Users should still be cautious about submitting sensitive information via generic Box file-request forms. To help prevent abuse, Box also includes a warning message beneath each form:

“ _Before submitting, please be sure you trust this site, have the rights to the data, and want to share this content to the owner of this file request._ ”

![](https://www.varonis.com/hs-fs/hubfs/CleanShot%202022-05-10%20at%2009-22-51@2x-png.png?width=600&name=CleanShot%202022-05-10%20at%2009-22-51@2x-png.png)

## Example No. 3: Zoom recordings

Zoom allows companies to sign up for a vanity URL, such as **yourcompany.zoom.us** to host webinar registration pages, employee login pages, meetings, recordings, and more. The feature allows the company to upload their logo and customize the color scheme as well.

![](https://www.varonis.com/hs-fs/hubfs/CleanShot%202022-05-10%20at%2009-26-15@2x-png-1.png?width=453&name=CleanShot%202022-05-10%20at%2009-26-15@2x-png-1.png)

### **The risk**

An attacker can change the URL of their own meeting recordings to your company domain to make it appear as though the content is hosted by your company. Unlike with our Box examples, this will (usually, but not always in our tests) result in a warning message, letting you know that you’re about to access external content that’s not part of your domain:

![](https://www.varonis.com/hs-fs/hubfs/CleanShot%202022-05-10%20at%2022-13-13@2x-png.png?width=601&name=CleanShot%202022-05-10%20at%2022-13-13@2x-png.png)

If the user proceeds, the external content will be branded as your own and, without proper training, remains an effective phishing technique.

Note: this works for recording URLs starting with **yourcompany.zoom.us/rec/share/** and **yourcompany.zoom.us/rec/play/**.

## ![](https://www.varonis.com/hubfs/CleanShot%202022-05-04%20at%2013-39-33@2x-png.png)Example No. 4: Zoom webinar registration URLs

For some Zoom webinars, we were able to change the registration URL to include any company’s subdomain without triggering a warning message until **after** the form was submitted. This means that a malicious webinar registration form could be used to phish your employees’ or customers’ personal information or passwords.

Here’s a webinar we created in our own Zoom account. We branded our account using Apple’s logo and changed the subdomain in the URL of the registration page from **varonis.zoom.us** to **apple.zoom.us** and it loaded our form:

![](https://www.varonis.com/hubfs/CleanShot%202022-05-04%20at%2012-19-52@2x-png.png)

When users fill in the form thinking it’s an official Apple event, we get an email with their personal info:

![](https://www.varonis.com/hubfs/CleanShot%202022-05-04%20at%2012-17-27@2x-png.png)

### **Mitigation**

Users may get a warning message when visiting a spoofed Zoom URL. However, since users often click through non-critical warning messages, Varonis Threat Labs recommends being cautious when accessing branded Zoom links and avoid entering sensitive personal information into meeting registration forms, even if the form appears to be hosted by your company on an official subdomain with the correct logo and branding.

## Example No. 5: Google Forms

Even web apps that do not have a vanity URL feature can be abused. For example, a Google Form requesting sensitive confidential data could be branded with your company’s logo and distributed to customers or employees as **yourcompanydomain.docs.google.com/forms/d/e/:form_id/viewform** to make it seem as though it came from your company. The form could require registering with an email from your company domain, making it seem more trustworthy to your employees.

This Google Form was not created by Salesforce, yet we’re able to arbitrarily prepend their subdomain.

![](https://www.varonis.com/hubfs/CleanShot%202022-05-10%20at%2010-04-41@2x-png.png)

## Example No. 6: Google Docs

Similarly, any Google Doc that is shared via the “publish to web” option can be spoofed.

![](https://www.varonis.com/hubfs/CleanShot%202022-05-03%20at%2014-22-02@2x-png.png)

Google Docs shared via this feature will have a **docs.google.com/document/d/e/:doc_id/pub** format and can be spoofed by prepending an arbitrary subdomain.

![](https://www.varonis.com/hubfs/CleanShot%202022-05-03%20at%2014-25-15@2x-png.png)

Google has approved and triaged this bug (see timeline below).

## **Summary**

SaaS vanity URLs are a great feature that provide customers with a more custom experience and, when implemented securely, can help protect users from phishing attempts. However, as we have shown, these URLs can be spoofed and should be treated with suspicion just like any other URL.

Vanity URLs exist in many SaaS applications and are not limited to just Box and Zoom. We recommend educating your coworkers about the risk associated with clicking on such links and especially submitting PII and other sensitive information via forms, even if they appear to be hosted by your company’s sanctioned SaaS accounts.

### **Disclosure timelines**

**Box:**

  * September 23, 2021 – First disclosure
  * September 25, 2021 – First response from HackerOne
  * October 1, 2021 – Bug triaged
  * October 5, 2021 – First response from Box requesting more information
  * October 11, 2021 – Varonis provides more information and video demos
  * February 8, 2022 – Box updates about fixes
  * April 22, 2022 – Box confirms all issues have been resolved

**Current state:** all bugs are fixed.

**Zoom:**

  * September 23, 2021 – First disclosure
  * September 23, 2021 – First non-automated response from Zoom
  * October 19, 2021 – Zoom confirms issues passed to engineering
  * November 4, 2021 – Zoom rewards bounty
  * March 3, 2022 – Zoom reports the issue fixed
  * March 23, 2022 – We notified Zoom we are still able to partially demonstrate the issue
  * May 9, 2022 – Zoom confirms current state considered works-as-designed

**Current state:** can still spoof but user will get a warning.

**Google:**

  * November 1, 2021 – First disclosure
  * November 1, 2021 – First non-automated response from Google
  * November 3, 2021 – Google approves the bug
  * November 23, 2021 – Google rewards bounty

**Current state** : bugs still exist for Google Forms and Google Docs that use the “publish to web” feature.

### What should I do now?

Below are three ways you can continue your journey to reduce data risk at your company:

1

[Schedule a demo with us](https://info.varonis.com/en/demo-request?hsLang=en "https://info.varonis.com/en/demo-request") to see Varonis in action. We'll personalize the session to your org's data security needs and answer any questions.

2

[See a sample of our Data Risk Assessment](https://www.varonis.com/hubfs/docs/DRA-sample.pdf?hsLang=en "https://info.varonis.com/hubfs/docs/DRA-sample.pdf?hsLang=en") and learn the risks that could be lingering in your environment. [Varonis' DRA](https://info.varonis.com/en/data-risk-assessment?hsLang=en "https://info.varonis.com/en/data-risk-assessment") is completely free and offers a clear path to automated remediation.

3

Follow us on[ LinkedIn](https://www.linkedin.com/company/varonis "https://www.linkedin.com/company/varonis"), [YouTube](https://www.youtube.com/channel/UCE9xUuH4lhIUDOFR1OHlNNg "https://www.youtube.com/channel/UCE9xUuH4lhIUDOFR1OHlNNg"), and [X (Twitter)](https://twitter.com/varonis "https://twitter.com/varonis") for bite-sized insights on all things data security, including DSPM, threat detection, AI security, and more.

![Tal Peleg](https://www.varonis.com/hubfs/tal-peleg.jpg)

Tal Peleg Tal Peleg is a senior security researcher at Varonis. Also known as TLP, Tal is a full-stack hacker with experience in malware analysis, Windows domains, web servers, and cloud. His research is currently focused on cloud applications and APIs.
