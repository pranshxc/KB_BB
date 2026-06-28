---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-08-02_path-traversal-arbitrary-file-write.md
original_filename: 2022-08-02_path-traversal-arbitrary-file-write.md
title: Path Traversal / Arbitrary File Write
category: documents
detected_topics:
- path-traversal
- api-security
- sqli
- command-injection
- file-upload
tags:
- imported
- documents
- path-traversal
- api-security
- sqli
- command-injection
- file-upload
language: en
raw_sha256: b302c143f326b24d0c2914bf4b3822df49fefdfde5a153e95ed17f68ce09fdf3
text_sha256: ce8ad8fdc0f1d81d030d13e1949f3529ae15b5a8a13e08c568697e864efb33ed
ingested_at: '2026-06-28T07:32:13Z'
sensitivity: unknown
redactions_applied: false
---

# Path Traversal / Arbitrary File Write

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-08-02_path-traversal-arbitrary-file-write.md
- Source Type: markdown
- Detected Topics: path-traversal, api-security, sqli, command-injection, file-upload
- Ingested At: 2026-06-28T07:32:13Z
- Redactions Applied: False
- Raw SHA256: `b302c143f326b24d0c2914bf4b3822df49fefdfde5a153e95ed17f68ce09fdf3`
- Text SHA256: `ce8ad8fdc0f1d81d030d13e1949f3529ae15b5a8a13e08c568697e864efb33ed`


## Content

---
title: "Path Traversal / Arbitrary File Write"
page_title: "(ZOHO) ManageEngine Desktop Central – Path Traversal / Arbitrary File Write | JUMPSEC Labs"
url: "https://labs.jumpsec.com/zoho-manageengine-desktop-central-path-traversal-arbitrary-file-write/"
final_url: "https://labs.jumpsec.com/zoho-manageengine-desktop-central-path-traversal-arbitrary-file-write/"
authors: ["Tom Ellson (@tde_sec)"]
programs: ["Zoho"]
bugs: ["SQL injection", "Arbitrary file write", "Path traversal"]
publication_date: "2022-08-02"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 2370
---

# (ZOHO) ManageEngine Desktop Central – Path Traversal / Arbitrary File Write

[![\(ZOHO\) ManageEngine Desktop Central – Path Traversal Arbitrary File Write](/assets/img/posts/zoho-manageengine-desktop-central-path-traversal-arbitrary-file-write/2022-05-01-13-22-130555-MEDC.png)](/assets/img/posts/zoho-manageengine-desktop-central-path-traversal-arbitrary-file-write/2022-05-01-13-22-130555-MEDC.png)(ZOHO) ManageEngine Desktop Central – Path Traversal / Arbitrary File Write

Posted  Aug 2, 2022  By _[tellson](https://labs.jumpsec.com/) _

_4 min_ read

(ZOHO) ManageEngine Desktop Central – Path Traversal / Arbitrary File Write __

Contents __

(ZOHO) ManageEngine Desktop Central – Path Traversal / Arbitrary File Write

__

**Software** : Zoho ManageEngine Desktop Central **Affected Versions** : Before 10.0.662 **Vendor page** : https://www.manageengine.com/products/desktop-central/vulnerabilities-in-reports-module.html **CVE Reference** : CVE-2021-46165 & CVE-2021-46166 **Published** : 09/01/2022 **CVSS 3.1 Score** : 8.8 High **Attack Vector** : SQL Injection / Arbitrary File Write **Credits** : Tom Ellson

This is the second post in our two part series on ManageEngine Desktop Central. All of the reported issues have since been acknowledged and resolved by ManageEngine.

JUMPSEC researchers have discovered multiple vulnerabilities in ManageEngine Desktop Central Application (MEDC). This is an endpoint management system that is used widely across the globe and is a prevalent vendor. Successful exploitation of these vulnerabilities would allow an adversary to execute code in the context of highest integrity (NT AUTHORITY / SYSTEM).

**In this second post, we will explore ways of exploiting the issues identified in our previous post, to facilitate attack path traversal leveraging the vulnerabilities identified.**

## **Summary** __

The application grants users full control over the “Images” and “Deployment” modules within the “OSD Controls”. This allows the user to add an application using the “add applications” control within the admin functionality of the “OS Deployment” tab.

Once the user adds the application, the “ _applicationsName_ ” parameter is vulnerable to a path / directory traversal attack. This in turn allows an attacker or user with malicious intent to upload / write any file to the operating system with the highest integrity as SYSTEM. This can then be leveraged to cause denial of service or code execution as SYSTEM.

[![2022 18 01 13 22 121804 MEDC](/assets/img/posts/zoho-manageengine-desktop-central-path-traversal-arbitrary-file-write/2022-18-01-13-22-121804-MEDC-1024x186.png)](/assets/img/posts/zoho-manageengine-desktop-central-path-traversal-arbitrary-file-write/2022-18-01-13-22-121804-MEDC-1024x186.png)

|  
---  
  
## **Attack Path Traversal** __

This attack chain begins with a POST request to the files API endpoint. This endpoint takes standard _webkitformboundary_ data. As there are no file upload restrictions, the endpoint can be used to upload all files inclusive of dll’s and exe’s. As seen below, the POST request to the _/emsapi/files_ endpoint allows for an exe file to be uploaded. Upon successful upload the endpoint returns JSON including the _fileID_ , _fileName_ , _customerID_ , _expiryDate_ and _fileStatus_. Making note of the _fileID_ is important here as it is used in subsequent API requests.

[![2022 11 01 13 22 121118 MEDC](/assets/img/posts/zoho-manageengine-desktop-central-path-traversal-arbitrary-file-write/2022-11-01-13-22-121118-MEDC.png)](/assets/img/posts/zoho-manageengine-desktop-central-path-traversal-arbitrary-file-write/2022-11-01-13-22-121118-MEDC.png)

|  
---  
  
[![2022 11 01 13 22 121128 MEDC](/assets/img/posts/zoho-manageengine-desktop-central-path-traversal-arbitrary-file-write/2022-11-01-13-22-121128-MEDC.png)](/assets/img/posts/zoho-manageengine-desktop-central-path-traversal-arbitrary-file-write/2022-11-01-13-22-121128-MEDC.png)

The _/emsapi/files_ endpoint can be used to introduce any files to the system. Using this function, we attempted to introduce said files to a location other than the intended directory. The initial attempt at traversal on the files API endpoint was unsuccessful, as the filename parameter does not accept any form of path or directory traversal. This is controlled by file name checks on that parameter which prevents the usage of unicode characters and characters that can be used as a traversal technique.

The _/emsapi/osdeployer/applications_ endpoint allows for the user to create a new “ _application_ ” in the system. Upon creation of an _application_ , a folder is created in the applications directory with the file that was uploaded in the previous API call that corresponds with the _fileID_.

The _applicationName_ is used as a basis to create the application directory folder, meaning traversal and identification of the created folder was trivial; developers often forget input sanitation that would prevent the traversal of the file system in order to create files and folders that should belong to the application directory.

If an _applicationName_ is requested that already exists, the application folder will not be created but the file will still be written. Therefore the _system32_ directory can be used and the _system32_ folder will not be overwritten, but the file that pertains to the fileID will be uploaded into _system32_.

[![2022 44 01 13 22 124447 MEDC](/assets/img/posts/zoho-manageengine-desktop-central-path-traversal-arbitrary-file-write/2022-44-01-13-22-124447-MEDC.png)](/assets/img/posts/zoho-manageengine-desktop-central-path-traversal-arbitrary-file-write/2022-44-01-13-22-124447-MEDC.png)

|  
---  
  
[![2022 05 01 13 22 130555 MEDC](/assets/img/posts/zoho-manageengine-desktop-central-path-traversal-arbitrary-file-write/2022-05-01-13-22-130555-MEDC.png)](/assets/img/posts/zoho-manageengine-desktop-central-path-traversal-arbitrary-file-write/2022-05-01-13-22-130555-MEDC.png)

Upon issuing the above API call, the previously uploaded file (_tomtest1.exe_ – _fileID_ 29) is written to the _C:\windows\system32_ \ directory. At this point we had proved arbitrary file write through the application creation endpoint. As per the figure below, the file is being written with the highest file integrity – “NT AUTHORITY\SYSTEM”. Upon file creation, the _java.exe_ binary creates the file and sets the owner to the local administrator’s group.

[![pasted image 0 6](/assets/img/posts/zoho-manageengine-desktop-central-path-traversal-arbitrary-file-write/pasted-image-0-6-1024x554.png)](/assets/img/posts/zoho-manageengine-desktop-central-path-traversal-arbitrary-file-write/pasted-image-0-6-1024x554.png)

|  
---  
  
[![2022 09 01 13 22 130940 MEDC](/assets/img/posts/zoho-manageengine-desktop-central-path-traversal-arbitrary-file-write/2022-09-01-13-22-130940-MEDC.png)](/assets/img/posts/zoho-manageengine-desktop-central-path-traversal-arbitrary-file-write/2022-09-01-13-22-130940-MEDC.png)

Upon achieving arbitrary file write, it’s important to understand the scope of what can be achieved. Arbitrary File Write (AFW) differs from Arbitrary File Overwrite (AFO). File overwrite is more beneficial to us as we don’t really need to find a binary that is called upon file service execution.

However, in this case we had AFW and not AFO, so it was necessary to find an executable or dll that is loaded at run time but was not present on the system. This could be done using first order dll hijacking. However, we opted for an approach similar to what was described [here](https://google.com) The following Java.com binary is missing from the system at service start time.

## **Summary** __

[![pasted image 0 2 1](/assets/img/posts/zoho-manageengine-desktop-central-path-traversal-arbitrary-file-write/pasted-image-0-2-1.png)](/assets/img/posts/zoho-manageengine-desktop-central-path-traversal-arbitrary-file-write/pasted-image-0-2-1.png)

This Arbitrary File Write allows for complete control over the Manage Engine Desktop Central Server as it can be used to execute code.

Whilst this attack requires some levels of privilege to have been obtained already and access to the application creation functionality. This functionality can be abused to achieve code execution at service start time.

This has been reported to the vendor and has been fixed as of the most recent version. The vendor was comprehensive with remediation and quick to respond issues outlined.

This post is licensed under [ CC BY 4.0 ](https://creativecommons.org/licenses/by/4.0/) by the author.

Share [ __](https://twitter.com/intent/tweet?text=\(ZOHO\)%20ManageEngine%20Desktop%20Central%20%E2%80%93%20Path%20Traversal%20/%20Arbitrary%20File%20Write%20-%20JUMPSEC%20Labs&url=https%3A%2F%2Flabs.jumpsec.com%2Fzoho-manageengine-desktop-central-path-traversal-arbitrary-file-write%2F "Twitter") [ __](https://www.linkedin.com/sharing/share-offsite/?url=https%3A%2F%2Flabs.jumpsec.com%2Fzoho-manageengine-desktop-central-path-traversal-arbitrary-file-write%2F "LinkedIn") [ __](https://www.facebook.com/sharer/sharer.php?title=\(ZOHO\)%20ManageEngine%20Desktop%20Central%20%E2%80%93%20Path%20Traversal%20/%20Arbitrary%20File%20Write%20-%20JUMPSEC%20Labs&u=https%3A%2F%2Flabs.jumpsec.com%2Fzoho-manageengine-desktop-central-path-traversal-arbitrary-file-write%2F "Facebook") [ __]( "Link") __
