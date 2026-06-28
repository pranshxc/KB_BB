---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-10-24_missing-authentication-in-zkteco-zemzmm-web-interface.md
original_filename: 2022-10-24_missing-authentication-in-zkteco-zemzmm-web-interface.md
title: Missing Authentication in ZKTeco ZEM/ZMM Web Interface
category: documents
detected_topics:
- access-control
- command-injection
- otp
- automation-abuse
- api-security
tags:
- imported
- documents
- access-control
- command-injection
- otp
- automation-abuse
- api-security
language: en
raw_sha256: f2549493919770c06e82637e1b5678cd53276c58af5c86277dc510365bb5fe2d
text_sha256: b41fe15a567245b14d3400183f3eae43222333b1d601d50bb13ae13929a59093
ingested_at: '2026-06-28T07:32:15Z'
sensitivity: unknown
redactions_applied: false
---

# Missing Authentication in ZKTeco ZEM/ZMM Web Interface

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-10-24_missing-authentication-in-zkteco-zemzmm-web-interface.md
- Source Type: markdown
- Detected Topics: access-control, command-injection, otp, automation-abuse, api-security
- Ingested At: 2026-06-28T07:32:15Z
- Redactions Applied: False
- Raw SHA256: `f2549493919770c06e82637e1b5678cd53276c58af5c86277dc510365bb5fe2d`
- Text SHA256: `b41fe15a567245b14d3400183f3eae43222333b1d601d50bb13ae13929a59093`


## Content

---
title: "Missing Authentication in ZKTeco ZEM/ZMM Web Interface"
page_title: "Missing Authentication in ZKTeco ZEM/ZMM Web Interface - RedTeam Pentesting"
url: "https://www.redteam-pentesting.de/en/advisories/rt-sa-2021-003/-missing-authentication-in-zkteco-zem-zmm-web-interface"
final_url: "https://www.redteam-pentesting.de/en/advisories/rt-sa-2021-003/"
authors: ["RedTeam Pentesting (@RedTeamPT)"]
programs: ["ZKTeco"]
bugs: ["Missing authentication"]
publication_date: "2022-10-24"
added_date: "2022-11-01"
source: "pentester.land/writeups.json"
original_index: 2004
---

![RedTeam Pentesting Header](/img/header/hl_header-1_hu_41ae128fa05e8693.webp)![RedTeam Pentesting Header](/img/header/hl_header-2_hu_b706eecb349ae33b.webp)![RedTeam Pentesting Header](/img/header/hl_header-3_hu_e5161ed53e060a19.webp)![RedTeam Pentesting Header](/img/header/hl_header-4_hu_127be93f1f7e2e27.webp)![RedTeam Pentesting Header](/img/header/hl_header-5_hu_ac28592db6870bd2.webp)![RedTeam Pentesting Header](/img/header/hl_header-6_hu_d040b8f4d4afe3ea.webp)![RedTeam Pentesting Header](/img/header/hl_header-7_hu_81ca52d452974fe5.webp)![RedTeam Pentesting Header](/img/header/hl_header-8_hu_1f647add36239205.webp)

[__newer ](https://www.redteam-pentesting.de/en/advisories/rt-sa-2021-004/)[back to overview](/en/advisories)[older __](https://www.redteam-pentesting.de/en/advisories/rt-sa-2021-002/)

# Missing Authentication in ZKTeco ZEM/ZMM Web Interface

The ZKTeco time attendance device does not require authentication to use the web interface, exposing the database of employees and their credentials.

### Details

  * Product: ZKTeco ZEM500-510-560-760, ZEM600-800, ZEM720, ZMM
  * Affected Versions: potentially versions below 8.88 (ZEM500-510-560-760, ZEM600-800, ZEM720) and 15.00 (ZMM200-220-210)
  * Fixed Versions: firmware version 8.88 (ZEM500-510-560-760, ZEM600-800, ZEM720), firmware version 15.00 (ZMM200-220-210)
  * Vulnerability Type: Missing Authentication
  * Security Risk: medium
  * Vendor URL: `https://zkteco.eu/company/history`
  * Vendor Status: fixed version released
  * Advisory URL: `https://www.redteam-pentesting.de/advisories/rt-sa-2021-003`
  * Advisory Status: published
  * CVE: CVE-2022-42953
  * CVE URL: `https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-42953`

### Introduction

“Time attendance and workforce management is an integrated set of processes that an institution uses to optimize the productivity of its employees on the individual, departmental, and entity-wide levels. ZKTeco has been at the forefront of time attendance solutions for the last 30 years, integrating advanced biometric technologies with innovative and versatile terminals.” (from company website)

### More Details

The ZKTeco ZEM/ZMM device allows to store a list of users and their credentials which may be used to log into the device to prove the users’ attendance. These credentials can either be a PIN, a card for a variety of card readers, or a fingerprint. The user list can be managed through the web interface.

When opening the web interface, for example on `http://192.0.2.1/`, the web server of the device sends a Set-Cookie header for a cookie with name and value similar to the following:
  
  
  Set-Cookie: SessionID=1624553126; path=/;
  

It was determined that the value of the cookie is roughly the number of seconds since January 1, 1970. Since the value has a constant offset, that might allow attackers to guess the cookie value. After setting the cookie, the webserver redirects the browser to “/csl/login”. The login form provided at this URL has its form action set to “/csl/check”. If the user provides wrong credentials, the web server responds with an error message. If the user provides correct credentials, the server responds with a frameset.

In this frameset various options are available, for example a user list. The list contains a link titled “Options” for each user item which references a URL similar to the following

`http://192.0.2.1/csl/user?did=0&uid=123`

Additionally, backups of all settings of the device can be downloaded from the backup page. The request to do so looks similar to the following:
  
  
  POST /form/DataApp HTTP/1.1
  Host: 192.0.2.1
  User-Agent: Mozilla/5.0
  Cookie: SessionID=1624553126
  Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
  Accept-Language: en-US,en;q=0.5
  Accept-Encoding: gzip, deflate
  Content-Type: application/x-www-form-urlencoded
  Content-Length: 7
  Origin: http://192.0.2.1
  Referer: http://192.0.2.1/form/Device?act=11
  
  style=1
  

When the value “1” is given for the field named “style”, the web server responds with the file “device.dat” (corresponding to the option “Backup System Data” in the web interface), for all other values the server responds with the file “data.dat” (corresponding to the option “Backup User Data” in the web interface). Both files can not only be requested using HTTP-POST, but also using HTTP-GET with the following URLs:
  
  
  http://192.0.2.1/form/DataApp?style=1
  http://192.0.2.1/form/DataApp?style=0
  

Both files are - even though it’s not obvious from the filename -compressed tar archives. They can be extracted in the following way:
  
  
  $ mv data.dat data.tgz
  $ tar xvzf data.tgz
  rwxr-xr-x root/root  0 1970-01-01 01:08 mnt/mtdblock/group.dat
  rwxr-xr-x root/root  0 1970-01-01 01:08 mnt/mtdblock/htimezone.dat
  rwxr-xr-x root/root  0 1970-01-01 01:08 mnt/mtdblock/lockgroup.dat
  rwxrwxrwx 500/513  10512 2021-06-23 07:23 mnt/mtdblock/ssruser.dat
  rwxr-xr-x root/root 819896 2021-06-18 07:23 mnt/mtdblock/tempinfo.dat
  rwxrwxrwx 500/513  19456 2005-05-05 07:05 mnt/mtdblock/template.dat
  rw-r--r-- root/root 360448 2021-06-18 07:23 mnt/mtdblock/templatev10.dat
  rwxr-xr-x root/root  0 1970-01-01 01:08 mnt/mtdblock/timezone.dat
  rwxrwxrwx 500/513  1372 2005-05-05 07:25 mnt/mtdblock/user.dat
  rwxr-xr-x root/root  120 1970-01-01 01:08 mnt/mtdblock/data/alarm.dat
  rwxr-xr-x root/root  0 2021-06-23 09:55 mnt/mtdblock/data/extlog.dat
  rwxr-xr-x root/root  0 2013-05-04 01:28 mnt/mtdblock/data/extuser.dat
  rwxr-xr-x root/root  0 1970-01-01 01:08 mnt/mtdblock/data/group.dat
  rwxr-xr-x root/root  0 1970-01-01 01:08 mnt/mtdblock/data/htimezone.dat
  rwxr-xr-x root/root  0 1970-01-01 01:08 mnt/mtdblock/data/lockgroup.dat
  rwxr-xr-x root/root  54800 2021-06-23 09:55 mnt/mtdblock/data/oplog.dat
  rwxr-xr-x root/root  33200 2021-06-23 07:23 mnt/mtdblock/data/sms.dat
  rwxr-xr-x root/root  0 2021-06-23 09:55 mnt/mtdblock/data/ssrattlog.dat
  rwxr-xr-x root/root  660 2018-11-09 17:28 mnt/mtdblock/data/stkey.dat
  rwxrwxrwx 500/513  0 2013-05-04 01:28 mnt/mtdblock/data/template.dat
  rwxr-xr-x root/root  0 1970-01-01 01:08 mnt/mtdblock/data/timezone.dat
  rwxr-xr-x root/root  0 1970-01-01 01:08 mnt/mtdblock/data/transaction.dat
  rwxr-xr-x root/root  952 2021-06-23 07:24 mnt/mtdblock/data/udata.dat
  rwxr-xr-x root/root  0 1970-01-01 01:08 mnt/mtdblock/data/user.dat
  rwxr-xr-x root/root  0 2013-05-04 01:28 mnt/mtdblock/data/wkcd.dat
  

In this archive, the file “mnt/mtdblock/templatev10.dat” will likely contain fingerprints, and the file “mnt/mtdblock/ssruser.dat” contains the user database. The user database contains 72 byte user records, each containing the privilege level, the PIN, the name of the user, data stored on external authentication tokens like cards, and the group of the user.

While the cookie value might be guessable, it is not used for authentication purposes. An attacker with knowledge of the corresponding URLs could access the user detail view or the backup without any authentication.

### Proof of Concept
  
  
  http://192.0.2.1/form/DataApp?style=1
  http://192.0.2.1/form/DataApp?style=0
  http://192.0.2.1/csl/user?did=0&uid=123
  

### Workaround

Network access to the device should be limited to trustworthy persons. This might be hard to implement if the device is installed in a public space, especially if it is used for access control, too.

### Fix

According to the vendor, upgrading to Version 8.88 for ZEM500-510-560-760, ZEM600-800, ZEM720 or version 15.00 for ZMM200-220-210 resolves the vulnerability.

### Security Risk

Attackers with network access to a ZKTeco ZEM/ZMM time attendance device can get access to employee data, including the credentials used for accessing the time attendance device. If these credentials are used for other purposes than time attendance, such as physical access control, attackers might use them to gain access to protected areas. The actual risk estimate varies wildly with the kind of access control system in place and whether network access to the device is prevented by other means, such as nearby security guards. For this reason, missing authentication to the ZEM/ZMM web interface is estimated to pose a medium risk. This estimate might need to be adjusted to the specific use case of the device.

### Timeline

  * 2021-06-24 Vulnerability identified
  * 2021-07-12 Customer approved disclosure to vendor
  * 2021-07-16 Vendor notified
  * 2021-08-20 Vendor provides fixed firmware
  * 2022-09-29 Customer approved release of advisory
  * 2022-10-10 CVE ID requested
  * 2022-10-15 CVE ID assigned
  * 2022-10-24 Advisory published

### RedTeam Pentesting GmbH

RedTeam Pentesting offers individual penetration tests performed by a team of specialised IT-security experts. Hereby, security weaknesses in company networks or products are uncovered and can be fixed immediately.

As there are only few experts in this field, RedTeam Pentesting wants to share its knowledge and enhance the public knowledge with research in security-related areas. The results are made available as public security advisories.

More information about RedTeam Pentesting can be found at: <https://www.redteam-pentesting.de/>

### Working at RedTeam Pentesting

RedTeam Pentesting is looking for penetration testers to join our team in Aachen, Germany. If you are interested please visit: <https://jobs.redteam-pentesting.de/>
