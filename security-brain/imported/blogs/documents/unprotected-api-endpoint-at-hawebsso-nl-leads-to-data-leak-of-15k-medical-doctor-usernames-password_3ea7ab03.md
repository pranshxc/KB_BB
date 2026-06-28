---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-12-14_unprotected-api-endpoint-at-hawebssonl-leads-to-data-leak-of-15k-medical-doctor-.md
original_filename: 2022-12-14_unprotected-api-endpoint-at-hawebssonl-leads-to-data-leak-of-15k-medical-doctor-.md
title: Unprotected API endpoint at HAwebsso.nl leads to data leak of +15k medical
  doctor usernames & password hashes
category: documents
detected_topics:
- sso
- idor
- mfa
- api-security
- access-control
- command-injection
tags:
- imported
- documents
- sso
- idor
- mfa
- api-security
- access-control
- command-injection
language: en
raw_sha256: 3ea7ab0362e9c7c62b2ffabee59e133deb3aa56cf5192cbd3b959a37ba3dc8e1
text_sha256: 662e404c9f49471aaeb4c88c886655dfe973ed1678834400d722ddc968f67fed
ingested_at: '2026-06-28T07:32:16Z'
sensitivity: unknown
redactions_applied: false
---

# Unprotected API endpoint at HAwebsso.nl leads to data leak of +15k medical doctor usernames & password hashes

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-12-14_unprotected-api-endpoint-at-hawebssonl-leads-to-data-leak-of-15k-medical-doctor-.md
- Source Type: markdown
- Detected Topics: sso, idor, mfa, api-security, access-control, command-injection
- Ingested At: 2026-06-28T07:32:16Z
- Redactions Applied: False
- Raw SHA256: `3ea7ab0362e9c7c62b2ffabee59e133deb3aa56cf5192cbd3b959a37ba3dc8e1`
- Text SHA256: `662e404c9f49471aaeb4c88c886655dfe973ed1678834400d722ddc968f67fed`


## Content

---
title: "Unprotected API endpoint at HAwebsso.nl leads to data leak of +15k medical doctor usernames & password hashes"
page_title: "Unprotected API endpoint at hawebsso.nl leaks 15k doctors usernames and hashed passwords | Medium"
url: "https://medium.com/@jonathanbouman/unprotected-api-endpoint-at-hawebsso-nl-5f1951e212fe"
authors: ["Jonathan Bouman (@JonathanBouman)"]
programs: ["HAwebsso.nl"]
bugs: ["SSO", "IDOR", "Missing authentication"]
publication_date: "2022-12-14"
added_date: "2022-12-20"
source: "pentester.land/writeups.json"
original_index: 1775
scraped_via: "browseros"
---

# Unprotected API endpoint at HAwebsso.nl leads to data leak of +15k medical doctor usernames & password hashes

Unprotected API endpoint at HAwebsso.nl leads to data leak of +15k medical doctor usernames & password hashes
Jonathan Bouman
Follow
11 min read
·
Dec 15, 2022

173

2

Press enter or click to view image in full size
Proof of concept, showing where the endpoint was found and how it leaks user data (censored in this video)

Background
As some might know, I work as a medical doctor (general practitioner) by day and as a security researcher by night. One of my goals in ethical hacking is to learn as much as possible in order to be able to audit myself healthcare products, apps, websites or infrastructure. Is it really, really, secure? I don’t trust shiny emblems or certificates.

Today we will have a look at the security of the Nederlandse Huisartsen Genootschap (NHG) and the Landelijke Huisartsen Vereniging (LHV). Those are professional organizations for general practitioners (GP) in the Netherlands. The NHG sets standards for GPs and provides education and training, while the LHV represents the interests of GPs and works to improve the quality and accessibility of primary care. Both organizations play important roles in the Dutch healthcare system, working to ensure that patients receive high-quality care from their GPs. At the moment we have 13k GPs in The Netherlands.

Recon, where to start?
What if the NHG and LHV are found vulnerable, could we impact those 13k associated medical doctors?

The NHG and LHV both have plenty of online applications that allow doctors to login and interact with. For example HAweb.nl, an online community for medical doctors and richtlijnen.nhg.org that allows doctors to add their personal notes to the professional guidelines.

Today I just start by clicking around on the LHV.nl main website looking for different subdomains and how the login procedure works.

What most of the LHV and NHG applications share is a Single Sign-On (SSO) authentication method using the domain hawebsso.nl. It pops up whenever you try to access some application that needs authorization, like haweb.nl

SSO is a method of authentication that allows users to access multiple applications and services with a single set of login credentials. This eliminates the need for users to remember and manage multiple sets of login information, and can greatly improve the user experience and productivity. Organizations often use SSO to streamline access to multiple systems and applications, improve security by reducing the number of places where user credentials are stored, and centralize control over access to resources. Additionally, SSO can be integrated with other security features, such as multi-factor authentication, to provide an additional layer of protection for sensitive systems and data.

The good news is, if we hack the SSO we got access to everything. The bad news most of the SSO systems used are heavily battle tested pieces of software (feel free to swap good news and bad news in this sentence).

Good luck breaking a battle proven SSO service.

Press enter or click to view image in full size
The login page of the SSO system used by the LHV & NHG

Bonus
A good trick to quickly see the possible scope of the SSO system is to check for OpenID endpoints, try to visit https://hawebsso.nl/.well-known/openid-configuration

Press enter or click to view image in full size
The SSO system holds interesting user data (called claims in OpenID). Furthermore it supports plenty of different scopes. For example it has the scope ‘HAWeb_SSO_Scope_WaarneemApp’ which gives access to WaarneemApp (a tool used to trade shifts between doctors).

Another thing I quickly check for is if I get any hints about which system is running behind the SSO. I look at the response headers of this HTTP request:

Press enter or click to view image in full size
The SSO runs on Microsoft IIS/10.0. No hints to the software used here.

So far so good, nothing special.

What about the source code of the login page?

Press enter or click to view image in full size
The login page references to an Javascript file named admin.js

The next step is to take a look at the source code of the login page. Are there any clues about the system being used for the SSO or do we see anything else odd?

Admin.js
As we can see the login page is loading different javascript files, some to add functionality to the login form. None of the files leak hints about the actual system used, it could be that this SSO front end is a custom built one; it’s wrapping around a ASP powered SSO back end system.

However one of the loaded files got my attention: admin.js. Whenever we see the word ‘admin’ we are eager to know more about it.

Part of the source code inside the admin.js file:

$scope.GetAdmin = function () {
  return $http({
  method: 'GET',
  url: '/api/v1/user/admin',
  }).then(function (response) {
  $scope.adminUser = response.data;
  if ($scope.adminUser.roles != null && $scope.adminUser.roles.length > 0) {
  var roles = $scope.adminUser.roles.split(",");
  $scope.permissions = {
  admin_level_1: roles.indexOf("Admin_level_1") > -1,
  admin_level_2: roles.indexOf("Admin_level_2") > -1,
  allow_edit: roles.indexOf("Admin_allow_edit") > -1,
  allow_merge: roles.indexOf("Admin_allow_merge") > -1,
  allow_activate: roles.indexOf("Admin_allow_activate") > -1,
  allow_deactivate: roles.indexOf("Admin_allow_deactivate") > -1,
  allow_make_admin: roles.indexOf("Admin_level_1") > -1,
  allow_deactivate_admin: roles.indexOf("Admin_level_1") > -1,
  show_field_id: roles.indexOf("Admin_show_field_id") > -1,
  show_field_firstname: roles.indexOf("Admin_show_field_firstname") > -1,
  show_field_insertion: roles.indexOf("Admin_show_field_insertion") > -1,
  show_field_lastname: roles.indexOf("Admin_show_field_lastname") > -1,
  show_field_lhv_id: roles.indexOf("Admin_show_field_lhv_id") > -1,
  show_field_nhg_id: roles.indexOf("Admin_show_field_nhg_id") > -1,
  show_field_emailaddress: roles.indexOf("Admin_show_field_emailaddress") > -1,
  show_field_cat_override: roles.indexOf("Admin_show_field_cat_override") > -1,
  congres_admin: roles.indexOf("Admin_congres") > -1
  };
  }
  }).catch(function (response) {
  $scope.addMessage(response.data, response.status, response.status == 200 ? "success" : "error");
  });
  }
  
  $scope.GetAdmin();

So there is an endpoint that admins could hit that returns the different roles of an user. In this situation the /admin user. Strange to share this code in the main login screen.

As I’m one of the GPs with a SSO login I could login and hit that endpoint.

Press enter or click to view image in full size
Woops. The endpoint returns all the currently logged in user its data. Including a password hash.

The endpoint does not properly checks who requests it and returns all our user information. Including email, full name, password hash and some membership details.

What if we hit the same endpoint and swap the /admin with an ID, as we can see I have the ID 2027 . Let’s see what happens if we try to hit ID 15000: https://hawebsso.nl/api/v1/user/15000

Press enter or click to view image in full size
User ID 15000 exists, all the account details are shared with us, including the password.

We now have showed the impact of this endpoint, it leaks all the user details of people enrolled in the SSO service hawebsso.nl

In technical terms we call this sort of bug an IDOR; Insecure direct object references.

The endpoint /api/v1/user/1 is a generic endpoint that could be easily discovered by hackers. One could use word lists to bruteforce endpoints on an asset like this, a good example is Assetnote.io their shared word lists. The wordlist https://wordlists-cdn.assetnote.io/data/automated/httparchive_apiroutes_2020_11_20.txt contains this specific endpoint with an ID that would return a hit.

Press enter or click to view image in full size
An example of a word list entry that would give a hit

Another approach the hacker could take is to scan all the used javascript files for endpoints. For example LinkFinder does this for you.

Get Jonathan Bouman’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

No authentication required
We now showed that a specific endpoint leaks the user details, however does it require authentication. Could one hit this endpoint while not being logged in?

Press enter or click to view image in full size
Open the same endpoint in incognito mode of the browser. No cookies are set, I’m not logged in. All user details are returned.

The answer is yes. This endpoint does not require any login. In technical terms we now have another bug, Missing Authentication for Critical Function. Opening the endpoint in a browser without being logged in returns us all the user details.

Press enter or click to view image in full size
Proof of concept that the endpoint works without being logged in (censored confidential data).

Password hash, how to break it?
Now we have the hash of the password. Using password hashes reduces the impact of a data leak, as one would have to break the hash first to retrieve the password. In the past password hashes like MD5 were easily broken by using something like Rainbow Tables; lists of all the possible hashes, that are computed in advance to crack the hash.

Nowdays this is resolved by using more secure hashing algorithms and including salts.

By changing my password to the same password I had I could confirm that a new unique hash is generated. Something that gives us a clue that rainbow tables might be not working here (for example if they include an unique salt per user).

For testing I used the following hash to crack (no worries, it is my own hash, with a dummy password): em1EijmR7gmSA0NC2fbbl488pWDpX6YEfPtU4BNRsu01VX9VZFRuvSBAPaaIwVe5KC0enebMfwJC1AGZVNFbRsZ+7Pa7hj718HfKfIolp/5rDgsp/52UOqawXrNGHgwCHYsd+S0gG4K+ba3zjsjg5cVXCpIrqvlJbO45DkPqZ+B/REWhOmkBdRdie76z9oWk1qp7LFa9l/4Z3TtCgucS+m0Sl66mYcWwafRZkAas5a5z15v9iweiZK4WyEbkmUFQDgAqXMAsljftoJxSP0QN/BbXUtAm0wENIGvt7PPTg7dGxdUoySbUFpmnzm/eTeCcgbEpsJhb3bwAulMVl0F3

After hacking for a while you could identify the most hash types by just looking at it, just like skin diseases.

098f6bcd4621d373cade4e832627b4f6 - MD5
5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8 - SHA-256
$2y$12$xyq65gSoKygKl5kxKYDbjeTocAh8BcbuprbohD.kkX0PZr73pH5LC - Bcrypt

However here I don’t have a clue now about which hash algorithm is used. After reaching out to one of my fellow ethical hackers I was told that this looked like a base64 encoded string, decoded it’s exactly 255 bytes long.

Press enter or click to view image in full size
The output of echo <hash> | base64 — decode | wc -c

Knowing from our recon that ASP is running on the server we might get more clues from the documentation provided by Microsoft: https://learn.microsoft.com/en-us/aspnet/core/security/authentication/identity

Later I found this (5 years old) blog about the different hashing algorithms https://andrewlock.net/exploring-the-asp-net-core-identity-passwordhasher/ and found the following piece interesting:ASP.NET Core Identity Version 3: PBKDF2 with HMAC-SHA256, 128-bit salt, 256-bit subkey, 10000 iterations

This gives me a hint that ASP uses, out of the box, a proper hashing algorithm, one that I could not easily crack at the moment. Some interesting discussion about PBKDF2 and the future could be read here.

For now I gave up on cracking those hashes.

However I would love to learn more from the readers of this blog, are you able to crack my hash? If so, let me know how you would do this. The first one to crack it will earn my rare shiny glitter sticker and some other unique swag! This world is all about stickers as you know.

Conclusion
We found a data leak that leaks about all of the emails and password hashes used by GPs in The Netherlands. This endpoint was unprotected and did not require any authorization. As it’s a generic path it could be easily guessed by hackers. Furthermore the reference to this endpoint was hidden in the admin.js file included on the login page, tools like LinkFinder would have informed any scanning hacker of this specific endpoint.

Discussion
The LHV published a responsible disclosure policy on their website that allowed me to do this research: https://www.lhv.nl/cvd-coordinated-vulnerability-disclosure/ Which is a great example how to support ethical hackers.

Furthermore they try to improve overall security in primary healthcare by developing guidelines how to handle data leaks. Recently they published about this in one of the magazines read by GPs: https://www.syntheshis.nu/wp-content/uploads/2022/12/Synth-2022-03-Totaal.pdf (Dutch, page 22). Associated members are able to view this guideline: https://www.lhv.nl/product/praktijkwijzer-informatiebeveiliging/

However it would be great if everyone could access this document, the more we share the better we are able to fight the risks. In primary healthcare I work with students, data-managers and plenty of people not being a member of the LHV; if I could easily share those documents that would help (I prefer not to share outdated PDFs).

Another important thing is to add the responsible disclosure policy on every online asset. For example hawebsso.nl does not include any references. Also the NHG.org website (using the SSO) is not sharing any online responsible disclosure policies. A good thing would be to publish this policy as soon as possible, and getting everyone working at NHG comfortable with this good practice; see https://www.ncsc.nl/onderwerpen/cvd-beleid/cvd-beleid-opstellen to learn how to proceed as an organisation.

A good protection against data leaks like these are dual factor authentication (2FA), HAwebsso.nl supports this, however it’s not activated by default. My recommendation is to activate this in order to make it harder for attackers to access your account whenever your password got leaked. Also it’s important to not re-use passwords, as showed in this report when leaked (and cracked) it could be abused on other services; credential stuffing.

How could we avoid bugs like this?
This bug existed for ~3 years, so that’s a lot of time to discover it.

There are different ways to approach this question. One is on management level; get certifications and adopt industry standards.

Industry standards
These days we have different international industry standards (ie. ISO 27001) or national standards (ie. NEN 7510) that describe how to manage information security. A great way to embed some good information security practices into your organisation. Implement it, get an auditor to conform everything is implemented properly and marketing can share the good news you are secure.

“Sir, we are ISO 27001 certified, we are super secure” — Every sales department

Press enter or click to view image in full size
Certificates are good, but don’t protect you from getting hacked.

As we will see today, no certification will stop you from getting hacked. However that does not mean we should not do this. Every structured way of improving security is something worth to implement.

Pen-test consultants versus Ethical Hackers
Another approach is to perform regular pen tests; hire a firm and ask them to hack you. This bug is pretty straight forward and it’s likely that it would be caught in a pen test.

However those pen tests often happen in specific periods of time, it’s not a continuous process. So any new bugs in assets being released in between pen tests might go unnoticed.

A solution to that could be to create a community of ethical hackers, using bug bounty platforms (like HackerOne or BugCrowd) and start investing in ethical hackers that find bugs in your assets. We have some great examples of how to create communities in The Netherlands: Hack the Hague.

Threat modeling
I’m a big fan of the INCLUDESNODIRT.com method; get together a group of people (ie. developer, ethical hacker, GP, product owner and privacy officer), fill in the questionnaire and brainstorm for 20 minutes. Whenever you introduce new assets, add functionality to an app or have changes in your organisation (ie. mergers and acquisition). In this example one would ask themselves “Is the new Admin functionality added to hawebsso.nl properly secured from unauthorized access? If yes, explain how.”

Press enter or click to view image in full size
Threat modeling for digital health care

I’ve not seen the method being used in production yet, however I would love to hear stories from others who implemented it already. What could we learn from it and is it really working?

Transparency is trust
From the start until the end of this specific bug report the LHV privacy officer was very responsive to my emails. He frequently sent me updates which helps me in getting confidence that the impact of the bug is understood by all stakeholders and it is getting fixed quickly. He did a great job and is an example to others how to handle a report like this, thanks!

In any organisation transparency is trust. If it’s about data leaks we got good flowcharts that help us how to proceed and transparently inform the end users (like being able to publish blogs like this one).

This report shows the power of the crowd, transparency and a proper disclosing policy enables all the ethical hackers in the world to help you getting more secure. You could apply this crowd model to all other levels in your organisation and reach your goals quicker.

In the end we all want a better and safer primary health care tomorrow, and learn from mistakes made in the past.

Timeline
04–12–2022 — Found the bug, reported it to the LHV privacy officer by email
05–12–2022 — Reply from the privacy officer to confirm the bug
06–12–2022 — Update from privacy officer
08–12–2022 — Update from privacy officer: bug exists for 3 years (since end 2019), no signs of abuse in the logs of the last 2 years
11–12–2022 — Wrote this blog
12–12–2022 — Sent draft of this blog to privacy officer by email
12–12–2022 — LHV & NHG informed all members about data leak by email; requested members to reset their password.
13–12–2022 — LHV suggested some minor changes
14–12–2022 — Published blog
15–12–2022 — Reader informed me the Admin.js file existed in 2017; https://web.archive.org/web/20170905141113/https://hawebsso.nl/Js/admin/admin.js Would this mean the bug existed for +5 years? Asked LHV for some insights on this, got reply they will double check with the developer.
