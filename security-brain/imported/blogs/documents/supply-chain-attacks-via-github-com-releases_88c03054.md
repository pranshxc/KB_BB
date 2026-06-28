---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-04-25_supply-chain-attacks-via-githubcom-releases.md
original_filename: 2021-04-25_supply-chain-attacks-via-githubcom-releases.md
title: Supply Chain Attacks via GitHub.com Releases
category: documents
detected_topics:
- supply-chain
- command-injection
- business-logic
- api-security
tags:
- imported
- documents
- supply-chain
- command-injection
- business-logic
- api-security
language: en
raw_sha256: 88c03054e9873bd873bc51794d4e564d913ca2c1875c95137ea24830f06367a8
text_sha256: c3048968aa55fd06ad3988dd119b5a0fd8f1cefef787a77a1b25029c533522ed
ingested_at: '2026-06-28T07:32:05Z'
sensitivity: unknown
redactions_applied: false
---

# Supply Chain Attacks via GitHub.com Releases

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-04-25_supply-chain-attacks-via-githubcom-releases.md
- Source Type: markdown
- Detected Topics: supply-chain, command-injection, business-logic, api-security
- Ingested At: 2026-06-28T07:32:05Z
- Redactions Applied: False
- Raw SHA256: `88c03054e9873bd873bc51794d4e564d913ca2c1875c95137ea24830f06367a8`
- Text SHA256: `c3048968aa55fd06ad3988dd119b5a0fd8f1cefef787a77a1b25029c533522ed`


## Content

---
title: "Supply Chain Attacks via GitHub.com Releases"
page_title: "Supply Chain Attacks via GitHub.com Releases | Nightwatch Cybersecurity"
url: "https://wwws.nightwatchcybersecurity.com/2021/04/25/supply-chain-attacks-via-github-com-releases/"
final_url: "https://wwws.nightwatchcybersecurity.com/2021/04/25/supply-chain-attacks-via-github-com-releases/"
authors: ["Nightwatch Cybersecurity (@nightwatchcyber)"]
programs: ["GitHub"]
bugs: ["Logic flaw"]
publication_date: "2021-04-25"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3706
---

# Supply Chain Attacks via GitHub.com Releases

[April 25, 2021April 25, 2021](https://wwws.nightwatchcybersecurity.com/2021/04/25/supply-chain-attacks-via-github-com-releases/) [nightwatchcyber](https://wwws.nightwatchcybersecurity.com/author/nightwatchcyber/) [Advisories](https://wwws.nightwatchcybersecurity.com/category/advisories/), [Research](https://wwws.nightwatchcybersecurity.com/category/research/)[github](https://wwws.nightwatchcybersecurity.com/tag/github/), [supplychainattack](https://wwws.nightwatchcybersecurity.com/tag/supplychainattack/)

# Summary

Release functionality on **[GitHub.com](https://github.com/)** allows modification of assets within a release by any project collaborator. This can occur after the release is published, and without notification or audit logging accessible in the UI to either the project owners or the public. However, some audit information may be available via the GitHub APIs. An attacker can compromise a collaborator’s account and use it to modify releases without the knowledge of project owners or the public, thus resulting in supply chain attacks against the users of the project.

This issue was reported to the vendor – their response is that this is intended behavior and is an intentional design decision. While the vendor is planning improvements in this area, they are not able to provide additional details. GitHub.com paid plans and the GitHub enterprise server were not tested.

As a mitigation measure, project owners using GitHub.com are encouraged to use other methods for securing releases such as digitally signing releases with PGP. Users are encouraged to check digital signatures and use the GitHub.com release APIs to extract and verify release assets data.

# Background

**[GitHub.com](https://github.com/)** is a widely used tool for software development offering source code management (SCM) and other tools. It is used for hosting and distribution by many open source projects (OSS). The release functionality within GitHub.com offers a way to publish packaged software iterations as releases. These include a compressed snapshot of the source within the project as a .ZIP and .TAR.GZ file, as well as as additional binary assets. This functionality is a common way for open source projects to distribute their releases.

# Vulnerability Details

The release functionality on **GitHub.com** allows modification of assets within a release by any project collaborator, after the initial release is published. An attacker can use this gap to modify releases without the knowledge of project owners by compromising an account of any project collaborator, thus resulting in supply chain attacks against those using the project. The following specific issues facilitate this:

  * **Release assets can be modified after initial publication** – except for the source code snapshots
  * **Any project collaborator can modify a release** – there are no fine-grained controls to allow code access and not release access.
  * **There is no notification or indication within the UI that a release was modified** – to either the project owners or other collaborators, or the public. However, some data is exposed via API. 
  * **A “verified” flag is displayed if the Git commit was verified** – but this only applies to the source code snapshot and not the other release assets

[The releases API provided by GitHub](https://docs.github.com/en/rest/reference/repos#releases) does expose additional information about release assets, which could potentially be used to see if a release was modified. This information includes the username of the uploader and the timestamp when the upload took place. This can be compared to the main release metadata. An example of using APIs for checking releases can be found at [our release_auditor project](https://github.com/nightwatchcybersecurity/release_auditor).

**NOTE: Paid GitHub.com plans and the GitHub enterprise server were not tested.**

Example of a release ([see here](https://github.com/nightwatchcyber/gh_release_test/releases/tag/0.1)):

![](https://wwws.nightwatchcybersecurity.com/wp-content/uploads/2021/04/screen-shot-2021-04-24-at-11.45.50-pm.png)

[Example of API response](https://api.github.com/repos/nightwatchcyber/gh_release_test/releases/41605278) exposing asset data:

![](https://wwws.nightwatchcybersecurity.com/wp-content/uploads/2021/04/screen-shot-2021-04-24-at-11.57.36-pm.png?w=954) ![](https://wwws.nightwatchcybersecurity.com/wp-content/uploads/2021/04/screen-shot-2021-04-24-at-11.58.15-pm.png?w=876)

# Steps to Replicate

The following steps can be used to replicate this issue:

  1. Alice creates a public repository on GitHub.com, and adds some code including a shell script “test.sh”.
  2. Alice invites Bob as a collaborator on this repository.
  3. Alice publishes a release including the shell script “test.sh” as a separate asset.
  4. Bob accesses the release, and modifies the “test.sh” script within the release.
  5. When viewing the release via GitHub.com UI, there is no indication the script was modified. Downloading the script shows that it is different from what Alice published.

**NOTE: Paid GitHub.com plans and the GitHub enterprise server were not tested.**

# Vendor Response and Mitigation

The issue was reported to the vendor via their bounty program. **Their response is that this is intended behavior and is an intentional design decision. While the vendor is planning improvements in this area, they are not able to provide additional details.**

GitHub.com paid plans and the GitHub enterprise server were not tested.

As a mitigation measure, project owners using GitHub.com are encouraged to use other methods for securing releases such as digitally signing releases with PGP. Users are encouraged to check digital signatures and use the GitHub.com release APIs to extract and verify release assets data.

An example of using APIs to check releases can be found in [our release_auditor project](https://github.com/nightwatchcybersecurity/release_auditor).

# References

Example repository: <https://github.com/nightwatchcyber/gh_release_test>  
GitHub.com docs: [here](https://docs.github.com/en/github/administering-a-repository/about-releases), [here](https://docs.github.com/en/github/administering-a-repository/managing-releases-in-a-repository) and [here](https://docs.github.com/en/rest/reference/repos#releases)  
HackerOne report # 1167780  
release_auditor: [see here](https://github.com/nightwatchcybersecurity/release_auditor)

# Credits

Advisory written by Y. Shafranovich

# Timeline

2021-04-18: Initial report submitted to the vendor  
2021-04-20: Automated response received  
2021-04-21: Vendor response received, intended behavior  
2021-04-21: Request to disclose sent  
2021-04-23: Vendor ok with disclosure  
2021-04-25: Public disclosure – added a link to the OSS project  

### Share this:

  * [ Share on X (Opens in new window) X ](https://wwws.nightwatchcybersecurity.com/2021/04/25/supply-chain-attacks-via-github-com-releases/?share=twitter)
  * [ Share on Facebook (Opens in new window) Facebook ](https://wwws.nightwatchcybersecurity.com/2021/04/25/supply-chain-attacks-via-github-com-releases/?share=facebook)
  * 

Like Loading...
