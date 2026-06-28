---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2019-10-26_illegal-rendered-at-download-feature-in-several-apps-including-opera-mini-that-l.md
original_filename: 2019-10-26_illegal-rendered-at-download-feature-in-several-apps-including-opera-mini-that-l.md
title: Illegal Rendered at Download Feature in Several Apps (including Opera Mini)
  that Lead to Extension Manipulation (with RTLO)
category: documents
detected_topics:
- mobile-security
- command-injection
- file-upload
- automation-abuse
tags:
- imported
- documents
- mobile-security
- command-injection
- file-upload
- automation-abuse
language: en
raw_sha256: 2fbbf7adb6d2fafd7e61c68ca6100538579956e896d308b11a72fd9ac329efbd
text_sha256: 0fe35c89b45e1a8a1145dc7ae231eb34603f87def9dd4bceb127aabba6b52263
ingested_at: '2026-06-28T07:32:00Z'
sensitivity: unknown
redactions_applied: false
---

# Illegal Rendered at Download Feature in Several Apps (including Opera Mini) that Lead to Extension Manipulation (with RTLO)

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2019-10-26_illegal-rendered-at-download-feature-in-several-apps-including-opera-mini-that-l.md
- Source Type: markdown
- Detected Topics: mobile-security, command-injection, file-upload, automation-abuse
- Ingested At: 2026-06-28T07:32:00Z
- Redactions Applied: False
- Raw SHA256: `2fbbf7adb6d2fafd7e61c68ca6100538579956e896d308b11a72fd9ac329efbd`
- Text SHA256: `0fe35c89b45e1a8a1145dc7ae231eb34603f87def9dd4bceb127aabba6b52263`


## Content

---
title: "Illegal Rendered at Download Feature in Several Apps (including Opera Mini) that Lead to Extension Manipulation (with RTLO)"
page_title: "CVE-2019–18624 – Illegal Rendered at Download Feature in Several Apps (including Opera Mini) that Lead to Extension Manipulation (with RTLO) – Just Another Simple Write-Up"
url: "http://firstsight.me/2019/10/illegal-rendered-at-download-feature-in-several-apps-including-opera-mini-that-lead-to-extension-manipulation-with-rtlo/"
final_url: "http://firstsight.me/2019/10/illegal-rendered-at-download-feature-in-several-apps-including-opera-mini-that-lead-to-extension-manipulation-with-rtlo/"
authors: ["YoKo Kho (@YokoAcc)"]
programs: ["Opera"]
bugs: ["RTLO"]
publication_date: "2019-10-26"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4971
---

[Bug Report](http://firstsight.me/category/bug-report/) / [Mobile Apps](http://firstsight.me/category/mobile-apps/) / [Write-Up](http://firstsight.me/category/write-up/)

# CVE-2019–18624 – Illegal Rendered at Download Feature in Several Apps (including Opera Mini) that Lead to Extension Manipulation (with RTLO)

October 26, 2019 

[__]()

The story of when you download a file that looks “legitimate”, but changes when you run the file.

**In the name of Allah, the Most Gracious, the Most Merciful.**

* * *

**Update I (Jan 21st, 2020):** Opera has replied the email and acknowledged the reported issue. On that occasion, Opera also apologized for the delay in their response.

![](http://www.firstsight.me/wp-content/uploads/2020/03/Response-from-Opera-1024x513.png)Response from Opera

**Update II (Feb 27th, 2020):** Opera notifies if Opera Mini 47 has been released and is being rolled out to 50%. They also offer a good HoF (I haven’t provided the information needed).

* * *

_So, let say you download the .png file. But when you try to open it, the file will be executed as a malicious .apk file._ _Yes, this happens at least in Opera Mini and few applications that have download feature._  
  
_As a little note, we also added few simple bug hunting tips related this RTLO things at the end of article._

* * *

### **I. TL;DR**

Change the filename to: malicious<RTLO_Char><fake_ext>.<real_ext>  
For example: **malicious%E2%80%AEtxt.apk**  
  
When the browser download feature fails to to parse the character perfectly, the filename will be changed to **maliciouskpa.txt**

* * *

### **II. Introduction**

As we know, most browsers that have been developed will have features that can be used by users to download any file. But sometimes there is a problem that arise when the browser fails to parse the characters used as file names (on download feature) or as URL. 

In this case, we found that there are some browsers that fail to render the RTLO characters perfectly and this issue can be used by Attacker to manipulate a filename automatically.

* * *

#### **2.1. Few Words about RTLO**

Honestly speaking, we cannot explain this very well from a technical point of view or standard in processing characters. However, as we know in general, the characters in this world are divided into two models, namely **left to right** and **right to left** character. The famous **right to left** readings that we know in this world is Arabic Character.

Based on several references, there is a standard method that was built to handle texts written from right to left. Basically, this allows computers to exchange information regardless of the language used.

So, in short, by using this method, the computer will recognize the characters that have been entered.

**References:**  
• <https://krebsonsecurity.com/2011/09/right-to-left-override-aids-email-attacks/https://krebsonsecurity.com/2011/09/right-to-left-override-aids-email-attacks/>  
• <https://blog.malwarebytes.com/cybercrime/2014/01/the-rtlo-method/>

* * *

### **III. Testing Environment**

For example, let’s use Opera as a case study (because some programs ask not to release full disclosure).

And this is the environment that we use to reproduce this issue:

  * **Device** : Asus Max Pro M1 (4/64GB)
  * **Operating System** : Android 9 (May 1st, 2019 Update)
  * **Opera Mini Version for Android** : 44.1.2254.142553 (built Aug 29th, 2019) – The version that we reported (since we got no response more than one month –  _lets assume if it not hit the security bar from their point of view_ – then we think it would be good for releasing the article).  
The latest version (Sept 19th, 2019 – 44.1.2254.143214) is also still vulnerable.
  * **Update III (June 06th, 2020):** This issue hits the security bar and Opera has fixed this problem as the information provided in the first part of this article.

* * *

### **IV. Step to Reproduce**

For example, the attacker wants to “send” this scenario to the victim:

  * Attacker’s **original** file type is: .txt.
  * Attacker’s **filename** is: malicious
  * In this situation, the attacker **wants to manipulate** the extension, so the victim will see the file as an image format (which is a .png extension). From this scenario, the Attacker will give the filename with: **malicious%E2%80%AEgnp.txt**.
  * When this file is downloaded by a vulnerable browser (in this case, Opera Mini), the file will be saved as: **malicioustxt.png** on the victim’s device.
  * Even though this file is saved as a .png format, Android will still run it as .txt (because **the original format is** .txt, not .png).
  * Of course, we can do it to others with bad impacts. Let’s say, the original extension was .apk, so we manipulated this extensions with .txt or other normal extensions.

Please kindly note, the **%E2%80%AE** character is **unicode U+202E** that used as **RTL Override**<https://www.charbase.com/202e-unicode-right-to-left-override>

* * *

### **V. PoC Video**

To complete the explanation, we add a simple PoC video that shows the situation:

  * There are 2 files placed on GDrive, namely .txt file (on the left) and .apk (file) on the right;
  * In this case, we took the direct download link. So when users want to download files, then they will see extensions that have been manipulated with RTLO characters;
  * The **first situation** in the video, the user will download the .txt file but the file will be saved as png. When the **user wants to open** the downloaded file, the file **will be executed as .txt** (original format);
  * The **2nd situation** in the video, the user will download the .apk file but the file will be saved as txt. Again, when **user wants to open** the downloaded file, the **file will be executed as .apk** and trying to install the program (original format).

* * *

### **VI. Screenshot Details**

In the screenshot below, we can see if Opera Mini renders the extension to .png for the original .txt file (the left one) and renders the extension to .txt for the real .apk file (the right one).

![](http://www.firstsight.me/wp-content/uploads/2020/03/Download-as-png-left-one-and-Download-as-txt-right-one-1024x524.png)Download as .png (left one) and Download as .txt (right one)

When we try to open a file with **malicioustxt.png** name (the left one from the image above), Android will recognize it as a .txt file (original format).

![](http://www.firstsight.me/wp-content/uploads/2020/03/Android-recognise-the-File-as-.txt-even-though-the-name-was-.png)Android recognise the File as .txt even though the name was .png

And for the file with **OMkpa.txt** name, the Android will execute it as .apk format. We can see from the behavior of Opera that wants to install a program.

![](http://www.firstsight.me/wp-content/uploads/2020/03/Opera-Mini-Trying-to-Install-the-App.png)Opera Mini trying to install the Software

* * *

### **VII. Reporting Timeline**

Opera Mini Browser for Android:

  * **Sept 10th 2019:** Reach Opera via <https://security.opera.com/report-security-issue/>. It might be a mistake to report through this line because you won’t receive any acknowledgment. We recommend that you report via “Report a problem feature” in the application:

![](http://www.firstsight.me/wp-content/uploads/2020/03/In-App-Report-Problem-Feature.png)In-App “Report a Problem” Feature

Even though you still haven’t received feedback, then at least you know that your email has reached them (because of their automation replies).

  * **Sept 10th, 2019:** Opera saw the PoC video few times.
  * **Sept 23rd, 2019:** Trying to contact them to ask about the situation and still not get any information. (Maybe they are really busy right now or it doesn’t hit the security bar from their point of view).
  * **Note:** Previously we thought if this problem was fixed in the latest release version (September 19, 2019). But when we tried to reproduce the problem again a few days ago, we found it still vulnerable. Don’t know why it works and somehow it doesn’t.
  * **Oct 30th, 2019:** Assigned as CVE-2019–18624.
  * **Update I:** **Jan 21st, 2020** : Opera has replied the email and acknowledged the reported issue. On that occasion, Opera also apologized for the delay in their response.
  * **Update II:** **Feb 27th, 2020** : Opera notifies if Opera Mini 47 has been released and is being rolled out to 50%. They also offer a good HoF (I haven’t provided the information needed).

![](http://www.firstsight.me/wp-content/uploads/2020/03/Response-from-Opera-1024x513.png)Response from Opera

* * *

_As a simple note, we also report this similar problem to one of our favorite bug bounty programs on one of the well-known platforms. And as usual, they respond and fix problems very quickly (with a nice bounty) without needing to ask their status. So far, they always respond in 1 day and improve in 5 days._

  * **July 22nd, 2019:** Reported via one of the well-known platform
  * **July 24th, 2019:** apologize for the late response (because usually they only need 1 day, and this time takes 2 days – Cool, isn’t?).

And they fix the problem very quickly (in the next few days) and give a nice bounty (as usual).

On the other hand, we also report this to other programs and get a response within 9 days with good points.

* * *

### **VIII. The Closing**

At this write-up, I would like to say thanks to [Rafay Baloch](https://twitter.com/rafaybaloch). [From one of his write-up at 2016](https://www.rafaybaloch.com/2017/06/google-chrome-firefox-address-bar.html) (Relates to Address Bar Spoofing at Google Chrome and Firefox for Android by using the combination of IP+RTL), I could know about this RTLO things.

Another credits:

  * RTLO in File Upload Feature at HackerOne: <https://hackerone.com/reports/298>
  * Domain Spoofing with RTLO in Redirect Feature at HackerOne: <https://hackerone.com/reports/299403>

As an additional information, if you would like to try to reproducing the issue, then here are the affected version of Opera Mini for Android:

  * Version 44.1.2254.143214 (Release Sept 19th, 2019): <https://apkpure.com/opera-mini-fast-web-browser/com.opera.mini.native/variant/44.1.2254.143214-APK>
  * Version 44.1.2254.142659 (Release Sept 03rd, 2019): <https://apkpure.com/opera-mini-fast-web-browser/com.opera.mini.native/variant/44.1.2254.142659-APK>
  * Version 44.1.2254.142553 (Release Aug 29th, 2019) <https://apkpure.com/opera-mini-fast-web-browser/com.opera.mini.native/variant/44.1.2254.142553-APK>

* * *

### **IX. Bug Hunting Tips Related to RTLO things**

From this very simple article, then we could conclude if this RTLO things could become a security issue at various feature (even not every program think so, but it’s worth to try). As far as we can think at this time are:

#### **9.1. RTLO in filename via file upload feature**

At this situation, we could test if the upload feature at an application is vulnerable to extension manipulation or not.  
Also, when we talk about “Filename” and “Upload Feature”, it doesn’t limited to only a web app, because it also possible to be “used” to Messaging, Email, and other similar application that has an ability to upload.  
**Reference (HackerOne)** : <https://hackerone.com/reports/298>  
**Reference (Telegram)** : <https://securelist.com/zero-day-vulnerability-in-telegram/83800/>

* * *

#### **9.2. RTLO in filename via cloud drive storage**

Similar with the previous one, just try to upload the file that contain RTLO name to the cloud drive storage, then see what happened.  
**Reference (OX App Suite)** : <https://hackerone.com/reports/210354>

* * *

#### **9.3. RTLO in chat feature**

It also could be test at every application that has a chat feature inside (not just a native chat app). In its implementation, it could used to switching the extension or maybe create a fake URL, for example:  _https://evil.com/RTLO/moc.rettiwt_. If vulnerable, somehow it will switch to  _twitter.com/moc.live//:sptth_. (it happened at Facebook bug report chat).

In other case, it also just switch the things at the back to the front (just like the [address bar spoofing via IP+RTL](https://www.rafaybaloch.com/2017/06/google-chrome-firefox-address-bar.html) at Chrome and Firefox).  
**Reference (Snapchat)** : <https://hackerone.com/reports/196222>

* * *

#### **9.4. RTLO in post feature**

Apart from the chat feature, we also could test this at an application that has a post feature. In the GitLab’s case, the RTLO issue works in the description field. From here, we also can conclude if this RTLO issue could works in every application that has an ability to post something such as “website address” information, post a reply, and other.  
**Reference (GitLab)** : <https://gitlab.com/gitlab-org/gitlab-foss/issues/29365>

* * *

#### **9.5. RTLO in “warning” redirect feature**

This RTLO things also could be use to trying to spoof the domain name with the combination of normal latin (LTR) with RTLO character.  
**Reference (HackerOne)** : <https://hackerone.com/reports/299403>

* * *

#### **9.6. RTLO in browser’s address bar**

From one of Rafay’s write-up, we could see if he successfully spoof the domain name via the combination of IP Address and RTLO character. For example:  _https://evil_IP_Address/RTLO/google.com/login_ become _google.com/login/RTLO/evil_IP_Address._  
**Reference (Google Chrome and Firefox for Android)** : <https://www.rafaybaloch.com/2017/06/google-chrome-firefox-address-bar.html>

* * *

#### **9.7. RTLO in browser’s download feature**

The example about this one has been explained at this simple write-up. Just as a note, **for “browser” things, it doesn’t limited** to only the native browser’s download feature. But also at the **in-App browser** (for example, the one that exist at **messaging app**) and also **few Password Manager Apps** (which is, mostly they also have in-App browser).  
**Reference (Opera Mini for Android)** : this article or <http://firstsight.me/2019/10/illegal-rendered-at-download-feature-in-several-apps-including-opera-mini-that-lead-to-extension-manipulation-with-rtlo/>
