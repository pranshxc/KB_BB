---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-10-10_how-i-hacked-billion-android-users-social-and-3rd-party-account-a-story-about-50.md
original_filename: 2021-10-10_how-i-hacked-billion-android-users-social-and-3rd-party-account-a-story-about-50.md
title: How I Hacked Billion Android Users Social And 3rd Party Account | A Story About
  5000$ Bug
category: documents
detected_topics:
- mobile-security
- password-reset
- otp
- command-injection
- mfa
tags:
- imported
- documents
- mobile-security
- password-reset
- otp
- command-injection
- mfa
language: en
raw_sha256: f08f3b7acbfc18eb5bd5419c36ab313e4ea739ce000bec0a777a4338f84b896c
text_sha256: da56f5c90c8720a22e71824606ee4ab514f2579b2be8640b658cd70ba02f02bc
ingested_at: '2026-06-28T07:32:08Z'
sensitivity: unknown
redactions_applied: false
---

# How I Hacked Billion Android Users Social And 3rd Party Account | A Story About 5000$ Bug

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-10-10_how-i-hacked-billion-android-users-social-and-3rd-party-account-a-story-about-50.md
- Source Type: markdown
- Detected Topics: mobile-security, password-reset, otp, command-injection, mfa
- Ingested At: 2026-06-28T07:32:08Z
- Redactions Applied: False
- Raw SHA256: `f08f3b7acbfc18eb5bd5419c36ab313e4ea739ce000bec0a777a4338f84b896c`
- Text SHA256: `da56f5c90c8720a22e71824606ee4ab514f2579b2be8640b658cd70ba02f02bc`


## Content

---
title: "How I Hacked Billion Android Users Social And 3rd Party Account | A Story About 5000$ Bug"
page_title: "HOW I HACKED BILLION ANDROID USERS SOCIAL AND 3rd PARTY ACCOUNT | A STORY ABOUT 5000$ BUG | CVE-2021–0334 | by cappriciosecurities | InfoSec Write-ups"
url: "https://medium.com/@cappriciosec/how-i-hacked-billion-android-users-social-and-3rd-party-account-a-story-about-5000-bug-c422ca43bd2"
authors: ["Karthikeyan.V (@karthithehacker)"]
programs: ["Google"]
bugs: ["Android"]
bounty: "5,000"
publication_date: "2021-10-10"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3249
scraped_via: "browseros"
---

# How I Hacked Billion Android Users Social And 3rd Party Account | A Story About 5000$ Bug

HOW I HACKED BILLION ANDROID USERS SOCIAL AND 3rd PARTY ACCOUNT | A STORY ABOUT 5000$ BUG | CVE-2021–0334
cappriciosecurities
Follow
4 min read
·
Oct 9, 2021

117

In this blog, I will explain the process of how I discovered a vulnerability that triggers the mobile application which in turn allows me to take over multiple accounts.

DEEPLINK

Deep links are a type of link that sends users directly to an app instead of a website or a store. They are used to send users straight to specific in-app locations, saving users the time and energy locating a particular page themselves — significantly improving the user experience.

Deep linking does this by specifying a custom URL scheme (iOS Universal Links) or an intent URL (on Android devices) that opens your app if it’s already installed. Deep links can also be set to direct users to specific events or pages, which could tie into campaigns that you may want to run.

Attack

Android has a component called app link to say it exactly it’s called deep link which is specifically developed for triggering any mobile application. As mentioned earlier, even if the app is updated it is possible to hijack it. how a researcher exploits it is … when an attacker develops an app he develops it with a deep link, secondly, that deep-link triggers the evil website. for example, if an update is out today the second update is out the next day and a bunch of users installs and update it. Whatever you give here it’s loaded in the deep link application. You know if you reset the password the link will be sent to the attacker and he can steal the token and he can do whatever he wants, so this is the scenario.

The researcher develops the malware with a deep link hijacking payload to exploit any deep-link integrated android application.

STEPS :

The researcher develops the malware with his own deep link hijacking payload. In this case, he then tests it on his own deep link (Deeplink: https://cappriciosec.com).

2. Whenever the user clicks this link a prompt appears asking to select either. one of the options to choose “ JUST ONCE ”or the other option “ALWAYS”.

3. When a user clicks the option “ ALWAYS” the malware opens and whenever he/she clicks the link it gets triggered automatically. This is the basic mechanism.

4. The researcher modifies the malware, in the first case he programmed in such a way that it triggers only the cappriciosec.com and then he added an additional payload that triggers any app link

5. Now the researcher releases an update in the google play store, Users will get an update and the users will update it

6. After the update, the application malware functionality will change because the researcher updated a new payload in the malware. as we already know the user had allowed access which in turn triggers the malware. Whenever the user clicks the Cappriciosec link.

Now if the user opens any link it will automatically trigger the malware and the pop-up will never ask the option to choose “just once” or “always”.

WHY IT IS VULNERABLE?

Earlier it was mentioned that the user allowed permission to open cappriciosec.com but after the update, any link is allowed to process and no pop-up appears. This all happens without the user’s knowledge so this is the vulnerable part.

IMPACT

Get cappriciosecurities’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Without the update, it was possible to inject a payload. The great impact is , it is easy to bypass the validation such as two-factor authentication, email verification code or token, password reset link or token, account credentials, and so on .. any web-related things can be easily hijacked. But to do this it doesn't need users authentication just by a code it was able to do this, any HTTP related things can be easily hijacked by this type of vulnerability

VULNERABILITY DISCOVERED By :- karthithehacker (
Karthikeyan.V
)

COLLABORATED & REPORT WRITTEN BY :- jeyasri.A (jeyasri__001)

TIMELINE

Reported to android os security team : Date Aug 7, 2020 12:11PM

Created issue : Aug 10, 2020 11:37PM

Assigned date : Aug 11, 2020 10:42AM

Press enter or click to view image in full size

Updated more

Press enter or click to view image in full size
Press enter or click to view image in full size

Fixed date : Feb 2, 2021 1:57AM

Acknowledgements :- https://source.android.com/docs/security/overview/acknowledgements

Rewarded date : Feb 2, 2021 1:57AM

Reward: $5000

Press enter or click to view image in full size
Press enter or click to view image in full size
Note:-

We have requested the android security team to keep this CVE private, so we cannot disclose the payload, malware source code, and the POC videos

-Thank you

WRITER:- AGNES RUSALIYA
