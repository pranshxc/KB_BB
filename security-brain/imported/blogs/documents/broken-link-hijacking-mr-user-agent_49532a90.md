---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-02-13_broken-link-hijacking-mr-user-agent.md
original_filename: 2022-02-13_broken-link-hijacking-mr-user-agent.md
title: Broken Link Hijacking - Mr. User-Agent
category: documents
detected_topics:
- command-injection
- mobile-security
- supply-chain
tags:
- imported
- documents
- command-injection
- mobile-security
- supply-chain
language: en
raw_sha256: 49532a90b90dc03b9a1edf74d0895dd82f1690a7ba889afd52282c1e6ff254bb
text_sha256: 002a686ad5f8b90a804f1367d17e5bb3fbba092ce8160643d35656b31d057d38
ingested_at: '2026-06-28T07:32:10Z'
sensitivity: unknown
redactions_applied: false
---

# Broken Link Hijacking - Mr. User-Agent

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-02-13_broken-link-hijacking-mr-user-agent.md
- Source Type: markdown
- Detected Topics: command-injection, mobile-security, supply-chain
- Ingested At: 2026-06-28T07:32:10Z
- Redactions Applied: False
- Raw SHA256: `49532a90b90dc03b9a1edf74d0895dd82f1690a7ba889afd52282c1e6ff254bb`
- Text SHA256: `002a686ad5f8b90a804f1367d17e5bb3fbba092ce8160643d35656b31d057d38`


## Content

---
title: "Broken Link Hijacking - Mr. User-Agent"
url: "https://shahjerry33.medium.com/broken-link-hijacking-mr-user-agent-cd124297f6e6"
authors: ["Jerry Shah (@Jerry)"]
bugs: ["Broken link hijacking"]
publication_date: "2022-02-13"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 2911
scraped_via: "browseros"
---

# Broken Link Hijacking - Mr. User-Agent

Top highlight

Broken Link Hijacking - Mr. User-Agent
Jerry Shah (Jerry)
Follow
5 min read
·
Feb 13, 2022

395

6

Press enter or click to view image in full size

Summary :

Broken Link Hijacking (BLH) is a web-based attack where it exploits external links that are no longer valid. The attackers take over this expired, stale, and invalid external links on credible websites or web applications for malicious or fraudulent purposes.

If your company uses an external link shortening service, for example, to include short links in tweets, it may be possible that the link shortener goes out of business after some time and is no longer valid. This means that all your old links are now broken.

If an attacker purchases the domain used by the link shortening service that went out of business, they can substitute your original content with their own malicious content.

Description :

I found a different kind of broken link hijacking attack where only android mobile users were affected, though broken link hijacking was out of scope but I found this issue to be unique so I thought of writing a blog on it. When I visited the website I did not find any external link services like twitter, instagram, linkedin etc. and so I started testing for other vulnerabilities and switched my User-Agent using a firefox extension called User-Agent Switcher and observed that after changing the user-agent from default to Android Phone/Firefox the external link to Google Play Store was displayed so I clicked on it and it redirected me to https://play.google.com and gave me an error saying “We’re sorry, the requested URL was not found on this server.”

I saw the URL and there was an ‘id=’ parameter with the value of com.target.androidappname so I thought to takeover it but the problem was I did not had a developer account of google, so I purchased it and build an application with the package name as the ‘id’ parameter value.

So for example if you find this kind of issue where the playstore URL is https://play.google.com/store/apps/details?id=com.target.appname and you want to takeover it then while building an app in android studio for the playstore the package name should as same as you ‘id’ parameter value.

You can also use a tool called dead link checker to find broken link hijacking issues.

How I found this vulnerability ?

I went to my target.com
Press enter or click to view image in full size
Target

2. Then I switched the User-Agent from default to Android Phone/Firefox

Press enter or click to view image in full size
Switch User-Agent Plugin - Firefox

3. After changing User-Agent, I reloaded the page and found a Google Play Store option below

Press enter or click to view image in full size
Google Play Store

4. I clicked on Google Play and was redirected to play store with an error saying “We’re sorry, the requested URL was not found on this server.”

Press enter or click to view image in full size
404 - Google Playstore

5. Then an app was created with the same package name as id (com.so_____.___am) and uploaded it on a playstore for a releasing it

Press enter or click to view image in full size
Production

6. After some days my app was published on the playstore

Press enter or click to view image in full size
Published

NOTE : The app is now removed from the playstore because it was only for a proof of concept.

Get Jerry Shah (Jerry)’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

What is a User-Agent and Why it is used ?

A user agent is any software, acting on behalf of a user, which retrieves, renders and facilitates end-user interaction with Web content. A user agent is therefore a special kind of software agent.

In HTTP, the User-Agent string is often used for content negotiation, where the origin server selects suitable content or operating parameters for the response. For example, the User-Agent string might be used by a web server to choose variants based on the known capabilities of a particular version of client software.

Why it happened ?

In my opinion,

It happened because the content of the User-Agent for a web browsers like firefox, Chrome etc. was served differently than that of a User-Agent of Android devices. By switching the User-Agents the content served was different which makes it an abnormal behaviour and led to broken link hijacking.

Impact :

It may not seem like much on the surface, but deep down, a broken link is doing some serious damage to your website, your reputation, and your business. A single broken link can impact your search engine rankings, your site’s user experience, result in lost customers and revenue, or, in worst case, all of the above. This kind of attacks can also lead to phishing scams.

Calculated CVSS :

Vector String - CVSS:3.0/AV:L/AC:H/PR:N/UI:R/S:U/C:L/I:L/A:N

Score - 3.6 (Low)

Mitigation :

There are three ways you can prevent this issue :

Use short, simple, easy-to-read and easy-to-type URLs. When creating links to a specific page, product, event, download, or any other content on your website, make it easy for everyone involved.
Check your links. Test them.
Use a link checker.

Mitigation (In My Case):

The content should be served same on all the User-Agents and if the different content is being served then it should be checked by the above mentioned mitigations.

Special thanks to App Developer :

droppyy33

Press enter or click to view image in full size
