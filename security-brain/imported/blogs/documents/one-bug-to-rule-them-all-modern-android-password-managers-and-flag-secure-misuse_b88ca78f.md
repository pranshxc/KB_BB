---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2019-08-22_one-bug-to-rule-them-all-modern-android-password-managers-and-flag_secure-misuse.md
original_filename: 2019-08-22_one-bug-to-rule-them-all-modern-android-password-managers-and-flag_secure-misuse.md
title: 'One Bug To Rule Them All: Modern Android Password Managers and FLAG_SECURE
  Misuse'
category: documents
detected_topics:
- mobile-security
- sso
- ssrf
- xss
- command-injection
- automation-abuse
tags:
- imported
- documents
- mobile-security
- sso
- ssrf
- xss
- command-injection
- automation-abuse
language: en
raw_sha256: b88ca78f1131c332e82c9b87e4b0f4b9d522727deca451b8e3921327bcdae8d7
text_sha256: 1e083069c4063d743b85e51f6b1b977afafdeb1dba8d70f7689dbdc8460f41fc
ingested_at: '2026-06-28T07:32:00Z'
sensitivity: unknown
redactions_applied: false
---

# One Bug To Rule Them All: Modern Android Password Managers and FLAG_SECURE Misuse

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2019-08-22_one-bug-to-rule-them-all-modern-android-password-managers-and-flag_secure-misuse.md
- Source Type: markdown
- Detected Topics: mobile-security, sso, ssrf, xss, command-injection, automation-abuse
- Ingested At: 2026-06-28T07:32:00Z
- Redactions Applied: False
- Raw SHA256: `b88ca78f1131c332e82c9b87e4b0f4b9d522727deca451b8e3921327bcdae8d7`
- Text SHA256: `1e083069c4063d743b85e51f6b1b977afafdeb1dba8d70f7689dbdc8460f41fc`


## Content

---
title: "One Bug To Rule Them All: Modern Android Password Managers and FLAG_SECURE Misuse"
page_title: "One Bug To Rule Them All: Modern Android Password Managers and FLAG_SECURE Misuse · Doyensec's Blog"
url: "https://blog.doyensec.com/2019/08/22/modern-password-managers-flag-secure.html"
final_url: "https://blog.doyensec.com/2019/08/22/modern-password-managers-flag-secure.html"
authors: ["Lorenzo Stella (@lorenzostella)"]
programs: ["1Password", "Keeper", "Dashlane"]
bugs: ["Information disclosure", "Content leak"]
publication_date: "2019-08-22"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5067
---

[![](/public/images/doyensec-logo.svg)](/index.html)

[![](/public/images/logo.svg)](/index.html)

#### ABOUT US

We are [**security engineers**](https://doyensec.com) who break bits and tell stories.  
  
Visit us  
[doyensec.com](https://doyensec.com)  
  
Follow us  
[@doyensec](https://twitter.com/doyensec)  
  
Engage us  
[info@doyensec.com](mailto:info@doyensec.com)  
  

#### Blog Archive

  * 2026

  * 2025

  * 2024

  * 2023

  * 2022

  * 2021

  * 2020

  * 2019

  * 2018

  * 2017

© 2026 [Doyensec LLC](https://doyensec.com) [![](/public/images/rss.png)](/atom.xml "RSS")

# One Bug To Rule Them All: Modern Android Password Managers and FLAG_SECURE Misuse

22 Aug 2019 - Posted by Lorenzo Stella

A few months ago I stumbled upon a 2016 [blog post](https://commonsware.com/blog/2016/06/06/psa-flag-secure-window-leaks.html) by Mark Murphy, warning about the state of `FLAG_SECURE` window leaks in Android. This class of vulnerabilities has been around for a while, hence I wasn’t confident that I could still leverage the same weakness in modern Android applications. As it often turns out, I was being too optimistic. After a brief survey, I discovered that the issue still persists today in many password manager applications (and others).

## The problem

The [`FLAG_SECURE`](https://developer.android.com/reference/android/view/WindowManager.LayoutParams.html#FLAG_SECURE) setting was initially introduced as an additional setting to `WindowManager.LayoutParams` to prevent DRM-protected content from appearing in screenshots, video screencaps or from being viewed on “[non-secure displays](https://developer.android.com/reference/android/view/Display.html#FLAG_SECURE)”.

This last term was created to distinguish between [virtual screens](https://developer.android.com/reference/android/media/projection/MediaProjection#createVirtualDisplay\(java.lang.String,%2520int,%2520int,%2520int,%2520int,%2520android.view.Surface,%2520android.hardware.display.VirtualDisplay.Callback,%2520android.os.Handler\)) created by the [MediaProjection API](https://developer.android.com/reference/android/media/projection/MediaProjection) (a native API to capture screen contents) and physical display devices like TV screens (having a DRM-secure video output). In this way Google forestalled the piracy apps issue by preventing unsigned apps from creating virtual “secure” displays, only allowing casting to physical “secure” devices.  
While `FLAG_SECURE` nowadays serves its original purpose well _(to the delight of e.g. Netflix, Google Play Movies, Youtube Red)_ , **developers during the years mistook this “secure” flag as an easy catch-all security feature** provided by Android to mark the entire app from being excepted from a screen capture or recording.

Unfortunately, **this functionality is not global for the entire app** , but can only be set on specific screens that contain sensitive data. To make matters worse, every Android fragment used in the application will not respect the `FLAG_SECURE` set for the activity and won’t pass down the flag to any other `Window` instances created on behalf of that activity. As a consequence of this, several native UI components like `Spinner`,`Toast`,`Dialog`,`PopupWindow` and many others will still leak their content to third party applications having the right permissions.

## The approach

After a short survey, I decided to investigate a category of apps in which a content leak would have had the biggest impact: mobile password managers. This would also be the category of applications a generic attacker would probably choose to target first, along with banking apps.  
With this in mind, I fired up a screen capture application ([mnml](https://github.com/afollestad/mnml)) and started poking around. After a few days of testing, **every Android password manager examined (4) was found to be vulnerable to some extent**.

The following sections provide a summary of the discovered issues. All vulnerabilities were disclosed to the vendors throughout the second week of May 2019.

### 1Password

In [1Password](https://1password.com/), the Account Settings’ section offers a way to manage 1Password accounts. One of the functionalities is “Large Type”, which allows showing an account’s Secret Key in a large, easy-to-read format. The fragment showing the Secret Key leaks the generated password to third-party applications installed on the victim’s device. The Secret Key is combined with the user’s Master Password to create the full encryption key used to encrypt the accounts data, [protecting them on the server side](https://support.1password.com/secret-key-security/#how-your-secret-key-protects-you).

![1Password Secret Key Leak Vulnerability](../../../public/images/1password-leak.jpg)

This was fixed in 1Password for Android in version [7.1.5](https://app-updates.agilebits.com/product_history/OPA4#v7010505), which was released on May 29, 2019.

### Keeper

When a user taps the password field, [Keeper](https://keepersecurity.com/) shows a “Copied to Clipboard” toast. But if the user shows the cleartext password with the “Eye” icon, the toast will also contain the secret cleartext password. This fragment showing the copied password leaks the password to third-party applications.

![Keeper Password Leak Vulnerability \(without FLAG_SECURE set\)](../../../public/images/keeper-leak-1.jpg) ![Keeper Password Leak Vulnerability \(with FLAG_SECURE set\)](../../../public/images/keeper-leak-2.jpg)

This was fixed in Keeper for Android version 14.3.0, which was released on June 21, 2019. [An official advisory was also issued](https://docs.keeper.io/release-notes/mobile-platforms/android/android-version-14.3.0).

### Dashlane

Dashlane features a random password generation functionality, usable when an account entry is inserted or edited. Unfortunately, the window responsible for choosing the parameter for the “safe” passwords is visible by third parties applications on the victim’s device.

![Dashlane Password Leak Vulnerability](../../../public/images/dashlane-leak-1.jpg)

Note that it is also possible for an attacker to infer the service associated with the leaked password, since the services list and autocomplete fragment is also missing the `FLAG_SECURE` flag, resulting in its leak.

![Dashlane Leak Vulnerability](../../../public/images/dashlane-leak-2.jpg) ![Dashlane Leak Vulnerability](../../../public/images/dashlane-leak-3.jpg)

The issue was fixed in Dashlane for Android in version [6.1929.2](https://support.dashlane.com/hc/en-us/articles/206553939-Release-notes#title2).

## The attack scenario

Several scenarios would result in an app being installed on a user’s phone recording their activity. These include:

  * Malicious casting apps requiring record permission, since users usually don’t know that casting apps can also record their screen;
  * Innocuous-looking apps using [Cloak & Dagger](http://cloak-and-dagger.org/) attacks;
  * Malicious app installed through third-party Android app stores or [bypassing](https://www.blackhat.com/docs/us-17/thursday/us-17-Anderson-Bot-Vs-Bot-Evading-Machine-Learning-Malware-Detection-wp.pdf) [PHA detection filters](https://security.googleblog.com/2018/03/android-security-2017-year-in-review.html) of the Play Store;
  * Malicious app pushed to the smartphone using the Play Store feature in a [Man-in-the-Browser](http://fc16.ifca.ai/preproceedings/24_Konoth.pdf) attack scenario;

If these scenarios seem unlikely to happen in real life, it is worth noting that there have been [several](https://elleenpan.com/files/panoptispy.pdf) [instances](https://www.zdnet.com/article/android-security-password-stealing-trojan-malware-sneaks-in-google-play-store-in-bogus-apps/) of apps abusing this class of attacks in the recent past.

Many thanks to the _1Password_ , _Keeper_ , and _Dashlane_ security teams that handled the report in a professional way, issued a payout, and allowed the disclosure. **Please remember that using a password manager is still the best choice these days to protect your digital accounts and that all the above issues are now fixed.**

As always, this research was possible thanks to my [25% research time](https://doyensec.com/careers.html) at Doyensec!

### Other relevant posts:

  * ###  [ Intercepting OkHttp at Runtime With Frida - A Practical Guide 22 Jan 2026 ](/2026/01/22/frida-instrumentation.html)

  * ###  [ Windows Installer, Exploiting Custom Actions 18 Jul 2024 ](/2024/07/18/custom-actions.html)

  * ###  [ Windows Installer EOP (CVE-2023-21800) 21 Mar 2023 ](/2023/03/21/windows-installer.html)

  * ###  [ SSRF Cross Protocol Redirect Bypass 16 Mar 2023 ](/2023/03/16/ssrf-remediation-bypass.html)

  * ###  [ Let's speak AJP 15 Nov 2022 ](/2022/11/15/learning-ajp.html)

  * ###  [ Diving Into Electron Web API Permissions 27 Sep 2022 ](/2022/09/27/electron-api-default-permissions.html)

  * ###  [ Regexploit: DoS-able Regular Expressions 11 Mar 2021 ](/2021/03/11/regexploit.html)

  * ###  [ Novel Abuses On Wi-Fi Direct Mobile File Transfers 10 Dec 2020 ](/2020/12/10/novel-abuses-wifi-direct-mobile-file-transfers.html)

  * ###  [ Researching Polymorphic Images for XSS on Google Scholar 30 Apr 2020 ](/2020/04/30/polymorphic-images-for-xss.html)

  * ###  [ Jackson gadgets - Anatomy of a vulnerability 22 Jul 2019 ](/2019/07/22/jackson-gadgets.html)
