---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-02-21_how-i-couldve-bypassed-the-2fa-security-of-instagram-once-again.md
original_filename: 2022-02-21_how-i-couldve-bypassed-the-2fa-security-of-instagram-once-again.md
title: How I could’ve bypassed the 2FA security of Instagram once again?
category: documents
detected_topics:
- mfa
- password-reset
- otp
- command-injection
- business-logic
- api-security
tags:
- imported
- documents
- mfa
- password-reset
- otp
- command-injection
- business-logic
- api-security
language: en
raw_sha256: d2a30553f1c27ff885fd3764d6143793cc7e106af3ed4dde95ba9739e525fd9d
text_sha256: 80e154be4e500719bdfa01479b7d1c8acd9302fac18eb026e2d8c40de9142f28
ingested_at: '2026-06-28T07:32:10Z'
sensitivity: unknown
redactions_applied: false
---

# How I could’ve bypassed the 2FA security of Instagram once again?

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-02-21_how-i-couldve-bypassed-the-2fa-security-of-instagram-once-again.md
- Source Type: markdown
- Detected Topics: mfa, password-reset, otp, command-injection, business-logic, api-security
- Ingested At: 2026-06-28T07:32:10Z
- Redactions Applied: False
- Raw SHA256: `d2a30553f1c27ff885fd3764d6143793cc7e106af3ed4dde95ba9739e525fd9d`
- Text SHA256: `80e154be4e500719bdfa01479b7d1c8acd9302fac18eb026e2d8c40de9142f28`


## Content

---
title: "How I could’ve bypassed the 2FA security of Instagram once again?"
page_title: "How I could’ve easily bypassed the 2FA security of Instagram in 2 minutes? | by Samip Aryal | InfoSec Write-ups"
url: "https://infosecwriteups.com/how-i-couldve-bypassed-the-2fa-security-of-instagram-once-again-43c05cc9b755"
authors: ["Samip Aryal (@samiparyal_)"]
programs: ["Meta / Facebook"]
bugs: ["2FA / MFA bypass", "Logic flaw"]
bounty: "3,150"
publication_date: "2022-02-21"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 2879
scraped_via: "browseros"
---

# How I could’ve bypassed the 2FA security of Instagram once again?

How I could’ve easily bypassed the 2FA security of Instagram in 2 minutes?
Samip Aryal
Follow
5 min read
·
Feb 21, 2022

546

5

…

Press enter or click to view image in full size

This writeup is about how i found a way to bypass the 2FA (Two-Factor Authentication) security of Instagram once again but this time anyone could’ve done it pretty easily with the victim’s email access under some quick minutes. Seeing the pretty neat vulnerable endpoint, facebook security team conveniently acknowledged the vulnerability report as valid.

So
this started when I was really interested in bypassing the 2FA security of Instagram using the Instagram-connected email account as I always felt, that integration was a bit less secured and there may be ways to bypass it. Nov-2020, I found a way to bypass the 2FA in Instagram using the ‘secure your account here’ option that comes with the ‘Email Changed’ notification email from Instagram.

2FA Bypass On Instagram Through A Vulnerable Endpoint
This report is about the missing 2FA check on Instagram login when a user uses the ‘Secure account here’ option from…

infosecwriteups.com

But due to its high complexities for an attack, the Facebook Sec Team closed it as Informative and didn’t fix it apparently. But like I mentioned in that report;

“vulnerability is a vulnerability & that may potentially affect somehow someday or open doors to even more scenarios if unfixed”

I still felt that there may be ways to bypass the 2FA using the email but I wasn’t really testing there then, until when DMs started flooding in my Instagram message request from different people requesting me to Bypass 2FA for their Instagram accounts. Some needed genuine help as they lost their ways to verify 2FA to get back into their Instagram personal/business accounts. But, of course in many cases; I could do nothing from my side but just show them ways to contact Instagram Help for recovering 2FA. But, this dissatisfaction also fueled me to really search for neat ways to bypass 2FA.

Late January this year, with reference to that previous report, I started looking for different endpoints that connect the access of the Instagram account of a user with the email itself. Using several automated emails that came over different periods of time from Instagram regarding password change, email change, password reset, 2FA enabled, 2FA disabled, etc; I started comparing them and the endpoints they carried, then I noticed a unique button in current days reset emails.

“we’ve made it easy to get back on Instagram”
Actually yes, a lot easier due to this ; )

So, these days; when a user requests a login link using the ‘Forgot Password’ option, there comes two buttons, one; the direct login button & another password resetting button. But, if you’ve noticed previously in previous years; it won’t use to be like that. You would’ve gotten only one button as ‘Log in as …’ and also a link below it with a reset token link as ‘You can also reset your Instagram password’ like this:

Reset Email from Instagram: Previously

Hence, since there was a new button for the same resetting functionality; it made me curious to test this button on the mobile because usually when a clickable button is included, a new interface is designed inside the app where the button redirects to when clicked. Exactly as my expectation, after clicking the above ‘Reset your password’ button, I was redirected to the Instagram app to a relatively apparent newer interface I guess, for resetting the password for the Instagram account.

Get Samip Aryal’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

So without hesitation, I initiated the 2FA bypass test using the following repro:

Assuming my phone to be the Attacker’s device and my PC to be the victim’s device,

1. I made a test Instagram account and enabled 2FA security for the account using the Instagram web.

2. Then, considering the Attacker compromising the victim’s email account, the attacker logs into the victim’s email account in the respective email app.

3. After that, the Attacker simply goes to Instagram>>Forget Password and inputs the Victim’s Instagram Account Username and asks for a login link in his/her email.

4. Finally, the Attacker gets the “we’ve made it easy to get back on Instagram” email from Instagram in the victim’s email account, clicks the vulnerable ‘Reset your password’ button; gets redirected to the Instagram app to that password resetting interface, resets the password and

GUESS WHAT?

Congratulations!🥳 you’ve got into an Instagram account without any 2FA validation / 2FA check.

To make it tastier, the attacker can now disable the 2FA from the victim’s account heading towards the Settings>>Security>>Two-factor authentication, completely taking over the “SECURED” Instagram account of the victim.

If you are curious like “What about the web ?” What did happen when that ‘Reset your password’ button was clicked on the Instagram web/PC ?. Well, in the web; it wasn’t vulnerable, The button would’ve and still redirects the user to the same old Instagram Reset page where you can reset the password but it will compulsorily ask for an OTP due to the proper 2FA check to get into the Instagram account successfully.

So, Wrapping up quickly about the vulnerability, I reported this vulnerability to Facebook Security Team ASAP. Tyler from Facebook Security Team quickly triaged the vulnerability within a day and sent it for a fix. After some days, the product developers team fixed it properly and rewarded me with a bounty.

Press enter or click to view image in full size
Reward Message From Facebook

If you would like to check the POC video of this vulnerability that I sent with the report, you can find it here.

…

Thank you for reading this write-up about how a simple vulnerable button and interface would’ve allowed anyone to bypass the 2FA security of Instagram. If you have any queries/suggestions, I’m available on Facebook/ Instagram.

…
