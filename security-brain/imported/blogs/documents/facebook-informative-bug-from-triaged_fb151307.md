---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2019-07-17_facebook-informative-bug-from-triaged.md
original_filename: 2019-07-17_facebook-informative-bug-from-triaged.md
title: Facebook Informative Bug From Triaged
category: documents
detected_topics:
- rate-limit
- command-injection
- password-reset
tags:
- imported
- documents
- rate-limit
- command-injection
- password-reset
language: en
raw_sha256: fb151307c5b0f286a6a2be8e5039c0c7e393ff4db9894a93780355c68ab880b6
text_sha256: 7b21e28b2dfdf990469015684fc9e42b48a9b17d7052852234cf2f401bcbf64c
ingested_at: '2026-06-28T07:31:59Z'
sensitivity: unknown
redactions_applied: false
---

# Facebook Informative Bug From Triaged

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2019-07-17_facebook-informative-bug-from-triaged.md
- Source Type: markdown
- Detected Topics: rate-limit, command-injection, password-reset
- Ingested At: 2026-06-28T07:31:59Z
- Redactions Applied: False
- Raw SHA256: `fb151307c5b0f286a6a2be8e5039c0c7e393ff4db9894a93780355c68ab880b6`
- Text SHA256: `7b21e28b2dfdf990469015684fc9e42b48a9b17d7052852234cf2f401bcbf64c`


## Content

---
title: "Facebook Informative Bug From Triaged"
url: "https://medium.com/@circleninja/facebook-informative-bug-from-triaged-76738e4d5938"
authors: ["Circle Ninja (@circleninja)"]
programs: ["Meta / Facebook"]
bugs: ["Lack of rate limiting"]
publication_date: "2019-07-17"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5142
scraped_via: "browseros"
---

# Facebook Informative Bug From Triaged

Facebook Informative Bug From Triaged
Ronnie Joseph
Follow
2 min read
·
Jul 17, 2019

15

1

With some of my other stories, I liked to include my personal feelings and views too, thinking it will make a connect with readers. Since then, hardly anything changed and it is making me seem like “unprofessional in Infosec”. So all posts from now will directly reflect real responses and content.

This bug is from Facebook whitehat program which got triaged and even went for the discussion for payout (after confirmed fix) and later said as not worth Mark’s money.

Bug- No Rate Limiting During FB Page Email Confirmation

The GET request for email confirmation in facebook pages is something like this

GET /pg/Lukas-1220909788091763/about/?conf_code=id&email_id=xyz%40gmail.com

Here if we send this to intruder and i used multiple numerical sequences to confirm the email with code which was sent , we find that all request gives an 302 redirect.

One of the redirects will successfully confirm the new mail.

Impact-

Get Ronnie Joseph’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Any page can verify and list email address without confirmation which comes to email account. No rate limiting so any script can be made to see that 302 responses back to browser and confirm the mail for any page.

Timeline- Submitted 18 June

Managed to Reproduce- 20 June

6 July- Sent to product team for fix

13 July- Fixed and asked for confirmation and asked to wait for bounty decision.

17 July- Sad Reply

“Thank you for sharing this information with us. After discussing with the bug bounty team, we’ve determined that this issue does not qualify for a bounty.The reason is that the email verification indicator on Pages is not really used and is currently only visible to the admin.Although this issue does not qualify as a part of our bounty program we appreciate your report. We will follow up with you on any security bugs or with any further questions we may have.”

Me- Asked some clarification. Ok. Glad it’s not N/A . Or else it would be in hindi, “Jale pe namak chidkna” .

Don’t expect POC for unpaid bugs. GO AWAY! :P

Join as writer to share your story in this publication. Contact me on twitter. Bye.
