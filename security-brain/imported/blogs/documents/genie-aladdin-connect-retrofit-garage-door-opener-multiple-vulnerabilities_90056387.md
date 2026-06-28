---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2024-01-03_genie-aladdin-connect-retrofit-garage-door-opener-multiple-vulnerabilities.md
original_filename: 2024-01-03_genie-aladdin-connect-retrofit-garage-door-opener-multiple-vulnerabilities.md
title: 'Genie Aladdin Connect Retrofit Garage Door Opener: Multiple Vulnerabilities'
category: documents
detected_topics:
- xss
- mobile-security
- idor
- command-injection
- api-security
- cloud-security
tags:
- imported
- documents
- xss
- mobile-security
- idor
- command-injection
- api-security
- cloud-security
language: en
raw_sha256: 9005638765d0027b577114c846cca8b5ea14da797ea99d7e5577724e6f70522f
text_sha256: 7d40fe190ba8d3e1649ed24287fadf928dda6567f18d6d4a2286d29a932ac7c3
ingested_at: '2026-06-28T07:32:29Z'
sensitivity: unknown
redactions_applied: false
---

# Genie Aladdin Connect Retrofit Garage Door Opener: Multiple Vulnerabilities

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2024-01-03_genie-aladdin-connect-retrofit-garage-door-opener-multiple-vulnerabilities.md
- Source Type: markdown
- Detected Topics: xss, mobile-security, idor, command-injection, api-security, cloud-security
- Ingested At: 2026-06-28T07:32:29Z
- Redactions Applied: False
- Raw SHA256: `9005638765d0027b577114c846cca8b5ea14da797ea99d7e5577724e6f70522f`
- Text SHA256: `7d40fe190ba8d3e1649ed24287fadf928dda6567f18d6d4a2286d29a932ac7c3`


## Content

---
title: "Genie Aladdin Connect Retrofit Garage Door Opener: Multiple Vulnerabilities"
page_title: "Genie Aladdin Connect Retrofit Garage Door Opener: Multiple Vulnerabilities | Rapid7 Blog"
url: "https://www.rapid7.com/blog/post/2024/01/03/genie-aladdin-connect-retrofit-garage-door-opener-multiple-vulnerabilities/"
final_url: "https://www.rapid7.com/blog/post/2024/01/03/genie-aladdin-connect-retrofit-garage-door-opener-multiple-vulnerabilities/"
authors: ["Deral Heiland (@Percent_X)"]
programs: ["The Genie Company (Aladdin Connect)"]
bugs: ["Android", "XSS", "Insecure data storage", "Missing authentication", "IDOR"]
publication_date: "2024-01-03"
added_date: "2024-01-08"
source: "pentester.land/writeups.json"
original_index: 584
---

Rapid7, Inc. (Rapid7) discovered vulnerabilities in Aladdin Connect retrofit kit garage door opener and Android mobile application produced by Genie. The affected products are:

  * Aladdin Garage door smart retrofit kit, Model ALDCM
  * Android Mobile application ALADDIN Connect, Version 5.65 Build 2075

Rapid7 initially reported these issues to Overhead Door — the parent company of The Genie Company — on August 22nd 2023. Since then, members of our research team have worked alongside the vendor to discuss the impact, resolution, and a coordinated response for these vulnerabilities.

## Product description

The Aladdin Connect garage door opener (Retrofit-kit) is a smart IoT solution which allows standard electric garage doors to be upgraded to support smart technology for remote access and use of mobile applications for opening and closing of the garage door.

## Credit

The vulnerabilities in Genie Aladdin Connect retrofit garage door opener and mobile application were discovered by Deral Heiland, Principal IoT Researcher at Rapid7. They are being disclosed in accordance with [Rapid7’s vulnerability disclosure policy](/security/disclosure/) after coordination with the vendor.

## Vendor statement

Trusted for generations by millions of homeowners, The Genie Company is committed to security, and we collaborate with valued researchers, such as Rapid7, to respond to and resolve vulnerabilities on behalf of our customers.

## Exploitation and remediation

This section details the potential for exploitation and our remediation guidance for the issues discovered and reported by Rapid7, so that defenders of this technology can gauge the impact of, and mitigations around, these issues appropriately.

## Android Application Insecure Storage (CVE-2023-5879) - FIXED

While examining the Android mobile application, Aladdin Connect, for general security issues, Rapid7 found that the user’s password was stored in clear text in the following file:

  * _/data/data/com.geniecompany.AladdinConnect/shared_prefs/com.genie.gdocntl.MainActivity.xml_

The persistence of this data was tested by logging out and rebooting the device. Typically logging out and rebooting a mobile device leads to the data being purged from the device. In this case neither the file, nor its contents, were purged. Figure 2 is copy of file content after logout and reboot:

![Screenshot-2024-01-03-at-12.58.11-PM.png](https://www.rapid7.com/cdn/images/blt908590221d3d676b/683de66c18a5536c96687240/Screenshot-2024-01-03-at-12.58.11-PM.png)

## Exploitation

An attacker with physical access to the user’s smartphone (i.e., via a lost or stolen phone), would be able to potentially extract this critical data, allowing access to the user’s service account to control the garage door opener.

## Remediation

To mitigate this vulnerability, users should [set a password pin code](https://support.google.com/android/answer/9079129?hl=en) on the mobile devices to restrict access.

## Additional Note from Vendor

This vulnerability is tied to the biometric capability (touch or face recognition).

Mitigation: Update to the latest app upgrade available in the play store. App version v5.73

## Cross-site Scripting (XSS) injected into Aladdin Connect garage door opener (Retrofit-Kit) configuration setup web server console via broadcast SSID name (CVE-2023-5880)

When the Aladdin connect device is placed into Wi-Fi configuration mode, the user web interface used for configuring the device is vulnerable to XSS injection via broadcast SSID names containing HTML and or JavaScript.

### Exploitation

This XSS attack via SSID injection method can be done by running a software-based Wi-Fi access point to broadcast HTML or JavaScript as the SSID name such as:

  * </script><svg onload=alert(1)>

An example of this is shown in Figure 3, using airbase-ng to broadcast the HTML and or JavaScript code:

![Screenshot-2024-01-03-at-1.02.28-PM.png](https://www.rapid7.com/cdn/images/blt4aa8b8b740566e07/683de689da5c30676da8368a/Screenshot-2024-01-03-at-1.02.28-PM.png)

In the example found in Figure 4, a simple alert box is triggered on the Aladdin base unit Wi-Fi configuration webpage from the above SSID name. Also, the image on the right of Figure 4 shows the actual web page source delivered to the end user. No user interaction is needed to trigger this, they only need to view the web page during configuration mode.

![Screenshot-2024-01-03-at-1.03.10-PM.png](https://www.rapid7.com/cdn/images/bltf44c6c32732fe9c4/683de6af4b2b7f552ee16305/Screenshot-2024-01-03-at-1.03.10-PM.png)

Also, a denial of service (DoS) of the Wi-Fi configuration page can be accomplished by just broadcasting an SSID containing </script> preventing the web page from being used to configure the device's setup. This corrupted web page is shown in Figure 5:

![Screenshot-2024-01-03-at-1.03.49-PM.png](https://www.rapid7.com/cdn/images/blt5368550c61712661/683de6d770aa950109fe31f6/Screenshot-2024-01-03-at-1.03.49-PM.png)

## Remediation

To mitigate this vulnerability, users should avoid running setup if any oddly named SSIDs are being broadcast in the general vicinity, such as SSIDs containing HTML markup language and/or JavaScript code in their names.

Also, in general the mobile application can be used to set up and configure the Garage Door opener. This will avoid any direct interaction with the vulnerable “ Garage Door Control Setup” configuration page.

## Additional Notes from the Vendor

This is a very low-impact vulnerability with minimal risk. This can only occur when the owner places the device in the wifi configuration mode for a limited period and the intruder operates within the 2.4 GHz band distance range during that limited configuration period. The device will not be impacted by the misconfiguration if that were to occur and it is fully capable of recovering from misconfiguration. The device cannot be operated with a misconfigured SSID as the device can only be claimed by the owner using the mobile app. There is no vulnerability in the mobile app which is the approved mode of device provisioning.

Mitigation: Use mobile app to configure the device.

## Unauthenticated access allowed to web interface for “Garage Door Control Module Setup” page (CVE-2023-5881) - FIXED

This vulnerability allows a user with network access to connect to the Aladdin Connect device web server's “Garage Door Control Module Setup” web page and alter the Garage doors connected WIFI SSID settings without authenticating.

### Exploitation

The device allows unauthenticated access to Garage Door Control Module Setup configuration page on TCP Port 80, This allows anyone with network access to reconfigure the Wi-Fi settings without being challenged to authenticate. A sample of this access to the configuration web page is shown in Figure 6:

![Screenshot-2024-01-03-at-1.03.49-PM.png](https://www.rapid7.com/cdn/images/blt5368550c61712661/683de6d770aa950109fe31f6/Screenshot-2024-01-03-at-1.03.49-PM.png)

### Remediation

To prevent exploitation, users should only attach the Aladdin Garage door smart retrofit kit to a network they own and control. Also, access to this network should not be allowed from any other network source such as the Internet.

### Additional Notes from the Vendor

This is a very low-impact vulnerability with minimal risk. This can only occur when the intruder has access to the same local network as the retrofit kit (use the same network router), so the attack vector is limited to local. This web interface is not accessible from the internet. The device cannot be operated with a misconfigured SSID, as the device can only be claimed using the mobile app that an owner would use.

Mitigation: Update the Retrofit device to the latest software version, 14.1.1. Fix was automatically updated on all online devices as of December 2023. Please reach out to customer service to confirm if your device has the update.

## Authenticated user access to others users data via service API - FIXED

An authenticated user can gain unauthorized access to other users’ data by querying the following API using a different device ID than their own.

  * https://pxdqkls7aj.execute-api.us-east-1.amazonaws.com/Android/devices/879267

Here are sample fields that are potentially viewable data using this method:

![Screenshot-2024-01-03-at-1.45.48-PM.png](https://www.rapid7.com/cdn/images/bltc25153fdfe28b3b4/683de6fb30073ee7b3eb1a46/Screenshot-2024-01-03-at-1.45.48-PM.png) ![Screenshot-2024-01-03-at-1.46.07-PM.png](https://www.rapid7.com/cdn/images/bltbdaf302e7bb77ab7/683de71c3a1c5a55914baa78/Screenshot-2024-01-03-at-1.46.07-PM.png)

## Additional Notes from the Vendor

This was resolved immediately after our internal penetration testing detected the issue. This happened because of a recent software update. The fix was applied to the API on 07/25/2023.

Mitigation: None

[![LinkedIn](/linkedin-logo.svg)](https://www.linkedin.com/shareArticle?mini=true&url=https%3A%2F%2Fwww.rapid7.com%2Fblog%2Fpost%2F2024%2F01%2F03%2Fgenie-aladdin-connect-retrofit-garage-door-opener-multiple-vulnerabilities&title=Genie%20Aladdin%20Connect%20Retrofit%20Garage%20Door%20Opener%3A%20Multiple%20Vulnerabilities)[![Facebook](/facebook-logo.svg)](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.rapid7.com%2Fblog%2Fpost%2F2024%2F01%2F03%2Fgenie-aladdin-connect-retrofit-garage-door-opener-multiple-vulnerabilities)[![X](/x-logo.svg)](https://twitter.com/intent/tweet?url=https%3A%2F%2Fwww.rapid7.com%2Fblog%2Fpost%2F2024%2F01%2F03%2Fgenie-aladdin-connect-retrofit-garage-door-opener-multiple-vulnerabilities&text=Genie%20Aladdin%20Connect%20Retrofit%20Garage%20Door%20Opener%3A%20Multiple%20Vulnerabilities)[![Bluesky](/bluesky-dark-logo.svg)](https://bsky.app/intent/compose?text=Genie%20Aladdin%20Connect%20Retrofit%20Garage%20Door%20Opener%3A%20Multiple%20Vulnerabilities%20https%3A%2F%2Fwww.rapid7.com%2Fblog%2Fpost%2F2024%2F01%2F03%2Fgenie-aladdin-connect-retrofit-garage-door-opener-multiple-vulnerabilities)

#### Article Tags

  * [IoT](/blog/tag/iot-security-news/)

[![Deral Heiland](/_next/image/?url=https%3A%2F%2Fwww.rapid7.com%2Fcdn%2Fimages%2Fblt9f9db121928e3816%2F6840441898bc4eb9f1818b21%2FDeral-Heiland.jpg&w=256&q=75)Deral HeilandAuthor Posts](/blog/author/deral-heiland/)
