---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2024-01-24_response-manipulation-lead-to-premium-feature-by-normal-user-reward-of-500.md
original_filename: 2024-01-24_response-manipulation-lead-to-premium-feature-by-normal-user-reward-of-500.md
title: Response Manipulation Lead To Premium Feature By Normal User Reward of $500
category: documents
detected_topics:
- access-control
- command-injection
tags:
- imported
- documents
- access-control
- command-injection
language: en
raw_sha256: d86c0c68dafc324060bd77931e7378387576c7ba331032763d8bd8d765d73930
text_sha256: 5b79e8c8b8330a96dc91775dff73068e16d563d4f9c8b883733352ab253c8208
ingested_at: '2026-06-28T07:32:30Z'
sensitivity: unknown
redactions_applied: false
---

# Response Manipulation Lead To Premium Feature By Normal User Reward of $500

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2024-01-24_response-manipulation-lead-to-premium-feature-by-normal-user-reward-of-500.md
- Source Type: markdown
- Detected Topics: access-control, command-injection
- Ingested At: 2026-06-28T07:32:30Z
- Redactions Applied: False
- Raw SHA256: `d86c0c68dafc324060bd77931e7378387576c7ba331032763d8bd8d765d73930`
- Text SHA256: `5b79e8c8b8330a96dc91775dff73068e16d563d4f9c8b883733352ab253c8208`


## Content

---
title: "Response Manipulation Lead To Premium Feature By Normal User Reward of $500"
url: "https://medium.com/@zikola1/response-manipulation-lead-to-premium-feature-by-normal-user-reward-of-500-43381f769ab1"
authors: ["Abdulrahman badawi (@zikolaasec)"]
bugs: ["HTTP response manipulation", "Privilege escalation", "Payment bypass"]
bounty: "500"
publication_date: "2024-01-24"
added_date: "2024-01-25"
source: "pentester.land/writeups.json"
original_index: 503
scraped_via: "browseros"
---

# Response Manipulation Lead To Premium Feature By Normal User Reward of $500

Response Manipulation Lead To Premium Feature By Normal User Reward of $500
Abdulrahman badawi
Follow
3 min read
·
Jan 25, 2024

536

3

Hello Hackers,

Today i will write about how i got my Second valid report and reward in Public program in BugCrowd

Allow me to introduce myself briefly, I am abdulrahman (https://www.linkedin.com/in/abdulrahman-badawi/), a Penetration Testing, Bug Bounty Hunter, and CTF player from Egypt. My journey in cybersecurity began with bugbountyhunter.com in two months, where I found more than 20 bugs. Additionally, I joined platforms such as Hack The Box, PortSwigger, and others to further enhance my skills.

Welcome to my write-up about a Broken Access control lead to premium feature by normal user

It took me three months to find the second bug After the first bug and because this

tip:

“always change in response from false to true you can find a magic”

Introduction:

So let’s Start, I can’t disclose any information about the target yet, because the report is not disclosed but we can call it: redacted.com

was offering some features to subscribers to the site, One of These features include deleting annoying ads that appear on the site.

So I tried more than one extension that deletes ads, but they are not deleted

At this moment, I remembered this advice: “Always change in response from false to true you can find a magic.”

I said why don’t I search the response for anything that contains the word false and change it to true

So I searched for the word false and found a lot, but I focused on something related to advertisements and found {“areAdsDisabled”:false} In the response

Get Abdulrahman badawi’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

I quickly went to Match and Replace in Burp suite and adjusted the settings as shown in the picture

Match and Replace

and I refreshed the page

Guess what….

Now we can browse the site without ads as a premium user using a regular user, and this will certainly cause financial loss for the company in two ways.
1- first is that the company will not profit from the sponsored ads that appear on the site
2 — second is that the user will not have to pay for a subscription to remove ads

Steps to reproduce:

1- run burp and login in website

2 — go to proxy options and go match and replace

3 — {{“areAdsDisabled”:false}} We change the value of this parameter to true in response body

4 — Now we do a refresh of the site and browse it and it will not show any ads

$$$
If you found the write-up insightful, feel free to share it !

Thanks for reading, and see you soon for a new write-ups.

Contact :

LinkedIn : https://www.linkedin.com/in/abdulrahman-badawi/

twitter : https://twitter.com/zikolaasec

bye bye
