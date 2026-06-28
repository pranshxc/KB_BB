---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2024-05-02_poppin-shells-with-okta-verify-on-windows.md
original_filename: 2024-05-02_poppin-shells-with-okta-verify-on-windows.md
title: Poppin shells with Okta Verify on Windows
category: documents
detected_topics:
- command-injection
- supply-chain
- sso
- access-control
- mfa
- otp
tags:
- imported
- documents
- command-injection
- supply-chain
- sso
- access-control
- mfa
- otp
language: en
raw_sha256: e1828fbf7435f817b4050a6fc4264a0f8abb46522a714ebfca384bd7576bcd12
text_sha256: 6e930941b8edbb14a4ebce013d99e6e66a5b672b5ad9183c8085e94fdfb6c4d1
ingested_at: '2026-06-28T07:32:33Z'
sensitivity: unknown
redactions_applied: false
---

# Poppin shells with Okta Verify on Windows

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2024-05-02_poppin-shells-with-okta-verify-on-windows.md
- Source Type: markdown
- Detected Topics: command-injection, supply-chain, sso, access-control, mfa, otp
- Ingested At: 2026-06-28T07:32:33Z
- Redactions Applied: False
- Raw SHA256: `e1828fbf7435f817b4050a6fc4264a0f8abb46522a714ebfca384bd7576bcd12`
- Text SHA256: `6e930941b8edbb14a4ebce013d99e6e66a5b672b5ad9183c8085e94fdfb6c4d1`


## Content

---
title: "Poppin shells with Okta Verify on Windows"
page_title: "Okta Verify for Windows Remote Code Execution – CVE-2024-0980 – Securifera"
url: "https://www.securifera.com/blog/2024/05/02/okta-verify-for-windows-remote-code-execution-cve-2024-0980/"
final_url: "https://www.securifera.com/blog/2024/05/02/okta-verify-for-windows-remote-code-execution-cve-2024-0980/"
authors: ["b0yd (@rwincey)"]
programs: ["Okta"]
bugs: ["RCE", "DLL Hijacking", "Local Privilege Escalation"]
bounty: "13,337"
publication_date: "2024-05-02"
added_date: "2024-07-15"
source: "pentester.land/writeups.json"
original_index: 310
---

Okta Verify for Windows Remote Code Execution – CVE-2024-0980

![](https://www.securifera.com/wp-content/uploads/2024/04/okta_blog_small.jpg)

### **This article is in no way affiliated, sponsored, or endorsed with/by Okta, Inc. All graphics are being displayed under fair use for the purposes of this article.**

## Poppin shells with Okta Verify on Windows

### These days I rarely have an opportunity to do bug hunting. Fortunately, over the holiday break, I found some free time. This started as it usually does with me looking at what software was running on my computer.

![](https://www.securifera.com/wp-content/uploads/2024/04/okta_icon.png)

### A while back I had installed Okta Verify on my Windows box as it was required for some “enhanced” 2FA that I was required to have to access a thing. Months later it sat there doing whatever it does. I googled to see if Okta had a bug bounty program because even though I had some time, it’d be nice to get paid if I found a thing. I was thrilled to find that Okta had a bug bounty with Bugcrowd, Okta Verify is in it, and the payouts look good, almost **_too_ **good.

![](https://www.securifera.com/wp-content/uploads/2024/04/bounties.jpg)

### I started with my usual bug hunting flow when approaching a random Windows service. This typically includes looking for the usual low hanging fruit. A good article for the types of things to look for can be found [here](https://itm4n.github.io/windows-dll-hijacking-clarified/).

### Firing up Sysinternal’s Procmon, I saw there is a service called Okta.Coordinator.Service that is running as SYSTEM. Without going into the details _(**namely because Okta hasn’t fixed it or issued it a CVE**), _I found a thing. I submitted the report and was promptly paid.

![](https://www.securifera.com/wp-content/uploads/2024/04/okta_bug.png)

### Well that’s weird. The bug I submitted is an unequivocal 7.8 CVSS. Which without knowing the voodoo behind P ratings (P1-P4), seems like would be a P2 at least. Instead I get a P3 and paid out at the lower end.

### Looking back on it, I’m betting this is probably an old bug bounty program trick to motivate researchers to dig deeper… because, it worked. I decided to take a closer look since I hadn’t even opened up the binary to see what it was doing – _**and I wanted to get that big payout**_.

## Let’s Get Crackin’

### I haven’t popped Okta.Coordinator.Service.exe into a disassembler yet, but I’m betting it’s a .NET application. My guess comes from its name and the fact that there’s an Okta.Coordinator.Service.exe.config file right there with it, which you usually see with .NET applications.

![](https://www.securifera.com/wp-content/uploads/2024/04/okta_files.png)

### When I open up the executable in JetBrains dotPeek, I can confirm it is indeed a .NET application. The binary appears to be a service wrapper. It handles the service related functionality: install, uninstall, start, stop, etc. It references a Okta.AutoUpdate.Executor class that just so happens to have a matching DLL in the same directory.

![](https://www.securifera.com/wp-content/uploads/2024/04/dot_peek.png)

### Moving on to the DLL in dotPeek, I found the code used by the service. The first thing I noticed was it sets up a NamedPipe server, which listens for commands to update the Okta Verify software. This is a common design paradigm in Windows for enabling low-privileged applications to communicate with a high-privileged service to perform updates, as these often require elevated privileges. It’s a complex mechanism that’s tricky to do right, and often a good place for finding bugs. I was able to confirm the existence of the named-pipe server with a little Powershell.

![](https://www.securifera.com/wp-content/uploads/2024/04/np.jpg)

### Next, I investigated how to initiate an update and what aspects of this process could be manipulated by an attacker. The handler for the named pipe processes a straightforward JSON message that includes several fields, some checked against expected values. The primary field of interest is the update URL. If the input data passes validation, the software will attempt to fetch details from the specified URL about the most recent update package available. As shown below, the URL (sub)domain is verified against a whitelist before proceeding. For now, I’ll avoid trying to meet/bypass this requirement and simply add an entry in the hosts file on my test machine.

![](https://www.securifera.com/wp-content/uploads/2024/04/validate.jpg)

![](https://www.securifera.com/wp-content/uploads/2024/04/trusted_domains.jpg)

### Typically at this stage, I’d code up a proof of concept (POC) to send a JSON message to the named pipe and check if the software connected to a web server I control. But since I haven’t spotted any potential vulnerabilities yet, I skipped that step and moved on.

### From here I took a look at the code responsible for processing the JSON message retrieved from the attacker controlled update server. The application is expecting a message that contains metadata about an update package including versioning and an array of file metadata objects. These objects contain several pertinent fields such the download URL, size, hash, type, and command line arguments. The provided download URL is validated with the same domain checking algorithm as before. If the check passes, the software downloads the file and writes it to disk. _**This is where things get interesting**_. The code parses the download URL from the received metadata and constructs the file path by calling the **Path.Combine** function.

![](https://www.securifera.com/wp-content/uploads/2024/04/path_combine_arb_file_write.png)

### Several factors are converging here to create a serious vulnerability. The most obvious is the use of the **Path.Combine** function with user supplied data. I went into depth about this issue in a previous blog post [here](https://www.securifera.com/blog/2023/03/06/attacking-net-web-services/). The TLDR is if a full path is provided as the second argument to this function, the first argument that typically specifies the parent folder, is _**ignored**_. The next issue is how the filename is parsed. The code splits the file location URL by forward slash and takes the last element as the filename. The problem (solution) is a full Windows path can be inserted here using back slashes and it’s still a valid URL. Since the service is running as SYSTEM, we have permissions to right anywhere. If we put all this together our payload looks something like the script below.

Copy to Clipboard

Syntax Highlightersha256_hash = hashlib.sha256() sha256_hash.update("AAAAA") lib_hash = sha256_hash.hexdigest() payload_name = "test.txt" class CustomRequestHandler(http.server.BaseHTTPRequestHandler): def do_GET(self): if self.path.startswith('/api'): # Handle GET requests here json_data = { "version": "5.0.0", "files": [ { "href": "https://test.okta.com/C:\\\%s" % payload_name, "size": len(payload), "hashValue": "abcd1234", "type": "Document", "fileHashes": { "SHA256": lib_hash }, "commandArgs": "", "requiresElevatedInstall": True },

### Now that I have a potential bug to test out, I craft the POC for the named pipe client to trigger the update. Luckily, this code already exists in the .NET DLL for me to repurpose. With my web server code also in place I send the request to test out the file write. As I had hoped, the file write succeeds!

![](https://www.securifera.com/wp-content/uploads/2024/04/test.jpg)

## Cool, but what about impact!

### I have the ability to write arbitrary files as SYSTEM on Windows. How can I leverage this to achieve on-demand remote code execution? The first thing that comes to mind is some form of [DLL hijacking](https://www.crowdstrike.com/blog/4-ways-adversaries-hijack-dlls/). I’ve used phantom DLL hijacking in the past but this is more appropriate for red team operations where time constraints aren’t really an issue. What I really need is the ability to force execution shortly after the file write.

### 

### Since the whole purpose behind this service is to install an update, can I just use it to execute my code? I reviewed the code after the file write to see what it takes to execute the downloaded update package. It appears the file type field in the file object metadata is used to indicate which file to execute. If the EXE or MSI file type is set, the application will attempt to validate the file signature before executing it, along with any supplied arguments. The process launcher executes the binary with UseShellExecute set to false so no possibility of command injection.

### 

![](https://www.securifera.com/wp-content/uploads/2024/04/installer_validate-1.png)

### My original thought was to deliver a legitimate Okta Verify package since this would pass the signature check. I could then use ProcMon to identify a DLL hijack in the install package. Privileged DLL hijacks occur in almost all services because the assumption is you already require the permissions to write to a privileged location. Ironically though, I found the service binary actually contained a DLL hijack just prior to the signature verification to load the necessary cryptographic libraries. If I write a DLL to **C:\Program Files (x86)\Okta\UpdateService\wintrust.dll** , it will get loaded just prior to signature verification.

### 

![](https://www.securifera.com/wp-content/uploads/2024/04/relative_DLL_import-1.png)

### Great, so now I have a way to execute arbitrary code from an unprivileged user to SYSTEM. _**“Guessing”**_ that this probably won’t meet the bar of P1 or P2, I start thinking of how to upgrade this to remote code execution. If RCE doesn’t get a P1 then what does? The interesting thing about named pipes is that they are often remotely accessible. It all depends on what permissions are set. Looking at the code below, it sets full control to the “BUILTIN\Users” group.

![](https://www.securifera.com/wp-content/uploads/2024/04/perms.jpg)

### Testing from a remote system in my network confirms that I get permissioned denied when I try to connect to the named pipe. After a couple of days I had an idea. If a Windows system is part of a Active Directory domain, does the BUILTIN/Users group permissions automatically get converted to the “Domain Users” group in a domain? This would mean any user in an AD domain could remotely execute code on any system that has Okta Verify installed. Moreover, considering that this software is aimed at large corporate enterprises, it would likely be included in the standard build and deployed broadly. So not explicitly “Domain Admin” but a good chance of it. I had to find out, so I stood up a test AD network in AWS and the following video shows what happened.

## Almost done

### Well that seems like a big deal right? Maybe get a P1 (and 70k…)? I’m guessing the **_small detail_** about not having an Okta subdomain to download from may keep it from landing a P1. Having worked at big tech companies, I know that subdomain takeover reports are common. However, without having a subdomain takeover, it’s likely the bug’s significance will be minimized. I decided to dedicate some time to searching for one to complete the exploit chain. After going through the standard bug bounty subdomain takeover tools, I came up with only one viable candidate: oktahelpspot.okta.com. It pointed to an IP with no open ports, managed by a small VPS provider named Arcustech.

### After signing up for an account and some very innocent social engineering, I got the following response. And then a second email from the first person’s manager. Oh well, so much for that.

![](https://www.securifera.com/wp-content/uploads/2024/04/email11.jpg)

![](https://www.securifera.com/wp-content/uploads/2024/04/email2.jpg)

### The next thing that came to mind was leveraging a custom Okta client subdomain. Whenever a new client registers with Okta, they receive a personalized Okta subdomain to manage their identity providers, e.g. trial-XXXXXXX.customdomains.okta.com. I found a way to set custom routes in the web management application that would redirect traffic from your custom domain to a user defined URL. Unfortunately, this redirect was implemented in Javascript, rather than through a conventional 302 or 301 HTTP redirect. Consequently, the .NET HTTP client that the Okta Verify update service uses did not execute the Javascript and therefore did not follow the redirect as a browser would.

## Reporting

### At this point, I decided it was time to report my findings to Okta. Namely, because they were offering a bonus at the time for what appeared to be Okta Verify, which I think they might have either forgotten or included without mentioning. Secondly, I didn’t want to risk someone else beating me to it. I am happy to report they accepted the report and awarded me a generous bounty of $13,337 as a P2. It wasn’t quite $70k, or a P1, but it’s nothing to sneeze at. I want to thank Okta for the bounty and quick resolution. They also kindly gave me permission to write this blog post and followed through with issuing CVE-2024-0980 along with an [advisory](https://trust.okta.com/security-advisories/okta-verify-windows-auto-update-arbitrary-code-execution-cve-2024-0980/).

### One last note, if anyone reading this identifies a way to bypass the subdomain validation check I would be very interested. I attempted most of the common URL parsing confusion techniques as well as various encoding tricks all for naught. Drop me a line at [@rwincey on X](https://twitter.com/rwincey)

By [b0yd](https://www.securifera.com/blog/author/b0yd/)|2024-05-02T17:43:12+00:00May 2nd, 2024|[BUG BOUNTY](https://www.securifera.com/blog/category/bug-bounty/), [EXPLOITS](https://www.securifera.com/blog/category/exploits/)|[0 Comments](https://www.securifera.com/blog/2024/05/02/okta-verify-for-windows-remote-code-execution-cve-2024-0980/#respond)

#### Share This Story, Choose Your Platform!

[Facebook](https://www.facebook.com/sharer.php?u=https%3A%2F%2Fwww.securifera.com%2Fblog%2F2024%2F05%2F02%2Fokta-verify-for-windows-remote-code-execution-cve-2024-0980%2F&t=Okta%20Verify%20for%20Windows%20Remote%20Code%20Execution%20%E2%80%93%20CVE-2024-0980 "Facebook")[X](https://x.com/intent/post?url=https%3A%2F%2Fwww.securifera.com%2Fblog%2F2024%2F05%2F02%2Fokta-verify-for-windows-remote-code-execution-cve-2024-0980%2F&text=Okta%20Verify%20for%20Windows%20Remote%20Code%20Execution%20%E2%80%93%20CVE-2024-0980 "X")[Reddit](https://reddit.com/submit?url=https://www.securifera.com/blog/2024/05/02/okta-verify-for-windows-remote-code-execution-cve-2024-0980/&title=Okta%20Verify%20for%20Windows%20Remote%20Code%20Execution%20%E2%80%93%20CVE-2024-0980 "Reddit")[LinkedIn](https://www.linkedin.com/shareArticle?mini=true&url=https%3A%2F%2Fwww.securifera.com%2Fblog%2F2024%2F05%2F02%2Fokta-verify-for-windows-remote-code-execution-cve-2024-0980%2F&title=Okta%20Verify%20for%20Windows%20Remote%20Code%20Execution%20%E2%80%93%20CVE-2024-0980&summary=This%20article%20is%20in%20no%20way%20affiliated%2C%20sponsored%2C%20or%20endorsed%20with%2Fby%20Okta%2C%20Inc.%20All%20graphics%20are%20being%20displayed%20under%20fair%20use%20for%20the%20purposes%20of%20this%20article.%20%20%0D%0A%0D%0APoppin%20shells%20with%20Okta%20Verify%20on%20Windows%20%0D%0AThese%20days%20I%20rarely%20have%20an%20opportunity%20to%20do "LinkedIn")[Tumblr](https://www.tumblr.com/share/link?url=https%3A%2F%2Fwww.securifera.com%2Fblog%2F2024%2F05%2F02%2Fokta-verify-for-windows-remote-code-execution-cve-2024-0980%2F&name=Okta%20Verify%20for%20Windows%20Remote%20Code%20Execution%20%E2%80%93%20CVE-2024-0980&description=This%20article%20is%20in%20no%20way%20affiliated%2C%20sponsored%2C%20or%20endorsed%20with%2Fby%20Okta%2C%20Inc.%20All%20graphics%20are%20being%20displayed%20under%20fair%20use%20for%20the%20purposes%20of%20this%20article.%20%20%0D%0A%0D%0APoppin%20shells%20with%20Okta%20Verify%20on%20Windows%20%0D%0AThese%20days%20I%20rarely%20have%20an%20opportunity%20to%20do%20bug%20hunting.%20Fortunately%2C%20over%20the "Tumblr")[Pinterest](https://pinterest.com/pin/create/button/?url=https%3A%2F%2Fwww.securifera.com%2Fblog%2F2024%2F05%2F02%2Fokta-verify-for-windows-remote-code-execution-cve-2024-0980%2F&description=This%20article%20is%20in%20no%20way%20affiliated%2C%20sponsored%2C%20or%20endorsed%20with%2Fby%20Okta%2C%20Inc.%20All%20graphics%20are%20being%20displayed%20under%20fair%20use%20for%20the%20purposes%20of%20this%20article.%20%20%0D%0A%0D%0APoppin%20shells%20with%20Okta%20Verify%20on%20Windows%20%0D%0AThese%20days%20I%20rarely%20have%20an%20opportunity%20to%20do%20bug%20hunting.%20Fortunately%2C%20over%20the&media=https%3A%2F%2Fwww.securifera.com%2Fwp-content%2Fuploads%2F2024%2F04%2Fokta_blog_small.jpg "Pinterest")[Vk](https://vk.com/share.php?url=https%3A%2F%2Fwww.securifera.com%2Fblog%2F2024%2F05%2F02%2Fokta-verify-for-windows-remote-code-execution-cve-2024-0980%2F&title=Okta%20Verify%20for%20Windows%20Remote%20Code%20Execution%20%E2%80%93%20CVE-2024-0980&description=This%20article%20is%20in%20no%20way%20affiliated%2C%20sponsored%2C%20or%20endorsed%20with%2Fby%20Okta%2C%20Inc.%20All%20graphics%20are%20being%20displayed%20under%20fair%20use%20for%20the%20purposes%20of%20this%20article.%20%20%0D%0A%0D%0APoppin%20shells%20with%20Okta%20Verify%20on%20Windows%20%0D%0AThese%20days%20I%20rarely%20have%20an%20opportunity%20to%20do%20bug%20hunting.%20Fortunately%2C%20over%20the "Vk")[Email](mailto:?body=https://www.securifera.com/blog/2024/05/02/okta-verify-for-windows-remote-code-execution-cve-2024-0980/&subject=Okta%20Verify%20for%20Windows%20Remote%20Code%20Execution%20%E2%80%93%20CVE-2024-0980 "Email")
