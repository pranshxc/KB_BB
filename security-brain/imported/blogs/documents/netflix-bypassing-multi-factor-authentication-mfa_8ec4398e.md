---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-04-30_netflix-bypassing-multi-factor-authentication-mfa.md
original_filename: 2023-04-30_netflix-bypassing-multi-factor-authentication-mfa.md
title: Netflix — Bypassing Multi-Factor Authentication (MFA)
category: documents
detected_topics:
- mfa
- rate-limit
- sso
- command-injection
- path-traversal
- automation-abuse
tags:
- imported
- documents
- mfa
- rate-limit
- sso
- command-injection
- path-traversal
- automation-abuse
language: en
raw_sha256: 8ec4398e496e2b9bc9ccbed8d457ef16f5e969e0bdbd5dc9f53209275d23fcc0
text_sha256: c3db7e24f4d7ee7acc70588a859307bd18e68339bf759bceb99d1ed5bf16192e
ingested_at: '2026-06-28T07:32:20Z'
sensitivity: unknown
redactions_applied: false
---

# Netflix — Bypassing Multi-Factor Authentication (MFA)

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-04-30_netflix-bypassing-multi-factor-authentication-mfa.md
- Source Type: markdown
- Detected Topics: mfa, rate-limit, sso, command-injection, path-traversal, automation-abuse
- Ingested At: 2026-06-28T07:32:20Z
- Redactions Applied: False
- Raw SHA256: `8ec4398e496e2b9bc9ccbed8d457ef16f5e969e0bdbd5dc9f53209275d23fcc0`
- Text SHA256: `c3db7e24f4d7ee7acc70588a859307bd18e68339bf759bceb99d1ed5bf16192e`


## Content

---
title: "Netflix — Bypassing Multi-Factor Authentication (MFA)"
url: "https://ltsirkov.medium.com/netflix-bypassing-multi-factor-authentication-mfa-53135c9d6d50"
authors: ["Lyubomir Tsirkov (@lyubo_tsirkov)"]
programs: ["Netflix"]
bugs: ["2FA / MFA bypass"]
publication_date: "2023-04-30"
added_date: "2023-05-04"
source: "pentester.land/writeups.json"
original_index: 1210
scraped_via: "browseros"
---

# Netflix — Bypassing Multi-Factor Authentication (MFA)

Netflix — Bypassing Multi-Factor Authentication (MFA)
Lyubomir Tsirkov
Follow
7 min read
·
Apr 29, 2023

154

1

Press enter or click to view image in full size
Introduction

During my participation in Netflix Bug Bounty Program, I discovered a vulnerability that allowed me to bypass their Multi-Factor Authentication (MFA) implemented on the “Change Email” endpoint.

This was possible due to the existence of alternative method for changing the email address that didn’t require completing the MFA process.

This finding was rated as P3 in Bugcrowd.

I would like to thank Netflix for allowing me to publish this report. This vulnerability has been patched and the fix is rolled out.

Understanding Netflix MFA

When logging into your Netflix account, you can update your email address at this URL: https://netflix.com/email. Upon visiting this link, you will be redirected to the /mfa endpoint, which requires identity verification before any changes can be made.

Verification options include receiving a code via email, phone number or providing the credit card number associated with your account.

Press enter or click to view image in full size
help.netflix.com
Press enter or click to view image in full size
https://netflix.com/mfa

This means that if you manage to steal someone’s credentials, you would still need to complete the MFA process to change the email address and take over their account completely.

Some common MFA/2FA bypass techniques include the following:
1. Response Manipulation.
2. Direct Request to the endpoint.
3. Missing 2FA Code Integrity Validation.
4. Lack of Brute-Force Protection / Rate Limiting.
5. 2FA Code Leakage in Response.

None of these worked in that case. Due to this reason I considered the MFA endpoint secured at this stage of the testing.

TL;DR

In this blog post, I present a finding where an alternative endpoint “/extramember/create-credentials” on Netflix lacked Multi-Factor Authentication (MFA), making it possible for users to change their email address without completing any additional verification steps.

Reported Steps to Reproduce

1. Navigate to https://www.netflix.com/YourAccount and select “Change Email”.
2. You will encounter the MFA page — https://www.netflix.com/mfa.
3. To bypass this, visit “https://www.netflix.com/extramember/create-credentials".
4. Complete the form using the new email address and password, then click Next.
5. You will be redirected to https://netflix.com, and your email address and password will be updated without requiring MFA.

Discovering Phase — Long Path

Netflix offers certain features to specific countries. Therefore, my strategy initially involved exploring their “Help Center” to collect more information about the available features and the corresponding countries where they are accessible.

At this stage, I created some automation to go over Netflix Help Center pages and examine their titles to identify any interesting features.

One particular caught my attention: “Extra Member.”
Link: https://help.netflix.com/en/node/123279/cl

At the time of the testing, this feature was available only for the following countries:

Peru
Chile
Nepal

It means that in order to get access to that functionality, you would need to register from one of those countries and pay for subscription.

To test it, I tried with IP addresses from all those three countries and successfully registered a new account.

To proceed with paying the subscription, for some countries, it’s also possible to buy Gift Cards from a third-party website and use them during the payment process in Netflix, however, in that case for those three countries I didn’t find a way to do buy any gift card.

Eventually, I gave up on trying to pay for the subscription as none of the payment methods worked.

Company Announcement— A few weeks later

While being engaged in a Bug Bounty program, I believe it’d be beneficial if you subscribe for the company’s newsroom so you can receive news about the recent changes and introducing new features.

In Netflix case, I noticed that the following article was released on 08 February, 2023.

Get Lyubomir Tsirkov’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Link: https://about.netflix.com/en/news/an-update-on-sharing

“So over the last year, we’ve been exploring different approaches to address this issue in Latin America, and we’re now ready to roll them out more broadly in the coming months, starting today in Canada, New Zealand, Portugal and Spain. Our focus has been on giving members greater control over who can access their account.”

An update regarding “Extra Member” feature was introduced in the article. It says that the feature is available additionally to the following countries:

Canada
New Zealand
Portugal
Spain

It still wasn’t available for the country where I’m currently located in, but knowing that new information, I decided to try to register from one of the aforementioned countries and pay for subscription again.

Registering an account

If you try to use a well-known VPN service, registering for a new account may prove to be difficult, as the VPN’s IP address may have been used for creating numerous registrations and subsequently landed on a blocklist. In such a scenario, attempting to register on Netflix.com would result in an error message “Something went wrong”.

In my case, I had an IP from Spain which wasn’t any well-known VPN service.

Unfortunately, it wasn’t enough because once you register with an IP from some of these countries, you will need to use some of the following methods to pay for the subscription:

PayPal
Debit Card
Gift Card

Again, I tried Paypal and a few debit cards to pay for the subscription, however, it failed again giving me error “Something Went Wrong”.

Finally, I decided to use Gift Card method. In Netflix, when you are using IP from Spain and go to Gift Card page you will notice that you can buy Gift Card from the following website: startselect.com

Note: Buying Gift cards depends on the country as well. For Spain, it seems that startselect.com is available.

Press enter or click to view image in full size
https://www.netflix.com/es/gift-cards

What I did was to open https://startselect.com/es-es/tarjeta-regalo-netflix-variable/42228 and register.

Press enter or click to view image in full size
Buying Voucher from StarSelect.com

Unfortunately, having registration on startselect.com wasn’t enough. I needed to go through verification check on that website which included:

Taking a selfie holding a list of paper on which I wrote “Netflix.com” and the amount of the voucher — in my case 25 Euro

Anyway, I did it for the sake of getting my hands on that feature.

Ready to use the Gift Card.

Finally! I registered with Spain IP and used recently bought Spain Gift Card.

The following feature was unlocked:

Press enter or click to view image in full size
Extramember feature.

Having access to that functionality I decided to find all possible endpoints related to it. I inspected main JS files and discovered multiple endpoints related to “Extra Member”.

)), (0, M.default) (j, J, (H = {
  }, (0, M.default) (H, et.ADD_ON_DECLINE_INVITE, '/extramember/declineinvitation'), 
  (0, M.default) (H, et.ADD_ON_DECLINE_CONFIRM, '/extramember/declineconfirmed'), 
  (0, M.default) (H, et.ADD_ON_ACTIVATE_ERROR, '/extramember/error'), 
  (0, M.default) (H, et.ADD_ON_ACTIVATE_INVITE_ACCEPTED_ERROR, '/extramember/accepted-error'), (0, M.default) (H, et.ADD_ON_ACTIVATE_INVITE_INVALID_ERROR, '/extramember/invalid-error'), (0, M.default) (H, et.ADD_ON_CLAIM_REGISTRATION_CONTEXT_ERROR, '/extramember/claim-error'), (0, M.default) (H, et.ADD_ON_ACTIVATE_CONTEXT, '/extramember/activate'), (0, M.default) (H, et.ADD_ON_PASSWORD_CONTEXT, '/extramember/context'), 
  (0, M.default) (H, et.ADD_ON_LOGIN_CREDENTIALS_SETUP_CONTEXT, '/extramember/activate-credentials'), 
  (0, M.default) (H, et.ADD_ON_CLAIM_REGISTRATION_SETUP_CONTEXT, '/extramember/claim'), 
  (0, M.default) (H, et.ADD_ON_PASSWORD_CREATION, '/extramember/createpassword'), 
  (0, M.default) (H, et.ADD_ON_LOGIN_CREDENTIALS_SETUP, '/extramember/create-credentials'), 
  (0, M.default) (H, et.ADD_ON_CLAIM_REGISTRATION_SETUP, '/extramember/claim-setup'), 
  (0, M.default) (H, et.ADD_ON_REGISTRATION, '/extramember/registration'), 
  (0, M.default) (H, et.ADD_ON_PROFILE_SELECTION, '/extramember/profileselection'), 
  (0, M.default) (H, et.PASSWORD_ENTRY, '/extramember/nameprofile'), 
  (0, M.default) (H, et.ADD_ON_WELCOME_BACK, '/simpleSetup/welcomeback'), 
  (0, M.default) (H, et.ADD_ON_PROFILE_CREATION, '/simpleSetup/createprofile'), 
  (0, M.default) (H, et.ENTER_PASSWORD_RESET, '/loginhelp'), H)), 
  (0, M.default) (j, $, (L = {
  }, (0, M.default) (L, et.DEMO_ADS_OPT_OUT, '/settings/demographics/demographicAdsOptOut'),
  (0, M.default) (L, et.BEHAVIORAL_ADS_OPT_OUT, '/settings/demographics/behavioralAdsOptOut'),
  (0, M.default) (L, et.EDIT_GENDER, '/settings/demographics/editGender'), L)), (0, M.default) (j, ee, (_ = {
  }, (0, M.default) (_, et.NOTIFICATION_SETTINGS, '/notificationsettings'), (0, M.default) (_, et.NOTIFICATION_SETTINGS_EMAIL, '/notificationsettings/email'), (0, M.default) (_, et.NOTIFICATION_SETTINGS_TEXT, '/notificationsettings/text'), (0, M.default) (_, et.NOTIFICATION_SETTINGS_PUSH, '/notificationsettings/push'), _)), j);
  t.MONEYBALL_PATHS = er

After checking out all of the endpoints, I found one to have weird behaviour. Upon visting /create-credentials, I was presented with the following page:

Press enter or click to view image in full size

If you enter new email and password, your current email and password would be changed and you would be redirected to /youraccount page.

That endpoint didn’t require any MFA. It means MFA was bypassed.

At this step, I though that this endpoint was accessible only for “Extra Member” users, but eventually it turned out to be working for all Netflix users.

Conclusion

As I demonstrated, I managed to find a way to bypass the MFA by using a different endpoint which was discovered in the process of exploring a feature that was available only for certain countries.

I believe it’s always a good idea to focus on paid features and spend some money on them as they are less tested. It will pay off for sure.

The total investments I have made in the Netflix Bug Bounty program since I started participating are:

Press enter or click to view image in full size
Netflix Bug Bounty Investment
