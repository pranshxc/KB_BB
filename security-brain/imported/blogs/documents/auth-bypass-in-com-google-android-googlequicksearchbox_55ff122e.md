---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-02-06_auth-bypass-in-comgoogleandroidgooglequicksearchbox.md
original_filename: 2022-02-06_auth-bypass-in-comgoogleandroidgooglequicksearchbox.md
title: Auth Bypass in com.google.android.googlequicksearchbox
category: documents
detected_topics:
- xss
- command-injection
- automation-abuse
- api-security
- mobile-security
tags:
- imported
- documents
- xss
- command-injection
- automation-abuse
- api-security
- mobile-security
language: en
raw_sha256: 55ff122e12a7ef0dcbcbb6d2789be0eff7551a23437c067c9c3d8ce8f1c09ccc
text_sha256: 6ad05e49cf9f96ea338af76610a654c63a2570157d56e558c7be9c7af613788e
ingested_at: '2026-06-28T07:32:09Z'
sensitivity: unknown
redactions_applied: false
---

# Auth Bypass in com.google.android.googlequicksearchbox

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-02-06_auth-bypass-in-comgoogleandroidgooglequicksearchbox.md
- Source Type: markdown
- Detected Topics: xss, command-injection, automation-abuse, api-security, mobile-security
- Ingested At: 2026-06-28T07:32:09Z
- Redactions Applied: False
- Raw SHA256: `55ff122e12a7ef0dcbcbb6d2789be0eff7551a23437c067c9c3d8ce8f1c09ccc`
- Text SHA256: `6ad05e49cf9f96ea338af76610a654c63a2570157d56e558c7be9c7af613788e`


## Content

---
title: "Auth Bypass in com.google.android.googlequicksearchbox"
page_title: "[#0013] Google Assistant allows leaking personal data via Bluetooth headphones | feed"
url: "https://feed.bugs.xdavidhu.me/bugs/0013"
final_url: "https://feed.bugs.xdavidhu.me/bugs/0013"
authors: ["David Schütz (@xdavidhu)"]
programs: ["Google"]
bugs: ["Authentication bypass"]
bounty: "1,337"
publication_date: "2022-02-06"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 2934
---

#0013  
Vendor: Google  
Status: fixed  
Reported: Jan 27, 2021  
Disclosed: Feb 06, 2022 (375 days) 

# Google Assistant allows leaking personal data via Bluetooth headphones

_This report is generated based on a comment of mine in[b/167400928](/bugs/0012)_

**Summary:**

Disabling `On headphones` in the Google app’s `Personalization` settings page still allows normal Bluetooth headphones to make personal queries on the locked screen. Also, the toggle which controls this, `Allow Bluetooth requests with device locked`, is enabled by default on every Android device with a Google app, while personal results on Pixel Buds & wired headphones require opt-in & approval from the user.

**Details:**

  * The “personal results” settings are now moved to a different location (`Google App` -> `More` -> `Settings` -> `Google Assistant` -> `Personalization`), where it should give you a central control page over all of the “personal results” settings. This would be great, but it does not contain all “personal results” settings, therefore it might confuse users and give a false sense of security.
  * If on this page you disable everything lock screen related (`Lock screen personal results`, `Personal suggestions on lock screen before you ask`, `On headphones`) you would think that now, there is no way to get personal results on the lock screen. **This is not true.**
  * **“Normal” bluetooth headphones can still issue personal queries.** To turn that off, you would have to go to `Google App` -> `More` -> `Settings` -> `Voice` and disable `Allow Bluetooth requests with device locked`. **This is enabled by default!**
  * So, on the `Personalization` page, turning off `On headphones` **only affects wired headphones** , and some special Bluetooth headphones, like the Pixel Buds. **Other normal BT headphones/speakers are unaffected** by this, they are controlled by the `Allow Bluetooth requests with device locked`, which is on a completely different page. **This`On headphones` setting should control every type of headphone/BT device.**
  * After looking at two different devices, and resetting the Google app on one, I can confirm that `Allow Bluetooth requests with device locked` is **enabled by default**. Why is that? It doesn’t feel right. For every other type of headphone (wired, Pixel Buds), you have to specially opt-in to allow personal results.
  * Also, confusingly, on the `Voice` page, you still have the `Allow wired headset requests with device locked`, which is now basically useless and doesn’t do anything, and sometimes toggling it redirects you to the `Personalization` page, but sometimes it does not, allowing you to toggle the switch, which just adds to the confusion.

So, all in all, “lock screen personal results” is in my opinion very sensitive setting, which should be presented very clearly to the users, and currently I doubt that an average user could make sense of all of this mess, and configure their device securely.

**Impact**

Currently, since `Allow Bluetooth requests with device locked` is **enabled by default** , if you have physical access to someone’s phone & an already paired BT headphone (which are usually stored together), **you can just ask personal queries** without knowing the unlock credentials on most of the Android devices out there. A user who proactively wants to turn this off, and disables `On headphones` on the `Personalization` settings page is still vulnerable.

* * *

### Comments:

**Vendor**

_automated response acknowledging my report_

* * *

**Vendor**

Thank David,

Thanks again for sharing this - I’ve filed a bug based on your report.

Although that might not qualify for a reward in scope of the program. The panel will still evaluate it at the next VRP panel meeting and we’ll update you once we’ve got more information. All you need to do now is wait. If you don’t hear back from us in 2-3 weeks or have additional information about the vulnerability, let us know!

Regards,  
[redacted], Google Trust & Safety Team

* * *

**Vendor**

_automated response of a $1337.00 reward_

* * *

**Me**

Hi,

Is it possible to ask what the fix will be for this issue?

Putting every personal-result setting in the same place, under `Personalization` should of course be one of the fixes, but I’m not quite sure what the solution is for the default-enabled `Allow Bluetooth requests with device locked`.

Will it be turned off for everyone? So they have to re-enable it? That seems like the best solution from a privacy standpoint.

If you have any updates or if a fix is rolling out, let me know, I will try it!

Thanks,  
David

* * *

**Vendor**

Hi David,

I connected with the product team and they got back to me with the message that I included below. Having said that, they are still working on resolving this issue and you will get a notification once the fix has been released. Let us know if you have any idea about the date for your blog. We are looking forward to it ;)

Also, if the message below is still unclear, if you have any feedback about this message or if you have questions after the fix goes out let us know as well.

Best,  
[redacted]

  * When you asked Google Assistant “what restaurants have I visited,” that request should have been treated as a verified query, which requires that an opt-in setting is enabled to answer your question by providing Personal Results on [phone lock screens](https://support.google.com/assistant/answer/9134021?hl=en) or on [shared devices](https://support.google.com/assistant/answer/7684543). 
  * On Android phones, people can choose to enable “personal” content (e.g. things like results from your Google Calendar, access to your contacts etc) to show on their phone lock screen. This setting is off by default, and lock screen personal results are only available when the Assistant recognizes [your voice](https://support.google.com/assistant/answer/9071681?hl=en).
  * Similarly, on shared devices like speakers and smart displays, you can choose to turn on the Personal Results setting to allow the Assistant to provide this personal content when you ask for it. Again, if you have set up Voice Match, your personal results are available only when the Assistant recognizes your voice, or on smart displays, if you have chosen to have personal results shown to you proactively.
  * Thanks to your report, we’ve identified the source of the issue that led to a temporary misclassification of this query, and have rolled out a fix for mobile devices last October, and a fix was recently rolled out on smart speakers.
  * As people’s interactions with Google Assistant expand, we continually evaluate what queries should be verified to serve a personal result to make sure we are getting it right.
  * Personal results for the Android lock screen are disabled by default – and people can choose their settings and if they want their personal results to surface while their phone is locked. 
  * A subset of personal queries including (but not limited to) payments, photos, your name or home address will always require the user to unlock their phone.
  * On mobile devices, you can control what kinds of info Google Assistant will say or show when your device is locked. If personal results on the lock screen are enabled but you would like to disable them on your [Android](https://support.google.com/assistant/answer/9134021?hl=en) phone, simply: 
  * Invoke Assistant with unlocked screen and say “Open Assistant settings” – or go to [Assistant settings](https://support.google.com/assistant/answer/9193492)
  * Tap on “See all Assistant Settings > “Personalization”
  * Turn off the “Lock screen Personal Results” setting
  * Some Google Assistant devices, like speakers and Smart Displays, can be shared with multiple people. For any shared device, you can [turn personal results on or off](https://support.google.com/assistant/answer/7684543?co=GENIE.Platform%3DAndroid&hl=en#zippy=%2Cspeakers-smart-displays-smart-clocks): 
  * Open the Google Home app
  * At the bottom, tap Home and then select your device
  * At the top right, tap Device settings
  * Tap “Recognition & Personalization”
  * Turn “Allow personal results” on or off
  * By default, Assistant’s settings do not allow personal results access to headphones. 
  * Thanks to your report, we’ve identified that for some models, bluetooth headphones were not properly configured under Assistant’s personal results settings. Instead, they operated under a separate bluetooth setting, which was not the intended behavior. We’re actively working on the fix and it will be available in an upcoming Android Google app release.

* * *

**Me**

Hi,

Thank you for the detailed response!

I noticed that the last statement in my opinion is incorrect, saying `By default, Assistant’s settings do not allow personal results access to headphones`, and I want to make sure this is clear for the team as well:

I can confirm after trying on multiple devices, that after reinstalling the Google app, the `Allow Bluetooth requests with device locked` setting got enabled on all of the tested devices. I just got a Pixel 5 yesterday, and the setting was enabled there also, by default, so I had to turn it off manually.

Again, the impact of having this setting enabled by default:

Currently, since `Allow Bluetooth requests with device locked` is **enabled by default** , if you have physical access to someone’s phone & an already paired BT headphone (which are usually stored together), **you can just ask personal queries** without knowing the unlock credentials on most of the Android devices out there.

And I don’t think this is intended behaviour, that is why I asked in comment #5 about the plans of fixing this issue:

Will it be turned off for everyone by rolling out a fix? So users will have to re-enable it? That seems like the best solution from a privacy standpoint. Or will moving this setting to the it’s proper place, (into `Personalization`) would fix this issue as well?

Thank you, David

* * *

**Vendor**

Hey there!

Understood! We’ll get this back to the team :-)

Once we are ready to share the fix we’ll get back to you.

* * *

**Me**

Hey,

Just a heads-up: From my testing it looks like all of the issues are fixed. I will be disclosing this report with all additional comments (with names redacted), this week.

Thank you,  
David
