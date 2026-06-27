---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '146179'
original_report_id: '146179'
title: 'REG: Content provider information leakage'
weakness: Command Injection - Generic
team_handle: nextcloud
created_at: '2016-06-21T07:24:01.841Z'
disclosed_at: '2016-06-24T08:48:39.291Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 4
tags:
- hackerone
- command-injection-generic
---

# REG: Content provider information leakage

## Metadata

- HackerOne Report ID: 146179
- Weakness: Command Injection - Generic
- Program: nextcloud
- Disclosed At: 2016-06-24T08:48:39.291Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

Issue :
While analyzing your code of manifest.xml i found a issue related to content provider information leakage .

Issue description :

Your content provider settings will allowing any other app on the device to access it (AndroidManifest.xml). You should modify the attribute to [exported="false"] or set at least "signature" protectionalLevel permission if you don't want to.

where i found the issue :

 provider => com.owncloud.android.providers.FileContentProvider
 provider => com.owncloud.android.ui.adapter.DiskLruImageCacheFileProvider

Whats the impact : 

other apps can read the contents,the malformed application can be used to extract information from the content provider .

Code from your manifest.xml kinldy note that **exported=true**  :
<service
            android:name=".authentication.AccountAuthenticatorService"
            android:exported="true" >
            <intent-filter android:priority="100" >
                <action android:name="android.accounts.AccountAuthenticator" />
            </intent-filter>
  <meta-data
                android:name="android.accounts.AccountAuthenticator"
                android:resource="@xml/authenticator" />
        </service>
        <service
            android:name=".syncadapter.FileSyncService"
            android:exported="true" >
            <intent-filter>
                <action android:name="android.content.SyncAdapter" />
            </intent-filter>
    <meta-data
                android:name="android.content.SyncAdapter"
                android:resource="@xml/syncadapter_files" />
        </service>
  <provider
            android:name=".providers.FileContentProvider"
            android:authorities="@string/authority"
            android:enabled="true"
            android:exported="false"
            android:label="@string/sync_string_files"
            android:syncable="true" />

<provider
            android:name=".providers.UsersAndGroupsSearchProvider"
            android:authorities="com.nextcloud.android.providers.UsersAndGroupsSearchProvider"
            android:enabled="true"
            android:exported="false"
            android:label="@string/search_users_and_groups_hint" />
<activity
            android:name=".authentication.AuthenticatorActivity"
            android:exported="true"
            android:launchMode="singleTask"
            android:theme="@style/Theme.ownCloud.noActionBar" >
            <intent-filter>
                <action android:name="android.intent.action.VIEW" />
 <category android:name="android.intent.category.DEFAULT" />
                <category android:name="android.intent.category.BROWSABLE" />
<data android:scheme="@string/oauth2_redirect_scheme" />
            </intent-filter>
            <intent-filter>
                <action android:name="com.owncloud.android.workaround.accounts.CREATE" />
<category android:name="android.intent.category.DEFAULT" />
            </intent-filter>
</activity>


references : 

(1)https://www.nowsecure.com/mobile-security/ebay-android-content-provider-injection-vulnerability.html
(2)http://blog.trustlook.com/2013/10/23/ebay-android-content-provider-information-disclosure-vulnerability/
(3)http://www.wooyun.org/bugs/wooyun-2010-039169

Let me know incase of any other concerns

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
