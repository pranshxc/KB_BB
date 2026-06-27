---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '282748'
original_report_id: '282748'
title: Detecting Tor Browser UI Language
weakness: Privacy Violation
team_handle: torproject
created_at: '2017-10-25T08:11:59.728Z'
disclosed_at: '2019-05-21T08:48:31.664Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 64
tags:
- hackerone
- privacy-violation
---

# Detecting Tor Browser UI Language

## Metadata

- HackerOne Report ID: 282748
- Weakness: Privacy Violation
- Program: torproject
- Disclosed At: 2019-05-21T08:48:31.664Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Suppose that a user downloads a non-English version of Tor Browser from https://www.torproject.org/projects/torbrowser.html.en, there is a way to detect which UI language the user is using. I don't think you want websites to detect this info, because at the first time I launched non-English Tor Browser, there's a warning dialog asking if I want to send my UI language to websites in the "Accept-Language" header, which may violate my privacy. **This trick works even if I choose "Don't send my language" in that warning dialog**.

Steps to reproduce:
1. Download and install 简体字 (zh-CN) version (i.e. Simplified Chinese) of Tor Browser from https://www.torproject.org/projects/torbrowser.html.en.
2. In the Chinese Tor Browser, navigate to https://xiaoyinl.github.io/juyt75/ttude.html. The page should be able to tell you "Your browser UI language is: Simplified Chinese".
3. Launch an English Tor Browser, and navigate to https://xiaoyinl.github.io/juyt75/ttude.html. The page should be able to tell you "Your browser UI language is: English".

The trick is that when I specify a button <input type="submit"> without a "value" property, the default text of the button depends on the UI language. If the UI language is Chinese, its text is 提交查询; if the UI language is English, its text is "Submit Query". Thus, these two buttons will have different width. If its width equals the width of <input type="submit" value="Submit Query">, the UI language is English. If its width equals the width of <input type="submit" value="提交查询">, the UI language is Simplified Chinese.

To fix this, always use the button with default text in English.

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
