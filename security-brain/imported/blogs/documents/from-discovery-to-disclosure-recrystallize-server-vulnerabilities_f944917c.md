---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2024-03-22_from-discovery-to-disclosure-recrystallize-server-vulnerabilities.md
original_filename: 2024-03-22_from-discovery-to-disclosure-recrystallize-server-vulnerabilities.md
title: 'From Discovery to Disclosure: ReCrystallize Server Vulnerabilities'
category: documents
detected_topics:
- command-injection
- path-traversal
- sso
- access-control
- file-upload
- api-security
tags:
- imported
- documents
- command-injection
- path-traversal
- sso
- access-control
- file-upload
- api-security
language: en
raw_sha256: f944917c708c0ea94dc3d08600eb3ce0890edb007e43e41d7a15c4445cbb0938
text_sha256: 433d7c6d548c38cea05727b0f5895e8dc487ab847bd34115fd232c516f57b7ee
ingested_at: '2026-06-28T07:32:32Z'
sensitivity: unknown
redactions_applied: false
---

# From Discovery to Disclosure: ReCrystallize Server Vulnerabilities

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2024-03-22_from-discovery-to-disclosure-recrystallize-server-vulnerabilities.md
- Source Type: markdown
- Detected Topics: command-injection, path-traversal, sso, access-control, file-upload, api-security
- Ingested At: 2026-06-28T07:32:32Z
- Redactions Applied: False
- Raw SHA256: `f944917c708c0ea94dc3d08600eb3ce0890edb007e43e41d7a15c4445cbb0938`
- Text SHA256: `433d7c6d548c38cea05727b0f5895e8dc487ab847bd34115fd232c516f57b7ee`


## Content

---
title: "From Discovery to Disclosure: ReCrystallize Server Vulnerabilities"
page_title: "SensePost | From Discovery to Disclosure: ReCrystallize Server Vulnerabilities"
url: "https://sensepost.com/blog/2024/from-discovery-to-disclosure-recrystallize-server-vulnerabilities/"
final_url: "https://sensepost.com/blog/2024/from-discovery-to-disclosure-recrystallize-server-vulnerabilities/"
authors: ["Paul van der Haas (@PvdH)"]
programs: ["ReCrystallize Software"]
bugs: ["Default credentials", "LFI", "Authentication bypass", "Privilege escalation", "Unrestricted file upload", "RCE"]
publication_date: "2024-03-22"
added_date: "2024-05-08"
source: "pentester.land/writeups.json"
original_index: 365
---

**TL &DR** – While on an assessment, I found an instance of ReCrystallize Server. It had many problems, some of which had to do with insufficient hardening on the client’s side while others were new vulnerabilities I found that when chained together, achieve Remote Code Execution (RCE). These vulnerabilities were disclosed to ReCrystallize Software and MITRE.

Besides the disclosed vulnerabilities, some “features” were also used for malicious purposes. The replication and validation of the findings were done on my own test environment.

This blog post was made public despite that there is no patch available (as far as I am aware of) due to a lack of reply from the vendor after multiple interactions.

**Hunting for vulnerabilities**

This blog post tells the tale of finding two vulnerabilities in ReCrystallize Server software. It started with a web application assessment that was not special in any way. The application in scope was meant for internal use only and the core application was kind of boring. This changed when the application threw some errors when I tried to print a report. Looking at the error is where the fun began!

The error showed that third-party software was used for printing reports. The third-party software was ‘ReCrystallize Server’ and was a standalone application.

[![](/img/pages/blog/2024/from-discovery-to-disclosure-recrystallize-server-vulnerabilities/4a47a0db6e60853dedfcfdf08a5ca249.png)](/img/pages/blog/2024/from-discovery-to-disclosure-recrystallize-server-vulnerabilities/4a47a0db6e60853dedfcfdf08a5ca249.png)

I had never heard of this software before and assumed it had something to do with SAP Crystal Reports. From here, I could follow the road in 2 directions. The one direction was to read the documentation and find known vulnerabilities for this software, and the other direction was to hit the login and see what would happen. My curiosity was triggered, so I just smashed the Log In button.

[![](/img/pages/blog/2024/from-discovery-to-disclosure-recrystallize-server-vulnerabilities/fb5c81ed3a220004b71069645f112867.png)](/img/pages/blog/2024/from-discovery-to-disclosure-recrystallize-server-vulnerabilities/fb5c81ed3a220004b71069645f112867.png)

Credentials like ‘admin/admin’ or ‘admin/password’ did not work, so back to direction number one. Let’s look for known vulnerabilities.

[![](/img/pages/blog/2024/from-discovery-to-disclosure-recrystallize-server-vulnerabilities/10fb15c77258a991b0028080a64fb42d.png)](/img/pages/blog/2024/from-discovery-to-disclosure-recrystallize-server-vulnerabilities/10fb15c77258a991b0028080a64fb42d.png)

The first hit was a bit misleading as the subject was not about vulnerabilities. Are there any known CVEs perhaps?

[![](/img/pages/blog/2024/from-discovery-to-disclosure-recrystallize-server-vulnerabilities/09dd8c2662b96ce14928333f055c5580.png)](/img/pages/blog/2024/from-discovery-to-disclosure-recrystallize-server-vulnerabilities/09dd8c2662b96ce14928333f055c5580.png)

It seems that this application is completely secure. As it often happens on assessments, I was short on time. So, let’s skip it right?

In the image above you see a search result referring to an [installation guide](https://www.recrystallize.com/merchant/ReCrystallize%20Server%20Installation%20and%20Administration.pdf). Perhaps some juicy information is disclosed in there, so I decided to have a look. This was not a wrong decision!

[![](/img/pages/blog/2024/from-discovery-to-disclosure-recrystallize-server-vulnerabilities/8266e4bfeda1bd42d8f9794eb4ea0a13.png)](/img/pages/blog/2024/from-discovery-to-disclosure-recrystallize-server-vulnerabilities/8266e4bfeda1bd42d8f9794eb4ea0a13.png)

Ok… My short list with default passwords did not work at first, but surely the password is not really ‘pw’? It actually was.

[![](/img/pages/blog/2024/from-discovery-to-disclosure-recrystallize-server-vulnerabilities/4ccc4eeff91df1a4d4789ba5a73762fb.png)](/img/pages/blog/2024/from-discovery-to-disclosure-recrystallize-server-vulnerabilities/10fb15c77258a991b0028080a64fb42d.png)

System Info, Settings, Manage Files…. I can smell it already, an over privileged process probably! The first thing I could think about was uploading a web shell within ‘Manage Files’. Unfortunately, the functionality was not working since there was no license present. Next would be ‘System Info’ to gather some information about the system.

[![](/img/pages/blog/2024/from-discovery-to-disclosure-recrystallize-server-vulnerabilities/9eb9cd58b9ea5e04c890326b5c1f471f.png)](/img/pages/blog/2024/from-discovery-to-disclosure-recrystallize-server-vulnerabilities/9eb9cd58b9ea5e04c890326b5c1f471f.png)

Let’s have a look at what could be important. Based on this information we know that the application runs on the system drive (C:). This is useful to know for command execution payloads or Local File Inclusion (LFI) vulnerabilities. The process is running as ‘NT AUTHORITY\SYSTEM’, which is a local account with the highest privileges. We also now know where ReCrystallize Server is installed and therefore would be able to find out where files are going to be stored. In this example you are also able to see that the server is domain joined (no this is not a client domain as I made an effort to set up a lab environment).

You might remember the ‘Settings’ button being present as an administrator function. A lot of options were present under settings such as configuring database credentials, configuring SMTP server settings, etc. None of them were configured, but I wanted to highlight one setting.

[![](/img/pages/blog/2024/from-discovery-to-disclosure-recrystallize-server-vulnerabilities/09dd8c2662b96ce14928333f055c5580.png)](/img/pages/blog/2024/from-discovery-to-disclosure-recrystallize-server-vulnerabilities/09dd8c2662b96ce14928333f055c5580.png)

As the admin user, I was able to allow the use of absolute paths. This seemed like an important setting for me, but later in this post you will find out that it really is not. This looks like the start of Local File Inclusion.

The installation manual I mentioned earlier showed this:

[![](/img/pages/blog/2024/from-discovery-to-disclosure-recrystallize-server-vulnerabilities/7afbb1602613ec52b265d7a54ad27330.png)](/img/pages/blog/2024/from-discovery-to-disclosure-recrystallize-server-vulnerabilities/7afbb1602613ec52b265d7a54ad27330.png)

Apparently, the application can view the contents of a folder specified in the ‘folderName’ parameter. Since I allowed absolute paths, let’s see the functionality in action.

[![](/img/pages/blog/2024/from-discovery-to-disclosure-recrystallize-server-vulnerabilities/586e508f161f26ce94633729ac56c602.png)](/img/pages/blog/2024/from-discovery-to-disclosure-recrystallize-server-vulnerabilities/586e508f161f26ce94633729ac56c602.png)

Sweet, I can see the contents of ‘C:\Program Files (x86)’. I just wished there was a way to get the files instead of folders. While playing around with the application and crawling through the manual, I was able to download files from the server.

[![](/img/pages/blog/2024/from-discovery-to-disclosure-recrystallize-server-vulnerabilities/59b2900aa03cb2182a51cdb520b535b6.png)](/img/pages/blog/2024/from-discovery-to-disclosure-recrystallize-server-vulnerabilities/59b2900aa03cb2182a51cdb520b535b6.png)

I exploited this a bit to get access to network shares, extract information regarding the associated Active Directory environment and got database credentials. 

Although I was not able to upload a web shell, I was happy with it and ready to notify the client. As if it was written in the almighty guidelines of system administrators, the reaction was:

“You were only able to do that because we did not configure it. After hardening the configuration, this would not be possible anymore”

[![](/img/pages/blog/2024/from-discovery-to-disclosure-recrystallize-server-vulnerabilities/3b475ad36bb5b6ef2294ce496c3ba2cd.png)](/img/pages/blog/2024/from-discovery-to-disclosure-recrystallize-server-vulnerabilities/3b475ad36bb5b6ef2294ce496c3ba2cd.png)

Hmm, challenge accepted then. The next morning, I was able to retest the findings on the ‘hardened’ configuration of ReCrystallize Server.

For the ones that watched Top Gear with James May, “Bollocks”! The default password was of course changed, the use of absolute paths was disabled. This shouldn’t be happening!

**CVE-2024-26331**  
Luckily, I took a note of some strange behaviour before the client reconfigured the ReCrystallize Server. On some occasions, the session of the core application expired but I was able to continue in the third-party software ReCrystallize Server. I also noted a cookie being set only for ReCrystallize Server, namely ‘AdminUsername=admin’.

[![](/img/pages/blog/2024/from-discovery-to-disclosure-recrystallize-server-vulnerabilities/c00b57557743e709b8b96933432e0dfa.png)](/img/pages/blog/2024/from-discovery-to-disclosure-recrystallize-server-vulnerabilities/c00b57557743e709b8b96933432e0dfa.png)

Let’s try to access the admin functionality without and with the cookie being set.

[![](/img/pages/blog/2024/from-discovery-to-disclosure-recrystallize-server-vulnerabilities/7b6fbd4c592d356e087a0f1053751007.png)](/img/pages/blog/2024/from-discovery-to-disclosure-recrystallize-server-vulnerabilities/7b6fbd4c592d356e087a0f1053751007.png) [![](/img/pages/blog/2024/from-discovery-to-disclosure-recrystallize-server-vulnerabilities/d642f8c3d2d6c1ab174d170d2dc8ed78.png)](/img/pages/blog/2024/from-discovery-to-disclosure-recrystallize-server-vulnerabilities/d642f8c3d2d6c1ab174d170d2dc8ed78.png) [![](/img/pages/blog/2024/from-discovery-to-disclosure-recrystallize-server-vulnerabilities/1e412544122065c25107eadecd8208c7.png)](/img/pages/blog/2024/from-discovery-to-disclosure-recrystallize-server-vulnerabilities/1e412544122065c25107eadecd8208c7.png)

Nice, I have administrative access again!

**CVE-2024-28269**  
With a license now present, it was possible to use the ‘Manage Files’ feature. This happened to be a way to upload files without restrictions. Unrestricted File Upload? Let’s get RCE!

Uploading a default ASPX web shell would probably raise an alert. We could do obfuscation and all other kinds of tricks. Instead, I wanted to keep things simple when I searched for an appropriate web shell on the Internet. I created 2 files, report.aspx and report.aspx.cs, where accessing report.aspx would execute the code in Report.aspx.cs. In this case I simply executed the `systeminfo` command.

[![](/img/pages/blog/2024/from-discovery-to-disclosure-recrystallize-server-vulnerabilities/c9baca3cda1c39194c04fe2170c3da65.png)](/img/pages/blog/2024/from-discovery-to-disclosure-recrystallize-server-vulnerabilities/c9baca3cda1c39194c04fe2170c3da65.png)

Content of report.aspx:
  
  
  <%@ Page Language="C#" AutoEventWireup="true" CodeFile="report.aspx.cs" Inherits="Report.Template" %>
  
  <!DOCTYPE html>
  <html>
  <head>
  <title>Report Template</title>
  </head>
  <body>
  <h1>Report Results:</h1>
  <pre><asp:Literal runat="server" ID="ReportOutput" EnableViewState="false" /></pre>
  </body>
  </html>

Content report.aspx.cs:
  
  
  using System;
  using System.Diagnostics;
  
  namespace Report
  {
  public partial class Template : System.Web.UI.Page
  {
  protected void Page_Load(object sender, EventArgs e)
  {
  // Set up process info
  var processStartInfo = new ProcessStartInfo
  {
  FileName = "cmd.exe",
  Arguments = "/c systeminfo", // Replace with your desired target
  RedirectStandardOutput = true,
  UseShellExecute = false,
  CreateNoWindow = true
  };
  
  // Start the process
  using (var process = new Process { StartInfo = processStartInfo })
  {
  process.Start();
  string output = process.StandardOutput.ReadToEnd();
  process.WaitForExit();
  
  // Display the output on the web page
  ReportOutput.Text = output;
  }
  }
  }
  }

The image below shows the result of calling report.aspx.

[![](/img/pages/blog/2024/from-discovery-to-disclosure-recrystallize-server-vulnerabilities/88399fdcf82e54c15ebbaabe86ff3e5e.png)](/img/pages/blog/2024/from-discovery-to-disclosure-recrystallize-server-vulnerabilities/88399fdcf82e54c15ebbaabe86ff3e5e.png)

This was extremely fun, and the client was happy and amazed with the results. The fact that I only needed to place a specific cookie blew their mind. In agreement with the client, I disclosed the vulnerability to ReCrystallize Software.

**Side quests**  
As mentioned in the beginning, there are some “features” that could be abused. An example was already given, namely the retrieval of files using absolute paths. Multiple parameters could be used for calling UNC paths, even when the tick-box regarding the use of absolute paths is turned off. An SMB request was sent out to my attacker system running [Responder](https://github.com/lgandx/Responder).

[![](/img/pages/blog/2024/from-discovery-to-disclosure-recrystallize-server-vulnerabilities/ba6beb7ae28ef0a97d7a0a038feb5060.png)](/img/pages/blog/2024/from-discovery-to-disclosure-recrystallize-server-vulnerabilities/ba6beb7ae28ef0a97d7a0a038feb5060.png) [![](/img/pages/blog/2024/from-discovery-to-disclosure-recrystallize-server-vulnerabilities/079f4fb55b755f6f198bee97d7c95390.png)](/img/pages/blog/2024/from-discovery-to-disclosure-recrystallize-server-vulnerabilities/079f4fb55b755f6f198bee97d7c95390.png)

The request shown above was executed while not being unauthenticated. It also turned out that the download of files could have been done unauthenticated…

[![](/img/pages/blog/2024/from-discovery-to-disclosure-recrystallize-server-vulnerabilities/7134f8f5aced525d1c11d229063305e7.png)](/img/pages/blog/2024/from-discovery-to-disclosure-recrystallize-server-vulnerabilities/7134f8f5aced525d1c11d229063305e7.png)

Even when the usage of absolute paths is disabled, you could still get the files. Below is just an example of a way to download system files without authentication.

[![](/img/pages/blog/2024/from-discovery-to-disclosure-recrystallize-server-vulnerabilities/75c168b671d4ce827fca23907d85f114.png)](/img/pages/blog/2024/from-discovery-to-disclosure-recrystallize-server-vulnerabilities/75c168b671d4ce827fca23907d85f114.png) [![](/img/pages/blog/2024/from-discovery-to-disclosure-recrystallize-server-vulnerabilities/7ae5e99a8c2f19cd25f44313293553aa.png)](/img/pages/blog/2024/from-discovery-to-disclosure-recrystallize-server-vulnerabilities/7ae5e99a8c2f19cd25f44313293553aa.png)

The image below shows that it is also still possible to send an outbound SMB request.

[![](/img/pages/blog/2024/from-discovery-to-disclosure-recrystallize-server-vulnerabilities/2484a7df36877a14689574eebda6dd7c.png)](/img/pages/blog/2024/from-discovery-to-disclosure-recrystallize-server-vulnerabilities/2484a7df36877a14689574eebda6dd7c.png)

**Recommendations**  
There is a lot that can be said about this software. In general, ReCrystallize Software should patch the issues mentioned above. As you’d see in the disclosure timeline, that did not go as well as one would hope for, and two years later there still is no formal patch these issues. In the meantime, if you need this application, you should isolate the server /service as much as possible making it only available to users who need it.

When a patch is available, the application itself should be hardened by making sure that absolute paths are not allowed, the default password is changed and encryption is turned on.

Also, do not forget to harden the underlying web server by keeping it up-to-date and making sure the principle of least privilege principle is applied. It is also recommended that you block outbound SMB traffic.

**Disclosure Timeline**  
General note: Due to the pandemic and the amount of other work, the disclosure timeline is a bit lengthier than I wanted. I also learned that requesting a CVE should have been done earlier..

08-09-2022 – Disclosure of authentication bypass and unrestricted file upload vulnerabilities to ReCrystallize Software.  
12-09-2022 – Vulnerabilities were accepted by ReCrystallize Software, expected patch in the next major release.  
15-11-2022 – Expected patch date moved to December 2022 or January 2023.  
01-03-2023 – Requested a status update, but no response.  
10-07-2023 – Requested a status update, but no response.  
15-02-2024 – Requested a CVE from MITRE for the authentication bypass.  
19-02-2024 – CVE-2024-26331 was reserved.  
19-02-2024 – Notified ReCrystallize Software about the reserved CVE and upcoming publication.  
19-02-2024 – Request to MITRE to add another CVE for the Unrestricted File Upload.  
14-03-2024 – CVE-2024-28269 was reserved.  
14-03-2024 – Notified ReCrystallize Software about the reserved CVE and a reminder about publication.  
14-03-2024 – Notified an organization that had an instance of ReCrystallize Server available online.
