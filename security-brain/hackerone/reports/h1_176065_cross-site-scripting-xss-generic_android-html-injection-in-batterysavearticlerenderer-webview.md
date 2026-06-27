---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '176065'
original_report_id: '176065'
title: '[Android] HTML Injection in BatterySaveArticleRenderer WebView'
weakness: Cross-site Scripting (XSS) - Generic
team_handle: brave
created_at: '2016-10-16T00:14:18.358Z'
disclosed_at: '2018-10-22T19:51:14.435Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 41
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# [Android] HTML Injection in BatterySaveArticleRenderer WebView

## Metadata

- HackerOne Report ID: 176065
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: brave
- Disclosed At: 2018-10-22T19:51:14.435Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

## Summary:

HTML Injection in BatterySaveArticleRenderer WebView.

## Products affected: 

 * Android Brave Browser 1.9.56

## Steps To Reproduce:

 * Open https://blackfan.ru/brave or html

```html
<script>
location="https://www.google.com/search?q=</title><h1><marquee><s>Injection<!--"
</script>
```
* Wait for a full load
* Click on ArticleModeButton

## Supporting Material/References:

Vulnerable code:
```java
public class aot
...
// s7 == title
if(s7 != null)
{
  s4 = (new StringBuilder()).append(s5).append("<title>").append(s7).append("</title>").toString();
  s1 = (new StringBuilder()).append(s6).append("<p style=\"font-size:").append(s1).append(";line-height:120%;font-weight:bold;margin:").append(s3).append(" 0px 12px 0px\">").append(s7).append("</p>").toString();
...
// s8 == authorName
if(s8 != null)
  s1 = (new StringBuilder()).append("<span class=\"nowrap\"><b>").append(s8).append("</b>,</span> ").toString();
```

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
