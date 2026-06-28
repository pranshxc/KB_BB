---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-02-06_auth-bypass-in-google-assistant.md
original_filename: 2022-02-06_auth-bypass-in-google-assistant.md
title: Auth Bypass in Google Assistant
category: documents
detected_topics:
- mobile-security
- access-control
- command-injection
- automation-abuse
- information-disclosure
- api-security
tags:
- imported
- documents
- mobile-security
- access-control
- command-injection
- automation-abuse
- information-disclosure
- api-security
language: en
raw_sha256: 00b2e30de906c26fd44204d83b37afb58edc63b64d1fb6e7fde1b3f1bdad7c7c
text_sha256: f5eb5a8a2ab0bf44a3e72387f34ff672bba946f03ae31708ee1627a2b4ca707f
ingested_at: '2026-06-28T07:32:09Z'
sensitivity: unknown
redactions_applied: false
---

# Auth Bypass in Google Assistant

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-02-06_auth-bypass-in-google-assistant.md
- Source Type: markdown
- Detected Topics: mobile-security, access-control, command-injection, automation-abuse, information-disclosure, api-security
- Ingested At: 2026-06-28T07:32:09Z
- Redactions Applied: False
- Raw SHA256: `00b2e30de906c26fd44204d83b37afb58edc63b64d1fb6e7fde1b3f1bdad7c7c`
- Text SHA256: `f5eb5a8a2ab0bf44a3e72387f34ff672bba946f03ae31708ee1627a2b4ca707f`


## Content

---
title: "Auth Bypass in Google Assistant"
page_title: "[#0012] Specific Google Assistant queries allow leaking Location History from a locked phone | feed"
url: "https://feed.bugs.xdavidhu.me/bugs/0012"
final_url: "https://feed.bugs.xdavidhu.me/bugs/0012"
authors: ["David Schütz (@xdavidhu)"]
programs: ["Google"]
bugs: ["Information disclosure", "Authentication bypass"]
bounty: "2674"
publication_date: "2022-02-06"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 2933
---

#0012  
Vendor: Google  
Status: fixed  
Reported: Sep 01, 2020  
Disclosed: Feb 06, 2022 (523 days) 

# Specific Google Assistant queries allow leaking Location History from a locked phone

Summary: Location history can be extracted from locked phone via Assistant queries

**Short summary:**

Sensitive location history information can be extracted from a locked Android phone / Google Home (with personal results disabled) via specific Assistant queries.

**Steps to reproduce:**

  1. Set up an Android phone with Assistant with an account that has places saved in location history
  2. Lock the device
  3. Trigger the Assistant on the lock screen
  4. Ask “What [PLACE_TYPE] have I visited?” (PLACE_TYPE can be for example: “places”, “restaurants”, “shops”)
  5. Assistant will respond with: “Here are the most recent ones:” and will list the places the vicim visited without unlocking the screen. It will also show e.g. “You visited yesterday.” or “You visited 3 weeks ago.” for places the victim visited recently.

This info can leak from multiple places. Another example:

  1. Make sure the victim account have visited a nearby Burger King
  2. Trigger the Assistant on the lock screen and say “Burger King”
  3. If multiple results are available, it will show a list, and will include sensitive info such as “You visited yesterday.” If there is only one result, or you select one by saying “the first one”, the “Place Card” result will also expose “You visited yesterday.” style sensitive information.

These steps (more or less similarly) work the same way on a Google Home device which has Personal Results disabled. My non personal results Google Home Mini listed 3 recent places from my account’s Location History when asked “What places have I visited?”

I suspect this is a server-side issue and these location history add-ons in Assistant do not set some kind of “personal” flag, so both the locked Assistant on a phone, and the non personal results Google Home respond to it without requesting unlock/permission.

Attack scenario: The location history of a user is extremely sensitive data. It or parts of it should never be accessible from a locked phone. If a user leaves his/her phone unattended a malicious attacker could issue a lot of queries and map out the location history of the user. Also, the same applies to Google Home with Personal Results disabled. **Location History in any form is a personal result.**

* * *

### Comments:

**Vendor**

_automated response acknowledging my report_

* * *

**Vendor**

Hey,

Thanks for your efforts for keeping our users secure! We’ve investigated your submission and made the decision not to track it as a security bug, as we’re already aware of this.

Users on Android phones are able to configure unlocking their phone when speaking “OK Google”. This feature may be called Voice Match or Trusted Voice, depending on you Android version. Sometimes this setting gets enabled, when setting up the Google Assistant application.

Please kindly check in your phone settings if this unlocking feature is enabled. This might me under different settings depending on your Android version, phone manufacturer or your locale settings - check your settings for “Smart Lock”, “Voice match” or “Trusted Voice”.

For example, In Google Pixel in Android Oreo, this should be visible under “Settings > Security and Location > Trust Agents”. In Samsung phones, this might under in “Settings > Lock Screen and Security > Smart Lock > Trusted Voice > Unlock with Voice Match”. See also https://support.google.com/pixelphone/answer/6093922 and https://support.google.com/assistant/answer/7394306.

To avoid having your phone unlock when speaking “OK Google”, or a closely matching phrase, please turn that feature off. We are aware that the voice recognition is not perfect, and that there might be various bypass methods by e.g. recording the phrase and then replaying it, or triggering certain actions in Google Assistant. You can stop all those vectors by disabling Voice Match/Trusted Voice in your settings.

If we misunderstood your report, please let us know.

== The fine print == Your report is now _closed_ , but you can still respond, and we’ll take a look at your response.

If you just reported this in order to help us make Google safer, thank you very much for your help! And please file a new bug if you find a different issue in the future.

If your report was about participating in the Google VRP,: Because we did not file a bug internally because of your report, it will not give you credit in the Google Bug Hunter Hall of Fame, and it is also not in scope for a reward for the VRP. We’ve built some learning resources for bug hunters that want to participate in the Google VRP. Check them out at http://g.co/bughunteruniversity

Thanks again for your help, and hope to hear back from you in the future.

* * *

**Me**

Hi,

I strongly suspect that you misunderstood this report and it is indeed a technical issue.

The device used to reproduce this issue has “Voice Match” / other voice unlock options disabled. Also, the device has “Lock screen personal results” disabled. Furthermore, the above mentioned Google Home Mini also has “Personal Results” disabled.

Any other personal query results in Assistant requesting me to unlock the device.

The specific Location History queries mentioned above do not get blocked by an unlock request, and proceed on a locked phone, therefore leaking sensitive the victim’s location data.

Thanks, David

* * *

**Vendor**

That is not the behaviour I experienced; therefore, I’d like to request a video PoC evidencing settings that the security settings appear to function in a manner contrary to actual function. I recommend annotating your video subtitles or including a summary of important timestamps to ease following your narrative.

[redacted]  
Google Trust & Safety

* * *

**Me**

Hi,

I made a POC video to showcase the issue. It shows the issue on both the locked Android and the Google Home Mini.

Video: `https://youtu.be/5ouB01TLE_g` (length: 1:27)

Thanks, David

* * *

**Vendor**

I see the process you followed. My teammate’s comment I uphold: “technical” I construe as “requiring technical expertise within security, and often knowledge within auditing or privacy to lead to the discovery of the process.” This may be deep expertise of network packets, WAP, so forth.

Furthermore, was this really something that is exclusive to Voice Match?

[redacted]  
Google Trust & Safety

* * *

**Me**

Hi,

I feel like you misunderstood my previous comment. By “technical” in comment #4, I was referring to the issue not being a misconfiguration on my device, but an actual issue in Assistant.

To address the second question, as far as I know there is no available public documentation showing what Assistant queries are considered “Personal”.

Therefore I can only assume, that if “What is my name?” is considered a “Personal” result requiring screen-unlock, accessing the underlying Google account’s location history would also be considered “Personal”, since location history data is arguably way more privacy sensitive information than a name.

Again, as I stated in my initial report, my personal opinion is that: **Location History in any form is a personal result.**

Thank you, David

* * *

**Vendor**

Hi,

🎉 **Nice catch!** I’ve filed a bug based on your report.

The panel will evaluate it at the next VRP panel meeting and we’ll update you once we’ve got more information. All you need to do now is wait. If you don’t hear back from us in 2-3 weeks or have additional information about the vulnerability, let us know!

Regards,  
[redacted], Google Trust & Safety Team

* * *

**Vendor**

_automated response of a $1337.00 reward_

* * *

**Vendor**

Hi David,

Per our email discussion, sending you a note just as an FYI: We classified this report as an abuse risk.

Best of luck in your future research, [redacted]

* * *

**Me**

Hi,

I have noticed that a fix has been pushed for this bug, and it indeed seems to fix the issue in `com.google.android.googlequicksearchbox`.

But it looks like that Google Home devices are still vulnerable. Today I asked my Nest Audio (with personal results disabled) `what restaurants have I visited?`, and it answered me, just like in the POC video.

This might be from the fact that some actions behave differently on phone, and on the Google Home, for example saying `turn on the lights` requires an unlock on the phone, but works without personal results on the Google Home.

I still think that location history **should never be leaked without enabling personal results** , not even on a Google Home device which is considered to be in a somewhat trusted physical environment.

Thanks,  
David

* * *

**Vendor**

Hi David,

Thanks for flagging this! We’ve notified the team and we will get back to you once we hear from them.

Happy New Year!

[redacted]

* * *

**Vendor**

Hey David,

Just one quick follow-up question, do you have voice recognition on your nest device? If yes, have you tried this with someone else voice as well?

Thanks in advance, [redacted]

* * *

**Vendor**

Hi David,

If you could also share the gmail address you used in the attack it would help the team to debug this issue.

Thanks in advance, [redacted]

* * *

**Me**

Hi,

I used this email address, `dadkalevelei@gmail.com`.  
I do not have any kind of voice recognition/voice match set up. Also of course `Personal Results` are disabled.

Thanks,  
David

* * *

**Vendor**

Great - thanks for a fast response David!

* * *

**Vendor**

_automated response of a $1337.00 reward_

* * *

**Me**

Oh, thank you for that, that was unexpected! :)  
I assume it is for bypassing the fix.

Thank you,  
David

* * *

**Me**

By the way, if it’s possible to ask, since it was my personal device/account’s email that I gave to the team, it made me think about how it could have helped in the debugging process.

Is it only used to get basic info about my devices, or can developers just get full access to query history based on an email address? I hope thats not possible.

Thank you,  
David

* * *

**Vendor**

Hi David,

In short: When you use our services, you’re trusting us with your information. We understand this is a big responsibility and work hard to protect your information and put you in control.

For more details about why and how we collect user data and the privacy controls that users can use you can read [this article](https://policies.google.com/privacy?hl=en-US#whycollect) which provides a detailed overview.

Best,

[redacted]

* * *

**Me**

Hi,

After routinely asking my Nest “what restaurants have I visited?” every other day, on Friday I noticed that it now gives me the standard “For help with that, first you’ll need to allow personal…”. So it looks like this issue is fixed now on both the mobile app and in the Home devices. Actually, now I can’t even trigger Assistant on the lock screen. Not sure why that is.

Can you please confirm that these fixes has been fully rolled out? Or that they will be until `2021-02-01`?

**[Disclosure Warning]**

Since all of the issues seem to be mitigated, I wanted to give a heads-up that I will be disclosing this bug publicly on my website https://bugs.xdavidhu.me/, **7 days from now** , on `2021-02-01`.

If you would like to delay/cancel the disclosure, please reply to this comment **before`2021-01-11`**.

Thank you,  
David

* * *

**Me**

Whoops, that was a typo. I meant “please reply to this comment **before`2021-02-01`**.”

I’m not that good with templates yet ;)

* * *

**Vendor**

Thanks for the heads-up David!

Let me reach to the product team for the confirmation and get back to you!

Best, [redacted]

* * *

**Vendor**

Hi David,

The issue is fixed and rolled out already. If you would like to share with us the draft of the blog in advance, that would be great! We can always share it with the teams for a review.

Best, [redacted]

* * *

**Me & Vendor**

_chatting about the disclosure timeline_

* * *

**Me**

Hi,

So I have been thinking about adding a section to the blog post about how to configure your phone and disable all personal results on the lock screen, but I realised even I don’t fully understand how this works, so I spent like an hour trying to figure it out, and now I think I get it. But, the settings are very confusing and misleading, and I don’t think an average user would understand them, even though this is a very important privacy setting.

So I could write my findings down about how to securely configure the Assistant in my blog, but it’s so weird that it might even be a bug on its own.

Here are my concerns:

  * The “personal results” settings are now moved to a different location (`Google App` -> `More` -> `Settings` -> `Google Assistant` -> `Personalization`), where it should give you a central control page over all of the “personal results” settings. This would be great, but it does not contain all “personal results” settings, therefore it might confuse users and give a false sense of security.
  * If on this page you disable everything lock screen related (`Lock screen personal results`, `Personal suggestions on lock screen before you ask`, `On headphones`) you would think that now, there is no way to get personal results on the lock screen. **This is not true.**
  * **“Normal” bluetooth headphones can still issue personal queries.** To turn that off, you would have to go to `Google App` -> `More` -> `Settings` -> `Voice` and disable `Allow Bluetooth requests with device locked`. **This is enabled by default!**
  * So, on the `Personalization` page, turning off `On headphones` **only affects wired headphones** , and some special Bluetooth headphones, like the Pixel Buds. **Other normal BT headphones/speakers are unaffected** by this, they are controlled by the `Allow Bluetooth requests with device locked`, which is on a completely different page. **This`On headphones` setting should control every type of headphone/BT device.**
  * After looking at two different devices, and resetting the Google app on one, I can confirm that `Allow Bluetooth requests with device locked` is **enabled by default**. Why is that? It doesn’t feel right. For every other type of headphone (wired, Pixel Buds), you have to specially opt-in to allow personal results.
  * Also, confusingly, on the `Voice` page, you still have the `Allow wired headset requests with device locked`, which is now basically useless and doesn’t do anything, and sometimes toggling it redirects you to the `Personalization` page, but sometimes it does not, allowing you to toggle the switch, which just adds to the confusion.

So, all in all, “lock screen personal results” is in my opinion very sensitive setting, which should be presented very clearly to the users, and currently I doubt that an average user could make sense of all of this mess, and configure their device securely.

Currently, since its **enabled by default** , if you have physical access to someone’s phone & an already paired BT headphone (which are usually stored together), **you can just ask personal queries** without knowing the unlock credentials on most of the Android devices out there. And I don’t think that is okay.

Thank you,  
David

* * *

**Vendor**

Hi David,

Thanks for investigating this and sharing your concerns.

Since this issue is slightly different from your original report, could you please file a separate bug about this? Would be great if you could share with me the report id here, so that I can find it quickly and reach out to the Assistant team fast.

Thanks, [redacted]

* * *

**Me**

Hi,

I made a new report with the ID [b/178587104](/bugs/0013).

Thank you,  
David

* * *

**Vendor**

Great - thanks a lot David!

I’ve filed a separate bug to track that.

Best, [redacted]

* * *

**Me & Vendor**

_chatting about me not being ready with the blog post & my surprise of the reward on the the other bug_

* * *

**Me**

Hi,

Sorry to bring this back up but I am still a bit worried about the privacy implications of comment #20. \

  * Is it possible for the product team to just search for someone’s email address and list all past queries & recordings (or other personal data) without previous consent?
  * Is that (hopefully) limited to some high privilege individuals? If so, was my current case elevated to such level?
  * Are these debug data accesses have to be approved by multiple individuals?
  * What would have happened if I had maliciously sent in someone else’s email address? Would the team look at the past queries of the individual, without consent?
  * Does disabling `Web & App Activity` on the given Google account prevents developers from accessing this data in a similar situation?

I hope asking about this doesn’t come off as offensive, I am just legitimately worried about stuff that I can’t see inside :D. And I hope there is proper protection against a malicious insider, or against a malicious reporter. But I also understand that this could be NDA territory which you can’t really share information about.

Thank you,  
David

* * *

**Vendor**

Hi David,

Thanks for reaching out and sharing your concerns - no offense taken I know your intensions are good ;).

I am sure you have already checked [Google external documentation](https://myaccount.google.com/yourdata/assistant) explaining how you can manage your data in Google Assistant. It describes how you can manage the information stored about your activity but I don’t think it fully addresses all your concerns. So here is more context:

Google Privacy team works with all products like Assistant to set up rules for data access. These rules are described in [Google Privacy Policy](https://policies.google.com/privacy?hl=en-US) and it has most of the answers to your questions (it also covers logs data and its format/storage).

[The same rules](https://policies.google.com/privacy?hl=en-US) apply to the debugging process, which is only possible during a very short period of time and only under very strict access controls. In cases when debugging requires accessing the data from individual users, there are some rules they have to follow before the tools let them read any data. The basic rules are in the privacy policy but depending on the sensitivity of the data, some teams have even stricter rules, like the ones you mentioned (requested/approved by users, law enforcement, etc).

Finally, for the past queries and recordings - these are described in [data retention policy](https://policies.google.com/technologies/retention?hl=en-US) but [Google My Activity](https://myactivity.google.com/myactivity) is the tool that allows to remove that data before the described periods of time.

Hope it helps,

[redacted]

* * *

**Me**

Hey,

Just a heads-up: From my testing it looks like all of the issues are fixed. I will be disclosing this report with all additional comments (with names redacted), this week.

Thank you,  
David
