---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2024-02-20_security-vulnerabilities-in-apex-code-could-leak-salesforce-data.md
original_filename: 2024-02-20_security-vulnerabilities-in-apex-code-could-leak-salesforce-data.md
title: Security Vulnerabilities in Apex Code Could Leak Salesforce Data
category: documents
detected_topics:
- idor
- access-control
- command-injection
- automation-abuse
- business-logic
- api-security
tags:
- imported
- documents
- idor
- access-control
- command-injection
- automation-abuse
- business-logic
- api-security
language: en
raw_sha256: 55ac1d3f3e62fe2566f20bdcdf076a47143f433762198d13fdb320c33db6f2cb
text_sha256: ca7cf1d1d47f82bffd1797d405ba7cd70ecaa8788653123596982d6ddea1aa23
ingested_at: '2026-06-28T07:32:31Z'
sensitivity: unknown
redactions_applied: false
---

# Security Vulnerabilities in Apex Code Could Leak Salesforce Data

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2024-02-20_security-vulnerabilities-in-apex-code-could-leak-salesforce-data.md
- Source Type: markdown
- Detected Topics: idor, access-control, command-injection, automation-abuse, business-logic, api-security
- Ingested At: 2026-06-28T07:32:31Z
- Redactions Applied: False
- Raw SHA256: `55ac1d3f3e62fe2566f20bdcdf076a47143f433762198d13fdb320c33db6f2cb`
- Text SHA256: `ca7cf1d1d47f82bffd1797d405ba7cd70ecaa8788653123596982d6ddea1aa23`


## Content

---
title: "Security Vulnerabilities in Apex Code Could Leak Salesforce Data"
url: "https://www.varonis.com/blog/apex-code-vulnerabilities"
final_url: "https://www.varonis.com/blog/apex-code-vulnerabilities"
authors: ["Nitay Bachrach"]
bugs: ["Salesforce", "SOQL injection"]
publication_date: "2024-02-20"
added_date: "2024-02-27"
source: "pentester.land/writeups.json"
original_index: 419
---

Varonis Threat Labs identified high- and critical-severity vulnerabilities and misconfigurations in Apex, the Java-like programming language commonly used to customize Salesforce instances. 

Varonis researchers identified these Apex issues within multiple Fortune 500 companies and government agencies and reported the vulnerabilities to the affected organizations.

[Varonis Threat Labs](/blog/tag/threat-research?hsLang=en) cautions that these risks are not isolated to large organizations. Because Apex code is used in many "off-the-shelf" applications, organizations of all sizes across many industries are at risk. 

If exploited, the vulnerabilities can lead to data leakage, data corruption, and damage to business functions in Salesforce. That's why keeping track of Apex classes and their properties, who can execute them, and how they're used is vital.

Under the shared responsibility model, Salesforce customers, not Salesforce, are responsible for the security of the Apex code they implement. Because customers implement Apex, they also must fix vulnerable Apex classes, triggers, or code. 

## What is Apex? 

The Apex programming language lets users write their own code and logic. It's one of the most common tools used to customize Salesforce instances. Developers use the strongly typed, object-oriented language to execute flow and transaction control statements on the Salesforce Lightning Platform server in conjunction with calls to the Lightning Platform API.

Apex enables developers to add business logic to most system events — including button clicks, related record updates, and Visualforce pages —using syntax that looks like Java and acts like database-stored procedures. Apex code can be initiated by web service requests and from triggers on objects.

An Apex class is a template or blueprint used to create Apex objects. Classes include other classes, user-defined methods, variables, exception types, and static initialization code.

Apex powers many Salesforce functionalities, and it's what makes Salesforce so powerful and customizable — but this can also lead to vulnerabilities. 

## Apex vulnerabilities 

Apex code can run in two different modes: 

  1. "Without sharing" — This mode means that the Apex code ignores the user's permissions; the code can access any record and commit changes. 
  2. "With sharing" — This mode means that the Apex code respects the user's record-level permissions but still ignores object-level and field-level permissions. 

  
  
  public without sharing class Example{  
  
  // Code in this class will ignore the sharing mechanism and will be able to access otherwise inaccessible records.
  
  }   
  
  
  
  
  
  public with sharing class Example2{ 
  
  
  // Code in this class will respect the sharing mechanism and will only be able to access records the calling user can access. 
  
  } 

Apex classes that run "without sharing" — ignoring the user's permissions — are a powerful and important capability often required for proper functionality. However, with great power comes great responsibility. This mode increases risk and should be used carefully, especially when assigned to guests or external users.

Two of the most common risks of the "without sharing" mode are:

  1. Insecure direct object references (IDOR) can allow users to read or even exfiltrate full tables of data they should not be able to access. This could also lead to data integrity issues because a user could manipulate data or delete files and records belonging to other users. 
  2. Apex code can be vulnerable, just like any other programming language. This means that someone can use the code in an unintended way or provide specially crafted input to exploit vulnerabilities and mistakes in the code. Common examples include [SOQL injection and SOSL injection](https://developer.salesforce.com/docs/atlas.en-us.soql_sosl.meta/soql_sosl/sforce_api_calls_soql_sosl_intro.htm), which means the attacker can manipulate the query run by the class, changing the process flow and allowing data exfiltration.

Vulnerabilities and misconfigurations can have dire consequences. Many of the discovered vulnerabilities were assigned high and critical severity by the security teams at the affected organizations. 

## Abusing vulnerable Apex classes

In this example, we'll demonstrate how to retrieve data from a user's record without permission using vulnerable Apex classes. To safely demonstrate these vulnerabilities, VTL created a Salesforce environment based on real Apex code vulnerabilities they encountered. 

The first step is to perform reconnaissance. In this example, we'll retrieve data from a user's field, which we are titling "VerySecretFlag," but it could be phone numbers, social security numbers, or other sensitive data.

As mentioned in our previous research, "[Abusing Misconfigured Salesforce Communities for Recon and Data Theft](/blog/abusing-salesforce-communities?hsLang=en)," attackers can use the aura method _"aura://RecordUiController/ACTION$getObjectInfo"_ to get more information about users in a system. 

![Using the aura method, attackers can get user metadata from a system.](https://www.varonis.com/hs-fs/hubfs/Blog/Apex%20Code%20Vulnerabilities/583295678-blog_vtl-apexvulnerabilitiesinsalesforce_incopyimage-1_v1.png?width=2619&height=930&name=583295678-blog_vtl-apexvulnerabilitiesinsalesforce_incopyimage-1_v1.png)_Using the aura method, attackers can get user metadata from a system._

Among the fields is a custom one named "VerySecretFlag__c," but it's inaccessible because users can only retrieve their own data. Attempting actions — such as asking for the field "CreatedBy.VerySecretFlag__c" — does not return the field's value for other users. The guest user cannot read the value of other users' "VerySecretFlag." 

![583295685-blog_vtl-apexvulnerabilitiesinsalesforce_incopyimage-2_v1](https://www.varonis.com/hs-fs/hubfs/Blog/Apex%20Code%20Vulnerabilities/583295685-blog_vtl-apexvulnerabilitiesinsalesforce_incopyimage-2_v1.png?width=2585&height=843&name=583295685-blog_vtl-apexvulnerabilitiesinsalesforce_incopyimage-2_v1.png)_Aura calls are not enough to read the value of another user's data._

This means we need to read a value without having permission to do so. If we submit a form to create a case, we can see it calls the method _"apex://CaseCreationController/ACTION$createCaseR"_. 

A custom Apex class is assigned to the guest user with the "AuraEnabled" method, making it callable using Aura. Notice that we can name the fields we want the procedure to return. 

![583295693-blog_vtl-apexvulnerabilitiesinsalesforce_incopyimage-3_v1](https://www.varonis.com/hs-fs/hubfs/Blog/Apex%20Code%20Vulnerabilities/583295693-blog_vtl-apexvulnerabilitiesinsalesforce_incopyimage-3_v1.png?width=2538&height=1022&name=583295693-blog_vtl-apexvulnerabilitiesinsalesforce_incopyimage-3_v1.png)_Submitting a form reveals which type of Apex class is in use._

Interestingly, the returned case cannot be retrieved by any means other than Apex, including Aura. This means the guest user cannot otherwise access that record. This might suggest that the Apex class is running "without sharing." To retrieve the value of the "VerySecretFlag," an attacker needs a class configured to run without sharing.

As we observed earlier, we can name the fields we want to retrieve. So, if we want the secret flag, we can specify the field "CreatedBy.VerySecretFlag__c". By abusing the over-permissive class and the fact that we can specify fields to get fields of other objects, we can retrieve the value of "VerySecrectFlag."

![583295690-blog_vtl-apexvulnerabilitiesinsalesforce_incopyimage-3_v1-1](https://www.varonis.com/hs-fs/hubfs/Blog/Apex%20Code%20Vulnerabilities/583295690-blog_vtl-apexvulnerabilitiesinsalesforce_incopyimage-3_v1-1.png?width=2526&height=909&name=583295690-blog_vtl-apexvulnerabilitiesinsalesforce_incopyimage-3_v1-1.png)_An attacker can retrieve data with permission by naming which fields to retrieve and using a vulnerable Apex class._

## Reduce the blast radius. 

Apex is a crucial building block within Salesforce. To strengthen the security of your Salesforce instance, it's critical to review the different Apex classes you have, especially those that run "without sharing."

While this process can be done manually, it requires considerable time and effort.

To determine who can call an Apex class, you must check both Profiles and Permission Sets (as of Winter, if you click "Security" while reviewing the Apex class itself, you will only see Profiles, which is not enough to determine who can call an Apex class). To get started, navigate to the current app's Salesforce setup.

Then, you must expand the User section under Administration and select "Profiles."

Here's where it gets complicated. You first must click on each profile in the list and check what's in the "Enabled Apex Class Access" section along the top or by scrolling down to the "Enabled Apex Class Access" within the profile to view the rights. 

![583295707-blog_vtl-apexvulnerabilitiesinsalesforce_incopyimage-5_v1](https://www.varonis.com/hs-fs/hubfs/Blog/Apex%20Code%20Vulnerabilities/583295707-blog_vtl-apexvulnerabilitiesinsalesforce_incopyimage-5_v1.png?width=2595&height=608&name=583295707-blog_vtl-apexvulnerabilitiesinsalesforce_incopyimage-5_v1.png)_"Enabled Apex Class Access" must be reviewed for each profile._

You then need to check your Permissions Sets for each entry by clicking on them one by one and then scrolling down to the Apps section and looking for the Apex Class Access option. Review which users are assigned to the Profiles and Permission Sets, which will reveal which users can access those Apex Classes. 

![583295713-blog_vtl-apexvulnerabilitiesinsalesforce_incopyimage-6_v1](https://www.varonis.com/hs-fs/hubfs/Blog/Apex%20Code%20Vulnerabilities/583295713-blog_vtl-apexvulnerabilitiesinsalesforce_incopyimage-6_v1.png?width=1482&height=921&name=583295713-blog_vtl-apexvulnerabilitiesinsalesforce_incopyimage-6_v1.png)_Apex Class Access controls permissions for executing Apex Classes.___

Click on the Apex Class Access option to view the rights.

To see if the Apex class is configured to run "without sharing," you'll need to review the class's source code. Look for the class declaration (usually one of the first lines). If it contains the string "without sharing," the class will ignore shares and be able to access all records. 

![583295722-blog_vtl-apexvulnerabilitiesinsalesforce_incopyimage-7_v1](https://www.varonis.com/hs-fs/hubfs/Blog/Apex%20Code%20Vulnerabilities/583295722-blog_vtl-apexvulnerabilitiesinsalesforce_incopyimage-7_v1.png?width=720&height=294&name=583295722-blog_vtl-apexvulnerabilitiesinsalesforce_incopyimage-7_v1.png)_Each Apex Class must be edited individually to remediate this vulnerability._

This process can be labor intensive. However, Varonis customers can view access rights within the "posture" page under the relevant posture. You can easily find Apex classes using the filters (for example, the title contains "Apex") or scroll until you locate it. Under "affected resources," you'll see all the Apex classes running without sharing that guest users can execute. You can click on any Apex class to learn more, such as all the users that can execute that class. 

![583295735-blog_vtl-apexvulnerabilitiesinsalesforce_incopyimage-8_v1](https://www.varonis.com/hs-fs/hubfs/Blog/Apex%20Code%20Vulnerabilities/583295735-blog_vtl-apexvulnerabilitiesinsalesforce_incopyimage-8_v1.png?width=2873&height=1487&name=583295735-blog_vtl-apexvulnerabilitiesinsalesforce_incopyimage-8_v1.png)_Varonis customers can easily monitor Apex use with event monitoring._

With Event Monitoring enabled, you can see which guest, community, and internal users are calling the Apex methods and remove unnecessary permissions. Varonis also centralizes this event monitoring to provide a one-stop shop for total Salesforce coverage.

Lastly, validate that the Apex class was created safely.

Salesforce introduced many ways to secure your in-house code, such as a safe way to include user input in SOQL queries. 
  
  
  public class SOQLController {  
  
    public String name {   
  
        get { return name;}    
  
        set { name = value;}    
  
    }    
  
    public PageReference query() {  
  
        String queryName = '%' + name + '%'; 
  
        List<Contact> queryResult = [SELECT Id FROM Contact WHERE    
  
           (IsDeleted = false and Name like :queryName)];   
  
        // Alternatively, it is possible to use the function String.escapeSingleQuotes to sanitize the input   
  
        System.debug('query result is ' + queryResult);   
  
        return null;    
    }    
  }

Note the _":queryName_ _"_ syntax — this ensures the input cannot be used to inject SOQL. Avoid incorrect programming patterns such as:
  
  
  public class SOQLController { 
  
    public String name { 
  
        get { return name;}   
  
        set { name = value;}   
  
    }    
  
    public PageReference query() {   
  
        String qryString = 'SELECT Id FROM Contact WHERE (IsDeleted = false and Name like \'%' + name + '%\')';   
  
        List<Contact> queryResult = Database.query(qryString);   
  
        System.debug('query result is ' + queryResult);   
  
        return null;   
  
    }   
  
  }

When it is not possible to use Salesforce's safe input feature, for example, when users need to choose what fields they want to retrieve, you must sanitize the input.

Additionally, consider adding "WITH SHARING_ENFORCED" to your queries to enforce object- and field-level permissions. Note that adding "WITH SHARING_ENFORCED" only affects SELECT clauses and not WHERE clauses. 

The following function is insecure: 
  
  
  @AuraEnabled  
  
    public static List<Case> getCases(List<String> fields) {  
  
         // Build the SOQL query dynamically based on the specified fields   
  
        String query = 'SELECT ' + String.join(fields, ',') + ' FROM Case';   
  
     
  
        // Execute the query and return the list of cases   
  
        return Database.query(query);   
  
      }

It's vulnerable to SOQL injection and does not enforce security. 

We can secure the function by verifying the fields do not contain non-alphanumeric characters (or underscores) and add "WITH SECURITY_ENFORCED" to the query so users will only be able to query fields they have access to and only if they can access cases to begin with.
  
  
  @AuraEnabled  
  
    public static List<Case> getCases(List<String> fields) {   
  
        // Validate and sanitize the input fields to prevent SOQL injection   
  
        for (String field : fields) {   
  
            if (!isValidField(field)) {   
  
                throw new AuraHandledException('Invalid field name: ' + field);   
  
            }   
  
          }   
  
  
  
        // Build the SOQL query dynamically based on the specified fields   
  
          String query = 'SELECT ' + String.join(fields, ',') + ' FROM Case WITH SECURITY_ENFORCED';   
  
  
  
        // Execute the query and return the list of cases   
        return Database.query(query);   
  
      }   
  
  
  
    // Helper method to validate field names and prevent SOQL injection   
  
    private static Boolean isValidField(String field) {   
  
        // Allow alphanumeric characters and underscores, remove spaces and commas   
  
        return field != null && field.replaceAll('[^a-zA-Z0-9_]', '') == field;   
  
      }

A comprehensive security strategy should verify that Apex classes have been reviewed by security specialists, not only Salesforce developers and admins. This is usually the case for code that is part of an AppExchange package, but it's not always true for other non-AppExchange codes. This especially applies to in-house code, which is often neglected.

Vulnerable Apex classes can lead to data leakage and corruption. Because Salesforce customers are ultimately responsible for the security of the Apex code they implement, organizations must securely manage Apex classes and their properties, who can execute them, and how they're used.

Learn more about [how Varonis can help secure your Salesforce environment](/coverage/salesforce?hsLang=en). 

### What should I do now?

Below are three ways you can continue your journey to reduce data risk at your company:

1

[Schedule a demo with us](https://info.varonis.com/en/demo-request?hsLang=en "https://info.varonis.com/en/demo-request") to see Varonis in action. We'll personalize the session to your org's data security needs and answer any questions.

2

[See a sample of our Data Risk Assessment](https://www.varonis.com/hubfs/docs/DRA-sample.pdf?hsLang=en "https://info.varonis.com/hubfs/docs/DRA-sample.pdf?hsLang=en") and learn the risks that could be lingering in your environment. [Varonis' DRA](https://info.varonis.com/en/data-risk-assessment?hsLang=en "https://info.varonis.com/en/data-risk-assessment") is completely free and offers a clear path to automated remediation.

3

Follow us on[ LinkedIn](https://www.linkedin.com/company/varonis "https://www.linkedin.com/company/varonis"), [YouTube](https://www.youtube.com/channel/UCE9xUuH4lhIUDOFR1OHlNNg "https://www.youtube.com/channel/UCE9xUuH4lhIUDOFR1OHlNNg"), and [X (Twitter)](https://twitter.com/varonis "https://twitter.com/varonis") for bite-sized insights on all things data security, including DSPM, threat detection, AI security, and more.

![Nitay Bachrach](https://www.varonis.com/hubfs/nitay-bachrach.jpg)

Nitay Bachrach Nitay is a security researcher based in Tel Aviv, but you might encounter him anywhere in world. He is a cloud security expert, highly experienced in offensive security operations and reverse engineering. Nitay’s expertise also includes IoT devices, Linux, and local network security.
