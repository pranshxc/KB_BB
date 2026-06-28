---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-10-02_arbitrary-code-execution-on-facebook-for-android-through-download-feature.md
original_filename: 2020-10-02_arbitrary-code-execution-on-facebook-for-android-through-download-feature.md
title: Arbitrary code execution on Facebook for Android through download feature
category: documents
detected_topics:
- mobile-security
- command-injection
- path-traversal
- supply-chain
tags:
- imported
- documents
- mobile-security
- command-injection
- path-traversal
- supply-chain
language: en
raw_sha256: 62976f9b0e9d0cb3ed0cd15d51dfdc70d6a43ad33a0f5ff98f1a4752b6fcd3dd
text_sha256: dc0ca76381216e2f027320a0f8bb31c3058c6e143e3d52d8b2b073b74039b452
ingested_at: '2026-06-28T07:32:03Z'
sensitivity: unknown
redactions_applied: false
---

# Arbitrary code execution on Facebook for Android through download feature

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-10-02_arbitrary-code-execution-on-facebook-for-android-through-download-feature.md
- Source Type: markdown
- Detected Topics: mobile-security, command-injection, path-traversal, supply-chain
- Ingested At: 2026-06-28T07:32:03Z
- Redactions Applied: False
- Raw SHA256: `62976f9b0e9d0cb3ed0cd15d51dfdc70d6a43ad33a0f5ff98f1a4752b6fcd3dd`
- Text SHA256: `dc0ca76381216e2f027320a0f8bb31c3058c6e143e3d52d8b2b073b74039b452`


## Content

---
title: "Arbitrary code execution on Facebook for Android through download feature"
url: "https://medium.com/@dPhoeniixx/arbitrary-code-execution-on-facebook-for-android-through-download-feature-fb6826e33e0f"
authors: ["Sayed Abdelhafiz (@dPhoeniixx)"]
programs: ["Meta / Facebook"]
bugs: ["Arbitrary code execution"]
bounty: "10,000"
publication_date: "2020-10-02"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4224
scraped_via: "browseros"
---

# Arbitrary code execution on Facebook for Android through download feature

Sayed Abdelhafiz
 highlighted

Arbitrary code execution on Facebook for Android through a download feature
Sayed Abdelhafiz
Follow
3 min read
·
Oct 2, 2020

512

3

TL;DR

Recently I discovered an ACE on Facebook for Android that can be triaged through download files from the group Files Tab without opening the file.

Background

I was digging into the method that Facebook uses to download files from the group, I found that Facebook uses two different mechanisms to download files. If the user downloads the file from the post itself It will be downloaded via a built-in android service called DownloadManager as far as I know It safe method to download files. If the user decides to download the file from Files Tab It will be downloaded through a different method, In a nutshell, the application will fetch the file and then will save it to the Download directory without any filter.

Press enter or click to view image in full size

Notice: the selected code is the fix that Facebook pushed. The vulnerable code was without this code.

Path traversal

The vulnerability was in the second method, security measures were implemented on the server side when uploading the files but It was easy to bypass. Simply the application fetches the download file and for example, saves the file /sdcard/Downloads/FILE_NAME without filtering the FILE_NAME to protect against path traversal attacks. The first idea that came to my mind is to use path traversal to overwrite native libraries which will lead to executing arbitrary code.

I have set up my burp suite proxy then Intercepted the upload file request and modify the filename to ../../../sdcard/PoC then forward the request.

Press enter or click to view image in full size
Web upload endpoint

Unfortunately, It wasn’t enough due to the security measures on the server side, my path traversal payload was removed. I decide to play with the payload but unfortunately, no payload worked.

Press enter or click to view image in full size
Bypass security measures. (Bypass?)

After many payloads, I wasn’t able to bypass that filter. I came back to browse the application again and may find something useful, It came!

Press enter or click to view image in full size

For the first time, I noticed that I can upload files via Facebook mobile application. set up burp suite proxy on my phone, enable white-hat settings on the application to bypass SSL pinning, intercepted upload file request, modify the filename to ../../../sdcard/PoC, the file was uploaded successfully and my payload is in the filename now!

Get Sayed Abdelhafiz’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

I tried to download the file from the post, but the DownloadManger service is safe as I told so the attack didn’t work. Navigated to the Files Tab, and download the file. And here is our attack. My file was written to /sdcard/PoC!

As I was able to perform path traversal, I can now overwrite the native libraries and perform an ACE attack.

Exploit

To exploit that attack I start a new android NDK project to create a native library and put my arbitrary code on the JNI_OnLoad function to make sure that the evil code will execute when loading the library.

#include <jni.h>
#include <string>
#include <stdlib.h>
JNIEXPORT jint JNI_OnLoad(JavaVM* vm, void* reserved) {
  system(“id > /data/data/com.facebook.katana/PoC”);
  return JNI_VERSION_1_6;
}

I built the project to get my malicious library, then upload it by mobile upload endpoint and renamed it to /../../../../../data/data/com.facebook.katana/lib-xzs/libbreakpad.so

Our exploit now is ready!

PoC Video: https://youtu.be/j0darcE5apo

Timeline

April 29, 2020, at 5:57 AM: Submitted the report to Facebook.
April 29, 2020, at 11:20 AM: Facebook was able to reproduce it.
April 29, 2020, at 12:17 PM: Triaged.
June 16, 2020, at 12:54 PM: The vulnerability has been fixed.
July 15, 2020, at 5:11 PM: Facebook rewarded me!

Have a nice day!
