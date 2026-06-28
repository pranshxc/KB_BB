---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-03-06_insecure-toyota-crm-exposed-mexican-customer-information.md
original_filename: 2023-03-06_insecure-toyota-crm-exposed-mexican-customer-information.md
title: Insecure Toyota CRM exposed Mexican customer information
category: documents
detected_topics:
- api-security
- command-injection
- otp
- supply-chain
tags:
- imported
- documents
- api-security
- command-injection
- otp
- supply-chain
language: en
raw_sha256: 74c803815a8da49bfcd2cdc21af8fad3ab5fcd26a7f4b381405d492b2e8e5ea6
text_sha256: 14fd4ec71970be83040c68a7c0870df6073c2cd2205ce453a3147987fdf63d2b
ingested_at: '2026-06-28T07:32:19Z'
sensitivity: unknown
redactions_applied: false
---

# Insecure Toyota CRM exposed Mexican customer information

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-03-06_insecure-toyota-crm-exposed-mexican-customer-information.md
- Source Type: markdown
- Detected Topics: api-security, command-injection, otp, supply-chain
- Ingested At: 2026-06-28T07:32:19Z
- Redactions Applied: False
- Raw SHA256: `74c803815a8da49bfcd2cdc21af8fad3ab5fcd26a7f4b381405d492b2e8e5ea6`
- Text SHA256: `14fd4ec71970be83040c68a7c0870df6073c2cd2205ce453a3147987fdf63d2b`


## Content

---
title: "Insecure Toyota CRM exposed Mexican customer information"
url: "https://eaton-works.com/2023/03/06/toyota-c360-hack/"
final_url: "https://eaton-works.com/2023/03/06/toyota-c360-hack/"
authors: ["Eaton Z. (@XeEaton)"]
programs: ["Toyota"]
bugs: ["Authentication bypass"]
publication_date: "2023-03-06"
added_date: "2023-03-08"
source: "pentester.land/writeups.json"
original_index: 1420
---

# Insecure Toyota CRM exposed Mexican customer information

![](/assets/images/ew-logo-4circle-48.png?cb=64e21a35) Eaton • Mar 6, 2023

Copy Link Share 

**News coverage:**

  * [Automotive News](https://www.autonews.com/mobility-report/hacker-accessed-toyotas-mexican-customers-information) ([Front page screenshot – March 8, 2023](https://eaton-works.com/cdn-cgi/imagedelivery/VwwCqBIYNXeyNQwEQ8uyVQ/6d77c60d-c771-4eb2-55e8-b35de1896300/full)) 
  * Also featured in: [Auto industry risks security breaches by underpaying white hat hackers](https://www.autonews.com/mobility-report/automakers-risk-cyberattacks-paying-white-hat-hackers-less)
  * [Jalopnik](https://jalopnik.com/automakers-dont-want-to-pay-hacker-bounties-and-your-ca-1850202032)

## **Key Points / Summary**

  * I broke into Toyota’s C360 CRM, a web app used by Toyota to manage Mexican customers. It was possible to bypass the corporate login screen by modifying the app.
  * Production data was accessible by modifying the dev app to use the production API instead of the dev API.
  * Production API that returned customer information was exposed via loading spinner settings and had no authentication.
  * Data access achieved: name, address, phone number, email address, tax ID, and vehicle/service/ownership history for an unknown number of Toyota customers residing in Mexico.
  * Issue was responsibly disclosed to Toyota in October 2022 and fixed in a timely manner.

[The GSPIMS hack I disclosed last month](https://eaton-works.com/2023/02/06/toyota-gspims-hack/) exposed a wealth of corporate data, but no customer data. In today’s writeup I am detailing the discovery of a Toyota CRM issue that left Mexican Toyota customer information exposed.

## **Toyota C360 CRM**

![](https://eaton-works.com/cdn-cgi/imagedelivery/VwwCqBIYNXeyNQwEQ8uyVQ/6af8065b-2ac5-4689-b3a8-d3ad484c6900/full)

Toyota maintains a “Customer 360” CRM. [This page](https://www.precisely.com/glossary/customer-360) has a good definition of what that means: 

_Customer 360 refers to the creation of a master customer record by aggregating all data about that customer from across the organization. Customer 360 provides a trusted, single view of a customer’s name, address, contact information, gender, and interactions with a business. The view can include information about purchase history, billing, service issues, social presence, and channel preferences. Businesses can use this data to inform engagement strategies, customer journey steps, communications, personalized offers, and deliveries. A Customer 360 view enables organizations to derive value, achieve sustainable competitive advantage, and maximize new customer acquisition opportunities whether in-store or online._

In this case it’s simply an [Angular](https://angular.io/) single-page-application intended to manage Toyota Mexico customers. According to comments in the code, it was also used to manage US customers at one point. US customers are presumably managed in a different CRM now.

![](https://eaton-works.com/cdn-cgi/imagedelivery/VwwCqBIYNXeyNQwEQ8uyVQ/82105197-a589-4c7e-fc84-0df5a8b8dd00/full)

There were a few different versions of the CRM – 3 development/testing versions and 1 production version:

  1. <https://c360.dev.customercentral.toyota.com/>
  2. <https://c360.qa.customercentral.toyota.com/>
  3. <https://www.devapp.customercentral.toyota.com/>
  4. <https://c360.customercentral.toyota.com/>

At the time of writing, Toyota has taken all but site #1 offline.

## **Bypassing the login**

When the production site (#4) was active, it would return a 403 error when you visited it. There was no way around it.

![](https://eaton-works.com/cdn-cgi/imagedelivery/VwwCqBIYNXeyNQwEQ8uyVQ/2ba274b2-74b2-40c7-c9c9-91bbbaead800/full)

Undeterred, I discovered the development/testing versions of the site and decided to investigate those instead, and found that instead of returning a 403 error, it would ask for corporate login credentials:

![](https://eaton-works.com/cdn-cgi/imagedelivery/VwwCqBIYNXeyNQwEQ8uyVQ/3ea261ea-77f7-43a1-2b13-cda074b44f00/full)

The Angular JavaScript code initiates this redirect, so the first goal was to stop that from occurring. A few patches do the job nicely:

![](https://eaton-works.com/cdn-cgi/imagedelivery/VwwCqBIYNXeyNQwEQ8uyVQ/804503a8-69e9-479e-a079-2fc719f72600/full)_Stop the login redirect in main.js._ ![](https://eaton-works.com/cdn-cgi/imagedelivery/VwwCqBIYNXeyNQwEQ8uyVQ/2fba95ef-63e8-4bb7-cf38-fe41d771f300/full)_Return an empty, non-null account object in vendor.js to avoid errors and trick the app into thinking an account is logged in._

The homepage then loads:

![](https://eaton-works.com/cdn-cgi/imagedelivery/VwwCqBIYNXeyNQwEQ8uyVQ/e71c9cfc-1d7e-4635-d49f-d17077d69900/full)

## **Accessing production data**

As stated previously, the production app is locked behind a 403 error. After analyzing the dev app, I managed to locate the dev, qa, and production API endpoints:

![](https://eaton-works.com/cdn-cgi/imagedelivery/VwwCqBIYNXeyNQwEQ8uyVQ/e95c7d61-c47c-4b59-e53d-516f793b5f00/full)_Secret API endpoints exposed via loading spinner settings, of all things._

The dev app I am working on is using the dev API, but it is trivial to update it to use the production API:

![](https://eaton-works.com/cdn-cgi/imagedelivery/VwwCqBIYNXeyNQwEQ8uyVQ/d688d4d7-0a82-445e-f1eb-61ffad6dde00/full)

It’s worth noting that these APIs did not require an authentication token. They would return data to anyone who sent a well-formed request. The access token is saved to [session storage](https://developer.mozilla.org/en-US/docs/Web/API/Window/sessionStorage), but it wasn’t actually used anywhere.

Toyota likely believed no one would find the production API endpoint since the production app was locked down, but it looks like their developers included it in the dev app. The API endpoints were included because [ngx-ui-loader](https://tdev.app/ngx-ui-loader) is used to enhance the loading experience in the app, and they excluded the API paths to avoid problems. There is nothing wrong with enhancing an app’s loading experience, but in this case, they accidentally exposed all their secret API endpoints across all environments.

The production and qa API endpoints use Amazon API Gateway and probably would have been impossible to find if they weren’t included in the dev app’s code.

With the login bypass and API change in place, it was possible to access production data.

## **Exploring the impact**

The “C360 Profile” page is where all the interesting stuff is. It is basically a lookup tool where you can search for customers. Searching for customers yields a lot of results when you put in a common name (note the scrollbar):

![](https://eaton-works.com/cdn-cgi/imagedelivery/VwwCqBIYNXeyNQwEQ8uyVQ/21317c7c-1bff-4244-c219-b6af7ff2fc00/full)

Clicking on a customer shows all their information and service history:

![](https://eaton-works.com/cdn-cgi/imagedelivery/VwwCqBIYNXeyNQwEQ8uyVQ/23d7fee8-acb2-4b26-a9dd-292b92ef2400/full) ![](https://eaton-works.com/cdn-cgi/imagedelivery/VwwCqBIYNXeyNQwEQ8uyVQ/7fa0e721-fe6d-40ac-8155-eff9c3267300/full)

That is basically everything that is interesting. This app is still in development and some sections are glitchy or unavailable. For example, the same service history was often duplicated across customers.

I would like to stress that **I do not know how many customers are in this CRM**. There wasn’t a user list – it was only possible to search for customers by name, ID, phone number, or email address.

The customer information appears to sync with [Dealer Daily](https://www.computerworld.com/article/2576666/dealer-daily--toyota-s-communication-pipeline.html), which is the central system Toyota (and Lexus) dealers use to manage their business with Toyota.

## **Reporting to Toyota**

The issue was reported to Toyota on October 30, 2022, and they responded later that same day confirming they received the report. On November 18, 2022, they confirmed the issue was remediated. I then informed them I would publish my writeup after the industry standard 90-day period has passed.

Toyota fixed the issue by taking some of the sites offline and updating the APIs to require an authentication token.

Basically a day after I reported the issue to Toyota, they took all the sites offline. I was impressed by how quickly they reacted. They likely spent the next few weeks making necessary security improvements and ensuring no one maliciously accessed any customer information. Toyota did not publish their own advisory regarding this issue, so it’s likely no malicious access was found.

There was no reward for this disclosure. Toyota currently does not offer rewards for security reports.

This is my last planned Toyota writeup for now, but who knows what the future holds! ~~PS: If you/your company’s security team are currently hiring, feel free to[say hello](https://eaton-works.com/contact/)🙂.~~
