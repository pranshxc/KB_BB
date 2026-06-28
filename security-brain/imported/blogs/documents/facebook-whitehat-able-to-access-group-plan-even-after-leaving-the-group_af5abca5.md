---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2018-12-06_facebook-whitehat-able-to-access-group-plan-even-after-leaving-the-group.md
original_filename: 2018-12-06_facebook-whitehat-able-to-access-group-plan-even-after-leaving-the-group.md
title: 'Facebook WhiteHat: Able to access group plan even after leaving the group'
category: documents
detected_topics:
- access-control
- command-injection
- business-logic
- api-security
tags:
- imported
- documents
- access-control
- command-injection
- business-logic
- api-security
language: en
raw_sha256: af5abca5a466ccd262b15395c19cf42079bc63d46bd48bad16de08a19fa34460
text_sha256: aa83eb548538eed9cdc20058974785327df0ed8e26e859f17667626021aba9de
ingested_at: '2026-06-28T07:31:58Z'
sensitivity: unknown
redactions_applied: false
---

# Facebook WhiteHat: Able to access group plan even after leaving the group

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2018-12-06_facebook-whitehat-able-to-access-group-plan-even-after-leaving-the-group.md
- Source Type: markdown
- Detected Topics: access-control, command-injection, business-logic, api-security
- Ingested At: 2026-06-28T07:31:58Z
- Redactions Applied: False
- Raw SHA256: `af5abca5a466ccd262b15395c19cf42079bc63d46bd48bad16de08a19fa34460`
- Text SHA256: `aa83eb548538eed9cdc20058974785327df0ed8e26e859f17667626021aba9de`


## Content

---
title: "Facebook WhiteHat: Able to access group plan even after leaving the group"
page_title: "Facebook WhiteHat: Able to access group plan details even after leaving the group."
url: "https://whitehatfamilyguy.blogspot.com/2018/12/able-to-access-facebook-group-plan-even.html"
final_url: "https://whitehatfamilyguy.blogspot.com/2018/12/able-to-access-facebook-group-plan-even.html"
authors: ["Family guy"]
programs: ["Meta / Facebook"]
bugs: ["Broken authorization", "Logic flaw"]
publication_date: "2018-12-06"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5542
---

###  Facebook WhiteHat: Able to access group plan details even after leaving the group. 

[ December 06, 2016  ](https://whitehatfamilyguy.blogspot.com/2018/12/able-to-access-facebook-group-plan-even.html "permanent link")

###  Facebook WhiteHat: Able to access group plan even after leaving the group.

###  **_Product/URL_ : **

###  https://www.facebook.com/messages/t/[group_messagesID]

###  _**Description and Impact**_

Facebook messages has an option to create group, where a user can add multiple friends to chat, plan share pictures together.

  

Whenever a user is not a part of the group, he is not allowed to see the updated information of the group.

  

However one can still access the group plan even when not in a group.

  

**_Peter, is it?_**

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEitcecAUQ7kpW6lvP6w5eePldAGx3tcEhV9TrhOW4GtxQbOqXyBJUjwrSWXcXgTIO06cZA5PKp7TUi1G_oQxM5zCS_P5cDNRy4SoEf6N259PQJzdAzrR0uVZtt04YZ5sxQSmKNcyEiN7vk/s400/giphy+%25282%2529.gif)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEitcecAUQ7kpW6lvP6w5eePldAGx3tcEhV9TrhOW4GtxQbOqXyBJUjwrSWXcXgTIO06cZA5PKp7TUi1G_oQxM5zCS_P5cDNRy4SoEf6N259PQJzdAzrR0uVZtt04YZ5sxQSmKNcyEiN7vk/s1600/giphy+%25282%2529.gif)

  

###  **_Reproduction Instructions/Proof of Concept_**

We have two test accounts, (test A) and (test B)

  

1\. Test A Creates a new Group, Test Group, add members.(test B, test C )

2\. Test A creates a plan in group, with date, venue and plan name.

3\. There is some argument between Test A and Test B, and Test B leaves the group.

4\. Test A and Test C decides to change the plan venue as Test B was already aware of the all plan details.

5\. Test A changes the plan venue and date, however Test B can see the plan updated information.

  

Ideally if one is not a part of the group he should not be able to see the updated changes in the plan.

###  _Impact:_

###  One who is not be a member of the group chat can see the updated details of the plan thus violating privacy feature of Facebook.

###  _**Timeline:**_

Reported on 03.02.2018

  

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj1Vc9jaBTBzSxUJriwECfn-nVge7acka87N5K6B8gcFdJi8wBfG-wPyzk7BnBo5WCfqJYHw2bbxgs6OxT30_PkXYPwKFpX30IOKSNh9qcx0ogSf92gwZXPzbXaimldKudsRdBvx1b7WL8/s400/Capture111.JPG)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj1Vc9jaBTBzSxUJriwECfn-nVge7acka87N5K6B8gcFdJi8wBfG-wPyzk7BnBo5WCfqJYHw2bbxgs6OxT30_PkXYPwKFpX30IOKSNh9qcx0ogSf92gwZXPzbXaimldKudsRdBvx1b7WL8/s1600/Capture111.JPG)

###  _Bounty:_

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj7V2hBRbTWzeHy_C4B5RUcJ59h7on4Qs4CjU1Rlxl-1P5-TPhphswRGNRiPqv0bRkAxgZdlwYahVq4_1SwLbysNnQ2aQ4Ko2nDDd8OEnyMVkh5Oy5UNX_xwSEcALoyiv8zwPOCXIUH3U4/s400/Capture2bb.JPG)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj7V2hBRbTWzeHy_C4B5RUcJ59h7on4Qs4CjU1Rlxl-1P5-TPhphswRGNRiPqv0bRkAxgZdlwYahVq4_1SwLbysNnQ2aQ4Ko2nDDd8OEnyMVkh5Oy5UNX_xwSEcALoyiv8zwPOCXIUH3U4/s1600/Capture2bb.JPG)

  

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiyNVXsdAMJecmvQUIdHpmULFkY5Giho2SnupKJ3F9dI4QEb2L7Rfohdo2doETtv1DY1c2t-0PYsDMnExbz_Vqfpkh6Iedk7diYxbavB4FpuYlq-D0SvP5Zb2yEw-yqHlruOaLej-uGlRI/s400/giphy+%25283%2529.gif)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiyNVXsdAMJecmvQUIdHpmULFkY5Giho2SnupKJ3F9dI4QEb2L7Rfohdo2doETtv1DY1c2t-0PYsDMnExbz_Vqfpkh6Iedk7diYxbavB4FpuYlq-D0SvP5Zb2yEw-yqHlruOaLej-uGlRI/s1600/giphy+%25283%2529.gif)

  

  

**Thanks Facebook Security for the quick resolution and an awesome program:**

**_./Family Guy_**

  

Share 

  * Get link
  * Facebook
  * X
  * Pinterest
  * Email
  * Other Apps

### Labels

[bugbounty](https://whitehatfamilyguy.blogspot.com/search/label/bugbounty) [facebook](https://whitehatfamilyguy.blogspot.com/search/label/facebook) [familyGuy](https://whitehatfamilyguy.blogspot.com/search/label/familyGuy) [whitehat](https://whitehatfamilyguy.blogspot.com/search/label/whitehat)

Labels: [bugbounty](https://whitehatfamilyguy.blogspot.com/search/label/bugbounty) [facebook](https://whitehatfamilyguy.blogspot.com/search/label/facebook) [familyGuy](https://whitehatfamilyguy.blogspot.com/search/label/familyGuy) [whitehat](https://whitehatfamilyguy.blogspot.com/search/label/whitehat)

Share 

  * Get link
  * Facebook
  * X
  * Pinterest
  * Email
  * Other Apps

### Comments

#### Post a Comment

[](https://www.blogger.com/comment/frame/181979799605168940?po=531934278096633664&hl=en&saa=85391&origin=https://whitehatfamilyguy.blogspot.com&skin=notable)
