---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '73257'
original_report_id: '73257'
title: PHP yaml_parse/yaml_parse_file/yaml_parse_url Unsafe Deserialization
team_handle: ibb
created_at: '2015-05-10T00:00:00.000Z'
disclosed_at: '2015-05-18T00:00:00.000Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 1
asset_identifier: PHP
asset_type: OTHER
max_severity: none
tags:
- hackerone
---

# PHP yaml_parse/yaml_parse_file/yaml_parse_url Unsafe Deserialization

## Metadata

- HackerOne Report ID: 73257
- Weakness: 
- Program: ibb
- Disclosed At: 2015-05-18T00:00:00.000Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

https://bugs.php.net/bug.php?id=69617

Description:
------------
The PHP unserialize() function is considered unsafe due to its behavior regarding class instantiation; in cases where serialized data is attacker controlled, it can be tampered with, allowing for the instantiation of arbitrary PHP classes and thus code execution via destructor.

Inversely, as per the documentation, the yaml_parse*() functions carry no such risk. In fact, among the YAML functions is yaml_parse_url, which retrieves and parses a remote YAML file. Deserialization of built-in YAML types appears safe, as the serializer utilizes arrays and scalar types, prohibiting control of instantiation. However, this limitation can be overcome with the largely undocumented !php/object extension type, which in turn invokes unserialize(), effectively making the yaml_parse* functions just as dangerous. An example follows:

```
<?php 
class A {
    function __destruct() {
       echo 'destructor invoked';
    }
}

yaml_parse('x: !php/object O:1:"A":0:{}');
?>
```

As mentioned previously, the yaml_parse_url function, which encourages the retrieval of YAML from remote endpoints, exhibits the same behavior:

```
<?php 
class A {
    function __destruct() {
       echo 'destructor invoked';
    }
}

yaml_parse_url('http://autosectools.com/yaml.txt');
?>
```

To mitigate this, it is recommended that the YAML serializer handle the !php/object type in a safe manner, such as prohibiting the deserialization of types that have destructors defined. If this is not possible, it is recommended that yaml_parse_url be removed and the documentation for the remaining yaml_* functions be updated with warnings akin to that of unserialize().

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
