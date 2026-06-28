---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-06-19_the-unexpected-0-master-id-for-account-data-manipulation.md
original_filename: 2023-06-19_the-unexpected-0-master-id-for-account-data-manipulation.md
title: The Unexpected “0” Master ID for Account Data Manipulation
category: documents
detected_topics:
- access-control
- otp
- sso
- idor
- command-injection
- automation-abuse
tags:
- imported
- documents
- access-control
- otp
- sso
- idor
- command-injection
- automation-abuse
language: en
raw_sha256: dd74cd08ddb18834bad9a81b4a987fe8f66573b8e512e702ff66dd4c65cba041
text_sha256: 899e65747dfac6ff2e86f1f7d4bb146e03b8f97101c8dce6f5c12a8bff107fb1
ingested_at: '2026-06-28T07:32:22Z'
sensitivity: unknown
redactions_applied: false
---

# The Unexpected “0” Master ID for Account Data Manipulation

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-06-19_the-unexpected-0-master-id-for-account-data-manipulation.md
- Source Type: markdown
- Detected Topics: access-control, otp, sso, idor, command-injection, automation-abuse
- Ingested At: 2026-06-28T07:32:22Z
- Redactions Applied: False
- Raw SHA256: `dd74cd08ddb18834bad9a81b4a987fe8f66573b8e512e702ff66dd4c65cba041`
- Text SHA256: `899e65747dfac6ff2e86f1f7d4bb146e03b8f97101c8dce6f5c12a8bff107fb1`


## Content

---
title: "The Unexpected “0” Master ID for Account Data Manipulation"
page_title: "The Unexpected “0” Master ID for Account Data Manipulation – Just Another Simple Write-Up"
url: "http://www.firstsight.me/2023/06/the-unexpected-0-master-id-for-account-data-manipulation/"
final_url: "http://firstsight.me/2023/06/the-unexpected-0-master-id-for-account-data-manipulation/"
authors: ["YoKo Kho (@YokoAcc)"]
bugs: ["IDOR", "Broken Access Control"]
bounty: "2,500"
publication_date: "2023-06-19"
added_date: "2023-06-21"
source: "pentester.land/writeups.json"
original_index: 1036
---

[Bug Report](http://firstsight.me/category/bug-report/) / [Web Apps](http://firstsight.me/category/web-apps/) / [Write-Up](http://firstsight.me/category/write-up/)

# The Unexpected “0” Master ID for Account Data Manipulation

June 19, 2023 

[__]()

A simple story when Allah allowed me to successfully achieve P1 through a broken access control issue using an unexpected master ID of “0”.

**In the name of Allah, the Most Gracious, the Most Merciful.**

* * *

As usual, I will try to release this write-up with two different approaches, which are: 

  * For those who only need the main points of this finding (InshaAllah it can saves tons of minutes if readers understanding every flow already) – please kindly see the TL;DR section, and
  * For those who need to understand the flow of execution or journey about this finding. InshaAllah, it can tell the readers about some mindsets and hopefully can help people to enrich their insights.

Please kindly enjoy the story.

* * *

Note: This write-up might be quite short, considering that most of the methods executed in this writing have been explained in another writing, by the will of Allah.

### **I. TL;DR**

Here are the simple points about this issue:

  * The update feature in the application has a POST Request consisting of ID, UUID, Email, and data parameter.
  * Delete the value in the UUID parameter.
  * Fill the ID parameter with the value 0 – this value seems to act as the master value for all accounts.
  * Fill the email parameter with the target’s email.
  * Send the request to the server, and the target’s data will change according to the Attacker’s will.
  * Alhamdulillah, it was marked as P1 and rewarded with 2,500 USD.

![](http://www.firstsight.me/wp-content/uploads/2023/06/image.png)

* * *

### **II. BEHIND THE SCENE**

At one point, I received a notification regarding the addition of an in-scope target (bounty program) in the form of an API in one of the programs I was participating in. This time, the addition of the scope was quite unique because there was no provided API documentation, and there was no information available when accessing the API URL directly. 

I tried several basic approaches such as file/directory crawling, searching for information through Google Dork, Wayback Machine, and urlscan. However, I couldn’t find any positive results (no visible endpoints and no sensitive files obtained.

* * *

For those who are not familiar, here are some simple information that can explain what I mean:

  * File/directory crawling can be done using tools like [dirsearch](https://github.com/maurosoria/dirsearch), [ffuf](https://github.com/ffuf/ffuf), or others. For example, using dirsearch, we can use the common command with adding some extensions, as follows: python3 dirsearch.py -e apk,bak,conf,config,csv,doc,docx,git,ipa,jar,js,json,old,pdf,ppt,pptx,rar,sql,svn,tar,tar.gz,xls,xlsx,xml,zip -u target_url_here

  * For Google Dork, you can refer to one of my write-ups on this topic: [Information Disclosure at PayPal and Xoom (via Google Dork)](http://www.firstsight.me/2017/12/information-disclosure-at-paypal-and-xoom-paypal-acquisition-via-search-engine/)

  * For an example of using URLScan, you can check out [one of the tweet by h4x0r_dz](https://twitter.com/h4x0r_dz/status/1516209890024378371).

  * And finally, regarding the use of Wayback Machine as a tool to search for endpoints or even subdomains, you can refer to the comprehensive documentation released by [Internet Archive on their offical GitHub page](https://github.com/internetarchive/wayback/blob/master/wayback-cdx-server/README.md).

As for how to use Wayback Machine, simply we can use the following keywords: [https://web.archive.org/cdx/search/cdx?url=*.target.tld/*&output=text&fl=original](https://web.archive.org/cdx/search/cdx?url=*.target.tld/*&output=text&fl=original) to search for information about subdomains and endpoints of target.tld that have been “recorded” by the Internet Archive. If you want to search for a specific subdomain, simply replace the asterisk symbol at the beginning with the target subdomain.

* * *

In short, I immediately abandoned this target for a while (because indeed I only wanted to see it in general at that time).

* * *

### **III. VDP TARGET THAT USING API IN BOUNTY PROGRAM**

After a few months had passed, I decided to do some refreshing by revisiting one of the targets I had previously tested in their VDP program (yes, VDP, not a bounty program). When I attempted to log in and observed the traffic recorded by Burp Suite, I discovered that the application was using an API (which I had abandoned a few months ago) for the data update feature. This caught my attention because they had not integrated that API before. 

Starting from this point, I decided to test that API.

* * *

### **IV. THE JOURNEY**

#### **4.1.**Request Format****

In the data update feature of the application, I found a detailed POST Request that included the values of “id” and “uuid” that seemed to be linked to an account. To clarify, the request looked something like this:
  
  
  id=<number_here>&uuid=<uuid_here>&email=<email_here>&Parameter1=<data1_here>&Parameter2=<date2_here> and so on

As an additional note:

  * Parameter1, Parameter2, and so on – represent the “data” values associated with a user when performing an update.
  * The UUID (Universal Unique Identifier) is a long string commonly used to provide a unique “identity” to an entity within an application (not limited to applications, but for the purpose of this discussion, let’s focus on the application level).
  * One of the benefits of using uuid is usually implemented to avoid easily “guessing” the id value – thus being able to “minimize” execution regarding broken access control that “might” be in the app.
  * An example format of a UUID is: e40011c0-fa88-4e6e-8e3e-205dacc594c1 (value obtained from uuidgenerator.net – version 4).

* * *

#### **4.2.**Testing of Broken Access Control****

Based on this situation, I decided to test the application’s logic first. In summary, I created another account and performed some basic steps as I previously explained in my other writing under sub-section [“2.2.1. I have 2 Different Type of Accounts, what should I do?”](http://www.firstsight.me/2020/06/from-399-to-1650-usd-part-i-simple-vertical-privilege-escalation-by-changing-http-response/), which are:

  * Changing the ID value (without changing the UUID value) from one account to another. However, as expected, this didn’t work well because there were three identities present in the POST request: ID, UUID, and email..
  * Changing the UUID, email, and target’s ID values to be executed using the Attacker’s session. Although this implementation was complex, at that time I thought there might be an opportunity to obtain the ID and UUID values from an email in another endpoint (if the scenario was run successfully). However, this also failed because all these values were tied to the active user session.
  * Deleting both the ID and UUID values simultaneously, and leaving only the email value. However, the application did not indicate any success.
  * Changing the method from POST to GET (and conduct the previous mentioned scenario), but the application only accepted POST as the method for this data update feature.

Since none of these steps were successful, I decided to take a break for a while.

* * *

#### **4.3.**Using the “Master” ID to Modify Data of All Accounts****

Remember when I mentioned that I tried deleting the ID and UUID values in the request, but it failed? At one point, I put the value of “0” to the ID parameter (and leaving the UUID value blank). Unexpectedly, this execution successfully modified another user’s data. 

In summary, the request would appear as follows:
  
  
  id=0&uuid=&email=<email_target_here>&Parameter1=<data1_here>&Parameter2=<date2_here> and so on

In this case, the value 0 in the ID parameter seemed to act as a master ID that could be used to modify the data of all users. 

![](http://www.firstsight.me/wp-content/uploads/2023/06/image-1.png)

After discovering this, I immediately reported it, and not long after, the program owner awarded a bounty worth P1 for this find.

![](http://www.firstsight.me/wp-content/uploads/2023/06/image-2.png)

* * *

#### **4.4.**Additional Notes****

This case issue indirectly reminded me of a write-up that was published at the end of 2018, where [a bug hunter successfully executed an account takeover by using a “master code”](https://ironfisto.medium.com/tokopedia-account-takeover-bug-worth-8-million-idr-5474cb5b5cc9) with a value of 000000 in the OTP parameter.

Although almost 6 years have passed, testing models like this still seem worth it to continue.

* * *

### **V. LESSON LEARNED**

There isn’t much I can write about in this lesson learned section. Most of it has been covered in the previous write-ups. What comes to mind right now are:

  * Everything happens according to the will of Allah. Even in the situation where I tested one of the targets in the VDP that used an API registered in the in-scope bounty program.
  * There seems to be no bug that is too old to be tested. In this context, at first glance, we might think that such bugs no longer exist, but reality says otherwise – bi’idznillah. We will never know the development process that happens behind it. Maybe the developer was under time pressure and took additional steps to make it easier to execute something (unintentionally causing negative impacts), or perhaps there are other reasons.

* * *

### **VI. REFERENCES**

  * [Instagram OTP token leaked via short links](https://twitter.com/h4x0r_dz/status/1516209890024378371) – by H4x0r_DZ
  * [Wayback CDX Server API](https://github.com/internetarchive/wayback/blob/master/wayback-cdx-server/README.md) – by Internet Archive
  * [Dirsearch](https://github.com/maurosoria/dirsearch) – by Maurosoria
  * [Fuzz Faster U Fool](https://github.com/ffuf/ffuf) – by ffuf
  * [Tokopedia Account Takeover Bug Worth 8 Million IDR](https://ironfisto.medium.com/tokopedia-account-takeover-bug-worth-8-million-idr-5474cb5b5cc9) – by Mukul Lohar
  * [Online UUID Generator](https://www.uuidgenerator.net/version4)
  * Akhii [Tomi Ashari](https://twitter.com/mastomii) and Akhii [Widyanto Ardy Prabowo](https://www.linkedin.com/in/ardyprabowo)
  * [Mario Sahertian](https://twitter.com/p4c3n0g3) – He was one of the first person to introduce dirsearch (and some of how it’s used) to me.
