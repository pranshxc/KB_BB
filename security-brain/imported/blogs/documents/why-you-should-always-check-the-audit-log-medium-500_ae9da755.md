---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-05-20_why-you-should-always-check-the-audit-log-medium-500.md
original_filename: 2023-05-20_why-you-should-always-check-the-audit-log-medium-500.md
title: Why You Should Always Check The Audit Log [Medium] — $500
category: documents
detected_topics:
- access-control
- idor
- command-injection
- information-disclosure
- api-security
- mobile-security
tags:
- imported
- documents
- access-control
- idor
- command-injection
- information-disclosure
- api-security
- mobile-security
language: en
raw_sha256: ae9da755809326e29086b1fd323295e79daa2ee4eb5fbe42a235d76f433f5367
text_sha256: 05044a257423d8b8c5c168ed90f0743f89cb34f4fb4ac4c5fdde820c7d429aa5
ingested_at: '2026-06-28T07:32:21Z'
sensitivity: unknown
redactions_applied: false
---

# Why You Should Always Check The Audit Log [Medium] — $500

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-05-20_why-you-should-always-check-the-audit-log-medium-500.md
- Source Type: markdown
- Detected Topics: access-control, idor, command-injection, information-disclosure, api-security, mobile-security
- Ingested At: 2026-06-28T07:32:21Z
- Redactions Applied: False
- Raw SHA256: `ae9da755809326e29086b1fd323295e79daa2ee4eb5fbe42a235d76f433f5367`
- Text SHA256: `05044a257423d8b8c5c168ed90f0743f89cb34f4fb4ac4c5fdde820c7d429aa5`


## Content

---
title: "Why You Should Always Check The Audit Log [Medium] — $500"
url: "https://emanuel-beni.medium.com/why-you-should-always-check-the-audit-log-medium-500-80a778bfbcd6"
authors: ["Emanuel Beni Harijanto"]
bugs: ["Information disclosure"]
bounty: "500"
publication_date: "2023-05-20"
added_date: "2023-05-22"
source: "pentester.land/writeups.json"
original_index: 1133
scraped_via: "browseros"
---

# Why You Should Always Check The Audit Log [Medium] — $500

Why You Should Always Check The Audit Log [Medium] — $500
Emanuel Beni Harijanto
Follow
4 min read
·
May 20, 2023

222

1

Disclaimer: Due to the program’s policy, the company in this write-up will be redacted. Don’t forget to read my previous Bug Bounty Writeup —Privilege Escalation from Improper Access Control [Medium] — $700. Thank you for your time!

Press enter or click to view image in full size
Photo by Markus Spiske on Unsplash

Discovering a bug should not always be a complicated process. Vulnerabilities like Information Disclosure, IDOR, etc. require us, security researchers, to be more attentive to identifying unusual responses rather than focusing on the technicality aspect of the web application. Discovering a simple hard-coded Secret API Key might score you up to a High severity report. In this blog post, I will discuss how I found an endpoint that discloses ‘supposedly’ non-sensitive information on a well-known Cyber Security Company. I was able to score a Medium and earn $500 by discovering this simple Information Disclosure bug.

What is Information Disclosure?

CWE-200 Information Disclosure, also known as the Exposure of Sensitive Information to an Unauthorized Actor is a type of vulnerability where sensitive information is unintentionally shared with the public or unauthorized parties. The scope of sensitive information does not only cover traditional sensitive information like Passwords, Secret API Keys, etc. but information like Support PIN, Recovery Code, and even Invitation Links can be considered sensitive information if discovered by the wrong actor.

Understanding Your Target

Before we start, it is essential for us to have a good understanding of our target web application in order to discover more bugs. Having a deep-down understanding of how the web application flows and what type of features are implemented in the web application is an asset to security researchers. This can be done by merely surfing through the web application at the beginning of our pentest and taking notes on features, functions, and flow of the web application and what type of vulnerability might arise from there. This will get you into a stronger position than other security researchers working on the program.

The Journey to $$$

As mentioned in the previous paragraph, I took my time and did my due diligence to understand my target web application and discovered a very common feature implemented in the web application, the Audit Log feature. The Audit Log feature is a very common feature implemented by companies in order to record detailed historical information of events and changes made to the account. Exploring the feature further, I noticed that almost all events are recorded in the audit log along with their details. For example, when inviting a new user, the audit log displays the event type along with invited user details (email address, name, time, etc.) This information might seem useless now, but I will show you how this can be capitalized in the future.

Get Emanuel Beni Harijanto’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Proceeding with my pentest, I discovered another very common feature that most companies have, the Invitation Link feature. In this case, the Invitation Link feature allows administrator users to generate an invitation link that can be used to invite other users to the organization. Knowing that the company has an Audit Log feature, I immediately try to generate a new invitation link and check whether the detail is disclosed on the Audit Log page. To my surprise, the Audit Log feature does indeed disclose the actual invitation link.

Now, we have connected the 2 different features together and have confirmed that the invitation link is indeed disclosed in the Audit Log. At this point, we should focus on how we could use the relationship of the 2 features to generate a bug. I would recommend every security researcher to use the ‘What Ifs’ method. The point here is to challenge your brain and ask as many What if questions that pose a security threat to the web application. The ‘What Ifs’ questions that came into my mind were the following:

- What if we delete an active invitation link and are still able to access it from the audit log?
- What if we override an active invitation link and still be able to access the overridden, presumably deleted, invitation link from the audit log?
- What if a lower privilege user, i.e. Read-Only User, could view the Audit Log page and use the invitation link to escalate privilege?

After exhausting all possible scenarios that might lead up to a bug, test them one by one. Fortunately, my third point turned out to be true. I created a new Read-Only account and was successful in accessing the Audit Log page. As you know, a read-only account should not have the ability to invite other users to the organization, but since the full invitation link is disclosed in the Audit Log page and we were able to access it, a Read-Only account could invite other users to the organization.

After confirming the vulnerability, I immediately report the bug to the Program’s page on HackerOne. Thankfully, the report was graded as a Medium severity report, and shortly after I was rewarded $500.

From this report, I learned that it is really important for us to have a deep-down understanding of our target. In addition, I learned that sensitive information ranges from passwords, Secret API Keys to even invitation links if accessed by the wrong actors. Technicality-wise, there is no fancy programming involved, no sophisticated payload bypass and etc. I just simply understand how the web application works and what might be considered sensitive information. I hope we can all learn from this report!

Thank you once again for reading this blog post. Don’t forget to read my other write-up, Privilege Escalation from Improper Access Control [Medium] — $700, drop a clap and comment. Thank you and have a great day y’all!
