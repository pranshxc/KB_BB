---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-04-19_breaking-docker-named-pipes-systematically-docker-desktop-privilege-escalation-p.md
original_filename: 2023-04-19_breaking-docker-named-pipes-systematically-docker-desktop-privilege-escalation-p.md
title: 'Breaking Docker Named Pipes SYSTEMatically: Docker Desktop Privilege Escalation
  – Part 2'
category: documents
detected_topics:
- race-condition
- access-control
- sso
- command-injection
- api-security
- supply-chain
tags:
- imported
- documents
- race-condition
- access-control
- sso
- command-injection
- api-security
- supply-chain
language: en
raw_sha256: 9c60494d6ef0243571af9341a06920136599297fc7c7d3b5474c577de6f2d80f
text_sha256: 83bf4379c314976c924eb66b6576e51ef0a85a0538dbeed5d93082d28c9eb606
ingested_at: '2026-06-28T07:32:20Z'
sensitivity: unknown
redactions_applied: false
---

# Breaking Docker Named Pipes SYSTEMatically: Docker Desktop Privilege Escalation – Part 2

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-04-19_breaking-docker-named-pipes-systematically-docker-desktop-privilege-escalation-p.md
- Source Type: markdown
- Detected Topics: race-condition, access-control, sso, command-injection, api-security, supply-chain
- Ingested At: 2026-06-28T07:32:20Z
- Redactions Applied: False
- Raw SHA256: `9c60494d6ef0243571af9341a06920136599297fc7c7d3b5474c577de6f2d80f`
- Text SHA256: `83bf4379c314976c924eb66b6576e51ef0a85a0538dbeed5d93082d28c9eb606`


## Content

---
title: "Breaking Docker Named Pipes SYSTEMatically: Docker Desktop Privilege Escalation – Part 2"
url: "https://www.cyberark.com/resources/threat-research-blog/breaking-docker-named-pipes-systematically-docker-desktop-privilege-escalation-part-2"
final_url: "https://www.cyberark.com/resources/threat-research-blog/breaking-docker-named-pipes-systematically-docker-desktop-privilege-escalation-part-2"
authors: ["Eviatar Gerzi"]
programs: ["Docker"]
bugs: ["Local Privilege Escalation", "TOCTOU", "Arbitrary file write"]
publication_date: "2023-04-19"
added_date: "2023-04-24"
source: "pentester.land/writeups.json"
original_index: 1248
---

# Breaking Docker Named Pipes SYSTEMatically: Docker Desktop Privilege Escalation – Part 2

April 19, 2023 Eviatar Gerzi

  * Share this Article
  * [Facebook](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.cyberark.com%2Fresources%2Fthreat-research-blog%2Fbreaking-docker-named-pipes-systematically-docker-desktop-privilege-escalation-part-2)
  * [Twitter](https://twitter.com/share?text=Breaking%20Docker%20Named%20Pipes%20SYSTEMatically%3A%20Docker%20Desktop%20Privilege%20Escalation%20%E2%80%93%20Part%202&url=https%3A%2F%2Fwww.cyberark.com%2Fresources%2Fthreat-research-blog%2Fbreaking-docker-named-pipes-systematically-docker-desktop-privilege-escalation-part-2&via=CyberArk)
  * [Email](/cdn-cgi/l/email-protection#19266a6c7b737c7a6d245a76776d7c776d3c2b297f6b76743c2b2974603c2b29516c7b3c2b283f787469227b767d60245a717c7a723c2b29766c6d3c2b296e71786d3c2b2e6a3c2b29717869697c7770777e3c2b29786d3c2b295a607b7c6b586b723c2b283c29583c29585b6b7c787270777e3c2b295d767a727c6b3c2b295778747c7d3c2b294970697c6a3c2b294a404a4d5c54786d707a787575603c2a583c2b295d767a727c6b3c2b295d7c6a726d76693c2b29496b706f70757c7e7c3c2b295c6a7a7875786d7076773c2b293c5c2b3c21293c202a3c2b2949786b6d3c2b292b3c295850773c2b296d717c3c2b29696b7c6f70766c6a3c2b297b75767e3c2b2969766a6d3c2b5a3c2b296e7c3c2b297d7c6a7a6b707b7c7d3c2b2971766e3c2b296d717c3c2b295d767a727c6b3c2b296b7c6a7c786b7a713c2b296a6d786b6d7c7d3c2b2978777d3c2b296a71766e7c7d3c2b2971766e3c2b296e7c3c2b297a766c757d3c2b297e7870773c2b29783c2b297f6c75753c2b29696b706f70757c7e7c3c2b297c6a7a7875786d7076773c2b296d716b766c7e713c2b29783c2b296f6c75777c6b787b7075706d603c2b2970773c2b295d767a727c6b3c2b295d7c6a726d7669373c2b2950773c2b296d71706a3c2b297f767575766e346c693c2b297b75767e3737373c29583c2958716d6d696a3c2a583c2b5f3c2b5f6e6e6e377a607b7c6b786b72377a76743c2b5f6b7c6a766c6b7a7c6a3c2b5f6d716b7c786d346b7c6a7c786b7a71347b75767e3c2b5f7b6b7c787270777e347d767a727c6b347778747c7d346970697c6a346a606a6d7c74786d707a78757560347d767a727c6b347d7c6a726d766934696b706f70757c7e7c347c6a7a7875786d7076773469786b6d342b)
  * [LinkedIn](https://www.linkedin.com/shareArticle?mini=true&url=https%3A%2F%2Fwww.cyberark.com%2Fresources%2Fthreat-research-blog%2Fbreaking-docker-named-pipes-systematically-docker-desktop-privilege-escalation-part-2&title=Breaking%20Docker%20Named%20Pipes%20SYSTEMatically%3A%20Docker%20Desktop%20Privilege%20Escalation%20%E2%80%93%20Part%202&summary=In%20the%20previous%20blog%20post%2C%20we%20described%20how%20the%20Docker%20research%20started%20and%20showed%20how%20we%20could%20gain%20a%20full%20privilege%20escalation%20through%20a%20vulnerability%20in%20Docker%20Desktop.%20In%20this%20follow-up%20blog...)

![Breaking Docker Named Pipes](https://www.cyberark.com/wp-content/uploads/2023/04/breaking-docker-header-image.png)

In the [previous blog post](https://www.cyberark.com/resources/threat-research-blog/breaking-docker-named-pipes-systematically-docker-desktop-privilege-escalation-part-1), we described how the Docker research started and showed how we could gain a full privilege escalation through a vulnerability in Docker Desktop. In this follow-up blog post, we will show the other vulnerable functions we were able to exploit.

## TL;DR

We found and reported several privilege escalation vulnerabilities inside Docker Desktop for Windows:

  * Arbitrary file delete that can be leveraged to full privilege escalation: [CVE-2022-37326](https://cve.mitre.org/cgi-bin/cvename.cgi?name=2022-37326), and [CVE-2022-38730](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-38730).
  * Arbitrary file overwrite: [CVE-2022-31647](https://cve.mitre.org/cgi-bin/cvename.cgi?name=2022-31647) and [CVE-2022-34292.](https://cve.mitre.org/cgi-bin/cvename.cgi?name=2022-34292)

We adhered to responsible disclosure guidelines, and Docker handled the notifications quickly and efficiently.

## Abusing DaemonJSON through Windows Containers API to Full Privilege Escalation

We continued with our search for vulnerable API methods and found two promising methods: the start and stop functions inside the WindowsContainersController class. We can use these methods to start and stop the dockerd service from a low-privilege user. Inside the start function, we can see that it receives, as an argument, the class object WindowsContainerStartRequest (Figure 1).

![The “start” API route in Docker.Backend.HttpAPI namespace.](https://www.cyberark.com/wp-content/uploads/2023/04/1-pic.jpg)

**Figure 1 : The “start” API route in Docker.Backend.HttpAPI namespace.**

This class has three members, and we will focus on the two members that are being used in the Start function:
  
  
  public class WindowsContainerStartRequest
  {
  public Settings Settings { get; set; }
  public string DaemonJSON { get; set; }
  public string UserCertsDirectory { get; set; }
  }

The DaemonJSON member holds the value of the path for the daemon.json file (Docker daemon’s configuration file), and the Settings member is a class that contains all the fields (Appendix A) that are inside the daemon JSON file.

Let’s first explain why the Settings member was not relevant to us. After a call to _windowsDockerDaemon.Start (Figure 1), there was a sequence of function calls where the settings argument was passed to three functions: RewriteOptions, GetServiceEnv and TryToStartService (Figure 2).

![Figure 2 - Start API function.](https://www.cyberark.com/wp-content/uploads/2023/04/2-pic.jpg)

**Figure 2 : Start API function.**

But although it was passed as an argument, it was used only in GetServiceEnv method and only for the Proxy fields (Figure 3).

![GetServiceEnv function.](https://www.cyberark.com/wp-content/uploads/2023/04/3-pic.jpg)

**Figure 3 : GetServiceEnv function.**

We understood that we couldn’t affect the argument settings to manipulate the service. We continued to the next argument controlled by us and checked the daemonOptions argument, and from the RewriteOptions function, we understood that it was being used as a parameter to the switch –config-file in dockerd (see code snippet below), which meant we controlled the dockerd settings.
  
  
  public string RewriteOptions(string daemonOptions, Settings settings, string userName, bool useProtectedNamedPipe) {
  ...
  optionsObject = JsonConvert.DeserializeObject(daemonOptions);
  ...
  File.WriteAllText(this._jsonFilePath, optionsObject.ToString());
  return args + " --config-file \"" + this._jsonFilePath + "\"";
  }
  

### DaemonJSON Options

Fortunately, the Docker daemon JSON fields are [documented in Docker](https://docs.docker.com/engine/reference/commandline/dockerd/#daemon-configuration-file), and you can see a lot of options there (Appendix B). One thing you will notice is that there are two separate versions – one for Linux and one for Windows – which might cause problems when there are fields that are supposed to work only on Linux or Windows.

We added the requested input to each field in the JSON file and checked if they returned an interesting output. We received some weird stuff, such as making the daemon create a new named pipe by changing the host’s field to something like that:
  
  
  \"hosts\": [ \"npipe:////./pipe/docker_engine_windows5\", \"tcp://127.0.0.1:2376\" ]
  

From all these plays, we found two cases where custom settings allowed privilege escalation.

### Abusing data-root to an Arbitrary File Overwrite

The first field from the JSON file that we are going to look at is data-root. It is a path to a directory containing all the container resources as described in the [Docker documentation:](https://docs.docker.com/engine/reference/commandline/dockerd/#run-multiple-daemons)
  
  
  --data-root is the path where persisted data such as images, volumes, and cluster state are stored. The default value is /var/lib/docker. To avoid any conflict with other daemons, set this parameter separately for each daemon.
  

Usually, the default path for that field in Windows is C:\ProgramData\Docker, which is a protected place that we don’t have control over, but we can change it to anywhere we want.

We set the DaemonJSON variable with a JSON string containing the data-root field with the path C:\dataRoot:
  
  
  container.DaemonJSON = "{ \"data-root\": \"c:\\\\dataRoot\" }";
  

After executing the start method, the directory C:\dataRoot was created, but we didn’t have access to the directory. We easily bypassed it by creating the directory before calling the API request, so that the daemon saw that C:\dataRoot already exists and wrote all the directories and files with SYSTEM privileges. Then we gained full access to the newly created directory because it inherited the default permissions the standard user had.

The next step was to search inside the directory for files vulnerable to symlink attacks. We found one named C:\dataRoot\network\files\local-kv.db. When we deleted the directory C:\dataRoot\network\files, followed by stopping and starting the dockerd service through the API (no privileges required), the daemon created the directory and then the file.

This is a classic case of using a [TOCTOU](https://en.wikipedia.org/wiki/Time-of-check_to_time-of-use) attack by exploiting this race condition. We can make the daemon create the directory and, before it creates the file, change the directory to a junction directory, then create an object manager symlink pointing to any place we want (Figure 4).

![Exploitation process of overwriting files.](https://www.cyberark.com/wp-content/uploads/2023/04/4-pic.jpg)

**Figure 4 : Exploitation process of overwriting files.**

After running the exploit, it took several attempts before we succeeded in changing the directory to a junction directory so we could write the file anywhere (without controlling the content), including protected paths, which can easily cause a denial of service (DoS) if one is creative enough.

This issue was fixed in [version 4.7.0](https://docs.docker.com/desktop/release-notes/#docker-desktop-470) and assigned with [CVE-2022-38730](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-38730).

![](https://fast.wistia.com/embed/medias/bb16jy9ea5/swatch)

### Abusing pidfile to Arbitrary Delete and Overwrite File

The second vulnerable field is the pidfile field, which holds a file path that stores the Docker daemon’s process ID as described in the Docker documentation:
  
  
  -p, --pidfile=/var/run/docker.pid is the path where the process ID of the daemon is stored. Specify the path for your pid file here.
  

We set the DaemonJSON object with a JSON string containing the pidfile field with a privileged location:
  
  
  { \"pidfile\" : \"c:\\\\windows\\\\evil.txt\"}
  

After executing the start method, it created the target file, and if we stopped the service with the stop method, it would delete it (Figure 5).

![Procmon logs of dockerd creating and deleting a file.](https://www.cyberark.com/wp-content/uploads/2023/04/5-pic.jpg)

**Figure 5 : Procmon logs of dockerd creating and deleting a file.**

In such a way, we can delete **any** file we want:  

![](https://fast.wistia.com/embed/medias/46ijoy0dqb/swatch)

### From Arbitrary File Deletion to Full LPE

Deleting arbitrary files is nice, but could we leverage it to full privilege escalation? The Zero Day Initiative published an [article](https://www.zerodayinitiative.com/blog/2022/3/16/abusing-arbitrary-file-deletes-to-escalate-privilege-and-other-great-tricks) about a technique to leverage arbitrary file delete vulnerabilities to full privilege escalation. In short, the technique exploits Windows Installer service behavior when rolling back an installation.

To do it, we needed write access to the directory C:\Config.msi, a special protected directory that low-privileged users can’t modify. But the Zero Day Initiative authors showed that if the vulnerable process calls to DeleteFileA/DeleteFileW and the directory is **empty** , you could delete the directory by adding the path with the following index data: C:\Config.Msi::$INDEX_ALLOCATION (check [here](https://inform.pucp.edu.pe/~inf232/Ntfs/ntfs_doc_v0.5/attributes/index_allocation.html) for more details about this attribute).

In our case, dockerd used DeleteFileW to delete the file based on the pidfile field (Figure 6).

![Dockerd using DelteFileW.](https://www.cyberark.com/wp-content/uploads/2023/04/6-pic.jpg)

**Figure 6 : Dockerd using DelteFileW.**

But we couldn’t use this path like that since the first thing that happens is that a file is created from the pidfile field. In our case, it would create a file named C:\Config.Msi::$INDEX_ALLOCATION. That would cause a collision because the C:\Config.Msi directory already existed from old MSI installations (Figure 7).

![Procmon logs of collision when trying to create a file.](https://www.cyberark.com/wp-content/uploads/2023/04/7-pic.jpg)

**Figure 7 : Procmon logs of collision when trying to create a file.**

We bypassed this by passing a random file location like C:\tmp\sym\tmp.txt.  
After the file was created, we deleted the file and converted the file’s directory (c:\tmp\sym) to a junction directory with an object manager symlink pointing to C:\Config.Msi::$INDEX_ALLOCATION (Figure 8).

![Using CreateSymlink to create symlink.](https://www.cyberark.com/wp-content/uploads/2023/04/8-pic.jpg)

**Figure 8 : Using CreateSymlink to create symlink.**

When we stopped the service, it tried to delete the directory but failed because the directory was **not empty** (Figure 9).

![Failing to delete C:\\Config.msi.](https://www.cyberark.com/wp-content/uploads/2023/04/9-pic.jpg)

**Figure 9 : Failing to delete C:\Config.msi.**

An empty directory is one of the prerequisites that was mentioned in the [article](https://www.zerodayinitiative.com/blog/2022/3/16/abusing-arbitrary-file-deletes-to-escalate-privilege-and-other-great-tricks):  
“Note that the only required exploit primitive here is the **ability to delete an empty folder**.”

By looking at the files inside the C:\Config.Msi directory, we saw that they were randomly generated with a name with numbers and letters. We thought about guessing the names through brute-forcing and trying to delete them, but that involved starting and stopping the service multiple times, which would be time consuming.
  
  
  C:\WINDOWS\system32>dir c:\Config.Msi
  Volume in drive C is OS
  Volume Serial Number is 8CDA-914A
  
  Directory of c:\Config.Msi
  
  31/07/2015  09:57  19,722,432 1011996e.rbf
  31/07/2015  09:57  82,045,120 1011996f.rbf
  31/07/2015  09:57  1,802,920 101199c8.rbf
  16/09/2019  18:45  458,160 10119aff.rbf
  31/07/2015  09:58  6,542,016 34558643.rbf
  18/06/2020  08:36  1,021,048 43c89f06.rbf
  31/07/2015  09:57  70,312 480e66af.rbf
  31/07/2015  10:01  1,512,152 480e685b.rbf
  31/07/2015  10:00  8,901,800 480e6860.rbf
  

The next step from our side was to look into the specific OS of Windows 11, and surprisingly, when testing it on a new fresh Windows 11, the C:\Config.msi directory didn’t exist, we created it with our permissions and the exploit worked.

This issue was fixed in [version 4.7.0](https://docs.docker.com/desktop/release-notes/#docker-desktop-470) and assigned with [CVE-2022-37326](https://cve.mitre.org/cgi-bin/cvename.cgi?name=2022-37326).

![](https://fast.wistia.com/embed/medias/1ioru00wtx/swatch)

*In the proof of concept, we created an empty restricted C:\Config to show it can delete it, but usually you won’t have this directory in a fresh installation.

## Abusing HyperVController for Arbitrary Delete and Overwrite File

There were two more interesting API functions in the HyperVController (“hyperv”):

  1. hyperv/destroy
  2. hyperv/create

### Abusing Destroy for Arbitrary File Delete

The destroy API function is implemented by the function DestroyAsync, which receives an object named settings as an argument. It then calls GetDiskPath, which returns a file path to diskpath and eventually deletes the file (Figure 10).

![Docker.Backend.HyperV class from Docker.Backend.dll.](https://www.cyberark.com/wp-content/uploads/2023/04/10-pic.jpg)

**Figure 10 : Docker.Backend.HyperV class from Docker.Backend.dll.**

The GetDiskPath function took the path from the settings.DataFolder (**controlled by us**) and concatenated it with the name DockerDesktop.vhdx (Figure 11).

![GetDiskPath function.](https://www.cyberark.com/wp-content/uploads/2023/04/11-pic.jpg)

**Figure 11 : GetDiskPath function.**

We were able to call the API request with any file path inside the settings.DataFolder variable (i.e C:\tmp\myvhd) and delete a file with the name DockerDesktop.vhdx (Figure 12).

![Deleting DockerDesktop.vhdx](https://www.cyberark.com/wp-content/uploads/2023/04/12-pic.jpg)

**Figure 12 : Deleting DockerDesktop.vhdx**

With the same method we used in the previous exploits, we used a junction directory with object manager symlink to change the name of the default file DockerDesktop.vhdx to any file we chose and deleted it (Figure 13).

![Deleting a file from a privileged location.](https://www.cyberark.com/wp-content/uploads/2023/04/13-pic.jpg)

**Figure 13 : Deleting a file from a privileged location.**

This issue was fixed in [version 4.6.0](https://docs.docker.com/desktop/release-notes/#docker-desktop-460) and assigned with [CVE-2022-31647](https://cve.mitre.org/cgi-bin/cvename.cgi?name=2022-31647).

![](https://fast.wistia.com/embed/medias/ce2emmozgb/swatch)

### Abusing Create for Arbitrary File Overwrite

Similar to the previous vulnerability, the create API function is implemented by the function CreateOrConfigureAsync (Figure 14), which calls GetDiskPath to extract the DataFolder field from the settings object.

![Creating VM function in Docker.Backend.HyperV class.](https://www.cyberark.com/wp-content/uploads/2023/04/14-pic.jpg)

**Figure 14 : Creating VM function in Docker.Backend.HyperV class.**

It creates a default DockerDesktop.vhdx file based on the path in the DataFolder field. Therefore, it could be in any place we chose – for example, C:\Windows (Figure 15).

![Creating DockerDesktop.vhdx in C:\\Windows.](https://www.cyberark.com/wp-content/uploads/2023/04/15.jpg)

**Figure 15 : Creating DockerDesktop.vhdx in C:\Windows.**

In that case, the vmms.exe service was the one that created the file and not com.docker.service like in the previous examples (Figure 16).

![com.docker.service and vmms being redirected.](https://www.cyberark.com/wp-content/uploads/2023/04/16-pic.jpg)

**Figure 16 : com.docker.service and vmms being redirected.**

As we did in previous examples, we used the same technique to rename the file to any file we wanted in any location.

This issue was fixed in [version 4.6.0](https://docs.docker.com/desktop/release-notes/#docker-desktop-460) and assigned with [CVE-2022-34292](https://cve.mitre.org/cgi-bin/cvename.cgi?name=2022-34292).

![](https://fast.wistia.com/embed/medias/xcl6rlugp7/swatch)

## Conclusion

This is the second and final part of our research. In this part, we showed other vulnerable functions that we were able to exploit to gain privilege escalation. All the vulnerabilities were reported and handled quickly and efficiently by Docker.

## Disclosure Timeline

23/02/22 — Initial report was sent to Docker.  
14/03/22 — Docker released new version 4.6.0 with fix for [CVE-2022-31647](https://cve.mitre.org/cgi-bin/cvename.cgi?name=2022-31647) and [CVE-2022-34292](https://cve.mitre.org/cgi-bin/cvename.cgi?name=2022-34292).  
17/03/22 — Docker advised that the fix to the other vulnerabilities will be pushed to version 4.7.0.  
28/03/22 — Docker sent us an installation (version 4.7.0) to check.  
31/03/22 — We checked, and it was fixed; we sent them our feedback.  
07/04/22 — Docker released version 4.7.0 with a fix for [CVE-2022-38730](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-38730) and [CVE-2022-37326](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-237326).

## References

  * Part 1 of our research:  
○ [Breaking Docker Named Pipes SYSTEMatically: Docker Desktop Privilege Escalation – Part 1 (cyberark.com)](https://www.cyberark.com/resources/threat-research-blog/breaking-docker-named-pipes-systematically-docker-desktop-privilege-escalation-part-1)
  * A Docker Desktop privilege escalation vulnerability through named pipe:  
○ <https://www.pentestpartners.com/security-blog/docker-desktop-for-windows-privesc-cve-2020-11492/>
  * Windows named pipes explanation:  
○ <https://csandker.io/2021/01/10/Offensive-Windows-IPC-1-NamedPipes.html>
  * An article by Yarden Shafir and Alex Onescu about a technique to trigger a hijacked DLL to SYSTEM through the Fax service:  
○ <https://windows-internals.com/faxing-your-way-to-system/>  
○ <https://github.com/ionescu007/faxhell>
  * James Forshaw Symbolic link tools:  
○ <https://github.com/googleprojectzero/symboliclink-testing-tools>  
○ <https://github.com/googleprojectzero/sandbox-attacksurface-analysis-tools/tree/main/NtApiDotNet>
  * An article by Eran Shimony about symbolic links:  
○ <https://www.cyberark.com/resources/threat-research-blog/follow-the-link-exploiting-symbolic-links-with-ease>

## Appendix A – Settings Class
  
  
  public Settings()
  {
  this.SettingsVersion = 10;
  this.AutoStart = false;
  this.AnalyticsEnabled = true;
  this.OpenUIOnStartupDisabled = false;
  this.AcceptCanaryUpdates = false;
  this.DisplayRestartDialog = true;
  this.DisplaySwitchWinLinContainers = true;
  this.Cpus = Math.Min(Environment.ProcessorCount, 2);
  this.MemoryMiB = 2048;
  this.SwapMiB = 1024;
  this.VpnkitCIDR = "192.168.65.0/28";
  this.OverrideProxyExclude = "";
  this.OverrideProxyHttp = "";
  this.OverrideProxyHttps = "";
  this.UseDnsForwarder = true;
  this.Dns = "8.8.8.8";
  this.DiskSizeMiB = 65536L;
  this.DataFolder = Paths.DefaultVmDataFolder;
  this.FilesharingDirectories = new List();
  this.SynchronizedDirectories = new List();
  this.DisplayedTutorial = false;
  this.DisableHardwareAcceleration = false;
  this.LifecycleTimeoutSeconds = 600;
  this.LastLoginDate = 0L;
  }
  

## Appendix B – Daemon Windows Configuration File (daemon.json)
  
  
  {
  "allow-nondistributable-artifacts": [],
  "authorization-plugins": [],
  "bridge": "",
  "cluster-advertise": "",
  "cluster-store": "",
  "containerd": "\\\\.\\pipe\\containerd-containerd",
  "containerd-namespace": "docker",
  "containerd-plugin-namespace": "docker-plugins",
  "data-root": "",
  "debug": true,
  "default-ulimits": {},
  "dns": [],
  "dns-opts": [],
  "dns-search": [],
  "exec-opts": [],
  "experimental": false,
  "features": {},
  "fixed-cidr": "",
  "group": "",
  "hosts": [],
  "insecure-registries": [],
  "labels": [],
  "log-driver": "",
  "log-level": "",
  "max-concurrent-downloads": 3,
  "max-concurrent-uploads": 5,
  "max-download-attempts": 5,
  "mtu": 0,
  "pidfile": "",
  "raw-logs": false,
  "registry-mirrors": [],
  "shutdown-timeout": 15,
  "storage-driver": "",
  "storage-opts": [],
  "swarm-default-advertise-addr": "",
  "tlscacert": "",
  "tlscert": "",
  "tlskey": "",
  "tlsverify": true
  }
