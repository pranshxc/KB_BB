---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-11-15_varonis-threat-labs-discovers-sqli-and-access-flaws-in-zendesk.md
original_filename: 2022-11-15_varonis-threat-labs-discovers-sqli-and-access-flaws-in-zendesk.md
title: Varonis Threat Labs Discovers SQLi and Access Flaws in Zendesk
category: documents
detected_topics:
- sqli
- api-security
- access-control
- command-injection
- graphql
- business-logic
tags:
- imported
- documents
- sqli
- api-security
- access-control
- command-injection
- graphql
- business-logic
language: en
raw_sha256: 2d32bf60905c3f07938f9eac579598965eb241dfa4716b3e8f66bee8dcd4e854
text_sha256: 79c4ff7891f426b24a25aa5a2f5a1256212ed9bca52905dbe4fe557a13d81c0c
ingested_at: '2026-06-28T07:32:15Z'
sensitivity: unknown
redactions_applied: false
---

# Varonis Threat Labs Discovers SQLi and Access Flaws in Zendesk

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-11-15_varonis-threat-labs-discovers-sqli-and-access-flaws-in-zendesk.md
- Source Type: markdown
- Detected Topics: sqli, api-security, access-control, command-injection, graphql, business-logic
- Ingested At: 2026-06-28T07:32:15Z
- Redactions Applied: False
- Raw SHA256: `2d32bf60905c3f07938f9eac579598965eb241dfa4716b3e8f66bee8dcd4e854`
- Text SHA256: `79c4ff7891f426b24a25aa5a2f5a1256212ed9bca52905dbe4fe557a13d81c0c`


## Content

---
title: "Varonis Threat Labs Discovers SQLi and Access Flaws in Zendesk"
url: "https://www.varonis.com/blog/zendesk-sql-injection-and-access-flaws"
final_url: "https://www.varonis.com/blog/zendesk-sql-injection-and-access-flaws"
authors: ["Tal Peleg"]
programs: ["Zendesk"]
bugs: ["SQL injection", "Logic flaw"]
publication_date: "2022-11-15"
added_date: "2022-11-17"
source: "pentester.land/writeups.json"
original_index: 1911
---

Varonis Threat Labs found a SQL injection vulnerability and a logical access flaw in Zendesk Explore, the reporting and analytics service in the popular customer service solution, [Zendesk](https://www.zendesk.com).

There is no evidence that any Zendesk Explore customer accounts were exploited, and Zendesk started working on a fix the same day it was reported. The company fixed multiple bugs in less than one workweek with zero customer action required.

Before it was patched, the flaw would have allowed threat actors to access conversations, email addresses, tickets, comments, and other information from Zendesk accounts with Explore enabled.

"Zendesk started working on a fix the same day it was reported. The company fixed multiple bugs in less than one workweek with zero customer action required."

To exploit the vulnerability, an attacker would first register for the ticketing service of its victim's Zendesk account as a new external user. Registration is enabled by default because many Zendesk customers rely on end-users submitting support tickets directly via the web. Zendesk Explore is not enabled by default but is heavily advertised as a requirement for the analytic insights page.

## Execute, nested encodings, and XMLs, oh my!

Zendesk uses multiple [GraphQL APIs](https://graphql.org/) in its products, especially in the administration console. Because GraphQL is a relatively new API format, we started our research there. We found one particularly interesting object type in Zendesk Explore named QueryTemplate.

The querySchema field stood out because it contains a Base64-encoded XML document named Query inside of a JSON object, and many of the attributes in the XML were Base64-encoded JSON objects themselves. Translation? That's a Base64-encoded JSON object, inside a Base64-encoded XML document, inside a JSON object. Phew!

![image1-1](https://www.varonis.com/hubfs/image1-1.png)

Multiple nested encodings always catch our attention because a large number of wrappers around data usually means that many different services (which were most likely created by separate developers or even teams) are used to process this data. More code usually means more potential locations for vulnerabilities.

For this reason, we dug deeper into Zendesk Explore using the admin user of our own lab account in Zendesk. When visualizing a report in Zendesk Explore, we found an API called execute-query. This API method accepts a JSON object with the Query XML, along with multiple other XML parameters, some of which are encoded in Base64.

## SQL injection

One of the fields passed to the API is extra_param3_value which includes a plain-text XML document, DesignSchema, not encoded in Base64. This document defines the relationship between an [AWS RDS](https://aws.amazon.com/rds/) (managed relational database) and the aforementioned Query XML document.

All the name attributes in this XML document, which define the tables and columns to be queried, were found to be vulnerable to a SQL injection attack. The challenge for our team was how to exploit the SQLi vulnerability to exfiltrate data.

![image2](https://www.varonis.com/hubfs/image2.png)

The XML parsing engine on the back end was willing to accept single-quoted attributes instead of the default double-quoted attributes, allowing us to escape the double-quotes in the table name.

Now we needed a way to write strings in the query without using single quotes or double quotes. Fortunately, PostgreSQL, the database used by Zendesk Explore, provides a convenient method for representing strings: [dollar-quoted string constants](https://www.postgresql.org/docs/current/sql-syntax-lexical.html). The characters “$$” can be used to define a string in lieu of the standard single quote character in an SQL statement.

Using this string representation method, we were able to extract the list of tables from Zendesk's RDS instance and continue to exfiltrate all the information stored in the database, including email addresses of users, leads, and deals from the CRM, live agent conversations, tickets, help center articles, and more.

![image3-1](https://www.varonis.com/hs-fs/hubfs/image3-1.png?width=630&height=693&name=image3-1.png)

## The logical access flaw

SQL injections are always interesting but being able to exfiltrate data as an admin is not very exciting. We were looking for a broader impact, so we decided to study how this execute-query API really worked.

The execute-query API method accepts a JSON payload containing a “content” object with “query,” “cubeModels,” and “datasources” properties.

![image4-1](https://www.varonis.com/hs-fs/hubfs/image4-1.png?width=1387&height=824&name=image4-1.png)

“query” contains a Query XML document with the columns, rows, slicers, measures, and explosions of the query, as well as the visualization configuration in JSON format. The document also contains a reference to the “cubeModels” property. “cubeModels” contains an XML document named “OLAPSchema” that defines the tables that can be queried in the selected data source.

The execute-query API did not perform several logical checks on requests:

  1. The integrity of documents was not checked, allowing our team to modify them in ways that exposed the inner workings of the system.
  2. “query,” “datasources,” and “cubeModels” IDs were not evaluated to see if they belonged to the current user.
  3. Finally, and most critically, the API endpoint did not verify that the caller had permission to access the database and execute queries. This meant that a newly created end-user could invoke this API, change the query, and steal data from any table in the target Zendesk account's RDS, no SQLi required.

## Summing it up

Varonis Threat Labs helped Zendesk solve a [SQLi vulnerability](https://www.varonis.com/blog/sql-injection-identification-and-prevention-part-1?hsLang=en) and an access control flaw in Zendesk Explore that would have allowed a threat actor to leak data from Zendesk customer accounts with Explore enabled. Zendesk quickly resolved the issue and there is no longer this flaw in Explore. No action is needed from current customers.

### What should I do now?

Below are three ways you can continue your journey to reduce data risk at your company:

1

[Schedule a demo with us](https://info.varonis.com/en/demo-request?hsLang=en "https://info.varonis.com/en/demo-request") to see Varonis in action. We'll personalize the session to your org's data security needs and answer any questions.

2

[See a sample of our Data Risk Assessment](https://www.varonis.com/hubfs/docs/DRA-sample.pdf?hsLang=en "https://info.varonis.com/hubfs/docs/DRA-sample.pdf?hsLang=en") and learn the risks that could be lingering in your environment. [Varonis' DRA](https://info.varonis.com/en/data-risk-assessment?hsLang=en "https://info.varonis.com/en/data-risk-assessment") is completely free and offers a clear path to automated remediation.

3

Follow us on[ LinkedIn](https://www.linkedin.com/company/varonis "https://www.linkedin.com/company/varonis"), [YouTube](https://www.youtube.com/channel/UCE9xUuH4lhIUDOFR1OHlNNg "https://www.youtube.com/channel/UCE9xUuH4lhIUDOFR1OHlNNg"), and [X (Twitter)](https://twitter.com/varonis "https://twitter.com/varonis") for bite-sized insights on all things data security, including DSPM, threat detection, AI security, and more.

![Tal Peleg](https://www.varonis.com/hubfs/tal-peleg.jpg)

Tal Peleg Tal Peleg is a senior security researcher at Varonis. Also known as TLP, Tal is a full-stack hacker with experience in malware analysis, Windows domains, web servers, and cloud. His research is currently focused on cloud applications and APIs.
