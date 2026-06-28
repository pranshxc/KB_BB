---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2016-05-17_when-your-privacy-disclosure-is-a-feature-not-a-bug-badoo-hotornot-failure.md
original_filename: 2016-05-17_when-your-privacy-disclosure-is-a-feature-not-a-bug-badoo-hotornot-failure.md
title: When your privacy disclosure is a “feature” not a “bug” – Badoo & HotorNot
  failure!
category: documents
detected_topics:
- sso
- command-injection
- mfa
- cors
- information-disclosure
- api-security
tags:
- imported
- documents
- sso
- command-injection
- mfa
- cors
- information-disclosure
- api-security
language: en
raw_sha256: 3f0856dbb4137727cee0de34207b84443850d4ff10e43cc21e9a0bc2ac5fda0d
text_sha256: 5f5e2675c3998cf47bd5cebab93437f30c10a71a7322ab1626da9a7e9bd22370
ingested_at: '2026-06-28T07:31:55Z'
sensitivity: unknown
redactions_applied: false
---

# When your privacy disclosure is a “feature” not a “bug” – Badoo & HotorNot failure!

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2016-05-17_when-your-privacy-disclosure-is-a-feature-not-a-bug-badoo-hotornot-failure.md
- Source Type: markdown
- Detected Topics: sso, command-injection, mfa, cors, information-disclosure, api-security
- Ingested At: 2026-06-28T07:31:55Z
- Redactions Applied: False
- Raw SHA256: `3f0856dbb4137727cee0de34207b84443850d4ff10e43cc21e9a0bc2ac5fda0d`
- Text SHA256: `5f5e2675c3998cf47bd5cebab93437f30c10a71a7322ab1626da9a7e9bd22370`


## Content

---
title: "When your privacy disclosure is a “feature” not a “bug” – Badoo & HotorNot failure!"
page_title: "When your privacy disclosure is a “feature” not a “bug” – Badoo & HotorNot failure! – Seekurity"
url: "https://www.seekurity.com/blog/general/badoo-hotornot-privacy-disclosure-feature-not-a-bug"
final_url: "https://seekurity.com/blog/2016/05/17/admin/general/badoo-hotornot-privacy-disclosure-feature-not-a-bug"
authors: ["Mohamed A. Baset"]
programs: ["Badoo", "Hot Or Not"]
bugs: ["Information disclosure"]
publication_date: "2016-05-17"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 6293
---

Your privacy on the internet is the biggest concern ever and when it comes to “Dating websites” and “Social Networks” it means more and more!

Let me tell you a story of two websites that don’t respect yours and putting it on danger…

**Introduction:**

.  
[Badoo](https://en.wikipedia.org/wiki/Badoo) is a dating-focused social networking service, founded in 2006 and headquarters in Soho, London. The site operates in 180 countries and is most popular in Latin America, Spain, Italy and France. Badoo ranks as the 281st most popular website in the world, according to Alexa Internet as of April 2014. The site operates on a freemium model. To gain extra features, a user can pay a fee or allow Badoo to email all his/her friends.

[Hot or Not](https://en.wikipedia.org/wiki/Hot_or_Not) is a rating site that allows users to rate the attractiveness of photos submitted voluntarily by others. The site offers a matchmaking engine called ‘Meet Me’ and an extended profile feature called “Hotlists”. The domain hotornot.com is currently owned by Hot Or Not Limited, and was previously owned by Avid Life Media. ‘Hot or Not’ was a significant influence on the people who went on to create the social media sites Facebook and YouTube.

.  
People are concerned about their privacy that’s why they’re using proxies, VPNs and other privacy solutions to keep themselves safe from specific attacks and surveillance issues (for the same reasons websites are using HTTPS). Using these solutions won’t keep you 100% safe when these websites/services/apps fails to protect its users from vulnerabilities that leads to malicious activities!

.

Unmasking and de-anonymizing online users is a popular techniques used by Hackers to identify their pre-targeted victims (this kind of techniques helps in online blackmailing and extortion).

.

**Technical Details:**

Badoo.com and HotOrNot.com started their own [public bug bounty program](https://en.wikipedia.org/wiki/Bug_bounty_program) on [HackerOne platform](https://hackerone.com/badoo) rewarding security researchers for responsibly reporting security/privacy bugs that would impact its users!

On Apr 13th, Seekurity team reported a bug which discloses the logged in users of Badoo.com and Hotornot.com websites but first let’s clarify why we consider this behaviour as a security issue?

When other websites have the ability to disclose your identity of a specific website/service in-theory this is a security issue! That’s why the world made a lot of effort paying attention to privacy and security and that’s clear when we hear about some browser based protection mechanisms like ([Same Origin Policy](https://en.wikipedia.org/wiki/Same-origin_policy) and [Cross-Origin Resource Sharing](https://en.wikipedia.org/wiki/Cross-origin_resource_sharing)).

.

**The bug:**

Requesting this url while you’re logged in on Badoo.com or Notornot.com “[https://eu1.badoo.com/worker-scope/chrome-service-worker.js?ws=1](https://eu1.badoo.com/worker-scope/chrome-service-worker.js?ws=1)” or “[https://hotornot.com/worker-scope/chrome-service-worker.js?ws=1](https://hotornot.com/worker-scope/chrome-service-worker.js?ws=1)” will disclose your user id, You will notice that file is dynamically rewritten and edited to reflect the currently logged in user’s ID (user_id)

![badoo user id disclose](https://seekurity.com/blog/wp-content/uploads/2016/05/Screen-Shot-2016-05-15-at-6.08.10-PM.png)

By digging more about that specific file it turned to be related to “[Chrome worker service](https://www.chromium.org/blink/serviceworker/getting-started)” and “[Chrome notifications pushing service](https://developers.google.com/web/fundamentals/getting-started/push-notifications/)“:

> A service worker is a script that is run by your browser in the background, separate from a web page, opening the door to features which don’t need a web page or user interaction. Today, they already include features like [push notifications](http://updates.html5rocks.com/2015/03/push-notificatons-on-the-open-web) and in the future it will include other things like, background sync, or geofencing. The core feature discussed in this tutorial is the ability to intercept and handle network requests, including programmatically managing a cache of responses.

But as a developer you’re free to customise the source code to match your needs, In our case it’s obvious that Badoo and HotOrNot developers did a big mistake by inserting the current user id which linked to the current user session cookie (missing best practise)!

.

**The PoC:**

An external domain can include that script url and read it’s content by calling this proof of concept code:

![](https://seekurity.com/blog/wp-content/uploads/2016/05/Screen-Shot-2016-05-15-at-6.24.04-PM.png)

We’ve created a PoC you can find it here: **[Click here to reveal your badoo.com id (you have to be logged in)](https://seekurity.com/researches/badoo/UnmaskPoC.html)**

.

.

**The Impact and attack scenario:**

Any popular website can embed the PoC code will be able to achieve one of these endless impacts:

1\. Personalized Ads targeting (rouge ads campaigns).

2\. Information/Privacy disclosure (unmasking current badoo user).

3\. Phishing/Targeted attacks (gathering a trusted information about the current user and retargeting him/her later, If the user is “blah” then BeEF OR Metasploit browser_autopwn attack).

4\. etc…

.

**Badoo privacy VS Vulnerabilities:**

> ### Does Badoo disclose my information to other parties?
> 
> We may share aggregated information with such parties as Foursquare that includes your personal information (but which doesn’t identify you directly), together with other information including log data with third parties for industry analysis and demographic profiling and to deliver targeted advertising about other products and services.
> 
> In particular, in relation to targeted advertising, we use third-party advertising companies to serve ads when you visit our Website. These companies may use information about your visits to this and other websites in order to provide advertisements about goods and services of interest to you. If you would like more information about this practice and to know your choices about not having this information used by these companies, please visit [this page](http://networkadvertising.org/managing/opt_out.asp).
> 
> If you choose to, we may share your information with vendors, service providers, and other carefully selected third parties to improve our services to you, such as by facilitating payments. We ensure these parties must adhere to strict data protection and confidentiality provisions that are consistent with this Privacy Policy.
> 
> Badoo also wishes to maintain a healthy community, and we will cooperate with all law enforcement inquiries and with all third parties to enforce their intellectual property or other rights. We may also disclose your personal information to government or law enforcement agencies, or private parties, as required by law when/or, in our sole discretion, we believe that disclosure is necessary to protect our legal rights, or those of third parties and/or to comply with a judicial proceeding, court order, or legal process served on us.
> 
> In the event that Badoo or any of its affiliates undergoes a business transition or change of ownership, such as a merger, acquisition by another company, re-organisation, or sale of all or a portion of its assets, or in the event of insolvency or administration, we may be required to disclose your personal information.

![](https://seekurity.com/blog/wp-content/uploads/2016/05/Screen-Shot-2016-05-16-at-2.26.42-AM.png)

.

Privacy Options that Badoo offers!

Although Badoo gives its user the ability to hide their online presence (ghosty accounts) but vulnerabilities still vulnerabilities!

> “At Badoo we understand protecting your [**privacy**](https://eu1.badoo.com/privacy/) is essential, so we have several settings in place to manage this.”

![](https://seekurity.com/blog/wp-content/uploads/2016/05/Screen-Shot-2016-05-16-at-2.20.32-AM.png)

![](https://seekurity.com/blog/wp-content/uploads/2016/05/Screen-Shot-2016-05-16-at-1.30.28-AM.png) ![](https://seekurity.com/blog/wp-content/uploads/2016/05/Screen-Shot-2016-05-16-at-1.31.19-AM.png)

.

**Report responses and timeline:**

Summary:

> “It’s a feature not a bug”

![](https://seekurity.com/blog/wp-content/uploads/2016/05/Screen-Shot-2016-05-16-at-3.23.30-AM.png)

The [report](https://hackerone.com/reports/130453) closed as Not Applicable then I requested the public disclosure since it’s a feature not a (bug), The irony!  
.

.  
Thanks for reading, Till the next adventure!  
.  
.  
.  
.  
**Hey!**  
Building a website? Or already built a one? Think twice before going public and let us [protect your business](https://www.seekurity.com/#pricing)!

[](https://www.addtoany.com/add_to/facebook?linkurl=https%3A%2F%2Fseekurity.com%2Fblog%2F2016%2F05%2F17%2Fadmin%2Fgeneral%2Fbadoo-hotornot-privacy-disclosure-feature-not-a-bug&linkname=When%20your%20privacy%20disclosure%20is%20a%20%E2%80%9Cfeature%E2%80%9D%20not%20a%20%E2%80%9Cbug%E2%80%9D%20%E2%80%93%20Badoo%20%26%20HotorNot%20failure%21 "Facebook")[](https://www.addtoany.com/add_to/pinterest?linkurl=https%3A%2F%2Fseekurity.com%2Fblog%2F2016%2F05%2F17%2Fadmin%2Fgeneral%2Fbadoo-hotornot-privacy-disclosure-feature-not-a-bug&linkname=When%20your%20privacy%20disclosure%20is%20a%20%E2%80%9Cfeature%E2%80%9D%20not%20a%20%E2%80%9Cbug%E2%80%9D%20%E2%80%93%20Badoo%20%26%20HotorNot%20failure%21 "Pinterest")[](https://www.addtoany.com/add_to/twitter?linkurl=https%3A%2F%2Fseekurity.com%2Fblog%2F2016%2F05%2F17%2Fadmin%2Fgeneral%2Fbadoo-hotornot-privacy-disclosure-feature-not-a-bug&linkname=When%20your%20privacy%20disclosure%20is%20a%20%E2%80%9Cfeature%E2%80%9D%20not%20a%20%E2%80%9Cbug%E2%80%9D%20%E2%80%93%20Badoo%20%26%20HotorNot%20failure%21 "Twitter")[](https://www.addtoany.com/add_to/whatsapp?linkurl=https%3A%2F%2Fseekurity.com%2Fblog%2F2016%2F05%2F17%2Fadmin%2Fgeneral%2Fbadoo-hotornot-privacy-disclosure-feature-not-a-bug&linkname=When%20your%20privacy%20disclosure%20is%20a%20%E2%80%9Cfeature%E2%80%9D%20not%20a%20%E2%80%9Cbug%E2%80%9D%20%E2%80%93%20Badoo%20%26%20HotorNot%20failure%21 "WhatsApp")[](https://www.addtoany.com/add_to/telegram?linkurl=https%3A%2F%2Fseekurity.com%2Fblog%2F2016%2F05%2F17%2Fadmin%2Fgeneral%2Fbadoo-hotornot-privacy-disclosure-feature-not-a-bug&linkname=When%20your%20privacy%20disclosure%20is%20a%20%E2%80%9Cfeature%E2%80%9D%20not%20a%20%E2%80%9Cbug%E2%80%9D%20%E2%80%93%20Badoo%20%26%20HotorNot%20failure%21 "Telegram")[](https://www.addtoany.com/add_to/linkedin?linkurl=https%3A%2F%2Fseekurity.com%2Fblog%2F2016%2F05%2F17%2Fadmin%2Fgeneral%2Fbadoo-hotornot-privacy-disclosure-feature-not-a-bug&linkname=When%20your%20privacy%20disclosure%20is%20a%20%E2%80%9Cfeature%E2%80%9D%20not%20a%20%E2%80%9Cbug%E2%80%9D%20%E2%80%93%20Badoo%20%26%20HotorNot%20failure%21 "LinkedIn")[](https://www.addtoany.com/add_to/google_gmail?linkurl=https%3A%2F%2Fseekurity.com%2Fblog%2F2016%2F05%2F17%2Fadmin%2Fgeneral%2Fbadoo-hotornot-privacy-disclosure-feature-not-a-bug&linkname=When%20your%20privacy%20disclosure%20is%20a%20%E2%80%9Cfeature%E2%80%9D%20not%20a%20%E2%80%9Cbug%E2%80%9D%20%E2%80%93%20Badoo%20%26%20HotorNot%20failure%21 "Gmail")[](https://www.addtoany.com/share)

"feature"  Badoo  Badoo.com  Bug  disclosure  failure!  HotorNot  HotorNot.com  is  not  privacy  Security  Vulnerability  When  When your privacy disclosure is a "feature" not a "bug" - Badoo.com/HotorNot.com failure!  your
