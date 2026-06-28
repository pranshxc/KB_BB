---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2018-08-28_idor-facebook-malicious-person-add-people-to-the-top-fans.md
original_filename: 2018-08-28_idor-facebook-malicious-person-add-people-to-the-top-fans.md
title: 'IDOR FACEBOOK: malicious person add people to the “Top Fans”'
category: documents
detected_topics:
- idor
- access-control
- command-injection
- api-security
tags:
- imported
- documents
- idor
- access-control
- command-injection
- api-security
language: en
raw_sha256: cd5f840601e56211e3dd8b2c876ecba9253c99ae882330aa08cc010b3eb1c405
text_sha256: ccf674a852b6f8792a6dbc68120696e90a25d3a94cff0bc31c229ed9d07c235d
ingested_at: '2026-06-28T07:31:57Z'
sensitivity: unknown
redactions_applied: false
---

# IDOR FACEBOOK: malicious person add people to the “Top Fans”

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2018-08-28_idor-facebook-malicious-person-add-people-to-the-top-fans.md
- Source Type: markdown
- Detected Topics: idor, access-control, command-injection, api-security
- Ingested At: 2026-06-28T07:31:57Z
- Redactions Applied: False
- Raw SHA256: `cd5f840601e56211e3dd8b2c876ecba9253c99ae882330aa08cc010b3eb1c405`
- Text SHA256: `ccf674a852b6f8792a6dbc68120696e90a25d3a94cff0bc31c229ed9d07c235d`


## Content

---
title: "IDOR FACEBOOK: malicious person add people to the “Top Fans”"
url: "https://medium.com/@UpdateLap/idor-facebook-malicious-person-add-people-to-the-top-fans-4f1887aad85a"
authors: ["Jafar Abo Nada (@Jafar_Abo_Nada)"]
programs: ["Meta / Facebook"]
bugs: ["IDOR"]
publication_date: "2018-08-28"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5736
scraped_via: "browseros"
---

# IDOR FACEBOOK: malicious person add people to the “Top Fans”

IDOR FACEBOOK: malicious person add people to the “Top Fans”
Jafar Abo Nada
Follow
3 min read
·
Aug 28, 2018

34

1

TOP FANS BUG
Hi hackers,

Today I will write the story of this publication that I shared with my friends when I discovered a security issues on Facebook

Jafar Abo Nada
Jafar Abo Nada is in Amman, Jordan.

web.facebook.com

Vulnerability Type
Privacy / Authorization
Product Area
Pages
Technical details of the bug.

After digging around in Facebook looking for possible bug’s, I watched Facebook recently added a feature that allows fans to allow them to submit requests to be categorized in their favorite pages as their “Top Fans”. Facebook has made this optional. If you want to send a request through the notification I received to add it to the list.

After poking around in the HTTP requests, I found that the endpoint to send an request to join the “Top fans” list did not verify the sender is actually the sender.

The security flaw you have discovered allows a malicious person add users to the list of the “Top fans”, without requiring the user to do so by sending or approving the request.

Steps

1. Facebook sends messages to all users who follow certain pages and Facebook considers them the “Top Fans” of the page.

Get Jafar Abo Nada’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

2. The malicious person clicks on the notification of the “Top Fans” Facebook has sent him.

https://web.facebook.com/top_fans/fan_opt_in_dialog/?page_id=[PageID]&fan_id= [UserID]

3. After clicking on the “display Top Fans badge” icon, the request is intercepted.

4. The attacker will modify the link to the victim’s information

https://web.facebook.com/top_fans/fan_opt_in/?status=OPTED_IN&entry_point=notification&creator_id=[Page ID]&fan_id=[Victim ID]

5. Send the request after editing.

6. Now the target person has been added to the list of the “Top Fans” without his knowledge or to send the request.

“PoC” Proof of Concept:
Impact

The impact of this situation on privacy is greater than security.

An attacker can know people who are interested in a page by simply following comments or like them and then add them to the list of the “Top fans”.

The attacker can not access any user data, but I can be interacting with a page, but I do not like content. I think my classification as one of my most unpopular users is a violation of my privacy.

TimeLine:

27-Jun-2018 The report was submitted

27-Jun-2018 The vulnerability was accepted

29-Jun-2018 The security team told me they were patching Vulnerability.

29-Jun-2018 Re-testing and showing that the security defect still exists

05-Jul-2018 Reopen the report

17-Jul-12018 Patches were done

19-Jul-2018 Bounty awarded
