---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-08-23_by-design-how-default-permissions-on-microsoft-power-apps-exposed-millions.md
original_filename: 2021-08-23_by-design-how-default-permissions-on-microsoft-power-apps-exposed-millions.md
title: 'By Design: How Default Permissions on Microsoft Power Apps Exposed Millions'
category: documents
detected_topics:
- sso
- idor
- command-injection
- rate-limit
- automation-abuse
- information-disclosure
tags:
- imported
- documents
- sso
- idor
- command-injection
- rate-limit
- automation-abuse
- information-disclosure
language: en
raw_sha256: 68d36c8c9b09518763c302d27270d9cc5f8279a4a8913b8ae871bc2c2a1decc2
text_sha256: d27d7d1fdce90aec2715c73b83f2c4e875e97ed5ae5b77e2e52b3dd4f4c3a00a
ingested_at: '2026-06-28T07:32:07Z'
sensitivity: unknown
redactions_applied: false
---

# By Design: How Default Permissions on Microsoft Power Apps Exposed Millions

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-08-23_by-design-how-default-permissions-on-microsoft-power-apps-exposed-millions.md
- Source Type: markdown
- Detected Topics: sso, idor, command-injection, rate-limit, automation-abuse, information-disclosure
- Ingested At: 2026-06-28T07:32:07Z
- Redactions Applied: False
- Raw SHA256: `68d36c8c9b09518763c302d27270d9cc5f8279a4a8913b8ae871bc2c2a1decc2`
- Text SHA256: `d27d7d1fdce90aec2715c73b83f2c4e875e97ed5ae5b77e2e52b3dd4f4c3a00a`


## Content

---
title: "By Design: How Default Permissions on Microsoft Power Apps Exposed Millions"
page_title: "By Design: How Default Permissions on Microsoft Power Apps Exposed Millions | UpGuard"
url: "https://www.upguard.com/breaches/power-apps"
final_url: "https://www.upguard.com/breaches/power-apps"
authors: ["UpGuard Team (@upguard)"]
programs: ["Microsoft"]
bugs: ["Information disclosure"]
publication_date: "2021-08-23"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3396
---

Table of contents![Dropdown chevron](https://cdn.prod.website-files.com/5efbe6918a9cfd65bb1608f9/5f026c713863088144ffac1f_chevron%20down.svg)

##### Join 27,000+ cybersecurity newsletter subscribers  

The UpGuard Research team can now disclose multiple [data leaks](/blog/data-leak) resulting from Microsoft Power Apps portals configured to allow public access - a new vector of data exposure. The types of data varied between portals, including personal information used for COVID-19 contact tracing, COVID-19 vaccination appointments, social security numbers for job applicants, employee IDs, and millions of names and email addresses. UpGuard notified 47 entities of exposures involving personal information, including governmental bodies like Indiana, Maryland, and New York City, and private companies like American Airlines, J.B. Hunt, and Microsoft, for a total of 38 million records across all portals. This research presents an example of a larger theme, which is how to [manage third-party risks](https://www.upguard.com/blog/third-party-risk-management) (and exposures) posed by platforms that don't slot neatly into vulnerability disclosure programs as we know them today, but still present as security issues.  

Product documentation for Power Apps describes the conditions under which OData APIs can be made publicly accessible, and the main Power Apps marketing page lists the ability to access “your data either anonymously or through commercial authentication” as one of the top features. In cases like registration pages for COVID-19 vaccinations, there are data types that should be public, like the locations of vaccination sites and available appointment times, and [sensitive data](/blog/sensitive-data) that should be private, like the [personally identifying information](/blog/personally-identifiable-information-pii) of the people being vaccinated.  

The number of accounts exposing sensitive information, however, indicates that the risk of this feature– the likelihood and [impact of its misconfiguration](https://www.upguard.com/blog/security-misconfigurations-causing-data-breaches)– has not been adequately appreciated. On one hand, the product documentation accurately describes what happens if an app is configured in this way. On the other hand, empirical evidence suggests a warning in the technical documentation is not sufficient to avoid the serious consequences of misconfiguring OData list feeds for Power Apps portals. Our conversations with the entities we notified suggested the same conclusion: multiple governmental bodies reported performing security reviews of their apps without identifying this issue, presumably because it has never been adequately publicized as a [data security](https://www.upguard.com/blog/data-security) concern before. In publishing this report we aim to make other security practitioners aware of the risk associated with configuring OData APIs for Power Apps portals so that such exposures can be prevented in the future. 

  

![Microsoft support forum post](https://cdn.prod.website-files.com/5efc3ccdb72aaa7480ec8179/673d81d96ba512e5759da315_611f350efa9743e06ad198b6_odata_forums.png)

Confirmation by Microsoft support that OData API feeds can be configured for anonymous access

## Background

Microsoft [Power Apps](https://powerapps.microsoft.com/) are a product for making “low code”, cloud-hosted business intelligence apps. [Power Apps portals](https://powerapps.microsoft.com/en-us/portals/) are a way to create a public website to “give both internal and external users secure access to your data.” Users can create websites in the Power Apps UI with application capabilities like user authentication, forms for users to enter data, data transformation logic, storage of structured data, and APIs to retrieve that data by other applications. Portals provide a public website for interacting with those apps. Typically a business unit or polity uses a portal as an interface with a closely-related audience like customers, sales partners, employees, or citizens.

One of the options for Power Apps is to enable [OData](https://docs.microsoft.com/en-us/odata/) (Open Data Protocol) APIs for retrieving data from Power Apps [lists](https://docs.microsoft.com/en-us/powerapps/maker/portals/configure/entity-lists), which are the Power Apps configuration used to “expose records for display on portals.” Lists pull data from tables, and [limiting access to the list data that a user can see requires enabling Table Permissions](https://docs.microsoft.com/en-us/powerapps/maker/portals/configure/entity-lists#securing-lists). “To secure a list, you must configure Table Permissions for the table for which records are being displayed and also set the Enable Table Permissions Boolean value on the list record to true.” If those configurations are not set and the OData feed is enabled, anonymous users can access list data freely.

![Warning to enable table permissions for sensitive information](https://cdn.prod.website-files.com/5efc3ccdb72aaa7480ec8179/673d810ee96c77f713782e74_611f3653b367bc0d192e598b_odata%2520list%2520caution.png)

[Microsoft’s Power Apps Portals documentation](https://docs.microsoft.com/en-us/powerapps/maker/portals/configure/entity-lists#list-odata-feeds) warns that OData feeds are public if misconfigured

‍

Configuration options that allow a product to sometimes be used for data sharing and sometimes be used for storing sensitive data create the potential for data leaks. Power Apps portals have options built in for sharing data, but they also have built in data types that are inherently sensitive. In this case, we found four separate portals with lists called “msemr_appointmentemrset” used for storing information about people setting medical appointments, strongly suggesting this is a schema in the Power Apps catalog rather than one that separate users all came up with.

Power Apps Portals [lists](https://docs.microsoft.com/en-us/powerapps/maker/portals/configure/entity-lists) are created to display data from [tables](https://docs.microsoft.com/en-us/powerapps/maker/data-platform/entity-overview). These tables are stored within [Microsoft Dataverse](https://docs.microsoft.com/en-us/powerapps/maker/data-platform/data-platform-intro). When a developer enables the OData feed on the “OData Feed” list settings tab, they must also activate the “Enable Table Permissions” option on the “General” list settings tab unless they wish to make the OData feed public. This is due to all lists having table permissions disabled by default. Table permissions by default will in fact prevent anonymous data access, but lists ignore these permissions and any custom table permissions unless the developer activates table permissions for the list. 

At least, that was the state of Power Apps portals in June, 2021. As a result of this research project, Microsoft has since made changes to Power Apps portals such that table permissions are enabled by default. This report documents the steps that led to that change.

## Discovery

On May 24 2021, an UpGuard analyst first discovered that the OData API for a Power Apps portal had anonymously accessible list data including personally identifiable information. The owner of that application was notified and the data secured. That case led to the question of whether there were other portals with the same situation– the combination of configurations allowing lists to be accessed anonymously via OData feed APIs, and sensitive data collected and stored by the apps.  

First we identified the addresses of Power Apps portals. Power Apps portals are assigned a subdomain of the site “powerappsportals.com,” so using common subdomain enumeration techniques generated a list of customer portals. We also discovered two other primary domains used for similar Microsoft products with the same OData configuration options: powerappsportals.us, which appears to be for US governmental use, and microsoftcrmportals.com, which is for a deprecated version of the product line. Because these portals are intended for users to be able to access them over the internet– people are supposed to be able to find these sites easily– they are generally indexed by search engines, which provides another method for finding portals. That said, there may also be portals (or other Microsoft products with similar configuration options) that were not surfaced using these methods and that we are not aware of.  

After identifying the addresses for a significant number of portals, we then determined whether any OData lists were publicly accessible for each portal. If OData APIs were enabled, the lists were listed at the `_odata` endpoint. That is, for any given portal, you can determine whether OData lists are enabled by going to example.powerappsportals.com/_odata, and the lists would be displayed in your browser. Visiting the URL for a list would either display the data, if anonymous access was allowed, or show a message that access was forbidden, if some level of table permissions were enabled. The full URL would be something like example.powerappsportals.com/_odata/mylist, making it very easy to go from a list of portals to publicly accessible lists.  

Finally, we manually analysed the data to determine sensitivity, which led to the conclusion that there were many Power Apps portals with likely sensitive data. Given the number of portals, the limitations of our discovery methods, and the lack of existing public awareness concerning this issue, we thought the best course would be to disclose our findings as a vulnerability to Microsoft. They would have the technical access and personnel resources to audit all Power Apps portals (and potentially other products in the Power Platform) and notify the owners of those accounts before public disclosure. That seemed like the best possible outcome– all sensitive data secured followed by a public disclosure of the underlying issue– and so this was the first route we pursued.  

### Vulnerability disclosure to Microsoft

On Thursday, June 24, 2021, we submitted a [vulnerability](https://www.upguard.com/blog/vulnerability) report to the Microsoft Security Resource Center. The report included the steps to identify OData feeds that allowed anonymous access to list data and URLs for accounts that were exposing sensitive data. Among the examples of sensitive data exposed via OData APIs were three Power Apps portals used by American governmental entities to track COVID-19 tracing or vaccination and a portal with job applicant data including Social Security Numbers. We mentioned that these instances were examples of a broader pattern, with a significant number of Power Apps portals configured to allow anonymous access to lists and exposing PII as a result. The case was accepted by the automated MSRC process and a Microsoft analyst began investigating that day.

Over the next day we corresponded with the Microsoft analyst to clarify steps to reproduce and Microsoft’s relationship to the powerappsportals.com domain. On Tuesday June 29, the case was closed, and the Microsoft analyst informed us that they had “determined that this behavior is considered to be by design.”

![Response from Microsoft Security Response Center](https://cdn.prod.website-files.com/5efc3ccdb72aaa7480ec8179/673d810ee96c77f713782e77_6122f13493ad599cecc66585_microsoft%2520response.png)

Response from Microsoft Security Response Center

‍

### Notification to affected entities  

We had discovered over a thousand anonymously accessible lists across a few hundred portals that needed to be analyzed and potentially notified. Ideally, Microsoft would have been involved in doing so, but our attempt to pursue this option thus far had been unsuccessful– though Microsoft would later take action after we had notified some of the most severe exposures. We spent the next few weeks analysing the data for indicators of sensitivity and reaching out to affected organizations. The notification timelines and data classes for some of the most significant exposures are described below to give a sense of the prevalence and impact of this design decision.  

#### American Airlines

UpGuard notified American Airlines on July 2, 2021. By July 6, 2021, the data was secured. Collection “contacts” had 398,890 records which included full names, job titles, phone numbers, and email addresses. Collection “test” had 470,400 records which included full names, job titles, phone numbers, and email addresses.  

#### Denton County, TX

UpGuard sent an email to a Denton County email address related to administering COVID-19 information on July 2. On July 7, an UpGuard analyst called Denton county and spoke with someone who provided the email address for the IT department. The information about the exposed portal was re-sent to that address. The data was secured that day. The significant lists included “msemr_appointmentemrset” which had 632,171 records including vaccination types, appointment dates and times, employee IDs, full names, email addresses, phone numbers, and data of birth. The list “contactVaccinationSet” had 400,091 records with fields for full names and vaccination types, and “contactset” had 253,844 records with full names and email addresses.  

#### Ford

UpGuard notified Ford on July 9, 2021 of an exposure related to their dealer self-service portal. The collections included “systemusers” with 104,578 records, which had fields for full name, title, phone number, and “domainname,” which was typically an email addresses. Not all data was present for every record, but 101,895 records had “ford.com” email addresses. Manual analysis confirmed that the job title and name given in some records matched natural persons working for Ford. Other collections described cars being provided to dealerships for use as loaners.  

#### J.B. Hunt

UpGuard notified J.B. Hunt on July 2, 2021. Between July 6 and July 7, 2021 the data was secured. The collection “Contacts” had 905,228 records with fields for full names, email addresses, physical addresses, and phone numbers. 253,288 of these contact records contained data for the field “jbht_ssnid,” which was a number matching the format for a US Social Security Number and which contained numbers that have been issued as SSNs. Collection “drugscreen” had 51,028 records containing full names and drug tests dates and locations. The collection “systemusers” had 5,843 containing full names, email addresses, job titles, and phone numbers.

![Example record from J.B. Hunt collection.](https://cdn.prod.website-files.com/5efc3ccdb72aaa7480ec8179/673d810ee96c77f713782e7a_6123217984ddbab14c712988_jbhunt.png)

Example record from J.B. Hunt collection. Values for “jbht_ssnid” could be verified as actually issued SSNs

#### Maryland Department of Health

UpGuard notified the Maryland Department of Health on Friday, July 2, 2021. By July 6, 2021, the data was secured. Two lists contained personal information. List “msemr_appointmentemrset” had 280,410 records and included what appeared to be Covid-19 testing appointments containing the appointment date, time, and location, as well as the reference ID of the contact associated with the appointment. List “contactset” had 108,102 records with full names, email addresses, and in some cases phone numbers.  

#### New York City Municipal Transportation Authority and NYC Schools

UpGuard submitted a notification through the MTA’s [complaint form,](https://new.mta.info/customer-feedback) per the link to [email their Internet Privacy Compliance Officer](http://web.mta.info/mta/privacy2.htm) on their [Privacy Policy](https://new.mta.info/privacy-policy), on July 2. The automated response to that form stated it can take up to fifteen days to receive a response. On Friday, July 9 an UpGuard analyst called the publicly listed phone number for the MTA Corporate Office. After speaking with a person at the help desk, the call was directed to Business Services, so the analyst found an email address for MTA Business Services on a public website and sent an email notification to them. Later in the day on July 9, we received a response to the original submission saying they had forwarded it to Threat Intelligence. On Monday, July 12 the data was still available, so we sent notification to the Office of Information Technology Services for the State of New York. On Thursday July 15, an analyst spoke on the phone with an employee at the NYC Department of Information Technology whose contact information had been provided by a mutual friend. The DOIT employee provided the email address for the NYC [security operations center](https://www.upguard.com/blog/security-operations-center), and email notification was sent to that address. The exposed data was secured by the next day.  

An exposure for NYC Schools had a similar notification arc. Email notification was first sent on July 9 to a public email address for NYC Schools. UpGuard sent another email to a different address related to NYC Schools on July 12. The notification to the State of New York Office of Information Technology Services on July 12 also included the location of the NYC Schools exposure. Like with the MTA exposure, it was closed within a day of the email to the NYC SOC.  

The MTA portal had lists called “EmployeeEsa” with 78,865 records containing full names, DoB, email addresses, phone numbers, union membership, and work locations. “VaccinatedEmployees” with 63,706 records containing full names, vaccination dates, and vaccination types. Another list, “VaccineIntakes”, held 52,253 records containing full names, DoB, email addresses, phone numbers, and physical addresses.  

![Example record from New York City MTA collection](https://cdn.prod.website-files.com/5efc3ccdb72aaa7480ec8179/673d81d96ba512e5759da318_612321c8db1476dd9c97d0f4_mta.png)

Example record from New York City MTA collection

  

The portal belonging to the NYC Department of Education had a list called “contacts” with 412,220 records containing full names and district borough numbers, and a list called “Studentaccounts” with 291,955 records containing full names, usernames, district borough numbers, and email addresses for the “nycstudents.net” mail domain– likely the school-assigned email addresses for students, though it is difficult to verify the identities of minors with publicly available data.

### State of Indiana

Per [Indiana’s privacy policy](https://www.in.gov/core/privacy.html), UpGuard notified their designated “privacy coordinator,” Deputy Chief Technology Officer Mike White, on July 2.

![Details of the privacy coordinator for the State of Indiana](https://cdn.prod.website-files.com/5efc3ccdb72aaa7480ec8179/673d81fbb78a48c06e51b736_612322be95658648a867d634_indiana-privacy.jpeg)

Details of the privacy coordinator for the State of Indiana

‍

The notification email followed the same, standardized template that we use for all data exposure notifications, which has been reviewed by our attorneys at Fenwick and West and approved by the UpGuard board. This notification includes the information that the recipient needs to understand the location of the data, establish its relevance to them, understand why it is sensitive, and confirm that the data is publicly accessible. It also includes the clear statement that the notification is not a sales pitch or solicitation, and no compensation is expected.

![Notification email sent by UpGuard researcher to the State of Indiana's privacy coordinator](https://cdn.prod.website-files.com/5efc3ccdb72aaa7480ec8179/673d81fcb78a48c06e51b78e_61237ed76fbcedc0d719378a_Notification%2520email%2520sent%2520by%2520UpGuard%2527s%2520researcher%2520to%2520the%2520State%2520of%2520Indiana%2520privacy%2520coordinator.png)

Notification email sent by UpGuard researcher to the State of Indiana's privacy coordinator

‍

Public access to the data was removed between July 6 and July 7. On July 12, a member of the Indiana Department of Health responded and we began coordinating on the steps toward data deletion, which ultimately led to a conference call on August 2 with several members of the Indiana Department of Health (INDOH), including the Privacy Officer and CIO, and UpGuard’s VP of Product and General Counsel. During that call Indiana requested a copy of the data UpGuard had been able to download in order to confirm what data had been anonymously accessible. Because Power Apps was software as a service managed by Microsoft, the end users did not have direct access to logs needed to audit access, making a data replica particularly necessary. From conversations with personnel in Indiana and elsewhere, it is UpGuard’s understanding that Microsoft has provided logs to customers upon request so that they can audit access for reported cases of data exposure.  

On August 3 UpGuard and INDOH personnel worked together to securely transfer a replica of the datasets to Indiana’s SFTP server, as well as confirming that another collection named “vg_covid19interview” had been configured to deny anonymous access, and thus was not part of the data UpGuard downloaded. UpGuard also clarified when the download occurred. As late as August 6, the INDOH team did not know when the data had been downloaded, though the logs they obtained from Microsoft ultimately allowed them to confirm that no other parties had accessed the data.  

By August 11, both parties signed a declaration certifying the facts about the exposure. These facts are that the data was publicly exposed, the number of individuals affected, the types of data exposed, and that UpGuard had destroyed its copy of the data. The certificate of destruction was returned to UpGuard by the Privacy Officer of the Indiana DOH and signed by the CIO of the Indiana DOH.

![Certificate of destruction co-signed by the State of Indiana and UpGuard](https://cdn.prod.website-files.com/5efc3ccdb72aaa7480ec8179/673d81d96ba512e5759da31b_612325e4d9957ba3fde12c4d_COD%2520IDOH%2520and%2520UpGuard%252008112021%2520\(signed\).jpeg)

Certificate of destruction co-signed by UpGuard and the State of Indiana, confirming that Indiana misconfigured their Power Apps portal to allow public access to the underlying data

In one portal, the list “contact” had 747,980 records and the list “vg_covid19case” had 339,260. Between them, 749,618 individuals’ data was impacted. Another portal had a similar schema but much smaller quantities of data, and may have been an earlier iteration of the same functional site. The data in “vg_covid19case” included full names, county, date of birth. The list “contact” had full names, date of birth, some email addresses, home address, and phone number.  

On August 10, INDOH requested that UpGuard wait until at least August 20 before publishing any report while they completed their response process. Out of respect for the privacy of the individuals whose data was impacted, UpGuard complied with the timeline requested by INDOH.  

On August 17, the State of Indiana issued a [press release](https://events.in.gov/event/state_notifying_hoosiers_about_improper_access_of_contact_tracing_information) announcing this exposure and saying it would be notifying affected persons. The press release also included several misrepresentations about the nature of UpGuard’s actions. UpGuard’s Director of PR repeatedly attempted to reach Indiana’s designated media contact by phone in order to make them aware of how to correct those misrepresentations but received no response.  

The most significant of those misrepresentations are that UpGuard “improperly accessed” the data and that UpGuard performed this action to seek business from Indiana. As the attestation signed from the INDOH CIO shows, the system was misconfigured by the State of Indiana such that anonymous users were authorized to access the data. UpGuard did not exceed our authorized access, and while the data should not have been public, the nature of the data could only be ascertained by downloading and analyzing it.  

Second, there is no evidence to support the statement by Tracy Barnes, CIO for the state of Indiana, that UpGuard “intentionally looks for software vulnerabilities, then reaches out to seek business.” UpGuard’s notification email explicitly states the non-commercial nature of the notification. The conference call with the INDOH team and UpGuard was recorded by INDOH, and if Mr. Barnes wishes to release it, the recording will show that all questions about UpGuard’s commercial offerings were addressed only insomuch as to say we could not discuss commercial relations with an entity we have notified of a breach. The same goes for all email communication between UpGuard and Indiana. During five years of sending data breach notifications, UpGuard has never approached Indiana or any other company notified of a breach for business, and there is no merit to Mr. Barnes’ statement. On the contrary, UpGuard has provided hours of unremunerated support in service of Indiana Department of Health and the people it serves.

### Abuse report to Microsoft

During our initial canvass of Power Apps portals we discovered a few for groups at Microsoft. Analyzing those portals, however, led to the discovery on July 6 of the deprecated microsoftcrmportals.com domain. This domain had more apps created by Microsoft groups, some with very large collections of data. By July 9 we had completed some analysis of the accounts across the three domains and determined which were for Microsoft groups.  

We replied to the original email thread with the MSRC, thinking that would be the quickest way to get it in front of an analyst who could route it to the correct recipient. After no response, we opened a new case in the MSRC on July 13 and were informed on July 14 that we needed to submit an abuse report instead. On July 15 we submitted an abuse report with a list of all Power Apps and Microsoft CRM accounts we knew of that had Microsoft data. By Friday, July 16, the most serious exposure (a collection of 332,000 email addresses and employee IDs used for Microsoft’s global payroll services) was no longer public. By the following Monday, July 19, all but one of the remaining portals that were exposing personally identifiable information had removed public access for lists. 

The one portal not yet secured on that day was for the administration of selling [Azure China](https://docs.microsoft.com/en-us/azure/china/overview-operations) through 21Vianet. On July 20 we sent notification to 21Vianet by an email address listed on their website. On July 22 we sent another notification to an @microsoft.com email address listed on the support page for the portal. Within an hour a contractor working for Microsoft– their email domain was microsoft.com but their signature identified them as working for another company– had responded and the data was secured soon after.  

### Significant Microsoft portals

#### Global Payroll Services 

The Global Payroll Services Portal was a site for handling payroll questions from Microsoft’s global workforce, deprecated as of October 2020, when it was migrated to a newer version of the software. The list “contacts” had 332,000 records of people on the global payroll with their @microsoft.com email address, full name, phone numbers that appear to be for personal use, and employee id, their “ops_company,” and whether they are an “ops_vip.” The convention for naming a user in their email address also tacitly denotes whether they are a contractor or an employee of Microsoft proper. The list “Cases” had metadata about the employees’ questions like the ticket title– examples include "Wrong Salary has been deposited to my account" and "Payslip January 2017 - Clarification on Taxable Amount"– the ticket status, and the name of the person who worked on it.

![Example record for Microsoft Global Payroll Services collection](https://cdn.prod.website-files.com/5efc3ccdb72aaa7480ec8179/673d81d96ba512e5759da31e_61232ca6957f100e2f3c7fbd_microsoft%2520payroll.png)

Example record for Microsoft Global Payroll Services collection

  

#### Business Tools Support

There were two portals related to Business Tools Support. One had a list “Contact” with 45,810 records, with data including users’ full names and users’ @microsoft.com email addresses. Other lists in this portal included “Incidents” and “CasesSharedToContacts” that described service tickets. The other portal had the same lists and appeared to be an older version of the same site.  

#### Customer Insights Portal

A portal to “manage customer engagements and programs” had the list “Contacts” with 277,400 records that included full name and business email address. Many but not all of the email addresses were for the microsoft.com mail domain. The others were email addresses for users that could be identified as natural persons given their name and their employer’s mail domain. Other lists described what programs the contacts were involved in.  

#### Mixed Reality

Three portals related to Mixed Reality had similar lists. The most significant list was “contacts,” which contained 39,210 records for primarily non-Microsoft users, some of which had business email accounts and some of which were from personal email providers like Gmail or universities. The data present was the user’s full name, email address, and the name of their Microsoft liaison.  

#### Azure China

Many U.S. tech companies sell their products in China through resellers, and Azure China is the same. From Microsoft’s documentation: “[Microsoft Azure operated by 21Vianet](https://docs.microsoft.com/en-us/azure/china/overview-operations) (Azure China) is a physically separated instance of cloud services located in China. It's independently operated and transacted by Shanghai Blue Cloud Technology Co., Ltd. ("21Vianet"), a wholly owned subsidiary of Beijing 21Vianet Broadband Data Center Co., Ltd..” This portal, which had a Microsoft logo and a link to the Microsoft privacy policy in the footer, appeared to be the partner interface for managing the agreements between Microsoft and 21Vianet. There were several lists for the identities involved in different roles, with 1,264 entries in “AllContacts” with full name, role, and email address. The list “AllAgreements” had 7,936 entries, each of which described an agreement with the customer company name and the people involved in executing it. Some of the agreement metadata indicated they had been last modified as recently as June of 2021.

## Microsoft Response  

The process of notifying affected entities has resulted in ongoing conversations and visibility into Microsoft’s extended response. From those conversations we learned that Microsoft eventually did take follow up actions. At some point, Microsoft notified government cloud customers of this issue. We did not receive that notification, of course, but could observe its effect in that several lists for portals on powerappsportals.us that had been public in June were no longer public by the end of July.

Additionally, Microsoft has released a tool for checking Power Apps portals and planned changes to the product so that table permissions will be enforced by default. To diagnose configuration issues, the [Portal Checker](https://docs.microsoft.com/en-us/powerapps/maker/portals/admin/portal-checker-analysis) can be used to detect lists that allow anonymous access. More importantly, newly created Power Apps portals will have [table permissions enabled by default](https://docs.microsoft.com/en-us/powerapps/maker/portals/important-changes-deprecations#table-permission-changes-for-forms-and-lists-on-new-portals). Tables configurations can still be changed to allow for anonymous access, but defaulting to permissions enabled will greatly reduce the risk of future misconfiguration.

## Conclusion  

For several months the UpGuard Research team has worked to navigate a way toward the best resolution of Power Apps portals exposing personal data. We have now reached the end of that journey, and if we haven’t reached the best conclusion possible, we can at least comment on what we have learned.  

While we understand (and agree with) Microsoft’s position that the issue here is not strictly a software vulnerability, it is a platform issue that requires code changes to the product, and thus should go in the same workstream as vulnerabilities. It is a better resolution to change the product in response to observed user behaviors than to label systemic loss of data [confidentiality](/blog/cia-triad) an end user misconfiguration, allowing the problem to persist and exposing end users to the [cybersecurity risk](/blog/cybersecurity-risk) of a [data breach](/blog/data-breach). Ultimately, Microsoft has done the best thing they can, which is to enable table permissions by default and provided tooling to help Power Apps users self-diagnose their portals. One potential learning for platform operators is to take ownership of misconfiguration issues sooner, rather than leave third-party researchers to identify and notify all instances of such [cloud misconfigurations](https://www.upguard.com/blog/cloud-misconfiguration).  

Another improvement for software as a service operators like Microsoft is to improve end user visibility of access logs. Software as a service is convenient because it removes the need to administer the underlying infrastructure, but certain information from that infrastructure– most notably access logs– is crucial to executing [incident response plans](https://www.upguard.com/blog/incident-response-plan).  

For anyone who digitally processes sensitive information– that is, virtually all companies and government bodies– being prepared for a notification of a data leak or other incident will improve outcomes. In some cases, we struggled to get in contact with anyone who would remediate the issue. Providing a designated privacy contact on an easily searchable web page improves that part of the response process. Further, it must be an email address rather than a form. Researchers sometimes need evidence of their exact message to affected entities in order to refute baseless smears, and email messages provide a useful record for those cases.

Finally, technology leaders should have a general understanding of the phenomenon of data exposures. As more information is moved online, the frequency of sensitive data being made publicly available increases. It is and always has been legal to view public information, and the U.S. Supreme Court has solidified the basis for security researchers to work on information that allows anonymous access in _Van Buren v. United States_. Efforts to malign researchers cannot undo mistakes of the past, but they can deter those who would help in the future.

![UpGuard customer support team](https://cdn.prod.website-files.com/5efbe6918a9cfd65bb1608f9/60507100244040a33e906e5c_avatar-02.jpg)![UpGuard customer support team](https://cdn.prod.website-files.com/5efbe6918a9cfd65bb1608f9/605071006bd44f2563595a62_avatar-01.jpg)![UpGuard customer support team](https://cdn.prod.website-files.com/5efbe6918a9cfd65bb1608f9/60507100499c0d504686d69e_avatar-03.jpg)

## Protect your organization

Get in touch or book a free demo.

[Contact sales](/demo)[Free demo](/demo)

## Related breaches

Learn more about the latest issues in cybersecurity.

[![Social Insecurity: Billions of Social Security Number and Passwords](https://cdn.prod.website-files.com/5efc3ccdb72aaa7480ec8179/6994f9ebdebd7b040bd76721_photo-1770068511790-091e2c8cb382.avif)](/breaches/social-insecurity-billions-of-social-security-number-and-passwords)#### [Social Insecurity: Billions of Social Security Number and PasswordsUpGuard research found a trove of sensitive information in an exposed Elastic database. Getting to the bottom of what it meant led us down an interesting path. ](/breaches/social-insecurity-billions-of-social-security-number-and-passwords)

[![Greg Pollock](https://cdn.prod.website-files.com/5efc3ccdb72aaa7480ec8179/684cb5b99dd4f2d803858774_1678294813918%20\(2\).jpeg)](/team/greg-pollock)

[Greg Pollock](/team/greg-pollock)

February 18, 2026

[![Sixth Sense: GPS and AI Data Exposed for Assistive Devices](https://cdn.prod.website-files.com/5efc3ccdb72aaa7480ec8179/679bb90451075346ccd89ae0_iStock-1094966082%20\(1\).jpg)](/breaches/angelsense-data-leak)#### [Sixth Sense: GPS and AI Data Exposed for Assistive DevicesUpGuard can now report that it has secured an Elasticsearch database for AngelSense, a GPS tracker for children and adults with special needs.](/breaches/angelsense-data-leak)

[![UpGuard Team](https://cdn.prod.website-files.com/5efc3ccdb72aaa7480ec8179/68a3c6d5794807b22cd7303d_upguard-team-avatar-k.png)](/team/upguard)

[UpGuard Team](/team/upguard)

January 30, 2025

[![Stolen Data: National PTA Database Available on Dark Web](https://cdn.prod.website-files.com/5efc3ccdb72aaa7480ec8179/6643d27de4d8e52ec70b5d27_iStock-1317007945%20\(1\).jpg)](/breaches/pta-database)#### [Stolen Data: National PTA Database Available on Dark WebOn May 13th, UpGuard discovered a new set of data recently posted on a prominent dark web forum, this time allegedly belonging to the National Parent Teacher Association.](/breaches/pta-database)

[![UpGuard Team](https://cdn.prod.website-files.com/5efc3ccdb72aaa7480ec8179/68a3c6d5794807b22cd7303d_upguard-team-avatar-k.png)](/team/upguard)

[UpGuard Team](/team/upguard)

May 14, 2024

[![Student Applications: How an Education Software Company Exposed Millions of Files](https://cdn.prod.website-files.com/5efc3ccdb72aaa7480ec8179/619b358baac35fa43c3c1a9b_smarterselect-leak.jpg)](/breaches/smarterselect)#### [Student Applications: How an Education Software Company Exposed Millions of FilesUpGuard can now report that a public Google Cloud Storage bucket containing approximately 1.5 terabytes of data used to administer funding programs for college students has been secured. The bucket belonged to SmarterSelect, a company that provides software for managing the application process for scholarships, grants, and awards. The more than 2.8 million files included documents like transcripts, resumes, personal essays, tax returns, and invoices for approximately 1.2 million applications to funding programs.](/breaches/smarterselect)

[![UpGuard Team](https://cdn.prod.website-files.com/5efc3ccdb72aaa7480ec8179/68a3c6d5794807b22cd7303d_upguard-team-avatar-k.png)](/team/upguard)

[UpGuard Team](/team/upguard)

November 22, 2021

[![By Design: How Default Permissions on Microsoft Power Apps Exposed Millions](https://cdn.prod.website-files.com/5efc3ccdb72aaa7480ec8179/612367224277a4498eae9845_microsoft-powerapps-leak.jpg)](/breaches/power-apps)#### [By Design: How Default Permissions on Microsoft Power Apps Exposed Millions38 million records were exposed in multiple data leaks resulting from misconfigured Microsoft Power Apps portals. Data included sensitive information such as COVID-19 contact tracing data, COVID-19 vaccination appointments, social security numbers for job applicants, employee IDs, and millions of names and email addresses.](/breaches/power-apps)

[![UpGuard Team](https://cdn.prod.website-files.com/5efc3ccdb72aaa7480ec8179/68a3c6d5794807b22cd7303d_upguard-team-avatar-k.png)](/team/upguard)

[UpGuard Team](/team/upguard)

August 23, 2021

[![Florida County Database Mistake: Election Officials’ Logins Among Exposed Data](https://cdn.prod.website-files.com/5efc3ccdb72aaa7480ec8179/5f98e6edf6f61375a545f5f8_electoral-data-leak-martin-county-florida.jpg)](/breaches/martin-county-florida-election-officials-passwords)#### [Florida County Database Mistake: Election Officials’ Logins Among Exposed DataUpGuard can now disclose that an Amazon S3 storage bucket containing publicly exposed backups of systems representing the intranet and web presence for Martin County, Florida has been secured.](/breaches/martin-county-florida-election-officials-passwords)

[![UpGuard Team](https://cdn.prod.website-files.com/5efc3ccdb72aaa7480ec8179/68a3c6d5794807b22cd7303d_upguard-team-avatar-k.png)](/team/upguard)

[UpGuard Team](/team/upguard)

October 30, 2020

[View all breaches](/breaches)

![Deliver icon](https://cdn.prod.website-files.com/5efbe6918a9cfd65bb1608f9/5f9219c9a4e8b23a4d0b058f_mail.svg)

### Sign up for our newsletter

UpGuard's monthly newsletter cuts through the noise and brings you what matters most: our breaking research, in-depth analysis of emerging threats, and actionable strategic insights.

##### Free instant security score

## How secure is your organization?

Request a free cybersecurity report to discover key risks on your website, email, network, and brand.

  * ![Check icon](https://cdn.prod.website-files.com/5efbe6918a9cfd65bb1608f9/5f90d45fd9c6cf679c29d57f_check-icon.svg)

Instant insights you can act on immediately

  * ![Check icon](https://cdn.prod.website-files.com/5efbe6918a9cfd65bb1608f9/5f90d45fd9c6cf679c29d57f_check-icon.svg)

Hundreds of risk factors including email security, SSL, DNS health, open ports and common vulnerabilities

[Free score](/instant-security-score)

![Website Security scan results](https://cdn.prod.website-files.com/5efbe6918a9cfd65bb1608f9/5f4751771f3a1a19e07a1b13_webscanner-table.svg)![Website Security scan rating](https://cdn.prod.website-files.com/5efbe6918a9cfd65bb1608f9/5f475174c3a17f4dc2e5dbed_webscanner-rating.svg)
