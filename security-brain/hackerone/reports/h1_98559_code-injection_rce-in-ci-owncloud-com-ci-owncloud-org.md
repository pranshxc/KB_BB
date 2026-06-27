---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '98559'
original_report_id: '98559'
title: RCE in ci.owncloud.com / ci.owncloud.org
weakness: Code Injection
team_handle: owncloud
created_at: '2015-11-08T08:25:14.881Z'
disclosed_at: '2015-11-09T17:37:12.240Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 9
tags:
- hackerone
- code-injection
---

# RCE in ci.owncloud.com / ci.owncloud.org

## Metadata

- HackerOne Report ID: 98559
- Weakness: Code Injection
- Program: owncloud
- Disclosed At: 2015-11-09T17:37:12.240Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hi,

I know you are more interested in vulnerabilities found in ownCloud Server, but I do would like to inform you on a RCE that can be executed on ci.owncloud.[com/org]. 

**Vulnerability**
There is a 0day vulnerability in Jenkins that can be exploited in certain circumstances. The Jenkins instance on ci.owncloud.[com/org] is vulnerabile for this attack since it is configured to run on a public IP address and is not firewalled.

The vulnerability exists in the common library used by Java to (de)serialize data. Jenkins will deserialize and execute configuration data sent to a specific port it is listening on. More information on the vulnerability can be found in this [article](http://foxglovesecurity.com/2015/11/06/what-do-weblogic-websphere-jboss-jenkins-opennms-and-your-application-have-in-common-this-vulnerability/).

It was easy to find the Jenkins instance because its name is easy guessable (only later on I found out its also being linked to from your GitHub page).

**POC**
I used a payload to confirm the RCE which tells me ci.jenkins.org is running `Debian 7`. You can use this information as confirmation on the RCE.

I was also able to read the `/etc/passwd` file, but I'd rather not send the data it contains in this report.

**Mitigation**
- Shut down ci.owncloud.com for the time being
- Run ci.owncloud.com on a VPN instead of on a world-accessible public IP address
- Firewall the Jenkins instance

Regards, @tomdev

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
