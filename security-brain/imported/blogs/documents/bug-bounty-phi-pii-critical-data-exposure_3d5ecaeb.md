---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-08-01_bug-bounty-phipii-critical-data-exposure.md
original_filename: 2021-08-01_bug-bounty-phipii-critical-data-exposure.md
title: Bug bounty - PHI/PII critical data exposure
category: documents
detected_topics:
- command-injection
- information-disclosure
- api-security
tags:
- imported
- documents
- command-injection
- information-disclosure
- api-security
language: en
raw_sha256: 3d5ecaeb5e5df29ebcd1701e8500d59a8f5052360051ffed7a0a8760323e06ed
text_sha256: 1d86b3d16eef5b7390a23bb38ab5ffba2547488f9a7c88ced8dbb8f23157022d
ingested_at: '2026-06-28T07:32:07Z'
sensitivity: unknown
redactions_applied: false
---

# Bug bounty - PHI/PII critical data exposure

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-08-01_bug-bounty-phipii-critical-data-exposure.md
- Source Type: markdown
- Detected Topics: command-injection, information-disclosure, api-security
- Ingested At: 2026-06-28T07:32:07Z
- Redactions Applied: False
- Raw SHA256: `3d5ecaeb5e5df29ebcd1701e8500d59a8f5052360051ffed7a0a8760323e06ed`
- Text SHA256: `1d86b3d16eef5b7390a23bb38ab5ffba2547488f9a7c88ced8dbb8f23157022d`


## Content

---
title: "Bug bounty - PHI/PII critical data exposure"
page_title: "CyberIntruder | Blog"
url: "https://molx32.github.io/blog/2021/Bug-bounty-00/"
final_url: "https://cyber-intruder.com/blog/2021/Bug-bounty-00/"
authors: ["Molx32"]
bugs: ["Information disclosure"]
bounty: "150"
publication_date: "2021-08-01"
added_date: "2023-04-27"
source: "pentester.land/writeups.json"
original_index: 3452
---

## About the company

This is one of my first bug bounty finding, and at this time I didn’t want to spend weeks on famous bug bounty programs, and I wasn’t looking for rewards. So I decided to look for a program not registered on famous bug bounty platforms so I could get a better chance to find something.

After some Google dorking, I found a SaaS application that provides simple service. Imagine being a hair salon manager : you could use this SaaS app to create virtual waiting lists where your customers can register and give some information such as “I want to change my hair color”. Altough it may be obvious, it is important to note that those waiting lists are public, so that anyone can register on the waiting list.

The scope of this program was the following :

  * company.com
  * v2.company.com
  * api.company.com
  * app.company.com

#### Data exposure

I started using the SaaS app as a business owner to understand how this waiting list system works. After publishing and playing with my first waiting list, I could understand how simple this system is. A waiting list looks like this : you can see your position in the waiting list, and you can register.

![](/assets/img/bug_bounty_01.png)

When clicking on the register button, the business owner invites you to provide some information, and after sending the form, you are added to the waitling list.

![](/assets/img/bug_bounty_02.png)

But still, I was surprised to see that, as an anonymous user, I could see names of the previous and next persons waiting. So I didn’t even fire Burp Suite, but I used Firefox developper tools to check how the list of waiting people was retrieved. I quickly identified that a subsequent request was sent to the API **https://api.company.com/v2/public/visits/nameofmywaitinglist?limit=200**. This API returns a JSON object with the list of the 200 first people waiting, and exposes all the information those people provided on the registering page.

In my case, this was not real data, so I searched for real waiting lists. This was simple since all my waiting lists were hosted at **https://company.com/l/nameofmywaitinglist**. So I used Google dorking to retrieve some public waiting lists : **site:company.com inurl:/l/**. And here is the most interesting data I found for a lot of them :

  * First name
  * Last name
  * Address
  * Phone number

The severity of this data exposure entirely depends on the business sensitivity : for example, I was able to retrieve many health information for health institutions that required patients to provide personnal health information.

#### Feedback and mitigation

I reported the issue, and within 2 business days I had a positive answer for a 150$ reward.

A few weeks later, a new version was released and now allows business owners to encrypt fields of the registration form. To me, this is not a true solution, because APIs are still very talkative, and business owners often don’t encrypt sensitive data.

Hope this was interesting!
