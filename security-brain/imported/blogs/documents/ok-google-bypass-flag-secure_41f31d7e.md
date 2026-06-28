---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-05-01_ok-google-bypass-flag_secure.md
original_filename: 2020-05-01_ok-google-bypass-flag_secure.md
title: Ok Google! bypass ‘flag_secure’
category: documents
detected_topics:
- mobile-security
- access-control
- command-injection
- api-security
tags:
- imported
- documents
- mobile-security
- access-control
- command-injection
- api-security
language: en
raw_sha256: 41f31d7e679e30a60c36c4f704906c0ef079f93d7fbe517f533ff4fe0cedc85d
text_sha256: 8c961620a3c2ec84348cbd73b9a6dd374abfb6b656f296879b08b925b7d13125
ingested_at: '2026-06-28T07:32:01Z'
sensitivity: unknown
redactions_applied: false
---

# Ok Google! bypass ‘flag_secure’

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-05-01_ok-google-bypass-flag_secure.md
- Source Type: markdown
- Detected Topics: mobile-security, access-control, command-injection, api-security
- Ingested At: 2026-06-28T07:32:01Z
- Redactions Applied: False
- Raw SHA256: `41f31d7e679e30a60c36c4f704906c0ef079f93d7fbe517f533ff4fe0cedc85d`
- Text SHA256: `8c961620a3c2ec84348cbd73b9a6dd374abfb6b656f296879b08b925b7d13125`


## Content

---
title: "Ok Google! bypass ‘flag_secure’"
page_title: "Ok Google! bypass ‘flag_secure’ – Pankaj Upadhyay"
url: "https://pankajupadhyay.in/2020/05/01/ok-google-bypass-flag-secure/"
final_url: "https://pankajupadhyay.in/2020/05/01/ok-google-bypass-flag-secure/"
authors: ["Pankaj Upadhyay (@_pupadhyay)"]
programs: ["Google"]
bugs: ["Broken authorization"]
publication_date: "2020-05-01"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4617
---

# Ok Google! bypass ‘flag_secure’

[May 1, 2020May 19, 2020](https://pankajupadhyay.in/2020/05/01/ok-google-bypass-flag-secure/)[Pankaj Upadhyay](https://pankajupadhyay.in/author/pupadhyay/)

> Google Assistant on Android 9 can bypass the screen-capture protection provided by Android’s FLAG_SECURE.

**Vulnerability Details:**

[**FLAG_SECURE**](https://developer.android.com/reference/android/view/WindowManager.LayoutParams.html#FLAG_SECURE) is a window level flag in Android ecosystem that allows mobile apps to safeguard their content from a screenshot capture. Application needs to enable it by specifying the `[WindowManager.LayoutParams#FLAG_SECURE](https://developer.android.com/reference/android/view/WindowManager.LayoutParams#FLAG_SECURE)` for the windows/screens, it doesn’t want to be recorded.  
  
**We observed that Google Assistant on Pixel devices, was able to capture screenshots even when screens were protected with FLAG_SECURE.**

This is also important to know that MediaProjectionAPI in Android, allows an app to capture screenshots programmatically. Any rogue app using this API and with proper permissions would have been able to capture screen of the device when other apps are in-use.  
  
[NightWatch CyberSecurity](https://wwws.nightwatchcybersecurity.com/2016/04/13/research-securing-android-applications-from-screen-capture/) has written a detailed post on FLAG_SECURE and MediaProjectionAPI. Google has some [sample code](https://github.com/android/media-samples/tree/master/ScreenCapture) on Github on how to use this API in capturing device screen in real time.  

**Testing Steps:**  
  
1\. Install the Google Search app (<https://play.google.com/store/apps/details?id=com.google.android.googlequicksearchbox>). Enable assistant.  
2\. Go to the settings for Google Search and enable screenshots under “General”. Also enable “Use Screen Context” option under “Google Assistant”, “Phone”  
3\. Open Chrome in **incognito mode** , press Power + Volume Down. Note that screenshots won’t work.  
4\. Now tap the home button and hold, and say **“take screenshot”** or **“share screenshot”** and google assistant will take screenshot bypassing the ‘flag_secure’ restrictions.  
  
**This was tested on Pixel 2 and Pixel 3 devices running Android 9.**

**Timeline:**  
03/12/2019 – Reported the finding through Google VRP  
03/14/2019 – Google confirms the finding. Also tells us that it is a duplicate of an already tracked bug.  
03/14/2019 – Asked when it will be patched and at what point we can disclose it publicly.  
03/19/2019 – Received below response. Google recommended to check the status of the fix time to time.  
![undefined](https://pankajupadhyay.in/wp-content/uploads/2020/05/screen-shot-2020-05-01-at-1.51.56-am.png)  
04/30/2019 – I reached out to Google to know about the status of the fix and shared a draft write-up. No response from Google.  
06/20/2019 – Asked again. No response.  
08/30/2019 – Asked for a status update. No response.  
04/14/2020 – Noticed that this finding was fixed in Android’s [September 2019 bulletin](https://source.android.com/security/bulletin/2019-09-01) and [CVE-2019-2103](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-2103) was assigned to this issue. I shared a modified write-up with Google and asked if CVE-2019-2103 is for the same vulnerability. I did not receive any response.  
05/01/2020 – Published this blog post.  
  

This was jointly discovered by [Pankaj Upadhyay](https://pankajupadhyay.in/) and [NightWatch CyberSecurity](https://wwws.nightwatchcybersecurity.com/).

### Share this:

  * [ Share on X (Opens in new window) X ](https://pankajupadhyay.in/2020/05/01/ok-google-bypass-flag-secure/?share=twitter)
  * [ Share on Reddit (Opens in new window) Reddit ](https://pankajupadhyay.in/2020/05/01/ok-google-bypass-flag-secure/?share=reddit)
  * [ Share on LinkedIn (Opens in new window) LinkedIn ](https://pankajupadhyay.in/2020/05/01/ok-google-bypass-flag-secure/?share=linkedin)
  * [ Share on Facebook (Opens in new window) Facebook ](https://pankajupadhyay.in/2020/05/01/ok-google-bypass-flag-secure/?share=facebook)
  * 

Like Loading...

### _Related_

[Security](https://pankajupadhyay.in/category/security/) [androidsecurity](https://pankajupadhyay.in/tag/androidsecurity/), [SecurityResearch](https://pankajupadhyay.in/tag/securityresearch/) [Leave a comment](https://pankajupadhyay.in/2020/05/01/ok-google-bypass-flag-secure/#respond)
