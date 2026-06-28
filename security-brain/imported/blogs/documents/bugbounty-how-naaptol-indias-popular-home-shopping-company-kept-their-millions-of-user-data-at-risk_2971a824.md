---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2018-09-07_bugbounty-how-naaptol-indias-popular-home-shopping-company-kept-their-millions-o.md
original_filename: 2018-09-07_bugbounty-how-naaptol-indias-popular-home-shopping-company-kept-their-millions-o.md
title: '#BugBounty — How Naaptol (India’s popular home shopping company) Kept their
  Millions of User Data at Risk!'
category: documents
detected_topics:
- idor
- sso
- command-injection
tags:
- imported
- documents
- idor
- sso
- command-injection
language: en
raw_sha256: 2971a8243ce953bb572d5c66eb18baedf4ae1684a6713faf247deedf9f73f864
text_sha256: 0c93a11b7afacc9223e5a2d94fcf2f003a70dfa3c45e2813246bedf6b2c09bd3
ingested_at: '2026-06-28T07:31:57Z'
sensitivity: unknown
redactions_applied: false
---

# #BugBounty — How Naaptol (India’s popular home shopping company) Kept their Millions of User Data at Risk!

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2018-09-07_bugbounty-how-naaptol-indias-popular-home-shopping-company-kept-their-millions-o.md
- Source Type: markdown
- Detected Topics: idor, sso, command-injection
- Ingested At: 2026-06-28T07:31:57Z
- Redactions Applied: False
- Raw SHA256: `2971a8243ce953bb572d5c66eb18baedf4ae1684a6713faf247deedf9f73f864`
- Text SHA256: `0c93a11b7afacc9223e5a2d94fcf2f003a70dfa3c45e2813246bedf6b2c09bd3`


## Content

---
title: "#BugBounty — How Naaptol (India’s popular home shopping company) Kept their Millions of User Data at Risk!"
url: "https://medium.com/@logicbomb_1/bugbounty-how-naaptol-indias-popular-home-shopping-company-kept-their-millions-of-user-data-e414cd4151c"
authors: ["Avinash Jain (@logicbomb_1)"]
programs: ["Naaptol"]
bugs: ["IDOR"]
publication_date: "2018-09-07"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5721
scraped_via: "browseros"
---

# #BugBounty — How Naaptol (India’s popular home shopping company) Kept their Millions of User Data at Risk!

#BugBounty — How Naaptol (India’s popular home shopping company) Kept their Millions of User Data at Risk!
Avinash Jain (@logicbomb)
Follow
3 min read
·
Sep 7, 2018

246

5

Hi Guys,

This particular hack is from my initial days of bugbounty hunting and the main reason to pick this up from the vault is not to describe the technique used to find the vulnerability but -

To expose and highlight the poor security standards in the IT industry and bring to the attention , the major security loopholes which are left unattended even by big firms and spread awareness among companies to take information security as importantly as any other branch.

Let’s see what was the complete scenario-

Just like every online shopping website has the functionality of allowing the user to select the address where he wants to ship the product, Naaptol was also having the same thing-

Press enter or click to view image in full size
Shipping Address HTTP request during payment

and the response of the above request contains the address including user complete details associated with that address id.

Press enter or click to view image in full size
User Address Details

And here’s loading a classic case of Insecure Direct Object Reference (IDOR) , I changed the address id to some other number (which is found to be incremental) from 17917835 to 17917837 and without any surprise, I was able to see full details of other user associated with that ID, which includes sensitive details like victim’s full name, complete address, mobile number etc.

Press enter or click to view image in full size
Accessing other user details
Press enter or click to view image in full size
Accessing other user details

and then I run intruder , bruteforced the address id and was able to fetch complete details of a large number of users of Naaptol.

Press enter or click to view image in full size
Naaptol User Details

It is also sad to see that still many companies fail to appreciate and acknowledge the efforts of ethical hackers who are trying to make the internet a safer place to surf. With the intent and hope that such articles create a positive change in bringing information security upfront.

Report details-

Get Avinash Jain (@logicbomb)’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

05-May-2016 — Notified the Naaptol team via mail.

Conversation dropped by Naaptol team in between.

Later vulnerability found to be fixed.

06-June-2016 — Notified the team for the responsible disclosure

Thanks for reading!

~Logicbomb ( https://twitter.com/logicbomb_1 )
