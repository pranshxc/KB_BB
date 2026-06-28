---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2016-05-12_firefoxos-find-my-device-service-clickjacking-bug-results-in-changing-pins-wipin.md
original_filename: 2016-05-12_firefoxos-find-my-device-service-clickjacking-bug-results-in-changing-pins-wipin.md
title: FirefoxOS Find My Device Service Clickjacking Bug results in Changing PINs,
  Wiping and Locking Phones!
category: documents
detected_topics:
- clickjacking
- mobile-security
- xss
- command-injection
- path-traversal
- mfa
tags:
- imported
- documents
- clickjacking
- mobile-security
- xss
- command-injection
- path-traversal
- mfa
language: en
raw_sha256: 8b4bf48d7a6bad0839d4a4e42fd70521772890cebb26fca7e620704e74344252
text_sha256: 13136bfff9572c7deb72e42b7d7d1e25ffc4d48cff715d0398ce37b5caf14875
ingested_at: '2026-06-28T07:31:55Z'
sensitivity: unknown
redactions_applied: false
---

# FirefoxOS Find My Device Service Clickjacking Bug results in Changing PINs, Wiping and Locking Phones!

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2016-05-12_firefoxos-find-my-device-service-clickjacking-bug-results-in-changing-pins-wipin.md
- Source Type: markdown
- Detected Topics: clickjacking, mobile-security, xss, command-injection, path-traversal, mfa
- Ingested At: 2026-06-28T07:31:55Z
- Redactions Applied: False
- Raw SHA256: `8b4bf48d7a6bad0839d4a4e42fd70521772890cebb26fca7e620704e74344252`
- Text SHA256: `13136bfff9572c7deb72e42b7d7d1e25ffc4d48cff715d0398ce37b5caf14875`


## Content

---
title: "FirefoxOS Find My Device Service Clickjacking Bug results in Changing PINs, Wiping and Locking Phones!"
page_title: "FirefoxOS Find My Device Service Clickjacking Bug results in Changing PINs, Wiping and Locking Phones! – Seekurity"
url: "https://www.seekurity.com/blog/general/firefox-find-my-device-service-clickjacking/"
final_url: "https://seekurity.com/blog/2016/05/12/admin/general/firefox-find-my-device-service-clickjacking"
authors: ["Mohamed A. Baset"]
programs: ["Mozilla"]
bugs: ["Clickjacking"]
publication_date: "2016-05-12"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 6298
---

**Introduction:**

Physical devices connected with web applications made everything easy to be managed. Screen size, availability, usage etc… is what pushing everyone to manage their devices through their desktops/laptops! On the other hand such advantages poses a threat if these web applications contains security issues!

For example android devices can be managed through “Google Device Manager”, iOS devices can be managed by “iCloud service”, Windows Phone devices can be managed via your Microsoft account, FirefoxOS devices can be managed also through your Mozilla account and finally Internet of Things devices or (IoT) are connected to their own vendors dedicated web apps!!

.

**About Firefox OS**

[Firefox OS](https://en.wikipedia.org/wiki/Firefox_OS) (project name: Boot to Gecko, also known as B2G) is an open-source operating system – made for smartphones, tablet computers and smart TVs – designed by Mozilla and external contributors, based on the rendering engine of their Firefox web browser and the Linux kernel.

Firefox OS is designed to provide a complete, community-based alternative operating system, for running web applications directly or those installed from an application marketplace. The applications use open standards and approaches such as JavaScript and HTML5, a robust privilege model, open web APIs that can communicate directly with hardware, e.g. cellphone hardware. As such, it competes with commercially developed operating systems such as Apple’s iOS, Google’s Android, Microsoft’s Windows Phone, BlackBerry’s BlackBerry 10 and Jolla’s Sailfish OS.

.  
**About Firefox Find My Device Service**

[Find My Device](https://wiki.mozilla.org/CloudServices/FindMyDevice) (aka “Where’s My Fox”) is a Firefox OS Service which is used to provide a means for users to locate, track and purge devices remotely.

Example Use Cases, MVP User Stories  
1) Albert can’t remember the location of his phone. Going to a nearby computer, he logs into WheresMyFox and requests the phone to report it’s location. The phone reports that it is nearby, so Albert requests the device to ring. Albert quickly finds that his phone is in his coat pocket.

2) Bea discovers that her phone is missing. Using a friends phone, she logs into WheresMyFox and requests the phone to report it’s location. She discovers that the phone is currently headed down Broadway, and realizes she has left it in the cab. Realizing that she may never see her phone again, she requests the phone to remotely wipe itself, before calling the cab agency to see if she can recover her device.

And here’s our story…

.

**[*] The bug:**

Firefox Find My Device service is not protected against [clickjacking](https://www.owasp.org/index.php/Clickjacking) vulnerability neither with the typical “X-Frame-Options” nor with the JS frame busting technique that means a malicious attacker capable of iframing the whole service and tricking the end-users to perform unwanted actions!

.

****[*]** Rolling around the bug:**

To iframe the service and perform a successful Clickjacking attack you need to know the full url of the service which contains a “Device ID” which is a random alphanumeric value (non guessable because it’s a 32 alphanumeric value or even can be MiTMed because of the fact that the service is using HTTPS).

So what we’re doing here?

Studied the web application more, tested it against other issues (XSS, CSRF, Open Redirections, etc..) but it seems pretty solid! hmmm I took a deep breath, drink some power stuff and suddenly came up with a nasty idea!

What about exploiting the usability?

Modern Web Applications are usually designed to satisfy the user’s sake of USABILITY so to be straightforward, “Find My Device” service is redirecting you automatically to the device id page but in one condition (if you’re already logged in from a browser that was used before to access the service “a trusted browser”) that little notice brought the whole scenario back to life, By calling an internal url eg. “https://find.firefox.com/” thanks to the usability thing we’re redirected to our treasure “https://find.firefox.com/8fcXXXXc40de04b3803945XXXXXXXXXX” and we’re good to go!

.

**Affected URL(s):**  
https://find.firefox.com

.

![](https://seekurity.com/blog/wp-content/uploads/2016/05/Screen-Shot-2016-05-12-at-4.03.14-AM.png)

.

**What attackers can do using such vulnerability?:**  
1- Erase the victim’s device data with just only 3 clicks by the victim himself if he tricked with “click here to win a 50 BTC for Example”  
2- Lock The victim device or change his lock code if it is the first time to be set “4 clicks”  
3- Makes the Device ringing “2 clicks”

.  
**PoC Video:**

.

**More Details About clickjacking:**  
Because of no frame busting techniques or X-Frame-Options header, the whole website is vulnerable to Clickjacking attacks which could lead to a full account takeover considering such scenario:  
1\. Attacker will iframe any sensitive the website page and adjust the iframe size and add a “divs” as a layers on the unwanted-to-show parts of the original web page to fool and trick the user.  
2\. User get tricked by the crafted page and followed the attacker’s instruction to do a specific clicks to the iframed page  
3\. Unwanted actions happened in the logged in user’s session in result to the attack’s clicks.

..

**Mitigation** :  
1- Add an X-Frame-Options HTTP Header and set it’s value to “Deny” or “Sameorigin” as you can see it suitable to mitigate such attacks  
2- Use iframe busting techmiques in JS code like this:

<script type=”text/javascript”>  
if (self === top) {  
var antiClickjack = document.getElementById (“antiClickjack”);  
antiClickjack.parentNode. removeChild(antiClickjack);  
} else {  
top.location = ‘Your_Website_URL_Here’;  
}  
</script>

or

<script type=”text/javascript”>  
// Disable frame hijacking  
if (top != self)  
top.location.href = location.href;  
</script>

.

**The Fix:**

Mozilla fixed the issue by implementing the X-Frame-Options header with a value of “DENY” which means even the same domain can’t iframe itself, Good job!

.

.

**References and other URLs:**

<http://news.softpedia.com/news/firefox-findmydevice-service-lets-hackers-wipe-or-lock-phones-change-pins-495003.shtml>

<http://techworm.net/2015/10/mozillas-firefox-find-my-device-lets-hackers-wipe-or-lock-phones-change-pins.html>

<https://www.dhs.gov/sites/default/files/publications/dhs-daily-report-2015-10-22.pdf> (Item 25)

<http://www.mnrdaily.com/article/mozilla-firefox-find-my-device-feature-allows-hackers-to-wipe-or-lock-phones-and-change-pins/5235.htm>

<http://www.nuanjiong.cn/page/news_softpedia_com/news/firefox-findmydevice-service-lets-hackers-wipe-or-lock-phones-change-pins-495003.shtml>

[http://flavioontivero.weebly.com/tech-news—noticias/mozillas-firefox-find-my-device-lets-hackers-wipe-or-lock-phones-change-pins-firefox-de-mozilla-buscar-mi-dispositivo-le-hackers-limpiar-o-bloquear-celulares-cambiar-pin](http://flavioontivero.weebly.com/tech-news---noticias/mozillas-firefox-find-my-device-lets-hackers-wipe-or-lock-phones-change-pins-firefox-de-mozilla-buscar-mi-dispositivo-le-hackers-limpiar-o-bloquear-celulares-cambiar-pin)

<http://www.expl0its.com/?p=4253>

[Hall of Fame (4th Quarter 2014) ](https://www.mozilla.org/en-US/security/bug-bounty/web-hall-of-fame/)

<https://developer.mozilla.org/en-US/docs/Web/HTTP/X-Frame-Options>

.

.

Thanks for reading, Till the next adventure!

.

**Hey!**  
Building a website? Or already built a one? Think twice before going public and let us [protect your business](https://www.seekurity.com/#pricing)!

[](https://www.addtoany.com/add_to/facebook?linkurl=https%3A%2F%2Fseekurity.com%2Fblog%2F2016%2F05%2F12%2Fadmin%2Fgeneral%2Ffirefox-find-my-device-service-clickjacking&linkname=FirefoxOS%20Find%20My%20Device%20Service%20Clickjacking%20Bug%20results%20in%20Changing%20PINs%2C%20Wiping%20and%20Locking%20Phones%21 "Facebook")[](https://www.addtoany.com/add_to/pinterest?linkurl=https%3A%2F%2Fseekurity.com%2Fblog%2F2016%2F05%2F12%2Fadmin%2Fgeneral%2Ffirefox-find-my-device-service-clickjacking&linkname=FirefoxOS%20Find%20My%20Device%20Service%20Clickjacking%20Bug%20results%20in%20Changing%20PINs%2C%20Wiping%20and%20Locking%20Phones%21 "Pinterest")[](https://www.addtoany.com/add_to/twitter?linkurl=https%3A%2F%2Fseekurity.com%2Fblog%2F2016%2F05%2F12%2Fadmin%2Fgeneral%2Ffirefox-find-my-device-service-clickjacking&linkname=FirefoxOS%20Find%20My%20Device%20Service%20Clickjacking%20Bug%20results%20in%20Changing%20PINs%2C%20Wiping%20and%20Locking%20Phones%21 "Twitter")[](https://www.addtoany.com/add_to/whatsapp?linkurl=https%3A%2F%2Fseekurity.com%2Fblog%2F2016%2F05%2F12%2Fadmin%2Fgeneral%2Ffirefox-find-my-device-service-clickjacking&linkname=FirefoxOS%20Find%20My%20Device%20Service%20Clickjacking%20Bug%20results%20in%20Changing%20PINs%2C%20Wiping%20and%20Locking%20Phones%21 "WhatsApp")[](https://www.addtoany.com/add_to/telegram?linkurl=https%3A%2F%2Fseekurity.com%2Fblog%2F2016%2F05%2F12%2Fadmin%2Fgeneral%2Ffirefox-find-my-device-service-clickjacking&linkname=FirefoxOS%20Find%20My%20Device%20Service%20Clickjacking%20Bug%20results%20in%20Changing%20PINs%2C%20Wiping%20and%20Locking%20Phones%21 "Telegram")[](https://www.addtoany.com/add_to/linkedin?linkurl=https%3A%2F%2Fseekurity.com%2Fblog%2F2016%2F05%2F12%2Fadmin%2Fgeneral%2Ffirefox-find-my-device-service-clickjacking&linkname=FirefoxOS%20Find%20My%20Device%20Service%20Clickjacking%20Bug%20results%20in%20Changing%20PINs%2C%20Wiping%20and%20Locking%20Phones%21 "LinkedIn")[](https://www.addtoany.com/add_to/google_gmail?linkurl=https%3A%2F%2Fseekurity.com%2Fblog%2F2016%2F05%2F12%2Fadmin%2Fgeneral%2Ffirefox-find-my-device-service-clickjacking&linkname=FirefoxOS%20Find%20My%20Device%20Service%20Clickjacking%20Bug%20results%20in%20Changing%20PINs%2C%20Wiping%20and%20Locking%20Phones%21 "Gmail")[](https://www.addtoany.com/share)

and  Bug  Changing  ClickJacking  Device  Find  FirefoxOS  in  Locking  My  Phones!  PINs  results  Service  Wiping
