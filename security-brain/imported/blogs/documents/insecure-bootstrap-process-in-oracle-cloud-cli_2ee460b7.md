---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-02-06_insecure-bootstrap-process-in-oracle-cloud-cli.md
original_filename: 2022-02-06_insecure-bootstrap-process-in-oracle-cloud-cli.md
title: Insecure Bootstrap Process in Oracle Cloud CLI
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
raw_sha256: 2ee460b7b7a6cfed6b3f29fccda12f82622d0e97f5cbc84a40052cfbef084c90
text_sha256: 52fced101ad7019ab41169cc496ec0554e69d1211c6392d19bf4689611d17858
ingested_at: '2026-06-28T07:32:09Z'
sensitivity: unknown
redactions_applied: false
---

# Insecure Bootstrap Process in Oracle Cloud CLI

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-02-06_insecure-bootstrap-process-in-oracle-cloud-cli.md
- Source Type: markdown
- Detected Topics: command-injection, supply-chain
- Ingested At: 2026-06-28T07:32:09Z
- Redactions Applied: False
- Raw SHA256: `2ee460b7b7a6cfed6b3f29fccda12f82622d0e97f5cbc84a40052cfbef084c90`
- Text SHA256: `52fced101ad7019ab41169cc496ec0554e69d1211c6392d19bf4689611d17858`


## Content

---
title: "Insecure Bootstrap Process in Oracle Cloud CLI"
page_title: "Insecure Bootstrap Process in Oracle Cloud CLI | Nightwatch Cybersecurity"
url: "https://wwws.nightwatchcybersecurity.com/2022/02/06/insecure-bootstrap-process-in-oracle-cloud-cli/"
final_url: "https://wwws.nightwatchcybersecurity.com/2022/02/06/insecure-bootstrap-process-in-oracle-cloud-cli/"
authors: ["Nightwatch Cybersecurity (@nightwatchcyber)"]
programs: ["Oracle"]
bugs: ["Supply chain attack"]
publication_date: "2022-02-06"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 2932
---

# Insecure Bootstrap Process in Oracle Cloud CLI

[February 6, 2022](https://wwws.nightwatchcybersecurity.com/2022/02/06/insecure-bootstrap-process-in-oracle-cloud-cli/) [nightwatchcyber](https://wwws.nightwatchcybersecurity.com/author/nightwatchcyber/) [Research](https://wwws.nightwatchcybersecurity.com/category/research/)[oracle](https://wwws.nightwatchcybersecurity.com/tag/oracle/)

## Summary

The bootstrap process for Oracle Cloud CLI using the “curl | bash” pattern was insecure since there was no way to verify authenticity of the downloaded binaries. The vendor is now publishing checksums that can be used to verify the downloaded binaries.

## Vulnerability Details

[As part of our ongoing research into supply chain attacks](https://wwws.nightwatchcybersecurity.com/2021/07/12/speaking-appsec_village-defcon-29/), we have been analyzing bash installer scripts using the “curl | basj” pattern. [Oracle provides such script](https://github.com/oracle/oci-cli#linux) used to install the CLI command for interaction with Oracle Cloud. However, there was no way to check whether the files that the script downloads are legitimate, which could potentially open the end-user to supply chain attacks. The installer is run as follows:
  
  
  bash -c "$(curl -L https://raw.githubusercontent.com/oracle/oci-cli/master/scripts/install/install.sh)"

## Vendor Response

The vendor [started publishing SHA-256](https://github.com/oracle/oci-cli/releases) checksums for the CLI.

## References

Vendor reference # S1456147

Vendor security advisory: [Jan 2022](https://www.oracle.com/security-alerts/cpujan2022.html)

## Timeline

2021-04-21: Initial report to the vendor  
2021-04-21: Vendor acknowledged the report  
2021-05-04: Vendor communicated that a fix is pending  
2021-12-28: Vendor reported that a fix has been implemented and credit will be provided in an advisory  
2022-01-18: Vendor advisory published  
2022-02-06: Public disclosure

### Share this:

  * [ Share on X (Opens in new window) X ](https://wwws.nightwatchcybersecurity.com/2022/02/06/insecure-bootstrap-process-in-oracle-cloud-cli/?share=twitter)
  * [ Share on Facebook (Opens in new window) Facebook ](https://wwws.nightwatchcybersecurity.com/2022/02/06/insecure-bootstrap-process-in-oracle-cloud-cli/?share=facebook)
  * 

Like Loading...
