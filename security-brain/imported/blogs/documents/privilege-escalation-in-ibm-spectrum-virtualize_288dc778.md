---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-08-15_privilege-escalation-in-ibm-spectrum-virtualize.md
original_filename: 2023-08-15_privilege-escalation-in-ibm-spectrum-virtualize.md
title: Privilege Escalation In Ibm Spectrum Virtualize
category: documents
detected_topics:
- access-control
- command-injection
- otp
- automation-abuse
- csrf
- information-disclosure
tags:
- imported
- documents
- access-control
- command-injection
- otp
- automation-abuse
- csrf
- information-disclosure
language: en
raw_sha256: 288dc778f5a44be85d67406cc020d6b3a9d26f152fc24b8d4c6ed7fb0a81963c
text_sha256: cc863c4fc665faff8b17088e51522b53cf8a129c1dce8654092fa31e27494c3e
ingested_at: '2026-06-28T07:32:25Z'
sensitivity: unknown
redactions_applied: false
---

# Privilege Escalation In Ibm Spectrum Virtualize

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-08-15_privilege-escalation-in-ibm-spectrum-virtualize.md
- Source Type: markdown
- Detected Topics: access-control, command-injection, otp, automation-abuse, csrf, information-disclosure
- Ingested At: 2026-06-28T07:32:25Z
- Redactions Applied: False
- Raw SHA256: `288dc778f5a44be85d67406cc020d6b3a9d26f152fc24b8d4c6ed7fb0a81963c`
- Text SHA256: `cc863c4fc665faff8b17088e51522b53cf8a129c1dce8654092fa31e27494c3e`


## Content

---
title: "Privilege Escalation In Ibm Spectrum Virtualize"
page_title: "Privilege Escalation in IBM Spectrum Virtualize – Certitude Blog"
url: "https://certitude.consulting/blog/en/privilege-escalation-in-ibm-spectrum-virtualize/"
final_url: "https://certitude.consulting/blog/en/privilege-escalation-in-ibm-spectrum-virtualize/"
authors: ["Wolfgang Ettlinger"]
programs: ["IBM"]
bugs: ["Privilege escalation", "Information disclosure"]
publication_date: "2023-08-15"
added_date: "2023-08-21"
source: "pentester.land/writeups.json"
original_index: 853
---

# Privilege Escalation in IBM Spectrum Virtualize

Written by [Wolfgang Ettlinger](https://certitude.consulting/blog/en/author/wet/) on [17.08.202317.08.2023](https://certitude.consulting/blog/en/privilege-escalation-in-ibm-spectrum-virtualize/)

**During a very short security test, Cert itude identified two vulnerabilities in the firmware of IBM Spectrum Virtualize, a storage solution by IBM. One of these vulnerabilities allows a low-privileged user of the administrative interface to gain code execution.**

## Privilege Escalation (CVE-2022-43873)

The administrative web interface utilizes an RPC protocol between the frontend web application and the backend. This protocol allows the browser application to call Java methods on the backend. However, there is no restriction on the callable Java methods. Thus, an authenticated user can call any `public static` Java methods e.g. defined by the JRE or any software library in the classpath.

As a result, many methods can be called that are not intended to be called in this scenario. Thus, low-privileged users can access functionality that allows code execution.

The following snippet shows a legitimate request issued by the frontend to the backend. This causes the backend to call the method `com.ibm.svc.gui.logic.ConfigRPC#getUpdateStatus()`. 
  
  
  POST /RPCAdapter?[CSRF Token Parameter] HTTP/1.1
  Host: [...]
  Cookie: [...]
  
  {
  "clazz": "com.ibm.evo.rpc.RPCRequest",
  "methodClazz": "com.ibm.svc.gui.logic.ConfigRPC",
  "methodName": "getUpdateStatus",
  "methodArgs": []
  }

The following snippet shows that e.g. the method `java.lang.System.load(String)` can be called with the parameter `/tmp/libtakeover.so`. This loads the shared library `libtakeover.so` into the Java process:
  
  
  POST /RPCAdapter?[CSRF Token Parameter] HTTP/1.1
  Host: [...]
  Cookie: [...]
  
  {
  "clazz": "com.ibm.evo.rpc.RPCRequest",
  "methodClazz": "java.lang.System",
  "methodName": "load",
  "methodArgs":[
  "/tmp/libtakeover.so"
  ]
  }

A low-privileged attacker could transfer a malicious shared library to `/tmp/libtakeover.so` using SCP. After executing the request above, the application server loads this library. An attacker can e.g. gain code execution by declaring a function that is to be called upon loading of the shared library (e.g. ld parameter `-init`).

## Passwords in Log Files (CVE-2022-43870)

The parameters `authpassphrase` and `privpassphrase` to the `mksnmpserver` command are not masked in the CLI logfile `/var/log/cli_audit`. As this logfile is accessible to all system users (e.g. via SCP), an attacker could retrieve the SNMPv3 authentication and privacy passwords configured.

## Resolution

IBM has issued updates addressing both issues. Additional information can be retrieved from the security bulletins:

  * <https://www.ibm.com/support/pages/node/6858047>
  * <https://www.ibm.com/support/pages/node/6858045>

## References

<https://certitude.consulting/advisories/CSA_2023_001_IBM_Spectrum_Virtualize_Multiple_Vulnerabilities.md.txt>
