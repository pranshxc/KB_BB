---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-12-06_microsoft-azure-portal-csv-injection.md
original_filename: 2021-12-06_microsoft-azure-portal-csv-injection.md
title: Microsoft Azure Portal – CSV Injection
category: documents
detected_topics:
- cloud-security
- sso
- access-control
- command-injection
- automation-abuse
tags:
- imported
- documents
- cloud-security
- sso
- access-control
- command-injection
- automation-abuse
language: en
raw_sha256: 9f011e5e4b57b597b27c314814fe2b113d0835382147983a754c7e11dce88966
text_sha256: 2fcf8635d2b7cf58ac95987bdaed85ac2abf12826dcc062dd2f8aac2faf33c1b
ingested_at: '2026-06-28T07:32:08Z'
sensitivity: unknown
redactions_applied: false
---

# Microsoft Azure Portal – CSV Injection

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-12-06_microsoft-azure-portal-csv-injection.md
- Source Type: markdown
- Detected Topics: cloud-security, sso, access-control, command-injection, automation-abuse
- Ingested At: 2026-06-28T07:32:08Z
- Redactions Applied: False
- Raw SHA256: `9f011e5e4b57b597b27c314814fe2b113d0835382147983a754c7e11dce88966`
- Text SHA256: `2fcf8635d2b7cf58ac95987bdaed85ac2abf12826dcc062dd2f8aac2faf33c1b`


## Content

---
title: "Microsoft Azure Portal – CSV Injection"
page_title: "Microsoft Azure Portal – CSV Injection - Y-Security GmbH"
url: "https://www.y-security.de/news-en/microsoft-azure-portal-csv-injection/index.html"
final_url: "https://www.y-security.de/news-en/microsoft-azure-portal-csv-injection/index.html"
authors: ["Christian Becker (@0xchrisb)"]
programs: ["Microsoft"]
bugs: ["CSV injection"]
publication_date: "2021-12-06"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3110
---

##  Microsoft Azure Portal – CSV Injection 

**Item** |  **Comment**  
---|---  
Software  |  Microsoft Azure Portal  
Version  |  [**https://portal.azure.com/**](https://portal.azure.com/)  
Type of Issue  |  CSV Injection / Formula Injection  
CWE  |  [**https://cwe.mitre.org/data/definitions/1236.html**](https://cwe.mitre.org/data/definitions/1236.html)  
OWASP  |  [**https://owasp.org/www-community/attacks/CSV_Injection**](https://owasp.org/www-community/attacks/CSV_Injection)  
Roles affected  |  All  
CVSS  |  **[Medium – 4.4](https://nvd.nist.gov/vuln-metrics/cvss/v3-calculator?vector=AV:N/AC:H/PR:L/UI:R/S:C/C:L/I:L/A:N&version=3.1)**  
Credits  |  [**Christian Becker**](https://twitter.com/0xchrisb) from Y-Security  
  
##  Summary 

Various Azure Active Directory components can be used to export displayed data in CSV format. A few components were identified in which the generated CSV values were found to be properly escaped. However, we also identified components in which data is not correctly escaped and therefore allows CSV Injection/Formula Injection. 

The vulnerability can be exploited by different user types and allows inserting data that can then be downloaded from any other user of the tenant. Final exploitation does not happen within Azure Portal, but in software opening/interpreting the CSV file, such as Microsoft Excel or LibreOffice Calc. Additional attack vectors cover inserting false data that when imported, e.g. when re-creating an Active Directory or automatically creating user on a system. 

##  Vulnerability Details 

We identified that CSV values are sometimes properly escaped. Therefore, we assume that the intended behavior is that downloaded CSV files should not allow CSV Injection/Formula Injection. The below table lists affected pages and URLs that were found to be accessible with the subscription used for testing. Please note, it is likely that additional injection points exist in the application and we have recommended Microsoft to review all CSV download/export functionalities. The following functions have been accessed: 

**Page** |  **Vulnerable to CSV Injection**  
---|---  
[**Users | All users (Preview)**](https://portal.azure.com/#blade/Microsoft_AAD_IAM/UsersManagementMenuBlade/MsGraphUsers) |  Yes  
[**Users | Sign-in logs**](https://portal.azure.com/#blade/Microsoft_AAD_IAM/UsersManagementMenuBlade/SignIns) |  No – Characters Escaped  
[**Users | Audit logs**](https://portal.azure.com/#blade/Microsoft_AAD_IAM/UsersManagementMenuBlade/Audit) |  No – Characters Escaped  
[**Users | Bulk operation results**](https://portal.azure.com/#blade/Microsoft_AAD_IAM/UsersManagementMenuBlade/UserBackgroundTasks) |  Yes  
[**Groups | All groups**](https://portal.azure.com/#blade/Microsoft_AAD_IAM/GroupsManagementMenuBlade/AllGroups) |  Yes  
[**Groups | Audit logs**](https://portal.azure.com/#blade/Microsoft_AAD_IAM/GroupsManagementMenuBlade/Audit) |  No – Characters Escaped  
[**Groups | Bulk operation results**](https://portal.azure.com/#blade/Microsoft_AAD_IAM/GroupsManagementMenuBlade/GroupBackgroundTasks) |  Yes  
[**Application administrator | Assignments**](https://portal.azure.com/#blade/Microsoft_AAD_IAM/ActiveDirectoryMenuBlade/RolesAndAdministrators) |  Yes  
[**Default Directory | Administrative units**](https://portal.azure.com/#blade/Microsoft_AAD_IAM/ActiveDirectoryMenuBlade/AdminUnit) |  Yes  
  
##  Steps to reproduce 

In the below example we have used a very basic payload, but we should note that it is also possible to execute operating system commands or exfiltrate content from the file . More details about payloads can be found in our previous post about **[Microsoft Teams – CSV Injection](../microsoft-teams-csv-injection/index.html)**. 

###  Proof of Concept: CSV Injection via User Details 

Both admin and non-admin users can download user lists from within the Azure AD Portal ([**ref**](https://docs.microsoft.com/en-us/azure/active-directory/enterprise-users/users-bulk-download)). In order to do this, the below steps need to be performed: 

  * Login to your organization and open the **[Users | All users (Preview)](https://portal.azure.com/#blade/Microsoft_AAD_IAM/UsersManagementMenuBlade/MsGraphUsers)** Blade 
  * Add a new user and set DisplayName, Firstname or LastName to a formula like “=3+1” (without quotes) 
  * The newly created user is now visible in the preview 
  * Click “Bulk operations” and “Download users” (**[ref](https://docs.microsoft.com/en-us/azure/active-directory/enterprise-users/users-bulk-download)**) and start the export 
  * Open “**[Bulk operations results](https://portal.azure.com/#blade/Microsoft_AAD_IAM/UsersManagementMenuBlade/UserBackgroundTasks\))** ” and wait for completion 
  * Download generated CSV file 

The generated CSV file would then look like the below showing that `=3+1` in line 3 was not properly escaped. 
  
  
  userPrincipalName,displayName,surname,mail,givenName,id,userType,jobTitle,department,accountEnabled,usageLocation,streetAddress,state,country,officeLocation,city,postalCode,telephoneNumber,mobilePhone,alternateEmailAddress,ageGroup,consentProvidedForMinor,legalAgeGroupClassification,companyName,creationType,directorySynced,invitationState,identityIssuer,createdDateTime
  MSOBBYSec_outlook.com#EXT#@MSOBBYSecoutlook.onmicrosoft.com,=1+3 MSOBB,MSOBB,,=1+3,7cc0c81b-f2a2-489a-8243-eda96da4214d,Member,,,True,DE,,,,,,,,,MSOBBYSec@outlook.com,,,,,,,,MSOBBYSecoutlook.onmicrosoft.com,8/19/2021 1:25:31 PM
  test12345@msobbysecoutlook.onmicrosoft.com,=3+1,=3+1,,=3+1,05f9eb61-470e-426c-b631-6db6bf429063,Member,,,True,,,,,,,,,,,,,,,,,,MSOBBYSecoutlook.onmicrosoft.com,8/19/2021 3:02:10 PM
  

##  Mitigation & Recommendation 

The vulnerability currently remains unfixed in Microsoft Azure Portal. Microsoft has asked to include the below statement: 

> We are working on defense in depth mitigation to ensure our customers are protected. 
> 
> MSRC 06.12.2021

We recommend to not allow Dynamic Data Exchange (DDE) in your data processor like Microsoft Excel or LibreOffice Calc. Additionally, we recommend to not use CSV exports generated by the Azure Portal for automated processing while the vulnerability remains unfixed. In general, it is recommended to surround characters by double quotes (” “) or always escape characters that can be used as part of a formula injection such as: 

  * Equals to (=) 
  * Plus (+) 
  * Minus (-) 
  * At (@) 
  * Comma (,) 
  * Tab (0x09) 
  * Line feed (0x0a) 
  * Carriage return (0x0D) 

##  Disclosure Policy 

At Y-Security we take security vulnerabilities seriously and follow a [**responsible disclosure policy**](../../disclosure-policy/index.html). The 90-day disclosure deadline was exceeded and therefore we decided to disclosure the vulnerability even though it remains unfixed. 

##  Disclosure Timeline 

****DATE**** |  ****COMMENT****  
---|---  
21.08.2021  |  Vulnerability Identification & Proof of Concept created  
21.08.2021  |  Vulnerability reported to Microsoft Security Response Center (MSRC)  
23.08.2021  |  MSRC requested Proof of Concept Video  
24.08.2021  |  Proof of Concept Video provided  
25.08.2021  |  MSRC Case 67001 was assigned  
15.09.2021  |  Update Requested from MSRC  
15.09.2021  |  MSRC confirmed the case is under investigation  
05.10.2021  |  Update Requested from MSRC  
05.10.2021  |  MSRC confirmed the case is under investigation  
19.11.2021  |  Disclosure Deadline of 90 days Hit  
29.11.2021  |  Informed MSRC about scheduled public disclosure at the 06/12/2021  
01.12.2021  |  MSRC asked for extension till end of December 2021  
01.12.2021  |  Request Declined  
06.12.2021  |  MSRC requested to include a statement regarding the vulnerability  
06.12.2021  |  Statement added to Mitigation & Recommendation  
06.12.2021  |  Coordinated Public Disclosure  
  
##  Read more articles 

[__# Previous Post Microsoft Teams – CSV Injection](../microsoft-teams-csv-injection/index.html)

[__# Next Post Looking at the Portswigger Burp Suite Certification](../looking-at-the-portswigger-burp-suite-certification/index.html)
