---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-06-16_proofpoint-discovers-potentially-dangerous-microsoft-office-365-functionality-th.md
original_filename: 2022-06-16_proofpoint-discovers-potentially-dangerous-microsoft-office-365-functionality-th.md
title: Proofpoint Discovers Potentially Dangerous Microsoft Office 365 Functionality
  that can Ransom Files Stored on SharePoint and OneDrive
category: documents
detected_topics:
- mfa
- supply-chain
- oauth
- sso
- command-injection
- otp
tags:
- imported
- documents
- mfa
- supply-chain
- oauth
- sso
- command-injection
- otp
language: en
raw_sha256: 83216f618fbdde22b67349f1bdd0db824d70d202e640d8deeeda52d29bbd109d
text_sha256: 67cd440a85db1c3fa1cd747ea79517ba66b4e530b950fcb0e9b4c3f303f6b6dd
ingested_at: '2026-06-28T07:32:12Z'
sensitivity: unknown
redactions_applied: false
---

# Proofpoint Discovers Potentially Dangerous Microsoft Office 365 Functionality that can Ransom Files Stored on SharePoint and OneDrive

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-06-16_proofpoint-discovers-potentially-dangerous-microsoft-office-365-functionality-th.md
- Source Type: markdown
- Detected Topics: mfa, supply-chain, oauth, sso, command-injection, otp
- Ingested At: 2026-06-28T07:32:12Z
- Redactions Applied: False
- Raw SHA256: `83216f618fbdde22b67349f1bdd0db824d70d202e640d8deeeda52d29bbd109d`
- Text SHA256: `67cd440a85db1c3fa1cd747ea79517ba66b4e530b950fcb0e9b4c3f303f6b6dd`


## Content

---
title: "Proofpoint Discovers Potentially Dangerous Microsoft Office 365 Functionality that can Ransom Files Stored on SharePoint and OneDrive"
page_title: "Windows 365 SharePoint & OneDrive Security Risk Discovered | Proofpoint US"
url: "https://www.proofpoint.com/us/blog/cloud-security/proofpoint-discovers-potentially-dangerous-microsoft-office-365-functionality"
final_url: "https://www.proofpoint.com/us/blog/cloud-security/proofpoint-discovers-potentially-dangerous-microsoft-office-365-functionality"
authors: ["Proofpoint (@proofpoint)"]
programs: ["Microsoft"]
bugs: ["Logic flaw"]
publication_date: "2022-06-16"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 2545
---

[Blog](/us/blog)

[Data Security](/us/blog/data-security)

Proofpoint Discovers Potentially Dangerous Microsoft Office 365 Functionality that Can Ransom Files Stored on SharePoint and OneDrive 

![Ransomware](/sites/default/files/styles/image_768_300/public/blog-banners/pfpt-rw-blog-banner-1.jpg.webp?itok=B0HpExxN)

#  Proofpoint Discovers Potentially Dangerous Microsoft Office 365 Functionality that Can Ransom Files Stored on SharePoint and OneDrive 

Share with your network!

June 16, 2022 Or Safran, David Krispin, Assaf Friedman and Saikrishna Chavali 

Ransomware attacks have traditionally targeted data across endpoints or network drives. Until now, IT and security teams felt that cloud drives would be more resilient to [ransomware attacks](/us/threat-reference/ransomware "Ransomware"). After all, the now-familiar “AutoSave” feature, along with versioning and the good old recycle bin for files, should have been sufficient as backups. However, that may not be the case for much longer.

Proofpoint has discovered a potentially dangerous piece of functionality in Office 365 or Microsoft 365 that allows ransomware to encrypt files stored on Windows 365 SharePoint and OneDrive in a way that makes them unrecoverable without dedicated backups or a decryption key from the attacker.

Our research focused on two of the most popular enterprise cloud apps – SharePoint Online and OneDrive within the Microsoft 365 and Office 365 suites and shows that ransomware actors can now target organizations’ data in the cloud and launch attacks on cloud infrastructure.

### Cloud ransomware attack chain

#### The Attack Chain

Proofpoint has identified the attack chain and documented the steps below. Once executed, the attack [encrypts the files](/us/threat-reference/encryption "Encryption") in the compromised users’ accounts. Like with endpoint ransomware activity, those files can only be retrieved with decryption keys. OneDrive and SharePoint security measures should be enhanced to help prevent such attacks.

The actions outlined below can be automated using Microsoft APIs, command line interface (CLI) scripts and PowerShell scripts.

  1. **Initial Access** : Gain access to one or more users’ Windows 365 SharePoint Online or OneDrive accounts by compromising or hijacking users’ identities.
  2. **Account Takeover & Discovery**: The attacker now has access to any file owned by the compromised user or controlled by the third-party [OAuth application](/us/threat-reference/oauth "OAuth") (which would include the user’s OneDrive account as well).
  3. **Collection & Exfiltration**: Reduce versioning limit of files to a low number such as 1, to keep it easy. Encrypt the file more times than the versioning limit. With the example limit of 1, encrypt the file twice. This step is unique to cloud ransomware compared to the attack chain for endpoint-based ransomware. In some cases, the attacker may exfiltrate the unencrypted files as part of a double [extortion](/us/threat-reference/cyber-extortion "Cyber Extortion") tactic.
  4. **Monetization** : Now all original (pre-attacker) versions of the files are lost, leaving only the encrypted versions of each file in the cloud account. At this point, the attacker can ask for a ransom from the organization.

![Cloud ransomware attack chain diagram](/sites/default/files/inline-images/Screen%20Shot%202022-06-14%20at%203.55.33%20PM.png)

_Figure 1: Cloud ransomware attack chain diagram. The collection and exfiltration phase is unique to Microsoft environments._

### Lists and document libraries: Microsoft terms for storage containers inside SharePoint Online sites and OneDrive accounts

A [list](https://sharepointmaven.com/sharepoint-lists-vs-libraries/) is a Microsoft web part that stores content such as tasks, calendars, issues, photos, files and more within SharePoint Online. OneDrive accounts are used mainly to store documents.

Document library is the term most associated with OneDrive. A [document library](https://sharepointmaven.com/sharepoint-lists-vs-libraries/) is a special type of list on a Windows 365 SharePoint site or OneDrive account where you can upload, create, update, and collaborate on documents with team members.

The version settings for lists and document libraries are both found under list settings. In the cloud ransomware attack chain outlined earlier in this post, we describe the collection and exfiltration step. This is the point in the attack chain when the [malicious actor](/us/threat-reference/threat-actor "Threat Actor") modifies the list settings that will affect all files within the document library.

#### Document library versioning mechanism

Every document library in Windows 365 SharePoint Online and OneDrive has a user-configurable setting for numbers of saved versions. The site owner can change this setting, and they don’t need to hold an administrator role or associated privileges to do so. The versioning settings are under list settings for each document library.

![Versioning settings for document libraries](/sites/default/files/inline-images/Screen%20Shot%202022-06-14%20at%203.55.45%20PM.png)

_Figure 2: Versioning settings for document libraries. Link:_[_https://support.microsoft.com/en-us/office/enable-and-configure-versioning-for-a-list-or-library-1555d642-23ee-446a-990a-bcab618c7a37_](https://support.microsoft.com/en-us/office/enable-and-configure-versioning-for-a-list-or-library-1555d642-23ee-446a-990a-bcab618c7a37)

By design, when you reduce the document library version limit, any further changes to the files in the document library will result in older versions becoming very hard to restore. (For more on this topic, see the “Responsible disclosure and discussion” section at the end of this post.)

There are two ways to abuse the versioning mechanism to achieve malicious aims – creating too many versions of a file or reducing the version limits of a document library. Edits that increment a version of a file include changes to the document contents, filename, file metadata and the file encryption status.

The method of too many file versions created works as such:

  * **Staging** : Most OneDrive accounts have a default version limit of 500. An attacker could edit files within a document library 501 times. Now, the original (pre-attacker) version of each file is 501 versions old and, therefore, no longer restorable.
  * **Data encryption** : Encrypt the file(s) after each of the 501 edits. Now all 500 restorable versions are encrypted. Organizations cannot independently restore the original (pre-attacker) version of the files even if they attempt to increase version limits beyond the number of versions edited by the attacker. In this case, even if the version limit was increased to 501 or more, the file(s) saved 501 versions or older cannot be restored.

Encrypting files 500+ times is unlikely to be seen in the wild. It requires more scripting and more machine resources while making your operation easier to detect than the next method.

The method of reducing document library versioning works as such:

  * **Staging** : Reduce document library versioning number to a low number, such as 1, to keep it easy. This means only the most recent version of the file before the last edit is saved and can be restored by a user.
  * **Data Encryption** : Edit each file twice - either by encrypting the file twice or a combination of encryption, major content changes and file metadata changes. This will ensure an organization cannot restore the original (pre-attacker) versions of the file without the decryption key from the attacker.

Setting the version limit to zero is red herring and will not delete the versions. The versions will be available to the user in one simple step. Reset the version limit or manually switch it off and back on.

Files stored in a hybrid state on both endpoint and cloud, such as through cloud sync folders, will reduce the impact of these novel risks as the attacker won’t have access to the local and endpoint files. To perform a full ransom flow, the attacker will have to compromise the endpoint and the cloud account to access the endpoint and cloud-stored files.

### Initial access to SharePoint Online and OneDrive user accounts

The three most common paths attackers would take to gain access to one or more users’ Windows 365 SharePoint Online or OneDrive accounts are:

  * **Account compromise** : Directly compromising the users’ credentials to their cloud account(s) through [phishing](/us/threat-reference/phishing "Phishing"), [brute-force attacks](/us/threat-reference/brute-force-attack "Brute-Force Attack"), and other credential compromise tactics.
  * **Third-party OAuth applications** : Tricking a user to authorize third-party OAuth apps with application scopes for SharePoint or OneDrive access.
  * **Hijacked sessions** : Either hijacking the web session of a logged-in user or hijacking a live API token for SharePoint Online and/or OneDrive.

### Protecting your organization and sensitive data from actions leading to cloud ransomware

Fortunately, many of the recommendations outlined below should look similar to the OneDrive and SharePoint security best practices your organizations already would employ to deal with ransomware on endpoints. We will emphasize the differences when it comes to protecting your cloud environments.

First, turn on detection of risky file configuration changes for Office 365 accounts with [Proofpoint Cloud App Security Broker (CASB)](/us/products/cloud-security/cloud-app-security-broker "Cloud App Security Broker"). While a user can accidentally change the setting, it’s not common behavior. If users change it unknowingly, they should be made aware and ideally, increase the version limit. This will reduce the risk of an attacker compromising users and taking advantage of already low version limits for those users’ lists.

Second, improve security hygiene around ransomware. This includes addressing:

  * **Very Attacked People™** : Use [Proofpoint Targeted Attack Protection](/us/products/email-protection "Core Email Protection") (TAP) to identify and prioritize greater protection for users who face the highest number of and most threatening cloud, email, and web attacks. These users can be outside your list of very important people, such as executives and privileged users.
  * **Access management** : Maintain a [strong password policy](/us/blog/security-awareness-training/how-strong-my-password-guide-enable-your-employees-set-strong "How Strong Is My Password? A Guide to Enable Your Employees to Set Strong Passwords "), increase the use of [multi-factor authentication (MFA)](/us/threat-reference/multifactor-authentication "Multifactor Authentication"), and instill a least-privilege, principles-based access policy across cloud applications, like Windows 365 SharePoint and OneDrive.
  * **Disaster recovery and backup** : Update disaster recovery and data backup policies to reduce losses in case of a ransomware attack. Ideally, complete external backups of cloud files with sensitive data regularly. Don’t rely only on Microsoft to provide backups through versioning of document libraries.
  * **Cloud security** : Detect and remediate account compromises and third-party application abuse. Proofpoint CASB integrates with [Proofpoint Nexus Threat Graph](/us/solutions/combat-email-and-cloud-threats "Combat Email and Cloud Threats") and third-party threat intelligence to stop [account takeovers](/us/threat-reference/account-takeover-fraud "Account Takeover Fraud") and third-party application abuse.
  * **Data loss prevention** : Prevent sensitive data downloads and large-scale data downloads to unmanaged devices to reduce the potential for double-extortion tactics in ransomware. Proofpoint CASB provides customizable policies to help you protect your data on unmanaged devices. And [Proofpoint Insider Threat Management](/us/products/insider-threat-management "Contain Insider Threats") helps you teach negligent users better security practices and collect evidence on malicious insiders if they make configuration changes.

And finally, you may want to add the following to your response and investigation strategies in case the risky configurations’ change detectors are triggered:

  * Increase restorable versions for the affected document libraries in your M365 or O365 settings immediately.
  * Look for any previous account compromise or risky configuration change alerts for the affected Office 365 account.
  * Hunt for suspicious third-party app activity. If found, revoke OAuth tokens for malicious or unused third-party apps in the environment.
  * Identify other risky behavior patterns associated with the users(s) across cloud, email, web, and endpoint, such as negligence in handling sensitive data or risky data movement.

### Responsible disclosure and discussion

Prior to this blog, Proofpoint followed Microsoft’s disclosure path and received a couple of responses.

Their claims are as follows:

  * The configuration functionality for versioning settings within lists is working as intended
  * Older versions of files can be potentially recovered and restored for an additional 14 days with the assistance of Microsoft Support.

However, Proofpoint attempted to retrieve and restore old versions through this process (i.e., with Microsoft Support) and was not successful. Secondly, even if the versioning settings configuration workflow is as intended, Proofpoint has shown that it can be abused by attackers toward cloud ransomware aims.

For more information on how Proofpoint can protect against ransomware, visit [our Ransomware Hub](/us/ransomware-hub "Ransomware Hub").

[Previous Blog Post](/us/blog/insider-threat-management/how-recognize-malicious-insider-threat-motivations)

[Next Blog Post](/us/blog/dspm/security-data-in-the-cloud-is-hard-normalyze-makes-it-easier)

###  Subscribe to the Proofpoint Blog
