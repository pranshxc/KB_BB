---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-10-19_alternative-link.md
original_filename: 2022-10-19_alternative-link.md
title: Alternative link
category: documents
detected_topics:
- command-injection
- supply-chain
tags:
- imported
- documents
- command-injection
- supply-chain
language: en
raw_sha256: 2cc19e1d2bbddfda3db0e48165e2b98220545c103d7e2d049b49a1de9055b227
text_sha256: 58a8c802dcff4431f71f73059a883be1e7212bcc766af7932ca154fac22238a1
ingested_at: '2026-06-28T07:32:15Z'
sensitivity: unknown
redactions_applied: false
---

# Alternative link

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-10-19_alternative-link.md
- Source Type: markdown
- Detected Topics: command-injection, supply-chain
- Ingested At: 2026-06-28T07:32:15Z
- Redactions Applied: False
- Raw SHA256: `2cc19e1d2bbddfda3db0e48165e2b98220545c103d7e2d049b49a1de9055b227`
- Text SHA256: `58a8c802dcff4431f71f73059a883be1e7212bcc766af7932ca154fac22238a1`


## Content

---
title: "Alternative link"
page_title: "Potential Remote Code Execution Vulnerability Discovered In HSQLDB | by Code Intelligence | Medium"
url: "https://medium.com/@CI_Fuzz/potential-remote-code-execution-vulnerability-discovered-in-hsqldb-4a2dfa6275ee"
authors: ["Code Intelligence (@CI_Fuzz)"]
programs: ["HSQL Development Group (HSQLDB)"]
bugs: ["RCE", "Security code review"]
publication_date: "2022-10-19"
added_date: "2022-10-25"
source: "pentester.land/writeups.json"
original_index: 2014
scraped_via: "browseros"
---

# Alternative link

Potential Remote Code Execution Vulnerability Discovered In HSQLDB
Code Intelligence
Follow
2 min read
·
Oct 19, 2022

4

19.10.2022 — To improve our vulnerability detectors, we continuously test various open-source projects with Jazzer, running inside OSS-Fuzz. In this case, a test run yielded a severe finding with a potential remote code execution in a HSQLDB (CVE-2022–41853).

Press enter or click to view image in full size
RCE in HyperSQL database
Vulnerability Description

A potential remote code execution vulnerability was detected in java.sql.Statement and java.sql.PreparedStatement, in the parsing procedure for binary and text format data. By default, SQL statements can be used to call any static method from any Java class in the class path. HSQLDB (HyperSQL DataBase) allowed direct use of methods, e.g. call org.hsqldb.clazz.meth().

Affected versions: all versions <= 2.7.0

Impact of CVE-2022–41853

Critical — CVSS Base Score: 9.8

Applications that are using java.sql.Statement or java.sql.PreparedStatement in HSQLDB with untrusted input may be vulnerable to a remote code execution attack.

Get Code Intelligence’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

The library ranks 139th in the Maven repository and 2nd in embedded SQL databases. It is used by more than 3,113 Maven packages including LibreOffice, JBoss, Log4j, Hibernate, Spring-Boot (having thousands of usages with the potential of transitive risk), and various enterprise software solutions.

Remediation and Mitigation

If HSQLDB is used to process queries with user input, the hsqldb.method_class_names property must be defined with a list of class names or wildcards in case a static Java method is used as a target of an HSQLDB routine. Without a property definition, the use of Java static methods, except those in java.lang.Math, should not be allowed. Developers can prevent the issue by defining the system property. For example:

System.setProperty("hsqldb.method_class_names", "abc");

or

java -Dhsqldb.method_class_names="abc"

The issue is already fixed upstream and will be available in the next release. From version 2.7.1. the property hsqldb.method_class_names must be defined with a list of class names or wild cards if any Java static method is used as an HSQLDB routine target.

References

http://hsqldb.org/doc/2.0/guide/sqlroutines-chapt.html#src_jrt_access_control
https://bugs.chromium.org/p/oss-fuzz/issues/detail?id=50212#c7

About HSQLQDB

HSQLDB (HyperSQL DataBase) is a popular SQL relational database system written in Java. It is used for development, testing, and deployment of database applications. The library, which gets maintained by the HSQL Development Group, ranks 139th in the Maven repository and 2nd in embedded SQL databases, and has been downloaded over 100 million times.

Acknowledgments

We are grateful to the HSQLDB maintainers for quickly responding to the issue and providing a fix and a workaround for current versions.

Original source: https://www.code-intelligence.com/potential-remote-code-execution-in-hypersql
