---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-05-01_apache-solr-831-rce-from-exposed-administration-interface.md
original_filename: 2023-05-01_apache-solr-831-rce-from-exposed-administration-interface.md
title: Apache Solr 8.3.1 RCE from exposed administration interface
category: documents
detected_topics:
- path-traversal
- api-security
- command-injection
- file-upload
- automation-abuse
tags:
- imported
- documents
- path-traversal
- api-security
- command-injection
- file-upload
- automation-abuse
language: en
raw_sha256: 4d88a896cf379a2edd3dada70a72bfd3e9ad75b9f0bae8059f5790ffb2e48872
text_sha256: f4457e48e946f6b719cdc1eb26eb3c52fae6aee34faf4b09770d97551cdf5dbe
ingested_at: '2026-06-28T07:32:20Z'
sensitivity: unknown
redactions_applied: false
---

# Apache Solr 8.3.1 RCE from exposed administration interface

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-05-01_apache-solr-831-rce-from-exposed-administration-interface.md
- Source Type: markdown
- Detected Topics: path-traversal, api-security, command-injection, file-upload, automation-abuse
- Ingested At: 2026-06-28T07:32:20Z
- Redactions Applied: False
- Raw SHA256: `4d88a896cf379a2edd3dada70a72bfd3e9ad75b9f0bae8059f5790ffb2e48872`
- Text SHA256: `f4457e48e946f6b719cdc1eb26eb3c52fae6aee34faf4b09770d97551cdf5dbe`


## Content

---
title: "Apache Solr 8.3.1 RCE from exposed administration interface"
page_title: "Apache Solr 8.3.1 RCE from exposed administration interface – SCRT Team Blog"
url: "https://blog.scrt.ch/2023/05/01/solr-rce-from-exposed-administration-interface/"
final_url: "https://blog.scrt.ch/2023/05/01/solr-rce-from-exposed-administration-interface/"
authors: ["Nicolas Brunner"]
programs: ["Apache Solr"]
bugs: ["RCE", "Unrestricted file upload", "XSLT injection", "Path traversal"]
publication_date: "2023-05-01"
added_date: "2023-05-04"
source: "pentester.land/writeups.json"
original_index: 1204
---

# Apache Solr 8.3.1 RCE from exposed administration interface

Back in 2020, during an external pentest, I stumbled upon a visible Solr administration panel. With nothing else of interest, I focused on this specific application to test what was hidden underneath.

![](/wp-content/uploads/2020/11/SolrBasePage-1024x462.png)_Main page of Solr_

The version of Apache Solr was 8.3.1 and running on Windows. Note that this pentest was performed in 2020, way before the discovery of _log4j_. Under this specific version, the application should be vulnerable to _CVE-2019-17558_ :

When text queries are handled by Solr, it is possible to add a custom Apache Velocity template that is processed with the result of the query. The issue is that this functionality can be activated **without authentication**. With this enabled Server-Side Template Injection, it is pretty straightforward to reach code execution using built-in feature of the Velocity language.

Solr solved this issue both in 8.3.1 and 8.4.0 by disabling the Velocity template rendering of this custom query by default. Furthermore the configuration is not modifiable from API endpoints anymore. However, version 8.3.1 is still vulnerable if some specific conditions are fulfilled, but not in this specific case. BummerŌĆ”

I then downloaded the exact same version from the Solr official website, opened the documentation, and started exploring the application in my Windows VM.

### First findings

On the main page, a large amount of information about the system is revealed, such as different paths on the server, as well as the version of Solr. On the left of the following screenshot, there are _no cores available_.

![](/wp-content/uploads/2020/11/SolrBasePage-1024x462.png)_Index page of Solr disclosing interesting information_

Apache Solr is based on _Cores_. Every _core_ is a separated database that can be queried and deleted from the web interface. It is also possible to create new _cores_ , but the user has to upload configuration files manually to the server beforehand.

From the point of view of the file directory of the server, each _core_ has a named directory inside `{Base Dir}/server/solr/{Core name}`. At the same level, there is also a default directory named `configsets` that contains examples of Solr core with their required files. I quickly found out that a dummy core can be created by using the default config files present in this directory. This creation is possible because there is no restriction to limit the path of the _InstanceDir_ variable. Because of that, it is possible have access to at least one core and its functionality, even on a brand new Solr installation. The parameters _instanceDir_ and _dataDir_ can be set to any absolute or relative path, which could simplify attacks.

![](/wp-content/uploads/2020/11/SolrCreateNewCore-1-1024x602.png)_The instanceDir is set to the path of the configsets directory_

![](/wp-content/uploads/2020/11/SolrCreateNewCore2-1024x489.png)_The new core is created_

This is also a good gadget for older CVEs of Solr such as _CVE-2019-17558_ , because most of them require that at least one _core_ be present in order to be exploitable.

While testing for _CVE-2019-17558_ , the documentation states that queries can be processed by Velocity or XSLT files if they exist in a specific directory. This is always a good thing to keep in mind, as arbitrary XSLT file upload would often mean arbitrary code execution on the server if they are interpreted.

Here is the summary of what was found so far:

  * If discovered, an arbitrary file upload can be used to execute arbitrary code.
  * A core can be created without the requirements of uploading files to the server.
  * If the node creation fails, it is possible to create empty directories anywhere on the disk.
  * It’s possible to discover if a file exists on the computer because of different errors returned by the interface using the core creation module.
  * The majority of the parameters of Solr are vulnerable to path traversals.

### File upload

In a _core_ , it is possible to upload files and send data to be processed by the backend. Using the test files provided by Solr, the application processes them and does not save them on the server. However, when the size of a file exceeds a threshold, the server saves the full contents inside a `.tmp` file in the server directory `{Base Dir}/server/tmp/`. 

![](/wp-content/uploads/2020/11/fileUpload-1024x624.png)_The page from the web UI that enables file upload._

The temporary file is stored with the following name: _`upload_{UUID}_{iterator}.tmp`. _

The UUID is a constant value that is set at each reboot of the Solr server. The iterator is set to `000000000` for the first uploaded file. It is then incremented if a new `.tmp` file is added to the folder. In the `/tmp` folder, the files are deleted after 1 hour, which leaves enough time to be used for our exploitation.

![](/wp-content/uploads/2020/11/directoryUpload.png)

I did not find another place where the UUID could be leaked, but since the server is running on Windows, the trick of **_Windows Short File Name_** can be used:

On Windows, files can have a simpler names composed of 6 alphanumeric characters followed by a tile character and a number. The names can easily be found with the windows command `dir /X`. As an example, the file named `upload_2c59709f_b0df_400b_ad3b_668e1f02e340_00000000.tmp` will have the shortname `UPLOAD~1.tmp`. The following files uploaded would have the shortname `UPLOAD~i.tmp`, with `i = 2,3,4`. Afterward the names become `UP{4 alphanumeric hashes}~1.tmp`, because of how the _short file name_ is implemented by Windows.

Now, arbitrary files can be uploaded in the `{Base Dir}/server/tmp/` directory and the name of the files are guessable. The next step is to upload an XSLT file and trigger it with a query:
  
  
  http://localhost:8983/solr/new_core/select?q=:&wt=xslt&tr=../../../../../tmp/UPLOAD~1.tmp&rows=1000
  
  
  Error 500: [Redacted] Caused by: java.io.IOException: File C:\Solr\solr-8.3.1\server\tmp\UPLOAD~1.tmp is outside resource loader dir C:\Solr\solr-8.3.1\server\solr\configsets_default\conf; set -Dsolr.allow.unsafe.resourceloading=true to allow unsafe loading

Even if our path traversal is successful, an additional security check is present. The XSLT file must be in the same folder as the core to be considered as `safe` to allow execution.

### Bring the Core to our file upload

The idea is straightforward. Arbitrary files can be uploaded in the `/tmp` directory. A _core_ can be created at an arbitrary path if the configuration files are present. Thus, the temporary directory can be leveraged to create a _core_. Then, if XSLT files exist in the temporary directory, they would be considered as `safe` by this _core_.

To create a core, the application needs at least 2 files: `solrconfig.xml` and `schema.xml`. In a real _core_ creation, the files reference other files to load such as language packs. To reduce the complexity, the 2 files were trimmed to a bare minimum.

![](/wp-content/uploads/2020/11/NewCoreTmp-1-1024x634.png)_Creation of the core using the 2 uploaded file in the tmp directory_

### RCE from an XSLT file

After the creation of a core in the `/tmp` directory, an XSLT file can be uploaded and safely triggered. Gaining arbitrary command execution is pretty trivial using the payloads available in [PayloadAllTheThings](https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/XSLT%20Injection/README.md#remote-code-execution-with-java).
  
  
  <xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
  xmlns:fo="http://www.w3.org/1999/XSL/Format" 
  xmlns:dyn="http://exslt.org/dynamic" 
  extension-element-prefixes="dyn" xmlns:rt="http://xml.apache.org/xalan/java/java.lang.Runtime" xmlns:sys="http://xml.apache.org/xalan/java/java.lang.System" xmlns:ob="http://xml.apache.org/xalan/java/java.lang.Object">
  <xsl:output media-type="text/xml" method="xml" indent="yes"/><xsl:template match='/'>
  <add>
  <xsl:variable name="rtobject" select="rt:getRuntime()"/>
  <xsl:variable name="process" select="rt:exec($rtobject,'calc.exe')"/>
  <xsl:variable name="processString" select="ob:toString($process)"/>
  <xsl:value-of select="$processString"/>
  </add>
  </xsl:template>
  [REDACTED]
  </xsl:stylesheet>
  <!-- comments used to make the file bigger than 20kb AAAAAAAAAAAAAA[REDACTED]AAAAAAAAA-->

It will run the famous _calc.exe_. For the last time the XSLT is triggered from the following URL:
  
  
  http://localhost:8983/solr/new_core_tmp/select?q=*:*&wt=xslt&tr=../UPLOAD~1.tmp

[![](/wp-content/uploads/2023/02/poc-1.gif)](/wp-content/uploads/2023/02/poc-1.gif)

### Note on the temporary files

Even if the short name of the uploaded files have to be guessed, this exploit is quite reliable because:  
1\. The temporary files are deleted every hour in the `/tmp` directory.  
2\. When the malicious core is created in the `/tmp` directory, it automatically removes all the other `.tmp` files. This is a nice feature for this exploit, because uploading the XSLT afterwards would mean that it is pretty sure to be reachable through the _Windows short name_ `UPLOAD~1.tmp`.

### Overview

From an exposed Solr interface it was possible to gain RCE on the server. This weakness exists until version 8.3.2 on Windows. In the newer versions, the following restrictions were implemented:

  * The `.tmp` files are not stored as plain files anymore
  * A new core cannot be created in the /tmp folder
  * Most of the path traversals are either blocked or whitelisted 

For linux, if there is a way to leak the UUID, this vulnerability won’t need the Windows short file name mechanism, thus RCE on a Unix server would be possible.

### Current exploitation of Solr

  * Solr had many vulnerabilities in the past that allow to find at least one reliable RCE. A good resource for their PoCs are listed in this repository: (CVEs before 2020) <https://github.com/veracode-research/solr-injection>
  * An arbitrary file upload vulnerability was found for the Solr version **before 8.8.1**. Uploading an XSLT with this could lead to a similar RCE. ­¤æē­¤śÄ­¤æē
  * The famous _log4shell_ exists in all the version of Solr **before 8.11.1**. So it’s far more reliable for quick wins.
  * Google Dork: _intitle:”Solr Admin” “Solr Query Syntax”_

### Disclosure timeline

_13.10.2020:_ Vulnerability disclosed to Apache.  
_20.10.2020:_ Apache responded that it is not viewed as a security vulnerability because, parts of the exploit uses the **Admin API**.  
_21.10.2020:_ Asked and got permission to write a blog post about it.  
2020-2023: The blog post caught covid and took a while to recover  
23.02.2023: Blog post released

### Note on the admin API

As far as I know, a basic installation of Solr does not use any type of security such as a password protection or account management. Improving the security is done manually by the user through the installation of additional plugins or a firewall configuration. Relying on the average user to secure the application is very risky, especially if the administrator interface is visible (and vulnerable) by default to everyone ┬»\\_(Ńāä)_/┬».

### PoC

The proof of concept is available here: <https://github.com/scrt/Apache-Solr-8.3.1-RCE>

[![](/wp-content/uploads/2023/02/fullPoc-2.gif)](/wp-content/uploads/2023/02/fullPoc-2.gif)

Posted on [May 1, 2023May 1, 2023](/2023/05/01/solr-rce-from-exposed-administration-interface/)Author [Nicolas Brunner](/author/nbr/)Categories [Exploit](/category/exploit/), [Pentest](/category/pentest/)Tags [RCE](/tag/rce/), [Solr](/tag/solr/)
