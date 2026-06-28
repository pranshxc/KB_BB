---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2018-10-03_facebook-bug-bounty-email-id-phone-number-can-be-exposed-through-business-manage.md
original_filename: 2018-10-03_facebook-bug-bounty-email-id-phone-number-can-be-exposed-through-business-manage.md
title: 'Facebook Bug Bounty: Email Id, Phone Number Can be exposed Through Business
  Manager'
category: documents
detected_topics:
- password-reset
- otp
- sso
- access-control
- command-injection
- path-traversal
tags:
- imported
- documents
- password-reset
- otp
- sso
- access-control
- command-injection
- path-traversal
language: en
raw_sha256: 40bab1055de94b2d6cb7242b6a9663739ae787aa0c991c67dfda19b00dff6c9b
text_sha256: 6f1f0924acf706e0599b354aa00b0ba4cd83b611e003959025fee03b7b32b326
ingested_at: '2026-06-28T07:31:57Z'
sensitivity: unknown
redactions_applied: false
---

# Facebook Bug Bounty: Email Id, Phone Number Can be exposed Through Business Manager

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2018-10-03_facebook-bug-bounty-email-id-phone-number-can-be-exposed-through-business-manage.md
- Source Type: markdown
- Detected Topics: password-reset, otp, sso, access-control, command-injection, path-traversal
- Ingested At: 2026-06-28T07:31:57Z
- Redactions Applied: False
- Raw SHA256: `40bab1055de94b2d6cb7242b6a9663739ae787aa0c991c67dfda19b00dff6c9b`
- Text SHA256: `6f1f0924acf706e0599b354aa00b0ba4cd83b611e003959025fee03b7b32b326`


## Content

---
title: "Facebook Bug Bounty: Email Id, Phone Number Can be exposed Through Business Manager"
url: "https://medium.com/@rohitcoder/email-id-phone-number-can-be-exposed-through-business-manager-e79b970ea288"
authors: ["Rohit kumar (@rohitcoder)"]
programs: ["Meta / Facebook"]
bugs: ["Logic flaw", "Information disclosure"]
bounty: "3,000"
publication_date: "2018-10-03"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5667
scraped_via: "browseros"
---

# Facebook Bug Bounty: Email Id, Phone Number Can be exposed Through Business Manager

Facebook Bug Bounty: Email Id, Phone Number Can be exposed Through Business Manager
Rohit kumar
Follow
11 min read
·
Oct 3, 2018

242

2

Press enter or click to view image in full size
Money $$$$ 👊

Facebook Hall of Fame Award https://www.facebook.com/whitehat/thanks/

Whitehat Report #786259078237254

ACTIVITY

What you submitted

30 May

Title

Email Id, Phone Number Can be exposed Through Business Manager

Vuln Type

Privacy / Authorization

Product Area

Facebook — Web

Description/Impact

Description
===
PoC Video — https://youtu.be/WiTb1NrWRss

Using this Vulnerability Any attacker can expose primary email id or phone number of any user from its friend list.

Attacker can expose those primary mail id or phone number in any privacy setting mode. It doesn’t matter whats the privacy settings are — only me, friends or public

Impact
===

Attacker can access private details of any user (In some circumstances Attacker & vicitm should be connected on facebook) on facebook like primary email, phone number.

Remember?
When you try forgot password option facebook shows you email and phone hint like this
We send a Otp on this Id fa*****@gmail.com or +9195*******3

Notice *** Are masked values now you can expose it.

Repro steps

Testing Methodology
=====
I am using my friend’s user account and my account for testing purpose with consents and approvals.

Setup
===
You need facebook page, business manager account

Steps
===
1. Endpoint URL — https://graph.facebook.com/v2.10/[PAGE-ID-HERE]?access_token=[TOKEN-FROM-YOUR-BUSINESS-MANAGER]&__business_id=[BUSINESS-ID-HERE]&_reqName=object%3Apage&fields="id","name","global_brand_page_name","page_user_with_leads_access","category","link","locations.fields(id).limit(1)","is_published","is_verified","userpermissions.fields(user,business,business_persona,role)","business","picture.type(square)","global_brand_root_id"]&locale=en_GB&method=get&pretty=1&suppress_http_code=1

2. Modify these 3 parameters in above URL

[PAGE-ID-HERE] => Enter Your Facebook Page ID
[TOKEN-FROM-YOUR-BUSINESS-MANAGER] => Get token of your Account from Business Manager Panel
[BUSINESS-ID-HERE] => Your Business Account ID Here

Now for testing purpose Go to page roles tab of your page now add any victim from your friend list. That will be added soon. Victim will not get any notification for any approval or something like that.

Now just visit above endpoint URL with proper parameters you can see Email iD, phone number of your victim. If vicitm’s privacy is set to “only me” still you can see email id, phone number

What to do if victim is not in your friend list?
Just add him/her through page roles tab. They will get notification for accepting invitation after accepting invitation you can see email id, phone number.

Our reply

30 May

Hi,

Thanks for reporting a security issue. Your report number is 786259078237254. Please give us reasonable time to investigate and mitigate the issue before sharing information with others, and note that we reserve the right to publish your report. (More details: https://www.facebook.com/whitehat/.) Note that if you’re writing to us in a language other than English, we’ll only be able to respond in English at this time. We’re sorry for any inconvenience this may cause.

If you’re trying to report another issue, please review the information below to get help.

- If your account or a friend’s account is sending out suspicious links: https://www.facebook.com/help/hacked
- To report abuse: https://www.facebook.com/help/reportlinks
- To report bugs that are not security issues: https://www.facebook.com/help/www/326603310765065
- For any other questions or concerns, please visit our Help Centre: https://www.facebook.com/help

Thanks,
Facebook Security

Your Reply

30 May

Hi Team,
I just wanted to give you new update. So, in this above current scenario i showed you how a page admin/ business manager account user can expose email id and phone number of any friend/person.

Now, another one update is if my partner admin will remove me from that page admin roles than still i can get email and phone number of people who are in admin roles of that page using my business account access_token

I tried it with other pages but its not working with other pages still am trying to find is this problem with access_token expiration time or something else.

If it’s access_token expirty then i want to mention that after removing myself from admin role i used new fresh access_token from business manager account and at that time i was able to see email, phone numbers

Thanks,
Rohit Kumar

Attachments

Capture.PNG

Our reply

1 Jun

Hi Rohit,

Thanks for your report but this might be intended functionality. If you navigate here you should be able to see the same information:https://business.facebook.com/settings/people?business_id=%5BID%5D&nav_source=mega_menu

Can you describe why you think this is security a vulnerability?

Thanks,

Stephen
Security

Your Reply

1 Jun

HI Stephen,

Thanks for your reply,
I checked your above link and while finding this bug i think i was on this same page. I want to mention that this might be intended functionality but do you really think you need to mention primary email/phone in “page_user_with_leads_access” field?

No, because in that page we need only admin role details, ids and other stuffs not some sensitive stuffs like email and phone. Because may be any user doesn’t want to expose his/her mail and phone but still you are showing it in that api link even after “only me” privacy.

After getting your reply, I started Googling for same kind of previous report in facebook reported by any other researcher and i found this report — http://roy-castillo.blogspot.com/2013/07/how-i-exposed-your-primary-facebook.html?m=1

This may lead to some catastrophic issues. Take example if you want to open my facebook account you don’t know my password you will try facebook reset password option there you will get email/phone hint and you can clarify which primary mail and phone i am using. With this bug.

Using this bug we are able to expose any user’s primary email,phone without any user’s interaction just add them in page roles and visit that API link then BINGO!
You can also spoof my mails and you can use it for phishing or other suspicious activities.

You know another one tricky & interesting thing?
I found a way to add multiple peoples in admin roles tab one by one using my custom made script and after adding that user, my script will extract his/her primary email/phone and in same way i can extract lot of emails and phone numbers of different users.

So, i think this is really a security vulnerability.

So, what should be mitigation?

Well, i think you should remove primary email, phone from “page_user_with_leads_access” field.

Thanks,
Rohit Kumar

Your Reply

1 Jun

Hi Stephen,

I think you should take a short look at this report https://sensorstechforum.com/facebook-bug-primary-email-address-user/ this will really clarify you why this is a security vulnerability. Few researchers already reported this kind of bug in groups via admin roles section and here am reporting it in business page manager via admin roles tab.

If you are having any more question. Feel free to ask me i will try to reply you as soon as possible.

Thanks,
Rohit Kumar

Our reply

5 Jun

Hi Rohit,

Since the attacker needs to be Admin of a business account and Page, and the victim needs to approve the Role invite we don’t consider this a security issue. This is a pretty high bar for entry and not something that can be exploited at scale. We appreciate your efforts but this finding doesn’t appear to qualify.

Thanks,

Stephen
Security

Your Reply

5 Jun

Hi Stephen,
I would like to mention that victim is not getting any approval button if victim is connected with attacker on facebook. So, was thinking this is a good idea but right now victim is not getting any button for approval th3y are getting added directly please have a look again.

Thanks,
Rohit kumar

Your Reply

5 Jun

And so creating automated scripts for gathering lot of private mails from my 3,000 friend list will be very easy for me because they aren’t getting any button for approval.

Get Rohit kumar’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

You should give them a button and something like consent screen that you are sharing some personal information like email, phone

Thanks

Your Reply

5 Jun

I would request you to check once again,

Here whats happening after adding anyone as admin or editor
Victim is just getting one notification “you were added by Rohit kumar as editor” and after i remove victim from page roles notification also gets deleted. So, this is one of the best way to collect 1,000 and so on.. emails and phone numbers after getting all informations victim can remove everyone no one knows what happened.

You should give a consent screen or approval button victim is not getting any page role approval button.

I already mentioned how i exposed multiple emails, phone numbers using simple script if you want i would like to share that script with you. That script will expose all emails & phone numbers of lot of emails & after that script will also remove all notifications from their respective accounts.

Thanks,
Rohit Kumar

Your Reply

6 Jun

Any updates?
Or you are looking for any more info?
Thanks,
Rohit Kumar

Our reply

12 Jun

Hi Rohit,

Thank you for reporting this information to us. We are sending it to the appropriate product team for further investigation. We will keep you updated on our progress.

Thanks,

Aaron
Security

Our reply

16 Jun

Hi Rohit,

We have looked into this issue and believe that the vulnerability has been patched. Please let us know if you believe that the patch does not resolve this issue. We will follow up regarding any bounty decisions soon.

Thanks,

Aaron
Security

Your Reply

16 Jun

Hi Aaron,

Yes Vulnerability has been patched and now it’s not showing any email or phone numbers.

But i just want to give you some extra information we’ve a group of bug bounty hunters on facebook and few peoples are trying to purchase bugs from hunters see attached snapshot!

I can confirm vulnerability has been patched.

Attachments

Screenshot_2018–06–16–13–47–21–901_com.facebook.mlite.png

Your Reply

18 Jun

Hi Aaron,

I want to mention another one thing using this vulnerability I was able to expose any user’s email and phone number only because facebook is not giving a approval button to another person.

So this finding was not limited to only expose email of admins only i was exposing email, phone number of any user.

While finding this bug I added multiple person as admin and at the same time I was able to access all emails and phone numbers. It will be good if you will add a limitation like approval button.

If attacker will add user ‘A’ as admin then user ‘A’ will get a button to approve that request without approval attacker can’t do anything so you need to fix this also to mitigate future issues.

Because without approval button I was able to collect emails and phone numbers of victim silently after removing the victim from admin roles notification was also deleted from victim’s account. So, there was no clue what attacker did with victims account.

I hope you will also fix it soon!

Thanks,
Rohit Kumar

Our reply

20 Jun

Hi Rohit,

Thanks for sharing this! It is expected that adding someone on your friends list won’t require an approval on the page role request. Please follow up if you have further questions. We’ll send out your bounty information shortly.

Thanks,

Aaron
Security

Our reply

20 Jun

Hi Rohit Kumar,

After reviewing this issue, we have decided to award you a bounty of $3000. Below is an explanation of the bounty amount. Facebook fulfills its bounty awards through Bugcrowd.

This could have let a malicious Business Manager Admin expose the primary email (or phone number) of any friend regardless of their email privacy settings, and possibly non-friends if the victim approves the attacker’s invite request.

Thank you again for your report. We look forward to receiving more reports from you in the future!

== Claim Your Bounty ==

You can claim this bounty with Bugcrowd by following this bounty URL: [LINK REDACTED]

When you visit the above URL, you will have the option to create a new Bugcrowd account or claim the bounty using an existing Bugcrowd account (if you are already logged in). The URL to claim this bounty expires after 30 days. Please contact support@bugcrowd.com you were unable to claim your bounty during this period.

Before it’s claimed, the URL is not associated with your Bugcrowd account. Please treat it as you would treat your password and do not share the URL with anyone.

== Donate to Charity ==

If you wish to donate your bounty to a recognized charitable organization, please do not click the claim link. Notify us by replying to this message with the charity of your choice. All charity donations will be matched by Facebook.

== Frequently Asked Questions ==

Please visit the Payouts FAQ at https://www.facebook.com/whitehat/faq/ for more information related to your bounty.

Thanks,
The Facebook Security Team

Your Reply

20 Jun

Thanks,

For this Bounty
Can i get listed here Please https://www.facebook.com/whitehat/thanks/ ?

Thanks,
Rohit Kumar

Your Reply

20 Jun

Please list me here https://www.facebook.com/whitehat/thanks/

Name — Rohit Kumar (@rohitcoder)
Link — https://facebook.com/rohitcoder

If you need any more information please let me know

Thanks,
Rohit

Our reply

20 Jun

Hi Rohit,

I’ve updated our hall of fame page with your name and Facebook link but am not able to add (@rohitcoder). You may change your link to Twitter, or a different link of your choosing. We push updates to the external hall of fame page a few times per month and we don’t have a set schedule. Next time we update that page you’ll see your requested changes. Thanks again for participating in the Whitehat program.

Thanks,

Stephen
Security

Your Reply

2 Jul

Hi Team!

You can close this report :)

Thanks,
Rohit Kumar
