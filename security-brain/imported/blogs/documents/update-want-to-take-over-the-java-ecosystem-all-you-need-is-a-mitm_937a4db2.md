---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-01-08_update-want-to-take-over-the-java-ecosystem-all-you-need-is-a-mitm.md
original_filename: 2020-01-08_update-want-to-take-over-the-java-ecosystem-all-you-need-is-a-mitm.md
title: 'Update: Want to take over the Java ecosystem? All you need is a MITM!'
category: documents
detected_topics:
- command-injection
- automation-abuse
- supply-chain
tags:
- imported
- documents
- command-injection
- automation-abuse
- supply-chain
language: en
raw_sha256: 937a4db2c9b714a0c1c3f6913ab73cb1e8d6927a98451cfa7898b41b55e87ce0
text_sha256: 01fd4564d66c312658dffe9a6305cfbcccad2bbc1966493e5b8a93478df1dcec
ingested_at: '2026-06-28T07:32:01Z'
sensitivity: unknown
redactions_applied: false
---

# Update: Want to take over the Java ecosystem? All you need is a MITM!

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-01-08_update-want-to-take-over-the-java-ecosystem-all-you-need-is-a-mitm.md
- Source Type: markdown
- Detected Topics: command-injection, automation-abuse, supply-chain
- Ingested At: 2026-06-28T07:32:01Z
- Redactions Applied: False
- Raw SHA256: `937a4db2c9b714a0c1c3f6913ab73cb1e8d6927a98451cfa7898b41b55e87ce0`
- Text SHA256: `01fd4564d66c312658dffe9a6305cfbcccad2bbc1966493e5b8a93478df1dcec`


## Content

---
title: "Update: Want to take over the Java ecosystem? All you need is a MITM!"
url: "https://medium.com/@jonathan.leitschuh/update-want-to-take-over-the-java-ecosystem-all-you-need-is-a-mitm-d069d253fe23"
authors: ["Jonathan Leitschuh (@jlleitschuh)"]
programs: ["Github"]
bugs: ["MiTM", "Insecure communications"]
bounty: "2,300"
publication_date: "2020-01-08"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4839
scraped_via: "browseros"
---

# Update: Want to take over the Java ecosystem? All you need is a MITM!

Update: Want to take over the Java ecosystem? All you need is a MITM!
January 13th-15th, 2020 will break over 21% of the industry’s Java build infrastructure. Six months since my initial article disclosing this industry-wide vulnerability, where are we now and what does the future hold?
Jonathan Leitschuh
Follow
5 min read
·
Jan 8, 2020

82

On June 10th, 2019 I publicly disclosed an industry-wide vulnerability impacting the Java ecosystem in an article titled ‘Want to take over the Java ecosystem? All you need is a MITM!’ In that article, I detailed how many of the most popular JVM based libraries were resolving their dependencies via their build tool over HTTP instead of HTTPS.

As a part of this research, I reached out to the security teams of several of the Java ecosystem’s most used artifact servers, and on January 15th, 2020 many of these artifact servers will drop support for HTTP in favor of only supporting HTTPS. It’s important to remember that as of June 2019, 25% of Maven Central downloads were still using HTTP. As of December 12th, 2019 21% of Sonatype Maven Central downloads are still using HTTP.

21% of Sonatype Maven Central downloads are still using HTTP

It’s important to stress that this breakage will force a very healthy and important shift in the security of the Java ecosystem’s supply chain.

Artifact Server Host Announcements

Listed below are the artifact servers I’ve reached out to and their current responses.

Maven Central — Sonatype

Maven Central will drop support for HTTP on January 15th, 2020.
You can read their full announcement here.

JCenter — JFrog

JCenter will drop support for HTTP on January 13th, 2020.
You can read their full announcement here.

Bintray — JFrog

JFrog has informed me that they will not be decommissioning HTTP for dl.bintray.com as it is used for resolving artifacts for other ecosystems. I have pleaded with them to reconsider this decision, but at this time they are not willing to commit to this breaking change.

Gradle Plugin Portal — Gradle

The Gradle Plugin Portal will drop support for HTTP on January 15th, 2020.
You can read their full announcement here.

Spring — Pivotal

The Spring Artifact Repository will drop support for HTTP on January 15th, 2020.
You can read their full announcement here.

Eclipse — Eclipse Foundation

Although I’ve reached out to the Eclipse Foundation here and they were initially receptive, currently there has been no commitment on their part.

JetBrains

JetBrains is not willing to commit to a timeline at this point for their repositories they use to host artifacts.

RedHat

I’ve reached out to the RedHat security team on multiple occasions about this initiative and they have been unwilling to commit to a timeline for backing this initiative at this time. They are concerned that such a change will break their paying customers and are therefore unwilling to commit to this change at this time.

Twitter

Similarly, the Twitter Security team has been unwilling to commit to this initiative.

Warnings from the Build Tools

Starting in Gradle 6.0 and Scala Build Tool (SBT) 1.3.x, both will begin warning users that they are using HTTP instead of HTTPS to resolve dependencies with the ability to disable the warning on a per-repository basis.
Additionally, Google’s Bazel build will now require users to specify an SHA-256 hash for any resources downloaded over HTTP.

Get Jonathan Leitschuh’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Unfortunately, at this time, no work has been made towards implementing the same warning in Apache Maven.

Deprecate HTTP Download & Upload
This Jira has been LDAP enabled, if you are an ASF Committer, please use your LDAP credentials to log in. Any problems…

issues.apache.org

Eliminating this vulnerability in Open Source
With GitHub’s Semmle QL we can do just this for the entire OSS ecosystem
GitHub Security Lab: CodeQL

GitHub recently acquired Semmle and with it their query language QL. QL enables security researchers to write an abstract query for a given vulnerability and find all variations of that vulnerability across Open Source Software (OSS). Additionally, GitHub recently announced a new Open Source Bug Bounty Program which rewards researchers for submitting their queries. Semmle’s QL query language is evaluated against every new Open Source project on GitHub. The implications of this are that researchers can now create queries that will eliminate entire classes of vulnerabilities across the OSS ecosystem.

I recently contributed this simple QL query as a part of the new GitHub Security Lab Bug Bounty Program. The submission to the Bug Bounty program can be found here.

This fairly simple query will detect and flag all POM.xml files that use HTTP or FTP. As soon as this query is merged and deployed, it will begin detecting this vulnerability in all future open source contributions to GitHub.

I highly recommend that all GitHub Repositories that haven’t applied the LGTM GitHub integration should do so here!

Press enter or click to view image in full size
Bounty!

For the above query, the GitHub Security Lab team was kind enough to award me with a $2,300 reward as a part of the ‘All for one, one for all’ program.

More information here: GitHub Security Lab Bug Bounty Program.

What do I need to do?

As a software developer, security engineer, or operations engineer, please proactively check your Maven, Gradle, SBT, Bazel, Buck, JFrog Artifactory and/or Sonatype Nexus configurations to ensure that your company or project won’t be impacted by this change on January 13th -15th, 2020.

Follow Infosec Write-ups for more such awesome write-ups.

InfoSec Write-ups
A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub…

medium.com
