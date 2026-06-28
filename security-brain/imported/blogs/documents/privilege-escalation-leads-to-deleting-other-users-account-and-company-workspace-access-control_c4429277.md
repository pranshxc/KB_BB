---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-12-14_privilege-escalation-leads-to-deleting-other-users-account-and-company-workspace.md
original_filename: 2022-12-14_privilege-escalation-leads-to-deleting-other-users-account-and-company-workspace.md
title: Privilege escalation leads to deleting other user’s account and company Workspace
  [Access Control]
category: documents
detected_topics:
- access-control
- xss
- sqli
- command-injection
- automation-abuse
- information-disclosure
tags:
- imported
- documents
- access-control
- xss
- sqli
- command-injection
- automation-abuse
- information-disclosure
language: en
raw_sha256: c4429277ddfc728b55814c00b0536867dc2f303ae05c27348ceef58080ac6cb3
text_sha256: c881deaa3e2df0ebddfd29b5a7ad8ff116d3b831b9fb42cb5db1ca5cf7d10654
ingested_at: '2026-06-28T07:32:16Z'
sensitivity: unknown
redactions_applied: false
---

# Privilege escalation leads to deleting other user’s account and company Workspace [Access Control]

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-12-14_privilege-escalation-leads-to-deleting-other-users-account-and-company-workspace.md
- Source Type: markdown
- Detected Topics: access-control, xss, sqli, command-injection, automation-abuse, information-disclosure
- Ingested At: 2026-06-28T07:32:16Z
- Redactions Applied: False
- Raw SHA256: `c4429277ddfc728b55814c00b0536867dc2f303ae05c27348ceef58080ac6cb3`
- Text SHA256: `c881deaa3e2df0ebddfd29b5a7ad8ff116d3b831b9fb42cb5db1ca5cf7d10654`


## Content

---
title: "Privilege escalation leads to deleting other user’s account and company Workspace [Access Control]"
url: "https://medium.com/@h4ck3rp4tik/privilege-escalation-leads-to-deleting-other-users-account-and-company-workspace-access-control-7b709eb88ef"
authors: ["Pratik Gaikwad"]
bugs: ["Privilege escalation", "Broken Access Control"]
bounty: "400"
publication_date: "2022-12-14"
added_date: "2022-12-15"
source: "pentester.land/writeups.json"
original_index: 1780
scraped_via: "browseros"
---

# Privilege escalation leads to deleting other user’s account and company Workspace [Access Control]

Privilege escalation leads to deleting other user’s account and company Workspace [Access Control]
Pratik Gaikwad
Follow
4 min read
·
Dec 14, 2022

121

1

Dear Folks!

Interesting heading?? It took me 15 minutes to think about the heading. Leave Just Kidding ;)

I’m excited to start this Article and share my interesting finding. I hope this can provide some insights into Privilege Escalation.

Welcome
1st Article Formalities:

~$root@pratik: whoami

Working as a Security Consultant in Blockchain Infrastructure, knowing DAO, DApps, Defi, Cex, and Dex. Having experience in Vulnerability Assessment Penetration Testing, Security Consulting, and Web 3.0

Huh! cool!

Let’s start this Article!

According to Wikipedia:

Privilege escalation is the act of exploiting a bug, a design flaw, or a configuration oversight in an operating system or software application to gain elevated access to resources that are normally protected from an application or user. The result is that an application with more privileges than intended by the application developer or system administrator can perform unauthorized actions.

Summary:

As usual, I started testing an application for the low-hanging fruits (reconnaissance) using Nuclei.

I tried XSS, SQLi, and Information disclosures, using automation but no luck.

I also tried Visual Recon using aquatone but didn’t find any suspicious screenshots. (Still no luck!)

GitHub - michenriksen/aquatone: A Tool for Domain Flyovers
A Tool for Domain Flyovers. Contribute to michenriksen/aquatone development by creating an account on GitHub.

github.com

So, it’s time to visit the web application manually.

As usual, I have created two accounts A’ and ‘B. I was testing the login and logout flow. I noted extra functionalities of the application so I could check those features manually later.

While browsing manually, I found that the application has a feature to create a workspace and many features like creating and managing APIs like payment APIs.

I created a workspace and also created a few important APIs. I noticed the ‘Invite Your Team’ to join your work feature. And I sent an invitation to my other email id to join the same workspace.

Now I Have 3 members in my team (including the Owner).

1 → Owner (Admin)

2 → Account A (Normal User)

3 → Account B (Normal User)

Press enter or click to view image in full size

After that, I tried various attack scenarios with Admin and Normal User accounts.

Meanwhile, testing the normal user flow, I visited current plan endpoint (`/account/subscription`).

Get Pratik Gaikwad’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

I noticed there’s a function called Change plan. I was shocked because the application allowed normal users to change their workspace plans.

Now here’s the main game. There was a button called `Downgrade a plan.`

Press enter or click to view image in full size

I clicked on Downgrade and saw something weird warning saying, `you will lose your entire work.` They also mentioned that ‘Account B’ and other teammates will be permanently deleted.

I went ahead and clicked Downgrade and Boooom!!!!

— -> The entire Work has been deleted

— -> All the APIs were deleted, including important payment APIs.

— -> `Account A` and `Account B` were permanently deleted (not only from the workspace but they also lost their main account)

Press enter or click to view image in full size

Interesting thing:

I went to the Admin dashboard (logged in) and was surprised because all the work was deleted including other teammates from the admin dashboard.

Haha! Now an admin was also downgraded to the normal plan. A 1-month Free trial for admin ended just by one click by a normal user.

Impact:

An entire organization suffered data loss because of a normal user.

To chain this Vulnerability, I mentioned one more Business logic bug that, after deleting, creating, or modifying the workspace settings, an admin was not receiving any email notification.

So, the admin has no idea what went wrong with his workspace.

What you learned here??

— -> Always make a note of extra features of the application

— -> Observe the behavior and try to visit each endpoint manually

What have Companies learned here?

— -> They should not give unnecessary access to normal users.

Thank you for taking the time to read my blog. I really appreciate your interest in my thoughts and opinions, and I’m glad that you found them engaging and worthwhile. I hope you continue to enjoy reading my blog in the future.

I’m open to suggestions and feedback, so please feel free to reach out and let me know what you’d like to see more of.

LinkedIn Profile: https://www.linkedin.com/in/pratikgaikwad3/

Timeline:

Report Date: THU, 25 NOV 2021 5:09:55 PM GMT+05:30
Accepted: FRI, 26 NOV 2021 7:51:24 AM GMT+05:30
Bounty: $400
Extra: Extra Marks for good handwriting ;)

Press enter or click to view image in full size
Bounty ;)
Good Bye……
