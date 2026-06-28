---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2017-07-19_business-logic-vulnerabilities-series-a-brief-on-abusing-invitation-systems.md
original_filename: 2017-07-19_business-logic-vulnerabilities-series-a-brief-on-abusing-invitation-systems.md
title: 'Business Logic Vulnerabilities Series: A brief on Abusing Invitation Systems'
category: documents
detected_topics:
- business-logic
- idor
- access-control
- command-injection
- mfa
- otp
tags:
- imported
- documents
- business-logic
- idor
- access-control
- command-injection
- mfa
- otp
language: en
raw_sha256: 110a0528de56ca4fe211e3c1acf1914c4c79b8a6ebe406243f5ba8db45d1c9e0
text_sha256: 6e3353c7bf66e4b97238ff314e24228bb168358779a16210acb1df5256710f77
ingested_at: '2026-06-28T07:31:56Z'
sensitivity: unknown
redactions_applied: false
---

# Business Logic Vulnerabilities Series: A brief on Abusing Invitation Systems

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2017-07-19_business-logic-vulnerabilities-series-a-brief-on-abusing-invitation-systems.md
- Source Type: markdown
- Detected Topics: business-logic, idor, access-control, command-injection, mfa, otp
- Ingested At: 2026-06-28T07:31:56Z
- Redactions Applied: False
- Raw SHA256: `110a0528de56ca4fe211e3c1acf1914c4c79b8a6ebe406243f5ba8db45d1c9e0`
- Text SHA256: `6e3353c7bf66e4b97238ff314e24228bb168358779a16210acb1df5256710f77`


## Content

---
title: "Business Logic Vulnerabilities Series: A brief on Abusing Invitation Systems"
page_title: "Business Logic Vulnerabilities Series: A brief on Abusing Invitation Systems – Seekurity"
url: "https://www.seekurity.com/blog/general/business-logic-vulnerabilities-series-a-brief-on-abusing-invitation-systems/"
final_url: "https://seekurity.com/blog/2017/07/19/ali-kabeel/general/business-logic-vulnerabilities-series-a-brief-on-abusing-invitation-systems"
authors: ["Ali Kabeel"]
programs: ["Meta / Facebook"]
bugs: ["Logic flaw"]
publication_date: "2017-07-19"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 6148
---

Hi Guys,  
I am Ali Kabeel an Application Security Intern at Seekurity team. This is my first blog i hope you like it. In this blog post I will be mainly focusing on Business Logic vulnerabilities by offering some tips and tricks on how to abuse invitation systems using real-world examples from my Facebook Bug Bounty experience but first let’s get a general knowledge about some concepts.

###### First, What are “Business Logic Vulnerabilities”? _-OWASP_

A [business logic vulnerability](https://www.owasp.org/index.php/Business_Logic_Security_Cheat_Sheet) is one that allows the attacker to misuse an application by circumventing the business rules. Most security problems are weaknesses in an application that result from a broken or missing security control (authentication, access control, input validation, etc…). By contrast, business logic vulnerabilities are ways of using the legitimate processing flow of an application in a way that results in a negative consequence to the organization.

Many articles that describe business logic problems simply take an existing and well understood web application security problem and discuss the business consequence of the vulnerability. True business logic problems are actually different from the typical security vulnerability. Too often, the business logic category is used for vulnerabilities that can’t be scanned for automatically. This makes it very difficult to apply any kind of categorization scheme. A useful rule-of-thumb to use is that if you need to truly understand the business to understand the vulnerability, you might have a business-logic problem on your hands. If you don’t understand the business, then it’s probably just a typical application vulnerability in one of the other categories.

For example, an electronic bulletin board system was designed to ensure that initial posts do not contain profanity based on a list that the post is compared against. If a word on the list is found the submission is not posted. But, once a submission is posted the submitter can access, edit, and change the submission contents to include words included on the profanity list since on edit the posting is never compared again.

Testing for business rules vulnerabilities involves developing business logic abuse cases with the goal of successfully completing the business process while not complying with one or more of the business rules.

###### What are “Invitation Systems”?

Invitation systems are a type of systems used in many parts of web applications such as groups, pages,invitations to join a website,etc… Beside the normal [CSRF](https://www.owasp.org/index.php/Cross-Site_Request_Forgery_\(CSRF\)) and [IDOR](https://www.owasp.org/index.php/Testing_for_Insecure_Direct_Object_References_\(OTG-AUTHZ-004\)) that may exist in such systems and may lead to their abuse; There are other [business logic flaws](https://www.owasp.org/index.php/Testing_for_business_logic) that you need to watch out for when creating/testing such a system.

###### What are the components of an invitation system?

An invitation system normally have 2 main components The person sending the invitation and the invitee.That only happens in systems that are really simple more complicated systems may have more than one type of invitations such as inviting to be admin, moderator, editor, analyst, etc… In an ideal invitation system the invitation must be Invitee specific,Privilege specific, used for one time , don’t follow a certain pattern in generation so not predictable, not easy to be brute forced and can’t be impersonated such that accepting a friend request from somebody who never invited me or joining a group that you were never invited to by an admin.

###### Example of abusing an invitation system:

Consider somebody sending you an invitation through email from website ([seekurity.com](https://seekurity.com/)) to join a group on that site invitation may look like: https://www.seekurity.com/group_id=123&Sender_id=456&member_type=1&token=KKKKKKK . Abusing such an invite is based on some questions:

1.Can I change group_id to join any group?  
2.Can I change Sender_id to bypass for example admin approvals?  
3.Can I change memeber_type and join as an admin rather than member? 4.Is the token predictable? Can it be brute forced? 5.Is the invitation specific to invitee,can it be used by another account? 6.Can more than one person use it to join the group? 7.Is the invitation reusable like joining and leaving a group whenever wanted? If the invitation system is applying correct logic the invitation must be like in an ideal system described above.

### Breaking Facebook invitation system! :

###### Bug#1: Abusing Facebook invite to site feature:

Back in 2015 I discovered the endpoint [facebook.com/invite.php](https://www.facebook.com/login.php?next=https%3A%2F%2Fwww.facebook.com%2Finvite.php) the end point was used to send invitations to join Facebook and was used initially when Facebook was small site to invite your friends to join it.The system send and email to invitee .This invitation is used to sign up and most importantly add the sender as friend.The bug existed in the invitations system as the invitee could abuse this in multiple of ways: 1.Anybody can use this invitation not the invitee only (Missing best practice).  
2.Invitation can be used with more than one person (Adding many people as friends to sender ).  
3.Invitation could be used to make sender a friend any number of times.That is to say I unfriend and then add sender as friend any number of times I want.

A detailed Video showing the bug can be seen [here:](https://www.youtube.com/watch?v=fS6XJZb7JxQ)

###### Bug#2: Abusing Facebook invite to group by email feature:

In 2016 I Found out about Invite to groups by the bug was vulnerable to abuse because with only one invitation many people could be added to the group and this indeed bypass admin approvals in some cases.Consider the case where the invitation sender is the group admin, the invitee can use one invite to add many people to the group thus bypassing admin approvals.

This was indeed another case of failing invitations system that you can find more about [here:](https://www.youtube.com/watch?v=XURhMKsfEes)

###### Bug#3: Bypassing protection in Facebook invite to group by email feature:

Facebook fixed Bug#2 by making invitations email specific.That is to say the person with the email(The email that was invited) verified in his account is the only person that can accept the invite.That was bypassed using the following steps:

1\. Get an invite link on email [[email protected]](/cdn-cgi/l/email-protection).  
2\. Add this email to your account and confirm it.  
3\. Load invite link “ONLY LOADING” do not accept it.  
4\. Remove email and then log out.  
5\. Log into another account that you own.  
6\. Add the email [[email protected]](/cdn-cgi/l/email-protection).  
7\. Load the invite link and accept the invite (first account added).  
8\. Log out and go to the first account that you loaded the invite into.  
9\. Go to the group link.  
10\. You will find the banner asking you to confirm or deny the invite.  
11\. Press confirm  
12\. BOOM account 2 added  
13\. Steps 3 to 5 can be repeated any number of times.

I hope you find that blog useful.Thanks for reading!!

## **A minute if you please!**

Building a website, an application or any kind of business? Or already have one? Worried about your security? Think twice before going public and let us [protect your business](https://www.seekurity.com/#pricing)!

[](https://www.addtoany.com/add_to/facebook?linkurl=https%3A%2F%2Fseekurity.com%2Fblog%2F2017%2F07%2F19%2Fali-kabeel%2Fgeneral%2Fbusiness-logic-vulnerabilities-series-a-brief-on-abusing-invitation-systems&linkname=Business%20Logic%20Vulnerabilities%20Series%3A%20A%20brief%20on%20Abusing%20Invitation%20Systems "Facebook")[](https://www.addtoany.com/add_to/pinterest?linkurl=https%3A%2F%2Fseekurity.com%2Fblog%2F2017%2F07%2F19%2Fali-kabeel%2Fgeneral%2Fbusiness-logic-vulnerabilities-series-a-brief-on-abusing-invitation-systems&linkname=Business%20Logic%20Vulnerabilities%20Series%3A%20A%20brief%20on%20Abusing%20Invitation%20Systems "Pinterest")[](https://www.addtoany.com/add_to/twitter?linkurl=https%3A%2F%2Fseekurity.com%2Fblog%2F2017%2F07%2F19%2Fali-kabeel%2Fgeneral%2Fbusiness-logic-vulnerabilities-series-a-brief-on-abusing-invitation-systems&linkname=Business%20Logic%20Vulnerabilities%20Series%3A%20A%20brief%20on%20Abusing%20Invitation%20Systems "Twitter")[](https://www.addtoany.com/add_to/whatsapp?linkurl=https%3A%2F%2Fseekurity.com%2Fblog%2F2017%2F07%2F19%2Fali-kabeel%2Fgeneral%2Fbusiness-logic-vulnerabilities-series-a-brief-on-abusing-invitation-systems&linkname=Business%20Logic%20Vulnerabilities%20Series%3A%20A%20brief%20on%20Abusing%20Invitation%20Systems "WhatsApp")[](https://www.addtoany.com/add_to/telegram?linkurl=https%3A%2F%2Fseekurity.com%2Fblog%2F2017%2F07%2F19%2Fali-kabeel%2Fgeneral%2Fbusiness-logic-vulnerabilities-series-a-brief-on-abusing-invitation-systems&linkname=Business%20Logic%20Vulnerabilities%20Series%3A%20A%20brief%20on%20Abusing%20Invitation%20Systems "Telegram")[](https://www.addtoany.com/add_to/linkedin?linkurl=https%3A%2F%2Fseekurity.com%2Fblog%2F2017%2F07%2F19%2Fali-kabeel%2Fgeneral%2Fbusiness-logic-vulnerabilities-series-a-brief-on-abusing-invitation-systems&linkname=Business%20Logic%20Vulnerabilities%20Series%3A%20A%20brief%20on%20Abusing%20Invitation%20Systems "LinkedIn")[](https://www.addtoany.com/add_to/google_gmail?linkurl=https%3A%2F%2Fseekurity.com%2Fblog%2F2017%2F07%2F19%2Fali-kabeel%2Fgeneral%2Fbusiness-logic-vulnerabilities-series-a-brief-on-abusing-invitation-systems&linkname=Business%20Logic%20Vulnerabilities%20Series%3A%20A%20brief%20on%20Abusing%20Invitation%20Systems "Gmail")[](https://www.addtoany.com/share)

Abusing  brief  Business  Invitation  Logic  on  Series  Systems  Vulnerabilities
