---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-11-15_optimizing-hunting-results-in-vdp-for-use-in-bug-bounty-programs-from-sensitive-.md
original_filename: 2020-11-15_optimizing-hunting-results-in-vdp-for-use-in-bug-bounty-programs-from-sensitive-.md
title: Optimizing Hunting Results in VDP for use in Bug Bounty Programs - From Sensitive
  Information Disclosure to Accessing Hidden APIs which can be used to Retrieve Customer
  Data
category: documents
detected_topics:
- rate-limit
- idor
- access-control
- api-security
- sso
- ssrf
tags:
- imported
- documents
- rate-limit
- idor
- access-control
- api-security
- sso
- ssrf
language: en
raw_sha256: b7f3a52f3ab2fe261f488fefe5207768fd3e113c4c9e0183a8e243546dbb0dee
text_sha256: bf86ed937c25381a4c20ffe8cf0b0b0437fe12a1bf5cc6d8450a5179efee85b2
ingested_at: '2026-06-28T07:32:03Z'
sensitivity: unknown
redactions_applied: false
---

# Optimizing Hunting Results in VDP for use in Bug Bounty Programs - From Sensitive Information Disclosure to Accessing Hidden APIs which can be used to Retrieve Customer Data

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-11-15_optimizing-hunting-results-in-vdp-for-use-in-bug-bounty-programs-from-sensitive-.md
- Source Type: markdown
- Detected Topics: rate-limit, idor, access-control, api-security, sso, ssrf
- Ingested At: 2026-06-28T07:32:03Z
- Redactions Applied: False
- Raw SHA256: `b7f3a52f3ab2fe261f488fefe5207768fd3e113c4c9e0183a8e243546dbb0dee`
- Text SHA256: `bf86ed937c25381a4c20ffe8cf0b0b0437fe12a1bf5cc6d8450a5179efee85b2`


## Content

---
title: "Optimizing Hunting Results in VDP for use in Bug Bounty Programs - From Sensitive Information Disclosure to Accessing Hidden APIs which can be used to Retrieve Customer Data"
page_title: "Optimizing Hunting Results in VDP for use in Bug Bounty Programs  -  From Sensitive Information Disclosure to Accessing Hidden APIs which can be used to Retrieve Customer Data – Just Another Simple Write-Up"
url: "http://www.firstsight.me/2020/11/optimizing-hunting-results-in-vdp-for-use-in-bug-bounty-programs-from-sensitive-information-disclosure-to-accessing-hidden-apis-which-can-be-used-to-retrieve-customer-data/"
final_url: "http://firstsight.me/2020/11/optimizing-hunting-results-in-vdp-for-use-in-bug-bounty-programs-from-sensitive-information-disclosure-to-accessing-hidden-apis-which-can-be-used-to-retrieve-customer-data/"
authors: ["YoKo Kho (@YokoAcc)"]
bugs: ["Information disclosure", "Broken Access Control", "IDOR", "SQL injection"]
bounty: "4,750"
publication_date: "2020-11-15"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4129
---

[Bug Report](http://firstsight.me/category/bug-report/) / [Web Apps](http://firstsight.me/category/web-apps/) / [Write-Up](http://firstsight.me/category/write-up/)

# Optimizing Hunting Results in VDP for use in Bug Bounty Programs - From Sensitive Information Disclosure to Accessing Hidden APIs which can be used to Retrieve Customer Data

November 15, 2020 

[__]()

A story when Allah willed me to tried to optimize my findings in the Points-Only program to be able to get 6 paid P1 issues in the bounty program.

**In the name of Allah, the Most Gracious, the Most Merciful.**

* * *

As usual, I will try to release this write-up with two different approaches, which are:

  * For those who only need the main points of this finding (InshaAllah it can saves tons of minutes if readers understanding every flow already) — please kindly see the TL;DR section, and
  * For those who need to understand the flow of execution or journey about this finding. InshaAllah, it can tell the readers about some mindsets and hopefully can help people to enrich their insights.

**Please kindly note:** this write-up will probably be quite a long write-up. Because in addition to trying to tell readers about where I started getting positive results from this activity, I also tried to link it with one of write-up I had previously released. InshaAllah, I will try to continue to improve this write-up (because **I find it a bit difficult to collect stories with a certain time**). There is a possibility if I might miss something.

Apart from that difficult things, enjoy the story.

**Note:** by the way, not many screenshots here. I hope you are not sleepy when you read it. But again, enjoy the story.

* * *

### **I. TL;DR**

Let’s just say the main target discussed in this ticket is **mainredacted.target.tld** (bounty program). So, here are simple points on the matter:

  * Unprotected Jira issue was discovered in **May 2018** at **sub1**.target.tld (points-only program) — allowed me to obtain various information (in the form of discussion and screenshots) consisting of email address (including credentials) and multiple endpoints. I keep all of this hunting results.
  * Found simple user enumeration issue in **August 2019** on **sub2**.target.tld (bounty program, but not mainredacted.target.tld) — I saved every email address that was enumerated.
  * Found multiple SQL Injection issue in **August 2019** at **sub3**.target.tld (points-only program) — allowed me to enumerate all registered email addresses (and yes, I saved these results).
  * Found a simple IDOR in **August 2019** at **sub4**.target.tld (points-only program) — allowed me to access their administrator dashboard and got a huge list of registered email addresses. Again, I saved these results too.
  * Found Broken Access Control issue in **October 2019** on mainredacted.target.tld using information I got from May 2018 (Unprotected Jira Application). Got 1 Paid P1 (2,250 USD).
  * In **December 2019** , I found sensitive information disclosure via debug mode which is still active in targetXYZ.tld (points-only program — this asset belongs to the target.tld). I managed to log into their administrator dashboard and downloaded a csv file which contains quite a list of email addresses from their internal employees. Yes, I also saved this result.

**Note:** I keep all hunting results for some consideration, namely because InshaAllah it will be useful one day, and because there is no provision to delete the test results (as is generally done in formal PenTest jobs).

  * In **December 2019 to January 2020** , I also found 4 paid P1 issues (at mainredacted.target.tld) which have been mostly explained in my other articles [“From Recon to Optimizing RCE Results”](https://medium.com/bugbountywriteup/from-recon-to-optimizing-rce-results-simple-story-with-one-of-the-biggest-ict-company-in-the-ea710bca487a). (total of this 4 paid P1s is 9,000 USD).
  * In **January 2020** , I found an issue similar to the previous 4 Paid P1 at mainredacted.target.tld, but I found it in their **development area** (decided as points-only program). At that time, I accidentally took a screenshot of the HTTP Request from the API in use (and this API will come in handy when I return to hunting on this target in September 2020).
  * In **September 2020** , I chained several issues from weak login implementation, weak credentials (because I got their pattern from the activity in December 2019 to January 2020), using hidden API, and rate limit issue. This got me into another paid P1 issue (2,500 USD).

Here is the general “timeframe” about this:

![](https://cdn-images-1.medium.com/max/1600/1*JAtTgAdbn_XR2KcxrZlZhw.png)Simple “Timeframe”

No exciting new techniques here. The only thing I do is gather one piece of information with another and try to use it on the in-scope (bounty) target.

* * *

### **II. LITTLE FLASHBACK**

#### **2.1. The story begins with the report I submitted in May 2018**

At that time, I was refreshing to find bugs in a (points-only) program because of its wide coverage. In short, I found a subdomain with the name “Jira” (and yes, a Jira App) that doesn’t require authentication in order to see enough tickets on it. Although at first glance it looks interesting, unfortunately most of these tickets were made by the end of 2016 (it seems that the latest tickets have been made in a mode that the public cannot see).

Of course, reporting findings like this would not be sufficient to increase the impact. Therefore, I tried to look at some ticket content that has a specific keyword (such as password, admin, root, email, database, etc.) in hopes that I can show the impact further.

After looking for a while, I finally found some interesting things, such as:

  * Few credentials (username and password) to log in to one of the portals,
  * Few screenshots showing the endpoint along with a little customer data, and
  * The endpoint information which cannot be accessed because it might only be for internal access or is no longer valid because the tickets were made at the end of 2016 (and I opened the ticket in 2018).

After submission, a few days later the program owner considers this issue valid and assigns P2 for this finding and stated that it was fixed 5 months later.

![](https://cdn-images-1.medium.com/max/1600/1*notKblBLnWrbfnrtazID4A.png)P2 for Unprotected Jira Application

**A short note:**

  * I tried to log into several accounts I found, but at that time I haven’t seen any good thing from using this account any further (I didn’t spend much time analyzing it because at that time I was just looking for bugs in order to refresh). So maybe this is the reason they decided the severity was P2.

**Note:** but when I reanalyzed this finding (1 year 5 months later — October 2019), Alhamdulillah, I finally found my first paid P1 in this program. And this continued until Allah willed me to get another 5 paid P1s between December 2019 and September 2020.

  * Remember one of my writings, InshaAllah, programs like this (legal and has a wide scope — although points only) can help us to learn many things so that they can help us in our hunting activities.
  * I keep all hunting results for some consideration, namely because InshaAllah it will be useful one day, and because there is no provision to delete the test results (as is generally done in formal PenTest jobs).

* * *

#### **2.2. Story reopened in October 2019**

On one occasion from August 2019 to September 2019, I was focusing on one of their subdomains that was in their bounty program (let’s call sub2.target.tld — I have written a write-up about this, but I deleted it few months later because it really messed up) and few subdomains that was in their points only program. After achieving results that I thought were good enough for that target (and I don’t have any more ideas about what I can do with this target), I tried to turn my attention to their other assets (let’s call **mainredacted.target.tld**) in October 2019 (which I finally realized if this asset was connected to one of their SSO service).

**So, what do I do to get started?**

One of the things I did to get started was to go back to seeing the results of my hunting in May 2018 (related to the information I got from Jira’s results). The reason is quite simple, namely because the subdomain I was aiming to at that time seemed familiar to me and because I believe I haven’t optimized my tests on this subdomain before.

* * *

#### **2.2.1. Take a Look (again) at the Credentials and Endpoints that have been Obtained**

After decided to look at the information I got from (some) tickets on their Jira, I started learning the credential and endpoints mapping I had created.

![](https://cdn-images-1.medium.com/max/1600/1*b4i09H-D9pQAwfBeyO9whA.png)Simple Mapping

**Unfortunately** , out of the 5 credentials I got (excluding FTP), only one valid credential is left (and it’s not using their official domain — more like a normal user email). But of course, it’s better than nothing, right?

After trying to play for a while with this account, I finally found that this account is connected to their SSO service. More or less the situation is like this:

![](https://cdn-images-1.medium.com/max/1600/1*LwXBlckb9DBM6LIq7yvbcg.png)Site Illustration

The picture above is just a simple illustration to make it easier to understand the situation. I personally don’t really remember how many subdomains are linked into this asset. When I found that there was a subdomain that was out-of-scope (bounty program), I passed it — because I tend to focus on targets that are in the scope of the bounty program.

After trying to visit every menu and every subdomain, I finally came across a subdomain that had a menu labeled “Internal Resources” in it (**mainredacted.target.tld**). From this situation, I tried to compare it with the account I have.

**A short note:**

  * The finding regarding the “internal resources” menu is interesting, considering the account I use is an account that looks like a normal user (because it doesn’t use an official domain). It’s like we create our own account and then this account is given the privilege to access that menu.
  * This application allows users to register and use some common features contained in it.

* * *

#### **2.2.2. Comparison between Access the Site with “Internal” and External Account (Special Privilege)**

When I first saw the menu labeled “Internal Resources”, I was quite surprised. Because as I have said, this account does not use an official email address from the target. So, I started to assume several things, namely:

  * Maybe this is a menu intended for all registered users on it (but this is almost impossible, because it is clear to me that they are using the word “internal”)
  * Maybe this menu accidentally appeared due to an error from their internal development, or
  * Maybe one of the internal users of this application has registered their personal email address to be able to get that “special” access.

But regardless of the reason, to make sure that it is not intended for the public, I tried to compare it with my personal account. In short, it turned out that one of my assumptions was correct, the internal users had registered his/her personal email addresses to be able to access this “Internal Resources” menu.

Initially I was quite happy to find this. Not long after, I tried to discuss with the program owner about this thing and got the decision that this did not qualify for the bounty (issues like this qualify for points only). Yes, the information in this menu is less dangerous even though it is intended for internal use (and after I opened it one by one, there were no signs of documents showing sensitive matters such as user data or the like. This is like a general operational manual document intended for internal use). They acknowledged that, but not for their bounty program.

* * *

#### **2.2.3. Take a Look (again) at the Screenshots that have been Obtained: An Endpoint to Retrieve Customer Data.**

**Did I stop?** No. Remember, I still have the 3rd thing besides the credentials and endpoint information, which is the screenshot I saved of some of the tickets in their Jira. From about 16 screenshots that I have saved, there is one screenshot that really catches my attention, which is a subdomain — **mainredacted.target.tld** (which I am focusing on) with an endpoint containing customer data.

More or less, the screenshot looks like this:

![](https://cdn-images-1.medium.com/max/1600/1*zFIxucuUlvlLHZAt7WVXXw.png)Feature Illustration

After making a simple comparison between the account I have with the one I found on Jira, it turns out that my account does not have an “interesting feature” that displays a “commercial accounts” column. Simply put, accounts that have access to this internal resource also have access to this interesting feature.

**So, what’s next?** From here, I tried to enter the email address that I found in the screenshot, and it turned out that I was able to retrieve customer data from the company’s email address.

A little note, the execution of this interesting feature will generate a request to the endpoint via the API.

**What else?** If I encounter such a situation, then there are several things that can be done, namely:

  * Of course, trying to inject the email column (SQL Injection, XSS, and other similar injection). But unfortunately, this is not going well because they have a WAF which blocks the various injections I do (it could be because I don’t have a good ability to bypass this WAF).
  * Rate limit issue to help us get customer data. Unfortunately, this also didn’t go well. I don’t have much data to use other than the data I got from their Jira ticket. (at that time I didn’t think about the hunting results I got in August 2019).
  * And another thing that can be done is, try to access this interesting feature with a general account that we have, or even without an account at all. And yes, this scenario works really well. We can access it without authentication!

**Short lesson:**

  * From here we can learn one valuable thing, that is we need to know the application well so that InshaAllah we can test it more optimally. In 2018, since I only intended to do a simple refresher, I didn’t try to look further into this which ended up making me to miss quite a lot.

But there is another good thing from this is, in 2019 they increased their reward range, so I also managed to get a reward that was much better. There is always a good lesson in everything. Alhamdulillah.

  * As you can see (from section #2.2.1), I only have 1 account left which is still valid to use. However, even if there is only 1 account left, don’t despair. Because this account, InshaAllah, can still be optimized in our hunting activities (as happened in this case).

* * *

#### **2.2.3.1. Broken Access Control Issue — Access a Private Endpoint (Internal Use Only) without needing to Have a Valid Account.**

In the previous section, I have explained a little that we will try to access that interesting feature with a general account that we have or even without an account.

At the time of execution, I tried to access this interesting feature **without** an account first. Because of course, the impact will be different when you are able to retrieve customer data without a valid account or with a valid account (although personally, I don’t know whether Bugcrowd and Program Owner will agree with this point of view or not. However, it’s worth to try).

As a simple illustration, here is an example of an API request — which I have censored of course:
  
  
  POST /api/1stRedacted/2ndRedacted/1stendpoint HTTP/1.1
  Host: mainredacted.target.tld
  X-CSRF-Token: unique_token_of_**valid_session** _here
  Cookie: **valid_user_cookies** _here
  
  [[email protected]](/cdn-cgi/l/email-protection)

The simplest step we can take to execute this scenario (access the feature without a valid account) is to delete everything associated with the session in the request (such as cookies or unique tokens in the header). Unfortunately, that didn’t work.

On that occasion, I tried to look back at the request sent by the application when we wanted to access several menus without using a valid account. From this situation, finally I realized that even though I wasn’t logged in, it turned out that this application still sent requests with a (non-login state) unique token in the header.

Not long after, I tried to retrieve the unique token and cookie (in this non-login state) to reuse it to that endpoint. In short, I managed to retrieve customer data without needing a valid account.
  
  
  POST /api/1stRedacted/2ndRedacted/1stendpoint HTTP/1.1
  Host: subdomain.target.tld
  X-CSRF-Token: unique_token_in_**non-login_state**
  Cookie: user_cookies_in_**non-login_state**
  
  [[email protected]](/cdn-cgi/l/email-protection)

After I reported this, Bugcrowd ASE and Program Owner decided that the severity of the issue was P1 and put it in the “authentication bypass” category (for your information, I selected the Broken Access Control category without any severity).

![](https://cdn-images-1.medium.com/max/1600/1*F8dsJ9JGBC0qxlt7XbQrrw.png)Broken Access Control — Determined as Authentication Bypass

Alhamdulillah, this is my first paid P1 in this program.

And after that, the hunting stopped here for about 2 months because I didn’t know what to do.

* * *

### **III. THE STORY CONTINUES IN DECEMBER 2019 TO JANUARY 2020**

I explained most of this in one of my writings earlier in the year — [“From Recon to Optimizing RCE Results”](https://medium.com/bugbountywriteup/from-recon-to-optimizing-rce-results-simple-story-with-one-of-the-biggest-ict-company-in-the-ea710bca487a). But there are a few things I want to add to this point so that readers can see the flow of the paid P1 issue that I got in September 2020.

* * *

#### **3.1. A Little Recap**

As I have explained, from these activities I found quite a lot of issues with the severity of P1 (and 4 of them touched the **mainredacted.target.tld** asset which led to paid P1).

For 3 paid P1 issues, the flow is quite the same as the previous one, namely I managed to log in with some of their **internal company accounts** (no longer an account that looks like a normal user with a public email address) that uses the credential pattern I found, which have access to the interesting features discussed earlier.

**Note:** They see this as an issue because the account I found **uses company email** and **has access to that feature (API)** that can be used to retrieve customer data.

![](https://cdn-images-1.medium.com/max/1600/1*Nb4BOfBfV8XYqBEvdsQQ8Q.png)4 Paid P1s

**Then, what about the other one?** When I managed to log into one of their other dashboards (which also critical enough but is not included in the scoped bounty assets yet), I found an email with the pattern [[email protected]](/cdn-cgi/l/email-protection) (replace the x with numbers). At that time, I tried to log in using this email (on **mainredacted.target.tld**) with the password pattern I found, and Alhamdulillah, it worked. And again, this account also has access to the feature (API) discusses earlier — and the total test accounts found were about 20 accounts. So, all of 4 paid P1 story is over.

**How did they mitigate at that time?** From what I can see, they are focused on fixing the account that is the problem. In other words, they changed the password or deactivated the account. I have recommended to them to blacklist any password patterns I find. But it looks like they didn’t do it (at least, as far as I know, until September 2020).

**How do I know?** Simple, because one of their applications (which is connected to their SSO) notifies from the message displayed when it fails to login. If the account exists but the password is wrong, it will say that the password is wrong. Meanwhile, if the account and the password are correct but the account has been deactivated, it will say that the account has been disabled.

* * *

#### **3.2. They Changed the Passwords of the Affected Accounts and Deactivated the Test Accounts, So What to do Next?**

To be honest, at that time I was a little bit unwilling if this hunting activity stopped here (even though at the end of this hunting activity, Allah willed me to find an RCE in one of their public assets and successfully access their internal network). So, what do I do?

Remember, in 2018 I have enumerated the subdomains of this target. From these results, I found that there are several subdomains that contain the names test, stg, uat, and the like. In short, after repeating the subdomain enumeration activity at this period, I tried to find a test version of the application I was testing (contain the names of test, stg, uat, and so on), and tried to login through that asset.

Surprisingly, it turns out that test accounts that have been deactivated in production area, can be reused in the development area.

After reporting it, I got another P1 again. But unfortunately, even though the impact is the same, they consider this subdomain not to be included in the in-scope assets of bounty program. However, at least this is much better than being considered a duplicate.

![](https://cdn-images-1.medium.com/max/1600/1*xTTthyp2m2f4k4zajWzfXQ.png)Issue in the Development Area

**There is one interesting thing here**. Do you know what that is? **Accidentally, I showed a screenshot equipped with an HTTP Request view in Burpsuite (on that report)** which I was aiming for to show that it is not reproducible in production but reproducible in the development area.

Please keep this in mind, because in the September 2020 story, we will return to this point.

* * *

### **IV. AND FINALLY, STARTING FROM HERE, THE CONTENTS OF MY PAID P1 REPORT FOR SEPTEMBER 2020 BEGIN**

In general, in September 2020, I came across one more account using the credential pattern I found (I’ll tell you how in another section) and came back to see the exact same interface I had found earlier (in October 2019). But when I try to enter an email address that I know has user data, it turns out that the application no longer displays user data in it. After I analyzed the request used, it turned out that the API had really changed.

With this situation in mind, I finally tried to do further analysis and went back to looking at some of my previous reports. In short, I’ve found a way to “bypass” the “protections” implemented by developers to prevent users (even with special privileges) from retrieving customer data (via previous API).

And the journey to reach this point requires at least 4 chains of vulnerability namely:

  * Weak login implementation at one of their Portal (let’s call weaksub.target.tld — which connected to their SSO) that can direct us to determine which target’s account is using a weak password.
  * The presence of weak passwords that some target’s employees still use.
  * “Bypass” (I quote this word for a specific purpose) protection that has been implemented on **mainredacted.target.tld** (which I’m focused on) to prevent some internal users from collecting customer data (this bypass uses unprotected direct API Access). And at that time, I able to extract customer personal information from multiple customers.
  * Rate limit issue in API endpoint that allows Attackers to determine which internal account is having customer personal information details. I have been able to brute force over 10.000 accounts in about 10 minutes.

I’ll paste my report here and redact anything associated with the company name, endpoint and any sensitive data. And of course, I will add in certain sections to strengthen the explanation of this flow.

* * *

#### **4.1. First Step — Try to Find an Endpoint that is not Well Protected**

As we know, there are several sites on the target subdomain that are connected to SSO. In simply, by only using one account created on one accountcreationsubdomain.target.tld, we will be able to login to other several sites (of course as long as we have the correct access rights on these other sites).

From most of the endpoints found, it can be seen that most of the endpoints are CAPTCHA protected. That means we definitely can’t carry out an automatic brute force against them. But after a little exploration, finally I found that one portal — <https://weaksub.target.tld/> is not protected by CAPTCHA. It only enforces a limit on login attempts (which is 6 attempts).

As a side note, this weaksub.target.tld asset is decided as a part of their points-only program. And this asset cannot be found in the main domain as I described earlier in section #2.2.1. I found this one by looking at my subdomain enumeration results (from the screenshots — since we can recognize it from the similar interface).

* * *

#### **4.2. Second Step — Found a not Well Protected Endpoint, then what? Try to Find the Valid Accounts!**

And as we know from one of the reports I have submitted (story in December 2019 to January 2020 period), I have collected many credentials via GitHub Recon (is the password valid / invalid). From this recon activity, I finally found a pattern of credentials that show up frequently. Based on this activity, I can assume that these are the default credentials provided by the administrator for each user (and the assumption is correct).

From here, then I use all of those credentials for the set of accounts I have gathered from extraction from SubW, SubX, SubY, TargetXYZ, and also from GitHub Recon.

* * *

#### **4.2.1. So, What Exactly is SubW, SubX, SubY, and TargetXYZ?**

Simply put, these four subdomains are subdomains that allow me to get all the emails listed on them.

  * **SubW — sub2.target.tld (August 2019) — Bounty Scope** : I found an issue that allowed me to enumerate all registered email addresses by simply changing the ID parameter (number based) in one of their endpoints. Yes, I kept the whole list. This one also offers a bounty, and I got my paid P4 from this.
  * **SubX — sub3.target.tld (August 2019) — Points Only Scope** : I found multiple SQL Injection issues which allows me to enumerate all registered email addresses. This one doesn’t offer a bounty, but they gave me 1,000 USD for this.
  * **SubY — sub4.target.tld (August 2019) — Points Only Scope** : I found a simple IDOR which allows me to access their administrator dashboard. In short, I managed to enumerate all the email addresses listed.
  * **TargetXYZ.tld (December 2019) — Points Only Scope** : I found debug mode still active in the Laravel application they are using. When I access one of the endpoints (crawled with dirsearch), it turns out that this endpoint displays an error message containing sensitive things such as the database password and also the password to login to the administrator dashboard. In short, I logged into the admin dashboard and I downloaded a csv file which contained quite a list of email addresses from their internal employees.

As we can see, the 3 targets above are a points program only. However, from these targets, I got optimal results in extracting the data contained in the **mainredacted.target.tld** (listed in their bounty program).

* * *

#### **4.2.2. The Result from Brute Force Attack in https://weaksub.target.tld/ (that not Protected with CAPTCHA)**

So, how is the result? Alhamdulillah, the results of this attack produce good output. I was able to find several valid accounts using the password pattern that I found.

**Note** : out of 6 “available” login attempts, I only use 2 password patterns they use the most. So, we will have no trouble being blocked. After all, blocking only lasted 15 minutes, so it’s no big deal if it’s blocked.

* * *

#### **4.3. Third Step — I Found Several Valid Accounts, then what? Try to Find out the Account that can Access Internal Menu in the mainredacted.target.tld Portal**

Well, this is the challenge. Even though we have found valid accounts, we must find among these accounts that have certain access rights on the **mainredacted.target.tld** (that has an interesting feature via API that discussed earlier). To make it short, from those several valid accounts, I finally found one account that has special access to the Portal. (Sounds familiar? But this time it’s not as easy as before **because their Developer has changed the application flow to prevent customer data extraction**).

So, before we go any further for the “bypass” trick, then let’s try returning to the situation on this **mainredacted.target.tld**.

* * *

#### **4.3.1. Back to Story in October 2019 (Section #2.2.2. on this report)**

From one of my old report related Broken Access Control in **mainredacted.target.tld** Portal, we have learned that in order to be able to extract customer data via that interesting Feature, we must have access rights to **/api/1stRedacted/2ndRedacted/1stendpoint** Endpoint. Basically, this endpoint will be responsible for providing detailed customer data by entering the correct email address.

**Note:** in my original report I showed them a screenshot of the HTTP request, response and also the interface. But I can’t show it here. Just remember the endpoint context in this section.

* * *

#### **4.3.2. As Said, Their Developer has Changed the way of the mainredacted.target.tld Portal Accesses that Interesting Feature**

If from the previous section we saw that we will immediately be able to see customer data by entering a valid email address, but at this time, the **mainredacted.target.tld** portal no longer displays customer details. In short, the features, the name of the features and the interface are similar, however, the results were very different. Instead of showing customer data, now this feature only shows date and some **in** sensitive information.

After looking at the request carefully, I found out if the endpoint was really different from the one, I previously mentioned.

Previous API Request:
  
  
  POST /api/1stRedacted/2ndRedacted/1stendpoint HTTP/1.1
  Host: mainredacted.target.tld
  X-CSRF-Token: unique_token_of_valid_session_here
  Cookie: valid_user_cookies_here
  
  [[email protected]](/cdn-cgi/l/email-protection)

Current API Request:
  
  
  GET /api/vx/3rdRedacted/4thRedacted/5thRedacted/2ndEndpoint?ParametercontainUserEmail= [[email protected]](/cdn-cgi/l/email-protection)  HTTP/1.1  
  Host: mainredacted.target.tld  
  X-CSRF-Token: unique_token_of_valid_session_here  
  Cookie: valid_user_cookies_here

As we can see, now they use version x for a very similar feature (with different path and endpoint). However, in this case, the flow totally prevents the user (with special access rights) from being able to extract customer data again.

Yes, I had put back the /api/1stRedacted/2ndRedacted/1stendpoint (the API that used in October 2019) endpoint in hopes of getting customer data, but it’s failed. This endpoint doesn’t work anymore.

So, this one will be another challenge.

* * *

#### **4.3.3. Remember about My Report about the Test Version of this Target Portal? Yes, Test Version! (section #3.2).**

At the end of section #3.2, I said: _“Accidentally, I showed a screenshot equipped with an HTTP Request view in Burpsuite (on that report) which I was aiming for to show that it is not reproducible in production but reproducible in the development area.”_

**Why is this interesting?** Because it turns out that they send requests to different endpoints to collect the exact same data such as flow in October 2019 and flow in December 2019 to January 2020, but with different endpoints.

In short, from the screenshot of my report, I realize that another API request has been made, which is:
  
  
  POST /api/vx/6thRedacted/3rdEndpoint HTTP/1.1
  Host: mainredacted.target.tld
  X-CSRF-Token: unique_token_of_valid_session_here
  Cookie: valid_user_cookies_here
  
  [[email protected]](/cdn-cgi/l/email-protection)

From here, then I try to put this endpoint (API vx) to the request and send it into the POST request with ParameterContainUserEmail POST Data. And surprisingly, I was able to extract customer details again via this endpoint. In short, we will be able to “bypass” the protection of this feature by using the OLD API requests. (Now you will understand why I quoted the word “bypass”, because this is not really a pure bypass, it just uses the old API in the development area — which their developers hide in the production area).

**WAIT** , so what’s the point of me saying about the set of accounts I have gathered from extraction from SubW, SubX, SubY, TargetXYZ, and also from GitHub Recon? Well, the fourth step will be the answer.

* * *

#### **4.4. Fourth Step — Rate Limit Issue in API Endpoint that allows Attackers to Determine which Internal Account is having Customer Personal Information.**

So, at this point, we already know about the Old API (which was hidden by their Developers to prevent data extraction from happening again) which can still be used. Here is a sample request:
  
  
  POST /api/vx/6thRedacted/3rdEndpoint HTTP/1.1
  Host: mainredacted.target.tld
  X-CSRF-Token: unique_token_of_valid_session_here
  Cookie: valid_user_cookies_here
  
  [[email protected]](/cdn-cgi/l/email-protection)

From here, we just need to change the “**ParameterContainUserEmail** ” value to something else. Maybe the question is, what values ​​am I currently using?

As mentioned earlier, I use bunch of accounts I have gathered from extraction from SubW, SubX, SubY, TargetXYZ, and also from GitHub Recon. So far, it has given around 10,000 unique email addresses.

In short, by using these 10,000 email addresses (it only took about 10 minutes), I finally found several accounts that have personal customer information. (In this section, I show them some proof of this).

* * *

#### **4.5. The Submission**

Not long after I submitted this report with some recommendations, they responded quickly and immediately followed up on the issue.

![](https://cdn-images-1.medium.com/max/1600/1*5kC41x33xZOq2T5ZVodDQg.png) ![](https://cdn-images-1.medium.com/max/1600/1*U-J_2--UG9v2YVfipSdejg.png)Response from Program Owner

How about the bounty? Alhamdulillah, they also give the maximum value from the range in P1 which they have defined.

![](https://cdn-images-1.medium.com/max/1600/1*DILmCm-lLIoBXi7olcoIiw.png)6th Paid P1

As a little information, I have obtained their permission to release this write-up by censoring their company name.

* * *

### **V. LESSON LEARNED**

So here we are, almost at the end of the write-up. In this section, I want to add a simple recap (which I actually tucked into some of the previous sections) to make it easier for readers to understand some of the lessons from this simple journey:

  * I keep all hunting results for some consideration, namely because InshaAllah it will be useful one day, and because there is no provision to delete the test results (as is generally done in formal PenTest jobs). With the permission of Allah, from this simple write-up, it can be seen that the results of the hunting we have been doing (even though it has been a long time) are still quite useful.
  * From this write-up, InshaAllah we also can learn one valuable thing, that is we need to know the application well so that InshaAllah we can test it more optimally. In 2018, since I only intended to do a simple refresher, I didn’t try to look further into this which ended up making me to miss quite a lot.

But there is another good thing from this is, in 2019 they increased their reward range, so I also managed to get a reward that was much better. There is always a good lesson in everything. Alhamdulillah.

  * As you can see (from section #2.2.1), I only have 1 account left which is still valid to use. However, even if there is only 1 account left, don’t despair. Because this account, InshaAllah, can still be optimized in our hunting activities (as happened in this case). Yes, better you have one than you don’t have it. Test with access always provides a wider perspective than without access.
  * If you find that an application is actually connected to SSO and can log in from multiple endpoints (not concentrated to one endpoint), then InshaAllah you have the opportunity to find the weakest endpoint that you can possibly use for (example) brute force (with account that already obtained). Some people may underestimate this kind of issue, **but I prefer to keep it in my eye**.
  * Security problem does not lie in just one thing. In this article, we can see that we can use the data from other assets to be used on the main asset belonging to the target (which is included in their bounty program).
  * Please kindly enjoy your bug hunting activity. Maybe not everyone agrees with this, but don’t always think about the bounty (especially if you just start in this one and never has an experience with it). Try to test the “legal/official” target as much as you can. InshaAllah it can improve your knowledge, methods, and anything when looking for bugs in the target that offering bounties.

I tried to learn many technologies (that I had never face) from the target that didn’t offer bounty (but open the responsible disclosure program). In this point, one thing that I can say is, those used technologies aren’t always the technology that we face every day. In other words, we need an official “land” (legal target) to learn it and make us familiar with it.

Well, finally my simple write-up ends here. See you next time, InshaAllah.

* * *

### **VI. CREDITS**

  * [Th3g3nt3lman](https://twitter.com/th3g3nt3lman) talks at Bugcrowd University: [Github Recon and Sensitive Data Exposure](https://www.youtube.com/watch?v=l0YsEk_59fQ).
  * [Aquatone](https://github.com/michenriksen/aquatone) by michenriksen
  * [Sudomy Subdomain Enumeration Tool](https://github.com/Screetsec/Sudomy) by Screetsec.
  * [From Recon to Optimizing RCE Results](http://www.firstsight.me/2020/02/from-recon-to-optimizing-rce-results-simple-story-with-one-of-the-biggest-ict-company-in-the-world/).
