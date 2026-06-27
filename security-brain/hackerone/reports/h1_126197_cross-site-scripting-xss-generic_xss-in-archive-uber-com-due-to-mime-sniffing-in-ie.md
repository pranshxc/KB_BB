---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '126197'
original_report_id: '126197'
title: XSS In archive.uber.com Due to Mime Sniffing in IE
weakness: Cross-site Scripting (XSS) - Generic
team_handle: uber
created_at: '2016-03-26T17:00:44.769Z'
disclosed_at: '2016-04-06T21:27:51.396Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 1
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# XSS In archive.uber.com Due to Mime Sniffing in IE

## Metadata

- HackerOne Report ID: 126197
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: uber
- Disclosed At: 2016-04-06T21:27:51.396Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

```archive.uber.com``` hosts a mirror of pypi at ```archive.uber.com/pypi/simple/```. It mirrors all of the ```.tar.gz``` that are uploaded to pypi. The MIME type of all the ```.tar.gz``` files is ```application/octet-stream```. Since the MIME type is not specified, browsers will automatically try to determine the type of the file. Chrome and Firefox both do so by looking the first few bytes of the file. Internet explorer scans the first 256 bytes of the file for ```html``` and if it finds ```html``` it will interpret the file as HTML. So by creating a ```.tar.gz``` that contains ```<html><script>alert(0)</script></html>``` one can inject javascript into the page. 

By default pypi doesn't allow you to create the ```.tar.gz``` manually (instead it creates it and uploads it with the same command). This can be bypassed by first building the ```.tar.gz``` by doing ```python setup.py sdist``` to build the ```.tar.gz``` before uploading it with an external program. After we create the ```.tar.gz``` we need to modify it so that it contains our inject HTML. Thankfully pypi doesn't validate a ```.tar.gz``` to check whether it is valid, so we can simply edit the ```.tar.gz``` and blindly insert the injected HTML. ```nano``` works just fine for this. Then we need to upload the modified/malicious ```.tar.gz```. In order to upload our modified ```.tar.gz``` we use twine (```pip install twine```) and run ```twine upload dist/evil.tar.gz```. 

I have done all of the above and uploaded it here: ```https://pypi.python.org/packages/source/I/IgnoreMe_mime/IgnoreMe_mime-1.0.1.tar.gz#md5=6a9aa8e15f726b161680fbb854281775```. Note that if you open that link in internet explorer you will get an ```alert(0)``` box. 

So far this has not been mirrored to ```archive.uber.com``` but as far as I can tell it is only a matter of time until it is pulled into that mirror. Once it is pulled into ```archive.uber.com``` it will work identically (since both pypi and uber fail to set a MIME type for these files). 

On a sidenote, while researching this vulnerability I discovered that pypi is also vulnerable (hence why the above link works). I am also reporting this to their security team. 

In order to patch this you need to either correctly specify the MIME type of the ```.tar.gz``` files or disable content sniffing. 

Thanks,
David Dworken

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
