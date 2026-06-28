---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-07-12_major-security-flaws-in-popular-quickblox-chat-and-video-framework-expose-sensit.md
original_filename: 2023-07-12_major-security-flaws-in-popular-quickblox-chat-and-video-framework-expose-sensit.md
title: Major Security Flaws in Popular QuickBlox Chat And Video Framework Expose Sensitive
  Data Of Millions
category: documents
detected_topics:
- otp
- mobile-security
- automation-abuse
- idor
- access-control
- command-injection
tags:
- imported
- documents
- otp
- mobile-security
- automation-abuse
- idor
- access-control
- command-injection
language: en
raw_sha256: 73fc5f29a08468a199850818343c35ddc5e3a78b6ec92bdde1c1d48d261ed1e9
text_sha256: 04ee1b9f0d306214e5c403ab66222f75bc2206af45542b0dac7145633ab04476
ingested_at: '2026-06-28T07:32:24Z'
sensitivity: unknown
redactions_applied: false
---

# Major Security Flaws in Popular QuickBlox Chat And Video Framework Expose Sensitive Data Of Millions

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-07-12_major-security-flaws-in-popular-quickblox-chat-and-video-framework-expose-sensit.md
- Source Type: markdown
- Detected Topics: otp, mobile-security, automation-abuse, idor, access-control, command-injection
- Ingested At: 2026-06-28T07:32:24Z
- Redactions Applied: False
- Raw SHA256: `73fc5f29a08468a199850818343c35ddc5e3a78b6ec92bdde1c1d48d261ed1e9`
- Text SHA256: `04ee1b9f0d306214e5c403ab66222f75bc2206af45542b0dac7145633ab04476`


## Content

---
title: "Major Security Flaws in Popular QuickBlox Chat And Video Framework Expose Sensitive Data Of Millions"
page_title: "Security Flaws Exposed in QuickBlox Chat And Video Framework | Claroty"
url: "https://claroty.com/team82/research/major-security-flaws-in-popular-quickblox-chat-and-video-framework-expose-sensitive-data-of-millions"
final_url: "https://claroty.com/team82/research/major-security-flaws-in-popular-quickblox-chat-and-video-framework-expose-sensitive-data-of-millions"
authors: ["Amir Preminger", "Sharon Brizinov", "Itay Cohen", "Oleg Ilushin"]
programs: ["QuickBlox"]
bugs: ["IDOR", "Information disclosure", "Authentication bypass"]
publication_date: "2023-07-12"
added_date: "2023-07-24"
source: "pentester.land/writeups.json"
original_index: 933
---

[ ![Team82 Logo](https://claroty.com/build/assets/team82-logo-white-BGiCQ9zb.svg) ](/team82)

  * [Research](/team82/research)
  * [Vulnerability Dashboard](/team82/disclosure-dashboard)
  * [Talks](/team82/talks)
  * [Tools](/team82/#tools)
  * [About](/team82/#about)

[ ![Claroty](https://claroty.com/build/assets/logo-solid-white-DcRiqKcD.svg) ](/)

[ Return to Team82 Research ](/team82/research)

# Major Security Flaws in Popular QuickBlox Chat And Video Framework Expose Sensitive Data Of Millions

Amir Preminger, 

Sharon Brizinov, 

Itay Cohen, 

Oleg Ilushin 

/ July 12th, 2023

![Security Flaws Exposed in QuickBlox Chat And Video Framework](/img/asset/YXNzZXRzL3F1aWNrYmxveC1ibG9nLWdyYXBoaWNzLTAzLTE2ODg1NzE0ODMuanBn/quickblox-blog-graphics-03-1688571483.jpg?fm=webp&fit=crop&w=800&h=450&s=7637cfa16b70b0b946a06192ff7e0d33)

## Executive Summary

  * Team82 and Check Point Research (CPR) collaborated to look at the security of the popular QuickBlox software development kit (SDK) and application programming interface (API). 

  * QuickBlox’s development framework runs under the hood of popular chat and video applications in critical industries such as finance and telemedicine. 

  * Together, we uncovered [critical vulnerabilities](https://claroty.com/team82/disclosure-dashboard) that could put the personal information of millions of users at risk. 

  * Team82 and CPR also demonstrate proof-of-concept exploits against applications running the QuickBlox SDK and API. 

  * We explain a number of unique attacks that could allow a threat actor to, for example, access smart intercoms and remotely open doors, or leak patient data from telemedicine applications. 

  * QuickBlox worked closely with Team82 and CPR to address our disclosure, and has fixed the vulnerabilities via a new secure architecture design and new API.

#### Table of Contents

  1. QuickBlox Architecture

  2. QuickBlox Vulnerabilities

  3. Impact

  4. Exploiting an Intercom IoT Platform: ROZCOM

  5. Controlling All the Intercoms

  6. Reviewing [REDACTED] Telemedicine Platform

  7. PII Leak en Masse

  8. Conclusion

## What is Quickblox Framework?

Real-time chat and video services available within telemedicine, finance, and smart IoT device applications used by millions of people, rely on the popular [QuickBlox framework](https://quickblox.com/). QuickBlox supplies mobile and web application developers with a SDK and APIs to deliver not only user management, real-time public and private chat features, for example, but also security features that ensure compliance with HIPAA and GDPR.

Claroty Team82, in collaboration with [Check Point Research (CPR)](https://research.checkpoint.com/), conducted a joint research project to look at the security of the QuickBlox SDK. Together, we uncovered a few major security vulnerabilities in the QuickBlox platform architecture that, if exploited, could allow threat actors to access tens of thousands of applications’ user databases and put millions of user records at risk.

![QuickBlox Features](/img/asset/YXNzZXRzL3F1aWNrYmxveC1mZWF0dXJlcy5wbmc/quickblox-features.png?fm=webp&fit=crop&s=9ca14a90cfff92ecb43b78ebd7ee6086) __ QuickBlox chat and video feature (Source: QuickBlox)

In this report, we will demonstrate exploits against multiple applications running the QuickBlox SDK under the hood, specifically against smart intercom and telemedicine applications. By chaining the vulnerabilities we identified with other flaws in the targeted applications, we found unique ways to carry out attacks that enabled us to remotely open doors via intercom applications, and also leak patient information from a major telemedicine platform. 

Team82 and CPR worked closely with QuickBlox to resolve all of the uncovered vulnerabilities. QuickBlox committed to the fix by designing a new, secure architecture and API, and urging its customers to migrate to the latest version. We would like to express our gratitude and appreciation.

## QuickBlox Architecture

QuickBlox is a chat and video calling platform for developing iOS, Android, and web applications. It provides an API for authentication, user management, chat, and messaging, file management, etc, and an easy-to-use SDK that enables voice and video features. Therefore, it’s no surprise we first encountered QuickBlox while researching a particular intercom mobile application that would rely on such a framework. This led us down the research rabbit hole into both the QuickBlox framework and various applications that use it.

Before we understand the vulnerabilities we uncovered in QuickBlox, we must understand how a developer integrates the framework into their application. First, developers must [create a QuickBlox account](https://admin.quickblox.com/signup). A new application is then created using the QuickBlox dashboard that will generate the following credentials for the application: 

  * Application ID

  * Authorization Key

  * Authorization Secret

  * Account Key

![QuickBlox Dashboard](/img/asset/YXNzZXRzL3F1aWNrYmxveC1kYXNoYm9hcmQucG5n/quickblox-dashboard.png?fm=webp&fit=crop&s=f9a0e375256d597266b89e226587f7e3) __ The QuickBlox account creation dashboard.

With these pieces of information, the application can [request](https://docs.quickblox.com/reference/create-session) a `QB-Token` that will be used in further API requests. The given token is an application-level token that has limited functionality.

![Requesting an application-level QB Token](/img/asset/YXNzZXRzL3F1aWNrYmxveC10b2tlbi1yZXF1ZXN0LnBuZw/quickblox-token-request.png?fm=webp&fit=crop&s=f0c1e89f35ad95d02fde33eb5c1fd462) __ Requesting an application-level QB Token via a /session.json API route

Once the application retrieves the `QB-Token`, it enables users to [log in](https://docs.quickblox.com/reference/log-in) on top of this session so the session will have the context of the logged-in user. This is done by providing both the application session and the user credentials. Now the session is fully authenticated and authorized with the user permissions.

However, this way of authentication exposes a major flaw: an application session is required to create a user session. This means that each user must obtain an application session, which requires knowledge of the application’s secrets, specifically the Application ID, Authorization Key, Authorization Secret, and Account Key. In order to make it technologically applicable, app developers had to make sure these secret keys are accessible to all users. When looking at applications using QuickBlox, we noticed that most of them chose to simply insert the application secrets into the application.

![Sample of application credentials from QuickBlox](/img/asset/YXNzZXRzL3NjcmVlbnNob3QtMjAyMy0wNy0wNS1hdC0xMS4wNS4wMi1hbS5wbmc/screenshot-2023-07-05-at-11.05.02-am.png?fm=webp&fit=crop&s=7a8b40178906c8ebf0bce493dc4ca4cd) __ A sample of application credentials from QuickBlox documentation.

When we first noticed that the official documentation guides customers to add secrets (`AUTH_KEY, AUTH_SECRET`) to their applications, we felt uneasy. It’s never a good idea to hide secret authentication tokens in applications because they are considered public information and can be easily extracted using various methods, from reverse engineering to dynamic analysis with [Frida](https://frida.re/).

## QuickBlox Vulnerabilities

Once we understood the QuickBlox architecture, we decided to look into the QuickBlox API and examine what we can access using “public” information: application secret keys. We discovered a few critical vulnerabilities in the QuickBlox API that could allow attackers to leak the user database from many popular applications.

By default, QuickBlox settings allow anyone with an application-level session to retrieve sensitive information such as:

  * Get a full list of all users using the `/users.json` API route

  * Get PII user information by ID using the `/ID.json` API route - including name, email, phone, etc

  * Create new users using the `/users.json`

This means that anyone who is able to extract the static QuickBlox settings from the application will be able to retrieve personal user information, below, of **all** application users, and also be able to create multiple attacker-controlled accounts.

![Obtained user information](/img/asset/YXNzZXRzL3F1aWNrYmxveF91c2VyLWluZm8ucG5n/quickblox_user-info.png?fm=webp&fit=crop&s=562cfa6204375d36987d31bf9fd4ab4f) __ Example of user information obtained from an application using QuickBlox.

Although the default API settings do allow all of the above (get the full list of users, retrieve user information, and create new users), application owners can limit the application-level API access using an inner-settings menu.

![QuickBlox user privacy settings](/img/asset/YXNzZXRzL3F1aWNrYmxveF9wcml2YWN5LnBuZw/quickblox_privacy.png?fm=webp&fit=crop&s=de1318faedbad6a92cc009583c10b79c) __ Available QuickBlox user privacy settings. 

While this does offer some mitigation to the vulnerabilities we discovered, we discovered another way of leaking the entire application database. By creating a rogue user account, it is possible for attackers to leak specific user information by accessing the `/ID.json`, where ID is the sequential user ID. Since QuickBlox uses sequential IDs, by simply brute-forcing a limited range, it is possible to leak all of an application’s user information. However, from a check we performed regarding this privacy setting on all of the applications we researched and retrieved the keys for, we discovered that only a handful chose to disable this API.

## Impact

To understand the full scope of the issue, we decided to explore what types of applications are using QuickBlox SDK and what would be the potential risk if attackers were to extract the secret tokens. Using various methods such as Google dorking, searches in [BeVigil](https://bevigil.com/), and other search engines we were able to find and extract QB tokens from dozens of different applications. Here’s a partial list:

![Quick Blox Redacted info](/img/asset/YXNzZXRzL3F1aWNrYmxveC1ibG9nLWdyYXBoaWNzLTAxLmpwZw/quickblox-blog-graphics-01.jpg?fm=webp&fit=crop&s=df83b7bff457a91036ffb08245caae1e) __

Extracting keys was not as simple as looking in the code. In some instances, the keys were encrypted, while in others, the code was heavily obfuscated. In some extreme cases they were dynamically received encrypted from a remote server. However, regardless of the application, any app would require the secret key and somehow use it with a QuickBlox server. Developers can only put in obstacles to complicate recovering the application key; which will always be accessible to attackers, whether it takes five minutes to extract or two hours.

After extracting the tokens from each application we tried to understand how attackers could leverage their attack based on the application’s capabilities and/or further vulnerabilities in the application platform. We found many interesting attack vectors; here we will explain two scenarios - Cloud-based Intercom solution and a Telemedicine app.  

## Exploiting an Intercom IoT Platform: ROZCOM

The first attack vector we’ll explore involves finding and exploiting vulnerabilities in a cloud-based IoT platform used to manage smart intercoms sold by Rozcom, an Israel-based vendor that sells intercoms for residential and commercial use cases. 

The company’s solutions include video intercoms that allow users to see who’s attempting to access a building or apartment that connects to Rozcom’s cloud-based management system via the QuickBlox platform. All of these connections and features can be accessed via Rozcom’s mobile application. 

We found multiple vulnerabilities in the Rozcom architecture that enabled us to download all user databases and perform full account takeover attacks. As a result, we were able to take over all Rozcom intercom devices, giving us full control and allowing us us to access device cameras and microphones, wiretap into its feed, open doors managed by the devices, and more.

Rozcom, for a year-and-a-half, ignored our attempts to privately disclose our findings with the [Israel National Cyber Directorate (INCD)](https://www.gov.il/en/Departments/faq/cve_advisories) acting as coordinator. INCD on May 4 allocated and published [CVE-2023-31184](https://www.gov.il/en/Departments/faq/cve_advisories), [CVE-2023-31185](https://www.gov.il/en/Departments/faq/cve_advisories) for the two vulnerabilities we uncovered.

### Rozcom Architecture

![Rozcom platform architecture](/img/asset/YXNzZXRzL3F1aWNrYmxveC1ibG9nLWdyYXBoaWNzLTAyLmpwZw/quickblox-blog-graphics-02.jpg?fm=webp&fit=crop&s=5cb4497227677ffc97da3367a235da1e) __ Rozcom platform architecture.

Rozcom uses many identifiers for its assets. First, each building has a unique 10-digit identification number (for example: 171XXXX708), used to differentiate between different buildings on the platform. Unlike build IDs, which are constructed from “random” numbers, users are identified using the following structure: BUILDING ID \+ PHONE NUMBER (for example: 171XXXX708 0501234567). This means that the user ID is actually constructed from two different identifiers that should be kept a secret.

Users can use the [Rozcom mobile application](https://play.google.com/store/apps/details?id=com.newlinks.intercomclient&hl=en&gl=US), below, to manage their personal intercom devices. Using the app they can open a door/gate, initiate a multimedia session with the device (stream video/audio, and do push-to-talk communication).

![Quick Blox Mobile](/img/asset/YXNzZXRzL3F1aWNrYmxveF9tb2JpbGUucG5n/quickblox_mobile.png?fm=webp&fit=crop&s=045325bd5963a112bcbe2ba649c9d106)

Behind the scenes, Rozcom is using the QuickBlox platform to handle multimedia sessions, transferring video/audio between the mobile app and the device.

As it turns out, Rozcom chose to use the user ID shown above as the user identifier in QuickBlox. And since we could leak the user database from QuickBlox we could get access to all of Rozcom users including Building IDs as well as the correlating users’ phone numbers.

![Rozcom User ID](/img/asset/YXNzZXRzL3F1aWNrYmxveF9yb3otdXNlcmlkLnBuZw/quickblox_roz-userid.png?fm=webp&fit=crop&s=2f25bf7ba8d41fc765c50560bae76695) __ An example of a QuickBlox user, containing the Rozcom User ID (building ID + phone number)

## Controlling All the Intercoms

Our next step was to look at Rozcom’s applications and cloud APIs in order to better understand the possible attack vector using the identifiers we leaked.

The first API we discovered allowed us to retrieve information about a building managed by Rozcom, by supplying the Building ID. By accessing the following API: `getbuildingdetailpublic?buildingId=BUILDING_ID`, we could return each building’s full address as well as the number of apartments in that building, below.

![Quick Blox Apartments](/img/asset/YXNzZXRzL3F1aWNrYmxveF9hcGFydG1lbnRzLnBuZw/quickblox_apartments.png?fm=webp&fit=crop&s=9b51251cedda9f7982b8c9028010c735) __

Next, we wanted to see if we could impersonate a user. By using the application, we noticed that users can access their account by entering their phone number and receiving a one-time password as an SMS message as an authenticator.

![Rozcom login form](/img/asset/YXNzZXRzL3F1aWNrYmxveF9yb3otbG9naW4ucG5n/quickblox_roz-login.png?fm=webp&fit=crop&s=8be0125140cbbcde8a1bb35cd053a636) __ The Rozcom login form. 

However, we discovered that this so-called OTP is actually not so one-time. Instead the same OTP token is maintained throughout every session. Users don’t usually notice this because they are only required to enter it during initial login, and the application saves the token behind the scenes. Then, using the user ID and the OTP, users authenticate to the application.

Furthermore, by reverse engineering the mobile application, we discovered another API route that could be used by attackers to leak the OTP token. By calling Rozcom’s API with the following function: `gettenantauth?cellular=PHONE_NUMBER`, the backend server returns the user’s OTP token.

![Rozcom API user's authcode](/img/asset/YXNzZXRzL3F1aWNrYmxveF9hdXRoY29kZS5wbmc/quickblox_authcode.png?fm=webp&fit=crop&s=d6d0ac6c7e09c923ca535f2691f93804) __ The Rozcom API result returning a user's authcode.

This means that the only requirement to retrieve a user’s credentials is their phone number, which we managed to leak using the QuickBlox vulnerability. Moreover, the authentication code is static. Therefore, attackers can easily login on behalf of any user and use the application’s functionality to its extent. This allows them to open the door/gate, open video streams and more; they now fully control the intercom device remotely.

![Quck Blox remote access](/img/asset/YXNzZXRzL3F1aWNrYmxveF9yZW1vdGUtYWNjZXNzLnBuZw/quickblox_remote-access.png?fm=webp&fit=crop&s=e3e2ef8f6ec8c284c2d576d0ab873ca5) __ Remote access to a Rozcom intercom’s video feed.

## Reviewing [REDACTED] Telemedicine Platform

Telemedicine is the distribution of health-related services and information via electronic information and telecommunication technologies. It allows long-distance patient and clinician contact, care, advice, reminders, education, intervention, monitoring, and remote admissions.

We chose to look at a popular telemedicine application integrated with the QuickBlox SDK, in order to explore its attack surface by abusing the QuickBlox vulnerabilities described above. We are not disclosing the name of the app because it has yet to update to the new QuickBlox API and remains vulnerable at the time of publication. 

This particular telemedicine platform provides chat and video services enabling patients to communicate with doctors. By combining the QuickBlox vulnerabilities alongside the specific telemedicine app vulnerabilities, we were able to leak all of its user database, along with related medical records and history stored in the application.

## PII Leak en Masse

While researching the affected Android application, we were able to extract the embedded QuickBlox application keys. We could then authenticate to the QuickBlox API server, get an authentication token and obtain a user database for the application. These steps are not different from any other application that uses QuickBlox. However, here we are talking about patient and physician information, below.

![Quick blox placeholder text](/img/asset/YXNzZXRzL3F1aWNrYmxveC1ibG9nLWdyYXBoaWNzLTA1LSgxKS0xNjg5MTY3Mzk5LnBuZw/quickblox-blog-graphics-05-%281%29-1689167399.png?fm=webp&fit=crop&s=fbe853f2464479d32ce52493e991316d) __

In this telemedicine app, each user chooses their UserID and Password credentials used by the application. However, we discovered through reverse-engineering that the [REDACTED] application creates a new QuickBlox user with their UserID as login and a hard-coded static password ([REDACTED] for patients, and [REDACTED] for doctors).

This makes it possible to login in QuickBlox on behalf of any user—doctor or patient—and view all of their data. This includes:

  * Personal information

  * Medical history

  * Chat history

  * Medical record files

![Successful Quick Blox exploit PII](/img/asset/YXNzZXRzL3F1aWNrYmxveC1ibG9nLWdyYXBoaWNzLTA0LnBuZw/quickblox-blog-graphics-04.png?fm=webp&fit=crop&s=066633352a3bc5e9d569c43e4a78daf5) __ A successful exploit can allow an attacker to steal chat history, and other personal data. 

Furthermore, because full impersonation is possible by this attack, anyone can impersonate a doctor and modify information or even communicate in real time via chat and video with real patients on the platform on behalf of an actual physician. This is a very scary scenario.

![An attacker may inject themselves in video telemedicine calls](/img/asset/YXNzZXRzL3F1aWNrYmxveC1ibG9nLWdyYXBoaWNzLTAzLTE2ODg1NzA3OTMuanBn/quickblox-blog-graphics-03-1688570793.jpg?fm=webp&fit=crop&s=11b5eff30a7a685d21903533100382c8) __ An attacker may inject themselves in video telemedicine calls between doctors and patients. 

## Conclusion

Team82 and Check Point Research collaborated on this extensive look at the QuickBlox API, which is prominent in many chat and video applications used by millions of people across different industries. Together, we were able to uncover vulnerabilities in the QuickBlox platform architecture that could be exploited to allow attackers access to applications’ user databases. Millions of user records were at risk because of these vulnerabilities.

Our joint research led to a number of proof-of-concept exploits against applications running the affected API. We demonstrated how the combination of secret tokens and passwords embedded in the application and usage of an insecure QuickBlox API design could allow attackers to obtain a great amount of information about the end-users. 

We worked closely with QuickBlox to remediate the issues. QuickBlox responded to our disclosure by designing a new secure architecture for its platform, and a new API. Its customers have been urged to migrate to the latest versions of both. Again, we thank QuickBlox for its cooperation and quick response to ensure these vulnerabilities were addressed and its users privacy and security ensured.

Share

[ __ LinkedIn ](https://www.linkedin.com/shareArticle/?url=https://claroty.com/team82/research/major-security-flaws-in-popular-quickblox-chat-and-video-framework-expose-sensitive-data-of-millions) [ __ Twitter ](https://twitter.com/intent/post?text=Major Security Flaws in Popular QuickBlox Chat And Video Framework Expose Sensitive Data Of Millions&url=https://claroty.com/team82/research/major-security-flaws-in-popular-quickblox-chat-and-video-framework-expose-sensitive-data-of-millions) [ __ Facebook ](https://www.facebook.com/sharer/sharer.php?u=https://claroty.com/team82/research/major-security-flaws-in-popular-quickblox-chat-and-video-framework-expose-sensitive-data-of-millions) [ __ ](mailto:?subject=Major Security Flaws in Popular QuickBlox Chat And Video Framework Expose Sensitive Data Of Millions&body=https://claroty.com/team82/research/major-security-flaws-in-popular-quickblox-chat-and-video-framework-expose-sensitive-data-of-millions)

### Itay Cohen

Research Lead

Check Point Research (CPR)

### Oleg Ilushin

Security researcher

Check Point Research (CPR)

![](https://claroty.com/build/assets/team82-newsletter-bg-BlXIsUMi.jpg)

Stay in the know Get the Team82 Newsletter

Share

[ __ LinkedIn ](https://www.linkedin.com/shareArticle/?url=https://claroty.com/team82/research/major-security-flaws-in-popular-quickblox-chat-and-video-framework-expose-sensitive-data-of-millions) [ __ Twitter ](https://twitter.com/intent/post?text=Major Security Flaws in Popular QuickBlox Chat And Video Framework Expose Sensitive Data Of Millions&url=https://claroty.com/team82/research/major-security-flaws-in-popular-quickblox-chat-and-video-framework-expose-sensitive-data-of-millions) [ __ Facebook ](https://www.facebook.com/sharer/sharer.php?u=https://claroty.com/team82/research/major-security-flaws-in-popular-quickblox-chat-and-video-framework-expose-sensitive-data-of-millions) [ __ ](mailto:?subject=Major Security Flaws in Popular QuickBlox Chat And Video Framework Expose Sensitive Data Of Millions&body=https://claroty.com/team82/research/major-security-flaws-in-popular-quickblox-chat-and-video-framework-expose-sensitive-data-of-millions)

Related Vulnerability Disclosures

  * ##### [CVE-2023-31184 CWE-798: Use of Hard-coded Credentials Misconfiguration may allow information disclosure via an unspecified request. CVSS v3: 8.0 ](/team82/disclosure-dashboard/cve-2023-31184)
  * ##### [CVE-2023-31185 Misconfiguration may allow information disclosure via an unspecified request. CVSS v3: 8.0 ](/team82/disclosure-dashboard/cve-2023-31185)

Solutions

  * [Claroty xDome Platform](/platform)
  * [Industrial Cybersecurity](/industrial-cybersecurity)
  * [Healthcare Cybersecurity](/healthcare-cybersecurity)
  * [Commercial Cybersecurity](/commercial-cybersecurity)
  * [Public Sector Cybersecurity](/public-sector-cybersecurity)

Threat Research

  * [Team82 Home](/team82)
  * [Vulnerability Disclosure Dashboard](/team82/disclosure-dashboard)
  * [Research](/team82/research)
  * [PGP Key](/team82/pgp-key)

Partners

  * [Partners](/partners)
  * [Technology Alliance Partners](/partners/technology-alliances)
  * [Channel Partners](/partners/channel-partners)
  * [Become a Partner](https://portal.claroty.com/#/page/partner-reg)
  * [Partner Login](https://portal.claroty.com/#/page/login)

Resources

  * [Resource Library](/resources)
  * [Blog](/blog)
  * [White Papers](/resources/white-papers)
  * [Reports](/resources/reports)
  * [Case Studies](/resources/case-studies)
  * [Datasheets](/resources/datasheets)
  * [Integration Briefs](/resources/integration-briefs)
  * [Videos](https://www.youtube.com/@claroty20)
  * [Claroty Nexus](https://nexusconnect.io)

Company

  * [About Us](/company)
  * [Careers](/careers)
  * [Leadership](/leadership)
  * [Newsroom](/newsroom)
  * [xCel Enablement & Training](/xcel-enablement-and-training)
  * [Trust Center](/trust)
  * [Customer Experience](/customer-experience)
  * [Events](/event-listing)
  * [Environmental, Social, and Governance Policies](/environmental-social-and-governance-policies)
  * [Contact Us](/contact-us)

[ ![Claroty](https://claroty.com/build/assets/logo-white-VeF9EwMy.svg) ](/)

© 2026 Claroty. All rights reserved.

[ __ LinkedIn ](https://www.linkedin.com/company/claroty/) [ __ Twitter ](https://twitter.com/claroty) [ __ YouTube ](https://www.youtube.com/@claroty20) [ __ Facebook ](https://www.facebook.com/ClarotyOT/)

[Terms & Conditions](/terms-conditions) / [Privacy Policy](/privacy-policy)

__ Close Modal ![QuickBlox Features](/img/asset/YXNzZXRzL3F1aWNrYmxveC1mZWF0dXJlcy5wbmc/quickblox-features.png?fm=webp&fit=crop&s=9ca14a90cfff92ecb43b78ebd7ee6086)

__ Close Modal ![QuickBlox Dashboard](/img/asset/YXNzZXRzL3F1aWNrYmxveC1kYXNoYm9hcmQucG5n/quickblox-dashboard.png?fm=webp&fit=crop&s=f9a0e375256d597266b89e226587f7e3)

__ Close Modal ![Requesting an application-level QB Token](/img/asset/YXNzZXRzL3F1aWNrYmxveC10b2tlbi1yZXF1ZXN0LnBuZw/quickblox-token-request.png?fm=webp&fit=crop&s=f0c1e89f35ad95d02fde33eb5c1fd462)

__ Close Modal ![Sample of application credentials from QuickBlox](/img/asset/YXNzZXRzL3NjcmVlbnNob3QtMjAyMy0wNy0wNS1hdC0xMS4wNS4wMi1hbS5wbmc/screenshot-2023-07-05-at-11.05.02-am.png?fm=webp&fit=crop&s=7a8b40178906c8ebf0bce493dc4ca4cd)

__ Close Modal ![Obtained user information](/img/asset/YXNzZXRzL3F1aWNrYmxveF91c2VyLWluZm8ucG5n/quickblox_user-info.png?fm=webp&fit=crop&s=562cfa6204375d36987d31bf9fd4ab4f)

__ Close Modal ![QuickBlox user privacy settings](/img/asset/YXNzZXRzL3F1aWNrYmxveF9wcml2YWN5LnBuZw/quickblox_privacy.png?fm=webp&fit=crop&s=de1318faedbad6a92cc009583c10b79c)

__ Close Modal ![Quick Blox Redacted info](/img/asset/YXNzZXRzL3F1aWNrYmxveC1ibG9nLWdyYXBoaWNzLTAxLmpwZw/quickblox-blog-graphics-01.jpg?fm=webp&fit=crop&s=df83b7bff457a91036ffb08245caae1e)

__ Close Modal ![Rozcom platform architecture](/img/asset/YXNzZXRzL3F1aWNrYmxveC1ibG9nLWdyYXBoaWNzLTAyLmpwZw/quickblox-blog-graphics-02.jpg?fm=webp&fit=crop&s=5cb4497227677ffc97da3367a235da1e)

__ Close Modal ![Rozcom User ID](/img/asset/YXNzZXRzL3F1aWNrYmxveF9yb3otdXNlcmlkLnBuZw/quickblox_roz-userid.png?fm=webp&fit=crop&s=2f25bf7ba8d41fc765c50560bae76695)

__ Close Modal ![Quick Blox Apartments](/img/asset/YXNzZXRzL3F1aWNrYmxveF9hcGFydG1lbnRzLnBuZw/quickblox_apartments.png?fm=webp&fit=crop&s=9b51251cedda9f7982b8c9028010c735)

__ Close Modal ![Rozcom login form](/img/asset/YXNzZXRzL3F1aWNrYmxveF9yb3otbG9naW4ucG5n/quickblox_roz-login.png?fm=webp&fit=crop&s=8be0125140cbbcde8a1bb35cd053a636)

__ Close Modal ![Rozcom API user's authcode](/img/asset/YXNzZXRzL3F1aWNrYmxveF9hdXRoY29kZS5wbmc/quickblox_authcode.png?fm=webp&fit=crop&s=d6d0ac6c7e09c923ca535f2691f93804)

__ Close Modal ![Quck Blox remote access](/img/asset/YXNzZXRzL3F1aWNrYmxveF9yZW1vdGUtYWNjZXNzLnBuZw/quickblox_remote-access.png?fm=webp&fit=crop&s=e3e2ef8f6ec8c284c2d576d0ab873ca5)

__ Close Modal ![Quick blox placeholder text](/img/asset/YXNzZXRzL3F1aWNrYmxveC1ibG9nLWdyYXBoaWNzLTA1LSgxKS0xNjg5MTY3Mzk5LnBuZw/quickblox-blog-graphics-05-%281%29-1689167399.png?fm=webp&fit=crop&s=fbe853f2464479d32ce52493e991316d)

__ Close Modal ![Successful Quick Blox exploit PII](/img/asset/YXNzZXRzL3F1aWNrYmxveC1ibG9nLWdyYXBoaWNzLTA0LnBuZw/quickblox-blog-graphics-04.png?fm=webp&fit=crop&s=066633352a3bc5e9d569c43e4a78daf5)

__ Close Modal ![An attacker may inject themselves in video telemedicine calls](/img/asset/YXNzZXRzL3F1aWNrYmxveC1ibG9nLWdyYXBoaWNzLTAzLTE2ODg1NzA3OTMuanBn/quickblox-blog-graphics-03-1688570793.jpg?fm=webp&fit=crop&s=11b5eff30a7a685d21903533100382c8)

![Claroty](https://claroty.com/build/assets/logo-white-VeF9EwMy.svg) __ Close Menu

  * [Platform](/platform) __

[The Claroty Platform](/platform) [Claroty CPS Protection Program](/cps-protection-program) [Claire, the AI Security Agent](/claire) [Asset Inventory](/platform/asset-inventory) [Exposure Management](/platform/exposure-management) [Network Protection](/platform/network-protection) [Secure Access](/platform/secure-access) [Threat Detection](/platform/threat-detection) [Operational Efficiency](/platform/operational-efficiency) [Integrations](/platform/integrations)

  * [Industries]() __

[Industrial Home](/industrial-cybersecurity) [Industrial Verticals](/industrial-cybersecurity/verticals) [Healthcare Home](/healthcare-cybersecurity) [Commercial Home](/commercial-cybersecurity) [Commercial Verticals](/commercial-cybersecurity/verticals)

  * [Public Sector](/public-sector-cybersecurity) __

[Public Sector Home](/public-sector-cybersecurity) [Federal Government Home](/public-sector-cybersecurity/us-government-cybersecurity) [SLED Home](/public-sector-cybersecurity/sled-government-cybersecurity)

  * [Customers](/customer-experience) __

[Customer Experience](/customer-experience) [Case Studies](/resources/case-studies) [xCel Enablement & Training for Customers](/xcel-enablement-and-training-for-customers)

  * [Partners](/partners) __

[Partners](/partners) [Technology Alliance Partners](/partners/technology-alliances) [Channel Partners](/partners/channel-partners) [Partner Login](https://portal.claroty.com/#/page/login)

  * [Threat Research](/team82) __

[Team82 Home](/team82) [Threat Intelligence](/threat-intelligence) [Vulnerability Disclosure Dashboard](/team82/disclosure-dashboard) [Research](/team82/research) [Talks](/team82/talks) [PGP Key](/team82/pgp-key)

  * [Resources](/resources) __

[Blog](/blog) [Reports](/resources/reports) [White Papers](/resources/white-papers) [Datasheets & Solution Overviews](/resources/datasheets) [Integration Briefs](/resources/integration-briefs) [Case Studies](/resources/case-studies) [On-Demand Webinars](/resources/webinars) [Visit our Nexus Website](https://nexusconnect.io)

  * [Company](/company) __

[About Us](/company) [Careers](/careers) [Leadership](/leadership) [Newsroom](/newsroom) [xCel Enablement & Training](/xcel-enablement-and-training) [Trust Center](/trust) [Events](/event-listing) [Environmental, Social, and Governance Policies](/environmental-social-and-governance-policies) [Contact Us](/contact-us)

  * [__Search](/search)

[ __ LinkedIn ](https://www.linkedin.com/company/claroty/) [ __ Twitter ](https://twitter.com/claroty) [ __ YouTube ](https://www.youtube.com/@claroty20) [ __ Facebook ](https://www.facebook.com/ClarotyOT/)
