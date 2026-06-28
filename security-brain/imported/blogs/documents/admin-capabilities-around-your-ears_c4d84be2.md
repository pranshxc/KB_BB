---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-01-02_admin-capabilities-around-your-ears.md
original_filename: 2020-01-02_admin-capabilities-around-your-ears.md
title: Admin capabilities around your ears
category: documents
detected_topics:
- access-control
- command-injection
- api-security
- mobile-security
tags:
- imported
- documents
- access-control
- command-injection
- api-security
- mobile-security
language: en
raw_sha256: c4d84be2dc1171d8d8f6470fa6f892e4c5d3f9e6e567e776d134daaf899144a1
text_sha256: 36d5c0ce6d8417df157065044084b7a2d7eafd000c9b25fdae91edfc856e101e
ingested_at: '2026-06-28T07:32:01Z'
sensitivity: unknown
redactions_applied: false
---

# Admin capabilities around your ears

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-01-02_admin-capabilities-around-your-ears.md
- Source Type: markdown
- Detected Topics: access-control, command-injection, api-security, mobile-security
- Ingested At: 2026-06-28T07:32:01Z
- Redactions Applied: False
- Raw SHA256: `c4d84be2dc1171d8d8f6470fa6f892e4c5d3f9e6e567e776d134daaf899144a1`
- Text SHA256: `36d5c0ce6d8417df157065044084b7a2d7eafd000c9b25fdae91edfc856e101e`


## Content

---
title: "Admin capabilities around your ears"
page_title: "Admin capabilities around your ears – Personal Page of Markus Krell"
url: "https://markus-krell.de/admin-capabilities-around-your-ears/"
final_url: "https://markus-krell.de/admin-capabilities-around-your-ears/"
authors: ["Markus Krell (@MarkusKrell)"]
programs: ["Poly (Plantronics)"]
bugs: ["Local Privilege Escalation"]
publication_date: "2020-01-02"
added_date: "2022-10-24"
source: "pentester.land/writeups.json"
original_index: 4847
---

#  Admin capabilities around your ears 

[January 2, 2020](/admin-capabilities-around-your-ears/) /  [markus](/author/markus/ "Posts by markus")

Do you own a Plantronics headset? If you do, you are probably using Plantronics Hub on your system. This software can be used to configure the headset and complete firmware upgrades.

As I went through the documentation of Plantronics Hub I noticed something interesting:

“PLTHub.exe is the Plantronics Hub process that runs at start up  
providing all of the functionality expected from Plantronics Hub.  
PlantronicsUpdate.exe is also a process that runs at start up. This  
process allows Windows users without administrative permissions  
to upgrade Plantronics Hub.”

Which means that there is a privileged process that can be triggered from a non-administrator context. My curiosity was raised!

What I did next was to install the application in a version, which was not the latest one on a test system and launch [Process Monitor](https://docs.microsoft.com/en-us/sysinternals/downloads/procmon). Filters were applied to only list actions from the elevated and the user process. After that I choose to upgrade the application through the user GUI. The output of Procmon is shown below:

![](/wp-content/uploads/2021/03/procmon-update-1024x362.png)Procmon output while updating Plantronics Hub

As can be identified from the output the elevated process “SpokesUpdateService.exe” is continuously probing for a file called “MajorUpgrade.config” in “C:\ProgramData\Plantronics\Spokes3G\”. The user application “PLTHub.exe” creates this file, which means that any user is able to create the corresponding file. The elevated process immediately consumes the file and deletes it. The update process was finished shortly after. I reverted back to the old version and retriggered the update process, but this time I stopped the service “SpokesUpdateService.exe”.

Now I was able to view the contents of the “MajorUpgrade.config” file and the contents were:

`markus|advertise|C:\Users\Markus\AppData\Local\Temp\PlantronicsHub\sec0pdbgi8tl92mykzw1jnao3h6rv5fu4qx7\PlantronicsHubBootstrapper.exe`

So basically, the file consists of the following structure `<username>|advertise|<path to exe>`

I went ahead and modified the path to the executable file with the following path “C:\Windows\System32\cmd.exe”, restarted the update service and was immediately given an elevated command prompt.

The issue was reported to Poly and they handled it professionally. Their fix was to make sure that the update executable is signed with their certificate. I tried to bypass their new validation (for example with a downgrade attack) but failed.

Affected Version: Plantronics Hub for Windows prior to version 3.14

CVSS v3: 7.3 (AV:L/AC:L/PR:L/UI:R/S:U/C:H/I:H/A:H)

CVE-2019-15742: <https://support.polycom.com/content/dam/polycom-support/global/documentation/plantronics-hub-local-privilege-escalation-vulnerability.pdf>

Exploit-DB: <https://www.exploit-db.com/exploits/47845>

Exploit was ported to Metasploit by bcoles: <https://github.com/rapid7/metasploit-framework/blob/master/modules/exploits/windows/local/plantronics_hub_spokesupdateservice_privesc.rb>

[Uncategorized](/category/uncategorized/)

##### [Previous post Heketi – Container escape ](/heketi-container-escape/) ##### [Next post iTop – Template Injection inside customer Portal ](/itop-template-injection-inside-customer-portal/)
