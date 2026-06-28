---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-12-20_from-postauth-rce-to-preauth-rce-on-liferay-portal.md
original_filename: 2022-12-20_from-postauth-rce-to-preauth-rce-on-liferay-portal.md
title: From PostAuth RCE to PreAuth RCE on Liferay Portal
category: blogs
detected_topics:
- command-injection
- mfa
- cloud-security
- supply-chain
tags:
- imported
- blogs
- command-injection
- mfa
- cloud-security
- supply-chain
language: en
raw_sha256: 7e9a92fa6b24c31a26f10bccab24099b0d51163bc919e025ad90f612ebb89263
text_sha256: 83bd0e98a63b763d09d1457701bfa3dbd232108957ae0d4fb3dd5a4715444d64
ingested_at: '2026-06-28T07:32:16Z'
sensitivity: unknown
redactions_applied: false
---

# From PostAuth RCE to PreAuth RCE on Liferay Portal

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-12-20_from-postauth-rce-to-preauth-rce-on-liferay-portal.md
- Source Type: markdown
- Detected Topics: command-injection, mfa, cloud-security, supply-chain
- Ingested At: 2026-06-28T07:32:16Z
- Redactions Applied: False
- Raw SHA256: `7e9a92fa6b24c31a26f10bccab24099b0d51163bc919e025ad90f612ebb89263`
- Text SHA256: `83bd0e98a63b763d09d1457701bfa3dbd232108957ae0d4fb3dd5a4715444d64`


## Content

---
title: "From PostAuth RCE to PreAuth RCE on Liferay Portal"
page_title: "An advisory for CVE-2019-16891: From PostAuth RCE to PreAuth RCE on Liferay Portal"
url: "https://dappsec.substack.com/p/an-advisory-for-cve-2019-16891-from"
final_url: "https://dappsec.substack.com/p/an-advisory-for-cve-2019-16891-from"
authors: ["RV Sharma"]
programs: ["Liferay"]
bugs: ["RCE", "Insecure deserialization"]
publication_date: "2022-12-20"
added_date: "2022-12-26"
source: "pentester.land/writeups.json"
original_index: 1758
---

# From PostAuth RCE to PreAuth RCE on Liferay Portal

### The post presents a discovery about CVE-2019-16891 that allows exploiting this vulnerability on Liferay Portal without authentication as everyone knows.

[![Dappsec's avatar](https://substackcdn.com/image/fetch/$s_!0vu7!,w_36,h_36,c_fill,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F0552a2d4-33f0-49f9-8ca6-325da0d4a358_578x610.png)](https://substack.com/@dappsec)

[Dappsec](https://substack.com/@dappsec)

Dec 20, 2022

2

Share

## About CVE-2019-16891

### References

  * [The public announcement of Liferay](https://portal.liferay.dev/learn/security/known-vulnerabilities/-/asset_publisher/HbL5mxmVrnXW/content/cst-7111)

> Liferay Portal 7.1.0 and earlier is vulnerable to remote code execution (RCE) via deserialization of JSON data.

  * [NVD database](https://nvd.nist.gov/vuln/detail/CVE-2019-16891)

According to NVD database, CVE-2019-16891 has a CVSS score of 8.8

because it requires an account on Liferay to exploit successfully.

[![](https://substackcdn.com/image/fetch/$s_!cA2l!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2Facf716fe-c946-44a8-ac40-b4aecf2185ad_1034x685.png)](https://substackcdn.com/image/fetch/$s_!cA2l!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2Facf716fe-c946-44a8-ac40-b4aecf2185ad_1034x685.png)Privileges Required (PR): Low

  * [Analysis from VNPT Cyber Immunity](https://sec.vnpt.vn/2019/09/liferay-deserialization-json-deserialization-part-4/)

### The root cause

Liferay [overridden ](https://github.com/liferay/liferay-portal/blob/6.2.x/portal-impl/src/com/liferay/portal/json/JSONFactoryImpl.java#L177)`deserialize` func when implementing `JSONFactoryImpl` class from `com.liferay.portal.kernel.json.JSONFactory `
  
  
  @Override
  public Object deserialize(String json) {
  try {
  return _jsonSerializer.fromJSON(json);
  }

We can see the actual deserialization issue is deeper:

  1. `deserialize()` call `fromJSON()`

  2. `fromJSON() `call `unmarshall()` : <https://github.com/Servoy/jabsorb/blob/master/src/org/jabsorb/JSONSerializer.java#L262>

  3. So the vulnerability is inside `org.jabsorb.JSONSerializer` library.

Liferay Team was fixed in 2018 by implementing `getClassFromHint `to whitelist during deserialization.

  * <https://github.com/liferay/liferay-portal/blame/master/portal-impl/src/com/liferay/portal/json/jabsorb/serializer/LiferayJSONSerializer.java#L68-L82>

## Found Second Vulnerable Endpoint

After determining the root cause. I searched the source code for locations using the `deserialize` function with the keyword `JSONFactoryUtil.deserialize`. A sufficient condition for successful exploiting is that the parameter passed to `JSONFactoryUtil.deserialize` is taint from user input.

  
And this is the location I found: <https://github.com/liferay/liferay-portal/blob/6.2.x/portal-impl/src/com/liferay/portal/action/PortletURLAction.java#L167:L172>

The endpoint is map to Portlet URL feature (turn off by default) and here is the endpoint that can be successfully called without authentication: 

### PoC
  
  
  POST /c/portal/portlet_url HTTP/1.1
  Host: liferay.victim.example.com
  User-Agent: Mozilla/5.0 
  Accept: */*
  Accept-Language: en-US,en;q=0.5
  Accept-Encoding: gzip, deflate
  X-Requested-With: XMLHttpRequest
  Content-Type: application/x-www-form-urlencoded; charset=UTF-8
  Origin: http://liferay.victim.example.com
  Connection: close
  Referer: http://liferay.victim.example.com
  
  parameterMap={"Json payload for deserialization in here!"}

[![](https://substackcdn.com/image/fetch/$s_!oEDL!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2Fe02b9348-ac4c-4cc6-9822-af5f374a49fc_1205x789.png)](https://substackcdn.com/image/fetch/$s_!oEDL!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2Fe02b9348-ac4c-4cc6-9822-af5f374a49fc_1205x789.png)

## Detect vulnerable Liferay Portal instance

  * `GET /c/portal/portlet_url` return 200 status code

[![](https://substackcdn.com/image/fetch/$s_!bYPV!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F2d0b2e76-b6e9-4d8f-a8c3-6a637952705c_582x155.png)](https://substackcdn.com/image/fetch/$s_!bYPV!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F2d0b2e76-b6e9-4d8f-a8c3-6a637952705c_582x155.png)

  * Version <= 7.1.0

## Conclusion

  * New CVSS score: 9.8 - Critical ([https://nvd.nist.gov/vuln-metrics/cvss/v3-calculator?vector=AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H&version=3.1](https://nvd.nist.gov/vuln-metrics/cvss/v3-calculator?vector=AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H&version=3.1))

  * Upgrade Liferay Portal (<https://liferay.dev/portal/security/known-vulnerabilities/-/asset_publisher/jekt/content/cst-7111>)

  * **Liferay Portal 7.1:** There is no patch available for Liferay Portal 7.1.0. Instead, users should upgrade to [Liferay Portal 7.1 CE GA2 (7.1.1)](http://sourceforge.net/projects/lportal/files/Liferay%20Portal/7.1.1%20GA2/) or later.

  * **Liferay Portal 7.0** : Source patch for Liferay Portal 7.0 GA7 (7.0.6) is available on [GitHub](https://github.com/community-security-team/liferay-portal/compare/7.0.6-ga7...7.0.6-cumulative.patch). Details for working with source patches can be found on the [Patching Liferay Portal](https://liferay.dev/learn/security/patching) page.

  * **Liferay Portal 6.2** : Source patch for Liferay Portal 6.2 GA6 (6.2.5) is available on [GitHub](https://github.com/community-security-team/liferay-portal/compare/6.2.5-ga6...6.2.5-cumulative.patch). Details for working with source patches can be found on the [Patching Liferay Portal](https://liferay.dev/learn/security/patching) page.  
  

## Update

  * 12/21/2022: [NVD rescored CVSS to 9.8 for this vulnerability](https://nvd.nist.gov/vuln/detail/CVE-2019-16891#VulnChangeHistorySection)

  * 12/27/2022: [MITRE added my advisory to the References](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-16891)

[About me on Twitter](https://twitter.com/lnlinh31)

Thanks for reading DappSec Blog! Subscribe for free to receive new posts and support my work.

Subscribe

2

Share
