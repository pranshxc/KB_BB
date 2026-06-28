---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-09-06_apache-superset-part-ii-rce-credential-harvesting-and-more.md
original_filename: 2023-09-06_apache-superset-part-ii-rce-credential-harvesting-and-more.md
title: 'Apache Superset Part II: RCE, Credential Harvesting and More'
category: documents
detected_topics:
- access-control
- command-injection
- supply-chain
- sso
- sqli
- automation-abuse
tags:
- imported
- documents
- access-control
- command-injection
- supply-chain
- sso
- sqli
- automation-abuse
language: en
raw_sha256: e963ed7cb77ccd6e64b5bd7d1a21e1ae7f1b4816b7ee1ead5d90162e7fbe9a3b
text_sha256: 0b13e039d60ec5f2be1b80d0bbeac083dedec354cfb19d5f524c64bf13a9c312
ingested_at: '2026-06-28T07:32:25Z'
sensitivity: unknown
redactions_applied: false
---

# Apache Superset Part II: RCE, Credential Harvesting and More

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-09-06_apache-superset-part-ii-rce-credential-harvesting-and-more.md
- Source Type: markdown
- Detected Topics: access-control, command-injection, supply-chain, sso, sqli, automation-abuse
- Ingested At: 2026-06-28T07:32:25Z
- Redactions Applied: False
- Raw SHA256: `e963ed7cb77ccd6e64b5bd7d1a21e1ae7f1b4816b7ee1ead5d90162e7fbe9a3b`
- Text SHA256: `0b13e039d60ec5f2be1b80d0bbeac083dedec354cfb19d5f524c64bf13a9c312`


## Content

---
title: "Apache Superset Part II: RCE, Credential Harvesting and More"
url: "https://www.horizon3.ai/apache-superset-part-ii-rce-credential-harvesting-and-more/"
authors: ["Naveen Sunkavally"]
programs: ["Apache Superset"]
bugs: ["RCE", "Insecure deserialization", "URL validation bypass", "Broken authorization", "Arbitrary file read", "Insufficiently Protected Credentials", "Default Flask Secret Key", "Hardcoded credentials"]
publication_date: "2023-09-06"
added_date: "2023-09-07"
source: "pentester.land/writeups.json"
original_index: 804
scraped_via: "browseros"
---

# Apache Superset Part II: RCE, Credential Harvesting and More

Apache Superset Part II: RCE, Credential Harvesting and More
Naveen Sunkavally
September 6, 2023
Attack Blogs, Disclosures

Apache Superset is a popular open source data exploration and visualization tool. In a previous post, we disclosed a vulnerability, CVE-2023-27524, affecting thousands of Superset servers on the Internet, that enables unauthorized attackers to gain admin access to these servers. We also alluded to methods that an attacker, logged in as an admin, could use to harvest credentials and execute remote code. We didn’t disclose these methods because they hadn’t been fixed yet at the time of that post.

In this post, we disclose all the issues we’ve reported to Superset, including two new high severity vulnerabilities, CVE-2023-39265 and CVE-2023-37941, that are fixed in the just released 2.1.1 version of Superset. We strongly recommend that all Superset users upgrade to this version.

Introduction

Apache Superset is written in Python and based on the Flask web framework. CVE-2023-27524 arises from an insecure default configuration of the Flask SECRET_KEY value. Knowing the value of the Flask SECRET_KEY, an attacker can forge session cookies and log in to Superset with admin privileges. More details are available in the first post.

This issue of the insecure default configuration was mostly fixed with the 2.1.0 release of Superset. If you’re a user of Superset, you can run a script available here to check if you’re vulnerable.

The rest of this post covers what an attacker can do once he/she has attained admin privileges, either from exploiting CVE-2023-27524, or by other means. In certain installs of Superset the admin account has the default credentials admin/admin.

Some of the attacks described here are also possible with a non-admin account. Superset has fine grained access control with multiple role types, and a user who happens to have the right permissions may be able to pull off certain attacks.

Getting Read/Write Access to the Metadata Database

Many of the attacks in this post start with first getting control of Superset’s metadata database, i.e. its configuration store. Superset by design allows privileged users to connect to arbitrary databases and execute arbitrary SQL queries against those databases using the powerful SQLLab interface. If Superset can be tricked into connecting to its own metadata database, an attacker can directly read or write application configuration through SQLLab. This leads to harvesting credentials and remote code execution, as we’ll describe later below.

SQLite Access via SQLAlchemy URI Bypass (CVE-2023-39265)

By default Superset uses SQLite as its metadata database, and the SQLite file is located on the Superset web server.

Attempting to connect to this SQLite database through the Superset UI doesn’t work, as Superset has safeguards in place to prevent sqlite connections.

We discovered, however, that it’s possible to bypass this safeguard by putting in the full SQLAlchemy URI containing both the dialect and driver name, e.g. sqlite+pysqlite:////app/superset_home/superset.db

After connecting to the metadata store, an attacker can then enable it for use in SQLLab and turn on write/DML statements.

This issue, tracked as  CVE-2023-39265, affects Superset versions <= 2.1.0. It was fixed in the 2.1.1 release by blocking any SQLAlchemy URIs starting with sqlite instead of just blocking the sqlite:// syntax.

SQLite Access via Import Database (also CVE-2023-39265)

Superset supports configuring databases by importing database connection information from a file. We discovered that this feature didn’t enforce any restrictions for connecting to SQLite stores. An attacker can gain control of a SQLite metadata database by creating a crafted database import zip file and importing it. This issue is also fixed in the 2.1.1 release and tracked under the same CVE ID as the previous issue, CVE-2023-39265.

The crafted database import zip file would contain a YAML file similar to below:

MySQL Arbitrary File Read Vulnerability

For production installs, Superset recommends using a more robust metadata database like Postgres running on a dedicated server instead of SQLite. For Superset versions <= 2.1.0, it’s possible to leverage a well-known “misfeature” in MySQL to get credentials to the metadata database, and then connect to the metadata database through the UI. To do this, an attacker would:

Setup a rogue attacker-controlled MySQL server with the local_infile setting enabled
Use the Superset UI to connect to the attacker-controlled MySQL server. (It’s not required to set the local_infile option explicitly on the client as it’s on by default in the python SQLAlchemy driver.)
Use the SQLLab interface to run a LOAD DATA LOCAL INFILE command to load the content of arbitrary files on the Superset server into the attacker-controlled MySQL server

Credentials to the metadata database are available in the environment (/proc/self/environ) or in the superset_config.py or config.py files. Here’s an example of reading credentials out of /proc/self/environ, using the docker-compose setup with Superset 2.1.0:

This MySQL misfeature has bitten many applications in the past. The Superset team chose not to track this as a vulnerability in their product, but it’s something users should be aware of. This issue is fixed in Superset 2.1.1.

Load Examples

Superset offers users the ability to load example data into the application using the superset load_examples CLI command. The examples data is unfortunately loaded into the metadata database, and the connection to the examples/metadata database is populated in the UI. This enables any privileged user to potentially explore and modify data in the metadata database.

This issue affects Superset versions <= 2.1.1. It’s fixed with this pull request, on the bleeding edge release as of this writing.

Default Metadata Database Credentials

Certain installations of Superset, such as docker-compose, use default credentials to access the metadata database. Knowing the defaults, an attacker can trivially connect to the metadata database and gain control over it.

Harvesting Credentials from the Metadata Database

Once an attacker has gained control of the metadata database, it’s straightforward to harvest credentials from it using SQLLab. An attacker would likely target Superset user password hashes and the credentials for accessing any configured databases.

User password hashes are stored in the ab_user table:

Database connection info is stored in the dbs table..

Passwords in this table are encrypted using the sqlalchemy-utils library, which by default uses AES128, and the encryption key is the SHA2 hash of the SECRET_KEY. Decryption is straightforward:

If the SECRET_KEY is not known ahead of time, an attacker can exploit the MySQL arbitrary file read vulnerability described above to read it out of the environment or config files.

Remote Code Execution on the Superset Server (CVE-2023-37941)

Superset versions from 1.5 to 2.1.0 use python’s pickle package to store certain configuration data. An attacker with write access to the metadata database can insert an arbitrary pickle payload into the store, and then trigger deserialization of it, leading to remote code execution.

Here’s an example exploiting dashboard permalink metadata, which Superset was storing using pickle:

First, an attacker would generate a dashboard permalink from the UI:

Next, an attacker generates a malicious pickle payload to run an arbitrary payload (e.g. a python reverse shell):

Then, an attacker uses SQLLab to write a malicious pickle payload into the key_value table of the metadata database:

The example above is for the default SQLite-based metadata database. The syntax is slightly different for a Postgres metadata database:

Finally, an attacker can browse to the permalink to trigger loading the malicious pickle, leading to remote code execution:

This issue, tracked as CVE-2023-37941, was fixed in Superset 2.1.1 by replacing pickle with JSON for storing configuration.

Other Findings
Remote Code Execution on a Database Server

In addition to RCE on the Superset web server, it’s possible to get RCE on any connected database, if the database is configured with a privileged user. There are a number of well-known techniques for doing this. Here’s an example of getting remote code execution on the Postgres server that is set up by default with the docker-compose install, using a perl reverse shell.

Database Credentials Leak (CVE-2023-30776)

For Superset versions < 2.1.0, we found that the credentials for databases configured in Superset are leaked in clear text when querying the Superset /api/v1/database API as a privileged user. This vulnerability (CVE-2023-30776) was fixed in Superset 2.1.0:

Remote Code Execution on Older Superset Servers

The pickle RCE vector we disclosed above affects Superset versions 1.5 to 2.1.0. We believe RCE is likely possible against older Superset servers. One option that looks promising but we didn’t fully explore is RCE via SQLite using the method described here.

Remediation Guidance

We recommend that users of Superset:

Double-check all your defaults: the Flask SECRET_KEY, Superset admin credentials, metadata database credentials, etc. Even if you’re on the latest version of Superset, you still may be using a default SECRET_KEY! You can run a script available here to check if you’re vulnerable to CVE-2023-27524.
Update to the latest Superset version 2.1.1.
Double-check that you’re not using any “root” level credentials to connect Superset to databases.
Remove the examples database.
If you’re exposing Superset to the Internet, seriously think about whether it’s truly required to do so. Consider putting it behind a VPN.
Remediation Status for CVE-2023-27524

In the first blog post, we reported that 67% of Superset installs (2124 out of 3176 instances found) were found to be using a default Flask SECRET_KEY.

We ran the numbers again, this time broadening our search to cover more Superset servers and also attempting to not only check for the default Superset SECRET_KEYs but other easily guessable SECRET_KEYs that a user may have configured. The results are below:

The new results show that ~54% of Superset installs (2076 out of 3842 servers found) are using a default SECRET_KEY. This is a modest reduction from the 67% we reported at the end of April.

Notably, a couple of Superset SECRET_KEYs are still defaulted depending on the type of install, even with the current latest release. thisISaSECRET_1234 has always been hard-coded as part of the helm-based install. TEST_NON_DEV_SECRET is hard-coded for the docker-compose-based install and was recently added with the 2.1 release. This means the ~345 installs using the TEST_NON_DEV_SECRET key were very likely installed within the last 4-5 months, and some of these users may have thought they were getting a Superset version that wasn’t vulnerable to CVE-2023-27524 but in fact still is.

Additionally, we found another ~2% of installs (72) using an easily guessable user provided SECRET_KEY. These are SECRET_KEY values like superset, SUPERSET_SECRET_KEY, 1234567890, admin, changeme, thisisasecretkey, your_secret_key_here, etc.

Indicators of Compromise

If you’re a user of Superset and think your Superset server may have been compromised, you can check the Superset action log and web server logs for suspicious activity. Calls to the DatabaseRestApi, DashboardPermalinkRestApi, and SqlLabRestApi should be scrutinized, as well as any actions for which there is no associated Superset user. The addition of any databases or modification of database configuration should be considered suspicious. The SQLLab query history interface can be used to view any prior queries that were executed against a database. Of course, an attacker who has compromised the Superset server can tamper with all logs to cover their tracks.

Conclusion

In this post, we’ve disclosed a number of vulnerabilities affecting Apache Superset that, in conjunction with the previously disclosed CVE-2023-27524, effectively lead to unauthenticated remote code execution, credential harvesting, and data compromise. Almost all of the issues we’ve disclosed are fixed in the Superset 2.1.1 release.

There are a few issues to be aware of:

As of this writing, there are still a few default settings to be aware in the Superset helm template and docker-compose setup. The Superset team is aware of these defaults and planning to remove them. The latest data we gathered supports removing these defaults and providing a complete fix for CVE-2023-27524.
The user is responsible for setting the Flask SECRET_KEY, which invariably leads to some users setting weak keys, as proven by the latest data we gathered. We recommend the Superset team automatically generate the SECRET_KEY and take this completely out of the users’ hands.
At the root of many of the vulnerabilities in this post is the fact that the Superset web interface permits users to connect to the metadata database. We recommend the Superset team add a security restriction to prevent users from ever connecting to the metadata database.

On the whole, we believe that Superset is significantly more secure now than it was at the start of the year. We’re also heartened to see a check for default SECRET_KEYs recently added into CodeQL, which will help “shift left” the discovery of these kind of issues in the future.

Timeline
Oct. 11, 2021: Initial communication from Horizon3 to Apache Security team about default SECRET_KEY
Oct. 12, 2021: Superset team says they will look into issue
Jan. 11, 2022: Superset team changes default SECRET_KEY and adds warning to logs with this Git commit
Feb. 9, 2023: Email to Apache Security team from Horizon3 about new data related to insecure default configuration. Started notifying certain organizations.
Feb. 13, 2023: Confirmation of email received by Apache Security team
Feb. 22, 2023: Preliminary blog post sent by Horizon3 to Apache Security team about insecure default configuration, MySQL arbitrary file read vulnerability, and database password leak.
Feb. 24, 2023: Superset team confirms code change will be made to address default SECRET_KEY
Mar. 1, 2023: Superset pull request merged with code change to address default SECRET_KEY
Apr. 5, 2023: Superset 2.1.0 release
Apr. 12, 2023: Superset team says the MySQL arbitrary file read issue is fixed
Apr. 13, 2023: Superset team confirms database password leak issue that was fixed in 2.1.0. Assigns CVE-2023-30776.
Apr. 14, 2023: Horizon3 reports the MySQL arbitrary file read issue is not fully fixed.
Apr. 19, 2023: Superset team updates that new fix has been made for MySQL arbitrary file read issue.
Apr. 21, 2023: Horizon3 informs Superset that RCE is possible via pickle deserialization.
Apr. 22, 2023: Horizon3 informs Superset about SQLite SQLAlchemy URI bypass to connect to SQLite metadata store.
Apr. 24, 2023: CVE-2023-27524 disclosed
Apr. 24, 2023: Superset confirms RCE and SQLite SQLAlchemy URI bypass
Apr. 25, 2023: Horizon3 releases first blog post on CVE-2023-27524
June 6, 2023: Superset confirms pickle has been replaced with json and the SQLite SQLAlchemy URI bypass has been fixed
July 14, 2023: Horizon3 tests 2.1.1rc2 build and raises new issue related to database import with a SQLite URI.
July 14, 2023: Superset confirms database import issue
July 26, 2023: Superset confirms creation of new CVEs and fix for database import issue
Aug. 26, 2023:: Horizon3 sends preview of this blog post to Superset
Aug. 29, 2023: Superset 2.1.1 released
Sept. 6, 2023: This post
References
CVE-2023-27524: Insecure Default Configuration in Apache Superset Leads to Remote Code Execution
Horizon3 Vuln Check/Exploit Script for CVE-2023-27524
CVE-2023-27524
Apache Superset on GitHub
Apache Superset 2.1.1 Release
CVE-2023-39265
CVE-2023-37941
How can NodeZero help you?
Let our experts walk you through a demonstration of NodeZero®, so you can see how to put it to work for your organization.
Get a Demo
Share:
