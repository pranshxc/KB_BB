---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-06-19_from-recon-to-bypassing-mfa-implementation-in-owa-by-using-ews-misconfiguration.md
original_filename: 2020-06-19_from-recon-to-bypassing-mfa-implementation-in-owa-by-using-ews-misconfiguration.md
title: From Recon to Bypassing MFA Implementation in OWA by Using EWS Misconfiguration
category: documents
detected_topics:
- mfa
- sso
- idor
- ssrf
- command-injection
- otp
tags:
- imported
- documents
- mfa
- sso
- idor
- ssrf
- command-injection
- otp
language: en
raw_sha256: cc5f33cfda44cdf68ab704adbb3152950de14002d2d01d30f072d72c488c459f
text_sha256: 19c3ce3b216e5640e1b1f3c738d3d84e9ca2a71b4e200011144f5a99e858c7ae
ingested_at: '2026-06-28T07:32:02Z'
sensitivity: unknown
redactions_applied: false
---

# From Recon to Bypassing MFA Implementation in OWA by Using EWS Misconfiguration

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-06-19_from-recon-to-bypassing-mfa-implementation-in-owa-by-using-ews-misconfiguration.md
- Source Type: markdown
- Detected Topics: mfa, sso, idor, ssrf, command-injection, otp
- Ingested At: 2026-06-28T07:32:02Z
- Redactions Applied: False
- Raw SHA256: `cc5f33cfda44cdf68ab704adbb3152950de14002d2d01d30f072d72c488c459f`
- Text SHA256: `19c3ce3b216e5640e1b1f3c738d3d84e9ca2a71b4e200011144f5a99e858c7ae`


## Content

---
title: "From Recon to Bypassing MFA Implementation in OWA by Using EWS Misconfiguration"
page_title: "From Recon to Bypassing MFA Implementation in OWA by Using EWS Misconfiguration – Just Another Simple Write-Up"
url: "http://www.firstsight.me/2020/06/from-recon-to-bypassing-mfa-implementation-in-owa-by-using-ews-misconfiguration/"
final_url: "http://firstsight.me/2020/06/from-recon-to-bypassing-mfa-implementation-in-owa-by-using-ews-misconfiguration/"
authors: ["YoKo Kho (@YokoAcc)"]
bugs: ["Information disclosure", "2FA / MFA bypass"]
bounty: "500"
publication_date: "2020-06-19"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4484
---

[Bug Report](http://firstsight.me/category/bug-report/) / [Web Apps](http://firstsight.me/category/web-apps/) / [Write-Up](http://firstsight.me/category/write-up/)

# From Recon to Bypassing MFA Implementation in OWA by Using EWS Misconfiguration

June 19, 2020 

[__]()

A story about how I Finally could use an AD account that unenrolled to MFA, by using an EWS Misconfiguration to Access Email Inbox and (Having the Ability) to Dump the Global Address List.

**In the name of Allah, the Most Gracious, the Most Merciful.**

* * *

**_Note:_**_I want to thank (again)_[_Th3g3nt3lman_](https://twitter.com/th3g3nt3lman) _for his talks about_[ _Github Recon and Sensitive Data Exposure_](https://www.youtube.com/watch?v=l0YsEk_59fQ)** _._**_I use it as a way to find the AD credentials._  
  
_And also thanks to_[ _Beau Bullock from Black Hills Infosec_](https://www.blackhillsinfosec.com/?team=beau-bullock) _for the research they have published on_[ _Bypassing Two-Factor Authentication on OWA and Office365 Portals_](https://www.blackhillsinfosec.com/bypassing-two-factor-authentication-on-owa-portals) _(by using the EWS Misconfiguration). I use it as a way to access this protected account and to increase its impact._

As usual, I will try to release this article with two different approaches, which are:

  * For those who only need the main points of this finding (InshaAllah it can saves tons of minutes if readers understanding every flow already) – please kindly see the TL;DR section, and
  * For those who need to understand the flow of execution or journey about this finding. InshaAllah, it can tell the readers about some mindsets and hopefully can help people to enrich their insights.

Please kindly enjoy the story.

* * *

### **I. TL;DR**

Here are the simple points about this issue:

  * Finding targets that allow for logging in by **two methods** , namely as an employee (using a domain account), and as a user whose account is created specifically for the site itself.
  * To log in with an employee account (a domain account), the site **will direct us to another .TLD** (for example: from .com to net) – **ADFS endpoint**.
  * **Mindset:** if we can log in with a domain account, we will have access to this site, right?
  * Started recon on GitHub using the .net domain (not .com). For example: **_password “.target.net”_**

_See[**Th3g3nt3lman**](https://twitter.com/th3g3nt3lman)**** talks at **Bugcrowd University:** [**Github Recon and Sensitive Data Exposure**](https://www.youtube.com/watch?v=l0YsEk_59fQ) or one of my write-up: [**From Recon to Optimizing RCE Results**](http://www.firstsight.me/2020/02/from-recon-to-optimizing-rce-results-simple-story-with-one-of-the-biggest-ict-company-in-the-world/)**.**_

  * Found a repository that contains several files with more than 3,000 lines of code. On one line, I **found a username (service account – svc_nameofsvc) and password that looks like a domain account**. Trying to log in with that account at ADFS, but the results show that the account is unenrolled with the used MFA. In short, the account must be enrolled with the MFA that is applied to be able to login. And of course, we need “thing” that is used as MFA too.
  * **Trying to increase its impact**. It’s not cool if we report an issue that we found a valid password but can’t log in because it’s blocked.
  * Try to **find the EWS endpoint** → Subdomain enumeration for both of .com and .net → Look for email subdomains (common implementation) → Place the EWS behind the found subdomain → Shows a log in prompt → Log in with the found credentials → **Able to log in** – no MFA was implemented at this endpoint (no inbox displayed, remember, this is EWS).
  * Execute the **MailSniper** tools to the **EWS endpoint**. Successfully read the inbox.

See [**Black Hills Infosec Research**](https://www.blackhillsinfosec.com/): **[Bypassing Two-Factor Authentication on OWA and Office365 Portals](https://www.blackhillsinfosec.com/bypassing-two-factor-authentication-on-owa-portals/).** The PoC video regarding their research: [**O365 MFA Bypass Information**](https://www.youtube.com/watch?v=Bb_T3ILfllU).

![](http://www.firstsight.me/wp-content/uploads/2020/06/1-Successfully-Read-the-Inbox-1024x433.png)Figure 1 – Successfully Read the Inbox

  * Make a report (about 7 pages) and report this issue to the program owner.
  * Trying to increase its impact again. Told them, there is a possibility if we have the ability **to dump the “Global Address List”** by using this issue. From there, we **also able to do password spraying** (with the same found password) **to** **other service accounts** that was created.

_See**[Abusing Exchange Mailbox Permissions with MailSniper](https://www.blackhillsinfosec.com/abusing-exchange-mailbox-permissions-mailsniper/) **– For Dump the Global Address List._ A _nd see[**Attacking Exchange with MailSniper**](https://www.blackhillsinfosec.com/attacking-exchange-with-mailsniper/) – For Password Spraying._

  * Triaged and rewarded **in the same day**. And fixed **in the next day**.

![](http://www.firstsight.me/wp-content/uploads/2020/06/2-The-Bug-was-Fixed-in-about-2-days-1024x197.png)Figure 2 – The Bug was Fixed in about 2 days

* * *

### **II. THE JOURNEY**

#### **2.1. Behind the Scene Part I**

One day, I want to test one of the subdomain that is included in an in-scope asset. From the many assets available, it seems that only this asset allows users to sign in with 2 methods, namely as an employee (using a domain account), and as a user whose account is created specifically for this app.

At that time, I tried to log in with some common passwords that were considered weak, but the results were not good. After several unsuccessful attempts, I decided to try testing the log in method with an employee account.

When we choose to log in with an employee account, the application will direct us to ADFS endpoint with another .TLD (for example, from .com to .net). From here, we can draw the conclusion that if we have an employee account (a domain account), then we can log in to those application.

**So, what should we do?**

Well, I’m trying to get back to basics again. In this situation, I started recon on GitHub to find things that might be useful for me to use. (This talks could be a very good reference: [Github Recon and Sensitive Data Exposure](https://www.youtube.com/watch?v=l0YsEk_59fQ)). In short, I found an interesting repository that made me find interesting findings (will not discuss it in this article). After sending the report, they triage and reward in two days.

![](http://www.firstsight.me/wp-content/uploads/2020/06/3-First-Finding-on-this-Program-1024x174.png)Figure 3 – First Finding on this Program

Another reference about this recon part: one of my write-up: [From Recon to Optimizing RCE Results](http://www.firstsight.me/2020/02/from-recon-to-optimizing-rce-results-simple-story-with-one-of-the-biggest-ict-company-in-the-world/).

* * *

#### **2.2. Behind the Scene Part II**

After that day, I found 2 other simple issues (rewarded too) and then I didn’t have a clue anymore about the things I had to do with the target available.

So, I returned to GitHub again to get some **fresh air**. Things that I do again is put the **password “.target.net”** keyword on GitHub. After the previous repository was removed from GitHub, I found another interesting repository **ranked 5th on the first page**.

Honestly speaking, there is no password information on those result. But from what I’ve experienced, **credentials aren’t always put behind the parameters**. From this mindset, then I began to explore this repository.

* * *

#### **2.3. Exploration**

When I opened that repository, I was really surprised by the number of lines (more than 3,000 lines of code). Well, it was midnight in my time zone when I found this and I’m not in good condition to reading so many lines at that time – remember, I do this GitHub Recon **for a fresh air**.

But then, the condition changed when I saw the 6th-27th line – about an AD account and Connection String (although **no credentials yet** on this rows).

From here, I hope that the developer makes a common mistake by put hardcode credentials in this repo. (and yes, **the hope come true**)!

In line 394, I find 2 texts that I believe are credentials (I doubt if there are developers who make such difficult parameters).
  
  
  string Table = "file.xlsx";
  XYZEndpoint endpoint = new XYZEndpoint("**username_here** ", "**very_complex_password_here** ");
  string response = endpoint.GetCollectionData(Table);

Based on this situation, then I immediately use it in ADFS endpoint (the one that use .net domain). After try to log in, then I can’t do anything. The account **wasn’t enrolled on _Censored_ MFA**.

(I deleted the MFA that was used to avoid misunderstanding this report. I’m worried if people consider it to be an MFA vendor vulnerability – Note: It’s not).

**Did I stop?** Not yet. I tried to find another endpoint (such as VPN service), but I again failed to use it to log in. I have tried about 3 VPN endpoints, and none of them have managed to get me logged in.

**So, did I stop?** Again, not yet. I **must try to increase its impact**. It’s not cool if we report an issue that we found a valid password but can’t log in because it’s blocked.

_In this situation, time is getting tight! Why? Because I’m sure,**there will be an alarm that is triggered** because there are (at least) more than **4 attempts conducted from the country where I came from**._

* * *

#### **2.4. A Way to Read an Inbox without Enrolled on Censored MFA**

#### **2.4.1. Exchange Web Services (EWS) Endpoint!**

Almost hopeless with this situation, then Alhamdulillah, I am reminded of one research released by BlackHills InfoSec about [Bypassing Two Factor Authentication on OWA Portals](https://www.blackhillsinfosec.com/bypassing-two-factor-authentication-on-owa-portals/).

From the research, they (BlackHills InfoSec) said, although the account was blocked by 2FA (in this case, the account was not blocked, but not enrolled yet on the used MFA), there is a possibility for us to read every email on this account. This can happen by using a common misconfiguration at the EWS endpoint.

I will quote a good explanation about this (and let the experts explain it to you, both those who gave a nice talk – [Outlook and Exchange for the Bad Guys by Nick Landers](https://www.youtube.com/watch?v=cVhc9VOK5MY) – and those who released this research – [Beau Bullock from Black Hills Infosec](https://www.blackhillsinfosec.com/?team=beau-bullock)).

> Beau said: While at DerbyCon I sat in on a talk called “Outlook & Exchange for the Bad Guys” by Nick Landers. It was an awesome talk that I highly recommend checking out. During his talk Nick received a question from the audience in regards to whether two-factor authentication (2FA) would stop the attacks he mentioned during the talk. Nick replied with a statement I found very interesting. He said __**“I’ve seen some organizations lockdown 2FA on OWA. So when you go to the Outlook Web Access you have to supply a token before you can finish logging in. That wouldn’t stop a lot of these attacks because two-factor auth doesn’t apply to EWS or the NTLM auth on the Autodiscover page.”**__

So, what is EWS? Quoted from Beau’s research: “ _EWS is a web-based API enabled on Exchange servers that Microsoft recommends customers use when developing client applications that need to interface with Exchange. The API allows for applications to have the ability to interact with email messages, contacts, calendar, and more from user’s mailboxes_.”

In short, in general implementation (thanks for the explanation from the program owner), even though ADFS has been protected by MFA, sometimes the system owner misses to enforce other endpoint to use MFA (in this case, EWS endpoint).

* * *

#### **2.4.2. Look for EWS Endpoint – Subdomain Enumeration!**

At first, I didn’t know whether there was an EWS endpoint misconfiguration on this target or not. So, what I’m doing is trying to do the subdomain enumeration.

To be honest, I know that the common implementation that do by company is put this EWS endpoint on **mail** / **email** / **webmail** subdomain. But, it is not a waste of time to do this enumeration. At least it only takes a few minutes. And the results, InshaAllah, will hopefully be useful for me later (who knows, maybe one day they will make *.target.com as part of the in-scope target).

**Note:** in this case, I use the [Sudomy Subdomain Enumeration Tool](https://github.com/Screetsec/Sudomy) that created by Screetsec.

After a few minutes, I got the results. Then as expected, they have “**mail** ” subdomain. When I first visited mail.target.com, this subdomain directed me to the ADFS endpoint again (in .net TLD). Then in the second try, I tried to put EWS behind mail.target.com, and it showed a log in prompt.

![](http://www.firstsight.me/wp-content/uploads/2020/06/4-Log-in-Prompt-1024x346.png)Figure 4 – Log in Prompt

When I put the found credentials at this prompt, then I finally made it in! I can log in without providing any MFA and without the need for this account to be enrolled with the MFA used.

![](http://www.firstsight.me/wp-content/uploads/2020/06/5-Success-to-Log-in-without-being-Enrolled-to-MFA-1024x212.png)Figure 5 – Success to Log in without being Enrolled to MFA

From this result, I decided to continue the journey to my first goal, which was to read the inbox without having to be enrolled with the MFA used.

* * *

#### **2.4.3. Preparing the Environment**

So, the first thing we need to do to read emails from those account is download the MailSniper tools on <https://github.com/dafthack/MailSniper>. Basically this tool is made to make it easier for someone to search data in an email **using certain words**. But, this tools also can help us to read an email within EWS environment.

* * *

#### **2.4.4. The “Bypass”**

After the tools has been downloaded, then run powershell and execute few of this commands:
  
  
  **C:\Users\YoKo\Tools > **powershell.exe -exec bypass
  Windows PowerShell
  Copyright (C) Microsoft Corporation. All rights reserved. 
   
  Try the new cross-platform PowerShell https://aka.ms/pscore6 
   
  **PS C:\Users\YoKo\Tools >** cd .\MailSniper-master\
  **PS C:\Users\YoKo\Tools\MailSniper-master >** Import-Module .\MailSniper.ps1
  **PS C:\Users\YoKo\Tools\MailSniper-master >** Invoke-SelfSearch -Mailbox **username** @**domain.tld** -ExchHostname **mail.domain.tld** -Remote

In short, there are 2 commands that should be executed, which are:

  * _Import-Module .\MailSniper.ps1_ , and
  *  _Invoke-SelfSearch -Mailbox**username** @**domain.tld** -ExchHostname **mail.domain.tld** -Remote_

Please kindly note, after we enter the command, **then a credential box will pop up** **requesting the credentials** of the **username** @**domain.tld**. All we need to do just type again the credentials.

![](http://www.firstsight.me/wp-content/uploads/2020/06/6-Windows-PowerShell-Credentials-Request.png)Figure 6 – Windows PowerShell Credentials Request

If everything correct, then the tools will give us an information if “they” found an Inbox Folder.
  
  
  [*] Trying Exchange version Exchange2010
   
  cmdlet Get-Credential at command pipeline position 1
  Supply values for the following parameters:
  Credential
  [*] Using EWS URL **_https://mail.domain.tld/EWS/Exchange.asmx_**
  [***] Found folder: Inbox
  [*] Now searching mailbox: **username** @**domain.tld** for the terms *password* *creds* *credentials*.

* * *

#### **2.4.5. The Result**

And after few minutes (depend on how much the email found with those provided keywords), we will get a result. In this case, things that relates to password, creds, or credentials on this account was a social media information.

![](http://www.firstsight.me/wp-content/uploads/2020/06/7-Accessing-the-Targets-Inbox-via-EWS-with-MailSniper-1024x233.png)Figure 7 – Accessing the Target’s Inbox via EWS with MailSniper

To ensure if the result is correct, then I also tried to login into those social media with the same account and password. **The result is, correct!** But not lucky yet, there is social media behaviour protection that asked me to put the correct phone number (It’s normal, I tried to log in from different country).

![](http://www.firstsight.me/wp-content/uploads/2020/06/8-Another-Test-to-See-my-Own-Message-on-Victims-Inbox-1024x116.png)Figure 8 – Another Test to See my Own Message on Victim’s Inbox

* * *

#### **2.4.6. Once Again, Try to Increase Its Impact**

Maybe some of us will ask, we can’t log into the VPN with this account, we also have limited access to exploit the system with this account (because we can’t use it to enter the target internal network). So, what else can we do with this?

Well, I also have a similar question, at least, until I saw another research released by Beau Bullock of Black Hills Infosec. In short, there are two more things that we can do for our situation.

* * *

#### **2.4.6.1. Global Address List Dump and Password Spraying to Entire Accounts**

Before we go further, let me ask you something, what is the common mistake made by system owners when maintaining multiple service accounts? (Remember, in this case, I found a service account).

If you think that there is a **possibility** if the system owner **uses the same password for another service account (or for another account that they managed)** , then I can say that the answer is correct.

So, if we able to dump the Global Address List, then InshaAllah we have the opportunity to find other service accounts with the same pattern. And we also have the opportunity to execute password spraying attack into all service accounts with passwords found (no need to test other credentials because I believe there is a rate-limit protection in the enterprise. We only need to test one password that we found).

To do this, we can see both of this research:

  * 1st research: [Abusing Exchange Mailbox Permissions with MailSniper](https://www.blackhillsinfosec.com/abusing-exchange-mailbox-permissions-mailsniper/). The way to dump the Global Address List can be found in “**Invoke-OpenInboxFinder** ” section in this research.
  * 2nd research: [Attacking Exchange with MailSniper](https://www.blackhillsinfosec.com/attacking-exchange-with-mailsniper/). One of the good information that was stated by Beau Bullock is: “ _In testing I’ve noticed the EWS password spraying method is significantly faster. Both Invoke-PasswordSprayOWA and using Burp Intruder with 15 threads took about 1 hour and 45 minutes to**complete spraying 10,000 users. Spraying that same list of users against EWS took only 9 minutes and 28 seconds**_**.** ”Nice, isn’t it?

From here, we just have an opportunity to increase its impact! Well, I said an opportunity, because I’m not really sure whether this technique can work or not. But by looking at the methods presented in the research, I’m sure it can work!

Note: I **didn’t execute this**. Without any permission, we can’t do it. (yes, in a real attack, the Attacker will do it without asking any permissions, but kindly note that **in bug hunting, we didn’t come with the intention to breach**).

* * *

#### **2.4.7. Another Possible Scenario**

In another scenario, there is a possibility for an external Attacker to combine this issue with social engineering activity. For example, they act like a valid account owner of those found account and try to communicate with the victim via email spoofing (target.tld domain).

Then the attacker “builds a relationship” with the internal team to ensure that those Attacker can get full access to the account (enrolled with the MFA with a device / phone number / etc. that controlled by the Attacker). Not sure how effective this scenario is, but it might be nice to consider the risk.

* * *

#### **2.5. The Reward**

The report has been triaged and rewarded in one day and fixed in the next day.

![](http://www.firstsight.me/wp-content/uploads/2020/06/2-The-Bug-was-Fixed-in-about-2-days-1024x197.png)Figure 9 – The Bug was Fixed in about 2 days

* * *

### **III. LESSONS LEARNED**

In this section, I would like to re-add few lessons learned that [has been stated in one of my writings](http://www.firstsight.me/2020/02/from-recon-to-optimizing-rce-results-simple-story-with-one-of-the-biggest-ict-company-in-the-world/):

  * In my simple perspective (just please kindly correct me if I’m wrong), recon doesn’t always mean an asset discovery activity. In this one, it can also mean that we try to learn how the API works, target’s development culture, and more.

Remember, while responding one of [@Mongobug](https://twitter.com/mongobug)‘s tweets, [@NahamSec](https://twitter.com/NahamSec) also [explains about one of recon’s definitions in the very simple words](https://twitter.com/NahamSec/status/1118525950117892096?s=20): “ _Recon shouldn’t just be limited to finding assets and outdated stuff. It’s also understanding the app and finding functionality that’s not easily accessible. There needs to be a balance between recon and good ol hacking on the application in order to be successful_ “.

![](http://www.firstsight.me/wp-content/uploads/2020/06/10-Recon-doesn’t-always-mean-an-Asset-Discovery-Activity-1024x227.png)Figure 10 – Recon doesn’t always mean an Asset Discovery Activity

  * Don’t give up on reading every line of code that you find on the GitHub Repository from your GitHub Recon activity. Honestly, I haven’t fully read the code. I just take the point, read the parameters, try to understand the flow, and see if there is anything good we can use.
  * From what I’ve experienced, credentials aren’t always put behind the parameters. From this mindset, try exploring the repository that you find.
  * Please kindly enjoy your bug hunting activity. Maybe not everyone agrees with this, but, don’t always think about the bounty (especially if you just start in this one and never has an experience with it). Try to test the “legal/official” target as much as you can. InshaAllah it can improve your knowledge, methods, and anything when looking for bugs in the target that offering bounties.

I tried to learn much technologies (that I had never face) from the target that didn’t offer bounty (but open the responsible disclosure program). In this point, one thing that I can say is, those used technologies aren’t always the technology that we face every day. In other words, we need an official “playground” (legal target) to learn it and make us familiar with it.

  * Just try going back to basics
  * If you think that someone can do it easily, then try to [see these motivational words](https://twitter.com/brutelogic/status/964143091635630080) from [@BruteLogic](https://twitter.com/brutelogic): ” They think we do things in a snap. But there’s a lot of hard work, endless hours of trial and error. Many hours parsing search engine results, reading tons of not so helpful information. What they end up seeing is the show time. We make it look easy but it’s not.”

![](http://www.firstsight.me/wp-content/uploads/2020/06/11-One-of-the-Motivational-Words.png)Figure 11 – One of the Motivational Words

  * And the last one is my really favorite quotes (seriously, this is beautiful) :

![](http://www.firstsight.me/wp-content/uploads/2020/06/12-No-one-Goes-from-Noob-to-Elite-just-like-that-1024x502.png)Figure 12 – No one Goes from Noob to Elite just like that

These words really motivate me a lot to share things even though things that I share aren’t always good things. But with the permission of Allah, I got a lot of feedback that motivate me to correct my mistakes or to improve things.

* * *

Well, finally my simple article ends here. See you next time, InshaAllah.

* * *

### **IV. CREDITS**

  * [Th3g3nt3lman](https://twitter.com/th3g3nt3lman) talks at Bugcrowd University: [Github Recon and Sensitive Data Exposure](https://www.youtube.com/watch?v=l0YsEk_59fQ).
  * [Bypassing Two-Factor Authentication on OWA & Office365 Portals](https://www.blackhillsinfosec.com/bypassing-two-factor-authentication-on-owa-portals/) – Black Hills Infosec.
  * [O365 MFA Bypass Information](https://www.youtube.com/watch?v=Bb_T3ILfllU) (PoC Video) – Black Hills Infosec.
  * [Outlook and Exchange for the Bad Guys](https://www.youtube.com/watch?v=cVhc9VOK5MY) by Nick Landers – on DerbyCon 6.0
  * [Abusing Exchange Mailbox Permissions with MailSniper](https://www.blackhillsinfosec.com/abusing-exchange-mailbox-permissions-mailsniper/) – Black Hills Infosec.
  * [Attacking Exchange with MailSniper](https://www.blackhillsinfosec.com/attacking-exchange-with-mailsniper/) – Black Hills Infosec.
  * MailSniper — <https://github.com/dafthack/MailSniper>.
  * [Sudomy Subdomain Enumeration Tool](https://github.com/Screetsec/Sudomy) by Screetsec.
  * [From Recon to Optimizing RCE Results](http://www.firstsight.me/2020/02/from-recon-to-optimizing-rce-results-simple-story-with-one-of-the-biggest-ict-company-in-the-world/).
