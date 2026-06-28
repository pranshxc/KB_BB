---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-03-06_protecting-android-clipboard-content-from-unintended-exposure.md
original_filename: 2023-03-06_protecting-android-clipboard-content-from-unintended-exposure.md
title: Protecting Android clipboard content from unintended exposure
category: documents
detected_topics:
- mobile-security
- command-injection
- sso
- access-control
- otp
- automation-abuse
tags:
- imported
- documents
- mobile-security
- command-injection
- sso
- access-control
- otp
- automation-abuse
language: en
raw_sha256: 0a04abb169dd263cd6c785a5701b6fa5b4f7c930d85838168008d033fef69ff1
text_sha256: fcfa4bf48beb02fce3aea404032046f6bd7f378bef84c87038c5ffa0ac9c90cf
ingested_at: '2026-06-28T07:32:19Z'
sensitivity: unknown
redactions_applied: false
---

# Protecting Android clipboard content from unintended exposure

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-03-06_protecting-android-clipboard-content-from-unintended-exposure.md
- Source Type: markdown
- Detected Topics: mobile-security, command-injection, sso, access-control, otp, automation-abuse
- Ingested At: 2026-06-28T07:32:19Z
- Redactions Applied: False
- Raw SHA256: `0a04abb169dd263cd6c785a5701b6fa5b4f7c930d85838168008d033fef69ff1`
- Text SHA256: `fcfa4bf48beb02fce3aea404032046f6bd7f378bef84c87038c5ffa0ac9c90cf`


## Content

---
title: "Protecting Android clipboard content from unintended exposure"
page_title: "Protecting Android clipboard content from unintended exposure | Microsoft Security Blog"
url: "https://www.microsoft.com/en-us/security/blog/2023/03/06/protecting-android-clipboard-content-from-unintended-exposure/"
final_url: "https://www.microsoft.com/en-us/security/blog/2023/03/06/protecting-android-clipboard-content-from-unintended-exposure/"
authors: ["Microsoft 365 Defender Research Team"]
programs: ["SHEIN"]
bugs: ["Android"]
publication_date: "2023-03-06"
added_date: "2023-03-06"
source: "pentester.land/writeups.json"
original_index: 1424
---

![](https://www.microsoft.com/en-us/security/blog/wp-content/themes/security-blog-2025/dist/images/single-bg.jpg)

![](https://www.microsoft.com/en-us/security/blog/wp-content/themes/security-blog-2025/dist/images/single-bg-dark.jpg)

  1. [ Home ](https://www.microsoft.com/en-us/security/blog/)
  2. Protecting Android clipboard content from unintended exposure 

Search

![a person standing in front of a building](https://www.microsoft.com/en-us/security/blog/wp-content/uploads/2023/03/Featured-image.jpg)

[ Research ](https://www.microsoft.com/en-us/security/blog/content-type/research/) March 6, 2023  6 min read 

#  Protecting Android clipboard content from unintended exposure 

By [Microsoft Threat Intelligence](https://www.microsoft.com/en-us/security/blog/author/microsoft-security-threat-intelligence/ "Posts by Microsoft Threat Intelligence")

* * *

## Share

  * [ Link copied to clipboard!  ](https://www.microsoft.com/en-us/security/blog/2023/03/06/protecting-android-clipboard-content-from-unintended-exposure/)
  * [ ](https://www.facebook.com/sharer/sharer.php?u=https://www.microsoft.com/en-us/security/blog/2023/03/06/protecting-android-clipboard-content-from-unintended-exposure/)
  * [ ](https://twitter.com/intent/tweet?url=https://www.microsoft.com/en-us/security/blog/2023/03/06/protecting-android-clipboard-content-from-unintended-exposure/&text=Protecting+Android+clipboard+content+from+unintended+exposure)
  * [ ](https://www.linkedin.com/sharing/share-offsite/?url=https://www.microsoft.com/en-us/security/blog/2023/03/06/protecting-android-clipboard-content-from-unintended-exposure/)

## Tags

  * [Android](https://www.microsoft.com/en-us/security/blog/tag/android/)

## Threats intelligence

  * [Vulnerabilities and exploits](https://www.microsoft.com/en-us/security/blog/threat-intelligence/vulnerabilities-and-exploits/)

## Content types

  * [Research](https://www.microsoft.com/en-us/security/blog/content-type/research/)

## Topics

  * [Threat intelligence](https://www.microsoft.com/en-us/security/blog/topic/threat-intelligence/)

Considering mobile users often use the clipboard to copy and paste sensitive information, like passwords or payment information, [clipboard contents can be an attractive target for cyberattacks](http://attack.mitre.org/techniques/T1414/). Leveraging clipboards can enable attackers to collect target information and exfiltrate useful data. Examples even exist of attackers [hijacking and replacing the clipboard contents](http://attack.mitre.org/techniques/T1641/001/) for malicious purposes, such as [modifying a copied cryptocurrency wallet address](https://www.threatfabric.com/blogs/sova-new-trojan-with-fowl-intentions.html) before the user pastes it into a crypto wallet app or chat message. Moreover, these types of attacks misuse a legitimate system feature rather than exploit a vulnerability, making the issue more challenging to mitigate.

Microsoft discovered that an old version of the SHEIN Android application periodically read the contents of the Android device clipboard and, if a particular pattern was present, sent the contents of the clipboard to a remote server. While we are not specifically aware of any malicious intent behind the behavior, we assessed that this behavior was not necessary for users to perform their tasks on the app.

SHEIN’s Android application is published on the Google Play Store with over 100 million downloads. Even if SHEIN’s clipboard behavior involved no malicious intent, this example case highlights the risks that installed applications can pose, including those that are highly popular and obtained from the platform’s official app store. We reported our findings to Google, the Play Store operator, leading to an investigation by their Android Security Team. In May 2022, Google informed us and we confirmed that SHEIN removed the behavior from the application. We would like to thank Google’s Android Security Team as well as the SHEIN team for their efforts and collaboration in addressing this issue. We would also like to thank the Google team for the improvements implemented to the Android platform to protect users from the risks associated with anomalous clipboard access.

In this blog, we detail how we identified the SHEIN app’s clipboard behavior and how Android users can protect themselves against clipboard-based attacks. We also share this research with the larger security community to emphasize the importance of collaboration in the effort to improve security for all.

## Static and dynamic analysis

The following analysis details how we identified and verified the presence of the SHEIN app’s clipboard behavior, analyzing SHEIN app version 7.9.2 (SHA-256: _ff07dc6e237acd19cb33e35c60cb2ae52c460aac76bc27116d8de76abec66c51_). We first performed a static analysis of the app to identify the relevant code responsible for the behavior. We then performed a dynamic analysis by running the app in an instrumented environment to observe the code, including how it read the clipboard and sent its contents to a remote server.

![Call chain diagram displaying how a user starting or resuming the SHEIN app progresses through various calls until it checks the clipboard text for the character sequences $ and "://", which, if found, will be sent as a parameter to a SHEIN server.](https://www.microsoft.com/en-us/security/blog/wp-content/uploads/2023/03/Figure-1.-An-example-of-a-call-chain-through-the-SHEIN-app-resulting-in-clipboard-access-1024x875.png)Figure 1. An example of a call chain through the SHEIN app resulting in clipboard access

### Identifying the code

Upon opening the application, the launcher activity _com.shein.user_service.welcome.WelcomeActivity_ extends the _com.zzkko.base.ui.BaseActivity_ class, which performs a call to the _iBaseActivityCallBack.h_ method in the _onResume_ callback, depicted below on Line 11: 

![graphical user interface, text, application, email](https://www.microsoft.com/en-us/security/blog/wp-content/uploads/2023/03/Figure-2.-The-com.zzkko_.base_.ui_.BaseActivity-class-performing-a-call-to-the-iBaseActivityCallBack.h-method-in-the-onResume-callback-1.png)Figure 2. The _com.zzkko.base.ui.BaseActivity_ class performing a call to the _iBaseActivityCallBack.h_ method in the _onResume_ callback 

The _com.zzkko.app.iBaseActivityCallBack_ is aninterfaceimplemented by the _com.zzkko.app.BaseActivityCallBack._ The method _h_ , partially depicted below, from the previous call performs a call to the method _o_ in the same class, as shown on Line 16: 

![graphical user interface, text, application, email](https://www.microsoft.com/en-us/security/blog/wp-content/uploads/2023/03/Figure-3.-Method-h-performing-a-call-to-the-method-o-in-the-same-class-3.png)Figure 3. Method _h_ performing a call to the method _o_ in the same class

Finally, in the _com.zzkko.app.BaseActivityCallBack.o_ method there is a call to the _com.zzkko.util.MarketClipboardPhaseLinker.f_ method, shown on Line 2: 

![graphical user interface, text, application, email](https://www.microsoft.com/en-us/security/blog/wp-content/uploads/2023/03/Figure-4.-The-com.zzkko_.app_.BaseActivityCallBack.o-method-calls-the-com.zzkko_.util_.MarketClipboardPhaseLinker.f-method-3.png)Figure 4. The _com.zzkko.app.BaseActivityCallBack.o_ method calls the _com.zzkko.util.MarketClipboardPhaseLinker.f_ method

Method _com.zzkko.app.BaseActivityCallBack.f,_ depicted below, checks whether the character sequences “$” and “://” are present in the clipboard text, depicted on Line 6. If both are present, method _k_ in the same class is called with the clipboard text provided as a parameter, as shown on Line 8: 

![graphical user interface, text, application, email](https://www.microsoft.com/en-us/security/blog/wp-content/uploads/2023/03/Figure-5.-The-com.zzkko_.app_.BaseActivityCallBack.f-method-checks-the-clipboard-for-and-providing-the-clipboard-text-as-a-parameter-to-method-k-2-1024x289.png)Figure 5. The _com.zzkko.app.BaseActivityCallBack.f_ method checks the clipboard for “$” and “://”, providing the clipboard text as a parameter to method _k_

Method _com.zzkko.app.BaseActivityCallBack.k_ initiates a flow that performs a POST request to the server at _BaseUrlConstant.APP_URL_ \+ “ _/marketing/tinyurl/phrase_ ”, which resolves to _https://api-service[.]shein[.]com/marketing/tinyurl/phrase_ :

![graphical user interface, text, application](https://www.microsoft.com/en-us/security/blog/wp-content/uploads/2023/03/Figure-6.-Method-com.zzkko_.app_.BaseActivityCallBack.k-initiating-a-flow-which-performs-a-POST-request-to-the-server-at-BaseUrlConstant.APP_URL-marketingtinyurlphrase-2-1024x199.png)Figure 6. Method _com.zzkko.app.BaseActivityCallBack.k_ initiating a flow, whichperforms a POST request to the server at _BaseUrlConstant.APP_URL_ \+ “ _/marketing/tinyurl/phrase_ ”

Since all of the application’s activities (user interfaces) extend _com.zzkko.base.ui.BaseActivity_ , the call chain described above was triggered any time the user launched a new activity, such as by starting or resuming the application or performing certain actions within the app.

### Verifying the code’s clipboard behavior

To verify our static analysis findings, we performed a dynamic analysis of the application, which we installed from the Google Play Store onto a Samsung device running Android 9.

We used [Frida](https://frida.re/) to intercept calls to the _android.content.ClipboardManager.getText_ and _com.zzkko.util.MarketClipboardPhaseLinker.f_ methods to analyze the application’s clipboard behavior. We also used Frida to bypass the application’s certificate pinning to enable us to analyze network traffic using [Burp Proxy](https://portswigger.net/burp/documentation/desktop/tools/proxy).

We set the contents of the device clipboard to _https://mybank[.]com/token=secretToken &transaction=100$_ and opened the application.

Upon opening the application, the following calls were logged: 

![Graphical user interface, text, application](https://www.microsoft.com/en-us/security/blog/wp-content/uploads/2023/03/Figure-7.-Call-log-displaying-the-apps-clipboard-filtering-1024x662.png)Figure 7. Call log displaying the app’s clipboard filtering

In Figure 7 above, we observe the following: 

  * **Lines 28** : Call to the function _com.zzkko.util.MarketClipboardPhaseLinker.f_
  * **Lines 29-49** : Stack trace to the function _com.zzkko.util.MarketClipboardPhaseLinker.__f_
  * **Lines 53, 55** : Calls to the _hasPrimaryClip_ and _getPrimaryClip_ methods of the _ClipboardManager_

Finally, a POST request to _api-service[.]shein[.]co_ m is performed. Subsequently, we captured the following request in Burp Proxy, showing the transmission of the clipboard contents to the remote server: 

![Graphical user interface, text, application depicting the transmission of the clipboard contents to the remote server.](https://www.microsoft.com/en-us/security/blog/wp-content/uploads/2023/03/Figure-8.-Transmission-of-the-clipboard-contents-to-the-remote-server-1024x222.png)Figure 8. Transmission of the clipboard contents to the remote server

## Android clipboard protections

As displayed in this case involving SHEIN, Android applications can call the _android.text.ClipboardManager_ API to read from or write to the device clipboard without requesting the user’s approval or requiring any specific Android permission. While calling the _ClipboardManager_ API can allow apps to make processes easier for users, such as quickly selecting text to copy, applications often should not need to do this since copying and pasting is typically performed by the device input method editor (keyboard), which is a separate application.

To address our research findings and the broader issue at hand, Google has recognized the risks associated with clipboard access and has made the following improvements to the Android platform to protect users:

On Android 10 and above, an application [cannot access the clipboard unless it currently has focus (is actively running on the device display) or is set as the default input method editor](https://developer.android.com/about/versions/10/privacy/changes#clipboard-data) (keyboard). This restriction guards against background applications accessing the clipboard, but it would not have prevented the behavior described here because the SHEIN application was running in the foreground.

On Android 12 and above, [a toast message notifies the user when an application calls the ClipboardManager to access clipboard data from another application for the first time](https://developer.android.com/about/versions/12/behavior-changes-all#clipboard-access-notifications).****

![Android message stating "Office pasted from your clipboard."](https://www.microsoft.com/en-us/security/blog/wp-content/uploads/2023/03/Figure-9.-Example-toast-message-shown-at-bottom-of-screen-when-the-device-clipboard-is-accessed..png) Figure 9. Example toast message shown at bottom of screen when the device clipboard is accessed.

Android 13 [clears the contents of the clipboard after a period of time](https://www.android.com/android-13/#a13-proactive-protection) to provide an additional degree of protection.

Users can protect themselves by watching out for the clipboard access message. If the message unexpectedly shows, they should assume that any data on the clipboard has been potentially compromised, and they should consider removing any applications that make suspicious clipboard accesses.

## Responsible disclosure and industry collaboration improves security for all

Although we’re not aware of any malicious intent by SHEIN, even seemingly benign behaviors in applications can be exploited with malicious intent. Threats targeting clipboards can put any copied and pasted information at risk of being stolen or modified by attackers, such as passwords, financial details, personal data, cryptocurrency wallet addresses, and other sensitive information.

We recommend users further follow the security guidelines below to defend against this and similar risks:

  * Always keep the device and the installed applications updated
  * Never install applications from untrusted sources
  * Consider removing applications with unexpected behaviors, such as clipboard access toast notifications, and report the behavior to the vendor or app store operator

After discovering the SHEIN Android application clipboard behavior, we worked with Google’s Android Security Team to ensure the removal of this behavior from the app. We thank both the Google and SHEIN teams for their efforts and collaboration in addressing the issue.

At Microsoft, we value, protect, and defend privacy—and this case demonstrates our efforts to investigate and protect customers’ privacy beyond security threats. As the threat landscape continues to evolve, Microsoft strives to continuously improve security for all through research-driven protection and collaboration with customers, partners, and industry experts, regardless of the device or platform in use.

We will continue to work with the security community to share research and intelligence about risks and threats in the effort to build better protection for all.

**_Dimitrios Valsamaras_** _,**Michael Peck** Microsoft 365 Defender Research Team_ __

## References

  * [Xiao Zhang and Wenliang Du, Attacks on Android Clipboard, International Conference on Detection of Intrusions and Malware and Vulnerability Assessment, July 2014.](https://web.ecs.syr.edu/~wedu/Research/paper/clipboard_attack_dimva2014.pdf)
  * [Lukas Stefanko, First clipper malware discovered on Google Play, ESET, February 2019.](https://www.welivesecurity.com/2019/02/08/first-clipper-malware-google-play/)
  * [ThreatFabric, S.O.V.A. – A new Android Banking trojan with fowl intentions, September 2021.](https://www.threatfabric.com/blogs/sova-new-trojan-with-fowl-intentions.html)
  * [Mishaal Rahman, Android 13 changelog, September 2022.](https://blog.esper.io/android-13-deep-dive/)

![](https://www.microsoft.com/en-us/security/blog/wp-content/themes/blog-in-a-box/dist/images/default-avatar.png)

  * [ X ](https://x.com/MsftSecIntel)
  * [ LinkedIn ](https://www.linkedin.com/showcase/microsoft-threat-intelligence/)

##  Microsoft Threat Intelligence 

[ See Microsoft Threat Intelligence posts ](https://www.microsoft.com/en-us/security/blog/author/microsoft-security-threat-intelligence/)

## Related posts

  * ![Graphic showing an icon of a key and digital lines representing secure access issues](https://www.microsoft.com/en-us/security/blog/wp-content/uploads/2026/04/MS_Actional-Insights_Access.webp)

April 9  9 min read 

##  [ Intent redirection vulnerability in third-party SDK exposed millions of Android wallets to potential risk  ](https://www.microsoft.com/en-us/security/blog/2026/04/09/intent-redirection-vulnerability-third-party-sdk-android/)

A severe Android intent‑redirection vulnerability in a widely deployed SDK exposed sensitive user data across millions of apps. 

  * ![Two colleagues in a courtyard on a laptop](https://www.microsoft.com/en-us/security/blog/wp-content/uploads/2024/08/OpenVpn-featured-image-1.webp)

August 8, 2024  15 min read 

##  [ Chained for attack: OpenVPN vulnerabilities discovered leading to RCE and LPE  ](https://www.microsoft.com/en-us/security/blog/2024/08/08/chained-for-attack-openvpn-vulnerabilities-discovered-leading-to-rce-and-lpe/)

Microsoft researchers found multiple vulnerabilities in OpenVPN that could lead to an attack chain allowing remote code execution and local privilege escalation. 

  * ![Young businesswoman holding a phone, looking out her office window overlooking the city](https://www.microsoft.com/en-us/security/blog/wp-content/uploads/2024/05/Featured-image.jpg)

May 1, 2024  15 min read 

##  [ “Dirty stream” attack: Discovering and mitigating a common vulnerability pattern in Android apps  ](https://www.microsoft.com/en-us/security/blog/2024/05/01/dirty-stream-attack-discovering-and-mitigating-a-common-vulnerability-pattern-in-android-apps/)

Microsoft discovered a vulnerability pattern in multiple popular Android applications that could enable a malicious application to overwrite files in the vulnerable application’s internal data storage directory, which could lead to arbitrary code execution and token theft, among other impacts.
