---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2018-01-02_abusing-internal-api-to-achieve-idor-in-new-relic.md
original_filename: 2018-01-02_abusing-internal-api-to-achieve-idor-in-new-relic.md
title: Abusing internal API to achieve IDOR in New Relic
category: documents
detected_topics:
- idor
- api-security
- command-injection
- automation-abuse
tags:
- imported
- documents
- idor
- api-security
- command-injection
- automation-abuse
language: en
raw_sha256: baafd509816d0aaed8caa28548c7175eb75994f5c733617513c7e24c8c5f1f35
text_sha256: 79b5ef78a73efda439af0d81e6dbbf8477cfd59ac4d8ff9101279115bc79ae99
ingested_at: '2026-06-28T07:31:56Z'
sensitivity: unknown
redactions_applied: true
---

# Abusing internal API to achieve IDOR in New Relic

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2018-01-02_abusing-internal-api-to-achieve-idor-in-new-relic.md
- Source Type: markdown
- Detected Topics: idor, api-security, command-injection, automation-abuse
- Ingested At: 2026-06-28T07:31:56Z
- Redactions Applied: True
- Raw SHA256: `baafd509816d0aaed8caa28548c7175eb75994f5c733617513c7e24c8c5f1f35`
- Text SHA256: `79b5ef78a73efda439af0d81e6dbbf8477cfd59ac4d8ff9101279115bc79ae99`


## Content

---
title: "Abusing internal API to achieve IDOR in New Relic"
page_title: "Abusing internal API to achieve IDOR in New Relic - Jon's Personal Blog"
url: "https://www.jonbottarini.com/2018/01/02/abusing-internal-api-to-achieve-idor-in-new-relic/"
final_url: "https://www.jonbottarini.com/2018/01/02/abusing-internal-api-to-achieve-idor-in-new-relic/"
authors: ["Jon Bottarini (@jon_bottarini)"]
programs: ["New Relic"]
bugs: ["IDOR"]
bounty: "1,000"
publication_date: "2018-01-02"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 6020
---

I recently found a nice [insecure direct object reference](https://www.owasp.org/index.php/Top_10_2010-A4-Insecure_Direct_Object_References) (IDOR) in New Relic which allowed me to pull data from other user accounts, and I thought it was worthy of writing up because it might make you think twice about the types (and the sheer number!) of API’s that are used in popular web services.

New Relic has a private bug bounty program (I was given permission to talk about it here), and I’ve been on their program for quite some time, so I’ve become very familiar with their overall setup and functionality of the application, but this bug took me a long time to find … and you’ll see why below.

**Some background first:** New Relic has a public [REST API](https://docs.newrelic.com/docs/apis/rest-api-v2/getting-started/introduction-new-relic-rest-api-v2) which can be used by anyone with a standard user account . This API operates by passing the `X-api-key` header along with your query. Here’s an example of a typical API call:
  
  
  curl -X GET 'https://api.newrelic.com/v2/applications/{application_id}/hosts.json' \
  -H 'X-Api-Key=***REDACTED*** -i

Pretty typical. I tried to poke at this a little bit by swapping the `{application_id}` with another user account’s `{application_id}` that belongs to me. I usually test for IDOR’s this way, by having one browser (Usually Chrome) setup as my “victim account” and another browser (usually Firefox) as the “attacker” account, where I route everything through Burp and check the responses after I change values here and there. It’s kind of an old school way to test for IDOR’s and permission structure issues, and there is probably a much more effective way to automate something like this, but it works for me. Needless to say this was a dead end, and it didn’t return anything fruitful.

I looked further and found that New Relic also implements an _internal API_ which occurs on both their **infrastructure** product and their **alerts** product. They conveniently identify this through the `/internal_api/` endpoint (and put references to their internal API in some of their .js files as well).

The two products operate on different subdomains, `infrastructure.newrelic.com` and `alerts.newrelic.com`. This is what it looks like in Burp, on the `alerts.newrelic.com` domain (where the IDOR originally occurred).

![](https://www.jonbottarini.com/wp-content/uploads/2017/12/Screen-Shot-2017-12-27-at-9.55.48-PM.png)The reason I bring up the fact there are two separate subdomains is because this bug sat there for an excessive amount of time because I didn’t bother checking _both subdomains_ and their respective internal API’s. To make it even more difficult, there are multiple versions of the internal_api, and the bug only worked on version 1. Here’s what the vulnerable endpoint looked like:
  
  
  https://alerts.newrelic.com/internal_api/1/accounts/{ACCOUNT NUMBER}/incidents

The account number increases by 1 every time a new account is created, so I could have literally enumerated every single account pretty easily by just running an intruder attack and increasing the value by one each time. **The IDOR was possible because the application did not ensure that the account number being requested through the above internal API GET request matched the account number of the authenticated user.**

This IDOR allowed me to view the following from any New Relic account:

  * Account Events
  * Account Messages
  * Violations (Through NR Alerts)
  * Policy Summaries
  * Infrastructure events and filters
  * Account Settings

This bug has been resolved and I was rewarded $1,000. I’d just like to point out that the New Relic engineering and development team was super quick to remediate this. Special thanks to the New Relic team for running one of, if not the best bug bounty programs out there!

[Follow me on Twitter](https://www.twitter.com/jon_bottarini) to stay up to date with what I’m working on and security/bug bounties in general 🙂
