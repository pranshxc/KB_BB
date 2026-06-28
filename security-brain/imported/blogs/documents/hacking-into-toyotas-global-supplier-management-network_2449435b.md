---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-02-06_hacking-into-toyotas-global-supplier-management-network.md
original_filename: 2023-02-06_hacking-into-toyotas-global-supplier-management-network.md
title: Hacking into Toyota’s global supplier management network
category: documents
detected_topics:
- api-security
- jwt
- sso
- command-injection
- mfa
- otp
tags:
- imported
- documents
- api-security
- jwt
- sso
- command-injection
- mfa
- otp
language: en
raw_sha256: 2449435bf7c0cb8e6dd0a238356b580d5a00cb3d8e1e9065ebcd74deaf7a051e
text_sha256: 63b742c509e7415dd3482846debb4edf5b2dba333aa1f30d50df7928e0ba544d
ingested_at: '2026-06-28T07:32:18Z'
sensitivity: unknown
redactions_applied: false
---

# Hacking into Toyota’s global supplier management network

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-02-06_hacking-into-toyotas-global-supplier-management-network.md
- Source Type: markdown
- Detected Topics: api-security, jwt, sso, command-injection, mfa, otp
- Ingested At: 2026-06-28T07:32:18Z
- Redactions Applied: False
- Raw SHA256: `2449435bf7c0cb8e6dd0a238356b580d5a00cb3d8e1e9065ebcd74deaf7a051e`
- Text SHA256: `63b742c509e7415dd3482846debb4edf5b2dba333aa1f30d50df7928e0ba544d`


## Content

---
title: "Hacking into Toyota’s global supplier management network"
url: "https://eaton-works.com/2023/02/06/toyota-gspims-hack/"
final_url: "https://eaton-works.com/2023/02/06/toyota-gspims-hack/"
authors: ["Eaton Z. (@XeEaton)"]
programs: ["Toyota"]
bugs: ["Authentication bypass", "Backdoor"]
publication_date: "2023-02-06"
added_date: "2023-02-16"
source: "pentester.land/writeups.json"
original_index: 1570
---

# Hacking into Toyota’s global supplier management network

![](/assets/images/ew-logo-4circle-48.png?cb=64e21a35) Eaton • Feb 6, 2023

Copy Link Share 

**Discussion links:** [X](https://x.com/XeEaton/status/1622636229362696192) | [Reddit](https://www.reddit.com/r/netsec/comments/10vb5qy/hacking_into_toyotas_global_supplier_management/)

**News coverage:**

  * [Automotive News](https://www.autonews.com/mobility-report/how-toyotas-supplier-portal-got-hacked) ([Front page screenshot – February 8, 2023](https://eaton-works.com/cdn-cgi/imagedelivery/VwwCqBIYNXeyNQwEQ8uyVQ/5123980a-3bc3-4a5e-e109-760bdb6ff000/full)) 
  * Also featured in: [Auto industry risks security breaches by underpaying white hat hackers](https://www.autonews.com/mobility-report/automakers-risk-cyberattacks-paying-white-hat-hackers-less)
  * [Autoblog](https://www.autoblog.com/2023/02/08/white-hat-hacker-toyota-supplier-portal/)
  * [PortSwigger](https://portswigger.net/daily-swig/toyota-sealed-up-a-backdoor-to-its-global-supplier-management-network)
  * [Bleeping Computer](https://www.bleepingcomputer.com/news/security/researcher-breaches-toyota-supplier-portal-with-info-on-14-000-partners/)

**February 13, 2023 update:** A previous version of this post indicated SHI might have developed the GSPIMS application based on a license key found in the JavaScript code. SHI has now confirmed they did **not** develop GSPIMS and simply sold Toyota the license key. Based on this information, GSPIMS is a Toyota-developed application and has no known third party development involvement.

## **Key Points / Summary:**

  * I hacked Toyota’s Global Supplier Preparation Information Management System (“GSPIMS”), a web app used by Toyota employees and their suppliers to coordinate projects, parts, surveys, purchases, and other tasks related to the global Toyota supply chain.
  * System Admin access achieved through accidentally introduced backdoor as part of a user impersonation/”Act As” feature.
  * Any user could be logged in to just by knowing their email, completely bypassing the various corporate login flows.
  * Read/write access to the global user directory containing 14k+ users was achieved.
  * Data access achieved: 14k+ corporate user account details, confidential documents, projects, supplier rankings/comments, and more. Data access was global and not limited to North America.
  * Issue was responsibly disclosed to Toyota in November 2022 and fixed in a timely manner.

Over the course of a slow week in late October 2022, I decided to explore the subdomains of various major companies to see if I could find any exploits worth reporting/writing about. I found several interesting Toyota websites. In 7 days, I reported 4 different security issues to Toyota, all of which were classified as “critical”. One of the reports had a remarkably severe impact and is one of the most severe vulnerabilities I have ever found (so far!)

I discovered what was essentially a backdoor login mechanism in the [Toyota GSPIMS website/application](https://gspims.toyota.com/) that allowed me to log in as any corporate Toyota user or supplier just by knowing their email. I eventually uncovered a system administrator email and was able to log in to their account. Once that was done, I had full control over the entire global system. I used the word “staggering” to describe the amount of data I had access to in the [Jacuzzi SmartTub hack](https://eaton-works.com/2022/06/20/hacking-into-the-worldwide-jacuzzi-smarttub-network/), but that was relatively minor compared to this. I had full access to internal Toyota projects, documents, and user accounts, including user accounts of Toyota’s external partners/suppliers. External accounts include users from:

  * [Michelin](https://www.michelin.com/en/)
  * [Continental](https://www.continental.com/en/)
  * [Stanley Black & Decker](https://www.stanleyblackanddecker.com/)
  * [HARMAN](https://www.harman.com/)
  * [Timken](https://www.timken.com/)
  * [BOS](https://bos.de/en.html)
  * [Magna](https://www.magna.com/)
  * Many more (note the various email domains in the screenshots below)

![](https://eaton-works.com/cdn-cgi/imagedelivery/VwwCqBIYNXeyNQwEQ8uyVQ/f461a7eb-27c1-4542-36b7-aa250a6ad600/full)

GSPIMS stands for “Global Supplier Preparation Information Management System”. It is an [Angular](https://angular.io/) single-page-application created and maintained by Toyota. At first, I didn’t know what GSPIMS was. Google showed a few job listings about it, but otherwise seemed obscure. I didn’t think it was that important at first, but I decided to put some time into it to see what might be hiding behind the login screen. It wasn’t until I bypassed the login screen that I saw the “Global Supplier Preparation Information Management System” label. Sounds important!

## **Bypassing the login**

The login screen features corporate Toyota and Supplier login options:

![](https://eaton-works.com/cdn-cgi/imagedelivery/VwwCqBIYNXeyNQwEQ8uyVQ/8f2b015c-f204-4a05-f1a9-c870f7ad3b00/full)_There should be a “Are you a Hacker?” option_.🙂

Both options supply the same list of login methods:

![](https://eaton-works.com/cdn-cgi/imagedelivery/VwwCqBIYNXeyNQwEQ8uyVQ/89f70843-4e95-49b9-5340-94583e53ba00/full)

  * TMNA = Toyota Motor North America
  * TME = Toyota Motor Europe
  * TMC = Toyota Motor Corporation (Japan)
  * TDEM = Toyota Daihatsu Engineering & Manufacturing (Asia)
  * Other Affiliates = Unknown, this button does not currently work

If you work for/with Toyota on any continent, it is likely you can log in to the system using one of these options. I do not work for Toyota, so I had to get past this login screen by patching the JavaScript code.

Developers control access to Angular routes/pages by implementing [CanActivate](https://angular.io/api/router/CanActivate) and [CanActivateChild](https://angular.io/api/router/CanActivateChild). Basically, when a user attempts to navigate to a route/page, you would determine if they are allowed to view it, and then return true or false. By patching both to return true, you can usually fully unlock an Angular app:

![](https://eaton-works.com/cdn-cgi/imagedelivery/VwwCqBIYNXeyNQwEQ8uyVQ/bc6f232f-6374-4df6-c6a1-2bb558814f00/full)

The logout code also needed to be removed to prevent a redirect back to the login page:

![](https://eaton-works.com/cdn-cgi/imagedelivery/VwwCqBIYNXeyNQwEQ8uyVQ/42568345-0e0a-4c30-5836-87237fff2000/full)

With those patches applied, the app loads and can be browsed:

[![](https://eaton-works.com/cdn-cgi/imagedelivery/VwwCqBIYNXeyNQwEQ8uyVQ/e46c7e13-21c4-4c85-3b71-0842234c7f00/full)](https://eaton-works.com/cdn-cgi/imagedelivery/VwwCqBIYNXeyNQwEQ8uyVQ/e46c7e13-21c4-4c85-3b71-0842234c7f00/full)

In the [Jacuzzi SmartTub case](https://eaton-works.com/2022/06/20/hacking-into-the-worldwide-jacuzzi-smarttub-network/), patching the JavaScript was all that was needed to achieve full access, since their API was improperly secured. In GSPIMS’ case, no data would load from the API. All the endpoints would return HTTP status 401 – Unauthorized responses due to the missing login cookie. This was the case for every page I browsed. Toyota had seemingly secured their API correctly, and at this point I was about to write this site off as “probably secure”. I don’t bother reporting single-page-application bypasses unless it also exposes a leaky/improperly secured API.

## **JWTs for everyone!**

Before abandoning work on the GSPIMS app, I looked through its code to see if there might have been any API keys, secret API endpoints, or anything else that might be interesting. I came across this function in the user service. Can you spot what is interesting about it?

![](https://eaton-works.com/cdn-cgi/imagedelivery/VwwCqBIYNXeyNQwEQ8uyVQ/af0ae08b-be07-40c6-bc6a-c39e62d98d00/full)_JWT stands for JSON Web Token. Think of it as a session token that represents your valid authenticated session on a website. You typically get a JWT after logging into a website using your email and password. You then provide the JWT to secured parts of a website or API to prove your identity and what you are allowed to access.[More information](https://en.wikipedia.org/wiki/JSON_Web_Token)_

It is interesting because it appears to be generating a JWT based on a provided email. No password required. I decided to compose this HTTP request to see if that _createJWT_ endpoint actually worked. Even if it worked, it wouldn’t be enough without a valid email, which could have been difficult to figure out, especially if the underlying userbase was small.

Corporate Toyota emails use a predictable format in North America: _firstname.lastname@toyota.com_. That made guessing a valid email easier, but I still had to find someone. I Googled for Toyota employees involved in the supply chain, hoping to find someone who may be registered in the GSPIMS system. I found a promising match and formulated their email address based on their name. Then I fired off the _createJWT_ HTTP request, and it returned a valid JWT!

![](https://eaton-works.com/cdn-cgi/imagedelivery/VwwCqBIYNXeyNQwEQ8uyVQ/0eadbc74-e140-4489-b565-9f1394e03c00/full)

It seems like I had discovered a way to generate a valid JWT for any Toyota employee or supplier registered in GSPIMS, **completely bypassing the various corporate login flows, which probably also enforce two-factor authentication options**. The reason _createJWT_ exists will be revealed later in this post.

Utilizing the JWT was easy. The GSPIMS API authenticates via cookie, so I just added it through Chrome’s dev tools:

![](https://eaton-works.com/cdn-cgi/imagedelivery/VwwCqBIYNXeyNQwEQ8uyVQ/6feb834f-94f7-4097-5165-6e99b74ccf00/full)

## **Escalating to System Admin**

The user I logged in had the role of “Mgmt – Purchasing” which probably means they are in charge of organizing purchases of things from suppliers through this system. I had access to some data at this point, but I felt there was more waiting to be unlocked. Looking at the HTTP requests and responses, there is a _rolePrivileges_ node in the _user/details_ API response that returns information about the currently logged in user:

![](https://eaton-works.com/cdn-cgi/imagedelivery/VwwCqBIYNXeyNQwEQ8uyVQ/e96e5637-e9f2-490c-1159-cf8c9532f800/full)

I wanted to try and find a user with the System Admin role. I noticed another API endpoint named _findByEmail_ that returned information about a user’s account by just providing a valid email. Conveniently, this also tells you who the user’s managers are:

![](https://eaton-works.com/cdn-cgi/imagedelivery/VwwCqBIYNXeyNQwEQ8uyVQ/f6a2abeb-4754-4cc7-ee44-87f45fa33600/full)_Imagine having 3 different managers to report to!_ 😱

Checking the managers of the managers, etc. made it easy to find accounts that had elevated access to the system. Eventually I found a North America Regional Admin. That gave me access to the User Administration section. I then poked around more and found users with even higher access, such as Supplier Admin, Global Admin, and finally, System Admin.

In the GSPIMS settings, the tabs that appear are dependent on your role. There’s Regional Settings for Regional Admins, Global Settings for Global Admins, and System Admin Settings for System Admins. System Admins can access all the tabs. I also noticed that System Admins had access to substantially more users in the User Administration section. Regional Admins are probably only able to manage users in their region, whereas System Admins could manage everyone. With a System Admin JWT, I basically had total, global control over the entire system.

![](https://eaton-works.com/cdn-cgi/imagedelivery/VwwCqBIYNXeyNQwEQ8uyVQ/14e3f09a-d9ac-42e9-f1d4-1228843ea500/full)

A few screenshots of various sets of users. Take note of the user and page counts in the bottom right corner (there’s a lot – 14,063 users across 563 pages!) Click on any image to enlarge it in a new tab.

[![](https://eaton-works.com/cdn-cgi/imagedelivery/VwwCqBIYNXeyNQwEQ8uyVQ/33cec25b-ab6e-4389-000c-3ffc630c7300/full)](https://eaton-works.com/cdn-cgi/imagedelivery/VwwCqBIYNXeyNQwEQ8uyVQ/33cec25b-ab6e-4389-000c-3ffc630c7300/full)_American users_ [![](https://eaton-works.com/cdn-cgi/imagedelivery/VwwCqBIYNXeyNQwEQ8uyVQ/59dc6201-20a8-4074-f518-b941ec957900/full)](https://eaton-works.com/cdn-cgi/imagedelivery/VwwCqBIYNXeyNQwEQ8uyVQ/59dc6201-20a8-4074-f518-b941ec957900/full)_Asian users_

[![](https://eaton-works.com/cdn-cgi/imagedelivery/VwwCqBIYNXeyNQwEQ8uyVQ/e8618f41-5e3f-447e-b499-5db006622500/full)](https://eaton-works.com/cdn-cgi/imagedelivery/VwwCqBIYNXeyNQwEQ8uyVQ/e8618f41-5e3f-447e-b499-5db006622500/full)_Japanese users_ [![](https://eaton-works.com/cdn-cgi/imagedelivery/VwwCqBIYNXeyNQwEQ8uyVQ/ba3abcbd-6b02-45db-4d98-2a72615fb600/full)](https://eaton-works.com/cdn-cgi/imagedelivery/VwwCqBIYNXeyNQwEQ8uyVQ/ba3abcbd-6b02-45db-4d98-2a72615fb600/full)_American System Admins_

[![](https://eaton-works.com/cdn-cgi/imagedelivery/VwwCqBIYNXeyNQwEQ8uyVQ/79f1897c-11fc-45de-3ae6-3256d98c3400/full)](https://eaton-works.com/cdn-cgi/imagedelivery/VwwCqBIYNXeyNQwEQ8uyVQ/79f1897c-11fc-45de-3ae6-3256d98c3400/full)_European users_ [![](https://eaton-works.com/cdn-cgi/imagedelivery/VwwCqBIYNXeyNQwEQ8uyVQ/2a9d56ee-21bc-4969-1711-b43856f50d00/full)](https://eaton-works.com/cdn-cgi/imagedelivery/VwwCqBIYNXeyNQwEQ8uyVQ/2a9d56ee-21bc-4969-1711-b43856f50d00/full)_More Japanese users_

I could edit any of those users:

![](https://eaton-works.com/cdn-cgi/imagedelivery/VwwCqBIYNXeyNQwEQ8uyVQ/fba969b7-395c-46f3-ebd9-2fff9d95f100/full)

Or add a new user using the user import button above the columns. There is also an export users button you can use to download user information.

## **Exploring the impact**

Having full access, I looked around the GSPIMS app to see what was available to me as a System Admin. I was very careful to not modify anything. Here’s the System Admin Settings if you are curious about what is there. Nothing too exciting – it just controls what roles can access certain features.

![](https://eaton-works.com/cdn-cgi/imagedelivery/VwwCqBIYNXeyNQwEQ8uyVQ/64570ee9-1dd7-4f03-2336-1b826090c000/full)

Now on to more interesting things. The Parts section has a list of parts associated with the various projects. You choose an affiliate at the top and then the project to see the list of parts. Here is the parts list for a project:

[![](https://eaton-works.com/cdn-cgi/imagedelivery/VwwCqBIYNXeyNQwEQ8uyVQ/3bbc7db7-baf6-4f51-65a3-fa4650883800/full)](https://eaton-works.com/cdn-cgi/imagedelivery/VwwCqBIYNXeyNQwEQ8uyVQ/3bbc7db7-baf6-4f51-65a3-fa4650883800/full)

It’s worth noting the projects are in codenames/numbers. It didn’t say anything like “2024 Toyota Corolla”. With a lot more time I probably could have figured out the codenames, but that was outside the scope of this investigation. Speaking of projects, I had access to all the active, global, and inactive projects:

[![](https://eaton-works.com/cdn-cgi/imagedelivery/VwwCqBIYNXeyNQwEQ8uyVQ/d4d1882d-a682-49e1-0fed-c6d30ed77500/full)](https://eaton-works.com/cdn-cgi/imagedelivery/VwwCqBIYNXeyNQwEQ8uyVQ/d4d1882d-a682-49e1-0fed-c6d30ed77500/full)

I could view the details of each project, including who is involved, the schedule and milestones, and some type of survey feature. Click on any image to enlarge it in a new tab.

[![](https://eaton-works.com/cdn-cgi/imagedelivery/VwwCqBIYNXeyNQwEQ8uyVQ/b14bb7da-6371-4d64-d871-554ca4b33e00/full)](https://eaton-works.com/cdn-cgi/imagedelivery/VwwCqBIYNXeyNQwEQ8uyVQ/b14bb7da-6371-4d64-d871-554ca4b33e00/full)_Project Parts List_

[![](https://eaton-works.com/cdn-cgi/imagedelivery/VwwCqBIYNXeyNQwEQ8uyVQ/c77d957e-2887-40e0-d7fb-5110f5210000/full)](https://eaton-works.com/cdn-cgi/imagedelivery/VwwCqBIYNXeyNQwEQ8uyVQ/c77d957e-2887-40e0-d7fb-5110f5210000/full)_Add/Remove Users_

[![](https://eaton-works.com/cdn-cgi/imagedelivery/VwwCqBIYNXeyNQwEQ8uyVQ/8e17b485-4df4-4a69-a695-32b955373d00/full)](https://eaton-works.com/cdn-cgi/imagedelivery/VwwCqBIYNXeyNQwEQ8uyVQ/8e17b485-4df4-4a69-a695-32b955373d00/full)_Project Schedule_

[![](https://eaton-works.com/cdn-cgi/imagedelivery/VwwCqBIYNXeyNQwEQ8uyVQ/c9b735bb-88ec-4725-bf13-0597a9313c00/full)](https://eaton-works.com/cdn-cgi/imagedelivery/VwwCqBIYNXeyNQwEQ8uyVQ/c9b735bb-88ec-4725-bf13-0597a9313c00/full)_Surveys_

[![](https://eaton-works.com/cdn-cgi/imagedelivery/VwwCqBIYNXeyNQwEQ8uyVQ/b7e904f1-f7e7-490a-59dc-4e0c0e26c500/full)](https://eaton-works.com/cdn-cgi/imagedelivery/VwwCqBIYNXeyNQwEQ8uyVQ/b7e904f1-f7e7-490a-59dc-4e0c0e26c500/full)_System Management_

Can’t forget about the documents! Classified documents are all the rage nowadays.

[![](https://eaton-works.com/cdn-cgi/imagedelivery/VwwCqBIYNXeyNQwEQ8uyVQ/dd45ec6f-d2f4-4c05-653c-7f725930aa00/full)](https://eaton-works.com/cdn-cgi/imagedelivery/VwwCqBIYNXeyNQwEQ8uyVQ/dd45ec6f-d2f4-4c05-653c-7f725930aa00/full)

Reviewing the HTTP trace I captured, I noticed you can also see Toyota’s various comments about their suppliers. It’s probably also visible in the UI somewhere.

![](https://eaton-works.com/cdn-cgi/imagedelivery/VwwCqBIYNXeyNQwEQ8uyVQ/4234c6a9-3fec-4520-014d-b26eefa40200/full) ![](https://eaton-works.com/cdn-cgi/imagedelivery/VwwCqBIYNXeyNQwEQ8uyVQ/40bb7251-f703-483f-db75-c3c7640f9b00/full)

The HTTP trace was captured by just having [Fiddler](https://www.telerik.com/fiddler) open while browsing the app. The API is very generous with the amount of data it returns, in particular with the users list. You could download a lot of user information by increasing the page size and flipping through the pages.

You could also see all the suppliers and how Toyota ranks them regarding risk, delivery, and prep. There are almost 3,000 of them:

[![](https://eaton-works.com/cdn-cgi/imagedelivery/VwwCqBIYNXeyNQwEQ8uyVQ/0c488a45-eeb2-4725-8160-208650ecb400/full)](https://eaton-works.com/cdn-cgi/imagedelivery/VwwCqBIYNXeyNQwEQ8uyVQ/0c488a45-eeb2-4725-8160-208650ecb400/full)

Finally, I discovered what the _createJWT_ API was actually used for. There is an “Act As” feature that let me log in as any of those 14k+ global users. I could easily log in as anyone and get an idea of what projects they are working on, their tasks, surveys, etc. Whoever made the Act As system apparently didn’t realize they added a backdoor to the entire system. The Act As feature is only visible to certain users, like the System Admin user I was logged in as.

![](https://eaton-works.com/cdn-cgi/imagedelivery/VwwCqBIYNXeyNQwEQ8uyVQ/d26fa3a8-6d32-430f-f953-17ba68172c00/full)_That is one**long** drop-down list._

If a threat actor had discovered this issue, the consequences could have been severe. Here’s a few bad things they could have done. Please note that these are just ideas and none of these were carried out.

  * Added their own user account with an elevated role, to retain access should the issue ever be discovered and fixed.
  * Downloaded and leaked all the data.
  * Delete everything or modify data in a way to be disruptive to global Toyota operations. Hopefully Toyota has working backups?
  * Craft a highly targeted phishing campaign to attempt to capture real corporate login details, which could have exposed other Toyota systems to attacks. There’s 14k+ users available to attack. It’s one thing to have 14k+ corporate emails, but it’s another to have 14+ corporate emails **and** know exactly what they are working on/have worked on. If a supplier user has a habit of reusing passwords, it’s possible their own infrastructure could be attacked too.

## **Reporting to Toyota**

The issue was reported to Toyota on November 3, 2022, and they responded later that same day confirming they received the report. On November 23, 2022, they confirmed the issue was remediated, although I noticed it was fixed before that when I randomly tested. I then informed them I would publish my writeup after the industry standard 90-day period has passed.

Toyota fixed the issue by making the _createJWT_ and _findByEmail_ endpoints return HTTP status 400 – Bad Request in all cases.

Out of all the security issues I have reported so far to various vendors, Toyota’s response was the fastest and most effective. I was very impressed with how quickly they responded and fixed the issue. Some companies can be slow to respond or fail to respond at all, so this experience was refreshing.

Thanks to this responsible disclosure, Toyota avoided what could have been a catastrophic leak of not only their own employees’ data, but the data of their partners/suppliers. Embarrassing internal comments and supplier rankings could have been published for the world to see. [Toyota and their suppliers have been hit by cyberattacks before](https://www.cnn.com/2022/03/01/business/toyota-japan-cyberattack-production-restarts-intl-hnk/index.html) and it could have easily happened again.

Unfortunately, the reward for reporting this critical issue was $0. While it’s fun to find significant vulnerabilities like these, I will probably start shifting my efforts to companies offering monetary rewards help to sustain these often-lengthy investigations and writeups. ~~PS: If you/your company’s security team are currently hiring, feel free to[say hello](https://eaton-works.com/contact/)🙂.~~
