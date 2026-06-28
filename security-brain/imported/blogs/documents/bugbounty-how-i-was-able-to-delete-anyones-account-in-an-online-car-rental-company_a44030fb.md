---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2018-01-14_bugbounty-how-i-was-able-to-delete-anyones-account-in-an-online-car-rental-compa.md
original_filename: 2018-01-14_bugbounty-how-i-was-able-to-delete-anyones-account-in-an-online-car-rental-compa.md
title: '#BugBounty — How I was able to delete anyone’s account in an Online Car Rental
  Company'
category: documents
detected_topics:
- command-injection
- otp
- csrf
- business-logic
- api-security
tags:
- imported
- documents
- command-injection
- otp
- csrf
- business-logic
- api-security
language: en
raw_sha256: a44030fb79d81db29d5d5dc3c874b4eb5e56c1d1e70fcc2ee5603b5a4580879a
text_sha256: a54e87d268251f3849f510a58d265ba7e1029bfd76fc890d50caeb231a2253a5
ingested_at: '2026-06-28T07:31:56Z'
sensitivity: unknown
redactions_applied: false
---

# #BugBounty — How I was able to delete anyone’s account in an Online Car Rental Company

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2018-01-14_bugbounty-how-i-was-able-to-delete-anyones-account-in-an-online-car-rental-compa.md
- Source Type: markdown
- Detected Topics: command-injection, otp, csrf, business-logic, api-security
- Ingested At: 2026-06-28T07:31:56Z
- Redactions Applied: False
- Raw SHA256: `a44030fb79d81db29d5d5dc3c874b4eb5e56c1d1e70fcc2ee5603b5a4580879a`
- Text SHA256: `a54e87d268251f3849f510a58d265ba7e1029bfd76fc890d50caeb231a2253a5`


## Content

---
title: "#BugBounty — How I was able to delete anyone’s account in an Online Car Rental Company"
page_title: "#BugBounty — How I was able to delete anyone’s account in an Online Car Rental Company | by Avinash Jain (@logicbomb) | InfoSec Write-ups"
url: "https://medium.com/bugbountywriteup/bugbounty-how-i-was-able-to-delete-anyones-account-in-an-online-car-rental-company-8a4022cc611"
authors: ["Avinash Jain (@logicbomb_1)"]
bugs: ["CSRF", "Parameter tampering"]
publication_date: "2018-01-14"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 6012
scraped_via: "browseros"
---

# #BugBounty — How I was able to delete anyone’s account in an Online Car Rental Company

Avinash Jain (@logicbomb)
Follow
2 min read
·
Jan 14, 2018

347

4

#BugBounty — How I was able to delete anyone’s account in an Online Car Rental Company

Hi Guys,

One more interesting finding that I recently discovered in a popular online car rental company. Some parameter manipulation combined with CSRF resulted into disabling account of any user. Let’s see how it was done —

So it comes to me as surprise, I was going through “Update Profile” functionality to find some bug and then I saw something fishy in the request. Parameter “method” :)

Press enter or click to view image in full size
Original HTTP Request

The original value going in the “method” parameter was “put” which suggest creating a new resource or replaces a representation of current resource with the requested data and then I knew what to do next — I just changed that value to method “delete” (HTTP DELETE request method deletes the specified resource) and forwarded it. As expected , account was gone,it was deleted! (and in actual there was no such functionality in the portal which allow user to deactivate his account) .

Now the next challenge was to do the same thing but to other user’s account . I tried , searched, dig into various areas but all was going into vain then I tried the most basic thing- CSRF . If you notice the above request, you will find “csrf_token” going in the post body. Just to check whether the token was getting validated or not , I removed the token value and forwarded the request and I got “200 OK”. Whoaa!

Get Avinash Jain (@logicbomb)’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Below is the CSRF exploit-

And on some more analysis, I came across that this was the only form where CSRF token was not getting validated- Most common case of weak CSRF implementation. :)

Report details-

08-Dec-2017 — Bug reported to the concerned company.

29-Dec-2017 — Bug was marked fixed.

01-Jan-2018 — Re-tested and confirmed the fix.

07-Jan-2018 — Awarded by company.

Thanks for reading!

~Logicbomb (https://twitter.com/logicbomb_1)
