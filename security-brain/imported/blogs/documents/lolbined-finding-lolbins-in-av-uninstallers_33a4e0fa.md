---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-05-17_lolbined-finding-lolbins-in-av-uninstallers.md
original_filename: 2023-05-17_lolbined-finding-lolbins-in-av-uninstallers.md
title: LOLBINed — Finding “LOLBINs” In AV Uninstallers
category: documents
detected_topics:
- api-security
- supply-chain
- access-control
- command-injection
- path-traversal
tags:
- imported
- documents
- api-security
- supply-chain
- access-control
- command-injection
- path-traversal
language: en
raw_sha256: 33a4e0fac45b71861924f972d8160807b5f2ea5c5e6aed1f6499b13f49affd61
text_sha256: 85b0794c8ac7189881fc24a4482b0f477cd05c2981986c5ae4b58c43fccbfc15
ingested_at: '2026-06-28T07:32:21Z'
sensitivity: unknown
redactions_applied: false
---

# LOLBINed — Finding “LOLBINs” In AV Uninstallers

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-05-17_lolbined-finding-lolbins-in-av-uninstallers.md
- Source Type: markdown
- Detected Topics: api-security, supply-chain, access-control, command-injection, path-traversal
- Ingested At: 2026-06-28T07:32:21Z
- Redactions Applied: False
- Raw SHA256: `33a4e0fac45b71861924f972d8160807b5f2ea5c5e6aed1f6499b13f49affd61`
- Text SHA256: `85b0794c8ac7189881fc24a4482b0f477cd05c2981986c5ae4b58c43fccbfc15`


## Content

---
title: "LOLBINed — Finding “LOLBINs” In AV Uninstallers"
url: "https://nasbench.medium.com/lolbined-finding-lolbins-in-av-uninstallers-bf29427d3cd8"
authors: ["Nasreddine Bencherchali (@nas_bench)"]
programs: ["Kaspersky", "F-Secure", "Trend Micro", "McAfee"]
bugs: ["Local Privilege Escalation"]
publication_date: "2023-05-17"
added_date: "2023-05-22"
source: "pentester.land/writeups.json"
original_index: 1145
scraped_via: "browseros"
---

# LOLBINed — Finding “LOLBINs” In AV Uninstallers

LOLBINed — Finding “LOLBINs” In AV Uninstallers
Nasreddine Bencherchali
Follow
8 min read
·
May 16, 2023

29

Press enter or click to view image in full size
Funny Picture

This blog was originally written in February 2022 and update through out the year as vendors responded

Introduction

U
sually when people think of LOLBINs they tend to think of built-in OS only binaries. But If we think of a typical enterprise system we find that there are additional software bundled with the OS which include third-party software.

These new additions then become “built-in” to the image and can be considered LOLBINs as well. One such software is the AntiVirus.

Whether be it the built-in MS defender or a third party one. Everyone has it installed in some form.

Last year I thought it’ll be fun to look into one aspect of these AV, their “uninstallers” and some of their tooling.

This blog post focuses on some of these uninstallers and how I was able to abuse them as LOLBINs

By the time you’re reading this, all of these “issues” have been reported and hopefully fixed by their respective vendors.

Methodology

In the course of this research for LOLBIN’s all I used was a healthy dose of “Following the Breadcrumbs” and some tools such as ProcessMonitor.

Kaspersky (Kavremover)

Note: This issue has been fixed https://support.kaspersky.com/vulnerability/list-of-advisories/12430#011122

Kaspersky offers an un-installation tool called “Kavremover” that can remove more than 30 Kaspersky products. I’ve detailed this finding in a separate blog published last year. Give it a read if you haven’t already.

LOLBINed — Using Kaspersky Endpoint Security “KES” Installer to Execute Arbitrary Commands
Here We Go Again

nasbench.medium.com

F-Secure/WithSecure (FsUninstallationTool)

Note: This issue has been reported and fixed by F-Secure with version 18.7.13 — [VersionHistory] and CVE-2021–44750

I’ve tweeted about this technique a last year, but I thought it’s worth documenting at least :)

F-Secure offers an uninstallation tool for supposedly “broken installations” of their products. This tool uses “Lua” scripts under the hood to remove the corresponding product.

Via the command line, we can specify which product to remove as shown via the help command.

Press enter or click to view image in full size
Help output

A little bit of debugging will reveal that the binary accepts another flag not shown here by the help command which is the “--script” flag. Using this we can trick the binary into loading our own custom LUA scripts.

We simply create a script directory and a Lua script with the name of one of the available products (for example “mdr”) and run the following command:

FsUninstallationTool.exe -s -p mdr --scripts [ScriptFolderLocation]

This will run our LUA script and we get arbitrary execution.

Press enter or click to view image in full size
FsUninstallationTool
Trend Micro (SupportTool)

Note: This issue has been reported last year and should be fixed in the latest version(s) of Trend Micro AV. A currently Unknown CVE has been assigned

Embed within Trend Micro AV (Maximum Security, Internet Security…) is a tool called “SupportTool” that is part of the “Trend Micro Diagnostic Toolkit”.

Using the “SupportTool” we can uninstall Trend Micro products. The tool uses a graphical interface and different prompts to make sure you want to uninstall your software.

The uninstallation process is done by executing among other things a couple of “.bat” files stored inside the directory. Looking at “Process Monitor” output we can see that these files are being called from a relative path to the execution.

Press enter or click to view image in full size

Knowing this we can simulate this file by creating one with a similar name. Now the only thing that’s left is to be able to run the “SupportTool” without a GUI interface.

Digging a little bit into the code we find that this tool can be run in without a GUI using a special flag named “/SILENTUNINST”.

Combining all of this knowledge we can now abuse this tool to run arbitrary commands from our batch script using the following syntax and placing a “ForceRemove.bat” or “AMSPForceRemove.bat” in the same location.

SupportTool.exe /SILENTUNINST="TME"
Process Tree after abuse

Another interesting thing I found is that the “SupportTool” also calls another process during its execution from a relative path. So if we put an executable file with the name “TMSToolEx.exe” in the same directory and executed the same command shown above, it’ll get called.

Note that the “SupportTool” binary is signed.

Signed Picture

Another thing to note is that binary is also available in the “Trend Micro Remnant File Remover Tool”.

Trend Micro (Setup.exe)

Note: Fix state is “Unknown” but “should” be fixed in theory :)

Trend Micro AV also offers an interesting “feature” similar to the one I talked about in my Kaspersky blog [Here] that offers the possibility to detect and remove “Incompatible” security software.

And similar to Kaspersky these detection's and remediation's are also based on a file. Namely “IncompatibilityAction.xml” and “IncompatibilityDetection.xml” which are located in the “Common” folder inside the decompressed installation folder.

Press enter or click to view image in full size
Incompatibility Detection for AVG 2015
Press enter or click to view image in full size
Incompatibility Action for AVG 2015

We can infer the logic behind this process by simply reading the XML.

Get Nasreddine Bencherchali’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

The next step is to simulate an AV via the registry. (Let’s take AVG 2015 as an example). We create the following key

HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall\AVG

And add the “UninstallString” with the value

C:\Windows\System32\notepad.exe

We then launch the “setup.exe” process as one would.

Press enter or click to view image in full size
TrendMicro Maximum Security

By pressing “OK” our payload stored inside the “UninstallString” will get executed as a child of the “setup.exe” process.

Press enter or click to view image in full size
TM MaxSec Process Tree
Trend Micro (dsa.com)

Note: This has been fixed in the Agent build 20.0.0.4959

The fix only included loading LUA scripts from outside of the installation directory. You can still load them from within if you have the permission.

Trend Micro claim This should be avoided by enabling the agent self-protection.

While not an uninstallers like the other. The executable “dsa.com” that’s of part of the TrendMicro Deep Security Agent was vulnerable to LUA script side loading and can be abused as a LOLBIN.

Similar to WithSecure FsUninstallationTool, we can create a quick Lua script for testing (lolbin.lua)

os.execute('calc')

We then put this in a ZIP file (lolbin.zip) and place it in any location (C:\users\test\downloads\lolbin.zip)

We then simply can levreage the dsa.com binary and pass our zip file with the following CLI flags

dsa.com -a lolbin -z C:\users\test\downloads\lolbin.zip

The dsa.com binary will actually unzip the file and read/execute the content of the Lua script :)

McAfee/Trellix — Consumer Product Removal tool (MCPR)

This issues has been fixed and assigned CVE-2022–1823 / CVE-2022–1824

Similar to the cases above, this binary uses “.ini” files to read its configuration and what needs to be deleted for which product. To be honest it contains a gold mine of information about a lot of McAfee products (Registry Keys, Services, Names, Folders…etc) and it’s definitely worth checking.

Anyways, to make things short basically, this utility will run another binary with the name “McClnUI.exe” that will in turn run “mccleanup.exe”. Which is the binary responsible for deleting the stuff.

The command line during the execution looks something like this

mccleanup.exe -p [NameOfService] -silent -uipipe McAfeeCleanupUIMessagePipe[RandomeNumner] -s -silent

The “NameOfService” in the command above is interesting to us because it’s read from the file “master.ini” which contains a reference to each product-specific “.ini” files.

master.ini

If you read the Kaspersky blog mentioned above then this will be very similar. What we’ll do is simulate a fake product and create our own “.ini” file.

By looking at other “.ini” files for inspiration we get this example to run our favorite POC tool “calc.exe”

[stop_mcupdate_service]
type=cmd
cmd=calc

With this and by re-running the command above we get a CALC popup.

Now let’s put all of this into simple steps.

We first download the MCPR tool and simply extract it using a tool like 7Z
We then navigate to the newly created folders and copy our “mccleanup.exe” to any location
We create a fake “master.ini” with the following content to simulate a product
[PRODUCTS]
Lolbin=lolbin.ini
Now we create the “lolbin.ini” file and for this, we just need a copy from an existing “.ini” for inspiration
[UNINSTALL]
10:64bit=uninstall_list_64_wss
[uninstall_list_64_wss]
malware
[malware]
type=cmd 
cmd=calc
We then finally execute the following command (Where “-p” is our product).
mccleanup.exe -p Lolbin -silent -uipipe anything -s -silent
And voila
Press enter or click to view image in full size
Calc Selfi

As a side note, it turns out that the “mccleanup.exe” binary was also vulnerable to an executable side-load. Since it had the “McClnUI” hardcoded in it. This means every time you call it, it’ll call a binary with the name “McClnUI”.

With this you can copy any binary and rename it to “McClnUI”, launch “mccleanup” and it’ll get executed as a child process.

Also, note that the “mccleanup.exe” binary is also signed

Signed “mccleanup”
McAfee/Trellix — McUICnt.EXE

Note: This issue has been reported and assigned CVE-2022–37025

This final one is also related to McAfee/Trellix. The “McUICnt” binary is bundled with “McAfee Security Scan Plus”

It allows any user to execute arbitrary commands from its context using a simple “.ini” file (C:\uninstaller.ini)

[CONFIG]
WIDTH = 0
HEIGHT = 0
HTMLRESDLL = .\McInstallerRes.dll
L10NDLL = .\McInstallerRes_LD.dll
PAGE_VISIBILITY_TIME = 0

[UIFLOW]
default = Uninstall.htm

[Install]  
ORDER = MSS

[MSS]  
LOCATION_TYPE = 1 
LOCATION =C:\Windows\System32
AGENT = cmd.exe

We can run the binary with the following CLI flags and we get a command prompt.

McUICnt.exe McInstallerStartup.dll config:..\..\..\..\..\..\uninstaller.ini mode:/l
Process Tree McUICnt
Conclusion

Thanks for reading and I hope you found the blog post interesting. This was just a taste of what’s out there in terms of LOLBINs from these third party AVs. I can assure you there are many more :) so happy hunting’ in advance.

If you wanna discuss this or related topics, you can find me on Twitter @nas_bench

Note: All of these “vulnerabilities”/”issues” were reported to their respective vendors at the start of the 2022 and enough time was given to create a fix :)
