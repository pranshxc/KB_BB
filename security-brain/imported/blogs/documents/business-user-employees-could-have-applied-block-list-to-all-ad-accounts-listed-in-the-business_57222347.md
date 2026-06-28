---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2019-06-17_business-user-employees-could-have-applied-block-list-to-all-ad-accounts-listed-.md
original_filename: 2019-06-17_business-user-employees-could-have-applied-block-list-to-all-ad-accounts-listed-.md
title: Business user Employees could have applied block list to all ad accounts listed
  in the business manager.
category: documents
detected_topics:
- access-control
- command-injection
- otp
- business-logic
tags:
- imported
- documents
- access-control
- command-injection
- otp
- business-logic
language: en
raw_sha256: 57222347144d3d93c8484170151194f2988c1037e9371abce88579c95bdb027e
text_sha256: a68971f8b3257fd85bb6bec2fa1167a7ee98124b17521f7c59ec30c4aa33c1ac
ingested_at: '2026-06-28T07:31:59Z'
sensitivity: unknown
redactions_applied: false
---

# Business user Employees could have applied block list to all ad accounts listed in the business manager.

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2019-06-17_business-user-employees-could-have-applied-block-list-to-all-ad-accounts-listed-.md
- Source Type: markdown
- Detected Topics: access-control, command-injection, otp, business-logic
- Ingested At: 2026-06-28T07:31:59Z
- Redactions Applied: False
- Raw SHA256: `57222347144d3d93c8484170151194f2988c1037e9371abce88579c95bdb027e`
- Text SHA256: `a68971f8b3257fd85bb6bec2fa1167a7ee98124b17521f7c59ec30c4aa33c1ac`


## Content

---
title: "Business user Employees could have applied block list to all ad accounts listed in the business manager."
url: "https://medium.com/@rohitcoder/business-user-employees-can-add-edit-change-or-apply-block-list-to-a-business-account-7b3e8aae667e"
authors: ["Rohit kumar (@rohitcoder)"]
programs: ["Meta / Facebook"]
bugs: ["Broken authorization", "Logic flaw"]
bounty: "500"
publication_date: "2019-06-17"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5202
scraped_via: "browseros"
---

# Business user Employees could have applied block list to all ad accounts listed in the business manager.

Business user Employees could have applied block list to all ad accounts listed in the business manager.
Rohit kumar
Follow
4 min read
·
Jun 18, 2019

113

Press enter or click to view image in full size

Summary: During BountyCon 2019 in Singapore, after getting multiple NA & Informative reports. I was digging Business manager more deeply and I noticed that it was possible to apply block list settings to the all ad accounts in a business manager account by an employee.

This writeup contains nothing fancy. Just simple conversation between me & Facebook employees.

Video PoC

What you submitted

31 Mar

Title

Business user Employees can add/edit/change or apply block list to a business account.

Vuln Type

Privacy / Authorization

Product Area

Facebook — Web

Description/Impact

Description
===
According to fb documentation — https://www.facebook.com/business/help/442345745885606

Facebook employees are not authorized to add,edit or change any data of any business manager account.

But, here a business user employee can add edit or delete csv,txt block list and he can also apply this same setting to all ad account or specified ad accounts.

In short:
A Facebook business manager-employee can manage the block list completely.

Impact
===
A business employee can add or edit block list and apply it.

Repro steps

Steps
===
1. Create business manager account
2. Add any employee
3. From employee account, you simply need to visit this link -https://business.facebook.com/block_lists?business_id=YOUR_BUSINESS_ID_HERE
4. From, here you can add, edit or change block list.
5. This link is accessible only from https://business.facebook.com/settings/block-lists?business_id=BUSINESS_ID (But, this link is not accessible to employees)
6. So, for exploiting this you can visit or type this link manually https://business.facebook.com/block_lists?business_id=YOUR_BUSINESS_ID_HERE and do every step as if you were admin.

I recently reported a bug a few months back where this kind of link was accessible without any protection (Fb was just hiding link) — Report id — #900076046855556

Now, I hope this is not intended behavior

Thanks,
Rohit Kumar

31 Mar

Hi Rohit,

Thank you for reporting this to us. Currently, this is intended behavior as employees are supposed to be able to create and edit blocks lists and apply them to ad accounts that you manage. This could be an issue if you can edit someone else’s block list or apply yours to other ad accounts that you do not manage. Hope that makes sense.

Thanks,

Hortons
Security

Your Reply

31 Mar

Hi, I am able to apply this block list to all ad accounts of current business manager. (This is not allowed from employee account)

Reproduce:
Send a request to this endpoint

https://graph.facebook.com/v3.2/block_list_id/auto_applied_businesses?access_token=CURRENT_ACCESS_TOKEN_FROM_YOUR_ACCOUNT

POST BODY

_reqName: object:blocklistID/auto_applied_businesses
_reqSrc: AdsBLApplyActions
business_id: BUSINESS_ID_HERE
is_auto_blocking_on: true
locale: en_GB
method: post
pretty: 0
suppress_http_code: 1

Check attached Screenshot for more info

Attachments

Screen Shot 2019–03–31 at 6.12.48 PM.png

Your Reply

10 Apr

Anyone is looking at this report?
Note: Please change the title of this report to
“Employee can apply block list to all ad accounts of business manager”

11 Apr

Hi Rohit,

The way I understand this is that if an admin gets demoted while on the block-list page the mutation would still succeed for some reason.

I’m having difficulties in reproducing this since if you wait a bit longer the mutation fails, so my guess is that what you were seeing is just a timing issue. Are you still having success in reproducing this issue consistently?

Thanks,

Hortons
Security

Your Reply

Get Rohit kumar’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

11 Apr

Hi Hortons,
I don’t think there is a problem with timings. I checked mutation after 1 hour and the mutation was working!
I checked properties of my access_token via https://developers.facebook.com/tools/debug/accesstoken and it shows my access_token will never expire so i don’t think this could happen.

I Checked it after 1 hour.

Thanks,
Rohit Kumar

Attachments

Screen Shot 2019–04–11 at 6.20.51 PM.png

11 Apr

Hi Rohit,

Can you provide the testing accounts/businesses/block lists you used to reproduce this? Your configuration might be a bit different than mine.

Thanks,

Hortons
Security

Your Reply

11 Apr

Hi Hortons,

Please use attached credentials for verifying this vulnerability.
And please also check detailed video PoC for more clarification.

////////////// CREDENTIALS Starts Here ///////////////

Business name —█████
Business ID — █████

1st Admin with admin access (This is very old admin with full access)
========================
Username — █████
Password — █████

2nd Admin with admin access (This is new admin so use this to shift this user to employee or admin every-time from 1st Admin account)
========================
Username — █████
Password — █████

///////////////// CREDENTIALS ENDS Here ///////////////////

Follow this video — If you need more info let me know.
Video PoC — https://www.youtube.com/watch?v=RkpdYKTIsbU&feature=youtu.be

Thanks,
Rohit Kumar

Your Reply

28 Apr

Hi Hortons,

You were able to reproduce this issue?

Thanks,
Rohit Kumar

10 May

Hi Rohit,

Thank you for being patient with us, we managed to reproduce and root cause. We are sending it to the appropriate product team for further investigation. We will keep you updated on our progress.

Regards,

Hortons
Security

Your Reply

14 Jun

Hi Hortons,

Any updates on this report?

Thanks,
Rohit kumar

Yesterday

Hi Rohit,

We have looked into this issue and believe that the vulnerability has been patched. Please let us know if you believe that the patch does not resolve this issue. We will follow up regarding any bounty decisions soon.

Thanks,

Hortons
Security

Your Reply

Yesterday

Hi Hortons,

Yes, I believe this vulnerability has been patched.

Thanks,
Rohit Kumar

Thanks,

Rohit Kumar
