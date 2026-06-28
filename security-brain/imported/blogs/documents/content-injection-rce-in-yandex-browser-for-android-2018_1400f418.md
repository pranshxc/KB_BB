---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-03-03_content-injection-rce-in-yandex-browser-for-android-2018.md
original_filename: 2021-03-03_content-injection-rce-in-yandex-browser-for-android-2018.md
title: Content Injection (RCE) in Yandex Browser for Android [2018]
category: documents
detected_topics:
- command-injection
- automation-abuse
- api-security
- mobile-security
tags:
- imported
- documents
- command-injection
- automation-abuse
- api-security
- mobile-security
language: en
raw_sha256: 1400f418ad26bf9d07b7982eb7f501b6d10d7c2fd710c0387eda175f761df571
text_sha256: 49a3666dd6b0309d0b0473c73f4229e3cc450773becb02c664c9612003a083b4
ingested_at: '2026-06-28T07:32:05Z'
sensitivity: unknown
redactions_applied: false
---

# Content Injection (RCE) in Yandex Browser for Android [2018]

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-03-03_content-injection-rce-in-yandex-browser-for-android-2018.md
- Source Type: markdown
- Detected Topics: command-injection, automation-abuse, api-security, mobile-security
- Ingested At: 2026-06-28T07:32:05Z
- Redactions Applied: False
- Raw SHA256: `1400f418ad26bf9d07b7982eb7f501b6d10d7c2fd710c0387eda175f761df571`
- Text SHA256: `49a3666dd6b0309d0b0473c73f4229e3cc450773becb02c664c9612003a083b4`


## Content

---
title: "Content Injection (RCE) in Yandex Browser for Android [2018]"
page_title: "Content Injection (RCE) in Yandex Browser for Android [2018] | Nightwatch Cybersecurity"
url: "https://wwws.nightwatchcybersecurity.com/2021/03/03/content-injection-rce-in-yandex-browser-for-android-2018/"
final_url: "https://wwws.nightwatchcybersecurity.com/2021/03/03/content-injection-rce-in-yandex-browser-for-android-2018/"
authors: ["Nightwatch Cybersecurity (@nightwatchcyber)"]
programs: ["Yandex"]
bugs: ["MiTM"]
publication_date: "2021-03-03"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3843
---

# Content Injection (RCE) in Yandex Browser for Android [2018]

[March 3, 2021](https://wwws.nightwatchcybersecurity.com/2021/03/03/content-injection-rce-in-yandex-browser-for-android-2018/) [nightwatchcyber](https://wwws.nightwatchcybersecurity.com/author/nightwatchcyber/) [Advisories](https://wwws.nightwatchcybersecurity.com/category/advisories/)[Android](https://wwws.nightwatchcybersecurity.com/tag/android/), [yandex](https://wwws.nightwatchcybersecurity.com/tag/yandex/)

## Summary

The **Yandex Browser** Android application provided by **Yandex** can be injected with malicious content by an MITM attacker. Because this application is a web browser, this can lead directly to remote code execution (RCE) within the app. The root cause is lack of SSL being used in the help section of the app as well as some other links in the about section, homepage and search engines. Because these links are likely to be clicked on by users and may be considered by users to be “more trusted”, they should be protected.

The recommended fix is to change all of these to use HTTPS instead of HTTP. The vendor has been notified but has not fixed the issue since they do not consider it to be a security problem. No CVE has been assigned. Version tested is v17.11.1.628, it is not known if other versions are affected.

Since vendor stopped responding in 2019, this is now publicly disclosed.

## Vulnerability Details

**Yandex Browser** is a web browser application based on Google’s Chromium and made by Yandex. While monitoring network traffic of a test device running Android, we observed that the help section of the application makes an initial HTTP call is made to a non-HTTPS site, which then redirects to an HTTPS version. There are also additional hyperlinks within the about section and the homepage which do not use HTTPS, as well as some search engines as set in the settings. Because these links are likely to be clicked on by users and may be considered by users to be “more trusted”, they should be protected.

Because the initial call is done without HTTPS, it is possible for an MITM attacker to intercept this traffic and inject their own content. **Since this is a web browser, this can result in remote code execution within the application since all the content is web based.  
**

Screenshots of the captured traffic:

![Screenshot_20180225-163514](https://wwws.nightwatchcybersecurity.com/wp-content/uploads/2018/02/screenshot_20180225-163514.png?w=169&h=300) ![Screenshot_20180225-163523](https://wwws.nightwatchcybersecurity.com/wp-content/uploads/2018/02/screenshot_20180225-163523.png?w=169&h=300)

## **Steps To Replicate (on Ubuntu 17.10)**

1\. Install the application on the Android device but do not start it.

2a. Install **dnsmasq** and **NGINX** on the Linux host:
  
  
  sudo apt-get install dnsmasq nginx
  

2b, Configure NGINX by changing the following in /etc/nginx/nginx.conf:
  
  
  default_type text/html;
  charset utf-8;

3\. Modify the **/etc/hosts** file to add the following entry to map the domain name to the Linux host:
  
  
  192.168.1.x help.yandex.com

4\. Configure**/etc/dnsmasq.conf** file to listen on the IP and restart DNSMASQ
  
  
  listen-address=192.168.1.x
  sudo /etc/init.d/dnsmasq restart

5\. Add a file with malicious content (you may need to use sudo):
  
  
  cd /var/www/html
  echo powned >mbrowser
  

6\. Modify the settings on the Android test phone to static, set DNS to point to “192.168.1.x”. AT THIS POINT – Android will resolve DNS against the Linux computer and serve the large servers file

7\. Open the app on the Android device, tap on the three vertical dots to the right of the URL bar, and select “Settings” to open the settings menu. Scroll to the bottom and tap “Help”.

We also checked [the HSTS preload list](https://hstspreload.org/) maintained by Chrome and did not find the “help.yandex.com” domain on that list. Therefore, Chromium on which this application is build would not force HTTPs for these URLs by default.

All testing was done on v17.11.1.628 of the Android application using a Linux host running Ubuntu v17.10 and Android test device running Android v7.

## Additional Vectors – “About” Links

There are also several links within the about section that do not use SSL and lead to the same result. To get that section, tap the “Settings” menu, scroll to the bottom and select “About”:

![Screenshot_20180225-163626](https://wwws.nightwatchcybersecurity.com/wp-content/uploads/2018/02/screenshot_20180225-163626.png?w=169&h=300)

These include the following links:

  * “Build xxx” credits – uses domain “storage.ape.yandex.net”
  * “Blink” – uses domain “chromium.org”
  * “Chromium” – uses domain “www.chromium.org”
  * “Opera Turbo” – uses domain “www.opera.com”
  * “License Agreement” – uses domain “m.legal.yandex.ru”

Screenshots of captured traffic below:

![Screenshot_20180225-163816](https://wwws.nightwatchcybersecurity.com/wp-content/uploads/2018/02/screenshot_20180225-163816.png?w=169&h=300) ![Screenshot_20180225-163732](https://wwws.nightwatchcybersecurity.com/wp-content/uploads/2018/02/screenshot_20180225-163732.png?w=169&h=300) ![Screenshot_20180225-163708](https://wwws.nightwatchcybersecurity.com/wp-content/uploads/2018/02/screenshot_20180225-163708.png?w=169&h=300) ![Screenshot_20180225-163743](https://wwws.nightwatchcybersecurity.com/wp-content/uploads/2018/02/screenshot_20180225-163743.png?w=169&h=300) ![Screenshot_20180225-163826](https://wwws.nightwatchcybersecurity.com/wp-content/uploads/2018/02/screenshot_20180225-163826.png?w=169&h=300)

## Additional Vectors – Homepage

There are also several links within the homepage of the application that do not use SSL and lead to the same result. To get that section, open the app and drag the screen down to display all of them. They also show up as a banner in the top of the Android screen in other apps as well – to see, go anywhere in the OS and drag down the top of the screen. Screenshots:

![Screenshot_20180225-184156](https://wwws.nightwatchcybersecurity.com/wp-content/uploads/2018/02/screenshot_20180225-184156.png?w=169&h=300) ![Screenshot_20180225-184205](https://wwws.nightwatchcybersecurity.com/wp-content/uploads/2018/02/screenshot_20180225-184205.png?w=169&h=300)

Of these, the following do not use SSL / HTTPS:

  * YouTube – uses domain “m.youtube.com”
  * Booking – uses domain “www.booking.com”

Screenshots of traffic attached:

![Screenshot_20180225-184258](https://wwws.nightwatchcybersecurity.com/wp-content/uploads/2018/02/screenshot_20180225-184258.png?w=169&h=300) ![Screenshot_20180225-184312](https://wwws.nightwatchcybersecurity.com/wp-content/uploads/2018/02/screenshot_20180225-184312.png?w=169&h=300)

## Additional Vectors – Search Engines

Some of the search engines that the browser supports are also not configured to use SSL, thus allowing for injection. To reach the search engine settings, tap the right side of the URL bar with the vertical “three dots” icon to show the settings menu, then scroll down to “Search Engine”. Screenshots attached:

![Screenshot_20180225-184941](https://wwws.nightwatchcybersecurity.com/wp-content/uploads/2018/02/screenshot_20180225-184941.png?w=169&h=300) ![Screenshot_20180225-184945](https://wwws.nightwatchcybersecurity.com/wp-content/uploads/2018/02/screenshot_20180225-184945.png?w=169&h=300)

In particular, the following search engines are affected:

  * Bing (which is used by default) – uses domains “m.trovi.com”, “m.bing.com” and “www.bing.com”

Screenshots of captured traffic attached:

![Screenshot_20180225-184645](https://wwws.nightwatchcybersecurity.com/wp-content/uploads/2018/02/screenshot_20180225-184645.png?w=169&h=300) ![Screenshot_20180225-184652](https://wwws.nightwatchcybersecurity.com/wp-content/uploads/2018/02/screenshot_20180225-184652.png?w=169&h=300) ![Screenshot_20180225-184658](https://wwws.nightwatchcybersecurity.com/wp-content/uploads/2018/02/screenshot_20180225-184658.png?w=169&h=300)

## Recommended Mitigation and Vendor Response

The recommended fix is to change all of these links to use HTTPS instead of HTTP. The vendor doesn’t consider these to be a security issue and has no plans to fix these issues at this time.

Users should consider using a different browser.

## References

Google Play Link: <https://play.google.com/store/apps/details?id=com.yandex.browser>

## Credits

Text of the advisory written by Y. Shafranovich.

# Timeline

2017-12-17: Initial report to the vendor via their bounty page  
2017-12-25: Initial vendor reply rejecting the bug, and our follow-up  
2018-01-14: Reminder email sent to the vendor  
2018-01-15: Vendor unable to replicate the issue  
2018-01-23: Reply to vendor sent  
2018-01-25: Follow-up communications with the vendor  
2018-01-26: Vendor asks for video  
2018-02-10: Videos and payloads sent to the vendor  
2018-02-14: Reminder email to vendor sent  
2018-02-22: Vendor rejecting the report, and a follow-up communication  
2018-02-25: Draft advisory sent to the vendor for review, along with another video  
2021-03-03: Vendor stopped responding in 2019; public disclosure

### Share this:

  * [ Share on X (Opens in new window) X ](https://wwws.nightwatchcybersecurity.com/2021/03/03/content-injection-rce-in-yandex-browser-for-android-2018/?share=twitter)
  * [ Share on Facebook (Opens in new window) Facebook ](https://wwws.nightwatchcybersecurity.com/2021/03/03/content-injection-rce-in-yandex-browser-for-android-2018/?share=facebook)
  * 

Like Loading...
