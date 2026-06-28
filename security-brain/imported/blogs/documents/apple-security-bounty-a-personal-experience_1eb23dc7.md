---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-07-13_apple-security-bounty-a-personal-experience.md
original_filename: 2021-07-13_apple-security-bounty-a-personal-experience.md
title: 'Apple Security Bounty: A personal experience'
category: documents
detected_topics:
- command-injection
- path-traversal
- automation-abuse
- mobile-security
tags:
- imported
- documents
- command-injection
- path-traversal
- automation-abuse
- mobile-security
language: en
raw_sha256: 1eb23dc7f8db9ccf3081396b24254d37f3692366d5f4b149e6e7ae0373dbb181
text_sha256: 398b5e274628ff198f55e856fb17a56090bab7d71965222f1278c1c7e6a62122
ingested_at: '2026-06-28T07:32:06Z'
sensitivity: unknown
redactions_applied: false
---

# Apple Security Bounty: A personal experience

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-07-13_apple-security-bounty-a-personal-experience.md
- Source Type: markdown
- Detected Topics: command-injection, path-traversal, automation-abuse, mobile-security
- Ingested At: 2026-06-28T07:32:06Z
- Redactions Applied: False
- Raw SHA256: `1eb23dc7f8db9ccf3081396b24254d37f3692366d5f4b149e6e7ae0373dbb181`
- Text SHA256: `398b5e274628ff198f55e856fb17a56090bab7d71965222f1278c1c7e6a62122`


## Content

---
title: "Apple Security Bounty: A personal experience"
url: "https://medium.com/macoclock/apple-security-bounty-a-personal-experience-fe9a57a81943"
authors: ["Nicolas Brunner"]
programs: ["Apple"]
bugs: ["Permission bypass", "iOS"]
publication_date: "2021-07-13"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3512
scraped_via: "browseros"
---

# Apple Security Bounty: A personal experience

Apple Security Bounty: A personal experience
Nicolas Brunner
Follow
5 min read
·
Jul 13, 2021

968

12

This is my personal story with the Apple Security Bounty program and why I believe it is a lie after reporting an issue, testing fixes and being left in the dark after 14 months.

Apple introduced the program a few years ago to motivate researchers and developers to share possible critical issues with them. Surprisingly, you wont be able to find a lot of experience reports from contributors to the program. This article is here to change this and I’d like to share my personal experience with the program.

In march 2020 I found a way to access a User’s location permanently and without consent on any iOS 13 (or older) device. This seemed like a critical issue to me — especially with Apple’s focus on privacy in the last years.

Demo App showing unauthorized background access to location data on iOS 13.

The report got accepted and the issue was fixed in iOS 14 and I got credited on the iOS 14 security content release notes. However, as of today, Apple refuses any bounty payment, although the report at hand very clearly qualifies according to their own guidelines. Also, Apple refuses to elaborate on why the report would not qualify. So read this article with a pinch of salt, since as a long-time iOS developer I’m very disappointed with Apple’s communication.

The reported security issue

iOS protects user data and the current location of a user by default. Apps cannot access it without user consent. Apps can typically require access to a user’s location by showing a prompt to the user.

Press enter or click to view image in full size
TCC prompt of an app to request access to location data (iOS 13).

User’s can choose to grant access once, when the app is in the foreground or also if the app is in the background (permanently). Typically users only grant access, while the app is in the foreground.

While working on a project using location and monitoring for beacons at the same time, I was suddenly able to permanently access the device’s location, even though I did never grant that permission.

Get Nicolas Brunner’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

So I decided to write a little demo app and to submit a report to the security bounty program.

Press enter or click to view image in full size

I’d not like to share any source code or instructions how this unauthorized access works, since this is still an open security issue for all iOS users who cannot update their devices to iOS 14. Just imagine what any app could potentially do with this: Collecting users location over years and storing it in their databases to create motion profiles.

Communication with Apple

Within a week’s time I received a response from “Brittany”:

Press enter or click to view image in full size

6 months later, “Deven” informed me, that they have fixed the issue in an upcoming security update. He also asked for my assessment, which I did and obviously, the iOS 14 beta version resolved the issue.

Press enter or click to view image in full size

Then he informed me, that Apple would like to credit me on the security advisories of iOS 14. So far, so good!

Press enter or click to view image in full size

Then I obviously also started to ask for the security bounty reward on multiple occasions over the next 8 months:

Press enter or click to view image in full size
Press enter or click to view image in full size
Press enter or click to view image in full size

Until finally, more than a year after my initial report I received the following e-mail, leaving me completely dazzled:

Press enter or click to view image in full size

I reached back to Apple in the person of “Brent” to ask, in what ways my report would not demonstrate the categories listed on the payouts page. In my humble opinion the report felt very clearly into the following category:

“App access to sensitive data normally protected by a TCC prompt”

Later on, Apple even elaborates on “Sensitive data”:

“Real-time or historical precise location data that would normally be prevented by the system”

Since that last e-mail you see above, I never received any further answers (and believe me, I tried many times).

Conclusion

In my understanding, the idea behind the bounty program is that developers report bugs directly to Apple and remain silent about them until fixed in exchange for a security bounty pay. They also state very clearly, what issues do qualify for the bounty program payout on their homepage. Unfortunately, in my case, Apple never fulfilled their part of the deal (until now).

To be frank: Right now, I feel robbed. However I still hope, that the security bounty program turns out to be a win-win situation for both parties. In my current understanding however, I do not see any reason, why developers like myself should continue to contribute to it. In my case, Apple was very slow with responses (the entire process took 14 months), then turned me away without elaborating on the reasons and stopped answering e-mails.

This left me wondering, why any developer should take the hassle to create a demo app, write source code and a report, maintain communication over many emails and test fixes in beta versions. For my part, I certainly won’t do it again.

Obviously your experience may differ, so I’d be glad to hear about your own experience with Apple’s Security Bounty program.

Further reading:
Hacking Apple by Sam Curry (who received a payout for some of his issues)
