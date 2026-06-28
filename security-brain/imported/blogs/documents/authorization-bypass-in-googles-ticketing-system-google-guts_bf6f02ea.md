---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-07-28_authorization-bypass-in-googles-ticketing-system-google-guts.md
original_filename: 2020-07-28_authorization-bypass-in-googles-ticketing-system-google-guts.md
title: Authorization bypass in Google’s ticketing system (Google-GUTS)
category: documents
detected_topics:
- access-control
- command-injection
- automation-abuse
- api-security
tags:
- imported
- documents
- access-control
- command-injection
- automation-abuse
- api-security
language: en
raw_sha256: bf6f02ea96bae37e96879f0a20e2f10979600bdff3ce861df559946af1453449
text_sha256: 5605f8216a52a0ddd31fa8a186075da5bd57981df0d0cd4ff11a391e95a1c624
ingested_at: '2026-06-28T07:32:02Z'
sensitivity: unknown
redactions_applied: false
---

# Authorization bypass in Google’s ticketing system (Google-GUTS)

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-07-28_authorization-bypass-in-googles-ticketing-system-google-guts.md
- Source Type: markdown
- Detected Topics: access-control, command-injection, automation-abuse, api-security
- Ingested At: 2026-06-28T07:32:02Z
- Redactions Applied: False
- Raw SHA256: `bf6f02ea96bae37e96879f0a20e2f10979600bdff3ce861df559946af1453449`
- Text SHA256: `5605f8216a52a0ddd31fa8a186075da5bd57981df0d0cd4ff11a391e95a1c624`


## Content

---
title: "Authorization bypass in Google’s ticketing system (Google-GUTS)"
url: "https://www.ehpus.com/post/authorization-bypass-in-google-s-ticketing-system"
final_url: "https://www.ehpus.com/post/authorization-bypass-in-google-s-ticketing-system"
authors: ["Zohar Shachar"]
programs: ["Google"]
bugs: ["Broken authorization"]
bounty: "1,337"
publication_date: "2020-07-28"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4375
---

# Authorization bypass in Google’s ticketing system (Google-GUTS)

  * zohar shachar
  * Jul 28, 2020
  * 6 min read

One of the first things you need to do when reporting bugs to Google under their VRP program is set up your ‘Supplier’ account. It’s something you do just once, before the first bounty is paid, and it is within this process that you set up your bank account and all other personal data that will be used for all future payouts (I’m focusing on VRP supplier accounts as these are the accounts I’m familiar with, but I assume the process and system is similar for all other types of suppliers for Google). This registration process is managed via a ticketing system called ‘Google-GUTS’. 

  

Tl;dr: an authorization bypass vulnerability in Google-GUTS allows you to update arbitrary tickets in the system and update other suppliers' data.

  

Tl:dr-2: It took 8 months and an onsite f2f meeting to convince Google’s team it was actually an issue :) 

  

**Finding the vulnerability**

The processes of setting up the account is completed in few simple steps (partially redacted following Google’s request, see Google’s response later in this blog):

  1. First, you start by filling your data (bank account, address, etc.) in Google’s ‘Supplier Enrollment Form’ here: https://services.google.com/sup******t/***. After sending the form, you receive an automated confirmation email from Google’s ticketing system with the summary of the data you entered. 

  2. Next, you are requested to forward the confirmation email you received to ‘****vrp@google.com’.

  3. Finally, you receive an automated email from ‘[ _ext-ticket@google.com_](mailto:ext-ticket@google.com) ’ letting you know your ticket has been created within ‘Google GUTS’. The ticket can be updated by both you and Google’s team by replying to the email.

It was early in 2019 when both me and my friend and colleague [_Moti Harmatz_](https://www.linkedin.com/in/moti-harmats-b232aa98/) started receiving our first bug bounty rewards from Google, and accordingly we both had to set up our supplier accounts around the same time. As we were struggling to understand all the financial angles involved we ended up talking about it quite a lot, and that was when we started realizing that something between step 2 and 3 in the above mentioned process was a bit ‘loose’. You send an email to one account (‘****vrp@google.com’), and it results in receiving an email from another system (Google GUTS) represented by another account (‘[ _ext-ticket@google.com_](mailto:ext-ticket@google.com) ’) notifying you about the creation of a ticket. Furthermore,you can update the ticket by replying to the email. Looking at this from a security perspective, two main questions pop in mind:

  1. How would the authorization be handled in this case? Would ‘Google GUTS’ hold a white list of email addresses allowed to update tickets?

  2. Even more curious, as all update requests are simple emails sent to ‘[ _ext-ticket@google.com_](mailto:ext-ticket@google.com) , how does ‘Google Guts’ even know which ticket it is that you’re trying to update?

It turns out the answer to question 2 is simpler than one might expect: The system distinguishes between tickets by looking at a 8-number ‘ticket ID’ provided in the email’s subject. And in case you wonder how difficult it is to guess these id’s, let me stop you right there - they are sequential. 

  

Oh, and regarding question 1? Turns out - there is simply no authorization mechanism, at all. Anyone can update any ticket, with a simple Email. What can go wrong?  ****

  

**Reporting to Google with a simple POC:**

These are, word-for-word, the recreation steps I reported to Google:

  1. With account1 (say alice@gmail.com) send an email to ****vrp@google.com.

  2. Alice will receive an email from 'Google Guts' (ext-ticket@google.com) that a new ticket was created. The email will have a ticket ID in the subject, in the form of t/XXXXXXXX (8 numbers).

  3. With account2 (say bob@gmail.com) send an email to ext-ticket@google.com, with the ticket id in the beginning of the email subject (subject: t/XXXXXXXX), and a malicious body of your choice (for example, asking for bank account details to be sent to bob's address along with other PII).

  4. Alice ticket will now be updated, and Alice will receive an email (from ext-ticket@google.com) saying the ticket was updated, with Bob's request.

[![](https://static.wixstatic.com/media/5527e6_78f7d78aed1a418895ada67e67e1b1b0~mv2.png/v1/fill/w_49,h_28,al_c,q_85,usm_0.66_1.00_0.01,blur_2,enc_avif,quality_auto/5527e6_78f7d78aed1a418895ada67e67e1b1b0~mv2.png)](https://static.wixstatic.com/media/5527e6_78f7d78aed1a418895ada67e67e1b1b0~mv2.png)

I went on explaining how the ID’s are simple increments and can be easily found by the attacker, and how these tickets tend to hold very sensitive data. I also gave an attack scenario where one hunter tries to update the bank account of another, to steal the bounties.

I sent the report, edged on my seat, waiting for ‘P0’ priority and sounds of emergency alarms. But that’s not exactly what happened.

  

**“Intended Behavior”**

Few hours after sending my report, the following arrived:

[![](https://static.wixstatic.com/media/5527e6_5085bca82c0e4a999e781bf3a8da4412~mv2.png/v1/fill/w_49,h_15,al_c,q_85,usm_0.66_1.00_0.01,blur_2,enc_avif,quality_auto/5527e6_5085bca82c0e4a999e781bf3a8da4412~mv2.png)](https://static.wixstatic.com/media/5527e6_5085bca82c0e4a999e781bf3a8da4412~mv2.png)

I was, for a lack of better word, baffled. How can this be? I mean, I would understand if it received a ‘duplicate’ flag as they seem to be aware of this, but ‘intended Behavior’? This is how the system **is meant** to operate, without any authorization checks?

  

Few further emails were exchanged between me and Google’s team, as I was sure we just misunderstood each other. At some point, I thought we reached a common ground:

[![](https://static.wixstatic.com/media/5527e6_178cedd1704349e5a2e29745628b88ba~mv2.png/v1/fill/w_49,h_14,al_c,q_85,usm_0.66_1.00_0.01,blur_2,enc_avif,quality_auto/5527e6_178cedd1704349e5a2e29745628b88ba~mv2.png)](https://static.wixstatic.com/media/5527e6_178cedd1704349e5a2e29745628b88ba~mv2.png)

As I understood it, there were some tickets that were indeed not meant to have authorization on them, but these ‘****vrp’ ones (the tickets that contain banking data), **were** supposed to be protected, so perhaps it wasn’t clear from my report that I can update **these** tickets. So I quickly sent a screenshot as requested (proving I can update any ticket, including the sensitive ones), but it was still a ‘no-go’. The submission remained as ‘intended behavior’, and I was told once more that Google is aware of the issue. 

  

At this point, I frankly gave up. I felt there was not much more I could do to push this further, as Google’s engineers are clearly seeing things different then I do. Disappointed and confused, I decided to let this go. 

  

**Google’s ESCAL8 and meeting f2f**

Months later, I was invited by Google to participate in a very cool event in Google’s offices in London called ‘ESCAL8’, along with fellow bug-hunters from the VRP program. [_It was truly a great experience_](https://twitter.com/GoogleVRP/status/1197449225405112320) of hacking, learning and mingling with fellow researchers and Google’s team. I was having a casual coffee with an engineer from Google, when I suddenly realized It was the same person with whom I was discussing this ticketing bug months before.

  

To my surprise, the engineer remembered the ticket clearly. Even more surprising, he too considered it a vulnerability, and said I should reopen the ticket. 

And there it was. More than 8 months after originally reported, I reopened the ticket and within a few days it was accepted as a bug.

  

[![](https://static.wixstatic.com/media/5527e6_61714ec8517b41fab1e8446495bd861b~mv2.png/v1/fill/w_49,h_17,al_c,q_85,usm_0.66_1.00_0.01,blur_2,enc_avif,quality_auto/5527e6_61714ec8517b41fab1e8446495bd861b~mv2.png)](https://static.wixstatic.com/media/5527e6_61714ec8517b41fab1e8446495bd861b~mv2.png)

Few days after that, a bounty was paid.

  

**Final thoughts**

I don’t know what changed between the original submission and the final decision 8 months later, but I know from experience that Google takes every submission seriously and professionally. Perhaps something changed policy-wise. From my part, I consider this as a ‘glitch in the Matrix’, and chunk most of it to my poor explanation skills. 

  

This last paragraph was the original end for this blog post. But then, shortly before publication I reached out to Google (just to have their ‘OK’). To my surprise, Google’s team asked me to censor some parts in the post and to include the following comment:

  

**Google’s team response**

 _“Thank you once again for partnering with Google and sharing your report on potential vulnerabilities in our ticketing systems._

_While Google has a robust set of automated and manual verification mechanisms in place to mitigate risk in financial requests, we are continuously evaluating our workflows to identify improvements to ensure user safety and data privacy._

_With regard to vulnerabilities in our finance operations, updates to our supplier records go through a multi-step automated and human-review process post a request from external partners. In addition, we are working to further improve the restrictions on the ability for outside parties to update interactions to further reduce risk in this space in response to the vulnerabilities highlighted.”_

  

From this response I understand better why Google’s security team was a bit reluctant to treat this as a bug, as it seems that a fix is not straight forward considering the legitimate product requirements. The choice is therefor to handle the risk via other, non technological compensating security mechanisms. Nonetheless, I’m happy that the efforts paid out. Hopefully, this publication might assist a bit more in getting a fix rolling.

  

**Timeline:**

  * 03/06/2019 Issue reported to Google

  * 03/06/2019 Google marked the issue as ‘intended behavior’

  * 03/27/2019 Last email exchange between me and Google team, when I decided to let the issue go. 

  * 11/01/2019 Following ESCAL8 convention I reopen the ticket

  * 11/05/2019 bug accepted by Google

  * 11/19/2019 reward (1337$) was issued
