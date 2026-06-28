---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-09-18_38tb-of-data-accidentally-exposed-by-microsoft-ai-researchers.md
original_filename: 2023-09-18_38tb-of-data-accidentally-exposed-by-microsoft-ai-researchers.md
title: 38TB of data accidentally exposed by Microsoft AI researchers
category: documents
detected_topics:
- supply-chain
- xss
- command-injection
- mobile-security
- sso
- access-control
tags:
- imported
- documents
- supply-chain
- xss
- command-injection
- mobile-security
- sso
- access-control
language: en
raw_sha256: 806cf4f709bbd39bc2f9614b8bd2ef285c52491fb1f2e085d7be377e03195623
text_sha256: 05934d718934def99120610ecf869312c5dfac8b306063945acb0726c862685d
ingested_at: '2026-06-28T07:32:26Z'
sensitivity: unknown
redactions_applied: false
---

# 38TB of data accidentally exposed by Microsoft AI researchers

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-09-18_38tb-of-data-accidentally-exposed-by-microsoft-ai-researchers.md
- Source Type: markdown
- Detected Topics: supply-chain, xss, command-injection, mobile-security, sso, access-control
- Ingested At: 2026-06-28T07:32:26Z
- Redactions Applied: False
- Raw SHA256: `806cf4f709bbd39bc2f9614b8bd2ef285c52491fb1f2e085d7be377e03195623`
- Text SHA256: `05934d718934def99120610ecf869312c5dfac8b306063945acb0726c862685d`


## Content

---
title: "38TB of data accidentally exposed by Microsoft AI researchers"
page_title: "38TB of data accidentally exposed by Microsoft AI researchers  | Wiz Blog"
url: "https://www.wiz.io/blog/38-terabytes-of-private-data-accidentally-exposed-by-microsoft-ai-researchers"
final_url: "https://www.wiz.io/blog/38-terabytes-of-private-data-accidentally-exposed-by-microsoft-ai-researchers"
authors: ["Hillai Ben-Sasson (@hillai)", "Ronny Greenberg"]
programs: ["Microsoft"]
bugs: ["Cloud", "Broken authorization"]
publication_date: "2023-09-18"
added_date: "2023-09-19"
source: "pentester.land/writeups.json"
original_index: 771
---

## 

**Executive summary**

  * Microsoft’s AI research team, while publishing a bucket of open-source training data on GitHub, accidentally exposed 38 terabytes of additional private data — including a disk backup of two employees’ workstations. 

  * The backup includes secrets, private keys, passwords, and over 30,000 internal Microsoft Teams messages. 

  * The researchers shared their files using an Azure feature called SAS tokens, which allows you to share data from Azure Storage accounts. 

  * The access level can be limited to specific files only; however, in this case, the link was configured to share the entire storage account — including another 38TB of private files. 

  * This case is an example of the [new risks organizations face](https://www.wiz.io/academy/ai-security-risks) when starting to leverage the power of AI more broadly, as more of their engineers now work with massive amounts of training data. As data scientists and engineers race to bring new AI solutions to production, the massive amounts of data they handle require additional security checks and safeguards. 

## 

**Introduction and Microsoft findings**

As part of the Wiz Research Team’s [_ongoing work_](https://www.youtube.com/watch?v=rbHALyrxj0Y) on accidental exposure of cloud-hosted data, the team scanned the internet for misconfigured storage containers. In this process, we found a GitHub repository under the Microsoft organization named `robust-models-transfer`. The repository belongs to Microsoft’s AI research division, and its purpose is to provide open-source code and AI models for image recognition. Readers of the repository were instructed to download the models from an Azure Storage URL: 

![](data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wCEAAoHBwgHBgoICAYGBgoLCg4SDgYGDhEJFgcNFxMZGBYTFhUaHysjGh0oHRUWJDUlKC0vMjIyGSI4PTcwPCsxMi8BCgsLBQUFEAUFEC8cFhwvLy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vL//AABEIAAgAGAMBIgACEQEDEQH/xAAXAAEBAQEAAAAAAAAAAAAAAAAABAYB/8QAGRAAAwEBAQAAAAAAAAAAAAAAAAECAzER/8QAFQEBAQAAAAAAAAAAAAAAAAAAAgD/xAAUEQEAAAAAAAAAAAAAAAAAAAAA/9oADAMBAAIRAxEAPwDIVrSgl01dLxnAIUmsp9ABJ//Z)

The exposed storage URL, taken from Microsoft’s GitHub repository

However, this URL allowed access to more than just open-source models. It was configured to grant permissions on the entire storage account, exposing additional private data by mistake. 

Our scan shows that this account contained 38TB of additional data — including Microsoft employees’ personal computer backups. The backups contained sensitive personal data, including passwords to Microsoft services, secret keys, and over 30,000 internal Microsoft Teams messages from 359 Microsoft employees. 

![](data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wCEAAoHBwgHBgoICAgFCgoFBQwFBQUFBREJCgUMFxMZGBYTFhUaHysjGh0oHRUWJDUlKC0vMjIyGSI4PTcwPCsxMi8BCgsLBQUFEAUFEC8cFhwvLy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vL//AABEIABQAGAMBIgACEQEDEQH/xAAVAAEBAAAAAAAAAAAAAAAAAAAAB//EABQQAQAAAAAAAAAAAAAAAAAAAAD/xAAVAQEBAAAAAAAAAAAAAAAAAAAAAv/EABQRAQAAAAAAAAAAAAAAAAAAAAD/2gAMAwEAAhEDEQA/AK+AlQAAAAAD/9k=)

Exposed containers under the 'robustnessws4285631339' storage account 

![](data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wCEAAoHBwgHBgoSEggSDhURDiENDQ0PDRENDQ4NFxQZGBYfFhYdHysjGh0oHSEWJDUlKC0vMjIyGSI4PTcwPCsxMi8BCgsLDg0OHQsNHC8oFh0vOy8vLy8vLy8vLy8vOzUvLy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vL//AABEIABIAGAMBIgACEQEDEQH/xAAZAAEBAAMBAAAAAAAAAAAAAAAABAMFBwH/xAAdEAACAgIDAQAAAAAAAAAAAAAAAQIDBEERITQS/8QAFgEBAQEAAAAAAAAAAAAAAAAAAQAC/8QAFBEBAAAAAAAAAAAAAAAAAAAAAP/aAAwDAQACEQMRAD8A6dnTSzUXU2wXHZr8ypzzUVLDlyuzIXKUZbBjro+NgUlu9yLz0EgACX//2Q==)

A small sample of sensitive files found on the computer backups

![](data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wCEAAoHBwgHBgoICAgFCgoFBQwFBQUFBREJCgUMFxMZGBYTFhUaHysjGh0oHRUWJDUlKC0vMjIyGSI4PTcwPCsxMi8BCgsLBQUFEAUFEC8cFhwvLy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vL//AABEIABgAGAMBIgACEQEDEQH/xAAVAAEBAAAAAAAAAAAAAAAAAAAAB//EABQQAQAAAAAAAAAAAAAAAAAAAAD/xAAVAQEBAAAAAAAAAAAAAAAAAAAAAv/EABQRAQAAAAAAAAAAAAAAAAAAAAD/2gAMAwEAAhEDEQA/AK2ApIAAAAAD/9k=)

Redacted Teams conversation between two Microsoft employees

In addition to the overly permissive access scope, the token was also misconfigured to allow “full control” permissions instead of read-only. Meaning, not only could an attacker view all the files in the storage account, but they could delete and overwrite existing files as well. 

This is particularly interesting considering the repository’s original purpose: providing AI models for use in training code. The repository instructs users to download a model data file from the SAS link and feed it into a script. The file’s format is `ckpt`, a format produced by the TensorFlow library. It’s formatted using Python’s `pickle` formatter, which is [_prone to arbitrary code execution_](https://huggingface.co/docs/hub/security-pickle) by design. Meaning, an attacker could have injected malicious code into all the AI models in this storage account, and every user who trusts Microsoft’s GitHub repository would’ve been infected by it. 

However, it’s important to note this storage account wasn’t directly exposed to the public; in fact, it was a private storage account. The Microsoft developers used an Azure mechanism called “SAS tokens”, which allows you to create a shareable link granting access to an Azure Storage account’s data — while upon inspection, the storage account would still seem completely private. 

![](data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wCEAAoHBwgHBgoICAgLChAPDhIPFQ0NDhINDQ0YFxMZGBYTIhUmHysjGh0oHRUWJDUlKC0vMjIyGSI4PTcwPCsxMi8BCgsLDg0OGA4QHDscIhwvLy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vL//AABEIAA4AGAMBIgACEQEDEQH/xAAZAAABBQAAAAAAAAAAAAAAAAAGAQIDBAX/xAAdEAACAgIDAQAAAAAAAAAAAAABAwAEAgUhMTIS/8QAFQEBAQAAAAAAAAAAAAAAAAAAAwH/xAAXEQEAAwAAAAAAAAAAAAAAAAAAAQIi/9oADAMBAAIRAxEAPwALrMrrpEDISfV4qYSQYPYLIrejLuqbmroxomqtLcJ+V8RY280sRzFjZR//2Q==)

## 

**Introduction to SAS tokens**

In Azure, a Shared Access Signature (SAS) token is a signed URL that grants access to Azure Storage data. The access level can be customized by the user; the permissions range between read-only and full control, while the scope can be either a single file, a container, or an entire storage account. The expiry time is also completely customizable, allowing the user to create never-expiring access tokens. This granularity provides great agility for users, but it also creates the risk of granting too much access; in the most permissive case (as we’ve seen in Microsoft’s token above), the token can allow full control permissions, on the entire account, forever – essentially providing the same access level as the account key itself. 

![](data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wCEAAoHBwgHBgoICAgLChMQDhgVDQ0WFRMOFg0YFx8eGBYVFhUdHysjGh0oHSEiJDUlKDkvMjIyGSI4PTcwPCsxMi8BCgsLDg0OHRANHC8cFhwvLy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vL//AABEIAAwAGAMBIgACEQEDEQH/xAAZAAACAwEAAAAAAAAAAAAAAAADBQEEBgD/xAAeEAACAQQDAQAAAAAAAAAAAAACAwABBREhBCJBFf/EABYBAAMAAAAAAAAAAAAAAAAAAAABBP/EABgRAAIDAAAAAAAAAAAAAAAAAABRAQIR/9oADAMBAAIRAxEAPwDDWpAfKLNYe3LXQS3FnAadLSWK+QPAezJdvZRE1QDW6IE1arOlZzCJO6yYtqgP/9k=)

There are 3 types of SAS tokens: Account SAS, Service SAS, and User Delegation SAS. In this blog we will focus on the most popular type – Account SAS tokens, which were also used in Microsoft’s repository. 

Generating an Account SAS is a simple process. As can be seen in the screen below, the user configures the token’s scope, permissions, and expiry date, and generates the token. Behind the scenes, the browser downloads the account key from Azure, and signs the generated token with the key. This entire process is done on the client side; it’s not an Azure event, and the resulting token is not an Azure object. 

![](data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wCEAAoHBwgHBg8NDggPEA4NDBgNDgkNDhENFg4YFx8ZGBYTFiEaHysjGh0oHRUWJDUlKC0vMjIyGSI4PTcwPCsxMi8BCgsLDg0OEg4NFi8cFhwvLy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vL//AABEIABMAGAMBIgACEQEDEQH/xAAYAAEBAQEBAAAAAAAAAAAAAAAABAUGA//EAB8QAAICAAcBAAAAAAAAAAAAAAABAgMSITEzQVFxEf/EABQBAQAAAAAAAAAAAAAAAAAAAAP/xAAXEQADAQAAAAAAAAAAAAAAAAAAAQIR/9oADAMBAAIRAxEAPwDi7qlhILKWa9kPsCGeXA1JBzhnyU0tAUy8AeIXEa62yOazAEoCDzaXQACGP//Z)

Creating a high privilege non-expiring SAS token

Because of this, when a user creates a highly-permissive non-expiring token, there is no way for an administrator to know this token exists and where it circulates. Revoking a token is no easy task either — it requires rotating the account key that signed the token, rendering all other tokens signed by same key ineffective as well. These unique pitfalls make this service an easy target for attackers looking for exposed data. 

Besides the risk of accidental exposure, the service’s pitfalls make it an effective tool for attackers seeking to maintain persistency on compromised storage accounts. A recent [_Microsoft report_](https://www.microsoft.com/en-us/security/blog/2023/09/07/cloud-storage-security-whats-new-in-the-threat-matrix/#:~:text=Create%20SAS%20Token) indicates that attackers are taking advantage of the service’s lack of monitoring capabilities in order to issue privileged SAS tokens as a backdoor. Since the issuance of the token is not documented anywhere, there is no way to know that it was issued and act against it. 

## 

**SAS security risks**

SAS tokens pose a security risk, as they allow sharing information with external unidentified identities. The risk can be examined from several angles: permissions, hygiene, management and monitoring. 

![](data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wCEAAoHBwsTDwoOBw4JBg0GDgwQDQcGCRENDQkNFx8ZGBYVFiEaHysjGh0oHRUWJDUlKC0vMjIyGSI4PTcwPCsxMi8BCgsLDg0OFhANHC8cFhwvLy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vL//AABEIAA8AGAMBIgACEQEDEQH/xAAWAAEBAQAAAAAAAAAAAAAAAAABBgD/xAAVEAEBAAAAAAAAAAAAAAAAAAAAEf/EABYBAQEBAAAAAAAAAAAAAAAAAAEDAP/EABYRAQEBAAAAAAAAAAAAAAAAAAASAf/aAAwDAQACEQMRAD8AhKKYIqck1hCw2X//2Q==)

### 

**Permissions**

A SAS token can grant a very high access level to a storage account, whether through excessive permissions (like read, list, write or delete), or through wide access scopes that allow users to access adjacent storage containers. 

### 

**Hygiene**

SAS tokens have an expiry problem — our scans and monitoring show organizations often use tokens with a very long (sometimes infinite) lifetime, as there is no upper limit on a token's expiry. This was the case with Microsoft’s token, which was valid until 2051. 

### 

**Management and monitoring**

Account SAS tokens are extremely hard to manage and revoke. There isn't any official way to keep track of these tokens within Azure, nor to monitor their issuance, which makes it difficult to know how many tokens have been issued and are in active use. The reason even issuance cannot be tracked is that SAS tokens are created on the client side, therefore it is not an an Azure tracked activity, and the generated token is not an Azure object. Because of this, even what appears to be a private storage account may potentially be widely exposed. 

As for revocation, there isn't a way to revoke a singular Account SAS; the only solution is revoking the entire account key, which invalidates all the other tokens issued with the same key as well. 

Monitoring the usage of SAS tokens is another challenge, as it requires enabling logging on each storage account separately. It can also be costly, as the pricing depends on the request volume of each storage account. 

## 

**SAS security recommendations**

SAS security can be significantly improved with the following recommendations.

### 

**Management**

Due to the lack of security and governance over Account SAS tokens, they should be considered as sensitive as the account key itself. Therefore, it is highly recommended to avoid using Account SAS for external sharing. Token creation mistakes can easily go unnoticed and expose sensitive data. 

For external sharing, consider using a Service SAS with a [_Stored Access Policy_](https://learn.microsoft.com/en-us/rest/api/storageservices/define-stored-access-policy). This feature connects the SAS token to a server-side policy, providing the ability to manage policies and revoke them in a centralized manner. 

If you need to share content in a time-limited manner, consider using a [_User Delegation SAS_](https://learn.microsoft.com/en-us/rest/api/storageservices/create-user-delegation-sas), since their expiry time is capped at 7 days. This feature connects the SAS token to Azure Active Directory’s identity management, providing control and visibility over the identity of the token’s creator and its users. 

Additionally, we recommend creating dedicated storage accounts for external sharing, to ensure that the potential impact of an over-privileged token is limited to external data only. 

To avoid SAS tokens completely, organizations will have to [_disable SAS access_](https://learn.microsoft.com/en-us/azure/storage/common/shared-key-authorization-prevent) for each of their storage accounts separately. We recommend using a [CSPM ](https://www.wiz.io/academy/what-is-cloud-security-posture-management-cspm)to track and enforce this as a policy. 

Another solution to disable SAS token creation is by blocking access to the “[ _list storage account keys_](https://learn.microsoft.com/en-us/rest/api/storagerp/storage-accounts/list-keys)” operation in Azure (since new SAS tokens cannot be created without the key), then rotating the current account keys, to invalidate pre-existing SAS tokens. This approach would still allow creation of User Delegation SAS, since it relies on the user’s key instead of the account key. 

### 

Monitoring 

To track active SAS token usage, you need to [_enable Storage Analytics logs_](https://learn.microsoft.com/en-us/azure/storage/common/manage-storage-analytics-logs) for each of your storage accounts. The resulting logs will contain details of SAS token access, including the signing key and the permissions assigned. However, it should be noted that only actively used tokens will appear in the logs, and that enabling logging comes with extra charges — which might be costly for accounts with extensive activity. 

[ _Azure Metrics_](https://learn.microsoft.com/en-us/azure/storage/blobs/blob-storage-monitoring-scenarios) can be used to monitor SAS tokens usage in storage accounts. By default, Azure records and aggregates storage account events up to [_93 days_](https://learn.microsoft.com/en-us/azure/azure-monitor/essentials/data-platform-metrics#retention-of-metrics). Utilizing Azure Metrics, users can look up SAS-authenticated requests, highlighting storage accounts with SAS tokens usage. 

### 

**Secret scanning**

In addition, we recommend using [secret scanning tools](https://www.wiz.io/academy/secret-scanning#open-source-secret-scanning-tools-47) to detect leaked or over-privileged SAS tokens in artifacts and publicly exposed assets, such as mobile apps, websites, and GitHub repositories — as can be seen in the Microsoft case. 

For more information on cloud secret scanning, please check out our recent talk from the fwd:cloudsec 2023 conference, [_"Scanning the internet for external cloud exposures"_](https://youtu.be/rbHALyrxj0Y). 

### 

**For Wiz customers**

Wiz customers can leverage the Wiz secret scanning capabilities to identify SAS tokens in internal and external assets and explore their permissions. In addition, customers can use the Wiz CSPM to track storage accounts with SAS support. 

  * **Detect SAS tokens:** use this [_query_](https://app.wiz.io/graph#~\(query~\(type~\(~'SECRET_DATA\)~select~true~where~\(presignedURL_type~\(EQUALS~\(~'PresignedURLTypeAzureSASToken\)\)\)~relationships~\(~\(type~\(~\(type~'PERMITS\)\)~optional~true~with~\(type~\(~'STORAGE_ACCOUNT\)~select~true\)\)~\(type~\(~\(type~'INSTANCE_OF~reverse~true\)\)~with~\(type~\(~'SECRET_INSTANCE\)~select~true~relationships~\(~\(type~\(~\(type~'CONTAINS~reverse~true\)\)~with~\(type~\(~'CLOUD_RESOURCE\)~select~true\)\)\)\)\)\)\)~view~'table~columns~\(~\(~'0~49\)~\(~'1~17\)~\(~'2~17\)~\(~'3~17\)\)\)) to surface all SAS tokens in all your monitored cloud environments. 

  * **Detect high-privilege SAS tokens:** use the following [_control_](https://app.wiz.io/graph#~\(control~'wc-id-927~view~'table\)) to detect highly-privileged SAS tokens located on publicly exposed workloads. 

  * **CSPM rule for blocking SAS tokens:** use the following [_Cloud Configuration Rule_](https://app.wiz.io/graph#~\(query~\(type~\(~'STORAGE_ACCOUNT\)~select~true~relationships~\(~\(type~\(~\(type~'ALERTED_ON~reverse~true\)\)~with~\(type~\(~'CONFIGURATION_FINDING\)~select~true~where~\(configurationRuleShortName~\(EQUALS~\(~'StorageAccount-026\)\)\)\)\)~\(type~\(~\(type~'CONTAINS~reverse~true\)\)~optional~true~with~\(type~\(~'SUBSCRIPTION\)~select~true\)\)\)\)\)) to track storage accounts allowing SAS token usage. 

## 

**Security risks in the AI pipeline**

As companies embrace AI more widely, it is important for security teams to understand the inherent security risks at each stage of the AI development process. 

![](data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wCEAAoHBwgHBgoICAgLChUTDRINDg4ZGhENDREYFxYZGBYTFhUaHysjGh0oHRUiJDUlKC0vMjIyGSI4PTcwPCsxMi8BCgsLDg0OEBANHC8cFhwvLy8vLy8vOy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vL//AABEIAAwAGAMBIgACEQEDEQH/xAAaAAAABwAAAAAAAAAAAAAAAAAAAQIDBAUG/8QAHhAAAQMEAwAAAAAAAAAAAAAAAwABBAITITIUIjH/xAAWAQADAAAAAAAAAAAAAAAAAAAAAQP/xAAYEQADAQEAAAAAAAAAAAAAAAAAARJRAv/aAAwDAQACEQMRAD8AxsSIOx6pHGAw8uqyMauxsjctb07K665wcoelRgsPDoJNfYGUEUsCEf/Z)

The incident detailed in this blog is an example of two of these risks. 

The first is **oversharing of data**.**** Researchers collect and share massive amounts of external and internal data to construct the required training information for their AI models. This poses inherent security risks tied to high-scale data sharing. It is crucial for security teams to define clear guidelines for external sharing of AI datasets. As we’ve seen in this case, separating the public [AI data](https://www.wiz.io/academy/ai-data-security) set to a dedicated storage account could’ve limited the exposure. 

The second is the risk of **supply chain attacks**. Due to improper permissions, the public token granted write access to the storage account containing the AI models. As noted above, injecting malicious code into the model files could’ve led to a supply chain attack on other researchers who use the repository’s models. Security teams should review and sanitize AI models from external sources, since they can be used as a remote code execution vector. 

## 

**Takeaways**

The simple step of sharing an AI dataset led to a major data leak, containing over 38TB of private data. The root cause was the usage of Account SAS tokens as the sharing mechanism. Due to a lack of monitoring and governance, SAS tokens pose a security risk, and their usage should be as limited as possible. These tokens are very hard to track, as Microsoft does not provide a centralized way to manage them within the Azure portal. In addition, these tokens can be configured to last effectively forever, with no upper limit on their expiry time. Therefore, using Account SAS tokens for external sharing is unsafe and should be avoided. 

In the wider scope, similar incidents can be prevented by granting security teams more visibility into the processes of AI research and development teams. As we see wider adoption of AI models within companies, it’s important to raise awareness of relevant security risks at every step of the AI development process, and make sure the security team works closely with the data science and research teams to ensure proper guardrails are defined. 

Microsoft's account of this issue is available on the [MSRC blog](https://msrc.microsoft.com/blog/2023/09/microsoft-mitigated-exposure-of-internal-information-in-a-storage-account-due-to-overly-permissive-sas-token/).

## 

**Timeline**

  * **Jul. 20, 2020** – SAS token first [_committed_](https://github.com/microsoft/robust-models-transfer/blob/e61568d613c025adfd07f61f2639f3ae78852143/README.md?plain=1#L36) to GitHub; expiry set to Oct. 5, 2021 

  * **Oct. 6, 2021** – SAS token expiry [_updated_](https://github.com/microsoft/robust-models-transfer/commit/a9e0e80bcd49bd8651c0b3198c7dc89179b2c0ac) to Oct. 6, 2051 

  * **Jun. 22, 2023** – Wiz Research finds and reports issue to MSRC 

  * **Jun. 24, 2023** – SAS token invalidated by Microsoft 

  * **Jul. 7, 2023** – SAS token [_replaced_](https://github.com/microsoft/robust-models-transfer/commit/c26ebfff3d01bd2a52a6c14febb8b7ea0234431d) on GitHub 

  * **Aug. 16, 2023** – Microsoft completes internal investigation of potential impact 

  * **Sep. 18, 2023** – Public disclosure 

## 

**Stay in touch!**

Hi there! We are Hillai Ben-Sasson ([@hillai](https://twitter.com/hillai)), Shir Tamari ([@shirtamari](https://twitter.com/shirtamari)), Nir Ohfeld ([@nirohfeld](https://twitter.com/nirohfeld)), Sagi Tzadik ([@sagitz_](https://twitter.com/sagitz_)) and Ronen Shustin ([@ronenshh](https://twitter.com/ronenshh)) from the Wiz Research Team. We are a group of veteran white-hat hackers with a single goal: to make the cloud a safer place for everyone. We primarily focus on finding new attack vectors in the cloud and uncovering isolation issues in cloud vendors.

We would love to hear from you! Feel free to contact us on Twitter or via email: [research@wiz.io](mailto:research@wiz.io). 

Tags

[#Research](/blog/tag/research)[#Security](/blog/tag/security)[#Product & Company News](/blog/tag/news)
